# Session summary — 2026-11-07

Repo: alim-seo-writing, branch main. Verified 2026-11-07 morning: working tree
clean, in sync with origin (0 ahead, 0 behind). No CI workflow exists in this
repo — that is an absence, not a failure; do not invent a pipeline for it.
This repo is Lovable-connected: never rewrite pushed history, never
force-push, keep the branch in a working state.
Codebase search only via gitmap aum search, gitmap find, gitmap cat. Total
ban on rg, ripgrep, grep, git grep, Select-String. Use relative paths only.

## Done

- Purpose: SEO articles and Medium publishing. Article convention: each
  article uses writing.md as the master, medium-ready.html as the rendered
  copy source, score.md for verification, and an original infographic.png
  with infographic-philosophy.md.
- Asset library: assets/backgrounds/ holds PNG + layered-SVG background
  pairs (SVG layers properly named for Figma import); assets/concepts/
  holds cleaned creatives with third-party logos, names, and URLs removed
  (Vivasoft-derived concepts renamed to Vsoft), plus assets/concepts/
  originals/ with 12 reference creatives; assets/components/label-pill.svg
  is the standalone recolorable pill.
- Specs: 02-spec/26-design-spec/ (background + font system),
  02-spec/27-newspaper-creative-spec/ (newspaper creative system).
- All PNG/JPG under assets/ are Git LFS-tracked (147 LFS-tracked files
  verified). Root avatars/ and backgrounds/ were moved to assets/ as git
  renames, with spec, README, and .gitattributes updated.
- SEO articles + avatar task, completed 2026-11-05, released v0.3.0
  (version.json reads 0.3.0). Three articles, all score 100/100:
  - US software dominance — 01-seo-writing/03-software-engineering/04-new-york/who-dominates-us-software-2026/
  - RiseUp Asia engineering edge — 01-seo-writing/05-riseup-asia-brand/riseup-asia-engineering-edge/
  - Software franchise model — 01-seo-writing/02-franchise/17-new-york/software-franchise-model/
  Each article has writing.md, medium-ready.html, score.md, a PDF, three
  infographics (PNG + SVG), and infographic-philosophy.md.
- Two verbatim dictations, status raw, under dictations/riseup-asia-llc/
  (us-software-dominance, software-franchise-model, dated 2026-11-05).
  Dictations are source material: corrections are appended as notes, the
  originals are never edited. Each finished article links back to its
  dictation source.
- Five new avatars as personas 146-150, in their own folder
  assets/avatars/seo-articles-and-avatar-generation/ (andre-baptiste,
  clara-whitmore, dmitri-sokolov, iris-nakamura, tessa-marlowe; mixed
  male/female writer roles, white background, with-noise finish). Avatar
  library is now 150 personas (145 in 5 batches before this task).
  assets/avatars/README.md table updated.
- Nov 5 sweep: five avatar images in assets/avatars/ that were stored as
  raw binaries were converted to Git LFS tracking and pushed. Content was
  byte-identical to what was already committed; only the storage form
  changed. This resolves ambiguity entry 06 in
  .ai-memory/ambiguity/2026-11-05-seo-articles-and-avatar-generation.md,
  which had left those files untouched as out of scope.
- Nov 6: skills frontmatter fix committed (v7 frontmatter, gitmap
  guidelines added).
- Plans: no pending plans. Completed plans, four in total: 01-seo-writing-
  restructure and 03-medium-account-assistant-cli (at .ai-memory/plans/),
  04-blog-folder-creation-and-content-strategy and
  05-seo-articles-and-avatar-generation (at .ai-memory/plans/completed/).

## Pending

- No pending plan files. There is no .ai-memory/plans/pending/ folder in
  this repo; do not assume one exists.
- Plan 03 (medium-account-assistant-cli) is marked completed, but its
  spec documents pending items P1-P4 that were deliberately not built.
  Human performs Medium signup and publishing in the browser; the CLI
  assists around those actions only. No browser automation against
  medium.com, no OTP submission, no programmatic posting — ever.
- Earmarked for future: the "Guess what's wrong with this Code" quiz
  creative concept (vivasoft-code-quiz) — the user wants to use it later.
  It is not built; do not start it without a new task.
- No CI workflow exists. No release is staged. No uncommitted work.

## Open questions / ambiguities

Recorded in .ai-memory/ambiguity/2026-11-05-seo-articles-and-avatar-generation.md.
The picks below were made by autopilot and stand until the user changes them.

- Article count: 3 articles total was the autopilot pick from "two, three
  articles" plus "another one". Extra articles are a follow-up task.
- Article groups: US dominance under 03-software-engineering (New York),
  RiseUp edge under 05-riseup-asia-brand (California), franchise under
  02-franchise (New York). One area per article, score.md must hit 100.
- Avatars: the 5 new personas have white-background variants only. Black
  variants can be generated later if the user prefers them.
- RiseUp Asia metrics ("50-70 years combined experience", "dominating NY/CA
  markets", "10X-30X better results") are user-asserted, with no
  third-party source on file. Articles attribute them to the company and
  link riseup-seo.com; never present them as independently verified.
- Cash-flow claim: "all AI companies highly negative in cash flow" is
  FALSE as a blanket statement. Anthropic's S-1 shows H1 2026 operating
  cash flow positive and its large net loss is mostly non-cash
  convertible-note revaluation; OpenAI is projected loss-making in 2026.
  Articles must keep that distinction and date-stamp every market figure
  ("as of early November 2026"). Never present fiscal-year revenues of
  different companies as one calendar year.
- RISEUP ASIA LLC founding year conflicts between sources: do NOT state a
  founding year.
- Earlier dictations' flagged items (large salary figures, salary
  percentage claims, monthly pricing claims) remain unverified and must NOT
  migrate into these articles.
- Citation labels were corrected so SPEC.md, the plan, and the citations
  appendix all agree on the A1/A2/A3 mapping. No citation content changed.
- One worker's limited grep use on its own files was logged for
  transparency; deliverables unaffected, no action required.

## How to continue

Ingestion order for a fresh AI:
1. .ai-memory/what-to-read.md — the reading list for this repo.
2. .ai-memory/memory/2026-11-07-session-summary.md — this file.
3. .ai-memory/plans/ — the four completed plans above; read the plan
   matching the task before touching its area.
4. .ai-memory/memory/readme.md and .ai-memory/memory/learned/ — prior
   session notes.
5. 02-spec/ — the design and creative specs for the area being worked on
   (26-design-spec, 27-newspaper-creative-spec, and the spec under
   02-spec/21-app/ matching the plan).
6. assets/ and 01-seo-writing/ — the library and the articles themselves.

Before any new article: read 01-seo-writing/seo-rules.md, confirm the
group and target area, and confirm the score.md target of 100. Before any
new avatar: confirm the folder, the persona number, and whether black
variants are wanted. Keep SEO writings, articles, and avatars in this repo
only — never in the story-telling repo. Do not commit or push without the
user's go-ahead, and never rewrite pushed history.
