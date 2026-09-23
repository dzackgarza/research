from dzack_research.preamble.all import ZZ, Lattices, RootLattices
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory


def test_root_lattices_are_an_owned_inhabited_semantic_category() -> None:
    category = RootLattices()
    witness = category.an_object()

    assert isinstance(category, OwnedCategory)
    assert witness in category
    assert witness is Lattices(ZZ)("A2")
    assert all(witness in super_category for super_category in category.super_categories())


def test_root_lattice_keeps_inherited_lattice_mor_and_automorphism_operations() -> None:
    lattice = RootLattices().an_object()
    identity = lattice.Aut().one()
    first, second = lattice.simple_roots()
    reflection = lattice.reflection(first)

    assert identity(first) == first
    assert reflection in lattice.Aut()
    assert reflection(first) == -first
    assert reflection(second) == first + second
    assert lattice.correlation_morphism().domain() is lattice
