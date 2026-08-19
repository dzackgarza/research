# Origin: gitclones/integral_lattice/cat/check_rr_order.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

from sage.all import RR

print(f"Has order: {hasattr(RR, 'order')}")
if hasattr(RR, 'order'):
    try:
        print(f"Order: {RR.order()}")
    except Exception as e:
        print(f"Order error: {e}")
