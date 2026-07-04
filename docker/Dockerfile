# syntax=docker/dockerfile:1
# Official Orcho container image.
#
# Build:
#   docker build -t orcho docker/
#   docker build --build-arg ORCHO_VERSION=0.1.1 -t orcho:0.1.1 docker/
#
# Run (project mounted at /workspace, agent credentials at /agent-auth):
#   docker run --rm -it -v "$PWD":/workspace -v ~/.orcho-auth:/agent-auth orcho run <task>
#
# See README.md in this directory for the credential bootstrap recipe.

FROM python:3.12-slim-bookworm

ARG ORCHO_VERSION=
ARG NODE_MAJOR=22

# git powers worktree orchestration; node powers the agent CLIs.
# gnupg is only needed to install the nodesource key and is purged after.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates curl git gnupg openssh-client \
    && curl -fsSL "https://deb.nodesource.com/setup_${NODE_MAJOR}.x" | bash - \
    && apt-get install -y --no-install-recommends nodejs \
    && apt-get purge -y gnupg \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Agent CLIs. Deliberately unpinned: scheduled image rebuilds track vendor
# releases without a commit in this repo. npm itself is upgraded first so
# its bundled dependencies carry current security fixes.
RUN npm install -g npm@latest \
    && npm install -g \
        @anthropic-ai/claude-code \
        @openai/codex \
        @google/gemini-cli \
    && npm cache clean --force

# Orcho itself (umbrella package). Empty ORCHO_VERSION installs the latest
# release; CI passes an explicit version on release builds. pip is upgraded
# first so the installer in the image carries current security fixes.
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir "orcho${ORCHO_VERSION:+==${ORCHO_VERSION}}"

# Agent CLIs run non-interactively as root inside the container; claude
# requires this marker to accept that combination.
ENV IS_SANDBOX=1
# Marker so tooling inside the container can detect the official envelope.
ENV ORCHO_ENVELOPE=container

# Default Orcho workspace: run state and evidence land here, never inside
# the mounted project. Bind-mount this path to keep run history across
# containers; without a mount it is ephemeral.
ENV ORCHO_WORKSPACE=/orcho-workspace
RUN mkdir -p /orcho-workspace

WORKDIR /workspace

COPY entrypoint.sh /usr/local/bin/orcho-entrypoint
RUN chmod +x /usr/local/bin/orcho-entrypoint

ENTRYPOINT ["orcho-entrypoint"]
CMD ["orcho", "--help"]
