# 16 Terminal / Dev Dark — ready prompts

## Codex
```
Build a single-file HTML landing page for "tern" (an open-source CLI that
records, replays and diffs AI coding-agent runs). Style: Terminal / Dev
Dark — dark-native (<html data-theme="dark">), bg #0B0D0E, surface #131618,
code panels #0F1213, text #E7E9E6, secondary #949CA3, 1px hairlines #262B2F,
ONE accent #5BE08F (label #04140A) for the primary action and success marks
only. Fonts: JetBrains Mono 700 for H1/H2 (56px, -0.03em), JetBrains Mono
12px uppercase labels, IBM Plex Sans 16px/1.6 for paragraphs. Radius 4–8px,
no shadows. Hero: headline + the real install command in a code panel with
an accent "$", a blinking block caret and a copy button (this IS the CTA),
next to a real terminal session showing ✓/▲/✗ steps and a +/− diff.
Then: three joined step cells with a command each, a comparison table,
a dated changelog, one large sans manifesto sentence, closing command CTA,
status-bar footer. Code scrolls inside its block; the page never overflows
at 360px. No glitch, no typing animation, no gradients, no fake stats.
prefers-reduced-motion stops the caret.
```

## Claude
```
Design a Terminal / Dev Dark landing page for tern, a CLI that makes agent
runs replayable. The audience runs things before they believe them, so the
page's content must be real: an install command they can copy, a session
with exit codes, a changelog with dates. Mono (JetBrains Mono) for display,
labels and data; IBM Plex Sans for prose. Near-black, never #000; one
phosphor green #5BE08F reserved for actions and success. Hairlines instead
of shadows, sections divided by 1px rules. Signature move: the command line
as the hero CTA, once. Rule-break: one human sentence in large sans.
Deliver one self-contained HTML file, dark by default with a light token
set, reduced-motion reset, and visible 2px accent focus rings.
```

## Lovable
```
Create a Terminal / Dev Dark landing page for "tern" (CLI for replaying AI
agent runs). Rules: dark background #0B0D0E, text #E7E9E6, secondary
#949CA3, hairlines #262B2F, ONE green accent #5BE08F for the primary button
and success icons only. JetBrains Mono for headings and labels, IBM Plex
Sans for body. Radius 4–8px, no shadows, no gradients. Sections: hero with
copyable install command + real terminal session, 3 step cells with
commands, comparison table, changelog with dates, CTA with command, status
bar footer. No matrix rain, no typewriter effect, no neon glow.
```

## v0
```
Landing page, style: Terminal / Dev Dark. Override shadcn defaults: dark
theme default, background #0B0D0E, card #131618, border #262B2F, radius
6px, shadows OFF, primary = #5BE08F with #04140A foreground, used only on
the main action. Font: JetBrains Mono for headings, labels, code; IBM Plex
Sans for body. Hero = install command block (with copy button) + terminal
session card with ✓/✗ step rows and a diff. Then joined step cells,
comparison Table, changelog list, status-bar footer. Code blocks use
overflow-x:auto. No glow, no gradient orbs, no Lucide icon grid.
```
