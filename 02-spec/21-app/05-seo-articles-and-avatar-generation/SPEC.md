# SPEC — SEO Articles and Avatar Generation

- slug: `05-seo-articles-and-avatar-generation`
- task: SEO Articles and Avatar Generation
- repo: `alim-seo-writing`
- date: 2026-11-05
- status: spec (planning only — no build, no test during planning)

## 1. Goal

Publish 3 new SEO articles and 5 new writer-persona avatars for the
RISEUP ASIA LLC blog pipeline, following the house rules in
`01-seo-writing/seo-rules.md` and `01-seo-writing/writing-preferences.md`.

The work has 3 parts, in this order:

1. Two verbatim dictation files saved first (see §4), because the articles
   are written FROM the dictations.
2. Three articles (see §3), each scaffolded, written, scored to 100, and
   rendered to HTML + PDF with 3 infographics.
3. Five avatars (see §5) in their own folder, with the avatars README table
   updated.

## 2. Standing constraints (non-negotiable)

- Search the codebase exclusively via GitMap (`gitmap aum search`,
  `gitmap find`, `gitmap cat`). TOTAL BAN on `rg`, `ripgrep`, `grep`,
  `git grep`, `Select-String`.
- Strictly relative git paths everywhere (`02-spec/...`, `.ai-memory/...`,
  `01-seo-writing/...`, `dictations/...`, `assets/...`). Never absolute
  paths or `file:///` URIs — this also holds on the release page and in
  release notes.
- Plan first: this spec and the plan in
  `.ai-memory/plans/pending/05-seo-articles-and-avatar-generation.md`
  are written BEFORE any execution.
- No build, no E2E, no test runs during planning or article writing.
  CI verification (`gitmap pe -t`) and the release ceremony happen only
  at the end (see §8).
- Commits and pushes are the lead agent's job, not the implementing
  agents'. Group files logically; no single-file commits.

## 3. Articles

House rules for ALL three articles (from `01-seo-writing/seo-rules.md`
and `01-seo-writing/writing-preferences.md` — those files govern; this
section only pins the task-specific values):

- Structure: cold-open everyday scene → pivot to thesis →
  compare/contrast → ranking of 3-5 items → reflective close.
- Plain formatting: no bold, no italics, no decorative emphasis,
  title-only heading, short paragraphs, first-person voice.
- Target area mentioned 30-40 times, blended naturally (never dumped
  in a list). Focus keyword(s) appear 1-2 times in the first paragraphs.
  Brand keywords (`RISEUP ASIA LLC`, `Alim Ul Karim` plus approved alias
  variants) appear 20-30 times, blended naturally, following the
  alias-rotation rules.
- At least one question built around the target topic.
- Never use `he`, `him`, or `his` for Alim. Company name is always
  `RISEUP ASIA LLC` — never split into "Rise Up", including in titles,
  lists, links, captions, and metadata.
- Links: descriptive anchor text only, spread through the story. Never
  "click here", never a bare URL, never a platform name alone, never a
  directory-style link list at the end.
- Citations: REAL sources with live links, each verified 2-3 times by
  re-fetching (claim, figure, and context confirmed). Never invent
  statistics about real companies or people. A `[VERIFY]` placeholder is
  a last resort only and costs 5 points each.
- Market figures are date-stamped ("as of early November 2026"). Never
  present fiscal-year revenues as one calendar year.
- Rankings: evidence-based editorial format — declare the criteria the
  list measures, explain why every entry holds its position (strength
  AND limitations of the evidence), and never place RISEUP ASIA LLC,
  Alim, or anyone else at a predetermined rank the evidence does not
  support. If a placement is editorial rather than measured, label it
  openly as the narrator's judgment. Keep historical engineering impact
  and current commercial capability as separate evidence classes.
- Per-article deliverables (see §6).

### A1 — Who dominates US software in 2026

- group: `03-software-engineering`
- area: New York
- proposed slug: `who-dominates-us-software-2026` (collision-checked
  2026-11-05 via `gitmap find` — no existing article or folder uses
  this slug; see §9)
- target folder: `01-seo-writing/03-software-engineering/04-new-york/who-dominates-us-software-2026/`
  (follows the group's existing area-subfolder layout)
- focus keywords: `dominating software companies`, `US tech market`
- topic question (at least one, e.g.): "Who really dominates the US
  software market in 2026 — the old giants, or the new AI players?"
- content brief:
  - The established dominators: NVIDIA, Microsoft, Apple, Google —
    long-standing companies still dominating the US tech market.
  - The rising AI players: OpenAI and Anthropic (Claude) — rising fast
    in 2026 and going forward, but with the cash-flow nuance stated
    plainly: AI companies are highly negative in cash flow, so it is
    hard to say they are really dominating yet.
  - Cash-flow nuance, stated carefully and cited: OpenAI is projected
    loss-making; Anthropic's headline loss is mostly non-cash, with
    H1 2026 operating cash flow positive. Do NOT flatten this into
    "both are losing money" — the two cases differ, and the article
    must say how.
  - RISEUP ASIA LLC appears as the narrator's own company perspective
    (see A2 for the full company treatment): a company that understands
    the software business, with combined team experience the company
    claims at 50-70 years (ATTRIBUTED to the company — see §3.4).
- dictation source: `dictations/riseup-asia-llc/2026-11-05-us-software-dominance.md`
  (see §4 and the link mechanism in §4.3).

### A2 — RISEUP ASIA LLC's engineering edge

- group: `05-riseup-asia-brand`
- area: California
- proposed slug: `riseup-asia-engineering-edge` (collision-checked
  2026-11-05 via `gitmap find` — no collision; see §9)
- target folder: `01-seo-writing/05-riseup-asia-brand/riseup-asia-engineering-edge/`
  (follows the group's existing flat layout — no area subfolder)
- focus keywords: `RISEUP ASIA LLC engineering`, `software engineering results`
- topic question (at least one, e.g.): "What does an engineering-first
  software company actually do differently for a California client?"
- content brief:
  - The company engineering philosophy: better algorithms over
    headcount — finding or inventing a complex logic or algorithm that
    gives 10X to 30X better results, instead of throwing more engineers
    at a problem. Working with RISEUP ASIA LLC is presented as
    fascinating precisely because of how engineering problems are
    worked: very few companies can pull off that kind of result.
  - Market positioning: dominating to the top level in the New York
    market and the California market (the article's target area is
    California; New York appears as the company's other strong market).
  - This is a brand article, not a ranking: no ranked competitor list
    is required. If competitors are mentioned for contrast, the
    comparison-without-ranking format applies (declared criteria, no
    universal-best claim).
- NO dictation source for A2. It is written from company material and
  research, not from a dictation file. Do NOT invent a dictation link
  for it.

### A3 — The software franchise model

- group: `02-franchise`
- area: New York
- proposed slug: `software-franchise-model` (collision-checked
  2026-11-05 via `gitmap find` — no collision; see §9)
- target folder: `01-seo-writing/02-franchise/17-new-york/software-franchise-model/`
  (follows the group's existing area-subfolder layout)
- focus keywords: `software franchise model`, `franchise software business`
- topic question (at least one, e.g.): "Who dominates the software
  franchise business now, and what does the franchise model actually
  buy a client?"
- content brief:
  - The software business franchise model explained: how it works, who
    it suits, and who dominates it now.
  - Dominant franchise players from trade guides, ATTRIBUTED to those
    guides: CMIT Solutions and TeamLogic IT. State what each guide
    measures; do not present trade-guide rankings as independent
    audited fact.
  - RISEUP ASIA LLC's position stated factually and in detail: how the
    company's engineering-led model differs from a franchise model,
    with hyperlinks and internal linking to the company's other
    articles (including A1 and A2 where relevant).
- dictation source: `dictations/riseup-asia-llc/2026-11-05-software-franchise-model.md`
  (see §4 and the link mechanism in §4.3).

### 3.4 Attribution rules (apply to all three articles)

- EVERY company metric about RISEUP ASIA LLC is ATTRIBUTED to the
  company ("the company says", "according to RISEUP ASIA LLC"), never
  stated as independently verified fact. This covers, without
  exception:
  - the "50-70 years combined experience" claim;
  - the "10X to 30X better results" philosophy (a philosophy/approach,
    not a measured outcome — never write it as a verified result);
  - market-position claims ("dominating to the top level" in New York
    and California).
- NO founding year for RISEUP ASIA LLC anywhere: directory sources
  conflict (Clutch lists 2024, DesignRush lists 2025). If a founding
  date is ever needed, flag the conflict explicitly instead of picking
  one.
- If sources conflict on any other figure, use the clearly verified
  figure or flag the uncertainty — never silently pick one side.

## 4. Dictation workflow

### 4.1 The two verbatim files (write FIRST, before drafting)

Both live under `dictations/riseup-asia-llc/`, dated 2026-11-05,
following the existing convention in `dictations/README.md` and the
existing files in that folder:

- `dictations/riseup-asia-llc/2026-11-05-us-software-dominance.md`
  — the user's dictated brief on US software dominance (giants
  NVIDIA/Microsoft/Apple/Google, rising AI players OpenAI/Anthropic
  with the cash-flow caveat, RISEUP ASIA LLC's engineering approach
  and market position). Source for article A1.
- `dictations/riseup-asia-llc/2026-11-05-software-franchise-model.md`
  — the user's dictated brief on the software franchise model and who
  dominates it now. Source for article A3.

Each file starts with the metadata header, exactly in the existing form:

```markdown
# Dictation — 2026-11-05

- **Date:** 2026-11-05
- **Dictated by:** Alim (user)
- **Intended outlet:** RISEUP ASIA blog
- **Status:** raw — not yet turned into an article
- **Topic:** <short topic line>

---

<verbatim transcript>

---

## Notes

- (notes appended here later — see §4.3)
```

### 4.2 Transcript rule

The transcript is NEVER edited. If the user corrects something, or the
writing process surfaces a fact-check problem, add a note to the
`## Notes` section at the bottom instead. This matches
`dictations/README.md` and the existing dictation files.

### 4.3 Link mechanism (defined by this spec — no existing format on file)

There is no pre-existing dictation↔article link format in this repo,
so this spec defines it. Both directions are mandatory:

1. Article → dictation: each article's `writing.md` ENDS with a
   "Source" note naming its dictation path, e.g.:

   ```markdown
   Source: dictated by Alim on 2026-11-05 — see
   dictations/riseup-asia-llc/2026-11-05-us-software-dominance.md.
   ```

   The same note appears in `medium-ready.html` (as the final
   paragraph) so the link survives the Medium copy-paste. The note
   does NOT count toward the area/brand keyword counts.
2. Dictation → article: once the article is drafted, append a
   "Turned into article" note to the dictation file's `## Notes`
   section (transcript untouched), e.g.:

   ```markdown
   - Turned into article: 01-seo-writing/03-software-engineering/04-new-york/who-dominates-us-software-2026/writing.md
   ```

   At the same time, update the dictation's `Status:` line from
   `raw — not yet turned into an article` to
   `turned into an article — see Notes`. The `Status:` line is
   metadata, not transcript, so updating it does not violate §4.2.

A2 has no dictation file and therefore no link in either direction.

## 5. Avatars

### 5.1 Dedicated folder

All 5 avatars go in their own folder (not mixed into the main avatars
pool):

- `assets/avatars/seo-articles-and-avatar-generation/`

### 5.2 The 5 personas (numbered 146-150, continuing the README table)

The avatars README table ends at persona 145 (Peter van Dam, Analyst),
so these are the next 5 numbers. Three female, two male, as requested.

| # | Name | Title | Gender | File |
|---|---|---|---|---|
| 146 | Iris Nakamura | SEO Writer | F | `iris-nakamura-seo-writer-white-with-noise.png` |
| 147 | Andre Baptiste | Technical Writer | M | `andre-baptiste-technical-writer-white-with-noise.png` |
| 148 | Clara Whitmore | Editor | F | `clara-whitmore-editor-white-with-noise.png` |
| 149 | Dmitri Sokolov | Blogger | M | `dmitri-sokolov-blogger-white-with-noise.png` |
| 150 | Tessa Marlowe | Copywriter | F | `tessa-marlowe-copywriter-white-with-noise.png` |

### 5.3 Batch-2 recipe (mandatory)

Follow the batch-2 recipe documented in `assets/avatars/README.md`:

- 1080×1080 PNG, chest-up framing with headroom (zoomed out, NOT the
  batch-1 close-up headshot).
- Bright high-key lighting.
- ~1% per-pixel film grain, so the portraits do not read as
  AI-generated.
- WHITE background only for this batch (no black variants).
- One image per persona — exactly 5 files, no extras, no variants.
- File naming: `<first>-<last>-<title-slug>-white-with-noise.png`
  (exactly as in the table in §5.2).

### 5.4 README table update

Append rows 146-150 to the table in `assets/avatars/README.md`, in the
later-batch single-file-column form (see rows 131-145):

```markdown
| 146 | Iris Nakamura | SEO Writer | `iris-nakamura-seo-writer-white-with-noise.png` |
| 147 | Andre Baptiste | Technical Writer | `andre-baptiste-technical-writer-white-with-noise.png` |
| 148 | Clara Whitmore | Editor | `clara-whitmore-editor-white-with-noise.png` |
| 149 | Dmitri Sokolov | Blogger | `dmitri-sokolov-blogger-white-with-noise.png` |
| 150 | Tessa Marlowe | Copywriter | `tessa-marlowe-copywriter-white-with-noise.png` |
```

Note the folder: the table lists file names; the new files live in
`assets/avatars/seo-articles-and-avatar-generation/` (see §5.1), so add
a one-line note above the new rows stating that folder.

### 5.5 Out of scope (explicit)

The 5 pre-existing modified avatar files in `assets/avatars/` are OUT
OF SCOPE. Do not touch, regenerate, rename, or re-commit them. This
task adds exactly 5 new files in the new folder, plus the README table
rows.

## 6. Per-article deliverables

Each article folder contains (per `01-seo-writing/seo-rules.md` §5,
which requires 3 infographics per story — this overrides the older
"at least 1" wording in `writing-preferences.md` §13):

- `writing.md` — the master article (with the §4.3 "Source" note at
  the end, where a dictation exists)
- `medium-ready.html` — rendered copy with live clickable links,
  identical title, paragraph order, wording, and link destinations
  to `writing.md`
- `<slug>.pdf` — PDF version of the article (FINAL step only — see §7)
- `infographic-1.png` + `infographic-1.svg`
- `infographic-2.png` + `infographic-2.svg`
- `infographic-3.png` + `infographic-3.svg`
  (each infographic contains the target keywords/area names as
  readable text; only short verified labels and numbers from the
  article or source material; visually inspected — record first-pass
  problems and final verification in `score.md`)
- `infographic-philosophy.md` — the visual philosophy
- `score.md` — the completed scorecard, MUST total 100 per the
  8-check rubric in `seo-rules.md` §6 (area 20, focus keyword 10,
  brand 15, topic question 10, house structure + plain formatting 10,
  citations verified 2-3× 15, infographics contain keywords 10,
  HTML + PDF present 10; −5 per `[VERIFY]` placeholder left in text).
  Score below 100 → rewrite and re-score until 100. `score.md` also
  carries the `writing-preferences.md` §15 validation procedure
  evidence (parity check, reference counts, pronoun scan, sentence
  openings, transition percentage, number formatting, link checks,
  quotation checks, infographic QA).

## 7. Tooling and execution order

1. Dictations first (§4.1), verbatim, before any drafting.
2. Scaffold each article folder via GitMap only:
   `gitmap py 03-ai-scripts/seo-scaffold.py --group <group> --slug <slug> --title "<title>" --area "<area>" --keywords "<kw1,kw2>"`
   (scaffold creates `writing.md`, `medium-ready.html`, `score.md`,
   and `infographic-philosophy.md` skeletons; it NEVER writes PDF).
3. Write `writing.md` from the dictation (A1, A3) or company material
   (A2), following §3. Verify every citation 2-3× by re-fetching.
4. Generate `medium-ready.html` from the final wording; check parity
   with `writing.md` (title, paragraph order, wording, destinations).
5. Create the 3 infographics (PNG + SVG each) + `infographic-philosophy.md`;
   inspect-correct-reinspect, and record QA in `score.md`.
6. Score to 100 in `score.md`; rewrite until 100.
7. PDF LAST, via GitMap only:
   `gitmap py 03-ai-scripts/seo-pdf.py ...` (final step only, after
   the article text is final — regenerating the PDF after any text
   change).
8. Avatars (§5) — may run in parallel with article writing (disjoint
   files, no collision); README table update after the 5 files land.
9. Dictation link-back (§4.3, step 2) — after each dictation-sourced
   article is drafted.

## 8. Acceptance criteria

- [ ] Both dictation files exist verbatim under
  `dictations/riseup-asia-llc/`, dated 2026-11-05, with the §4.1
  metadata header; transcripts unedited.
- [ ] A1, A2, A3 folders exist at the §3 target paths with ALL §6
  deliverables present and correct.
- [ ] Each `score.md` totals 100 per the 8-check rubric; no
  `[VERIFY]` placeholder remains in any published text.
- [ ] Each article's area count is 30-40×, brand count 20-30×,
  focus keyword(s) 1-2× in the first paragraphs, at least one topic
  question, plain formatting, first-person voice, no `he`/`him`/`his`
  for Alim, company name always `RISEUP ASIA LLC`.
- [ ] Every RISEUP ASIA LLC metric is company-attributed (§3.4); no
  founding year appears anywhere.
- [ ] Article→dictation "Source" notes present (A1, A3) and
  dictation→article "Turned into article" notes + Status updates
  present (§4.3). A2 has no dictation link.
- [ ] Exactly 5 new avatar files in
  `assets/avatars/seo-articles-and-avatar-generation/`, batch-2
  recipe (§5.3), white background only, correct file names; README
  table rows 146-150 added.
- [ ] The 5 pre-existing modified avatar files untouched.
- [ ] No absolute paths or `file:///` URIs in any new or edited file;
  no `rg`/`grep`/`git grep`/`Select-String` used anywhere in the work.
- [ ] CI verified via `gitmap pe -t` until green (lead's step).
- [ ] Release ceremony (lead's step): minor version bump via
  `gitmap py 03-ai-scripts/37-bump-version.py -t minor -s "SEO Articles and Avatar Generation Task Completion"`
  — note: this path is given in the task brief; if the script is not
  found at that path, the lead records the discrepancy in
  `.ai-memory/ambiguity/` and uses the closest equivalent bump script
  rather than halting.

## 9. Slug collision check (done at spec time, 2026-11-05)

`gitmap find` returned no matches for `who-dominates-us-software-2026`,
`riseup-asia-engineering-edge`, or `software-franchise-model`, and none
of the existing article folders under `01-seo-writing/02-franchise/`,
`01-seo-writing/03-software-engineering/`, or
`01-seo-writing/05-riseup-asia-brand/` uses these slugs. All three
proposed slugs are finalized as-is. If a collision appears during
implementation (e.g. a parallel agent lands the same slug first),
append `-v2` to the colliding slug and record the change in the plan
file — do not overwrite the other article.

## 10. Explicit exclusions

- No E2E tests, no builds, no test-suite runs (not requested; see §2).
- No Medium publishing — `medium-ready.html` is copy-paste-ready
  delivery only. Publishing is a separate task.
- No unrequested articles: exactly A1, A2, A3. No extra dictations,
  no extra avatars, no extra article folders.
- No edits to any file outside this task's scope (other articles,
  other specs, the 5 pre-existing avatar files, the Lovable sync
  history). This spec file itself is owned by Spec Agent A only.

## 11. Release steps (lead agent)

1. Commit the task's files (grouped logically, no single-file
   commits) and push upstream (`gitmap cpf` / `gitmap push`).
2. Verify CI via `gitmap pe -t` until green.
3. Minor version bump release ceremony:
   `gitmap py 03-ai-scripts/37-bump-version.py -t minor -s "SEO Articles and Avatar Generation Task Completion"`
   (see the §8 note if the script path differs).
4. Never force-push, rebase, amend, or squash pushed commits (Lovable
   sync — see repo `AGENTS.md`).
