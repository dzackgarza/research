# Repo-scoped stubs; see lexicon/README.md.
from collections.abc import Iterable
from typing import Any, Generic, TypeVar

from sage.categories.category import Category
from sage.categories.category_types import Category_over_base_ring
from sage.categories.morphism import Morphism
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.structure.element import Element
from sage.structure.parent import Parent

# A module parent IS a Sage Parent; the element parameter is bound like
# Parent._E (covariant, default Element) so implementation classes that
# declare the Modules.ParentMethods edge keep element construction typed
# (see structure/parent.pyi) and stay assignable to the bare noun
# ``Modules.ParentMethods``.
_E = TypeVar("_E", default=Element, covariant=True)

class Modules(Category_over_base_ring):
    def __init__(self, base_ring: Any = ...) -> None: ...
    def FiniteDimensional(self) -> Category: ...
    def WithBasis(self) -> Category: ...

    # Category-first typing (lexicon/INVENTORY.md Part III): Modules.ParentMethods
    # is the static type of "a module parent" — every parent placed in
    # Modules(R), whatever its implementation (free, finitely presented,
    # quotient, subobject, ...), is a Module. At runtime Sage COPIES the
    # category's ParentMethods into each parent's dynamic class rather than
    # inheriting it, so the stub tree declares the mathematically true MRO
    # edge on each implementation class it stubs (FreeModule_generic,
    # FGP_Module_class, ...); the noun's type is the category's surface,
    # never an enumeration of today's implementation classes.
    class ParentMethods(Parent[_E], Generic[_E]):
        # Element construction, membership and base_ring come from Parent.
        # The operations below are the common module surface, verified
        # against the FreeModule_generic and FGP_Module_class representatives
        # and against the runtime dir of Modules(ZZ).ParentMethods.
        def zero(self) -> _E: ...
        def gen(self, i: int | Integer = ...) -> _E: ...
        def gens(self) -> tuple[_E, ...]: ...
        def ngens(self) -> int: ...
        def is_finite(self) -> bool: ...
        # Free modules answer an integer or +Infinity (free_module.py:2595),
        # torsion modules a finite integer; the union is the honest common
        # type on the category surface.
        def cardinality(self) -> Integer | PlusInfinity: ...
        # The runtime surface of Modules(R).ParentMethods (verified by dir).
        # Input elements are stated as Element (Sage coerces them into the
        # module); _E stays in return position for covariance.
        def linear_combination(
            self,
            iter_of_elements: Iterable[Element],
            iter_of_coeffs: Iterable[Element] | None = ...,
            check: bool = ...,
        ) -> _E: ...
        def module_morphism(
            self,
            on_generators: object = ...,
            codomain: Modules.ParentMethods[Any] | None = ...,
            **kwds: object,
        ) -> Morphism: ...
        def quotient(self, sub: object, **kwds: Any) -> Modules.ParentMethods[Any]: ...
        def tensor_square(self) -> Modules.ParentMethods[Any]: ...

# Canonical short name for "a module parent" (a Sage object, so it belongs
# with the Sage typing, not with preamble vocabulary). Type-only: Sage's
# runtime sage.categories.modules exports ``Modules``, not ``Module`` — code
# that imports this name does so under TYPE_CHECKING.
Module = Modules.ParentMethods
