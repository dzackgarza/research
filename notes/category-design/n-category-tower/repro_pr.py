# Origin: gitclones/integral_lattice/cat/repro_pr.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

from sage.all import PolynomialRing as PR_Factory
from sage.rings.polynomial.polynomial_ring import PolynomialRing_general as PR_Class
from sage.all import QQ

try:
    print("Trying PR Factory:")
    R = PR_Factory(QQ, "x")
    print("Factory success:", R)
except Exception as e:
    print("Factory failed:", e)

try:
    print("\nTrying PR Class:")
    R = PR_Class(QQ, "x", sparse=False) # Class might need more args or be abstract
    print("Class success:", R)
except Exception as e:
    print("Class failed:", e)
