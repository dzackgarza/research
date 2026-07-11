r"""Thin public constructors for synthetic lattices (spec section 6).

Every path routes through the section-1.4 category-namespace entry
``Lattices(R).from_gram_matrix`` — the only entry point into the language.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING

from sage.matrix.constructor import column_matrix, identity_matrix, matrix
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ

from .categories import Lattices
from .parents import SyntheticIntegralNondegenerateLattice, SyntheticLattice

if TYPE_CHECKING:
    from .. import lexicon
    from ..lexicon import (
        BaseRing,
        DiscriminantFormElement,
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
) -> lexicon.Lattice:
    r"""THE constructor: minimal routing on ``Lattice`` itself — subcategory
    membership is output, never input (vault decision 2026-07-09).

    Accepts a Gram matrix, or a lattice NAME — ``"U"``/``"H"``, an A/D/E
    string like ``"E8"``, or a Cartan datum ``("A", 2)``. A name is
    construction data, so ``Lattice("E8")`` yields a root-generated lattice
    (the Cartan certificate rides the name); the same Gram passed as a raw
    matrix never acquires the axiom.

    Named root lattices are **negative definite** by construction, the AG
    convention: ``Lattice("E8")`` has signature ``(0, 8)`` and roots of square
    ``-2``, realized as a subobject of the standard negative-definite lattice
    ``I_{0,m}`` via the Bourbaki simple roots. The positive (crystallographic)
    form is the ``-1`` twist, spelled ``Lattice("E8(-1)")`` or, equivalently,
    ``Lattice("E8").twist(-1)``. There is no sign flag: the sign is carried by
    the twist, not a boolean mode."""
    from ..algebra.arithmetic import _is_named_gram_data

    if _is_named_gram_data(gram_matrix):
        return _named_lattice(gram_matrix, base_ring, label, names)
    return SyntheticLatticeFromGram(gram_matrix, base_ring=base_ring, label=label if label is not None else "L", names=names)


def _default_named_label(name: LatticeName) -> str:
    return name if isinstance(name, str) else f"{name[0]}{name[1]}"


def _named_lattice(
    name: LatticeName,
    base_ring: BaseRing,
    label: str | None,
    names: Sequence[str] | str | None,
) -> lexicon.Lattice:
    r"""Build a named lattice. A trailing ``"(-1)"`` on a string name is the
    positive (crystallographic) twist of the negative-definite default."""
    from ..algebra.arithmetic import named_cartan_type, named_gram

    base_name: LatticeName
    if isinstance(name, str) and name.endswith("(-1)"):
        positive_twist = True
        base_name = name[:-4]
    else:
        positive_twist = False
        base_name = name
    base_label = _default_named_label(base_name)
    final_label = label if label is not None else base_label + ("(-1)" if positive_twist else "")

    cartan = named_cartan_type(base_name)
    if cartan is None:
        # U/H: the hyperbolic plane; no root provenance, no subobject ambient.
        plane = SyntheticLatticeFromGram(named_gram(base_name), base_ring=base_ring, label=base_label, names=names)
        return plane.twist(-1, label=final_label) if positive_twist else plane

    negative = _negative_definite_root_lattice(cartan, base_ring, base_label, names)
    return negative.twist(-1, label=final_label) if positive_twist else negative


def _negative_definite_root_lattice(
    cartan: LatticeName,
    base_ring: BaseRing,
    label: str,
    names: Sequence[str] | str | None,
) -> lexicon.Lattice:
    r"""The AG-convention root lattice: Gram ``= -Cartan``, so it is negative
    definite with roots of square ``-2``. The Bourbaki roots realize it inside
    ``I_{0,m} = I_{m,0}(-1)`` (m the ambient dimension), but the lattice itself
    is stored on its intrinsic rank-``n`` coordinates -- its identity is the
    pair ``(R, G)`` -- so every rank-``n`` operation (dual, finite quotient,
    reflection) is well defined; A_n / E_6 / E_7 have ``m > n`` and must not be
    pinned to the oversized ambient."""
    from ..algebra.arithmetic import named_cartan_type, named_gram

    return Lattices(base_ring).from_gram_matrix(
        -named_gram(cartan),
        label=label,
        cartan_type=named_cartan_type(cartan),
        names=names,
    )


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

    # The overlattice basis B, in the direct-sum ambient's coordinates. glued is
    # the plain lattice on that basis; each summand embeds by expressing its
    # generators (block units of the ambient) in B -- computed once, here.
    glue_matrix = matrix(QQ, lift_rows) if lift_rows else matrix(QQ, 0, ambient.rank())
    combined = identity_matrix(QQ, ambient.rank()).stack(glue_matrix)
    overlattice_basis = matrix(QQ, (QQ ** ambient.rank()).span(combined.rows(), ZZ).basis_matrix())
    assert isinstance(ambient, SyntheticLattice), f"gluing builds the overlattice on the direct-sum ambient; found={type(ambient)}"
    glued = ambient._from_rows(overlattice_basis, ZZ, label)
    assert glued.is_integral(), f"glued overlattice is not integral; gram={glued.gram_matrix()}"
    if not return_embeddings:
        return glued
    embeddings = tuple(
        lattice.Hom(glued).from_matrix(column_matrix(ZZ, [overlattice_basis.solve_left(identity_matrix(QQ, ambient.rank()).row(start + j)) for j in range(lattice.rank())]))
        for lattice, start in zip(lattices, offsets)
    )
    return glued, embeddings
