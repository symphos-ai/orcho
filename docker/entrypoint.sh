#!/bin/sh
# Bootstrap agent-CLI credentials, then exec the requested command.
#
# Mount a directory at /agent-auth (override with ORCHO_AGENT_AUTH_DIR)
# containing any of:
#
#   claude-credentials.json  -> installed to ~/.claude/.credentials.json
#   codex-auth.json          -> installed to ~/.codex/auth.json
#   gitconfig                -> installed to ~/.gitconfig
#
# Environment alternatives (used when the matching file is absent):
#
#   ANTHROPIC_API_KEY / CLAUDE_CODE_OAUTH_TOKEN  claude reads these directly
#   OPENAI_API_KEY                               written to ~/.codex/auth.json
#   GEMINI_API_KEY                               gemini reads this directly
#
# Credentials are copied (not symlinked) so the agent CLIs can rewrite them
# on token refresh without touching the mounted originals.
set -e

AUTH_DIR="${ORCHO_AGENT_AUTH_DIR:-/agent-auth}"

if [ -f "$AUTH_DIR/claude-credentials.json" ]; then
    mkdir -p "$HOME/.claude"
    cp "$AUTH_DIR/claude-credentials.json" "$HOME/.claude/.credentials.json"
    chmod 600 "$HOME/.claude/.credentials.json"
fi

if [ -f "$AUTH_DIR/codex-auth.json" ]; then
    mkdir -p "$HOME/.codex"
    cp "$AUTH_DIR/codex-auth.json" "$HOME/.codex/auth.json"
    chmod 600 "$HOME/.codex/auth.json"
elif [ -n "${OPENAI_API_KEY:-}" ] && [ ! -f "$HOME/.codex/auth.json" ]; then
    mkdir -p "$HOME/.codex"
    python -c 'import json, os; print(json.dumps({"OPENAI_API_KEY": os.environ["OPENAI_API_KEY"]}))' > "$HOME/.codex/auth.json"
    chmod 600 "$HOME/.codex/auth.json"
fi

if [ -f "$AUTH_DIR/gitconfig" ]; then
    cp "$AUTH_DIR/gitconfig" "$HOME/.gitconfig"
fi

# Delivery commits need a git identity; without one the run halts at the
# delivery step. Fall back to a container identity unless the operator
# provided a gitconfig or identity environment variables.
if [ ! -f "$HOME/.gitconfig" ] && [ -z "${GIT_AUTHOR_EMAIL:-}" ]; then
    git config --global user.name "Orcho Container"
    git config --global user.email "orcho@container.local"
fi

exec "$@"
