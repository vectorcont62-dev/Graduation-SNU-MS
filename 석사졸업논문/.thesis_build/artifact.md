# Thesis template execution contract

## Reference

- Retained reference: `C:\Users\joshs\Desktop\local-laptop\Graduation-SNU-MS\석사졸업논문\석사학위논문_이찬_초안.docx`
- SHA-256: `be3c1b20c5aa7ef02962026d4291b3ee2b2b2fd6685108a3a19ea4726b359f02`
- Word-rendered page count: 113
- Section count: 3
- Render evidence: `.thesis_build/reference_pages/page-001.png` through `page-113.png`
- Structural evidence: `.thesis_build/template_style_evidence.json`
- Package evidence: `.thesis_build/template_package_inventory.json` (91 parts, each with size and SHA-256)

## Page system

- All sections use portrait pages sized 7.48125 x 10.2375 in.
- Left/right margins are 1.18125 in throughout.
- Section 1: top 0.98472 in, bottom 0.39375 in, header/footer distance 0 in.
- Sections 2-3: top 0.7875 in, bottom 0.59097 in, header/footer distance 0.59097 in.
- Section 1 ends after the degree-submission/approval pages and has no visible pagination.
- Section 2 contains the Korean abstract and front matter, uses lower-Roman page numbering, and starts on a new page.
- Section 3 contains Chapters 1-7, references, and the English abstract, uses Arabic page numbering beginning at 1, and starts on a new page.
- No odd/even variants or first-page variants are used. Each section break is a new-page break.

## Typography and paragraph roles

- Primary Korean face: HY신명조. Primary English/reference face: Times New Roman. Equations use Cambria Math when direct formatting is required.
- `본문 내용`: HY신명조 11 pt, justified, 2.0 line spacing. This is the normal thesis prose role.
- `Heading 1`: HY신명조 20 pt bold, centered by direct formatting, chapter page break before.
- `Heading 2`: HY신명조 16 pt bold, centered or left according to the retained source paragraph role.
- `그림`: centered image paragraph, 14.4 pt spacing before, 1.25 line spacing.
- `Caption`: centered, bold, 14.4 pt spacing after. Figure/table numbering uses Word SEQ fields.
- `수식`: centered with 8 pt space before/after.
- `References`: Times New Roman with the retained expanded line spacing.
- `toc 1`, `toc 2`, and `table of figures`: retained Word TOC/list styles with dotted leaders and page numbers.
- The title and approval pages remain source-derived, with run-level HY신명조/Century formatting, large centered Korean title, smaller English title, school/department/author block, and signature lines.

## Lists, tables, figures, and recurring components

- TOC and lists of figures/tables are true Word fields, updated in Microsoft Word before delivery.
- Figure and table captions use `SEQ 그림` and `SEQ 표`, respectively, so the front-matter lists populate deterministically after field refresh.
- Figures are inline only. No floating/anchored drawings are introduced.
- Figures are restricted to raster crops from the locally supplied PDFs and exported slides from `진명 석사졸업 연구 정리 - TAT 제외.pptx`.
- Tables are limited to actual repeated parameter/result data, use fixed widths within the 5.11875 in text measure, explicit column widths, cell margins, and repeating header rows where useful.
- Footer page numbers retain the reference footer position and alignment.

## Content flow and slot map

- Section 1 editable slots: Korean title, English title, date, department, author, adviser, submission text, approval text, committee placeholders.
- Section 2 editable slots: Korean abstract, keywords, student-number placeholder, TOC, list of tables, list of figures.
- Section 3 editable slots: seven numbered chapters, figure/table/equation blocks, references, English abstract.
- All body prose, captions, equations, tables, references, and images from the reference thesis are removed and replaced.
- Styles, numbering definitions, theme, headers/footers, page geometry, and recurring page furniture are preserve-only unless a user-requested content replacement requires a field refresh.
- Stable locators: body order plus paragraph style; section breaks at the end of the approval block and the end of front matter; footer fields in `word/footer*.xml`; styles in `word/styles.xml`; numbering in `word/numbering.xml`.

## Package preservation

- Preserve-only parts include `[Content_Types].xml`, theme, styles, numbering, settings except field-update state, font table, headers/footers except refreshed cached page-field text, and document properties.
- Editable parts include `word/document.xml`, document relationships needed for newly inserted figures, and `word/media/*` for the approved local-source figures.
- Existing unused figure relationships/media may be removed by the Word-compatible save path; this is an intentional consequence of replacing every old body figure.
- No comments, tracked changes, footnotes, endnotes, or content controls are present in the reference.

## Fidelity gates

- Retained reference hash must remain unchanged.
- Final page geometry and three-section structure must match the contract.
- The first two title/approval pages, Korean abstract/front matter, chapter openings, dense figure pages, references, and English abstract must remain visually recognizable as the source thesis family.
- Every page must be rendered through Microsoft Word to PDF and rasterized for inspection.
- Final page count must be at least 100 including title pages and references.
- No old vertical-redistribution prose, figures, captions, references, author name, student number, or thesis title may remain.
- No figure may originate outside the supplied local PDFs/PPTX.
- Fields must be refreshed in Microsoft Word; the TOC and lists must show final page numbers.
- No clipping, overlap, missing glyphs, broken table, unintended blank page, or stale placeholder other than clearly labeled committee/student-number placeholders is acceptable.
