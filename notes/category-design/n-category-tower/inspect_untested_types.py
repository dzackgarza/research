# Origin: gitclones/integral_lattice/cat/inspect_untested_types.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

from sage.all import *
from src._sage_types import SageTypeChecks, SageType

def inspect(obj, name):
    print(f"--- {name} ---")
    print(f"Type: {type(obj)}")
    print(f"Is Set: {SageTypeChecks.is_set(obj)}")
    print(f"Is Ring: {SageTypeChecks.is_ring(obj)}")
    try:
        print(f"Is Matrix Group: {SageTypeChecks.is_matrix_group(obj)}")
    except:
        print("Is Matrix Group check failed")
    
    has_card = hasattr(obj, "cardinality")
    print(f"Has cardinality(): {has_card}")
    if has_card:
        try:
            print(f"Cardinality: {obj.cardinality()}")
        except Exception as e:
            print(f"Cardinality error: {e}")

    try:
        from src.utils.Cardinality import cardinality
        print(f"Computed Cardinality: {cardinality(obj)}")
    except Exception as e:
        print(f"Computed Cardinality error: {e}")

# Permutation Group
S3 = SymmetricGroup(3)
inspect(S3, "SymmetricGroup(3)")

# Vector Space
V = VectorSpace(QQ, 3)
inspect(V, "VectorSpace(QQ, 3)")

V_R = VectorSpace(RR, 2)
inspect(V_R, "VectorSpace(RR, 2)")

# Graph
G = Graph({0:[1,2], 1:[2]})
inspect(G, "Graph")

# Semigroup / Monoid (Finite)
S = Semigroups().example()
inspect(S, "Semigroup Example")

# Infinite Monoid (Free Monoid)
M = Monoids().example() # Usually FreeMonoid
inspect(M, "Monoid Example")

