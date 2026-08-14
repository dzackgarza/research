# Repo-scoped stubs; see lexicon/README.md.
#
# The generic univariate polynomial ring parent: R['x']. Conversion into the
# ring (from a coefficient sequence or an expression) is Parent.__call__ with
# the element parameter bound to Polynomial.
from sage.categories.rings import Rings
from sage.rings.polynomial.polynomial_element import Polynomial

class PolynomialRing_general(Rings.ParentMethods[Polynomial]): ...
