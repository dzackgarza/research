# Origin: gitclones/integral_lattice/cat/tests/conftest.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

# """Shared test fixtures and hypothesis strategies for lattice tests."""

# from __future__ import annotations

# from hypothesis import strategies as st
# from sage.all import ZZ, Matrix
# from sage.structure.element import Matrix as MatrixType

# from src.lattice import IntegralLattice


# @st.composite
# def positive_definite_matrices(draw: st.DrawFn, min_size: int = 1, max_size: int = 5) -> MatrixType:
#     """
#     Strategy for generating random positive definite integer matrices.

#     Uses A^T * A + n*I to ensure positive definiteness.
#     """
#     n = draw(st.integers(min_value=min_size, max_value=max_size))
#     # Generate a random integer matrix
#     entries = draw(
#         st.lists(
#             st.lists(st.integers(min_value=-3, max_value=3), min_size=n, max_size=n),
#             min_size=n,
#             max_size=n,
#         )
#     )
#     a = Matrix(ZZ, entries)
#     # A^T * A is positive semi-definite; add n*I to make it positive definite
#     return a.transpose() * a + n * Matrix.identity(ZZ, n)


# @st.composite
# def integral_lattices(draw: st.DrawFn, min_size: int = 1, max_size: int = 5) -> IntegralLattice:
#     """Strategy for generating random IntegralLattice instances."""
#     gram = draw(positive_definite_matrices(min_size=min_size, max_size=max_size))
#     return IntegralLattice(gram_matrix=gram)


# @st.composite
# def lattice_vectors(draw: st.DrawFn, lattice: IntegralLattice) -> list[int]:
#     """Strategy for generating random vectors in a lattice."""
#     n = lattice.rank
#     return draw(st.lists(st.integers(min_value=-10, max_value=10), min_size=n, max_size=n))
