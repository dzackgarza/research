r"""Typed composition checks for the category's operations (V2 type fixture).

These functions are NEVER executed — every grammar stub raises — and this
module is not runtime code (it is not imported by the package). It exists so
the type checker exercises the LANGUAGE: each research-shaped workflow below
composes the protocol arrows, and an incoherent signature (an arrow that does
not compose, a missing narrowing, a wrong return type) surfaces as a mypy
error before any implementation exists. Check with:

    cd computations/experiments && uvx mypy --strict --ignore-missing-imports \
        --follow-imports=silent sage_lattice_category_spike/domain_algebra.py \
        sage_lattice_category_spike/domain_algebra_typecheck.py

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

from .domain_algebra import (
    DiscriminantOrthogonalGroup,
    DiscriminantFormElement,
    ExactScalar,
    GramMatrix,
    Lattice,
    LatticeElement,
    LatticeMorphism,
    RootLattice,
    U,
    in_hyperbolic,
    in_integral_nondegenerate,
    in_positive_definite,
)


def enriques_discriminant_pipeline() -> tuple[tuple[int, ...], GramMatrix]:
    """U(2) + E8(2) -> A_L -> normal form (the T7 research smoke, as types)."""
    e8_twisted = RootLattice("E", 8).twist(ExactScalar(2))
    enriques: Lattice = U(2).direct_sum(e8_twisted)
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
    a2_negative = in_integral_nondegenerate(RootLattice("A", 2, negative=True))
    return a2_negative.embeds_primitively_in_unimodular((3, 19), even=True)


def definite_enumeration_and_group() -> tuple[int, int]:
    """E8: root count and |O(E8)| — finite vocabulary via PD narrowing only."""
    e8 = in_positive_definite(RootLattice("E", 8))
    roots: tuple[LatticeElement, ...] = e8.roots()
    group = e8.isometry_group()
    assert group.is_finite()
    return len(roots), group.order()


def hyperbolic_vocabulary() -> bool:
    """U carries the Weyl/chamber vocabulary as declared contracts."""
    u = U()
    weyl = u.weyl_group()
    preserved: bool = weyl.preserves(u.radical())
    return u.is_reflective() and preserved


def morphism_algebra(lattice: Lattice, vector: LatticeElement) -> LatticeMorphism:
    """Reflection -> induced discriminant action -> kernel/cokernel arrows."""
    sigma = lattice.reflection(vector)
    action = sigma.induced_map_on_discriminant_group()
    assert not action.is_identity() or sigma.is_isometry()
    kernel: Lattice = sigma.kernel()
    cokernel_order: int = sigma.cokernel().cardinality()
    assert kernel.rank() >= 0 and cokernel_order >= 1
    return sigma


def subgroup_and_seams(lattice: Lattice, isometry: LatticeMorphism) -> object:
    """Caller-supplied generators live ONLY in the typed subgroup; GAP arrives
    through the declared points where it is called, by composition."""
    subgroup = lattice.isometry_group().subgroup([isometry])
    image: DiscriminantOrthogonalGroup = subgroup.discriminant_image()
    return image.as_permutation_group()


def genus_roundtrip() -> bool:
    """genus -> representative -> same_genus, with the forced narrowing."""
    lattice = in_integral_nondegenerate(U().direct_sum(RootLattice("E", 8)))
    genus = lattice.genus()
    representative = in_integral_nondegenerate(genus.representative())
    return lattice.same_genus(representative)


def reduction_suite_is_positive_definite_vocabulary() -> None:
    """BKZ/CVP live on the positive-definite narrowing itself (D1 revision)."""
    pd = in_positive_definite(RootLattice("A", 2))
    reduced = pd.BKZ(block_size=10)
    reduced.closest_vector([ExactScalar(0), ExactScalar(1)])


def orbit_vocabulary() -> tuple[tuple[DiscriminantFormElement, ...], ...]:
    """Orbits take a GROUP OBJECT, never a raw generator list."""
    lattice = in_integral_nondegenerate(RootLattice("A", 2))
    disc = lattice.discriminant_group()
    return disc.orbits(disc.orthogonal_group())


def hyperbolic_narrowing_of_composite() -> bool:
    """A composite that happens to be hyperbolic still needs the assertion."""
    composite = in_hyperbolic(U(2).direct_sum(RootLattice("E", 8, negative=True)))
    return composite.has_isotropic_vector()
