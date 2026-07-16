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

from sage.categories.sets_cat import Sets as SageSets

from sage_lattice_category_spike.lattice_categories import Lattice
from sage_lattice_category_spike.morphisms import constructions
from sage_lattice_category_spike.objects.cardinals import Cardinal, aleph0
from sage_lattice_category_spike.objects.fundamental_sets import Integers
from sage_lattice_category_spike.objects.set_constructions import CartesianProduct
from sage_lattice_category_spike.objects.sets import Sets


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
    assert isinstance(cokernel.cardinality(), Cardinal)
    assert doubling.index() == 2  # classical scalar spelling of the same order
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


def test_the_lattice_direct_sum_is_the_module_theoretic_one():
    r"""A lattice is module data: ``(L, b)`` with ``b in Hom(L, L*)``, and
    ``(L1, b1) (+) (L2, b2) = (L1 (+) L2, b1 (+) b2)`` — nothing here is
    form-specific. Executable witness: the summed lattice's canonical map
    to its dual IS the direct sum of the summands' canonical maps, as a
    morphism identity (boundaries included), not a matrix coincidence."""
    a2 = Lattice("A2")
    a1 = Lattice("A1")
    summed_form = constructions.direct_sum(a2.dual_inclusion(), a1.dual_inclusion())
    assert summed_form == (a2 + a1).dual_inclusion()
    assert summed_form.domain() == (a2 + a1)
    assert summed_form.codomain() == (a2 + a1).dual()


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


def test_the_owned_cartesian_product_lives_in_the_standard_construction_category():
    r"""Integration, not invention: the owned product parent is a member of
    Sage's ``CartesianProducts()`` construction category — reached through
    the owned ``Sets()`` and agreeing with Sage's own node."""
    product = CartesianProduct(Integers(), Integers())
    assert product in Sets().CartesianProducts()
    assert product in SageSets().CartesianProducts()
    assert CartesianProduct() in Sets().CartesianProducts()
    assert product.cartesian_factors() == product.factors()


def test_the_cartesian_projections_answer_both_spellings():
    product = CartesianProduct(Integers(), Integers())
    point = product((ZZ(3), ZZ(-1)))
    assert product.cartesian_projection(0)(point) == ZZ(3)
    assert product.cartesian_projection(1)(point) == product.projection(1)(point)
