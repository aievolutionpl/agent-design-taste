# DESIGN.md — the visual contract pattern

When generating a project (v0, Lovable, Codex, Claude), don't keep design in
chat — **write a DESIGN.md at the project root** and treat it as binding.

## Why

- Chat context evaporates; the contract survives.
- Both browser builders and local agents read the same file.
- Consistency is auditable: "list every value that doesn't match a token".

## Template (compact, paste-first)

```markdown
# DESIGN.md — <project>
## Product
What / for whom / one key action:
## Style
Dominant: <style> + Supporting: <style or none>. Why: <audience fit>.
## Constraints (follow exactly, no exceptions)
- Surfaces: bg #…, card #…, border #…
- Text: primary #…, muted #…
- Action: #…, text-on-action #…
- Type: <family>. Display clamp(2.5rem, 8vw, 7rem)/600, heading 20/600, body 15-17/400
- Radius: cards Npx, controls Npx, pills 999px
- Borders 1px only. No gradients. No drop shadows. (adjust per style)
- Spacing scale: 4 8 12 16 24 32 48
## Anti-references ("Not like this")
- Not like <generic AI SaaS>: purple gradient, glass everywhere, 24px radius on everything
- Not like <other failure mode>
## Full tokens
See styles/<style>/tokens.css (copied below / linked).
```

## Workflow

1. **First message of any project** = create DESIGN.md, before any UI.
2. Instruct the builder: "Treat DESIGN.md as the visual contract — every
   component uses only its tokens for color, spacing, radius, type."
3. Re-paste the constraint block when starting a big new screen (chat memory
   fades).
4. Weekly audit prompt: "Audit every component against DESIGN.md. List each
   value that does not match a token, with file and line. Change nothing yet."
5. Consistency probe: render two unrelated screens, compare greys and radii.
   Divergence = the contract got diluted; re-paste it.

## Why anti-references matter

"Not like this" removes a region of the solution space; "like this" gestures
at a point. Always fill the Anti-references section.
