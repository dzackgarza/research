# Repo-scoped stubs; see lexicon/README.md.
#
# The generic univariate polynomial ring parent: R['x']. Conversion into the
# ring (from a coefficient sequence or an expression) is Parent.__call__ with
# the element parameter bound to Polynomial.
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.parent import Parent

class PolynomialRing_general(Parent[Polynomial]): ...
