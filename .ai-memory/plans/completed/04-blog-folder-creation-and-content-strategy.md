# Plan: 04-blog-folder-creation-and-content-strategy

- **Status:** COMPLETED 2026-10-13
- **Spec:** 02-spec/21-app/04-blog-folder-creation-and-content-strategy/ (01-overview.md, 02-content-pipeline.md)
- **Subtasks:** .ai-memory/plans/subtasks/04-blog-folder-creation-and-content-strategy/ (01-riseup-asia-outlet.md, 02-medium-outlet.md)
- **Hard boundary:** blog content only under 04-blogs/. No changes to 01-seo-writing/, 02-spec/ (beyond this spec), 03-ai-scripts/, dictations/.

## Phases and owners

| Phase | Work | Owner | Owned files |
|---|---|---|---|
| 1 | Research (repo conventions, content strategy) | Lead + 2 research agents | (read-only) |
| 1 | Spec authoring (overview + pipeline, disjoint) | Spec Author A / Spec Author B | 02-spec/21-app/04-blog-folder-creation-and-content-strategy/01-overview.md / 02-content-pipeline.md; subtasks 01 / 02 |
| 2 | RiseUp Asia outlet: 2 articles (scaffold, draft, score, rewrite to >=95, html, philosophy) | Worker 01 | 04-blogs/riseup-asia/ (both article folders) |
| 2 | Medium outlet: 2 articles (same pipeline, differentiated framing) | Worker 02 | 04-blogs/medium/ (both article folders) |
| 3 | Consolidate, verify, atomic gitmap cpf + push | Lead | .ai-memory/plans/readme.md, 02-spec/21-app/readme.md |

## Rules for all workers

- Workdir is the repo root. Every shell command first: export PATH="$HOME/.local/bin:$PATH".
- TOTAL BAN on git commands (no status/diff/add/commit/push) — lead only.
- TOTAL BAN on rg, grep, git grep, Select-String — GitMap only (gitmap aum search, gitmap find, gitmap cat, gitmap py).
- Relative paths, lowercase filenames. Keep files under ~300 lines.
- Scaffold new folders with: gitmap py 03-ai-scripts/seo-scaffold.py --group <outlet> --slug <slug> --title <title> --area <area> --dest 04-blogs
- Tool failing twice: reply STATUS: BLOCKED with exact error, stop.

## Acceptance

- 04-blogs/riseup-asia/ and 04-blogs/medium/ each hold 2 article folders with writing.md, score.md, medium-ready.html, infographic-philosophy.md.
- Every article: cold-open in a named local place (CA / San Diego / NY), 1-2 natural anchors to https://riseup-asia.com, primary keyword cluster at 30-60 combined mentions (no exact phrase above ~3% density), brand token exactly `RISEUP ASIA LLC`, score.md total >=95 after rewrite gate.
- Zero duplicated paragraphs across outlets; risk-handling register from 01-overview.md applied verbatim (desi passage deleted, no fake Jobs quotes, no unverified figures, no H1B salary falsehoods).
- One atomic commit via gitmap cpf at the end; pushed.

## Assumptions

- Spec/plan paths use the 04- numeric prefix per house convention (user's message gave the slug without prefix; prefix applied).
- New top-level root 04-blogs/ (02- was taken by 02-spec).
- 2 dictations x 2 outlets = 4 articles; localities split CA/San Diego/NY across the four.
- Infographic PNG/SVG generation is a follow-up (philosophy briefs only in this run).

## Follow-ups

- Generate infographic PNG/SVG per article via 03-ai-scripts/seo-infographic.py.
- Generate article PDFs via 03-ai-scripts/seo-pdf.py.
- Refresh Excel tracker if these blogs join the publishing pipeline.

## Completion summary
- 4 articles written, scored, rendered: 04-blogs/riseup-asia/san-diego/vibe-coding-is-dead (100/100), 04-blogs/riseup-asia/california/cheap-h1b-vs-premium-developers (100/100), 04-blogs/medium/01-new-york/vibe-coding-is-dead (100/100), 04-blogs/medium/02-san-diego/cheap-h1b-vs-premium-developers (98/100).
- Independent lead verification: 0 identical paragraphs across outlets; keyword clusters 34-48 (within 30-60); brand token exact; 2 riseup-asia.com anchors each; 0 pronoun/style violations; HTML content parity confirmed (lists as <ol>/<li>, image as <img>).
- Spec: 02-spec/21-app/04-blog-folder-creation-and-content-strategy/ (01-overview.md, 02-content-pipeline.md).
