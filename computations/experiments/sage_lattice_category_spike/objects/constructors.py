r"""Thin public constructors for synthetic lattices (spec section 6).

Every path routes through the section-1.4 category-namespace entry
``Lattices(R).from_gram_matrix`` — the only entry point into the language.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING

from sage.matrix.constructor import column_matrix
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ
from sage.structure.element import Matrix

from .categories import Lattices
from .parents import SyntheticIntegralNondegenerateLattice

if TYPE_CHECKING:
    from .. import lexicon
    from ..lexicon import (
        BaseRing,
        DiscriminantFormElement,
        ExactScalar,
        LatticeMorphism,
        LatticeName,
        RawGramMatrix,
    )


def SyntheticLatticeFromGram(gram_matrix: RawGramMatrix | LatticeName, base_ring: BaseRing = ZZ, label: str = "L", names: Sequence[str] | str | None = None) -> lexicon.Lattice:
    r"""Construct a synthetic based lattice ``(base_ring, G)`` from its Gram matrix."""
    return Lattices(base_ring).from_gram_matrix(gram_matrix, label=label, names=names)


def Lattice(
    gram_matrix: RawGramMatrix | LatticeName,
    base_ring: BaseRing = ZZ,
    label: str | None = None,
    names: Sequence[str] | str | None = None,
    negative: bool = False,
) -> lexicon.Lattice:
    r"""THE constructor: minimal routing on ``Lattice`` itself — subcategory
    membership is output, never input (vault decision 2026-07-09).

    Accepts a Gram matrix, or a lattice NAME — ``"U"``/``"H"``, an A/D/E
    string like ``"E8"``, or a Cartan datum ``("A", 2)``. A name is
    construction data, so ``Lattice("E8")`` yields a root-generated lattice
    (the Cartan certificate rides the name); the same Gram passed as a raw
    matrix never acquires the axiom. ``negative=True`` twists a named Gram
    by ``-1`` (the K3 convention)."""
    from ..algebra.arithmetic import _is_named_gram_data, named_cartan_type, named_gram

    if _is_named_gram_data(gram_matrix):
        name = gram_matrix
        gram = -named_gram(name) if negative else named_gram(name)
        if label is None:
            label = (name if isinstance(name, str) else f"{name[0]}{name[1]}") + ("(-1)" if negative else "")
        return Lattices(base_ring).from_gram_matrix(gram, label=label, cartan_type=named_cartan_type(name), names=names)
    assert not negative, "negative= twists a NAMED lattice by -1; for a raw Gram matrix, negate the matrix"
    return SyntheticLatticeFromGram(gram_matrix, base_ring=base_ring, label=label if label is not None else "L", names=names)


def U(n: int | ExactScalar = 1, label: str | None = None, names: Sequence[str] | str | None = None) -> lexicon.Lattice:
    r"""The hyperbolic plane ``U(n)`` with Gram ``[[0, n], [n, 0]]``."""
    n = ZZ(n)
    assert n != 0, "U(n) requires a nonzero scale; U(0) is the degenerate rank-2 zero form, not a hyperbolic plane"
    if label is None:
        label = "U" if n == 1 else f"U({n})"
    return Lattices(ZZ).from_gram_matrix([[0, n], [n, 0]], label=label, names=names)


def IntegralLatticeGluing(
    lattices: Sequence[lexicon.Lattice],
    glue: Sequence[Sequence[DiscriminantFormElement]],
    return_embeddings: bool = False,
    label: str = "gluing",
) -> lexicon.Lattice | tuple[lexicon.Lattice, tuple[LatticeMorphism, ...]]:
    r"""Construct the owned overlattice determined by discriminant glue vectors."""
    assert lattices, "gluing requires at least one lattice; fix the caller's lattice list"
    ambient = lattices[0]
    for lattice in lattices[1:]:
        ambient = ambient.direct_sum(lattice, label=label)

    lift_rows = []
    offsets = []
    offset = 0
    for lattice in lattices:
        offsets.append(offset)
        offset += lattice.rank()

    for glue_vector in glue:
        assert len(glue_vector) == len(lattices), (
            f"each glue vector must provide one discriminant element per lattice; lattices={len(lattices)}, glue_vector={glue_vector}; fix the caller's glue data"
        )
        row = [QQ.zero()] * ambient.rank()
        for lattice, start, discriminant_element in zip(lattices, offsets, glue_vector):
            # glue vectors live in discriminant groups, so each glued summand
            # must carry that vocabulary (integral nondegenerate)
            assert isinstance(lattice, SyntheticIntegralNondegenerateLattice), f"gluing requires integral nondegenerate summands; found={type(lattice)}"
            from ..forms.discriminant_forms import SyntheticSourcedDiscriminantForm

            discriminant_group = lattice.discriminant_group()
            assert isinstance(discriminant_group, SyntheticSourcedDiscriminantForm), f"expected a sourced discriminant group; found={type(discriminant_group)}"
            lift = discriminant_group._coset_representative_in_source(discriminant_element)
            for i, value in enumerate(lift):
                row[start + i] = value
        lift_rows.append(row)

    glued = ambient.overlattice(lift_rows, check_integral=True, label=label)
    if not return_embeddings:
        return glued
    embeddings = tuple(lattice.Hom(glued).from_matrix(_embedding_matrix(lattice, glued, start)) for lattice, start in zip(lattices, offsets))
    return glued, embeddings


def _embedding_matrix(domain: lexicon.Lattice, codomain: lexicon.Lattice, start: int) -> Matrix:
    ambient_basis = codomain._rationalization_module().basis()
    return column_matrix(
        ZZ,
        [codomain._underlying_module().coordinate_vector(ambient_basis[start + j]) for j in range(domain.rank())],
    )
