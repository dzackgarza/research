r"""Typed composition checks for the category's operations (V2 type fixture).

These functions are NEVER executed — every grammar stub raises — and this
module is not runtime code (it is not imported by the package). It exists so
the type checker exercises the LANGUAGE: each research-shaped workflow below
composes the protocol arrows, and an incoherent signature (an arrow that does
not compose, a missing narrowing, a wrong return type) surfaces as a mypy
error before any implementation exists. Check with:

    cd computations/experiments && MYPYPATH=sage_lattice_category_spike/typings \
        uvx mypy --strict --follow-imports=silent \
        sage_lattice_category_spike/algebra/domain_algebra.py \
        sage_lattice_category_spike/algebra/domain_algebra_typecheck.py

Notable coherence facts the types already enforce, on purpose:

- ``direct_sum``/``twist`` return the base ``Lattice`` (a sum or twist does not
  inherit the operands' axioms); reaching discriminant/genus vocabulary forces
  an explicit assertion-shaped narrowing — exactly the two-axis discipline.
- ``Genus.representative()`` returns a base ``Lattice``; comparing it back
  against its source forces the same narrowing.
- ``in_positive_definite(...)`` exposes the reduction/CVP/Voronoi suite
  directly (decision D1 revised 2026-07-04 as a type fact: the suite is
  positive-definite vocabulary, not an opt-in refinement).
"""

from __future__ import annotations

from ..lexicon import (
    DiscriminantFormElement,
    DiscriminantOrthogonalGroup,
    GramMatrix,
    Lattice,
    LatticeElement,
    LatticeMorphism,
    PermutationGroup,
    in_hyperbolic,
    in_integral_nondegenerate,
    in_positive_definite,
)
from .domain_algebra import from_gram_matrix


def enriques_discriminant_pipeline() -> tuple[tuple[int, ...], GramMatrix]:
    """U(2) + E8(2) -> A_L -> normal form (the T7 research smoke, as types)."""
    e8_twisted = from_gram_matrix("E8").twist(2)
    enriques: Lattice = from_gram_matrix("U").twist(2).direct_sum(e8_twisted)
    lattice = in_integral_nondegenerate(enriques)
    disc = lattice.discriminant_group()
    invariants: tuple[int, ...] = disc.invariants()
    assert invariants == disc.invariants()
    return disc.miranda_morrison_normal_form()


def sterk_comparison(left: Lattice, right: Lattice) -> bool:
    """is_isometric is total vocabulary on the base (the Sage-backed implementations are per-leaf)."""
    return left.is_isometric(right)


def k3_primitive_embedding_check() -> bool:
    """A2(-1) embeds primitively in the K3 lattice signature (3, 19)?"""
    a2_negative = in_integral_nondegenerate(from_gram_matrix("A2").twist(-1))
    return a2_negative.embeds_primitively_in_even_unimodular((3, 19))


def definite_enumeration_and_group() -> tuple[int, int]:
    """E8: root count and |O(E8)| — finite vocabulary via PD narrowing only."""
    e8 = in_positive_definite(from_gram_matrix("E8"))
    roots: tuple[LatticeElement, ...] = e8.roots()
    group = e8.isometry_group()
    assert group.is_finite()
    return len(roots), group.order()


def hyperbolic_vocabulary() -> bool:
    """U carries the Weyl/chamber vocabulary as declared contracts; a subgroup
    preservation question consumes a subobject (the carried inclusion), never
    a bare lattice."""
    u = in_hyperbolic(from_gram_matrix("U"))
    weyl = u.weyl_group()
    preserved: bool = weyl.preserves(u.subobject([u.gen(0)]))
    return u.is_reflective() and preserved


def morphism_algebra(lattice: Lattice, vector: LatticeElement) -> LatticeMorphism:
    """Reflection -> induced discriminant action -> kernel/cokernel arrows."""
    sigma = lattice.reflection(vector)
    action = sigma.induced_map_on_discriminant_group()
    assert not action.is_identity() or sigma.is_isometry()
    kernel: Lattice = sigma.kernel().lattice()
    cokernel_order: int = sigma.cokernel().cardinality()
    assert kernel.rank() >= 0 and cokernel_order >= 1
    return sigma


def subgroup_and_seams(lattice: Lattice, isometry: LatticeMorphism) -> PermutationGroup:
    """Caller-supplied generators live ONLY in the typed subgroup; GAP arrives
    through the declared points where it is called, by composition."""
    subgroup = lattice.isometry_group().subgroup([isometry])
    image: DiscriminantOrthogonalGroup = subgroup.discriminant_image()
    return image.as_permutation_group()


def genus_roundtrip() -> bool:
    """genus -> representative -> same_genus, with the forced narrowing."""
    lattice = in_integral_nondegenerate(from_gram_matrix("U").direct_sum(from_gram_matrix("E8")))
    genus = lattice.genus()
    representative = in_integral_nondegenerate(genus.representative())
    return lattice.same_genus(representative)


def reduction_suite_is_positive_definite_vocabulary() -> None:
    """BKZ/CVP live on the positive-definite narrowing itself (D1 revision)."""
    pd = in_positive_definite(from_gram_matrix("A2"))
    reduced = pd.BKZ(block_size=10)
    reduced.closest_vector(reduced.gen(0).coefficient_vector())


def orbit_vocabulary() -> tuple[tuple[DiscriminantFormElement, ...], ...]:
    """Orbits take a GROUP OBJECT, never a raw generator list."""
    lattice = in_integral_nondegenerate(from_gram_matrix("A2"))
    disc = lattice.discriminant_group()
    return disc.orbits(disc.orthogonal_group())


def hyperbolic_narrowing_of_composite() -> bool:
    """A composite that happens to be hyperbolic still needs the assertion."""
    composite = in_hyperbolic(from_gram_matrix("U").twist(2).direct_sum(from_gram_matrix("E8").twist(-1)))
    return composite.has_isotropic_vector()


def mono_factors_through_its_saturation(lattice: Lattice, vector: LatticeElement) -> bool:
    """The morphism-sited saturation triangle: ``iota = (A^sat -> B) . (A -> A^sat)``
    (#100 ratified placement) — all three arrows are morphisms, no coordinates."""
    inclusion = lattice.subobject([vector]).inclusion()
    factor: LatticeMorphism = inclusion.saturation_factorization()
    recomposed: LatticeMorphism = inclusion.saturation().inclusion() * factor
    return recomposed.is_primitive_embedding()


def endomorphism_stability(lattice: Lattice, vector: LatticeElement) -> LatticeMorphism:
    """``preserves`` is a factorization query on the morphism; ``restrict``
    is precomposition with the carried inclusion."""
    sigma = lattice.reflection(vector)
    stable_line = lattice.subobject([vector])
    assert sigma.preserves(stable_line)
    return sigma.restrict(stable_line)


def complement_consumes_the_mono(lattice: Lattice, vector: LatticeElement) -> bool:
    """The orthogonal complement is sited on the monomorphism (kernel of the
    composed pairing); the radical is the complement of the identity."""
    line_complement = lattice.subobject([vector]).inclusion().orthogonal_complement()
    radical = lattice.identity_morphism().orthogonal_complement()
    return line_complement.is_primitive() and radical.is_primitive()


def isometry_existence_is_a_homset_question(left: Lattice, right: Lattice) -> LatticeMorphism:
    """``is_isometric`` is a router for ``Isom(L, M) != {}``; the homset is a
    parent whose elements compose like any morphisms."""
    isometries = left.Isom(right)
    assert left.is_isometric(right) == (not isometries.is_empty())
    for isometry in isometries:
        assert isometry.is_isometry()
    return isometries.an_element()


def embedding_existence_is_a_homset_question(small: Lattice, big: Lattice) -> bool:
    """Nikulin-class existence lives on ``Emb(L, M)``, not on a bare boolean."""
    embeddings = small.Emb(big)
    if embeddings.is_empty():
        return False
    return embeddings.an_element().is_primitive_embedding()


def quotient_descent_is_morphism_sited(lattice: Lattice, isometry: LatticeMorphism, vector: LatticeElement) -> bool:
    """Descent to a finite quotient is asked of the morphism, gated by the
    relation subobject through the projection."""
    quotient = lattice.finite_quotient(lattice.subobject([vector]))
    action = isometry.induced_map_on_quotient(quotient)
    return action.is_identity()
