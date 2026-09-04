# 15 Expressive Kinetic Typography — ready prompts

## Codex
```
Build a single-file HTML landing page for "Pressform" (an independent
type foundry & print studio). Style: kinetic typography — the type IS
the interface. NO animation libraries (no GSAP/anime.js): vanilla CSS
keyframes/transitions + a small vanilla JS block only. Fonts: Fraunces
variable for display (animate font-variation-settings 'wght'/'SOFT'/
'WONK'), Inter 17px/1.6 body, Space Mono 12px uppercase labels.
Hero: one line of Fraunces at clamp(48px,9vw,96px) revealing with a
line-mask (translateY 100%→0, staggered 60ms), then the word "type"
inflates wght 560→800 on hover (400ms). Add a pausable-on-hover CSS
marquee band of studio words between sections (42s loop). Nav: purely
typographic 22px links that swap wght on hover — no pill buttons.
Palette: paper bg #FAF7F2, ink #14120E, ONE accent #E4572E used on the
kinetic word + CTA only. Hairline rules as section separators, radius
0. Sections: kinetic hero, typographic feature list (numbered 01–04,
rows inflate on hover), quiet manifesto section (static reading),
type-only pricing ($/$$/$$$ numbers count up once), marquee, footer.
MANDATORY fallbacks: prefers-reduced-motion renders everything in
final state with marquees stopped; content must be fully visible with
JS disabled (initial hidden states set in JS, not CSS).
```

## Claude
```
Design a kinetic-typography landing page for Pressform, an independent
type foundry. The words are the interface: hero headline in variable
Fraunces at ~90px spanning the viewport, one kinetic idea per viewport
— a line-mask reveal on load, a variable-axis (wght) response on hover,
then stillness so people can read. Animate ONLY display type; body
copy never moves. Support all vanilla: CSS transitions/keyframes plus
at most ~40 lines of vanilla JS (IntersectionObserver for scroll
reveals, count-up numbers, letter shuffle for one word). Inter for
body, Space Mono for labels. Paper #FAF7F2 / ink #14120E / one accent
#E4572E, high contrast, hairline rules, radius 0. Include a marquee
that pauses on hover. Deliver one self-contained HTML file. The
prefers-reduced-motion version must render the complete page in final
state (reveals done, marquee stopped, counters at final values), and
the no-JS version must show all content — set animation initial states
from JS, never in CSS.
```

## Lovable
```
Create a kinetic typography landing page for "Pressform" (independent
type foundry). Rules: no animation libraries, only CSS animations +
vanilla JS. Fraunces variable font for headings (hover animates
font-variation-settings wght 560→800), Inter body 17px, Space Mono
uppercase labels. Hero: giant headline with line-mask reveal, staggered
lines. Add: hover-inflating numbered feature rows, a CSS marquee band
(pauses on hover), count-up prices, typographic nav (no buttons).
Palette: bg #FAF7F2, text #14120E, accent #E4572E only. Radius 0,
hairline borders, generous 96px section spacing. IMPORTANT
accessibility: prefers-reduced-motion shows everything in final state,
and the page must be fully readable without JavaScript.
```

## v0
```
Landing page, style: expressive kinetic typography, NO animation
libraries. Override shadcn defaults: radius 0, shadows off, hairline
rules as separators, bg #FAF7F2, text #14120E, accent #E4572E on
interactive type only. Fonts: Fraunces variable (use
font-variation-settings, animate wght/SOFT on hover via CSS
transition), Inter body, Space Mono labels. Build a KineticText
component: line-mask reveal on mount (staggered translateY, runs
once), wght 560→800 hover inflation. Marquee component: infinite CSS
loop, pause on hover, stops under prefers-reduced-motion. Nav is pure
type (display face, wght swap on hover). Use IntersectionObserver +
CSS vars for scroll reveals; set hidden initial states in JS so the
page works with JS off. One kinetic effect per section; body text
never animates.
```