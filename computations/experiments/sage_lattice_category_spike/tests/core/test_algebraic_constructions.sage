r"""Algebraic constructions at their first valid categories (issue #213, CP3).

``R``-Mod is an abelian category: kernel, image, and cokernel exist for
EVERY morphism by contract, and are computed once from the matrix
presentation at the module level (``morphisms/constructions.py``). The
form-bearing lattice spellings delegate there and add no computation of
their own. The direct sum is a functor, so it acts on morphisms, not only
on objects. No same-named construction categories are invented: the typed
operations sit on the data they consume — a morphism or a pair of them.
"""

from __future__ import annotations

from sage.all import ZZ, matrix

from sage_lattice_category_spike.lattice_categories import Lattice
from sage_lattice_category_spike.morphisms import constructions


def _collapse_of_degenerate_rank_two():
    r"""A morphism with a genuine kernel: nondegenerate lattices admit only
    injective form-preserving maps, so the interesting source is degenerate —
    an A1 line plus a radical line, collapsing onto A1."""
    degenerate = Lattice(matrix(ZZ, [[-2, 0], [0, 0]]), label="A1-plus-radical")
    a1 = Lattice("A1")
    return degenerate.hom(matrix(ZZ, [[1, 0]]), codomain=a1), degenerate, a1


def _index_two_embedding():
    r"""A morphism with a finite nontrivial cokernel: multiplication by 2
    from the rescaled line ``(-8)`` into ``A1 = (-2)``, image of index 2."""
    doubled = Lattice(matrix(ZZ, [[-8]]), label="2A1-source")
    a1 = Lattice("A1")
    return doubled.hom(matrix(ZZ, [[2]]), codomain=a1), a1


def test_kernel_and_image_are_module_level_operations():
    collapse, degenerate, a1 = _collapse_of_degenerate_rank_two()

    kernel = constructions.kernel(collapse)
    assert kernel.rank() == 1
    assert kernel.ambient() == degenerate
    for generator in kernel.lattice().gens():
        assert collapse(kernel.inclusion()(generator)) == a1([0])

    image = constructions.image(collapse)
    assert image.ambient() == a1
    assert image.rank() == 1
    assert image.index() == 1


def test_cokernel_exists_for_every_morphism_and_measures_the_index():
    doubling, _ = _index_two_embedding()
    cokernel = constructions.cokernel(doubling)
    assert not cokernel.is_torsion_free()
    assert cokernel.cardinality() == 2
    assert cokernel.invariants() == (2,)

    collapse, _, _ = _collapse_of_degenerate_rank_two()
    surjective_cokernel = constructions.cokernel(collapse)
    assert surjective_cokernel.is_torsion_free()
    assert surjective_cokernel.cardinality() == 1


def test_the_image_inclusion_and_cokernel_compose_exactly():
    r"""Exactness at the codomain: the cokernel of ``f`` and the cokernel of
    its image inclusion are the same finitely generated module."""
    doubling, _ = _index_two_embedding()
    image_inclusion = constructions.image(doubling).inclusion()
    assert constructions.cokernel(doubling).invariants() == constructions.cokernel(image_inclusion).invariants()


def test_direct_sum_acts_on_morphisms_functorially():
    r"""The direct sum is a functor, not an object-only construction: it
    preserves identities and composition."""
    a2 = Lattice("A2")
    a1 = Lattice("A1")
    first, second = a2.isometry_group().gens()[:2]
    other = a1.identity_morphism()

    summed = constructions.direct_sum(first, other)
    assert summed.domain() == a2.direct_sum(a1)
    assert summed.codomain() == a2.direct_sum(a1)

    identity_sum = constructions.direct_sum(a2.identity_morphism(), other)
    assert identity_sum == a2.direct_sum(a1).identity_morphism()

    composed = constructions.direct_sum(second * first, other)
    assert composed == constructions.direct_sum(second, other) * constructions.direct_sum(first, other)


def test_direct_sum_of_morphisms_commutes_with_the_summand_embeddings():
    r"""Naturality of the embeddings: ``(f (+) g)`` restricted along a
    summand embedding is that summand's morphism followed by its embedding."""
    a2 = Lattice("A2")
    a1 = Lattice("A1")
    isometry = a2.isometry_group().gens()[0]
    other = a1.identity_morphism()

    _, into_first, into_second = a2.direct_sum_with_embeddings(a1)
    summed = constructions.direct_sum(isometry, other)
    assert summed * into_first == into_first * isometry
    assert summed * into_second == into_second * other


def test_the_morphism_direct_sum_spelling_delegates_to_the_construction():
    a2 = Lattice("A2")
    a1 = Lattice("A1")
    isometry = a2.isometry_group().gens()[0]
    other = a1.identity_morphism()
    assert isometry.direct_sum(other) == constructions.direct_sum(isometry, other)


def test_lattice_morphism_spellings_delegate_to_the_constructions():
    collapse, _, _ = _collapse_of_degenerate_rank_two()
    assert collapse.kernel() == constructions.kernel(collapse)
    assert collapse.image() == constructions.image(collapse)

    doubling, _ = _index_two_embedding()
    assert doubling.cokernel().invariants() == constructions.cokernel(doubling).invariants()
    assert doubling.image().cokernel().invariants() == constructions.cokernel(doubling).invariants()
