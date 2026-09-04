# 13 · Y2K / Retrofuturism

**Chrome, bubble, optimism.**

## 01 · Overview

The future as imagined from 1999 — optimistic, glossy, bubbly. Chrome made of CSS gradients (never images), iridescent pastels, pill and bubble shapes, pixel-precise tech details. It believes technology is fun.

## 02 · Design philosophy

The optimism of 1998–2004 rendered in chrome, gloss and bubble geometry: iridescent gradients, starbursts, hard specular highlights, interfaces that look like hardware. Nostalgia is the mechanism; the era's belief that the future would be shiny is the message.

**Design decisions explained — why, not just what**

- **Why these fonts:** bubble/techno display (Orbitron-like, ultra-rounded) — Y2K type is nostalgic hardware UI; neutral grotesks kill the era
- **Why this radius:** extreme pills and bubbles (999px) plus blob shapes — Y2K never met a corner it liked
- **Why this density:** medium-high visual density with metallic shine stacking — but interactive content stays on solid 'screen' areas

## 03 · Visual principles

chrome & metallic sheen (CSS gradients only) · iridescence · bubble/pill geometry · retro-tech chrome (windows, bezels, LED dots) · optimistic pastels · glossy 3D-lite feel without 3D assets.

## 04 · Typography

- **Recommended families (Google Fonts):** Techno display: Orbitron, Michroma, Audiowide. Grotesk body: Space Grotesk. Mono/pixel: Space Mono, VT323 (display accents only).
- **Pairing:** Orbitron 700 (H1–H2, wide letter-spacing on labels) + Space Grotesk (H3–body) + Space Mono (data readouts, blinking-cursor labels).
- **Scale:** H1 56/1.05 · H2 38/44 · H3 26/34 · body 16/1.6 · small 13. Display headings get letter-spacing 0.02–0.06em (techy, airy); body stays neutral.
- **Body:** 16px, 1.6, measure 62ch. Contrast body's calm against glossy chrome headlines.
- **CSS:**
```css
h1 { font: 700 56px/1.05 'Orbitron'; letter-spacing: 0.03em;
     background: linear-gradient(180deg,#EAF6FF 0%,#9FB8CC 55%,#3A4A5C 100%);
     -webkit-background-clip: text; color: transparent; } /* chrome text */
body { font: 400 16px/1.6 'Space Grotesk'; }
.readout { font: 500 12px/1 'Space Mono'; letter-spacing: 0.14em; text-transform: uppercase; }
```
- **Typical mistakes:** VT323 for body text (unreadable); all-caps body; gradient text on paragraphs; more than one chromed headline per screen.

## 05 · Layout & grid

- **Grid:** 12-col, max-width 1200px, but panels float with big rounded radii (24–32px). Symmetry and centered heroes are welcome (Y2K loves front-facing optimism).
- **Spacing:** sections 96px; panels padded 28–40px with visible "bezel" padding (surface inside border = plastic shell).
- **Hero:** centered chrome headline over iridescent sky gradient + one bubble-shaped device/card cluster (a "device" = nested panel with dot-matrix header). Optional orbiting ring via CSS.
- **Frame patterns:** device panels, pill navigation bar, bubble feature triads, status-bar footer (LED dots + mono readout), capsule CTA bands, "window chrome" cards (title bar with 3 dots).

## 06 · Visual hierarchy

- First seen: chromed H1 or the bubble hero device, then the pill CTA (high-gloss capsule, strongest contrast), then supporting panels. Chrome gradients make headlines loud automatically — so supporting panels must stay matte: chrome is reserved for H1 and primary CTA only.

## 07 · Color system

- **Light:** bg #E8F1F8 (ice blue) · surface #FFFFFF · text #1B2A3A · secondary #5A7086 · border #B9CCDD · primary action #3B5BDB (electric blue) · accents: #C77DFF (lilac), #64E0D4 (aqua), #FFB8D1 (bubble pink).
- **Iridescent surfaces (the signature):** soft multi-stop gradients across pastel hues:
```css
--iridescent: linear-gradient(135deg,#FFB8D1 0%,#E3D0FF 35%,#A8E8FF 65%,#B8FFE3 100%);
--chrome: linear-gradient(180deg,#F5FAFF 0%,#C6D6E4 30%,#6E8497 55%,#EAF2F8 75%,#8FA6B8 100%);
```
- **Dark:** bg #0E1626 · surface #1A2A44 · text #E8F1F8 · border #34507A · primary #7AA8FF · accents brighter versions; chrome gradient keeps its value range.
- Rules: iridescence = backgrounds and one CTA; chrome = text and thin bezels; both CSS gradients, zero image files. Avoid: muddy browns, flat matte-only palettes (kills the Y2K feel), neon green matrix vibes (that's hacker, not Y2K).

## 08 · Components

- Buttons: capsule/pill, chrome or iridescent fill, 1px light inner highlight (`box-shadow: inset 0 2px 2px rgb(255 255 255/.8), inset 0 -3px 4px rgb(0 0 0/.12)`), soft outer glow in primary color on hover.
- Cards: 24–32px radius, 1px border + bezel double-layer (outer border + inner surface with inset highlight), optional window-chrome header (3 dots + mono title).
- Navbar: floating pill nav (rounded-full container) or slim bar with LED status dots. Inputs: pill, inset shadow, mono placeholder. 
- Pricing: bubble cards, featured plan gets iridescent gradient border (double-background trick). Badges: pill chips, dot separators. Modals: device panel with title bar. Footer: status bar — LED dots, mono system readout, fake-signal bars (honest decoration).
- Everything plastic-glossy: every surface gets the inset highlight; nothing is dead flat.

Anatomy and the required state matrix (default / hover / focus-visible / active / disabled / loading / error / success) are universal — see `component-patterns/COMPONENT-PATTERNS.md`. This section defines the *skin*, not the behaviour.

## 09 · Shape language

- Radius 16px minimum, pills 999px, true bubbles (asymmetric border-radius blobs ok sparingly). Ellipses and rings, dot-matrix grids, dashed orbit circles. Depth via inset highlights + soft colored glows (NOT hard offset shadows, NOT heavy drop shadows). Beveled feel from double-layer surfaces.

## 10 · Imagery & visual direction

Fits: CSS-built chrome, iridescent gradient skies, dot matrices, pixel cursors, orb/ring decorations, translucent bubble panels, flip-phone-era device motifs, holographic foil accents. Breaks cohesion: real photography in chrome frames (unless product render), paper textures, grunge/brutalist elements, wooden/organic palettes, cyberpunk neon-on-black.

Per-style image direction table: `visual-language/VISUAL-LANGUAGE-FOUNDATIONS.md` § 10.

## 11 · Motion

Glossy & mechanical: hovers 200ms with glow bloom + slight scale (1.03); panels float with 6s ease-in-out bob (max 4px); shimmer sweep across chrome CTA every 4s; blinking cursor on readout labels (1s step). Reveals: translateY 20px + scale .98→1, 400ms. `prefers-reduced-motion`: stop bobbing, shimmer, blinking; keep opacity fades. Max 2 ambient animations on screen at once.

## 12 · Responsive behaviour

Verify at **1440 · 768 · 390** (canonical mobile) and once at **360** (narrow floor). Responsive means recomposition, not stacking — `responsive/RESPONSIVE-FOUNDATIONS.md`.

- **Adaptation:** pills stay; device panels stack; chrome H1 → 32px; bubble clusters become vertical stack; hide orbit decorations under 700px.
- **Non-negotiable for this style:** Pills and chrome stay. Orbit decorations, starbursts and secondary shine layers go below 700px.

## 13 · Accessibility

- Contrast targets: body 4.5:1, large text/UI 3:1 — verify every text/background pair in this style's palette.
- Focus states: chrome and iridescence swallow thin focus rings — bold dark outlines or inverted pills required.
- Motion: this style tempts toward looping shimmer/glow on everything — loop ONE hero element; shimmer fatigue is instant. Every animated surface needs a `prefers-reduced-motion` static fallback.
- Common a11y failure in this style: silver/chrome text on light backgrounds, white on iridescent gradients — chrome needs a dark backing plate to pass contrast.

The universal floor — contrast, focus, keyboard, semantics, motion, touch targets, zoom — is in `accessibility/ACCESSIBILITY.md`. This section covers what *this style specifically* gets wrong.

## 14 · When to use

Consumer tech, music/audio apps, fashion/beauty drops with tech edge, crypto-lite/fintech-for-consumers (careful), gaming casual, event sites, anything targeting audiences nostalgic for 1998–2008 or younger audiences that read Y2K as retro-cool.

## 15 · When NOT to use

Enterprise B2B, healthcare, legal, government, luxury (chrome reads toy-like), dense data dashboards, accessibility-first products where gloss reduces contrast discipline.

## 16 · Do

- Build chrome/iridescence with CSS gradients — never image files
- Reserve chrome for H1 + primary CTA; keep panels matte
- Pill everything: nav, buttons, badges, inputs
- Bezel double-layers: border outside, inset highlight inside
- Mono readout labels for the retro-tech detail
- Ice-blue/pastel base; accents in small glowing doses
- Max 2 ambient animations; pause them for reduced-motion
- Dark mode: keep chrome value range, deepen the sky

## 17 · Don't

- Chrome via embedded images or heavy textures
- Gradient text on body copy
- Hard offset shadows or brutalist borders
- Matrix-green hacker palette
- More than one chromed headline per screen
- Glassmorphism blur stacks (translucency yes, frosted blur no)
- Blinking/glowing everything at once
- Fake "loading…" spinners as decoration

## 18 · Anti-slop — Y2K edition

Slop here = purple-blue mesh gradient hero with white glass cards (that's generic AI SaaS, not Y2K), vaporwave aesthetic without craft, every surface glowing, VT323 walls of text, emoji 🌈✨ plastered as design. Also slop: 3D chrome renders stolen from tutorials instead of CSS-built sheen. Test: can every gradient be named (chrome? iridescent sky? glow?) — if a gradient is "just because", delete it. The era detail (dot matrices, readouts, bezels) must be precise, not sprinkled.

**Good vs bad**

- **Good:** early-2000s Sony/Nokia product pages reborn — chromed headlines, capsule navs, bezel panels, disciplined pastel skies with mono system readouts.
- **Bad:** dark page with neon green code rain, glass navbar, purple mesh blob and gradient button text — four trend fragments, zero 1999 optimism, unreadable contrast.

Universal severity levels (BLOCKER / STRONG / MINOR): `ANTI-SLOP.md`.

## 19 · Style combinations

One dominant + at most one supporting style. The supporting style owns exactly one layer — typography, one section type, or micro-motion — never structure.

- **Works with:** Maximalism (12) — chrome plus layered decoration
- **Avoid pairing with:** Minimalism (01) — nostalgia needs density · Swiss (10) — order versus chaos

Full rules: `STYLE-COMBINATIONS.md`.

## 20 · Signature move

**A chrome or iridescent element with a hard specular highlight, on a dark backing plate** — so the metal reads as metal and the text stays legible against it.

Use it **once per page**, deliberately. A signature move repeated on every element is no longer a signature.

## 21 · When to break the rules

one flat, modern, quiet section makes the retro zones read as intentional art direction instead of a costume

## 22 · Example prompts

Ready-to-paste prompts for Codex, Claude, Lovable and v0: [`prompts.md`](prompts.md)

## 23 · Design tokens

- [`tokens.css`](tokens.css) — **canonical.** If this file and the prose above disagree, the token wins.
- [`tokens.json`](tokens.json) — generated, for design tools and JS
- [`tokens.tailwind.css`](tokens.tailwind.css) — generated, Tailwind v4 `@theme`

Regenerate the two derived files with `python3 scripts/gen_tokens.py` after editing `tokens.css`.

## 24 · Example implementation

[`example.html`](example.html) — a single-file, zero-dependency page built strictly from this style's DNA and tokens. Open it in a browser.

It is **one valid interpretation, not a spec.** Copying it wholesale is how every page ends up identical — read it, then compose something else.
