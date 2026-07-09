r"""Issue #51 (milestone-2, #18): random example lattices with prescribed
invariants.

There is no "random lattice" type or category. Randomness generates
construction DATA -- a Gram matrix of prescribed signature -- and the ordinary
constructor ``Lattice`` routes that data into its EXISTING category by
refinement. A random ``SL(rank, ZZ)`` congruence ``A^T G A`` preserves the
signature of a random diagonal seed ``G`` by Sylvester's law of inertia (any
real invertible ``A``) and its determinant because ``det(A)^2 = 1``.

Generation is a pure data helper in ``algebra/`` (like ``named_gram``); the
lattice is built and refined by the existing language, never by a bespoke
``Random*`` constructor.
"""
from __future__ import annotations

from sage.all import ZZ
from sage.misc.randstate import set_random_seed

from sage_lattice_category_spike.algebra.arithmetic import (
    random_gram_of_determinant,
    random_gram_of_rank,
    random_gram_of_signature,
    random_unimodular_gram_of_signature,
)
from sage_lattice_category_spike.lattice_categories import Lattice, Lattices


def test_random_signature_gram_builds_a_lattice_of_that_signature():
    L = Lattice(random_gram_of_signature(3, 2, seed=0))
    assert L.signature_pair() == (3, 2)
    assert L.rank() == 5


def test_random_definite_gram_routes_into_the_definite_category():
    L = Lattice(random_gram_of_signature(4, 0, seed=0))
    assert L in Lattices(ZZ).Definite()


def test_random_indefinite_gram_routes_into_the_indefinite_category():
    L = Lattice(random_gram_of_signature(3, 2, seed=0))
    assert L in Lattices(ZZ).Indefinite()


def test_random_signature_gram_is_reproducible_under_seed():
    first = random_gram_of_signature(2, 3, seed=42)
    second = random_gram_of_signature(2, 3, seed=42)
    assert first == second


def test_random_unimodular_gram_builds_a_unimodular_lattice_of_that_signature():
    L = Lattice(random_unimodular_gram_of_signature(3, 1, seed=0))
    assert L.is_unimodular()
    assert L.signature_pair() == (3, 1)


def test_random_determinant_gram_builds_a_lattice_of_that_determinant():
    L = Lattice(random_gram_of_determinant(12, 3, seed=0))
    assert L.determinant() == 12
    assert L.rank() == 3


def test_random_rank_gram_builds_a_nondegenerate_lattice_of_that_rank():
    L = Lattice(random_gram_of_rank(5, seed=0))
    assert L.rank() == 5
    assert not L.is_degenerate()


def test_random_isotropic_gluing_yields_a_proper_overlattice_of_the_sublattice():
    # U(2) has discriminant group (Z/2)^2 with nontrivial isotropic subgroups;
    # gluing by one is a random proper overlattice that still contains U(2).
    sublattice = Lattice("U").twist(2)
    subgroup = sublattice.discriminant_group().random_isotropic_subgroup(seed=0)
    overlattice = sublattice.glue(list(subgroup.gens()))
    assert overlattice.rank() == sublattice.rank()
    assert sublattice.absolute_discriminant() % overlattice.absolute_discriminant() == 0
    assert overlattice.absolute_discriminant() < sublattice.absolute_discriminant()


def test_gram_generators_do_not_perturb_the_global_random_stream():
    # Library code must draw within a scope, never reseed the process-global
    # random state. Record a draw, call a generator (with an UNRELATED inner
    # seed), then draw again: the post-call draw must equal what the outer
    # stream would have produced with no call in between. Fails against the old
    # ``set_random_seed(seed)`` implementation, which leaks the inner seed into
    # the outer stream.
    generators = [
        lambda: random_gram_of_signature(3, 2, seed=101),
        lambda: random_unimodular_gram_of_signature(3, 1, seed=101),
        lambda: random_gram_of_determinant(12, 3, seed=101),
        lambda: random_gram_of_rank(4, seed=101),
    ]
    for draw_generator in generators:
        set_random_seed(20260710)
        before = ZZ.random_element(0, 10 ** 9)
        reference_after = ZZ.random_element(0, 10 ** 9)

        set_random_seed(20260710)
        before_again = ZZ.random_element(0, 10 ** 9)
        draw_generator()
        observed_after = ZZ.random_element(0, 10 ** 9)

        assert before == before_again
        assert observed_after == reference_after


def test_random_isotropic_subgroup_does_not_perturb_the_global_random_stream():
    form = Lattice("U").twist(2).discriminant_group()

    set_random_seed(20260710)
    before = ZZ.random_element(0, 10 ** 9)
    reference_after = ZZ.random_element(0, 10 ** 9)

    set_random_seed(20260710)
    before_again = ZZ.random_element(0, 10 ** 9)
    form.random_isotropic_subgroup(seed=101)
    observed_after = ZZ.random_element(0, 10 ** 9)

    assert before == before_again
    assert observed_after == reference_after
