"""External sequence database smoke checks."""

from sage.databases.oeis import OEISSequence


def test_oeis_fibonacci_sequence_fingerprint():
    """OEIS-backed sequence coefficients stay numerically anchored."""
    fib = OEISSequence("A000045")
    assert fib[0] == 0
    assert fib[1] == 1
    assert fib[5] == 5
