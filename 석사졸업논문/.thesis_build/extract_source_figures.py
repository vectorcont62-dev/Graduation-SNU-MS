from __future__ import annotations

from pathlib import Path

import pypdfium2 as pdfium
from PIL import Image, ImageChops


ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / ".thesis_build" / "figures"
OUT.mkdir(parents=True, exist_ok=True)


def render_page(pdf_path: Path, page_number: int, dpi: int = 300) -> Image.Image:
    pdf = pdfium.PdfDocument(str(pdf_path))
    page = pdf[page_number - 1]
    bitmap = page.render(scale=dpi / 72.0, rotation=0)
    image = bitmap.to_pil().convert("RGB")
    page.close()
    pdf.close()
    return image


def crop_norm(image: Image.Image, box: tuple[float, float, float, float]) -> Image.Image:
    x0, y0, x1, y1 = box
    return image.crop(
        (
            round(x0 * image.width),
            round(y0 * image.height),
            round(x1 * image.width),
            round(y1 * image.height),
        )
    )


def trim_white(image: Image.Image, pad: int = 20) -> Image.Image:
    bg = Image.new("RGB", image.size, "white")
    diff = ImageChops.difference(image, bg).convert("L")
    bbox = diff.point(lambda p: 0 if p < 12 else 255).getbbox()
    if not bbox:
        return image
    left = max(0, bbox[0] - pad)
    top = max(0, bbox[1] - pad)
    right = min(image.width, bbox[2] + pad)
    bottom = min(image.height, bbox[3] + pad)
    return image.crop((left, top, right, bottom))


SPECS = [
    # Minsoo Kim and Hyungcheol Shin, IEEE TED 2021.
    (
        "Kim(김민수)_Analysis_and_Compact_Modeling_of_Fast_Detrapping_From_Bandgap-Engineered_Tunneling_Oxide_in_3-D_NAND_Flash_Memories.pdf",
        2,
        (0.055, 0.045, 0.49, 0.405),
        "km_fig01_betox_structure_and_paths.png",
    ),
    (
        "Kim(김민수)_Analysis_and_Compact_Modeling_of_Fast_Detrapping_From_Bandgap-Engineered_Tunneling_Oxide_in_3-D_NAND_Flash_Memories.pdf",
        2,
        (0.075, 0.485, 0.49, 0.755),
        "km_table01_model_parameters.png",
    ),
    (
        "Kim(김민수)_Analysis_and_Compact_Modeling_of_Fast_Detrapping_From_Bandgap-Engineered_Tunneling_Oxide_in_3-D_NAND_Flash_Memories.pdf",
        3,
        (0.055, 0.055, 0.49, 0.255),
        "km_fig02_trapped_electron_contours.png",
    ),
    (
        "Kim(김민수)_Analysis_and_Compact_Modeling_of_Fast_Detrapping_From_Bandgap-Engineered_Tunneling_Oxide_in_3-D_NAND_Flash_Memories.pdf",
        3,
        (0.505, 0.055, 0.95, 0.24),
        "km_fig03_thermal_emission_calibration.png",
    ),
    (
        "Kim(김민수)_Analysis_and_Compact_Modeling_of_Fast_Detrapping_From_Bandgap-Engineered_Tunneling_Oxide_in_3-D_NAND_Flash_Memories.pdf",
        4,
        (0.055, 0.055, 0.49, 0.245),
        "km_fig04_band_and_trapped_distribution.png",
    ),
    (
        "Kim(김민수)_Analysis_and_Compact_Modeling_of_Fast_Detrapping_From_Bandgap-Engineered_Tunneling_Oxide_in_3-D_NAND_Flash_Memories.pdf",
        4,
        (0.055, 0.275, 0.49, 0.455),
        "km_fig05_dt_calibration.png",
    ),
    (
        "Kim(김민수)_Analysis_and_Compact_Modeling_of_Fast_Detrapping_From_Bandgap-Engineered_Tunneling_Oxide_in_3-D_NAND_Flash_Memories.pdf",
        4,
        (0.505, 0.055, 0.95, 0.245),
        "km_fig06_tbt_calibration.png",
    ),
    (
        "Kim(김민수)_Analysis_and_Compact_Modeling_of_Fast_Detrapping_From_Bandgap-Engineered_Tunneling_Oxide_in_3-D_NAND_Flash_Memories.pdf",
        5,
        (0.09, 0.055, 0.455, 0.40),
        "km_fig07_temperature_path_rates.png",
    ),
    (
        "Kim(김민수)_Analysis_and_Compact_Modeling_of_Fast_Detrapping_From_Bandgap-Engineered_Tunneling_Oxide_in_3-D_NAND_Flash_Memories.pdf",
        5,
        (0.55, 0.055, 0.91, 0.40),
        "km_fig08_position_path_rates.png",
    ),
    (
        "Kim(김민수)_Analysis_and_Compact_Modeling_of_Fast_Detrapping_From_Bandgap-Engineered_Tunneling_Oxide_in_3-D_NAND_Flash_Memories.pdf",
        5,
        (0.59, 0.475, 0.88, 0.68),
        "km_fig09_stretched_exponential_fit.png",
    ),
    (
        "Kim(김민수)_Analysis_and_Compact_Modeling_of_Fast_Detrapping_From_Bandgap-Engineered_Tunneling_Oxide_in_3-D_NAND_Flash_Memories.pdf",
        6,
        (0.055, 0.035, 0.49, 0.36),
        "km_fig10_curve_shape_analysis.png",
    ),
    (
        "Kim(김민수)_Analysis_and_Compact_Modeling_of_Fast_Detrapping_From_Bandgap-Engineered_Tunneling_Oxide_in_3-D_NAND_Flash_Memories.pdf",
        6,
        (0.12, 0.39, 0.43, 0.59),
        "km_fig11_activation_energy.png",
    ),
    # Myung Jin and Hyungcheol Shin, IEEE TED 2025.
    (
        "Modeling_Attempt-to-Escape_Frequency_Tunneling_Emission_of_Trapped_Electrons_in_Tunneling_Oxides_of_3-D_NAND_Flash_Memory.pdf",
        1,
        (0.51, 0.285, 0.955, 0.735),
        "mj_ted_fig01_structure_and_reliability.png",
    ),
    (
        "Modeling_Attempt-to-Escape_Frequency_Tunneling_Emission_of_Trapped_Electrons_in_Tunneling_Oxides_of_3-D_NAND_Flash_Memory.pdf",
        3,
        (0.055, 0.055, 0.49, 0.56),
        "mj_ted_fig02_tcad_program_retention.png",
    ),
    (
        "Modeling_Attempt-to-Escape_Frequency_Tunneling_Emission_of_Trapped_Electrons_in_Tunneling_Oxides_of_3-D_NAND_Flash_Memory.pdf",
        3,
        (0.505, 0.055, 0.95, 0.31),
        "mj_ted_fig03_band_trap_transition.png",
    ),
    (
        "Modeling_Attempt-to-Escape_Frequency_Tunneling_Emission_of_Trapped_Electrons_in_Tunneling_Oxides_of_3-D_NAND_Flash_Memory.pdf",
        4,
        (0.055, 0.055, 0.49, 0.37),
        "mj_ted_fig04_trap_profile_and_specification.png",
    ),
    (
        "Modeling_Attempt-to-Escape_Frequency_Tunneling_Emission_of_Trapped_Electrons_in_Tunneling_Oxides_of_3-D_NAND_Flash_Memory.pdf",
        5,
        (0.055, 0.055, 0.49, 0.34),
        "mj_ted_fig05_tcad_model_validation.png",
    ),
    (
        "Modeling_Attempt-to-Escape_Frequency_Tunneling_Emission_of_Trapped_Electrons_in_Tunneling_Oxides_of_3-D_NAND_Flash_Memory.pdf",
        5,
        (0.515, 0.055, 0.95, 0.33),
        "mj_ted_fig06_attempt_frequency_and_rate.png",
    ),
    # Myung Jin, Haechan Choi, and Hyungcheol Shin, IEEE EDL 2026.
    (
        "Time-Step-Free_Physics-Based_Modeling_of_Retention_Loss_in_Cryogenic_3-D_NAND_Flash.pdf",
        2,
        (0.055, 0.045, 0.49, 0.43),
        "mj_edl_fig01_charge_node_discretization.png",
    ),
    (
        "Time-Step-Free_Physics-Based_Modeling_of_Retention_Loss_in_Cryogenic_3-D_NAND_Flash.pdf",
        2,
        (0.505, 0.055, 0.95, 0.46),
        "mj_edl_fig02_band_initial_profile_parameters.png",
    ),
    (
        "Time-Step-Free_Physics-Based_Modeling_of_Retention_Loss_in_Cryogenic_3-D_NAND_Flash.pdf",
        3,
        (0.055, 0.055, 0.49, 0.37),
        "mj_edl_fig03_validation.png",
    ),
    (
        "Time-Step-Free_Physics-Based_Modeling_of_Retention_Loss_in_Cryogenic_3-D_NAND_Flash.pdf",
        3,
        (0.065, 0.405, 0.49, 0.565),
        "mj_edl_table01_runtime_comparison.png",
    ),
]


def main() -> None:
    cache: dict[tuple[str, int], Image.Image] = {}
    for pdf_name, page_number, box, out_name in SPECS:
        key = (pdf_name, page_number)
        if key not in cache:
            cache[key] = render_page(ROOT / pdf_name, page_number)
        figure = trim_white(crop_norm(cache[key], box))
        figure.save(OUT / out_name, optimize=True)
        print(f"{out_name}: {figure.width}x{figure.height}")
        figure.close()
    for image in cache.values():
        image.close()

    ppt_map = {
        "슬라이드15.PNG": "ppt_slide16_cryogenic_measurement.png",
        "슬라이드16.PNG": "ppt_slide17_cryogenic_tcad_convergence.png",
        "슬라이드17.PNG": "ppt_slide18_cryogenic_model_validation.png",
        "슬라이드18.PNG": "ppt_slide19_computational_impact.png",
        "슬라이드19.PNG": "ppt_slide20_tat_route_count.png",
        "슬라이드20.PNG": "ppt_slide21_tat_quantitative_comparison.png",
    }
    ppt_dir = ROOT / ".thesis_build" / "ppt_render"
    for source_name, out_name in ppt_map.items():
        image = Image.open(ppt_dir / source_name).convert("RGB")
        image.save(OUT / out_name, optimize=True)
        print(f"{out_name}: {image.width}x{image.height}")
        image.close()


if __name__ == "__main__":
    main()
