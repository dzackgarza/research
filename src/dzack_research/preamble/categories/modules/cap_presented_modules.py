"""Private CAP/homalg kernel crossing for finitely presented modules.

The public objects remain the repository's owned finitely presented modules.
CAP receives only selected presentation matrices over a supported computable
coefficient ring and returns a kernel embedding.  This module crosses the
returned relation and embedding matrices back to the owned coefficient ring;
no CAP object is part of the public mathematical interface. Repository-local GAP
package selection and version validation are delegated to released ``sage-categories``.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import cache

from sage.libs.gap.libgap import libgap

from sage_categories.engines.gap import (
    GapPackage,
    PRESENTED_MODULE_PACKAGES,
    load_packages,
    load_repository_package,
)


@cache
def _polynomial_ring(variable_names: tuple[str, ...]):
    # sage-categories owns repository-local GAP package selection and exact
    # version validation. RingsForHomalg supplies the polynomial coefficient
    # ring; ModulePresentationsForCAP and its categorical dependencies use the
    # same selected package root.
    load_repository_package(GapPackage("RingsForHomalg", "2026.05-01"))
    load_packages(PRESENTED_MODULE_PACKAGES)
    integers = libgap.HomalgRingOfIntegersInSage()
    return libgap.PolynomialRing(integers, list(variable_names))


def _homalg_matrix(rows, columns: int, ring):
    rows = tuple(tuple(str(entry) for entry in row) for row in rows)
    if not rows:
        return libgap.HomalgZeroMatrix(0, columns, ring)
    return libgap.HomalgMatrix([list(row) for row in rows], len(rows), columns, ring)


def _matrix_rows(matrix, owned_ring):
    row_count = int(libgap.NumberRows(matrix))
    column_count = int(libgap.NumberColumns(matrix))
    entries = tuple(libgap.EntriesOfHomalgMatrix(matrix))
    if len(entries) != row_count * column_count:
        raise ArithmeticError("CAP returned a matrix with inconsistent dimensions")
    return tuple(
        tuple(
            owned_ring(str(entries[row * column_count + column]))
            for column in range(column_count)
        )
        for row in range(row_count)
    )


@dataclass(frozen=True, eq=False, slots=True)
class CAPKernelPresentation:
    """Private native kernel data with owned-matrix crossings."""

    owned_ring: object
    ring: object
    category: object
    source: object
    target: object
    morphism: object
    embedding: object

    def relation_rows(self):
        return _matrix_rows(
            libgap.UnderlyingMatrix(libgap.Source(self.embedding)),
            self.owned_ring,
        )

    def inclusion_rows(self):
        return _matrix_rows(libgap.UnderlyingMatrix(self.embedding), self.owned_ring)

    def lift_row(self, source_row):
        """Lift one represented source element through the kernel embedding."""
        free_one = libgap.FreeLeftPresentation(1, self.ring)
        tau = libgap.PresentationMorphism(
            free_one,
            _homalg_matrix((tuple(source_row),), len(tuple(source_row)), self.ring),
            self.source,
        )
        lifted = libgap.KernelLift(self.morphism, free_one, tau)
        rows = _matrix_rows(libgap.UnderlyingMatrix(lifted), self.owned_ring)
        if len(rows) != 1:
            raise ArithmeticError("CAP returned a kernel lift with the wrong source rank")
        return rows[0]


def kernel_presentation(
    *,
    variable_names: tuple[str, ...],
    owned_ring,
    source_rank: int,
    target_rank: int,
    source_relation_rows,
    target_relation_rows,
    morphism_rows,
):
    """Return retained private CAP data for a categorical kernel embedding."""
    ring = _polynomial_ring(tuple(variable_names))
    morphism_rows = tuple(tuple(row) for row in morphism_rows)
    source_rank = int(source_rank)
    target_rank = int(target_rank)
    if len(morphism_rows) != source_rank or any(len(row) != target_rank for row in morphism_rows):
        raise ValueError("the CAP morphism matrix has the wrong selected framing dimensions")
    category = libgap.LeftPresentations(ring)
    source = libgap.AsLeftPresentation(
        category,
        _homalg_matrix(source_relation_rows, source_rank, ring),
    )
    target = libgap.AsLeftPresentation(
        category,
        _homalg_matrix(target_relation_rows, target_rank, ring),
    )
    morphism = libgap.PresentationMorphism(
        source,
        _homalg_matrix(morphism_rows, target_rank, ring),
        target,
    )
    embedding = libgap.KernelEmbedding(morphism)
    return CAPKernelPresentation(
        owned_ring, ring, category, source, target, morphism, embedding
    )


__all__ = ["CAPKernelPresentation", "kernel_presentation"]
