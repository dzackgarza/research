# Origin: gitclones/integral_lattice/cat/tests/test_finite_set.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

# from __future__ import annotations

# import pytest
# from src._types import BoolProof
# from src.abc.concrete.sets.finite_set import FiniteSet

# class TestFiniteSet:
#     """Tests for the FiniteSet concrete implementation."""

#     def test_construction_and_cardinality(self):
#         s = FiniteSet(frozenset([1, 2, 3]))
#         assert s.cardinality() == 3
#         # is_finite handled by SetObject_Base
#         assert s.is_finite().is_true()
#         assert not s.is_empty().is_true()
        
#         empty = FiniteSet(frozenset())
#         assert empty.cardinality() == 0
#         assert empty.is_empty().is_true()

#     def test_set_operations(self):
#         s1 = FiniteSet(frozenset([1, 2]))
#         s2 = FiniteSet(frozenset([2, 3]))
        
#         # Union
#         union = s1.union(s2)
#         assert union.cardinality() == 3
#         assert union.contains(1)
#         assert union.contains(2)
#         assert union.contains(3)
        
#         # Intersection
#         inter = s1.intersection(s2)
#         assert inter.cardinality() == 1
#         assert inter.contains(2)
        
#         # Difference
#         diff = s1.difference(s2)
#         assert diff.cardinality() == 1
#         assert diff.contains(1)
        
#         # Symmetric Difference (inherited)
#         sym_diff = s1.symmetric_difference(s2)
#         assert sym_diff.cardinality() == 2
#         assert sym_diff.contains(1)
#         assert sym_diff.contains(3)
#         assert not sym_diff.contains(2)

#     def test_predicates(self):
#         s1 = FiniteSet(frozenset([1, 2]))
#         s2 = FiniteSet(frozenset([1, 2, 3]))
        
#         assert s1.is_subset_of(s2).is_true()
#         # proper subset inherited
#         assert s1.is_proper_subset_of(s2).is_true()
#         # superset inherited
#         assert s2.is_superset_of(s1).is_true()
#         assert not s2.is_subset_of(s1).is_true()
        
#         s3 = FiniteSet(frozenset([4]))
#         # disjoint inherited
#         assert s1.is_disjoint_from(s3).is_true()

#     def test_functional_methods(self):
#         s = FiniteSet(frozenset([1, 2, 3, 4]))
        
#         # Map: x -> x^2
#         mapped = s.map(lambda x: x**2)
#         assert mapped.contains(1)
#         assert mapped.contains(4)
#         assert mapped.contains(9)
#         assert mapped.contains(16)

#         # Preimage: {x | x^2 in {4,16}} -> {2,4}
#         preim = s.preimage(lambda x: x**2, FiniteSet(frozenset([4, 16])))
#         assert preim.cardinality() == 2
#         assert preim.contains(2)
#         assert preim.contains(4)
        
#         # Filter: even numbers
#         filtered = s.filter(lambda x: x % 2 == 0)
#         assert filtered.cardinality() == 2
#         assert filtered.contains(2)
#         assert filtered.contains(4)
        
#         # Reduce: sum
#         total = s.reduce(lambda x, y: x + y, 0)
#         assert total == 10
        
#         # Quantifiers (inherited via iteration)
#         assert s.forall(lambda x: x > 0).is_true()
#         assert not s.forall(lambda x: x > 2).is_true()
#         assert s.exists(lambda x: x == 3).is_true()
#         assert not s.exists(lambda x: x == 5).is_true()

#     def test_relations_and_partitions(self):
#         s = FiniteSet(frozenset([1, 2, 3, 4]))
        
#         # Partition by parity: {1,3}, {2,4}
#         quotient = s.quotient_by_relation(lambda x, y: (x % 2) == (y % 2))
#         assert quotient.cardinality() == 2
        
#         # Check that we have the correct equivalence classes
#         classes = list(quotient) # uses __iter__
#         assert len(classes) == 2
        
#         # Partitions
#         small = FiniteSet(frozenset([1, 2]))
#         parts = list(small.partitions())
#         assert len(parts) == 2

#     def test_combinatorics(self):
#         s = FiniteSet(frozenset([1, 2, 3]))
        
#         # Subsets of size 2: {1,2}, {1,3}, {2,3} -> 3
#         subs2 = list(s.subsets_of_size(2))
#         assert len(subs2) == 3
        
#         # Partitions of size 2 for {1,2,3}: {{1,2},{3}}, {{1,3},{2}}, {{2,3},{1}} -> 3
#         parts2 = list(s.partitions_of_size(2))
#         assert len(parts2) == 3
