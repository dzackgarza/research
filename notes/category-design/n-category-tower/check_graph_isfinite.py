# Origin: gitclones/integral_lattice/cat/check_graph_isfinite.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

from sage.all import Graph, RR

def check(obj, name):
    print(f"--- {name} ---")
    print(f"Has is_finite: {hasattr(obj, 'is_finite')}")
    if hasattr(obj, 'is_finite'):
        try:
            print(f"is_finite(): {obj.is_finite()}")
        except Exception as e:
            print(f"is_finite error: {e}")

check(Graph({0:[1]}), "Graph")
check(RR, "RR")
