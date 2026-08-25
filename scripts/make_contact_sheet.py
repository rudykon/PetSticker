#!/usr/bin/env python3
"""Build a numbered contact sheet for visual review of sticker images."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stickers", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--columns", type=int, default=6)
    parser.add_argument("--cell", type=int, default=260)
    args = parser.parse_args()

    files = sorted(
        p for p in args.stickers.iterdir()
        if p.is_file() and p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".gif"}
    )
    if not files:
        raise SystemExit("no sticker images found")

    columns = max(1, args.columns)
    cell = max(80, args.cell)
    label_h = max(24, cell // 10)
    rows = (len(files) + columns - 1) // columns
    canvas = Image.new("RGB", (columns * cell, rows * (cell + label_h)), "#D8D8D8")
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default()

    for index, path in enumerate(files):
        row, col = divmod(index, columns)
        x, y = col * cell, row * (cell + label_h)
        with Image.open(path) as source:
            if getattr(source, "n_frames", 1) > 1:
                source.seek(0)
            image = source.convert("RGBA")
            image.thumbnail((cell - 16, cell - 16), Image.Resampling.LANCZOS)
            px = x + (cell - image.width) // 2
            py = y + (cell - image.height) // 2
            canvas.paste(image, (px, py), image)
        label = f"{index + 1:02d}  {path.name}"
        draw.rectangle((x, y + cell, x + cell, y + cell + label_h), fill="#222222")
        draw.text((x + 6, y + cell + 6), label, fill="white", font=font)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(args.output)
    print(args.output.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
