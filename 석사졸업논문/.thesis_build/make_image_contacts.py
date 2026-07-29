from __future__ import annotations

import argparse
import re
from pathlib import Path

from PIL import Image, ImageDraw


def natural_key(path: Path) -> int:
    match = re.search(r"(\d+)", path.stem)
    return int(match.group(1)) if match else 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--cols", type=int, default=2)
    parser.add_argument("--rows", type=int, default=2)
    args = parser.parse_args()

    paths = sorted(
        (
            p
            for p in args.input_dir.iterdir()
            if p.suffix.lower() in {".png", ".jpg", ".jpeg"}
        ),
        key=natural_key,
    )
    args.output_dir.mkdir(parents=True, exist_ok=True)
    per_sheet = args.cols * args.rows
    for start in range(0, len(paths), per_sheet):
        subset = paths[start : start + per_sheet]
        images = [Image.open(p).convert("RGB") for p in subset]
        width = max(img.width for img in images)
        height = max(img.height for img in images)
        gap = 20
        label = 32
        sheet = Image.new(
            "RGB",
            (
                args.cols * width + (args.cols + 1) * gap,
                args.rows * (height + label) + (args.rows + 1) * gap,
            ),
            "white",
        )
        draw = ImageDraw.Draw(sheet)
        for idx, (path, image) in enumerate(zip(subset, images)):
            row = idx // args.cols
            col = idx % args.cols
            x = gap + col * (width + gap)
            y = gap + row * (height + label)
            draw.text((x, y + 6), path.stem, fill="black")
            sheet.paste(image, (x, y + label))
        sheet.save(
            args.output_dir / f"slides-{start + 1:02d}-{start + len(subset):02d}.png",
            optimize=True,
        )
        for image in images:
            image.close()

    print(f"images={len(paths)}")
    print(f"sheets={(len(paths) + per_sheet - 1) // per_sheet}")


if __name__ == "__main__":
    main()
