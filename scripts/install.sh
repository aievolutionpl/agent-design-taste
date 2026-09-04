#!/usr/bin/env bash
# Install Agent Design Taste adapter files into the current project.
#
#   bash agent-design-taste/scripts/install.sh --agent claude
#   bash agent-design-taste/scripts/install.sh --agent all --dry-run
#
# Never overwrites an existing file without --force.
set -euo pipefail

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="${PWD}"
AGENT=""
FORCE=0
DRY=0

usage() {
  cat <<'USAGE'
Usage: install.sh --agent <name> [--target DIR] [--force] [--dry-run]

  --agent   claude | codex | cursor | windsurf | copilot | gemini | agents | all
  --target  project root to install into (default: current directory)
  --force   overwrite existing files
  --dry-run print the plan, change nothing
USAGE
}

while [ $# -gt 0 ]; do
  case "$1" in
    --agent)   AGENT="${2:-}"; shift 2 ;;
    --target)  TARGET="${2:-}"; shift 2 ;;
    --force)   FORCE=1; shift ;;
    --dry-run) DRY=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "unknown option: $1" >&2; usage; exit 2 ;;
  esac
done

[ -n "$AGENT" ] || { echo "error: --agent is required" >&2; usage; exit 2; }
[ -d "$TARGET" ] || { echo "error: target not a directory: $TARGET" >&2; exit 2; }

install_one() {
  src="$SKILL_DIR/adapters/$1"
  dst="$TARGET/$2"
  [ -f "$src" ] || { echo "  !! missing adapter: $src" >&2; return 1; }
  if [ -e "$dst" ] && [ "$FORCE" -eq 0 ]; then
    echo "  -- skip   $2 (exists; use --force to overwrite)"
    return 0
  fi
  if [ "$DRY" -eq 1 ]; then
    echo "  ++ would write $2"
    return 0
  fi
  mkdir -p "$(dirname "$dst")"
  cp "$src" "$dst"
  echo "  ++ wrote  $2"
}

echo "Agent Design Taste installer"
echo "  source: $SKILL_DIR"
echo "  target: $TARGET"
[ "$DRY" -eq 1 ] && echo "  mode:   dry run (nothing will be written)"
echo

case "$AGENT" in
  claude)   install_one "CLAUDE.md" "CLAUDE.md" ;;
  codex)    install_one "AGENTS.md" "AGENTS.md" ;;
  agents)   install_one "AGENTS.md" "AGENTS.md" ;;
  gemini)   install_one "GEMINI.md" "GEMINI.md" ;;
  cursor)   install_one "cursor/agent-design-taste.mdc" ".cursor/rules/agent-design-taste.mdc" ;;
  windsurf) install_one "windsurf/agent-design-taste.md" ".windsurf/rules/agent-design-taste.md" ;;
  copilot)  install_one "copilot/copilot-instructions.md" ".github/copilot-instructions.md" ;;
  all)
    install_one "AGENTS.md" "AGENTS.md"
    install_one "CLAUDE.md" "CLAUDE.md"
    install_one "GEMINI.md" "GEMINI.md"
    install_one "cursor/agent-design-taste.mdc" ".cursor/rules/agent-design-taste.mdc"
    install_one "windsurf/agent-design-taste.md" ".windsurf/rules/agent-design-taste.md"
    install_one "copilot/copilot-instructions.md" ".github/copilot-instructions.md"
    ;;
  *) echo "error: unknown agent '$AGENT'" >&2; usage; exit 2 ;;
esac

echo
if [ "$AGENT" = "claude" ] || [ "$AGENT" = "all" ]; then
  cat <<'NEXT'
Optional — register as a Claude Code skill (loads only when relevant):

  mkdir -p .claude/skills
  ln -s ../../agent-design-taste .claude/skills/agent-design-taste
NEXT
  echo
fi
cat <<'VERIFY'
Verify it worked — ask your agent, with no other context:

  "What file do you read first before changing UI here,
   and what are the canonical viewports?"

Correct answer: AGENT-BOOTSTRAP.md, and 1440 / 768 / 390 (390 = primary mobile).
VERIFY
