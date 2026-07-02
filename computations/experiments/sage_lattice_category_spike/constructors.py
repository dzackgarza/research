r"""Thin public constructors for synthetic lattices (spec section 6).

Every path routes through the section-1.4 category-namespace entry
``Lattices(R).from_gram_matrix`` — the only door into the language.
"""

from __future__ import annotations

from sage.matrix.constructor import matrix
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ

from .categories import Lattices


def SyntheticLatticeFromGram(gram_matrix, base_ring=ZZ, label="L"):
    r"""Construct a synthetic based lattice ``(base_ring, G)`` from its Gram matrix."""
    return Lattices(base_ring).from_gram_matrix(gram_matrix, label=label)


def Lattice(gram_matrix, base_ring=ZZ, label="L"):
    r"""Public constructor for the owned synthetic lattice spike."""
    return SyntheticLatticeFromGram(gram_matrix, base_ring=base_ring, label=label)


def U(n=1, label=None):
    r"""The hyperbolic plane ``U(n)`` with Gram ``[[0, n], [n, 0]]``."""
    n = ZZ(n)
    assert n != 0, "U(n) requires a nonzero scale; U(0) is the degenerate rank-2 zero form, not a hyperbolic plane"
    if label is None:
        label = "U" if n == 1 else f"U({n})"
    return Lattices(ZZ).from_gram_matrix([[0, n], [n, 0]], label=label)


def RootLattice(type_, n=None, negative=False, label=None):
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
        letter, n = type_[0].upper(), int(type_[1:])
    else:
        letter, n = str(type_).upper(), int(n)
    assert letter in ("A", "D", "E"), (
        f"RootLattice supports the simply-laced types A/D/E; found {letter!r} "
        "(B/C/F/G Cartan matrices are not symmetric, hence not Gram matrices)"
    )
    gram = matrix(QQ, CartanMatrix([letter, n]))
    if negative:
        gram = -gram
    if label is None:
        label = f"{letter}{n}" + ("(-1)" if negative else "")
    return Lattices(ZZ).from_gram_matrix(gram, label=label, cartan_type=(letter, n))


def IntegralLatticeGluing(lattices, glue, return_embeddings=False, label="gluing"):
    r"""Construct the owned overlattice determined by discriminant glue vectors."""
    if not lattices:
        raise ValueError("gluing requires at least one lattice")
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
        if len(glue_vector) != len(lattices):
            raise ValueError(
                "each glue vector must provide one discriminant element per lattice; "
                f"lattices={len(lattices)}, glue_vector={glue_vector}"
            )
        row = [QQ.zero()] * ambient.rank()
        for lattice, start, discriminant_element in zip(lattices, offsets, glue_vector):
            lift = lattice.discriminant_group()._coset_representative_in_source(discriminant_element)
            for i, value in enumerate(lift):
                row[start + i] = value
        lift_rows.append(row)

    glued = ambient.overlattice(lift_rows, check_integral=True, label=label)
    if not return_embeddings:
        return glued
    embeddings = tuple(lattice.Hom(glued).from_matrix(_embedding_matrix(lattice, glued, start)) for lattice, start in zip(lattices, offsets))
    return glued, embeddings


def _embedding_matrix(domain, codomain, start):
    rows = []
    for i in range(codomain.rank()):
        row = []
        for j in range(domain.rank()):
            row.append(ZZ.one() if i == start + j else ZZ.zero())
        rows.extend(row)
    return matrix(ZZ, codomain.rank(), domain.rank(), rows)
