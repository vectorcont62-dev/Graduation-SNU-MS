from __future__ import annotations

import argparse
import math
from pathlib import Path

import pypdfium2 as pdfium
from PIL import Image, ImageDraw


def render_pdf(pdf_path: Path, out_dir: Path, dpi: int) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    pdf = pdfium.PdfDocument(str(pdf_path))
    scale = dpi / 72.0
    paths: list[Path] = []
    for idx in range(len(pdf)):
        page = pdf[idx]
        bitmap = page.render(scale=scale, rotation=0)
        image = bitmap.to_pil().convert("RGB")
        target = out_dir / f"page-{idx + 1:03d}.png"
        image.save(target, optimize=True)
        paths.append(target)
        page.close()
    pdf.close()
    return paths


def make_contact_sheets(
    image_paths: list[Path],
    out_dir: Path,
    cols: int = 2,
    rows: int = 2,
    gap: int = 24,
    label_h: int = 36,
) -> None:
    sheet_dir = out_dir / "contact_sheets"
    sheet_dir.mkdir(parents=True, exist_ok=True)
    per_sheet = cols * rows
    for start in range(0, len(image_paths), per_sheet):
        subset = image_paths[start : start + per_sheet]
        opened = [Image.open(path).convert("RGB") for path in subset]
        cell_w = max(img.width for img in opened)
        cell_h = max(img.height for img in opened) + label_h
        sheet = Image.new(
            "RGB",
            (cols * cell_w + (cols + 1) * gap, rows * cell_h + (rows + 1) * gap),
            "white",
        )
        draw = ImageDraw.Draw(sheet)
        for local_idx, (path, img) in enumerate(zip(subset, opened)):
            row = local_idx // cols
            col = local_idx % cols
            x = gap + col * (cell_w + gap) + (cell_w - img.width) // 2
            y = gap + row * (cell_h + gap) + label_h
            draw.text((x, y - label_h + 7), path.stem, fill="black")
            sheet.paste(img, (x, y))
        end = start + len(subset)
        sheet.save(
            sheet_dir / f"pages-{start + 1:03d}-{end:03d}.png",
            optimize=True,
        )
        for img in opened:
            img.close()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("out_dir", type=Path)
    parser.add_argument("--dpi", type=int, default=120)
    args = parser.parse_args()
    paths = render_pdf(args.pdf.resolve(), args.out_dir.resolve(), args.dpi)
    make_contact_sheets(paths, args.out_dir.resolve())
    print(f"rendered_pages={len(paths)}")
    print(f"contact_sheets={math.ceil(len(paths) / 4)}")


if __name__ == "__main__":
    main()
