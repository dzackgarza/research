# Origin: gitclones/integral_lattice/cat/check_rr_crash.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

from sage.all import RR, GF, Zp, ZZ

def verify(obj, name):
    print(f"--- {name} ---")
    has_card = hasattr(obj, "cardinality")
    has_isfin = hasattr(obj, "is_finite")
    print(f"Has cardinality: {has_card}")
    print(f"Has is_finite: {has_isfin}")
    
    if has_isfin:
        try:
            print(f"is_finite: {obj.is_finite()}")
        except Exception as e:
             print(f"is_finite error: {e}")
             
    if has_card:
        try:
             print(f"cardinality(): {obj.cardinality()}")
        except Exception as e:
             print(f"cardinality error: {e}")

verify(RR, "RR")
verify(GF(7), "GF(7)")
verify(Zp(5), "Zp(5)")
verify(ZZ, "ZZ")
