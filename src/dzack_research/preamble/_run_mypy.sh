#!/usr/bin/env bash
# Usage: _run_mypy.sh <file.sage> [cache-dir]
set -u
cd /home/dzack/research/src/dzack_research/preamble
TARGET="$1"
PY="${TARGET%.sage}.sage.py"
CACHE="${2:-/tmp/mypy-cache-$$}"
# mypy-global.ini sets `mypy_path = typings`, resolved relative to CWD -- which
# here has no typings/. The stub tree lives in the spike; MYPYPATH is absolute
# and is appended to mypy_path, so point it there. Without this every Sage noun
# resolves to Any and the whole type pass checks nothing.
export MYPYPATH=/home/dzack/research/computations/experiments/sage_lattice_category_spike/typings
rm -f "$PY"
# The project's own preparser, not `sage --preparse`. The native one is what
# the repo's pinned regressions exist to work around -- it mangles integer
# literals inside match/case patterns (`case -1:` -> `case -_sage_const_1:`,
# invalid pattern syntax), so files using them cannot be checked at all.
sage -python -c "
import sys, pathlib
from dzack_research.preamble.preparser import preparse_file
source = pathlib.Path(sys.argv[1])
pathlib.Path(sys.argv[2]).write_text(preparse_file(source.read_text()))
" "$TARGET" "$PY" 2>/dev/null
timeout 600 uvx --python 3.14 \
  --with-editable . \
  --with 'sage-lattice-category-spike @ file:///home/dzack/research/computations/experiments/sage_lattice_category_spike' \
  --from mypy mypy --no-incremental --cache-dir="$CACHE" \
  --config-file /home/dzack/ai-review-ci/tool-configs/mypy-global.ini \
  "$PY" 2>&1 | grep -v 'sitecustomize\|ModuleNotFoundError\|unused section' | grep -E 'error:|Found ' | head -50
echo "EXIT=${PIPESTATUS[0]}"
