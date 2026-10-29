# seo article workspace

this repository is a personal seo article workspace: proofread, rewritten personal articles with validated scores and one original infographic per article.

## folder structure

```text
01-seo-writing/
  writing-preferences.md        master writing instructions for every article
  <article-slug>/               one folder per article, named by its slug
    writing.md                  plain-text master article
    medium-ready.html           rendered copy with clickable links, ready to paste into medium
    score.md                    validation results, category scores, and verification tables
    infographic.png             original infographic for the article
    infographic-philosophy.md   the visual philosophy used to make the infographic
```

```text
assets/                         shared creative assets (images via git-lfs)
  avatars/                      author/writer avatar images
  backgrounds/                  reusable background plates, png + layered svg pairs
  concepts/
    originals/                  reference creatives, kept as found
    <name>-clean.png            brand-stripped reusable versions
    layered/                    figma-ready layered svg recreations of each concept
  components/                   reusable vector components (e.g. label-pill.svg)
```
## how a new article is made

1. a draft gets proofread and rewritten inside `01-seo-writing/<slug>/writing.md` following `writing-preferences.md` (personal tone, plain text, descriptive links, digit-formatted numbers).
2. the same final wording and paragraph order generate `medium-ready.html` with live descriptive links.
3. validation runs against `writing-preferences.md`, and `score.md` records the measured results and category scores.
4. an original `infographic.png` is created from `infographic-philosophy.md`, visually inspected, corrected, and reinspected.

## sample article

`01-seo-writing/its-been-a-crazy-wake-up-night/` is the working example: a personal wake-up-night story about the inventor and software architect behind riseup asia llc. the folder holds the scored writing, the medium-ready copy with descriptive links spread through the story, and an "engineered wonder" infographic built from the article's own verified numbers and its `infographic-philosophy.md`.

## why the infographic

every article includes at least 1 original infographic. it communicates the article's central idea visually rather than summarizing each paragraph, using only short verified labels and numbers from the article, and stays legible at full size and as a medium-width image. the reasoning behind each design lives in the article's `infographic-philosophy.md`.

## publishing

paste `medium-ready.html` into medium and the links carry over as clickable, descriptive anchors. for other platforms and the repackaging rules (canonical links, varied anchors, avoiding duplicate copy), see the "publication platforms for seo backlinks" section in `01-seo-writing/writing-preferences.md`.

## Memory

- .ai-memory/memory/readme.md
- .ai-memory/memory/learned/01-recent-session-2026-10-29.md
- .ai-memory/plans/readme.md
