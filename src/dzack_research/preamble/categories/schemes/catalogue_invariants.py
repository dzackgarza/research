"""Mathematical invariants of abstract geometric catalogue data.

These computations were migrated from ``lattice-database/geometric.py``.
They apply to cited numerical tables even when no live scheme realization has
been constructed in the preamble.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class HodgeTermData:
    p: int
    q: int
    coefficient: int


class HodgePoincareInvariants:
    """Arithmetic and symmetry of a finite Hodge--Poincare table."""

    def __init__(self, dimension: int, terms):
        self.dimension = int(dimension)
        self.terms = tuple(terms)
        self._table = {(term.p, term.q): term.coefficient for term in self.terms}

    def has_unique_bidegrees(self) -> bool:
        return len(self._table) == len(self.terms)

    def exponents_within_dimension(self) -> bool:
        return all(
            0 <= p <= self.dimension and 0 <= q <= self.dimension
            for p, q in self._table
        )

    def is_connected(self) -> bool:
        return self._table.get((0, 0)) == 1

    def satisfies_hodge_symmetry_and_serre_duality(self) -> bool:
        n = self.dimension
        return all(
            self._table.get((p, q), 0) == self._table.get((q, p), 0)
            and self._table.get((p, q), 0) == self._table.get((n - p, n - q), 0)
            for p in range(n + 1)
            for q in range(n + 1)
        )

    def symmetry_group(self) -> str:
        n = self.dimension
        return (
            "D4"
            if all(
                self._table.get((p, q), 0) == self._table.get((n - p, q), 0)
                for p in range(n + 1)
                for q in range(n + 1)
            )
            else "V4"
        )

    def hodge_number(self, p: int, q: int) -> int:
        return int(self._table.get((int(p), int(q)), 0))

    def betti_number(self, degree: int) -> int:
        degree = int(degree)
        return sum(
            term.coefficient for term in self.terms if term.p + term.q == degree
        )

    def euler_characteristic(self) -> int:
        return sum(
            (-1) ** (term.p + term.q) * term.coefficient for term in self.terms
        )


def complete_intersection_configuration_dimension(
    ambient_projective_dimensions, equation_multidegrees
) -> int:
    """Return ``sum n_i - number_of_equations`` for a product-projective configuration."""
    return sum(int(value) for value in ambient_projective_dimensions) - len(
        tuple(equation_multidegrees)
    )


def complete_intersection_is_calabi_yau(
    ambient_projective_dimensions, equation_multidegrees
) -> bool:
    """Return whether the multidegrees sum to ``n_i+1`` in every factor."""
    ambient = tuple(int(value) for value in ambient_projective_dimensions)
    equations = tuple(tuple(int(value) for value in row) for row in equation_multidegrees)
    return all(
        sum(degrees[index] for degrees in equations) == dimension + 1
        for index, dimension in enumerate(ambient)
    )


def chern_indices_are_top_degree(indices, dimension: int) -> bool:
    indices = tuple(int(value) for value in indices)
    return tuple(sorted(indices)) == indices and sum(indices) == int(dimension)


def pontryagin_indices_are_top_degree(indices, complex_dimension: int) -> bool:
    return 2 * sum(int(value) for value in indices) == int(complex_dimension)


def surface_data_fits_dimension(complex_dimension: int) -> bool:
    return int(complex_dimension) == 2


def cohomology_degree_fits_dimension(degree: int, complex_dimension: int) -> bool:
    return 0 <= int(degree) <= 2 * int(complex_dimension)


def symmetric_space_rank_fits_dimension(rank: int, real_dimension: int) -> bool:
    return int(rank) <= int(real_dimension)


def symmetric_space_dual_types_are_consistent(
    curvature_type: str, compact_dual, noncompact_dual
) -> bool:
    if compact_dual is not None and curvature_type != "noncompact":
        return False
    if noncompact_dual is not None and curvature_type != "compact":
        return False
    return True


def hermitian_dimensions_are_consistent(real_dimension: int, complex_dimension: int) -> bool:
    return int(real_dimension) == 2 * int(complex_dimension)
