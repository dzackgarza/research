r"""End-to-end proofs for the Sage symbol-import resolver."""

from pathlib import Path

from dzack_research.preamble.symbols import synthetic_imports


def test_generated_imports_support_a_polynomial_matrix_identity(
    tmp_path: Path,
) -> None:
    r"""The generated imports expose Sage objects for exact algebra."""
    program = synthetic_imports(
        ["QQ", "PolynomialRing", "matrix"], tmp_path / "symbols.sqlite"
    )
    program += '''
ring = PolynomialRing(QQ, "x")
x = ring.gen()
square = matrix(ring, [[x, 1], [0, x]])
assert square.det() == x**2
'''

    exec(program)
