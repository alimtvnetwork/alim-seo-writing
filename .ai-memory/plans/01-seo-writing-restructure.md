# Plan: 01-seo-writing-restructure

Status: ACTIVE — Phase 1 (spec/plan) complete; Phase 2 waves dispatch next.
Spec: 02-spec/21-app/01-seo-writing-restructure/

## Phases and owners

| Phase | Work | Owner | Owned files |
|---|---|---|---|
| 1 | Spec + this plan + subtasks | lead | 02-spec/21-app/01-seo-writing-restructure/, .ai-memory/plans/ |
| 2a | Folder restructure moves (mapping rules in spec 01) | Worker 01 | 01-seo-writing/** (moves only) |
| 2b | Python scripts + transcribe inbox (spec 02) | Worker 02 | 03-ai-scripts/**, 02-transcribed-ideas/** |
| 2c | Backfill medium-ready.html + PDF where missing | Worker 02 (wave 2) | 01-seo-writing/** (new files only) |
| 3 | gitmap reset --confirm + gitmap scan on ~/workspace/repos; secrets gate; atomic push | lead | — |

## Rules for all workers

- Workdir repo root. `export PATH="$HOME/.local/bin:$PATH"` before any gitmap call.
- TOTAL BAN on git commands (no status/diff/add/commit/mv) — plain `mv` / python `shutil`.
- TOTAL BAN on rg, ripgrep, grep, git grep, Select-String — use `gitmap aum search`,
  `gitmap find`, `gitmap lf`, `gitmap cat`.
- Python only via `gitmap py`. Relative paths only, lowercase filenames.
- On any tool failing twice: stop, report STATUS: BLOCKED with the exact error.

## Acceptance

- ~200 article dirs regrouped per mapping rules; file count before == after;
  every leaf dir keeps its `writing.md`.
- `03-ai-scripts/seo-scaffold.py` + `03-ai-scripts/seo-pdf.py` run clean via `gitmap py`;
  sample scaffold + sample PDFs verified in /tmp.
- `02-transcribed-ideas/` inbox with README + template.
- Backfill: no article dir left without `medium-ready.html` + PDF.
- `gitmap reset --confirm` + `gitmap scan` on repos root re-index the new structure.
- Single `gitmap cpf "seo-writing - <summary>"` commit, pushed (no colon in message).

## Assumptions

- Alphabetical area sequencing (01-california …) per spec; user can renumber later.
- 05-riseup-asia-brand vs 07-engineering-culture split per RULE C/E lists in spec.
- Ato SEO repo item stays blocked until the user names the repo.

## Follow-ups (not this run)

- Refresh Excel tracker GitHub URLs (old paths).
- Ato SEO repo: clone into SEO folder, create SEO/SEO-writing, move content.
