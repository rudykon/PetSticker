#!/usr/bin/env python3
"""Validate deterministic file requirements for a WeChat pet sticker album."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageSequence


@dataclass(frozen=True)
class AssetSpec:
    names: tuple[str, ...]
    size: tuple[int, int]
    transparent: bool | None
    warn_bytes: int


BASE_ASSETS = {
    "character_avatar": AssetSpec(("character_avatar.png",), (240, 240), True, 500_000),
    "detail_banner": AssetSpec(
        ("detail_banner.jpg", "detail_banner.jpeg", "detail_banner.png"),
        (750, 400), False, 500_000,
    ),
    "album_cover": AssetSpec(("album_cover.png",), (240, 240), True, 500_000),
    "chat_icon": AssetSpec(("chat_icon.png",), (50, 50), True, 100_000),
}

TIPPING_ASSETS = {
    "tipping_prompt": AssetSpec(
        ("tipping_prompt.jpg", "tipping_prompt.jpeg", "tipping_prompt.png", "tipping_prompt.gif"),
        (750, 560), None, 500_000,
    ),
    "tipping_thanks": AssetSpec(
        ("tipping_thanks.jpg", "tipping_thanks.jpeg", "tipping_thanks.png", "tipping_thanks.gif"),
        (750, 750), None, 500_000,
    ),
}


def has_alpha(image: Image.Image) -> bool:
    if image.mode in {"RGBA", "LA"}:
        return image.getchannel("A").getextrema()[0] < 255
    if image.mode == "P" and "transparency" in image.info:
        return image.convert("RGBA").getchannel("A").getextrema()[0] < 255
    return False


def check_image(path: Path, spec: AssetSpec, label: str,
                errors: list[str], warnings: list[str]) -> None:
    try:
        with Image.open(path) as image:
            image.load()
            if image.size != spec.size:
                errors.append(
                    f"{label}: {path.name} is {image.size[0]}x{image.size[1]}, "
                    f"expected {spec.size[0]}x{spec.size[1]}"
                )
            alpha = has_alpha(image)
            if spec.transparent is True and not alpha:
                errors.append(f"{label}: {path.name} does not contain real transparency")
            if spec.transparent is False and alpha:
                errors.append(f"{label}: {path.name} must be opaque")
    except Exception as exc:
        errors.append(f"{label}: cannot read {path.name}: {exc}")
        return
    size_bytes = path.stat().st_size
    if size_bytes > spec.warn_bytes:
        warnings.append(
            f"{label}: {path.name} is {size_bytes} bytes; platform may compress "
            f"above {spec.warn_bytes}"
        )


def find_asset(directory: Path, spec: AssetSpec) -> Path | None:
    return next((directory / name for name in spec.names if (directory / name).is_file()), None)


def check_gif_animation(
    path: Path,
    expected_frames: int | None,
    expected_loop_ms: int | None,
    expected_delays: list[int] | None,
    duration_tolerance_ms: int,
    require_infinite_loop: bool,
    require_transparency: bool,
    require_clear_edges: bool,
    errors: list[str],
) -> None:
    try:
        with Image.open(path) as image:
            frame_count = getattr(image, "n_frames", 1)
            if expected_frames is not None and frame_count != expected_frames:
                errors.append(
                    f"animation: {path.name} has {frame_count} frames, "
                    f"expected {expected_frames}"
                )

            loop = image.info.get("loop")
            if require_infinite_loop and loop != 0:
                errors.append(
                    f"animation: {path.name} loop={loop!r}; expected infinite loop (0)"
                )

            durations: list[int] = []
            transparent_frames = 0
            edge_frames: list[int] = []
            for index, frame in enumerate(ImageSequence.Iterator(image), start=1):
                if frame.size != (240, 240):
                    errors.append(
                        f"animation: {path.name} frame {index} is "
                        f"{frame.size[0]}x{frame.size[1]}, expected 240x240"
                    )
                durations.append(int(frame.info.get("duration", image.info.get("duration", 0))))
                rgba = frame.convert("RGBA")
                alpha = rgba.getchannel("A")
                if alpha.getextrema()[0] < 255:
                    transparent_frames += 1
                if require_clear_edges:
                    width, height = rgba.size
                    border = Image.new("L", (width * 2 + max(0, height - 2) * 2, 1), 0)
                    pieces = [
                        alpha.crop((0, 0, width, 1)),
                        alpha.crop((0, height - 1, width, height)),
                        alpha.crop((0, 1, 1, height - 1)).resize((max(0, height - 2), 1)),
                        alpha.crop((width - 1, 1, width, height - 1)).resize((max(0, height - 2), 1)),
                    ]
                    offset = 0
                    for piece in pieces:
                        border.paste(piece, (offset, 0))
                        offset += piece.width
                    if border.getbbox() is not None:
                        edge_frames.append(index)

            if require_transparency and transparent_frames != frame_count:
                errors.append(
                    f"animation: {path.name} has real transparency in "
                    f"{transparent_frames}/{frame_count} frames"
                )
            if edge_frames:
                errors.append(
                    f"animation: {path.name} has nontransparent canvas-edge pixels "
                    f"in frames {edge_frames}"
                )
            if expected_delays is not None and durations != expected_delays:
                errors.append(
                    f"animation: {path.name} frame delays {durations} do not match "
                    f"expected {expected_delays}"
                )
            total_ms = sum(durations)
            if (
                expected_loop_ms is not None
                and abs(total_ms - expected_loop_ms) > duration_tolerance_ms
            ):
                errors.append(
                    f"animation: {path.name} loop duration is {total_ms} ms, "
                    f"expected {expected_loop_ms}±{duration_tolerance_ms} ms"
                )
    except Exception as exc:
        errors.append(f"animation: cannot inspect {path.name}: {exc}")


def load_manifest(album: Path, errors: list[str]) -> dict | None:
    path = album / "manifest.json"
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"manifest.json is invalid: {exc}")
        return None
    if not isinstance(data, dict):
        errors.append("manifest.json root must be an object")
        return None
    return data


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("album", type=Path)
    parser.add_argument("--expected-stickers", type=int, default=24)
    parser.add_argument("--with-tipping", action="store_true")
    parser.add_argument(
        "--allow-gif-stickers",
        action="store_true",
        help="include GIF files when validating dynamic sticker sets",
    )
    parser.add_argument("--gif-frames", type=int, help="required frame count for every GIF sticker")
    parser.add_argument("--gif-loop-ms", type=int, help="required total loop duration in milliseconds")
    parser.add_argument(
        "--gif-frame-delays",
        help="required comma-separated per-frame delays in milliseconds",
    )
    parser.add_argument(
        "--gif-duration-tolerance-ms",
        type=int,
        default=20,
        help="allowed total-duration difference; default: 20 ms",
    )
    parser.add_argument("--require-infinite-loop", action="store_true")
    parser.add_argument("--require-transparent-gif", action="store_true")
    parser.add_argument("--require-clear-gif-edges", action="store_true")
    parser.add_argument(
        "--require-qa-docs",
        action="store_true",
        help="require non-empty manifest.json, character_bible.md, and qa_report.md",
    )
    parser.add_argument("--json", action="store_true", dest="json_output")
    args = parser.parse_args()

    expected_gif_delays: list[int] | None = None
    if args.gif_frame_delays:
        try:
            expected_gif_delays = [
                int(value.strip()) for value in args.gif_frame_delays.split(",")
                if value.strip()
            ]
        except ValueError as exc:
            parser.error(f"--gif-frame-delays must contain integers: {exc}")

    album = args.album.resolve()
    stickers_dir = album / "stickers"
    assets_dir = album / "assets"
    errors: list[str] = []
    warnings: list[str] = []

    if not stickers_dir.is_dir():
        errors.append(f"missing stickers directory: {stickers_dir}")
        stickers: list[Path] = []
    else:
        allowed_extensions = {".png", ".jpg", ".jpeg"}
        if args.allow_gif_stickers:
            allowed_extensions.add(".gif")
        stickers = sorted(
            p for p in stickers_dir.iterdir()
            if p.is_file() and p.suffix.lower() in allowed_extensions
        )
    if len(stickers) != args.expected_stickers:
        errors.append(f"sticker count is {len(stickers)}, expected {args.expected_stickers}")

    seen_numbers: set[int] = set()
    for path in stickers:
        match = re.match(r"^(\d{2})[_-]", path.name)
        if not match:
            warnings.append(f"sticker filename has no two-digit prefix: {path.name}")
        else:
            number = int(match.group(1))
            if number in seen_numbers:
                errors.append(f"duplicate sticker number: {number:02d}")
            seen_numbers.add(number)
        # PNG is the reliable default for transparent static stickers. JPG/JPEG
        # and GIF can be valid platform files, so validate dimensions without
        # falsely requiring transparency for those formats.
        sticker_spec = AssetSpec(
            ("",), (240, 240), True if path.suffix.lower() == ".png" else None, 500_000
        )
        check_image(path, sticker_spec, "sticker", errors, warnings)
        if path.suffix.lower() == ".gif":
            check_gif_animation(
                path,
                args.gif_frames,
                args.gif_loop_ms,
                expected_gif_delays,
                max(0, args.gif_duration_tolerance_ms),
                args.require_infinite_loop,
                args.require_transparent_gif,
                args.require_clear_gif_edges,
                errors,
            )

    expected_numbers = set(range(1, args.expected_stickers + 1))
    if seen_numbers and seen_numbers != expected_numbers:
        errors.append(
            "sticker numbering mismatch; "
            f"missing={sorted(expected_numbers-seen_numbers)}, "
            f"extra={sorted(seen_numbers-expected_numbers)}"
        )

    if not assets_dir.is_dir():
        errors.append(f"missing assets directory: {assets_dir}")
    else:
        specs = dict(BASE_ASSETS)
        if args.with_tipping:
            specs.update(TIPPING_ASSETS)
        for label, spec in specs.items():
            path = find_asset(assets_dir, spec)
            if path is None:
                errors.append(f"missing {label}; accepted names: {', '.join(spec.names)}")
            else:
                check_image(path, spec, label, errors, warnings)

    if args.require_qa_docs:
        for name in ("character_bible.md", "qa_report.md"):
            path = album / name
            if not path.is_file():
                errors.append(f"missing required QA document: {name}")
            elif not path.read_text(encoding="utf-8").strip():
                errors.append(f"required QA document is empty: {name}")

    manifest = load_manifest(album, errors)
    if manifest is None:
        message = "manifest.json not found; captions and ordering cannot be cross-checked"
        if args.require_qa_docs:
            errors.append(message)
        else:
            warnings.append(message)
    else:
        entries = manifest.get("stickers")
        if not isinstance(entries, list):
            errors.append("manifest stickers must be an array")
        else:
            files = [entry.get("file") for entry in entries if isinstance(entry, dict)]
            captions = [entry.get("caption") for entry in entries if isinstance(entry, dict)]
            if len(files) != args.expected_stickers:
                errors.append(
                    f"manifest sticker count is {len(files)}, expected {args.expected_stickers}"
                )
            actual = {p.name for p in stickers}
            declared = {name for name in files if isinstance(name, str)}
            if actual != declared:
                errors.append(
                    f"manifest/file mismatch; undeclared={sorted(actual-declared)}, "
                    f"missing={sorted(declared-actual)}"
                )
            duplicate_captions = sorted({
                caption for caption in captions
                if isinstance(caption, str) and captions.count(caption) > 1
            })
            if duplicate_captions:
                warnings.append(f"duplicate captions in manifest: {duplicate_captions}")

    result = {
        "album": str(album),
        "stickers_found": len(stickers),
        "errors": errors,
        "warnings": warnings,
        "status": "PASS" if not errors else "FAIL",
        "manual_review_required": True,
    }
    if args.json_output:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"[{result['status']}] {album}")
        print(f"stickers: {len(stickers)}/{args.expected_stickers}")
        for error in errors:
            print(f"ERROR: {error}")
        for warning in warnings:
            print(f"WARN: {warning}")
        print("MANUAL REVIEW REQUIRED: identity, anatomy, text pixels, fake transparency, semantics")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
