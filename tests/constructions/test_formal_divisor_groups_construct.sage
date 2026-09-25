r"""A formal divisor is a finite-support integral combination of prime labels."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_formal_divisor_from_terms() -> None:
    divisors = FormalDivisorGroups(ZZ)
    divisor = divisors.from_terms(((2, "p"), (-1, "q")))

    assert divisor.parent() in FormalDivisorGroups(ZZ)
    assert divisor.parent().terms(divisor).cardinality() == cardinal(2)
    assert divisor.parent().components(divisor).cardinality() == cardinal(2)
    assert divisor.parent().divisor_repr(divisor) == "2*p - 1*q"
    assert isinstance(divisor.parent().divisor_latex(divisor), str)
    assert divisor + divisor == divisors.from_terms(((4, "p"), (-2, "q")))
