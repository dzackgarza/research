r"""Thin public constructors for synthetic lattices."""

from __future__ import annotations

from sage.matrix.constructor import identity_matrix, matrix
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ

from arithmetic import as_square_qq_matrix
from parents import SyntheticLattice


def SyntheticLatticeFromGram(gram_matrix, base_ring=ZZ, label="L"):
    r"""Construct a synthetic lattice from a distinguished-basis Gram matrix."""
    gram = as_square_qq_matrix(gram_matrix)
    basis_matrix = identity_matrix(QQ, gram.nrows())
    basis_matrix.set_immutable()
    return SyntheticLattice(gram, base_ring, basis_matrix, gram, label)


def Lattice(gram_matrix, base_ring=ZZ, label="L"):
    r"""Public constructor for the owned synthetic lattice spike."""
    return SyntheticLatticeFromGram(gram_matrix, base_ring=base_ring, label=label)


def IntegralLatticeGluing(lattices, glue, return_embeddings=False, label="gluing"):
    r"""Construct the owned overlattice determined by discriminant glue vectors."""
    assert lattices, "gluing requires at least one lattice"
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
            "each glue vector must provide one discriminant element per lattice; "
            f"lattices={len(lattices)}, glue_vector={glue_vector}"
        )
        row = [QQ.zero()] * ambient.rank()
        for lattice, start, discriminant_element in zip(lattices, offsets, glue_vector):
            lift = lattice.discriminant_group().lift(discriminant_element).rational_coordinates()
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
