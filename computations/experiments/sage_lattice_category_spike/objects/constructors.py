r"""Thin public constructors for synthetic lattices (spec section 6).

Every path routes through the section-1.4 category-namespace entry
``Lattices(R).from_gram_matrix`` — the only entry point into the language.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING

from sage.matrix.constructor import column_matrix, matrix
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ
from sage.structure.element import Matrix

from .categories import Lattices
from .parents import SyntheticIntegralNondegenerateLattice

if TYPE_CHECKING:
    from .. import lexicon
    from ..lexicon import (
        BaseRing,
        CartanType,
        DiscriminantFormElement,
        ExactScalar,
        LatticeMorphism,
        RawGramMatrix,
    )


def SyntheticLatticeFromGram(gram_matrix: RawGramMatrix, base_ring: BaseRing = ZZ, label: str = "L", names: Sequence[str] | str | None = None) -> lexicon.Lattice:
    r"""Construct a synthetic based lattice ``(base_ring, G)`` from its Gram matrix."""
    return Lattices(base_ring).from_gram_matrix(gram_matrix, label=label, names=names)


def Lattice(gram_matrix: RawGramMatrix, base_ring: BaseRing = ZZ, label: str = "L", names: Sequence[str] | str | None = None) -> lexicon.Lattice:
    r"""Public constructor for the owned synthetic lattice spike."""
    return SyntheticLatticeFromGram(gram_matrix, base_ring=base_ring, label=label, names=names)


def U(n: int | ExactScalar = 1, label: str | None = None, names: Sequence[str] | str | None = None) -> lexicon.Lattice:
    r"""The hyperbolic plane ``U(n)`` with Gram ``[[0, n], [n, 0]]``."""
    n = ZZ(n)
    assert n != 0, "U(n) requires a nonzero scale; U(0) is the degenerate rank-2 zero form, not a hyperbolic plane"
    if label is None:
        label = "U" if n == 1 else f"U({n})"
    return Lattices(ZZ).from_gram_matrix([[0, n], [n, 0]], label=label, names=names)


def RootLattice(
    type_: str | CartanType,
    n: int | None = None,
    negative: bool = False,
    label: str | None = None,
    names: Sequence[str] | str | None = None,
) -> lexicon.Lattice:
    r"""The A/D/E root lattice with its standard Cartan Gram.

    ``negative=True`` twists by ``-1`` (the K3 convention). Attaches the
    RootGenerated provenance axiom with the stored Cartan type — the ONLY
    path that attaches it (spec 1.3: the axiom is a certificate, never
    detected from the Gram).
    """
    from sage.combinat.root_system.cartan_matrix import CartanMatrix

    if n is None:
        assert isinstance(type_, str) and len(type_) >= 2 and type_[0].isalpha() and type_[1:].isdigit(), (
            f"RootLattice needs a type like 'E8' or ('E', 8); found type_={type_!r}, n=None"
        )
        letter, rank = type_[0].upper(), int(type_[1:])
    else:
        assert not isinstance(type_, tuple), "RootLattice tuple type_ requires n=None"
        letter, rank = str(type_).upper(), int(n)

    if letter == "A":
        cartan_type: CartanType = ("A", rank)
    elif letter == "D":
        cartan_type = ("D", rank)
    elif letter == "E":
        cartan_type = ("E", rank)
    else:
        raise AssertionError(f"RootLattice supports the simply-laced types A/D/E; found {letter!r} (B/C/F/G Cartan matrices are not symmetric, hence not Gram matrices)")

    gram = matrix(QQ, CartanMatrix([letter, rank]))
    if negative:
        gram = -gram
    if label is None:
        label = f"{letter}{rank}" + ("(-1)" if negative else "")
    return Lattices(ZZ).from_gram_matrix(gram, label=label, cartan_type=cartan_type, names=names)


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
