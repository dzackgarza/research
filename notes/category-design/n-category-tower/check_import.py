# Origin: gitclones/integral_lattice/cat/check_import.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

try:
    from sage.groups.matrix_gps.matrix_group import MatrixGroup_generic
    print("Found MatrixGroup_generic in sage.groups.matrix_gps.matrix_group")
except ImportError:
    print("Not found in sage.groups.matrix_gps.matrix_group")

try:
    from sage.groups.group import Group
    print("Found Group in sage.groups.group")
except ImportError:
    print("Not found Group")
