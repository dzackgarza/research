# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/two_category_interface/two_category_mixins.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.


from __future__ import annotations

from src.local_typing import *

from src._types import BoolProof, CategoryABCs

# Minimal category mixins:

class Required_Sage_Methods(ABC):
    ...

class Basic_Metadata(ABC):

    @final
    @abstractmethod
    def __eq__(self, other: Any) -> bool: ...

    @final
    @abstractmethod
    def __hash__(self) -> int: ...

    @final
    @abstractmethod
    def __call__(self, **cell_data: Any) -> Any: ...

    @final
    @abstractmethod
    def __repr__(self) -> str: ...

    @final
    @abstractmethod
    def __str__(self) -> str: ...

class Object_And_Morphism_Classes(ABC):

    @classmethod
    @final
    @abstractmethod
    def element_class(cls) -> type[CategoryABCs.Element] | None:
        """Return the class of elements of objects in this category."""
        ...

    @classmethod
    @final
    @abstractmethod
    def object_class(cls) -> type[CategoryABCs.Object]:
        """Return the class of objects in this category."""
        ...

    @classmethod
    @final
    @abstractmethod
    def morphism_class(cls) -> type[CategoryABCs.OneMorphism]:
        """Return the class of morphisms in this category."""
        ...

    @classmethod
    @final
    @abstractmethod
    def two_morphism_class(cls) -> type[CategoryABCs.OneMorphism]:
        """Return the class of morphisms in this category."""
        ...

    # Hom/End/Aut category classes
    @classmethod
    @final
    @abstractmethod
    def homC_category_class(cls) -> type[CategoryABCs.HomC]: ...

    @classmethod
    @final
    @abstractmethod
    def homC_xy_category_class(cls) -> type[CategoryABCs.HomC_xy]: ...

    @classmethod
    @final
    @abstractmethod
    def endC_category_class(cls) -> type[CategoryABCs.EndC]: ...

    @classmethod
    @final
    @abstractmethod
    def endC_x_category_class(cls) -> type[CategoryABCs.EndC_x]: ...

    @classmethod
    @final
    @abstractmethod
    def endomorphism_class(cls) -> type[CategoryABCs.EndoOneMorphism]: ...

    @classmethod
    @final
    @abstractmethod
    def autC_category_class(cls) -> type[CategoryABCs.AutC]: ...

    @classmethod
    @final
    @abstractmethod
    def autC_x_category_class(cls) -> type[CategoryABCs.AutC_x]: ...

    @classmethod
    @final
    @abstractmethod
    def automorphism_class(cls) -> type[CategoryABCs.AutoOneMorphism]: ...

class Predicates_On_This_Category(ABC):

    @final
    @abstractmethod
    def is_compactly_generated(self) -> BoolProof: ...

    @final
    @abstractmethod
    def is_additive(self) -> BoolProof: ...

    @final
    @abstractmethod
    def is_pointed(self) -> BoolProof: ...

    @final
    @abstractmethod
    def is_discrete(self) -> BoolProof: ...

    @final
    @abstractmethod
    def is_groupoid(self) -> BoolProof: ...

    @final
    @abstractmethod
    def is_complete(self) -> BoolProof: ...

    @final
    @abstractmethod
    def is_cocomplete(self) -> BoolProof: ...

    @final
    @abstractmethod
    def is_bicomplete(self) -> BoolProof: ...

    @final
    @abstractmethod
    def is_abelian(self) -> BoolProof: ...

    @final
    @abstractmethod
    def is_op_category(self) -> bool:
        """True if this is an opposite category C^op."""
        ...

class Ambient_Category_Interactions(ABC):
    """
    For each method f here, define:
    self.f(x) := self.amb().f_C(self, other).

    E.g. self.product(x) := self.amb().product_C(self, x), so
    x * y := Prod_A([x,y])
    """

    @final
    @abstractmethod
    def product(self, other: CategoryABCs.Object) -> CategoryABCs.Object: ...

    @final
    @abstractmethod
    def coproduct(self, other: CategoryABCs.Object) -> CategoryABCs.Object: ...

    @final
    @abstractmethod
    def directsum(self, other: CategoryABCs.Object) -> CategoryABCs.Object: ...

    @final
    @abstractmethod
    def quotient(self, other: CategoryABCs.Object) -> CategoryABCs.Object: ...

    # Predicates determined by the ambient category

    @final
    @abstractmethod
    def is_terminal(self) -> BoolProof: ...

    @final
    @abstractmethod
    def is_initial(self) -> BoolProof: ...

    @final
    @abstractmethod
    def is_zero(self) -> BoolProof: ...

class Equivalence_Of_Self_With_Other_Checks(ABC):

    @final 
    def is_equal_to(self, other: Any) -> bool: ...

    @final
    @abstractmethod
    def is_equivalent_to(self, other: Any) -> BoolProof: ...

    @final
    @abstractmethod
    def is_isomorphic_to(self, other: Any) -> BoolProof: ...

class Self_With_Other_Operators(ABC):

    @final
    @abstractmethod
    def __and__(self, other: CategoryABCs.Object) -> Any: ...

    @final
    @abstractmethod
    def __bool__(self) -> bool: ...

    @final
    @abstractmethod
    def __ge__(self, other: CategoryABCs.Object) -> bool: ...

    @final
    @abstractmethod
    def __getitem__(self, key: int) -> Any: ...

    @final
    @abstractmethod
    def __gt__(self, other: CategoryABCs.Object) -> bool: ...

    @final
    @abstractmethod
    def __invert__(self) -> CategoryABCs.Object: ...

    @final
    @abstractmethod
    def __le__(self, other: CategoryABCs.Object) -> bool: ...

    @final
    @abstractmethod
    def __len__(self) -> int: ...

    @final
    @abstractmethod
    def __lshift__(self, other: CategoryABCs.Object) -> CategoryABCs.Object: ...

    @final
    @abstractmethod
    def __lt__(self, other: CategoryABCs.Object) -> bool: ...

    @final
    @abstractmethod
    def __matmul__(self, other: CategoryABCs.Object) -> CategoryABCs.Object: ...

    @final
    @abstractmethod
    def __mod__(self, other: CategoryABCs.Object) -> CategoryABCs.Object: ...

    @final
    @abstractmethod
    def __ne__(self, other: Any) -> bool: ...

    @final
    @abstractmethod
    def __neg__(self) -> CategoryABCs.Object: ...

    @final
    @abstractmethod
    def __next__(self) -> CategoryABCs.Object: ...

    @final
    @abstractmethod
    def __or__(self, other: CategoryABCs.Object) -> CategoryABCs.Object: ...

    @final
    @abstractmethod
    def __pow__(self, other: int) -> CategoryABCs.Object: ...

    @final
    @abstractmethod
    def __rmul__(self, other: int) -> CategoryABCs.Object: ...

    @final
    @abstractmethod
    def __rshift__(self, other: CategoryABCs.Object) -> CategoryABCs.Object: ...

    @final
    @abstractmethod
    def __sub__(self, other: CategoryABCs.Object) -> CategoryABCs.Object: ...

    @final
    @abstractmethod
    def __truediv__(self, other: CategoryABCs.Object) -> CategoryABCs.Object: ...

    @final
    @abstractmethod
    def __add__(self, other: CategoryABCs.Object) -> CategoryABCs.Object: ...

    @final
    @abstractmethod
    def __mul__(self, other: CategoryABCs.Object | int) -> CategoryABCs.Object: ...

# Nontrivial category mixins:

class Hom_Constructors(ABC):

    # Homs in C
    @final
    @abstractmethod
    def hom_C(
        self, 
        x: CategoryABCs.Object | None = None, 
        y: CategoryABCs.Object | None = None
    ) -> CategoryABCs.HomC | CategoryABCs.HomC_xy:
        """
        self.hom_C() := Hom_C
        self.hom_C(x, y) := Hom_C(x, y)
        """
        ...

    # Endomorphisms in C

    @overload
    def end_C(self) -> CategoryABCs.EndC:
        """
        self.end_C() := End_C
        """
        ...

    @overload
    def end_C(self, x: CategoryABCs.Object) -> CategoryABCs.EndC_x:
        """
        self.end_C(x) := End_C(x)
        """
        ...

    @final
    @abstractmethod
    def end_C(
        self, x: CategoryABCs.Object | None = None
    ) -> CategoryABCs.EndC_x | CategoryABCs.EndC:
        """
        self.end_C() := End_C
        self.end_C(x) := End_C(x)
        """
        ...

    # Automorphisms in C

    @overload
    def aut_C(self) -> CategoryABCs.AutC:
        """
        self.aut_C() := Aut_C
        """
        ...

    @overload
    def aut_C(self, x: CategoryABCs.Object) -> CategoryABCs.AutC_x:
        """
        self.aut_C(x) := Aut_C(x)
        """
        ...

    @final
    @abstractmethod
    def aut_C(
        self, x: CategoryABCs.Object | None = None
    ) -> CategoryABCs.AutC_x | CategoryABCs.AutC:
        """
        self.aut_C() := Aut_C
        self.aut_C(x) := Aut_C(x)
        """
        ...

    # Little homs: homs/ends/auts in the category containing C.
    @final
    @abstractmethod
    def hom(self, D: Self) -> CategoryABCs.HomC_xy:
        """
        If this category is C and C is an object of A,
        self.hom(D) := Hom_A(C, D).
        """
        ...

    @final
    @abstractmethod
    def end(self) -> CategoryABCs.EndC_x | CategoryABCs.EndC:
        """
        self.end() := End_C(self)
        """
        ...

    @final
    @abstractmethod
    def aut(self) -> CategoryABCs.AutC_x | CategoryABCs.AutC:
        """
        self.aut() := Aut_C(self)
        """
        ...

class Predicates_On_Objects(ABC):

    @final
    @abstractmethod
    def is_terminal_object_C(self, x: CategoryABCs.Object) -> BoolProof:
        """Check if x is terminal in this category."""
        ...

    @final
    @abstractmethod
    def is_initial_object_C(self, x: CategoryABCs.Object) -> BoolProof:
        """Check if x is initial in this category."""
        ...

    @final
    @abstractmethod
    def is_zero_object_C(self, x: CategoryABCs.Object) -> BoolProof:
        """Check if this category is pointed with zero object."""
        ...

    @final
    @abstractmethod
    def is_object_C(self, x: Any) -> bool:
        """Check if x is an object (instance of object_class) in this category."""
        ...

    @final
    @abstractmethod
    def is_morphism_C(self, x: Any) -> bool:
        """Check if x is a morphism (instance of morphism_class) in this category."""
        ...

    @final
    @abstractmethod
    def is_product_C(self, x: CategoryABCs.Object) -> bool:
        """Check if x is a product in this category."""
        ...

    @final
    @abstractmethod
    def is_coproduct_C(self, x: CategoryABCs.Object) -> bool:
        """Check if x is a coproduct in this category."""
        ...

    # Existence of compositional structures
    @final
    @abstractmethod
    def is_pullback_C(self, x: CategoryABCs.Object) -> bool:
        """Check if x is a pullback in this category."""
        ...

    @final
    @abstractmethod
    def is_pushout_C(self, x: CategoryABCs.Object) -> bool:
        """Check if x is a pushout in this category."""
        ...

    @final
    @abstractmethod
    def is_direct_sum_C(self, x: CategoryABCs.Object) -> bool:
        """Check if x is a direct sum in this category."""
        ...

    @final
    @abstractmethod
    def is_tensor_product_C(self, x: CategoryABCs.Object) -> bool:
        """Check if x is a tensor product in this category."""
        ...

    @final
    @abstractmethod
    def is_slice_object_C(self, x: CategoryABCs.Object) -> bool: ...

    @final
    @abstractmethod
    def is_coslice_object_C(self, x: CategoryABCs.Object) -> bool: ...

    @final
    @abstractmethod
    def __contains__(self, x: Any) -> bool: ...

class Limit_C_Classes(ABC):

    @classmethod
    @final
    @abstractmethod
    def product_class(cls) -> type[CategoryABCs.Product]: ...

    @classmethod
    @final
    @abstractmethod
    def coproduct_class(cls) -> type[CategoryABCs.Coproduct]: ...

    @classmethod
    @final
    @abstractmethod
    def pullback_class(cls) -> type[CategoryABCs.Pullback]: ...

    @classmethod
    @final
    @abstractmethod
    def pushout_class(cls) -> type[CategoryABCs.Pushout]: ...

    @classmethod
    @final
    @abstractmethod
    def direct_sum_class(cls) -> type[CategoryABCs.DirectSum]: ...

    @classmethod
    @final
    @abstractmethod
    def tensor_product_class(cls) -> type[CategoryABCs.TensorProduct]: ...

    @classmethod
    @final
    @abstractmethod
    def slice_class(cls) -> type[CategoryABCs.Slice]: ...

    @classmethod
    @final
    @abstractmethod
    def coslice_class(cls) -> type[CategoryABCs.Coslice]: ...

class Internal_Object_And_Morphism_Constructors(ABC):

    @final
    @abstractmethod
    def object_C_from(self, **cell_data: Any) -> CategoryABCs.Object:
        """Construct an object in C from given data."""
        ...

    @final
    @abstractmethod
    def morphism_C_from(self, **cell_data: Any) -> CategoryABCs.Cell:
        """Construct a morphism f: X -> Y in C from given data."""
        ...

    @final
    @abstractmethod
    def terminal_object_C(self) -> CategoryABCs.Object:
        """* in C."""
        ...

    @final
    @abstractmethod
    def initial_object_C(self) -> CategoryABCs.Object:
        """∅ in C."""
        ...

    @final
    @abstractmethod
    def zero_object_C(self) -> CategoryABCs.Object:
        """0 in C if C is pointed."""
        ...

    @final
    @abstractmethod
    def subobject_C(self, xs: Sequence[CategoryABCs.Element]) -> CategoryABCs.Object:
        """
        Construct the subobject ⟨x_1, ..., x_n⟩_C generated by the elements x in xs.
        """
        ...

    @final
    @abstractmethod
    def product_C(self, factors: Sequence[CategoryABCs.Object]) -> CategoryABCs.Object:
        """Returns the product of objects X_i in C, denoted ∏_i X_i."""
        ...

    @final
    @abstractmethod
    def coproduct_C(self, factors: Sequence[CategoryABCs.Object]) -> CategoryABCs.Object:
        """Returns the coproduct of objects X_i in C, denoted ∐_i X_i."""
        ...

    @final
    @abstractmethod
    def pullback_C(
        self, f1: CategoryABCs.OneMorphism, f2: CategoryABCs.OneMorphism
    ) -> CategoryABCs.Object:
        """Returns the pullback of morphisms f_1: X → Z, f_2: Y → Z, denoted X ×_Z Y."""
        ...

    @final
    @abstractmethod
    def pushout_C(
        self, f1: CategoryABCs.OneMorphism, f2: CategoryABCs.OneMorphism
    ) -> CategoryABCs.Object:
        """Returns the pushout of morphisms f_1: Z → X, f_2: Z → Y, denoted X +^Z Y."""
        ...

    @final
    @abstractmethod
    def tensor_C(self, factors: Sequence[CategoryABCs.Object]) -> CategoryABCs.Object:
        """Returns the tensor product of objects X_i in C, denoted ⨂_i X_i."""
        ...

    @final
    @abstractmethod
    def directsum_C(self, factors: Sequence[CategoryABCs.Object]) -> CategoryABCs.Object:
        """Returns the direct sum of objects X_i in C, denoted ⊕_i X_i."""
        ...

    @final
    @abstractmethod
    def diagonal_morphism_C(self, x: CategoryABCs.Object) -> CategoryABCs.OneMorphism:
        """Returns the diagonal morphism Δ: X → X × X."""
        ...

    @final
    @abstractmethod
    def codiagonal_morphism_C(self, x: CategoryABCs.Object) -> CategoryABCs.OneMorphism: ...

    @final
    @abstractmethod
    def subobjects_C_of(self, x: CategoryABCs.Object) -> Sequence[CategoryABCs.Object]:
        """Return a list of all subobjects of C in A."""
        ...

    @final
    @abstractmethod
    def quotients_C_of(self, x: CategoryABCs.Object) -> Sequence[CategoryABCs.Object]:
        """Return a list of all quotient objects of this object in the ambient category."""
        ...

    @final
    @abstractmethod
    def superobjects_C_of(self) -> Sequence[CategoryABCs.Object]:
        """Return a list of all superobjects of this object in the ambient category."""
        ...

    @final
    @abstractmethod
    def dual_C(self, x: CategoryABCs.Object, additive: bool = False) -> CategoryABCs.Nontrivial_TwoCategory: ...

    @final
    @abstractmethod
    def cofiber_C(self, f: CategoryABCs.OneMorphism) -> CategoryABCs.Object: ...

    @final
    @abstractmethod
    def fiber_C(self, y: CategoryABCs.Object, f: CategoryABCs.OneMorphism) -> CategoryABCs.Object: ...

    @final
    @abstractmethod
    def kernel_C(self, f: CategoryABCs.OneMorphism) -> CategoryABCs.Object: ...

    @final
    @abstractmethod
    def quotient_C(
        self, data: CategoryABCs.OneMorphism | CategoryABCs.Object
    ) -> CategoryABCs.Object: ...

    @final
    @abstractmethod
    def multiplicative_unit_C(self) -> CategoryABCs.Object: ...

    @final
    @abstractmethod
    def additive_unit_C(self) -> CategoryABCs.Object: ...

class Object_Enumerating_And_Sampling(ABC):

    @final
    @abstractmethod
    def __iter__(self) -> Iterator[CategoryABCs.Object]: ...

    @final
    @abstractmethod
    def __next__(self) -> CategoryABCs.Object: ...

    @final
    @abstractmethod
    def __getitem__(self, x: Any) -> Any: ...

    @final
    @abstractmethod
    def an_object(self) -> CategoryABCs.Object:
        """Return an arbitrary object in C."""
        ...

    @final
    @abstractmethod
    def some_objects(self) -> CategoryABCs.Object:
        """Return an arbitrary object in C."""
        ...

    @final
    @abstractmethod
    def a_morphism(self) -> CategoryABCs.OneMorphism:
        """Return an arbitrary morphism in C."""
        ...

    @final
    @abstractmethod
    def some_morphisms(self) -> CategoryABCs.OneMorphism:
        """Return an arbitrary morphism in C."""
        ...

    @final
    @abstractmethod
    def random_object(self) -> CategoryABCs.Object:
        """Return a random object in C."""
        ...
    
    @abstractmethod
    def random_objects(self, n: int | None = 5) -> Sequence[CategoryABCs.Object]: 
        ...

    @final
    @abstractmethod
    def random_morphism(self) -> CategoryABCs.OneMorphism:
        """Return a random morphism in C."""
        ...

    @abstractmethod
    def random_morphisms(self, n: int | None = 5) -> Sequence[CategoryABCs.OneMorphism]: 
        ...

class Element_Enumerating_And_Sampling(ABC):
    
    @final
    @abstractmethod
    def __iter__(self) -> Iterator[CategoryABCs.Element]: ...
    
    @final
    @abstractmethod
    def __next__(self) -> CategoryABCs.Element: ...
    
    @final
    @abstractmethod
    def __getitem__(self, x: Any) -> Any: ...
    
    @final
    @abstractmethod
    def an_element(self) -> CategoryABCs.Element:
        """Return an arbitrary element in C."""
        ...
    
    @final
    @abstractmethod
    def random_element(self) -> CategoryABCs.Element:
        """Return a random element in C."""
        ...

    @abstractmethod
    def random_elements(self, n: int | None = 5) -> Sequence[CategoryABCs.Element]: 
        ...
