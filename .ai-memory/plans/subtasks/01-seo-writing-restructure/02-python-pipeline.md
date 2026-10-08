# Subtask 02 — python pipeline scripts (Worker 02)

Owner: Worker 02. Owned files: 03-ai-scripts/**, 02-transcribed-ideas/**.
Read first: 02-spec/21-app/01-seo-writing-restructure/02-pipeline.md.

## Steps

1. Copy 2–3 sample article dirs to /tmp/samples first (Worker 01 is moving the
   originals — never read 01-seo-writing/ directly for pattern reference after step 1).
   Study `writing.md` + `medium-ready.html` for the article pattern.
2. Build `03-ai-scripts/seo-scaffold.py` per spec (argparse CLI, pattern skeleton,
   frontmatter, medium-ready.html wrapper, score.md checklist, philosophy template).
3. Build `03-ai-scripts/seo-pdf.py` per spec. Select the renderer with evidence, in
   order: `gitmap py -c "import weasyprint"` → headless chromium
   (`which chromium || which chromium-browser || which google-chrome`) --print-to-pdf →
   reportlab. `gitmap py -m pip install --user <pkg>` only if the import check fails.
4. Verify: scaffold a sample article to /tmp/scaffold-test (NOT in the repo);
   render the /tmp sample HTMLs to /tmp/pdf-test/*.pdf; confirm PDFs are valid
   (size > 0, page count readable).
5. Create `02-transcribed-ideas/README.md` + `02-transcribed-ideas/_template.md` per spec.
6. Do NOT write anything into 01-seo-writing/ yet (backfill is wave 2, after moves).

## Output contract

Reply with: {"task": "Task-03/04", "status": "DONE|BLOCKED",
"files": ["03-ai-scripts/seo-scaffold.py", "03-ai-scripts/seo-pdf.py",
"02-transcribed-ideas/README.md", "02-transcribed-ideas/_template.md"],
"checks": "<commands> -> exit codes", "renderer": "<chosen lib + evidence>",
"blockers": []}
