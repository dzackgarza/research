# Origin: gitclones/integral_lattice/cat/repro_nf.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

from sage.all import NumberField as NF_Factory
from sage.rings.number_field.number_field_base import NumberField as NF_Class
from sage.all import QQ, PolynomialRing

x = PolynomialRing(QQ, "x").gen()
try:
    print("Trying Factory:")
    K = NF_Factory(x**2 - 2, "a")
    print("Factory success:", K)
except Exception as e:
    print("Factory failed:", e)

try:
    print("\nTrying Class:")
    K = NF_Class(x**2 - 2, "a")
    print("Class success:", K)
except Exception as e:
    print("Class failed:", e)
