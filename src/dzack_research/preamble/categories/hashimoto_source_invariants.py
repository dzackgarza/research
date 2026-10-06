"""Lattice computations used to validate the stored Hashimoto source tables.

The source parser and row/tag bookkeeping live in ``lattice-database``.  This
module owns the lattice mathematics used by that provenance check: signatures,
discriminant-group factors, basis isometries, and primitive orthogonal
complement embeddings.
"""

from __future__ import annotations

from sage.arith.misc import factor
from sage.matrix.constructor import matrix
from sage.rings.integer_ring import ZZ as SageZZ


def discriminant_prime_powers(lattice) -> tuple[int, ...]:
    """Return the prime-power cyclic factors of the discriminant group of ``lattice``."""
    factors = tuple(
        abs(int(value))
        for value in lattice.discriminant_group().invariant_factors()
        if abs(int(value)) > 1
    )
    return tuple(
        sorted(
            int(prime) ** int(exponent)
            for value in factors
            for prime, exponent in factor(value)
        )
    )


def lattice_summary(lattice) -> tuple[int, int, int, tuple[int, ...]]:
    """Return ``(rank, n_plus, |det|, prime-power discriminant factors)``."""
    signature = lattice.signature_pair()
    return (
        int(lattice.module_rank()),
        int(signature.first()),
        abs(int(lattice.determinant())),
        discriminant_prime_powers(lattice),
    )


def printed_summary(lattice) -> tuple[int, tuple[int, int], int, tuple[int, ...]]:
    """Return rank, full signature, determinant magnitude and discriminant factors."""
    signature = lattice.signature_pair()
    return (
        int(lattice.module_rank()),
        (int(signature.first()), int(signature.second())),
        abs(int(lattice.determinant())),
        discriminant_prime_powers(lattice),
    )


def basis_gives_isometry(source, target, basis_rows) -> bool:
    """Whether ``basis_rows`` is unimodular and gives an isometry ``source -> target``."""
    basis = matrix(SageZZ, basis_rows)
    match abs(int(basis.det())) == 1:
        case False:
            return False
        case True:
            images = tuple(
                target(tuple(int(basis[row, column]) for row in range(basis.nrows())))
                for column in range(basis.ncols())
            )
            try:
                source.Mor(target)(images)
            except ValueError:
                return False
            return True


def primitive_orthogonal_complements(
    ambient,
    first_embeddings,
    first_scale: int,
    second_embeddings,
    second_scale: int,
) -> bool:
    """Whether two stored embedding families contain primitive orthogonal complements.

    Each embedding family is an iterable of ``(matrix_rows, scale)``.  Matrix
    columns are images of the selected source basis in the selected basis of
    ``ambient``.
    """
    ring = ambient.base_ring()
    ambient_module = ring.free_module(int(ambient.module_rank()))
    ambient_rank = int(ambient.module_rank())
    for first, scale in first_embeddings:
        for second, other_scale in second_embeddings:
            if (int(scale), int(other_scale)) != (int(first_scale), int(second_scale)):
                continue
            first_rank = len(first[0]) if first else 0
            second_rank = len(second[0]) if second else 0
            if first_rank + second_rank != ambient_rank:
                continue
            first_columns = tuple(
                tuple(int(row[column]) for row in first)
                for column in range(first_rank)
            )
            second_columns = tuple(
                tuple(int(row[column]) for row in second)
                for column in range(second_rank)
            )
            first_span = ambient_module.subobject_on(
                tuple(ambient_module(column) for column in first_columns)
            )
            second_span = ambient_module.subobject_on(
                tuple(ambient_module(column) for column in second_columns)
            )
            first_vectors = tuple(ambient(column) for column in first_columns)
            second_vectors = tuple(ambient(column) for column in second_columns)
            orthogonal = all(
                left.b(right) == ring.zero()
                for left in first_vectors
                for right in second_vectors
            )
            if (
                orthogonal
                and int(first_span.module_rank()) == len(first_columns)
                and int(second_span.module_rank()) == len(second_columns)
                and first_span.is_primitive()
                and second_span.is_primitive()
            ):
                return True
    return False
