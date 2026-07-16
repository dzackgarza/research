r"""Synthetic algebra joins (issue #212, CP2).

The algebra nodes are synthetic deliverables: they must construct the
correct joins — an algebra is simultaneously a module over its scalars
and a multiplicative structure, an associative unital algebra is in
particular a ring — and compose into both rollup routes, without any
concrete parent invented merely to look exercised. Based and
finite-dimensional refinements arrive through Sage's standard axioms.
"""

from __future__ import annotations

from sage.all import QQ, ZZ
from sage.categories.algebras import Algebras as SageAlgebras
from sage.categories.magmatic_algebras import MagmaticAlgebras as SageMagmaticAlgebras

from sage_lattice_category_spike.objects.algebras import Algebras, MagmaticAlgebras
from sage_lattice_category_spike.objects.magmas import AdditiveMagmas, Magmas, Monoids
from sage_lattice_category_spike.objects.modules import Modules
from sage_lattice_category_spike.objects.scalars import Rings


def test_magmatic_algebras_join_the_module_and_multiplicative_branches():
    node = MagmaticAlgebras(ZZ)
    assert node.is_subcategory(SageMagmaticAlgebras(ZZ))
    assert node.is_subcategory(Modules(ZZ))
    assert node.is_subcategory(Magmas())
    assert node.is_subcategory(AdditiveMagmas())


def test_associative_unital_algebras_are_in_particular_rings():
    node = Algebras(ZZ)
    assert node.is_subcategory(SageAlgebras(ZZ))
    assert node.is_subcategory(MagmaticAlgebras(ZZ))
    assert node.is_subcategory(Rings())
    assert node.is_subcategory(Monoids())


def test_standard_refinements_arrive_through_sage_axioms():
    commutative = Algebras(QQ).Commutative()
    assert commutative.is_subcategory(Algebras(QQ))
    assert "Commutative" in commutative.axioms()

    based = Algebras(QQ).WithBasis()
    assert based.is_subcategory(Algebras(QQ))
    assert "WithBasis" in based.axioms()

    finite_dimensional = based.FiniteDimensional()
    assert finite_dimensional.is_subcategory(based)
    assert "FiniteDimensional" in finite_dimensional.axioms()
