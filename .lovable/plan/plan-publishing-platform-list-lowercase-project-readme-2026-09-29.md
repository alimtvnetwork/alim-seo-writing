# Plan: Publishing-platform list + lowercase project README

## Goal

1. Record the top free places (like Medium) to publish each article for SEO backlinks, inside `01-seo-writing/writing-preferences.md`.
2. Rewrite the root `README.md` to be a clean, all-lowercase guide to this repo's article workflow — with no Lovable marketing text.

## 1. Update `01-seo-writing/writing-preferences.md`

Add a new section: "Publication platforms for SEO backlinks".

Top free platforms to include, each with a one-line purpose note:

- Medium (primary; current workflow with medium-ready.html)
- LinkedIn Articles (professional reach, personal profile authority)
- Dev.to (developer audience, strong community, easy repost)
- Hashnode (developer blogging, custom domain on free plan)
- Substack (newsletter + archive pages)
- Tumblr (long-standing high-authority, free posts)
- WordPress.com free (classic blogging, own subdomain)
- Blogger / Blogspot (Google property, fast indexing)
- HubPages and Vocal Media (revenue-share article sites)
- DZone (tech article community)
- Write.as / WriteFreely (minimal, clean markdown publishing)
- Re-packaging tips: keep canonical link back to the main article, vary anchor wording, never paste identical copy everywhere (duplicate content), one paragraph teaser + link is acceptable.

Also note in the workflow: when the user asks to "publish/adapt" an article for another platform, generate a matching ready-to-paste file next to medium-ready.html (for example linkedin-ready.html, devto-ready.md) using the same verified wording and links.

## 2. Rewrite root `README.md`

Fully lowercase text. No Lovable branding or lovable.dev links — remove the existing "Built with Lovable" boilerplate entirely.

Contents:

- short intro: this repo is a personal SEO article workspace
- folder structure:

```text
01-seo-writing/
  writing-preferences.md        master writing instructions
  <article-slug>/               one folder per article
    writing.md                  plain-text master article
    medium-ready.html           rendered copy with clickable links for Medium
    score.md                    validation scores and verification tables
    infographic.png             original infographic for the article
    infographic-philosophy.md   visual philosophy behind the infographic
```

- how a new article is created: proofread and rewrite into a slug folder, then score, then infographic
- sample article section: `its-been-a-crazy-wake-up-night/` — wake-up-night story about the inventor and software architect, with the scored writing, medium-ready copy, and an "engineered wonder" infographic built from the article's own numbers and philosophy file
- why the infographic exists: one original visual per article, communicating the central idea with verified labels only; see infographic-philosophy.md
- publishing: paste medium-ready.html into Medium; adaptation rules for other platforms point back to writing-preferences.md

## Verification

- Read back the new README.md and the preferences section; confirm all-lowercase README and zero lovable.com/lovable.dev mentions.
- Confirm the folder-structure block matches the actual sample article folder contents.
- No other files changed.

## Notes

Platform notes are general guidance from current web research, not measured facts; they describe purpose and audience rather than guaranteed dofollow behavior, which each platform can change at any time.
