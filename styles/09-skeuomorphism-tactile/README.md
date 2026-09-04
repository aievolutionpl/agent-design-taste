# 09 · Skeuomorphism Tactile

**Overview:** The modern revival — not 2008 leather-stitching iOS, but believable physical controls: dials, switches, knobs, faders, embossed buttons. Born from audio hardware UIs (Teenage Engineering, Ableton, pro-audio apps) and premium finance products. Surfaces feel machined; controls feel like they'd clunk.

**Visual principles:** believable depth from light logic (top-lit) · real affordances (ridges, dials, notches, knurled textures) · matte materials, not glass · restrained palette around one material (aluminum, dark plastic, brass accent) · controls look pressable, everything else recedes.

## Typography
- **Recommended families (Google Fonts):** Technical: Space Grotesk, IBM Plex Sans, Chivo Mono. Mono/labels: JetBrains Mono, IBM Plex Mono, Chivo Mono.
- **Pairing:** Space Grotesk (H1–H3, 500) + IBM Plex Sans (body) + JetBrains Mono (readouts, labels, values).
- **Scale:** H1 48/56 · H2 34/42 · H3 24/32 · H4 19/27 · body 16/1.6 · small 13/1.5.
- **Body:** 16px, line-height 1.6, measure 62ch. Readouts always mono with tabular numbers.
- **Uppercase:** engraved labels — 10–11px mono uppercase, +0.15em tracking, etched look (light text with dark text-shadow below on raised surfaces, inverse on recessed).
- **CSS:**
```css
h1 { font: 500 48px/1.15 'Space Grotesk'; letter-spacing: -0.01em; }
body { font: 400 16px/1.6 'IBM Plex Sans'; }
.readout { font: 500 28px/1 'JetBrains Mono'; font-variant-numeric: tabular-nums; }
.engraved { font: 500 10px/1 'JetBrains Mono'; letter-spacing: .15em; text-transform: uppercase;
  color: #9AA0A6; text-shadow: 0 1px 0 rgba(255,255,255,.4); }
```
- **Typical mistakes:** display serif or script faces (breaks the machined feel); centered round body type; neon readouts (readouts are etched or backlit amber/white, never rainbow).

## Layout & Frames
- **Grid:** panels, not freeform — 12-col, max-width 1160px, gutters 20px. Sections read as rack-mounted panels: surface with inset/recessed zones.
- **Spacing:** 8-base; panel padding 24–32px; sections 88–112px apart.
- **Hero:** split hero — copy left, physical device/control console right (the console is the product). Controls arranged like a real front panel: aligned rows, screw heads at corners optional.
- **Frame patterns:** panel hero, recessed-zone feature rows (each feature = a recessed well in one big panel), spec-sheet sections, CTA as a physical switch/button panel.
- **Responsive:** stack panel zones under 900px, controls keep min touch size 44px, H1→32px, drop decorative screws.

## Visual hierarchy
- First seen: the hero console (highest material contrast), then H1, then primary control (biggest knob/switch). Eye path: device → headline → one big control → specs. Readouts (numbers) pull secondarily — keep them few. One control per row; controls never compete.

## Color system
- **Light ("brushed aluminum"):** bg #E8E9EB · panel #F2F3F4 · well/inset #D7D9DC · text #1F2328 · secondary #5A6068 · primary action #2F6FED or hardware-orange #F25C05 · readout amber #FFB000 (backlit). Border = highlight/shadow pairs, not hairlines: `border-top:1px solid rgba(255,255,255,.8); border-bottom:1px solid rgba(0,0,0,.25)`.
- **Dark ("rack unit"):** bg #14161A · panel #1E2126 · well #0E1013 · text #E8EAED · secondary #9AA0A6 · primary same · amber readouts brighter. Material contrast from light direction, not hue shifts.
- Saturation low everywhere; color only as: one action hue + amber readouts + tiny LED status dots (green/amber/red, 6–8px, glowing). Avoid: pastels, gradients with hue changes (gradients here are light-on-material: gray→darker gray), rainbow LEDs.

## Components
Buttons: raised — 2–3px vertical gradient (#fff top edge → surface → dark bottom edge), press state inverts (inset, content shifts 1px). Knobs/dials: circular, radial tick marks, indicator line, rotate via drag (in CSS demos: static with position set); knurled edge via repeating-conic-gradient. Switches: track inset with well shadow, knob with strong drop shadow, slide 200ms with clunk easing `cubic-bezier(.2,.9,.3,1.2)`. Faders: recessed slot + raised thumb. Inputs: recessed wells — inset shadow `inset 0 2px 4px rgba(0,0,0,.25)`, value text mono. Cards/panels: material surface with 1px top highlight + bottom dark edge, 8–12px radius max. Navbar: matte bar, hairline separator, engraved logo. Tabs: physical toggle group. LED indicators: small glowing dots for status. Tables: spec-sheet style, mono numerals, hairline rows on recessed panel.

## Shape language
Radius 4–12px (machined, not puffy). Everything rectangular-precision; circles only for knobs and LEDs. Depth = light logic: top-lit always — top edges light, bottom edges dark, recessed areas invert this. Texture via subtle repeating gradients (brushed metal: repeating-linear-gradient 90deg, 1px alpha stripes) — barely visible, 3–4% opacity.

## Visual direction
Fits: product photography of hardware, engraved/etched iconography (thin, single weight), backlit displays, blueprint-style spec diagrams, subtle brushed/conductive textures. Breaks cohesion: pastel blobs, glassmorphism, clay puffs, hand-drawn illustration, colorful gradients, emoji.

## Motion & Interaction
Mechanical: fast travel, firm settle. 150–220ms, ease `cubic-bezier(.2,.9,.3,1.2)` for switches (slight overshoot = clunk), plain ease-out elsewhere. Hover: brightness +4%, no lift. Press: inset invert, 1px shift. Knob rotate: requestAnimationFrame drag, snap to notches (15° steps). `prefers-reduced-motion`: disable slide/rotate animation, jump states instantly. No parallax, no floating, nothing hovers in mid-air — physics here are rigid bodies.

## When to use
Audio/music software, DJ tools, podcast apps, hardware product landing pages, premium finance dashboards (trading terminals, "engine room" money apps), automotive interfaces, simulators, engineer-audience dev tools.

## When NOT to use
Content sites, fashion, wellness, kids products, corporate marketing pages — fake physicality adds cognitive load where warmth or clarity is needed. Never skeuomorph body text containers; controls only.

## Do
- One light source: top. Every shadow follows it
- Highlight/shadow edge pairs on every surface
- Monospace tabular numerals for readouts
- Engraved uppercase micro-labels (+0.15em)
- Controls ≥44px with real press states
- Status via LED dots, not colored banners
- Restrict to one material family per page

## Don't
- Leather, wood, stitching, paper textures (that's 2008, not the revival)
- Rainbow neon glows on everything
- Skeuomorph entire layouts — control zones only
- Gradients that change hue (material gradients are neutral)
- Large radii (16px+ reads toy-like, not machined)
- Round friendly fonts
- Decorative screws on every corner in a web layout

## Anti AI-slop (skeuomorphism edition)
Neon-glow "cyberpunk" dials, glass knobs, glowing purple rings, fake stitching, Instagram-filter wood — all slop. The revival is Industrial: Teenage Engineering / rack hardware / trading terminal, neutral materials, one action hue, amber readouts. If it looks like a 2009 iPhone app or a Vaporwave grid, redo it.

## Good vs Bad examples
- **Good:** a hardware synth product page — aluminum hero console with real dials and a master fader, engraved labels, amber VU readout, spec sheet in mono, one orange action button.
- **Bad:** dark landing with purple-glowing glass knobs, neon cyan rings, leather-textured header and stitching — five materials, zero light logic, 2008 costume party.
## 14 · Accessibility Notes
- Contrast targets: body 4.5:1, large text/UI 3:1 — verify every text/background pair in this style's palette.
- Focus states: physical controls already have affordance — add invisible-until-focus rings for keyboard users.
- Motion: this style tempts toward dials and levers animating on page load — controls should move only when operated. Every animated surface needs a `prefers-reduced-motion` static fallback.
- Common a11y failure in this style: real-world mimicry without semantics: a volume knob must still be a range input with aria — looks are decoration, roles are real.

## 15 · Design Decisions Explained (why, not just what)
- **Why these fonts:** era-appropriate faces (serif for vintage audio, industrial sans for hardware) — the material tells you the family
- **Why this radius:** material-driven: brushed metal = small radius, wooden/plastic = larger; inconsistency between materials is fine, within one material it isn't
- **Why this density:** controls need physical size — touch-sized knobs and switches cap density; this is an instrument panel, not a spreadsheet
- **Signature move:** the ONE element that makes a page instantly recognizable as this style — use once per page, deliberately.
- **When to break the rules:** let data display go flat/digital (LCD-style) inside the tactile frame — pure physical everything gets exhausting; contrast makes tactility pop
