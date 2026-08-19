# Origin: gitclones/integral_lattice/cat/src/abc_specs/new_w_categories/_arrow_abcs.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
Abstract Base Classes for ω-category scaffolding.

This module defines the globular structure of ω-categories using a hierarchy
of n-arrows. The key insight: an n-arrow in category C corresponds to an 
(n-1)-arrow in a hom-category Hom_C(x,y). This correspondence is implemented
via the Morphism_Arrow variants and the hom functor.
"""
from __future__ import annotations

from src.local_typing import *

S = TypeVar("S", covariant=True)
T = TypeVar("T", covariant=True)

type P2[T] = tuple[T,T]


class _Covariant_Callable(ABC, Generic[S, T]):
    """
    A morphism between categories, abstracted as a callable.
    
    Variance note: We intentionally violate standard variance rules.
    If F: A → B, then for A' ≤ A and B' ≤ B, we want the restriction F|_{A'}: A' → B'.
    Python's type system cannot express this, hence the type: ignore.
    """
    @abstractmethod
    def __call__(self, x: S) -> T: ... # type: ignore

    @abstractmethod
    def source(self) -> S: ...
    @abstractmethod
    def target(self) -> T: ...

type _Endo_Covariant_Callable[T] = _Covariant_Callable[T, T]

Obj_in = TypeVar("Obj_in", covariant=True)
Obj_out = TypeVar("Obj_out", covariant=True)
Mor_in = TypeVar("Mor_in", covariant=True)
Mor_out = TypeVar("Mor_out", covariant=True)

class _Functor(ABC, Generic[S, T, Obj_in, Obj_out, Mor_in, Mor_out]):
    """
    A morphism between categories, abstracted as a callable.
    """
    @abstractmethod
    def source(self) -> S: ...
    @abstractmethod
    def target(self) -> T: ...
    @abstractmethod
    def apply_to_object(self, x: Obj_in) -> Obj_out: ... # type: ignore
    @abstractmethod
    def apply_to_morphism(self, f: Mor_in) -> Mor_out: ... # type: ignore
    
    @overload
    def __call__(self, x: Obj_in) -> Obj_out: ... # type: ignore
    @overload
    def __call__(self, x: Mor_in) -> Mor_out: ... # type: ignore
    
    @abstractmethod
    def __call__(self, x: Obj_in | Mor_in) -> Obj_out | Mor_out: ... # type: ignore

type _EndoFunctor[S, Obj_in, Mor_in] = _Functor[S, S, Obj_in, Obj_in, Mor_in, Mor_in]

class _Arrow(ABC):
    """
    Base class for n-cells in a globular ω-category.
    
    The globular structure requires source/target to satisfy:
    - s(s(f)) = s(t(f))  (globular identity)
    - t(s(f)) = t(t(f))  (globular identity)
    
    underlying_data() provides access to the mathematical content
    independent of the categorical structure.
    
    wrapped_arrow() returns the higher-dimensional arrow this cell wraps
    in a hom-category context. For base category cells, returns empty arrow.
    """
    @abstractmethod
    def underlying_data(self) -> Any:
        """The mathematical content this arrow represents."""
        ...

    @abstractmethod
    def source(self) -> Arrow.n | None:
        """The (n-1)-arrow this arrow starts from."""
        ...

    @abstractmethod
    def target(self) -> Arrow.n | None:
        """The (n-1)-arrow this arrow ends at."""
        ...

    @staticmethod
    @abstractmethod
    def level() -> int:
        """The level of this arrow."""
        ...

    @staticmethod
    def is_hom_arrow(x: Any) -> TypeIs[_Hom_Arrow]:
        """Is this arrow a hom-arrow?"""
        return isinstance(x, _Hom_Arrow)

    @staticmethod
    def is_non_hom_arrow(x: Any) -> TypeIs[_Non_Hom_Arrow]:
        """Is this arrow a non-hom arrow?"""
        return isinstance(x, _Non_Hom_Arrow)

class _Arrow_m1(_Arrow):
    """
    (-1)-arrows: elements/points of objects.
    
    These are the terminal level of the globular hierarchy. An element x ∈ X
    lives in a specific object X but has no further source/target structure.
    Used to define what morphisms act on: f(x) for x ∈ source(f).
    """
    @final
    @override
    def source(self) -> None: 
        return None

    @final
    @override
    def target(self) -> None: 
        return None
    
    @abstractmethod
    def ambient_object(self) -> Arrow.n0:
        """The object X containing this element."""
        ...

    @final
    @override
    @staticmethod
    def level() -> int:
        return -1

class _Connective_Arrow(_Arrow):
    """
    Arrows with non-trivial source/target (dimension ≥ 0).
    
    These are the "morphism-like" cells that connect lower-dimensional cells.
    Type refinement guarantees source()/target() never return None.
    """
    @abstractmethod
    @override
    def source(self) -> Arrow.n: ...

    @abstractmethod
    @override
    def target(self) -> Arrow.n: ...

class _Non_Hom_Arrow(_Connective_Arrow):
    """Arrows in a base (non-hom) category."""
    
    @abstractmethod
    def ambient_category(self) -> Arrow.wCategory:
        """The category this object belongs to."""
        ...

class _Hom_Arrow(_Non_Hom_Arrow):
    """Arrows in a hom-category, extending non-hom arrows with wrapping methods."""

    @abstractmethod
    @override
    def ambient_category(self) -> Arrow.Hom_wCategory:
        """The hom-category Hom_C(x,y) containing this arrow."""
        ...

    @abstractmethod
    def wrapped_arrow(self) -> Arrow.n_non_hom | Arrow.n_hom:
        """The higher-dimensional arrow this cell wraps."""
        ...

    @abstractmethod
    def fully_unwrap(self) -> Arrow.n_non_hom:
        """Recursively unwrap to a base category arrow."""
        ...

class _Arrow_n0_non_hom(_Non_Hom_Arrow):
    """
    0-arrows: objects in a category.
    
    In the globular model, objects have degenerate (-1)-arrows as source/target,
    representing the "point" the object occupies. For any object X:
    source(X) = target(X) (the unique empty element of X).
    
    This ensures the globular identities hold trivially at level 0.
    """
    @abstractmethod
    @override
    def source(self) -> Arrow.m1:
        """The empty element of this object."""
        ...

    @abstractmethod
    @override
    def target(self) -> Arrow.m1:
        """The empty element of this object (same as source)."""
        ...

    @override
    @final
    @staticmethod
    def level() -> int:
        return 0

class _Arrow_n0_In_Hom_Category(_Arrow_n0_non_hom, _Hom_Arrow):
    """
    Objects in a hom-category, representing morphisms in the base category.
    
    A morphism f: X → Y in category C becomes an object in Hom_C(X,Y).
    This "dimension shift" is central to the ω-category structure:
    - n-arrows in C ↔ (n-1)-arrows in Hom_C(x,y)
    """
    @abstractmethod
    @override
    def wrapped_arrow(self) -> Arrow.n1:
        """A 0-arrow in Hom_C(x,y) wraps a 1-arrow."""
        ...

class _Arrow_n1_non_hom(_Non_Hom_Arrow):
    """
    1-arrows: morphisms between objects.
    
    A morphism f: X → Y acts on elements via underlying_data.
    For x ∈ X, f(x) ∈ Y is computed by applying underlying_data.
    """
    @abstractmethod
    @override
    def underlying_data(self) -> Arrow.EndoMap[Arrow.m1]:
        """The function on elements: x ↦ f(x)."""
        ...

    @abstractmethod
    @override
    def source(self) -> Arrow.n0_non_hom:
        """Domain object."""
        ...

    @abstractmethod
    @override
    def target(self) -> Arrow.n0_non_hom:
        """Codomain object."""
        ...

    @override
    @final
    @staticmethod
    def level() -> int:
        return 1

class _Arrow_n1_In_Hom_Category(_Arrow_n1_non_hom, _Hom_Arrow):
    """
    1-arrows in a hom-category, representing 2-arrows in the base category.
    
    A 2-morphism α: f ⇒ g in C becomes a morphism in Hom_C(x,y)
    between the objects corresponding to f and g.
    """
    # @abstractmethod
    # @override
    # def underlying_data(self) -> Any: 
    #     """
    #     Leave unspecified for now.
    #     In principle, a morphism η: f => g should act on elements of X as η(f(x)) = g(x), yielding a commutative square:
    #     X --f--> Y
    #     |η_X    |η_Y
    #     v       v
    #     X --g--> Y
    #     """
    #     ...
    
    @abstractmethod
    @override
    def source(self) -> Arrow.n0_hom:
        """The morphism-as-object this starts from."""
        ...

    @abstractmethod
    @override
    def target(self) -> Arrow.n0_hom:
        """The morphism-as-object this ends at."""
        ...

    @abstractmethod
    @override
    def wrapped_arrow(self) -> Arrow.n2:
        """A 1-arrow in Hom_C(x,y) wraps a 2-arrow (in C or in some hom category)."""
        ...

class _Arrow_n2_non_hom(_Non_Hom_Arrow):
    """
    2-arrows: morphisms between morphisms.
    
    A 2-arrow α: f ⇒ g connects two parallel 1-arrows f, g: X → Y.
    The underlying_data gives the structural content of the 2-cell.
    """
    @abstractmethod
    @override
    def underlying_data(self) -> Arrow.EndoMap[Arrow.n1_non_hom]:
        """The structural content of this 2-cell."""
        ...

    @abstractmethod
    @override
    def source(self) -> Arrow.n1_non_hom:
        """The morphism this 2-arrow starts from."""
        ...

    @abstractmethod
    @override
    def target(self) -> Arrow.n1_non_hom:
        """The morphism this 2-arrow ends at."""
        ...

    @override
    @final
    @staticmethod
    def level() -> int:
        return 2

class _Arrow_n2_In_Hom_Category(_Arrow_n2_non_hom, _Hom_Arrow):
    """
    2-arrows in a hom-category, representing 3-arrows in the base category.
    Since 3-arrows are assumed invertible/trivial, these are identity 2-cells.
    """
    @abstractmethod
    @override
    def source(self) -> Arrow.n1_hom:
        """The 1-arrow-in-hom this starts from."""
        ...

    @abstractmethod
    @override
    def target(self) -> Arrow.n1_hom:
        """The 1-arrow-in-hom this ends at."""
        ...

    @abstractmethod
    @override
    def wrapped_arrow(self) -> Arrow.n_geq_3:
        """A 2-arrow in Hom_C wraps a 3-arrow (assumed invertible)."""
        ...

    

class _Arrow_n_geq_3_non_hom(_Non_Hom_Arrow):
    """
    Any n-arrow for n >= 3 is assumed to be invertible.
    These form a contractible space (all parallel arrows are equal).
    """
    ...

class _Arrow_n_geq_3_In_Hom_Category(_Arrow_n_geq_3_non_hom, _Hom_Arrow):
    """
    A 3+ arrow in a hom category wraps a 4+ arrow, etc.
    In Hom^n_C, 0-arrows correspond to n-arrows in C.
    """

    @abstractmethod
    @override
    def wrapped_arrow(self) -> Arrow.n_geq_3:
        """Wraps a higher-dimensional (4+) arrow."""
        ...

class _wCategory(ABC):
    """
    Abstract ω-category.
    
    An ω-category has n-cells for all n ≥ -1, with composition operations
    satisfying coherence laws. This ABC provides:
    
    - elements()/objects()/morphisms()/two_morphisms(): Type constructors for cells
    - hom(): The internal hom functor (X,Y) ↦ Hom_C(X,Y)
    """

    @abstractmethod
    def category_name(self) -> str:
        """The name of this category."""
        ...
        
    @abstractmethod
    def elements(self) -> type[Arrow.m1] | None:
        """The type of (-1)-cells (elements of objects) in this category."""
        ...

    @abstractmethod
    def objects(self) -> type[Arrow.n0 | Arrow.n0_hom]:
        """The type of 0-cells (objects) in this category."""
        ...

    @abstractmethod
    def morphisms(self) -> type[Arrow.n1 | Arrow.n1_hom]:
        """The type of 1-cells (morphisms) in this category."""
        ...

    @abstractmethod
    def two_morphisms(self) -> type[Arrow.n2 | Arrow.n2_hom]:
        """The type of 2-cells (2-morphisms) in this category."""
        ...

    @abstractmethod
    def hom_categories(self) -> type[Arrow.Hom_wCategory]:
        """The type of hom-categories in this category."""
        ...

    @abstractmethod
    def hom(self) -> Arrow.Map[
        P2[Arrow.n0], Arrow.Hom_wCategory
        ]:
        """
        The internal hom functor: (X, Y) ↦ Hom_C(X, Y).
        
        Returns a hom-category whose objects are morphisms X → Y
        and whose morphisms are 2-cells between them.
        """
        ...

    def __contains__(self, item: Any) -> bool:
        """Membership test: is this cell in this category?"""
        match item:
            case _ if isinstance(item, self.morphisms()):
                src = item.source()
                return src.ambient_category() is self if hasattr(src, 'ambient_category') else False
            case _ if isinstance(item, self.objects()):
                return item.ambient_category() is self
            case _:
                return False

    @staticmethod
    def is_hom_category(x: Any) -> TypeIs[Arrow.Hom_wCategory]:
        """Is this category a hom-category?"""
        return isinstance(x, Arrow.Hom_wCategory)

class _Hom_wCategory(_wCategory):
    """
    Hom-category Hom_C(x, y) for objects x, y in base category C.
    
    Implements the dimension shift:
    - Objects are morphisms x → y in C
    - Morphisms are 2-cells between morphisms in C
    
    The bijections one_arrow_to_zero_arrow/zero_arrow_to_one_arrow
    witness the equivalence between 1-arrows in C and objects in Hom_C.
    """
    @abstractmethod
    def base_category(self) -> Arrow.wCategory | Arrow.Hom_wCategory:
        """The category C this hom-category is internal to."""
        ...

    @abstractmethod
    def root_base_category(self) -> Arrow.wCategory:
        """
        If this category is of the form
        Hom_{Hom_{.... _{Hom_C}}}, return C by iteratively applying base_category() until a non-hom category is obtained.
        """

    @abstractmethod
    def domain(self) -> Arrow.n0 | Arrow.n0_hom:
        """The source object x in C (or in a parent hom-category)."""
        ...

    @abstractmethod
    def codomain(self) -> Arrow.n0 | Arrow.n0_hom:
        """The target object y in C (or in a parent hom-category)."""
        ...

    @override
    @final
    def elements(self) -> None:
        """Morphisms do not have 'elements'."""
        return None

    @abstractmethod
    @override
    def objects(self) -> type[Arrow.n0_hom]: ...

    @abstractmethod
    @override
    def morphisms(self) -> type[Arrow.n1_hom]: ...

    @abstractmethod
    @override
    def hom(self) -> Arrow.Map[
        P2[Arrow.n0_hom], Arrow.Hom_wCategory
    ]:
        """Nested hom: Hom_{Hom_C(x,y)}(f, g) for morphisms f, g: x → y."""
        ...

    @staticmethod
    def is_hom_category(x: Any) -> TypeIs[Arrow.Hom_wCategory]:
        return True

class Arrow:
    """Namespace collecting all arrow ABCs for convenient import."""
    n = _Arrow  # arbitrary n-arrow
    Connective = _Connective_Arrow
    n_non_hom = _Non_Hom_Arrow
    n_hom = _Hom_Arrow
    wCategory = _wCategory
    Hom_wCategory = _Hom_wCategory

    Functor = _Functor
    EndoFunctor = _EndoFunctor
    m1 = _Arrow_m1

    n0_non_hom = _Arrow_n0_non_hom
    n1_non_hom = _Arrow_n1_non_hom
    n2_non_hom = _Arrow_n2_non_hom
    n_geq_3_non_hom = _Arrow_n_geq_3_non_hom

    n0_hom = _Arrow_n0_In_Hom_Category
    n1_hom = _Arrow_n1_In_Hom_Category
    n2_hom = _Arrow_n2_In_Hom_Category
    n_geq_3_hom = _Arrow_n_geq_3_In_Hom_Category

    n0 = n0_non_hom | n0_hom
    n1 = n1_non_hom | n1_hom
    n2 = n2_non_hom | n2_hom
    n_geq_3 = n_geq_3_non_hom | n_geq_3_hom

    Map = _Covariant_Callable
    EndoMap = _Endo_Covariant_Callable
    P2 = P2

