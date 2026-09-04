# 12 · Maximalism

**Overview:** More is more — but choreographed. Layered richness, pattern mixing, saturated color fields and dense ornament, all disciplined by a strict grid and a single dominant idea per screen. Controlled chaos: abundance in content, order in structure.

**Visual principles:** layered richness · pattern mixing · saturated color fields · ornamental density · oversized type · symmetry broken on purpose · chaos inside a grid.

## Typography
- **Recommended families (Google Fonts):** Display serif: Fraunces, Playfair Display, DM Serif Display. Grotesk: Archivo, Space Grotesk. Script/accent: Pacifico or Bungee (sparingly). Mono: Space Mono.
- **Pairing:** Fraunces Black (H1, SOFT optical axis high) + Archivo (H2–body) + Space Mono (labels/marquee strips).
- **Scale:** H1 72/0.95 (tight, oversized, may overlap imagery) · H2 44/50 · H3 30/38 · body 17/1.65 · small 14. Type is a graphic object: rotate, outline, fill with color, layer over patterns.
- **Body:** 17px, 1.65. Body stays calm — readability is the anchor that lets everything else go loud. Measure 60–65ch.
- **Mixing:** max 3 families per screen. Contrast by classification (serif × grotesk × mono), never by similar weights.
- **CSS:**
```css
h1 { font: 900 72px/0.95 'Fraunces'; letter-spacing: -0.02em; }
h1 .outline { color: transparent; -webkit-text-stroke: 2px var(--ink); }
body { font: 400 17px/1.65 'Archivo'; }
.stamp { font: 700 12px/1 'Space Mono'; letter-spacing: 0.12em; text-transform: uppercase; }
```
- **Typical mistakes:** all type loud (nothing is a headline); 5+ families; body text set in display serif; centered walls of decorated text; gradients on body text.

## Layout & Frames
- **Grid:** 12-col exists underneath — patterns, cards and type blocks snap to it. Density comes from filling cells, not abandoning the grid.
- **Spacing:** sections 80–96px apart (less air than minimalism, but never cramped). Inside sections, components pack tight (16–24px gaps).
- **Hero:** full-bleed collage or oversized type over pattern field; allow one rotated/overlapping element. Rule of controlled chaos: exactly ONE element may break the grid per section.
- **Frame patterns:** collage hero, tiled pattern bands, dense card mosaics (masonry), marquee/ticker strips, sticker clusters, editorial multi-column magazine sections.
- **Responsive:** mobile drops to single column but keeps pattern backgrounds; collage heroes become stacked layers (z-index), H1→40px; hide at most one decorative layer per section on small screens.

## Visual hierarchy
- First seen: the dominant visual (giant type or hero collage), then the ONE primary CTA (highest-contrast object on screen), then supporting layers. Density is ranked: every layer has a clear z-order; the eye must find the CTA in one scan despite ornament. If you must squint to find the button, reduce decorative layers by one.

## Color system
- **Light:** bg #FDF6EC (warm cream) · surface #FFFFFF · ink #1A0B2E (deep plum-black) · secondary #5C4A72 · border #1A0B2E (2px, always visible) · primary action #E8442E (vermilion) · accents: #FFB000 (marigold), #7B2FA0 (violet), #0FA3A3 (teal) — max 3 accents + primary per screen.
- **Dark:** bg #1A0B2E · surface #2A1745 · text #FDF6EC · border #FDF6EC · primary #FFB000.
- Rules: color fields (full-bleed section backgrounds in saturated hues) are structural, not decorative accents. Avoid: muddy desaturated palettes (reads broken, not rich), neon-on-neon without dark separators, more than 5 hues in one viewport.

## Components
- Buttons: chunky, 2px ink border, hard offset shadow (4px 4px 0 var(--ink)), 999px pill or 0-radius — pick one per system. Hover: shadow grows + element translates -2px.
- Cards: 2px border, hard shadow, patterned headers, sticker/label badges rotated -4°. Cards may differ in bg color but share border/shadow language.
- Navbar: thick top border bar or ticker strip; logo may be a badge. Inputs: 2px border, hard shadow on focus, label in stamp caps.
- Pricing: cards intentionally unequal (featured plan gets pattern bg + bigger shadow); "most popular" as a rotated sticker, not a ribbon.
- Badges: rotated stamps, zigzag/wavy borders. Modals: poster-like panels with header pattern band. Tables: thick header rule, zebra rows in alternating tints.
- Decoration budget: each component gets max 2 decorative devices (pattern + stamp, or rotation + hard shadow).

## Shape language
- Mixed on purpose but grouped: wavy/zigzag borders, stars, sunburst blobs, arches, stickers, halftone dots. Radius family: either 0 (posterpunk) or 999px/organic blobs — no in-between 8px defaults. Depth via hard offset shadows (never soft blurs — blur reads corporate here). Dashed borders and hand-drawn rules connect scattered elements.

## Visual direction
Fits: bold illustration, collage, pattern swatches (terrazzo, checkers, florals, halftone), stickers, marquee text, oversized product cutouts, retro print texture (subtle paper grain ok). Breaks cohesion: corporate stock photography, soft pastel minimal cards dropped into a loud page, photorealistic 3D renders, frosted glass.

## Motion & Interaction
Playful but short: hovers 200ms spring (scale 1.04 + shadow shift); reveals with slight rotation (-2°→0°) and translateY 24px/450ms; marquees at 60–80px/s, pause on hover; stickers wiggle 2° on hover. Parallax max 1 layer. `prefers-reduced-motion`: stop marquees, wiggles, parallax; keep opacity fades. Motion is garnish — never the reason the design works.

## When to use
Youth brands, music/events/festivals, food & beverage, fashion drops, creator brands, gaming, D2C with attitude, cultural institutions. Audience expects personality and energy; conversion benefits from memorability over trust-signals.

## When NOT to use
Fintech, healthcare, legal, B2B enterprise, dev tooling, government — abundance reads unserious and raises perceived risk. Also not for content-heavy dashboards where scanning speed beats delight.

## Do
- One dominant idea per screen; everything else supports it
- Fill the grid, keep the grid
- Max 3 fonts, contrast by classification
- Hard offset shadows, never soft blur
- One grid-breaking element per section, maximum
- Body text stays plain and readable
- Rank density: hero loudest, supporting layers quieter
- Pattern mixing with shared palette (patterns differ, colors repeat)

## Don't
- Loud everything — no typographic ranking
- Random chaos with no underlying grid
- Soft drop shadows or glassmorphism
- More than 5 hues in a viewport
- Decoration on body paragraphs
- Pattern behind pattern behind pattern (max 2 layers)
- Neon-on-neon without a dark separator
- Marquees that never pause or respect reduced motion

## Anti AI-slop (maximalism edition)
Slop here = randomness mistaken for richness: AI-gradient blobs, confetti emoji walls, five mismatched font-pair gradients, purple-blue mesh heroes with white glass cards. Also slop: "maximalism" that's just a dark SaaS page with neon text. Real maximalism has deliberate pattern families, repeated palette, and ranked density. Test: pick any ornament — can you name which pattern family it belongs to? If not, delete it.

## Good vs Bad examples
- **Good:** Gossip/collage editorial sites, Gucci campaign pages — dense patterns, oversized serif, saturated fields, all on strict grids with one idea per screen.
- **Bad:** landing with a pastel gradient blob, glass navbar, neon gradient headline, 4 font families, soft shadows, confetti emojis — every layer shouting, zero shared DNA, no grid underneath.
## 14 · Accessibility Notes
- Contrast targets: body 4.5:1, large text/UI 3:1 — verify every text/background pair in this style's palette.
- Focus states: thick, high-contrast outlines that survive background chaos — focus must be findable in noise.
- Motion: this style tempts toward everything animating always — in maximalism, ONE animated element reads stronger than ten; motion needs a spotlight, not a rave. Every animated surface needs a `prefers-reduced-motion` static fallback.
- Common a11y failure in this style: patterned backgrounds behind text — always put text on solid plates; busy-on-busy fails every contrast rule.

## 15 · Design Decisions Explained (why, not just what)
- **Why these fonts:** expressive display families (Unbounded, Archivo Expanded) + a disciplined text face — maximalism needs ONE calm voice amid the noise
- **Why this radius:** intentionally mixed: mixed radii per layer is part of the language (this is the exception to consistency) — but within one component, stay consistent
- **Why this density:** high is the point, but layers must have a hierarchy: background pattern → mid decoration → sharp foreground content
- **Signature move:** the ONE element that makes a page instantly recognizable as this style — use once per page, deliberately.
- **When to break the rules:** one zone of extreme minimalism (a plain white section) makes the maximalist rest hit harder — contrast is the real system
