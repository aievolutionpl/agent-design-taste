# 11 · Editorial Magazine

**Overview:** The page reads like a printed feature: a serif display face with real editorial contrast, drop caps opening body text, pull quotes breaking the column, and an asymmetric layout where images and text overlap the grid with intent.

**Visual principles:** magazine typography · serif display + readable serif body · drop caps and pull quotes · asymmetric, editorial grid · photography-led storytelling · hairline rules like a broadsheet.

## Typography
- **Recommended families (Google Fonts):** Display serif: Fraunces, Playfair Display, Libre Caslon Text. Body serif: Source Serif 4, Newsreader, Lora. Sans for captions/UI: Inter. 
- **Pairing:** Fraunces (H1–H2, 500–600, optical size high) + Source Serif 4 (body) + Inter (captions, eyebrows, UI labels).
- **Scale:** H1 56/60 · H2 40/44 · H3 28/34 · H4 22/28 · H5 18/24 · H6 16/22 · body 18/1.7 · caption 13/1.4.
- **Body:** 18px serif, line-height 1.7, measure 60–65ch. First paragraph after a heading opens with a **drop cap** (3-line float).
- **Uppercase:** 11–12px sans eyebrows and kickers only (+0.14em), never the serif display.
- **CSS:**
```css
h1 { font: 600 56px/1.07 'Fraunces'; letter-spacing: -0.01em; }
body { font: 400 18px/1.7 'Source Serif 4'; }
.dropcap::first-letter { font: 600 64px/0.9 'Fraunces'; float: left; padding: 8px 12px 0 0; }
.kicker { font: 500 12px/1 'Inter'; letter-spacing: 0.14em; text-transform: uppercase; }
blockquote { font: 500 32px/1.3 'Fraunces'; font-style: italic; }
```
- **Typical mistakes:** display serif at small sizes; centered long-form body; drop cap on every paragraph; mixing three serifs; bold weights above 600 on display serif.

## Layout & Frames
- **Grid:** 12-col, max-width 1200px — but content deliberately breaks symmetry: 7/5 splits, offset image columns, wide pull quotes spanning 8 cols with the text wrapping below.
- **Spacing:** sections 80–120px apart; rules (1px hairlines) act as section dividers like magazine folios.
- **Hero:** magazine cover logic — kicker, huge serif headline over/above a full-bleed or large-cropped photo, deck (standfirst) in 20–22px serif italic, byline in sans.
- **Frame patterns:** cover hero with overlapping headline, asymmetric 7/5 feature sections, wide pull-quote interludes, image + caption ("Fig." or photographer credit) pairs, editorial footer with colophon.
- **Responsive:** asymmetric splits stack (image first), H1→34px, pull quotes become full-width, drop caps shrink to 2 lines.

## Visual hierarchy
- First seen: display headline, then hero photo, then deck. Eye path: kicker → headline → deck → drop-cap opening → pull quote → CTA. Serif contrast (light body vs. 600 display) does the ranking.

## Color system
- **Light:** bg #FDFBF7 (warm paper) · surface #F4EFE6 · text #1A1815 · secondary #6B6259 · border #E3DCD0 · primary action #1A1815 · accent #8C2F1B (deep editorial red / bordeaux — one only).
- **Dark:** bg #14110E · surface #1F1B16 · text #F2ECE2 · border #35302A · accent same.
- Warm paper neutrals plus one ink-red accent. Avoid: neon, cold blue-grays, gradients, more than one accent.

## Components
Buttons: rectangular with 2px radius, solid ink fill or outlined, serif label acceptable. Cards: paper-toned panels with hairline borders, no elevation. Navbar: thin masthead bar with hairline rules above and below, serif wordmark. Inputs: 1px border on paper bg, label in sans caps. Tabs: hairline underline. Pricing: editorial table, serif figures, hairline rows. Dashboards: rare — keep as ruled panels. Modals: paper panel, dim backdrop. Badges: small caps sans, outline. Pull quotes: 28–36px Fraunces italic, optional oversized quotation mark in accent. Captions: 13px Inter with em-dash or credit prefix.

## Shape language
Radius 0–4px — print-like. Hairlines over shadows; at most a soft paper shadow on overlapping images. Depth = overlap and crop, not elevation. Icons minimal or none — photography and rules carry the visuals.

## Visual direction
Fits: editorial and documentary photography, duotone treatment, film grain (subtle), no illustration-heavy fluff, no 3D. Breaks cohesion: gradients, glass, neon, emoji, rounded blob shapes.

## Motion & Interaction
Restrained: hover 150ms color shift or image scale 1.02, reveals fade 400ms once. `prefers-reduced-motion`: disable all. Motion should feel like a page turning, never like an app.

## When to use
Media, journalism, culture, publishing, travel, food & wine, fashion editorial, long-form product storytelling, newsletters. Audience expects depth and craft.

## When NOT to use
Dense SaaS dashboards, dev tools, gaming, fintech utilities — serif-led editorial slows scanning; grotesk systems serve those better.

## Do
- Drop cap on the opening paragraph
- Pull quotes at column-breaking widths
- Asymmetric 7/5 and offset layouts
- Serif display with a sans for captions/UI
- Warm paper background, ink text
- One deep-red accent, used like ink stamps
- Photographer/figure credits in 13px sans
- Hairline rules as section structure

## Don't
- Center long-form body text
- Drop caps on every paragraph
- Three type families or two serifs
- Neon or cold-gray palettes
- Glass cards or gradient text
- Sans-serif display headlines (that's Swiss, not editorial)
- Shadows where a hairline would do

## Anti AI-slop (editorial edition)
Gradient hero text, purple CTAs, glass nav, "Trusted by 10,000 readers" ticker walls — all slop. If it wouldn't survive a print proof, cut it.

## Good vs Bad examples
- **Good:** The New Yorker / Kinfolk web features — serif display, disciplined columns, pull quotes, warm paper, one accent.
- **Bad:** "editorial" landing with Playfair on a blue-purple gradient, glass cards and centered wall-of-text — magazine costume over template defaults.
## 14 · Accessibility Notes
- Contrast targets: body 4.5:1, large text/UI 3:1 — verify every text/background pair in this style's palette.
- Focus states: elegant but visible: 2px serif-weighted underline or outline that fits the typography.
- Motion: this style tempts toward smooth-scroll hijacking for 'reading experience' — reading flow belongs to the reader, never animate their scroll. Every animated surface needs a `prefers-reduced-motion` static fallback.
- Common a11y failure in this style: light gray serif body text at 15px — long-form needs 17px+, #333 minimum, 65-75ch measure.

## 15 · Design Decisions Explained (why, not just what)
- **Why these fonts:** serif display (Fraunces, Playfair) + readable text serif/sans pairing — the pairing carries literary authority; two sans-serifs is not editorial
- **Why this radius:** 0-2px: print has no radius; images are sharp rectangles like magazine plates
- **Why this density:** high text density with dramatic whitespace alternation — dense column next to full-page image is the magazine rhythm
- **Signature move:** the ONE element that makes a page instantly recognizable as this style — use once per page, deliberately.
- **When to break the rules:** contemporary editorials mix in one grotesk element (labels, data) — pure serif-only pages feel costume-like; the mix IS modern editorial
