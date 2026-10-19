#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

docker run --rm -it \
  -v "${ROOT}:/docs" \
  -w /docs \
  --entrypoint sh \
  squidfunk/mkdocs-material \
  -c 'pip install -r requirements.txt && mkdocs build'
