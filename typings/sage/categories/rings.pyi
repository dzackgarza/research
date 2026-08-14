# Category-first typing (lexicon/INVENTORY.md Part III): Rings.ParentMethods
# is the static type of "a ring parent". At runtime Sage COPIES ParentMethods
# into each parent's dynamic class rather than inheriting it, so the stub tree
# declares the mathematically true MRO edge on each implementation class it
# stubs (IntegerRing_class, RationalField, IntegerModRing_generic, ...);
# implementations that fail to opt into their category get a documented union
# fallback instead. Method claims here are verified against representative
# ring parents (ZZ, QQ) by lexicon/verify_against_sage.py.

from typing import Generic, TypeVar

from sage.categories.category import Category
from sage.modules.free_module import FreeModule_generic
from sage.rings.integer import Integer
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput, MembershipInput, Parent

_E = TypeVar("_E", bound=RingElement, default=RingElement, covariant=True)

class Rings(Category):
    def __init__(self) -> None: ...

    # A ring parent IS a Sage Parent: the holder class declares the
    # mathematically true edge (realized at runtime by method copying, so the
    # verifier checks it extensionally through representative parents, never
    # by issubclass).
    class ParentMethods(Parent[_E], Generic[_E]):
        def __call__(
            self,
            x: ElementConstructorInput = ...,
            *args: ElementConstructorInput,
            **kwds: ElementConstructorInput,
        ) -> _E: ...
        def __contains__(self, x: MembershipInput) -> bool: ...
        # R^n is the free module over R with entries in R.
        def __pow__(self, n: int | Integer) -> FreeModule_generic[_E]: ...
        def zero(self) -> _E: ...
        def one(self) -> _E: ...
        def gen(self, i: int = ...) -> _E: ...
        def random_element(self) -> _E: ...
        def characteristic(self) -> Integer: ...
        def is_field(self, proof: bool = ...) -> bool: ...

    class ElementMethods: ...

# Canonical short name for "a ring parent" (a Sage object, so it belongs
# with the Sage typing, not with preamble vocabulary). Type-only: Sage's
# runtime sage.categories.rings exports ``Rings``, not ``Ring`` — code that
# imports this name does so under TYPE_CHECKING.
Ring = Rings.ParentMethods
