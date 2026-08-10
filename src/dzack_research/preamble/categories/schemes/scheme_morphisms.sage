r"""Subtree for scheme morphisms in Sch/S.

Hierarchy:
  SchemeMorphism(Morphism)
    ├── domain()            --> abstract method returning domain scheme X
    ├── codomain()          --> abstract method returning codomain scheme Y
    ├── compose(g)          --> abstract method returning composition g o f
    ├── pullback(Z)         --> abstract method returning fiber product X \times_Y Z
    ├── evaluate_at(p)      --> f * p  (morphism composition f o p for S-point p: S -> X)
    └── fiber_over(y)       --> f.pullback(y) (fiber product X \times_Y S over S-point y: S -> Y)
"""

from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.misc.abstract_method import abstract_method
from sage.rings.integer_ring import ZZ as SageZZ


class SchemeMorphism(Morphism):
    r"""Abstract base class for scheme morphisms over S in Sch/S.

    In Sch/S:
      1. Domain & codomain are abstract methods returning schemes in Sch/S.
      2. Point evaluation at an S-point p: S -> X is composition f * p.
      3. Preimages / fibers over S-points or subobjects Z -> Y are fiber products X \times_Y Z.
    """

    def __init__(self, parent=None) -> None:
        if parent is not None:
            Morphism.__init__(self, parent)

    @abstract_method
    def domain(self) -> object:
        r"""Return the domain scheme of this morphism."""

    @abstract_method
    def codomain(self) -> object:
        r"""Return the codomain scheme of this morphism."""

    @abstract_method
    def compose(self, g: SchemeMorphism) -> SchemeMorphism:
        r"""Return composition (g o self): X -> Z for g: Y -> Z."""

    @abstract_method
    def pullback(self, Z: object) -> object:
        r"""Return pullback / fiber product X \times_Y Z for a morphism or subobject Z -> Y."""

    def evaluate_at(self, p: SchemeMorphism) -> SchemeMorphism:
        r"""Evaluate self at an S-point p: S -> X via composition f * p."""
        return self * p

    def fiber_over(self, y: SchemeMorphism) -> object:
        r"""Return the fiber X \times_Y S over an S-point y: S -> Y via pullback."""
        return self.pullback(y)


def install_scheme_morphisms() -> None:
    r"""Register post-init hooks and installation for scheme morphisms."""
    pass


install_scheme_morphisms()
