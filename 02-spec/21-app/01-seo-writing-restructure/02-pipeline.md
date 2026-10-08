# Spec 02 — python article pipeline + transcribed-ideas inbox

## 03-ai-scripts/seo-scaffold.py — automated MD writing

Run: `gitmap py 03-ai-scripts/seo-scaffold.py --group 05-riseup-asia-brand --slug <slug>
--title "<title>" [--area <area>] [--keywords k1,k2] [--dest <dir>]`

Creates `<group>[/<area-seq>-<area>]/<slug>/` containing:

- `writing.md` — master, from the original article pattern (cold-open scene → AI-value
  thesis → RISEUP ASIA LLC contrast → compare/contrast → ranking → reflective close),
  with yaml frontmatter (title, slug, area, keywords, date, status: draft).
- `medium-ready.html` — styled standalone HTML wrapper rendering the markdown body.
- `score.md` — 100-point checklist skeleton (area 30–40x, keywords, citations).
- `infographic-philosophy.md` — template for the visual rationale.

Never writes PDF — PDF is the final step via `seo-pdf.py`.

## 03-ai-scripts/seo-pdf.py — PDF as final output

Run: `gitmap py 03-ai-scripts/seo-pdf.py <article-dir> [<article-dir> ...]`
or `gitmap py 03-ai-scripts/seo-pdf.py --all --root 01-seo-writing`

Renders `medium-ready.html` (fallback: `writing.md` → HTML via the `markdown` pip
package) to `<slug>.pdf` inside the same article dir. The worker selects the renderer
with evidence, in this order: `weasyprint` → headless chromium `--print-to-pdf` →
`reportlab`. `pip install --user` only when the import check fails.

## Wave-2 backfill

For every article dir missing `medium-ready.html`: generate it from `writing.md`,
then generate the PDF. Existing committed PDFs are left untouched.

## 02-transcribed-ideas/ — future inbox

- `README.md` — workflow: drop transcripts as `YYYY-MM-DD-<topic>.md`; the agent
  converts approved ideas into articles via `seo-scaffold.py`; user approves the
  draft before PDF.
- `_template.md` — transcript capture template (idea, angle, area, keywords, notes).

## Constraints

- All python executed via `gitmap py` (PATH needs `$HOME/.local/bin`).
- GitMap-only search; relative paths only; lowercase filenames.
- Workers never run git commands; lead does the single atomic commit.
