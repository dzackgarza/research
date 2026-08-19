# Origin: gitclones/integral_lattice/cat/check_new_types.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

from sage.all import SymmetricGroup, Monoids, Infinity

def inspect(obj, name):
    print(f"--- {name} ---")
    print(f"Type: {type(obj)}")
    print(f"Has cardinality: {hasattr(obj, 'cardinality')}")
    print(f"Has order: {hasattr(obj, 'order')}")
    if hasattr(obj, 'cardinality'):
         try:
             print(f"cardinality(): {obj.cardinality()}")
         except Exception as e:
             print(f"cardinality error: {e}")
    if hasattr(obj, 'order'):
         try:
             print(f"order(): {obj.order()}")
         except Exception as e:
             print(f"order error: {e}")

inspect(SymmetricGroup(3), "SymmetricGroup(3)")
try:
    M = Monoids().example()
    inspect(M, "Monoid Example (FreeMonoid)")
except Exception as e:
    print(f"Monoid example error: {e}")
