# Component Patterns

How the 12 universal components are built — the style DNA defines their look,
this file defines their anatomy and states. Every style must cover all 12.

## Universal component checklist

For each component, a style DNA must specify: default state, hover, active,
focus-visible, disabled, and dark-mode variant.

| Component | Anatomy | State requirements |
|---|---|---|
| **Button** | label ± icon, padding 12/24, radius from tokens | hover, active, focus-visible ring, loading, disabled |
| **Card** | container + optional media + body + actions | hover elevation OR none (static), consistent radius |
| **Navbar** | logo · links (≤6) · CTA; sticky; mobile → overlay/burger | scrolled state, active link, focus states |
| **Input** | label above, placeholder ≠ label, helper + error slots | focus ring, error (color + text, not color alone), disabled |
| **Tabs** | list + panels, keyboard arrows, visible active indicator | active, hover, focus-visible, disabled |
| **Pricing card** | plan name · price · feature list · CTA; recommended plan visually anchored | highlight must survive grayscale |
| **Dashboard widget** | title · value · delta · sparkline (optional) | loading skeleton, empty, error states |
| **Modal** | overlay + panel, close button, ESC + click-out, focus trap | open/close animation per motion tokens |
| **Badge** | label, radius, semantic colors (info/success/warn/error) | readable in both themes |
| **Tooltip** | trigger + arrow + text, 4px gap, max 2 lines | show 300ms delay, hide instantly, touch = tap toggle |
| **Table** | header row, zebra OR lines (not both), numeric right-aligned | sortable headers, hover row, empty state |
| **Form** | groups with labels, logical tab order, inline validation after blur | submit disabled until valid OR forgiving validation |

## Rules

1. Anatomy is fixed; style changes skin only.
2. Every interactive component needs a visible `:focus-visible` style.
3. Error states never rely on color alone (icon + text).
4. Icon + label buttons beat icon-only; icon-only requires aria-label.
5. Component radius/spacing/shadow ALWAYS from style tokens.
