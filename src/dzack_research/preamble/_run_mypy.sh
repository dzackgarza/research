#!/usr/bin/env bash
# Usage: _run_mypy.sh <file.sage> [cache-dir]
#
# One file's type pass while iterating.  It runs the same preparse and the
# same mypy configuration the QC gates run; it is a narrower target, never a
# different check.
set -u
cd /home/dzack/research/src/dzack_research/preamble
TARGET="$1"
PY="${TARGET%.sage}.sage.py"
CACHE="${2:-/tmp/mypy-cache-$$}"
# mypy-global.ini sets `mypy_path = typings`, resolved relative to CWD -- which
# here has no typings/. The stub tree lives in the spike; MYPYPATH is absolute
# and is appended to mypy_path, so point it there. Without this every Sage noun
# resolves to Any and the whole type pass checks nothing.
export MYPYPATH=/home/dzack/research/computations/archives/sage_lattice_category_spike/typings
rm -f "$PY"
# `sage --preparse` is this project's preparser: src/sitecustomize.py installs
# it into every Sage process, so the CLI, the QC gates and this script all
# compile the same way. Hand-rolling the preparse here would be a second
# compiler to keep in step.
sage --preparse "$TARGET"
timeout 600 uvx --python 3.14 \
  --with-editable . \
  --with 'sage-lattice-category-spike @ file:///home/dzack/research/computations/archives/sage_lattice_category_spike' \
  --from mypy mypy --no-incremental --cache-dir="$CACHE" \
  --config-file /home/dzack/ai-review-ci/tool-configs/mypy-global.ini \
  "$PY" 2>&1 | grep -v 'sitecustomize\|ModuleNotFoundError\|unused section' | grep -E 'error:|Found ' | head -50
echo "EXIT=${PIPESTATUS[0]}"
