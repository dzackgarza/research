# Repo-scoped stubs; see lexicon/README.md.
from collections.abc import Callable, Iterable
from typing import Generic, TypeVar

from sage.categories.category import Category
from sage.categories.category_types import Category_over_base_ring
from sage.categories.morphism import Morphism
from sage.categories.rings import Rings
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.structure.element import Element, RingElement
from sage.structure.parent import Parent

# A module parent IS a Sage Parent; the element parameter is bound like
# Parent._E (covariant, default Element) so implementation classes that
# declare the Modules.ParentMethods edge keep element construction typed
# (see structure/parent.pyi) and stay assignable to the bare noun
# ``Modules.ParentMethods``.
_E = TypeVar("_E", default=Element, covariant=True)
_CategoryScalar = TypeVar(
    "_CategoryScalar",
    bound=RingElement,
    default=RingElement,
    covariant=True,
)
_ParentScalar = TypeVar(
    "_ParentScalar",
    bound=RingElement,
    default=RingElement,
    covariant=True,
)
_CodomainElement = TypeVar("_CodomainElement", default=Element)

class Modules(Category_over_base_ring, Generic[_CategoryScalar]):
    def __init__(self, base_ring: Rings.ParentMethods[_CategoryScalar]) -> None: ...
    def base_ring(self) -> Rings.ParentMethods[_CategoryScalar]: ...
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
    class ParentMethods(Parent[_E], Generic[_E, _ParentScalar]):
        # Element construction and membership come from Parent. Placement in
        # Modules(R) narrows the optional Parent base ring to R.
        def base_ring(self) -> Rings.ParentMethods[_ParentScalar]: ...
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
            iter_of_elements: Iterable[_E],
            iter_of_coeffs: Iterable[_ParentScalar] | None = ...,
            check: bool = ...,
        ) -> _E: ...
        def module_morphism(
            self,
            function: Callable[[_E], _CodomainElement],
            *,
            codomain: Modules.ParentMethods[_CodomainElement, _ParentScalar],
            category: Category | None = ...,
        ) -> Morphism[_E, _CodomainElement]: ...
        def quotient(
            self,
            submodule: Modules.ParentMethods[_E, _ParentScalar],
        ) -> Modules.ParentMethods[Element, _ParentScalar]: ...
        def tensor_square(self) -> Modules.ParentMethods[Element, _ParentScalar]: ...

# Canonical short name for "a module parent" (a Sage object, so it belongs
# with the Sage typing, not with preamble vocabulary). Type-only: Sage's
# runtime sage.categories.modules exports ``Modules``, not ``Module`` — code
# that imports this name does so under TYPE_CHECKING.
Module = Modules.ParentMethods
