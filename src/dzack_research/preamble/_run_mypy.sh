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
# here has no typings/. The stub tree lives at the repo root; MYPYPATH is
# absolute and is appended to mypy_path, so point it there. Without this every
# Sage noun resolves to Any and the whole type pass checks nothing.
export MYPYPATH=/home/dzack/research/typings
# Sage's own interpreter, which has sageparse on its path. `sage -python` is
# not available on this build either, so the venv's python is named directly.
SAGE_PYTHON="${SAGE_PYTHON:-/home/dzack/gitclones/sage-dev-allopts/.venv/bin/python}"
rm -f "$PY"
# The lowering is `sageparse.build.lower_file`, which is the compiler the QC
# gates and every Sage process use; hand-rolling the preparse here would be a
# second compiler to keep in step. It is called directly rather than through
# `sage --preparse`, because this machine's Sage CLI (sage.cli) has no such
# flag -- `sage: error: unrecognized arguments: --preparse`. Sage's own
# interpreter runs it, so the lowering is the same one the gates apply.
"$SAGE_PYTHON" -c '
import sys
from pathlib import Path
from sageparse.build import lower_file
lower_file(Path(sys.argv[1]), Path(sys.argv[2]))
' "$TARGET" "$PY"
timeout 600 uvx --python 3.14 \
  --with-editable . \
  --from mypy mypy --no-incremental --cache-dir="$CACHE" \
  --config-file /home/dzack/ai-review-ci/tool-configs/mypy-global.ini \
  "$PY" 2>&1 | grep -v 'sitecustomize\|ModuleNotFoundError\|unused section' | grep -E 'error:|Found ' | head -50
echo "EXIT=${PIPESTATUS[0]}"
