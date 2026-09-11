# Origin: gitclones/integral_lattice/cat/inspect_gl.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

from sage.all import *
from sage.groups.matrix_gps.linear import GL

G = GL(2, RR)
print("Type:", type(G))
print("MRO:", [c.__name__ for c in type(G).mro()])
print("Module:", type(G).__module__)
