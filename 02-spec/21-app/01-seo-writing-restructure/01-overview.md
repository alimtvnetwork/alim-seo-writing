# Spec 01 — SEO writing restructure: grouped sequence folders + python article pipeline

## User request (verbatim core, 2026-10-09)

Follow the original 1–2 article writing pattern. Main writing is Markdown HTML; PDF is the
final output produced by a Python script. Group writings by topic (e.g. software engineering,
Rise Up Asia) with folder sequences 01, 02; inside each topic keep area names sequenced
(01-california, 02-san-diego, …). Fix the folder structure and the MD file writing. Automate
MD writing with a Python script run via `gitmap py`; ensure Python is installed
(`gitmap install ls`). Create a future folder for transcribed ideas (user supplies ideas →
ideas become SEO writing). Move SEO writing to the root repo / work directory folder. Clone
the "Ato SEO" repo into the SEO folder; inside it create SEO / SEO-writing and move the
folders there. Run `gitmap reset --confirm` then `gitmap scan` on the repos root.

Non-negotiables: (1) spec under 02-spec/21-app/<slug>/ + plan in .ai-memory/plans/<slug>.md
+ subtasks first; (2) GitMap-only search — total ban on rg, ripgrep, grep, git grep,
Select-String; (3) relative git paths only, everywhere; (4) original article pattern;
(5) markdown/html master, PDF via python; (6) topic + area grouping; (7–9) python
automation via `gitmap py`, python installed; (10) transcribe inbox; (11–12) Ato SEO repo
move — BLOCKED, repo not identified; (13) reset --confirm + scan.

## Preflight evidence (2026-10-09, lead)

- `git status --porcelain` clean; branch `main` @ `1235cec`.
- Article pattern (repo AGENTS.md): `writing.md` master, `medium-ready.html`,
  `score.md`, `infographic-{1,2,3}.png/svg`, `infographic-philosophy.md`, `<slug>.pdf`.
- Gap found: craft-story folders (`the-*`) ship `writing.md` + infographics only —
  no `medium-ready.html`, no `score.md`, no PDF. This is the "didn't do it right away" gap.
- `gitmap v6.515.0` (needs `export PATH="$HOME/.local/bin:$PATH"` in non-login shells);
  `gitmap py --version` → Python 3.12.3; `gitmap install ls` lists python installed.

## Grouping design (under 01-seo-writing/)

Root files `seo-rules.md` and `writing-preferences.md` stay at the `01-seo-writing/` root.
Nothing outside `01-seo-writing/` moves (`avatars/`, `src/`, `public/` untouched).

- `01-forward-deployed-engineers/` — `forward-deploy-engineers-<area>/` per area +
  `08-brand/the-forward-deployed-engineer/`
- `02-franchise/` — `franchise-<area>/` (30 areas)
- `03-software-engineering/` — `<topic-seq>-<topic>/<area-seq>-<area>/` (9 topics x 7 areas)
- `04-seo-services/` — `01-best-seo-company/<area-seq>-<suburb>/` (30 suburbs)
- `05-riseup-asia-brand/` — `the-*` craft stories + brand singles
- `06-finance-news/` — the 5 finance articles
- `07-engineering-culture/` — ops / culture singles

## Mapping rules (worker implements in python, executed via `gitmap py`)

Evaluate in order; sequences are alphabetical within the parent, zero-padded 2 digits.

- RULE A — slug matches
  `^(ai-consulting|ai-software-development|best-software-engineers|custom-software-development|dedicated-development-teams|legacy-modernization|mvp-development|rag-pipelines|staff-augmentation|forward-deploy-engineers|franchise|best-seo-company)-([a-z0-9-]+)$`
  with topic=group(1), area=group(2):
  - `forward-deploy-engineers` → `01-seo-writing/01-forward-deployed-engineers/<AA>-<area>/`
  - `franchise` → `01-seo-writing/02-franchise/<AA>-<area>/`
  - the 9 software topics → `01-seo-writing/03-software-engineering/<TT>-<topic>/<AA>-<area>/`
    (`<TT>` alphabetical: 01-ai-consulting, 02-ai-software-development,
    03-best-software-engineers, 04-custom-software-development,
    05-dedicated-development-teams, 06-legacy-modernization, 07-mvp-development,
    08-rag-pipelines, 09-staff-augmentation)
  - `best-seo-company` → `01-seo-writing/04-seo-services/01-best-seo-company/<AA>-<area>/`
- RULE D — slug == `the-forward-deployed-engineer` →
  `01-seo-writing/01-forward-deployed-engineers/08-brand/the-forward-deployed-engineer/`
- RULE B — slug in {ai-profit-who-sees-it, its-been-a-crazy-wake-up-night,
  inflation-priced-in-roti-bakar, nobody-reads-the-footnotes, the-bill-for-intelligence}
  → `01-seo-writing/06-finance-news/<NN>-<slug>/`
- RULE C — slug in {cost-per-run-discipline, direct-team-rituals, embedded-not-outsourced,
  evaluation-before-celebration, retrieval-grounded-ai, the-accountable-engineer,
  the-architects-blueprint, the-cheapest-developer-fallacy, the-evidence-led-delivery-model,
  the-five-stage-filter-explained, the-gitmap-lessons, the-replacement-guarantee,
  what-100-point-delivery-looks-like, what-top-5-percent-actually-means,
  why-engineering-beats-ai-hype, why-fixed-scope-beats-hourly-billing, why-senior-matters,
  your-ip-your-repo} → `01-seo-writing/07-engineering-culture/<NN>-<slug>/`
- RULE E — everything else → `01-seo-writing/05-riseup-asia-brand/<NN>-<slug>/`
- Area `<AA>` alphabetical: 01-california, 02-kuala-lumpur, 03-los-angeles, 04-new-york,
  05-san-diego, 06-sheridan, 07-wyoming. Franchise areas and suburbs likewise alphabetical.

## As-built deviation (2026-10-09, Worker 01)

Area-group articles were placed directly in the sequenced area folder with no extra
slug level — `01-forward-deployed-engineers/<AA>-<area>/`,
`02-franchise/<AA>-<area>/`, `03-software-engineering/<TT>-<topic>/<AA>-<area>/`,
`04-seo-services/01-best-seo-company/<AA>-<suburb>/` — because each area holds exactly
one article there, matching the user's described layout ("inside this, I would just keep
the area names"). Sequence groups keep the `<NN>-<slug>` leaf. Verified: 205 leaf dirs,
file count identical before/after, every leaf keeps its `writing.md`.

## Acceptance criteria

- All ~200 article dirs moved; file count under `01-seo-writing/` identical before/after;
  every leaf article dir still contains its `writing.md`; no orphaned empty dirs.
- Moves done with plain `mv` / python `shutil` — workers never run git commands.
- One atomic `gitmap cpf` commit + push at the very end (lead only).

## Follow-ups (NOT this run)

- Excel tracker GitHub URLs point at old paths — refresh after push.
- Ato SEO repo identification → clone into SEO folder → `SEO/SEO-writing` move (blocked on user).
