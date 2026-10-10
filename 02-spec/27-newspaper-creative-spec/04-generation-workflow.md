# 04 — Generation Workflow

How to produce a new creative in this style — similar to the sample,
or better — without hand-drawing anything.

## The pipeline (3 steps)

### Step 1 — Background (AI)

Generate or reuse an empty texture. Do NOT ask the image model for any
text, logos, or layout — it will garble non-Latin scripts and misspell
Latin ones.

Prompt template (adapt the era/colour to taste):

> "A clean, empty vintage newspaper texture background, portrait
> orientation. Aged sepia newsprint paper with faint columns of blurred
> unreadable newsprint text texture, subtle paper grain, slightly darker
> vignette at the edges, warm beige-brown tones. No readable words, no
> headlines, no people, no logos — just the empty textured paper
> background."

Starter asset: `../../backgrounds/newsprint-texture-bg.png`.
Want a different mood? Regenerate with "dark charcoal broadsheet",
"cream modern newsprint", or "torn tabloid" variants — same prompt
skeleton.

### Step 2 — Type + ornaments (Figma or SVG, never AI)

1. Import the texture PNG as the bottom layer (`bg-texture`).
2. Set the five copy blocks (file `03`) as real text layers using the
   display/label faces from file `02`. Name layers
   `headline-brand`, `headline-role`, `label-salary`, `figure-salary`,
   `figure-bonus`, `cta-button`, `cta-text`.
3. Highlighter strokes: draw rough vector bands *behind* the text
   layers (`highlight-brand`, `highlight-role`, …). Slight rotation,
   uneven edges — or generate a few marker-stroke PNGs once and reuse.
4. Red underline under the money line (`accent-underline`).
5. Margin slashes/chevrons as stroke vectors (`ornament-*`).
6. CTA: black rough-edged rect + white text + yellow triangle
   (`cta-button`, `cta-text`, `cta-arrow`).

Because everything except the texture is vector, the same file
re-renders in any language by swapping the text layers — the layout,
highlights, and ornaments stay put.

### Step 3 — Export

- PNG at 2x for social posting; keep the Figma/SVG source as the
  editable master.
- File naming: `newspaper-<topic>-<lang>.png`,
  e.g. `newspaper-hiring-bn.png`, `newspaper-hiring-en.png`.

## Quality checklist

- [ ] No AI-generated text anywhere (zoom to 200% and check every glyph)
- [ ] Native numerals for the audience's script
- [ ] At most 4 highlighted phrases; red used exactly once
- [ ] Ink-on-paper contrast above 7:1 in the content column
- [ ] CTA names a place ("in the comments", "link in bio")
- [ ] Nothing touches — each block has breathing room

## Beating the sample

Ideas the sample leaves on the table:

- **Motion:** export the highlight strokes as a reveal animation for
  reels/Stories (stroke draws on, block by block).
- **Texture variants:** night-edition (dark broadsheet + cream type),
  single-column broadsheet for long-form announcements.
- **Modular ornaments:** a shared library of 6–8 marker strokes,
  slashes, and chevrons so every new creative takes minutes.
- **A/B the CTA:** "comment below" vs "link in bio" vs QR block —
  the sample only tries one.
