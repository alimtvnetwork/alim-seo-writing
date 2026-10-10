# 27 — Newspaper-Style Creative Spec

**Purpose:** A reusable design system for vintage newspaper-style recruitment /
announcement creatives, reverse-engineered from the Design Monks sample ad.
Use it to produce similar — or better — creatives in any language.

**Reference sample:** `sample-design-monks-ad.png` (kept in this folder).
**Reusable asset:** `../../backgrounds/newsprint-texture-bg.png` — empty
aged-newsprint texture, no text, ready for overlay.

**Files in this spec:**

- `01-sample-inventory.md` — anatomy of the sample ad, element by element
- `02-design-system.md` — palette, typography, texture, ornaments
- `03-copy-formula.md` — the persuasive structure, in any language
- `04-generation-workflow.md` — how to produce new creatives (AI texture +
  real text overlay, Figma workflow, prompt templates)

**The one rule this whole spec rests on:** never let an AI image model render
the words. Image models garble Bengali, Arabic, and most non-Latin scripts.
Generate the *texture* with AI; set the *text* as real type in Figma or SVG.
