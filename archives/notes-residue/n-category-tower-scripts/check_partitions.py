# Origin: gitclones/integral_lattice/cat/check_partitions.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

from sage.all import Partitions
from src._sage_types import SageType, SageTypeChecks

P = Partitions()
print(f"Object: {P}")
print(f"Is Set: {SageTypeChecks.is_set(P)}")
print(f"Is Ring: {SageTypeChecks.is_ring(P)}")
print(f"Is Group: {SageTypeChecks.is_matrix_group(P)}") # or is_group locally if I could access it, but matrix_group is what is used.
print(f"Cardinality: {P.cardinality()}")

from src.utils.Cardinality import cardinality
c = cardinality(P)
print(f"Computed Cardinality: {c}")
