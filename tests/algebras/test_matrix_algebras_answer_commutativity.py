r"""A matrix algebra decides whether it commutes.

\(M_n(R)\) over a commutative \(R\) is commutative exactly for \(n\le 1\): rank
one is \(R\) itself, and from rank two the matrix units \(e_{12}\) and
\(e_{21}\) multiply to different idempotents in the two orders.

The predicate is what a ring is asked for when it is placed among commutative
rings and among the algebras over itself, so an endomorphism ring that cannot
answer it cannot take that placement.
"""

from dzack_research.preamble.all import QQ
from dzack_research.preamble.rings import MatrixSpace


def test_the_two_by_two_matrix_algebra_does_not_commute() -> None:
    matrices = MatrixSpace(QQ, 2)
    rows = matrices.row_index_set()
    first = matrices.matrix_unit(rows[0], rows[1])
    second = matrices.matrix_unit(rows[1], rows[0])

    assert first * second != second * first
    assert matrices.is_commutative() is False


def test_the_one_by_one_matrix_algebra_commutes() -> None:
    line = MatrixSpace(QQ, 1)

    assert line.is_commutative() is True
    assert line.identity_matrix() * line.identity_matrix() == line.identity_matrix()
