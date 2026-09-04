@AGENTS.md

## Claude Code specifics

- `SKILL.md` at the repository root is a valid Agent Skill. Its frontmatter
  (`name`, `description`, `version`) is load-bearing — keep `name` matching the
  repository directory name if the skill is installed by symlink.
- Before committing: `python3 scripts/validate.py`. It is what CI runs, and it
  catches broken links, missing files, stale generated output and drift in the
  24-section style architecture.
- Generated files — `styles/*/tokens.json`, `styles/*/tokens.tailwind.css`,
  `styles/index.json`, `design-taste.manifest.json` — are never hand-edited.
  Change the source, then run `scripts/gen_tokens.py` / `scripts/gen_manifest.py`.
