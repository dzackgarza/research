#!/usr/bin/env bash
# Build the dependency graph of the numbered blocks into the render output, where the
# page dependency-graph.md reads it. A post-render step, so the registry that gives
# each block its printed number is the one this render wrote.
#
# Run by Quarto with the working directory at the project root and the output
# directory in QUARTO_PROJECT_OUTPUT_DIR. The script is scripts/docs_dependency_graph.py.
set -euo pipefail

out="${QUARTO_PROJECT_OUTPUT_DIR:?post-render step run outside Quarto}"
# .assets is writing/.assets, reached through a symlink; the repository is two levels up.
root="$(cd "$(dirname "$(readlink -f "$0")")/../.." && pwd)"

uv run --script "${root}/scripts/docs_dependency_graph.py" \
    --project . --registry ._htmlbook_xref.json --out "${out}/dependency-graph" 2>&1 |
    tail -n 1
