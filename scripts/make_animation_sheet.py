#!/usr/bin/env python3
"""Build a row-per-sticker, frame-by-frame QA sheet for animated GIF stickers."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageSequence


def checkerboard(size: int, block: int = 10) -> Image.Image:
    image = Image.new("RGB", (size, size), "#F1F1F1")
    draw = ImageDraw.Draw(image)
    for y in range(0, size, block):
        for x in range(0, size, block):
            if (x // block + y // block) % 2:
                draw.rectangle((x, y, x + block - 1, y + block - 1), fill="#D0D0D0")
    return image


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stickers", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--cell", type=int, default=104)
    parser.add_argument("--label-width", type=int, default=72)
    parser.add_argument("--expected-frames", type=int)
    args = parser.parse_args()

    files = sorted(
        path for path in args.stickers.iterdir()
        if path.is_file() and path.suffix.lower() == ".gif"
    )
    if not files:
        raise SystemExit("no GIF stickers found")

    cell = max(48, args.cell)
    label_width = max(48, args.label_width)
    frame_sets: list[list[Image.Image]] = []
    max_frames = 0
    for path in files:
        with Image.open(path) as source:
            frames = [frame.convert("RGBA") for frame in ImageSequence.Iterator(source)]
        if args.expected_frames is not None and len(frames) != args.expected_frames:
            raise SystemExit(
                f"{path.name}: {len(frames)} frames; expected {args.expected_frames}"
            )
        frame_sets.append(frames)
        max_frames = max(max_frames, len(frames))

    canvas = Image.new(
        "RGB",
        (label_width + max_frames * cell, len(files) * cell),
        "#B8B8B8",
    )
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default()
    tile_background = checkerboard(cell)

    for row, (path, frames) in enumerate(zip(files, frame_sets)):
        top = row * cell
        draw.rectangle((0, top, label_width, top + cell), fill="#252525")
        number = path.name[:2] if path.name[:2].isdigit() else f"{row + 1:02d}"
        draw.text((10, top + 10), number, fill="white", font=font)
        draw.text((10, top + 28), f"{len(frames)}f", fill="#D8D8D8", font=font)
        for column, frame in enumerate(frames):
            tile = tile_background.copy()
            preview = frame.copy()
            preview.thumbnail((cell - 8, cell - 8), Image.Resampling.LANCZOS)
            tile.paste(
                preview,
                ((cell - preview.width) // 2, (cell - preview.height) // 2),
                preview,
            )
            left = label_width + column * cell
            canvas.paste(tile, (left, top))
            draw.text((left + 3, top + 3), str(column + 1), fill="#202020", font=font)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(args.output)
    print(args.output.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
