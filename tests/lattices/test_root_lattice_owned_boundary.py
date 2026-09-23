from dzack_research.preamble.all import RootLattices




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
