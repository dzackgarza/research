# Origin: gitclones/integral_lattice/cat/check_order.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

from sage.all import *

S = Semigroups().example()
print(f"Semigroup: {S}")
print(f"Type: {type(S)}")
print(f"Has order: {hasattr(S, 'order')}")
if hasattr(S, 'order'):
    print(f"Order: {S.order()}")
    
G = Graph({0:[1]})
print(f"Graph: {G}")
print(f"Has order: {hasattr(G, 'order')}")
if hasattr(G, 'order'):
    print(f"Order: {G.order()}")
