# 02-transcribed-ideas — transcript inbox

This folder is where the user drops transcribed ideas. Each transcript becomes
the seed for one or more SEO articles. Nothing here is published directly.

## Workflow

1. Drop a transcript as `YYYY-MM-DD-<topic>.md` (copy `02-transcribed-ideas/_template.md`).
2. The agent reads the transcript and drafts the article with
   `gitmap py 03-ai-scripts/seo-scaffold.py --group <group> --slug <slug> --title "<title>" --area "<area>" --keywords "k1,k2"`.
3. The user reviews and approves the `writing.md` draft (status: draft -> approved).
4. Only after approval: `gitmap py 03-ai-scripts/seo-pdf.py <article-dir>` renders the final PDF.

Rules:

- One transcript file per recording; never edit a transcript after the draft is approved — append corrections as a new dated file.
- Ideas stay in this folder until approved; `01-seo-writing/` holds only approved, scaffolded articles.
- The agent converts approved ideas into articles; the user approves the draft before PDF.
