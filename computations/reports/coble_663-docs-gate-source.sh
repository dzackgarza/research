#!/usr/bin/env bash
# research#663: the book's source gate, run and recorded, with this issue's pages checked for findings.
#
# Usage, from a FULL worktree of main (the gate reads every page and needs the assets):
#   cp ~/.pandoc/bib/references.bib writing/.assets/references.bib
#   cp ~/.pandoc/templates/css/mathjax-macros.html writing/.assets/mathjax-macros.html
#   bash computations/reports/coble_663-docs-gate-source.sh
set -uo pipefail
python3 scripts/docs_check.py --source > /tmp/gate.txt 2>&1
status=$?
echo "docs_check --source exit status: $status"
echo "findings: $(grep -c '^  - ' /tmp/gate.txt)"
echo "--- findings naming this issue's pages (want none):"
grep -E 'heegner-line-and-the-coble|heegner-research-report|open-problems\.md|open-questions\.md' /tmp/gate.txt || echo "   none"
echo "--- the findings themselves:"
grep '^  - ' /tmp/gate.txt
rm -f /tmp/gate.txt
