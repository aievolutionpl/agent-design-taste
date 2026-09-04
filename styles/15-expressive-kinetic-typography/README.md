# 15 · Expressive Kinetic Typography

**Overview:** The type IS the interface. Words move, stretch, react and navigate — headlines tick like departure boards, variable font axes respond to cursor and scroll, and navigation can literally be typography. No animation libraries: pure CSS transitions/keyframes plus a small vanilla JS toolkit.

**Visual principles:** type as interface · variable-font axes (wght/wdth/opsz/SOFT) as material · motion with meaning · rhythm and repetition of words · one kinetic idea per screen · content remains readable without JS.

## Typography
- **Recommended families (Google Fonts):** Variable display: Fraunces (SOFT/WONK/opsz — the most expressive on Google Fonts), Anybody (wdth), Bricolage Grotesque (wdth/opsz). Text: Inter, Instrument Sans. Mono: Space Mono, IBM Plex Mono.
- **Pairing:** Fraunces variable (H1, `font-variation-settings` experiments) + Inter (body) + Space Mono (labels/ticker).
- **Scale:** H1 64–96px (kinetic type wants BIG; clamp to viewport) · H2 42/48 · H3 26/34 · body 17/1.6 · small 14/1.5 · ticker/labels 12–14px mono.
- **Body:** 17px, line-height 1.6 — never animate body copy; kinetic energy is spent on display type only. Measure 60ch.
- **CSS:**
```css
h1 { font: 600 clamp(48px, 9vw, 96px)/1.02 'Fraunces'; font-variation-settings: 'SOFT' 0, 'WONK' 1; letter-spacing: -0.02em; }
.kin { font-variation-settings: 'wght' var(--w, 600), 'SOFT' var(--s, 0); transition: font-variation-settings 400ms cubic-bezier(.16,1,.3,1); }
body { font: 400 17px/1.6 'Inter'; }
.ticker { font: 400 12px/1 'Space Mono'; letter-spacing: .14em; text-transform: uppercase; }
```
- **Typical mistakes:** animating paragraphs; 5 fonts + 5 animation styles at once; letterspacing +0.5em "for effect" on body; variable axes animated at 30fps jank (always transition, or rAF-lerp).

## Layout & Frames
- **Grid:** type-driven asymmetric layout — oversized display type breaks the 12-col grid deliberately; supporting content sits in a disciplined 1200px container.
- **Hero:** a full-viewport typographic composition — one line of display type, 80–90% of viewport width, doing the kinetic work. Supporting visuals optional; never compete.
- **Frame patterns:** kinetic hero (line-by-line mask reveal, word ticker, hover-weight headline), typographic feature list (numbered lines that inflate on hover), marquee band between sections, typographic pricing (numbers count up), type-only footer.
- **Sections:** 96–120px apart; alternating "loud" (kinetic) and "quiet" (static reading) sections — the ear needs silence too.
- **Responsive:** H1 clamps via `clamp()`; marquees slow down; hover-only kinetics degrade to scroll-triggered or static. No kinetic type below 14px.

## Visual hierarchy
- First seen: the moving headline — motion is the strongest hierarchy tool, so spend it only on the thing that matters (usually H1 or the CTA word). Static hierarchy must survive with motion frozen: if the layout only makes sense while animating, redesign.

## Color system
- **Light:** bg #FAF7F2 (paper) · surface #FFFFFF · text #14120E · secondary #6B675F · border #E8E3DA · primary action #14120E · accent #E4572E (one hot color, on the moving word / CTA).
- **Dark:** bg #0D0C0A · surface #171512 · text #F5F1E8 · secondary #9B968B · border #262320 · accent #FF6B3D. High contrast is non-negotiable — motion + low contrast = illegible.
- Type may invert (knockout: bg-colored text inside a filled block). Avoid: gradient text everywhere, more than one accent, neon on paper bg.

## Components
Buttons: words behave as buttons — the CTA can be plain underlined text that inflates (font-variation wght 400→700) with an arrow that slides; also allow solid blocks. Nav: typographic — links set in display face at 20–24px, hover swaps weight or shows a filled underline wipe; no pill buttons. Marquee: infinite word band, 30–60s loop, pauses on hover. Cards: minimal frames or none — a rule (hairline) + big word is the card. Inputs: big typographic inputs (28px+). Badges: mono uppercase. Tickers/status: mono 12px. Never: kinetic dropdown menus, animated error messages, moving body links.

## Shape language
Shape is typographic: rules (hairlines), filled blocks behind inverted text, marquees as separators. Radius 0 (blocks) — roundness fights letterforms. No drop shadows on type; if a word needs weight, change the axis.

## Visual direction
Fits: huge variable type, hairline rules, marquee bands, index numbers (01–09), occasional soft solid shapes behind type, film-grain at ≤4% opacity. Breaks cohesion: photos competing with the hero type, 3D/parallax scenes (that's style 14), emoji in headlines, animated borders.

## Motion & Interaction
Signature moves (all vanilla): line-mask reveals (translateY 100%→0 inside overflow:hidden parents, stagger 60ms/line); variable-axis hover (word wght 400→750, 400ms); departure-board letter shuffle (JS swaps chars for 300–500ms then settles); scroll-driven axis change (wght rises as headline enters viewport, via IntersectionObserver + CSS var); infinite marquee; number count-up. Durations: reveals 600–800ms, hover 200–400ms, easings `cubic-bezier(.16,1,.3,1)` / steps() for board shuffle. **Fallbacks are mandatory:** `prefers-reduced-motion` → all reveals render final-state, marquees stop (show first phrase), axis changes become instant, counters show final numbers; no-JS → content fully visible (never hide lines behind JS-applied animation classes; set initial state in JS, not CSS). One kinetic idea per viewport; everything else static.

## When to use
Creative portfolios, studios, events/festivals, music/culture, fashion, editorial, agency sites, brand campaigns — anywhere the words themselves are the product. Great on one-pagers.

## When NOT to use
Docs, dashboards, banking/insurance, e-commerce checkout, healthcare, anything data-dense or trust-first — moving type reads as instability. Also not for i18n-heavy UIs (variable fonts with extreme axes can hurt legibility across scripts).

## Do
- One kinetic idea per viewport
- Animate only display type; body copy stays still
- Use variable axes as the main expressive material
- Set initial visible state in CSS/HTML; add motion in JS
- High contrast, always
- Alternate loud kinetic sections with quiet reading sections
- Ship the reduced-motion + no-JS versions deliberately
- Big type: the hero line should span the viewport

## Don't
- Animate paragraphs, prices while user reads, or nav dropdowns
- Five animation techniques on one page
- Motion that hides or moves content the user is trying to read
- Decorative letter-by-letter chaos
- Gradient text + animation + italic (pick one voice)
- Kinetic type for critical info (legal, checkout, errors)
- Fake variable fonts (animating font-weight on non-variable families = reflow jank)
- Autoplaying loud marquees that can't be paused

## Anti AI-slop (kinetic typography edition)
Every headline letter bouncing on load, scroll-triggered word fireworks on every section, `mix-blend-mode` rainbow headlines on every page, marquees of meaningless buzzwords ("INNOVATION · SYNERGY · DISRUPT"), kinetic type over unreadable video, GSAP-on-everything pages. Slop = motion without typographic intent.

## Good vs Bad examples
- **Good:** a studio hero where "Studio" inflates from wght 300→800 as you move the cursor across it, lines reveal once with a mask, then everything sits still and lets you read.
- **Bad:** a landing where every headline shuffles letters like a slot machine, the marquee never pauses, body text fades in letter-by-letter, and nothing is readable under reduced-motion — the fallback shows an empty page.