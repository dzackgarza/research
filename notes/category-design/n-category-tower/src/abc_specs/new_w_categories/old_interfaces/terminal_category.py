# Origin: gitclones/integral_lattice/cat/src/abc_specs/new_w_categories/old_interfaces/terminal_category.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

from __future__ import annotations

from src._types import *
from src.local_typing import *

from .___cells import Cell
from .__arrows import Arrow
from .empty_category import (E_mor, E_obj, Empty_wCategory, _EmptyMorphism,
                             _EmptyObject)
from .scaffolding import wCategory


@dataclass
class Singleton_Object(Arrow.n0):

    _underlying_data: Any
    _ambient_category: wCategory

    @override
    def source(self) -> _EmptyObject:
        """A 0-arrow has (-1)-arrow source."""
        return E_obj

    @override
    def target(self) -> _EmptyObject:
        """A 0-arrow has (-1)-arrow target."""
        return E_obj

    @override
    def suspend(self) -> Arrow.n1:
        """Suspend to a 1-arrow in ΣC. Requires explicit construction."""
        raise NotImplementedError  # Suspension requires explicit 1-arrow construction

    @override
    def desuspend(self) -> Arrow.m1:
        """Desuspend to (-1)-arrow."""
        return _EmptyMorphism(
            _underlying_data=self,
            _ambient_category=self._ambient_category
        )

    @override
    def underlying_data(self) -> Any:
        return self._underlying_data

    @override
    def as_cell(self) -> Cell.m0:
        """Convert this arrow to a cell."""
        raise NotImplementedError

    def as_nm1_arrow(self) -> None:
        """Convert this arrow to a (-1)-arrow."""
        return None

    @override
    def amb(self) -> Arrow.n0 | None:
        """The ambient category containing this arrow."""
        return None  # wCategory is not an Arrow.n0; return None per ABC

    @override
    def identity_arrow(self) -> Identity_One_Morphism:
        """Return the identity arrow on this object."""
        return Identity_One_Morphism(_on_object=self)

    def ambient_category(self) -> wCategory:
        """Public getter for the ambient category."""
        return self._ambient_category

    @override
    def some_elements(self) -> Iterable[Arrow.m1]:
        """Return some elements of this object."""
        return [E_obj]

@dataclass
class Singleton_One_Morphism(Arrow.n1):
    _underlying_data: Callable[[Any], Any]
    _domain: Arrow.n0
    _codomain: Arrow.n0
    _ambient_category: wCategory
    _is_injective: BoolProof = field(default_factory=lambda: BoolProof.no_proof("No proof or disproof of injectivity known."))
    _is_surjective: BoolProof = field(default_factory=lambda: BoolProof.no_proof("No proof or disproof of surjectivity known."))

    @override
    def source(self) -> Arrow.n0:
        return self._domain

    @override
    def target(self) -> Arrow.n0:
        return self._codomain

    @override
    def suspend(self) -> Arrow.n2:
        raise NotImplementedError  # TODO: implement suspension construction.

    @override
    def desuspend(self) -> Arrow.n0:
        return self._ambient_category.object_from(self)

    @override
    def underlying_data(self) -> Callable[[Any], Any]:
        return lambda x: x

    @override
    def as_cell(self) -> Cell.m1:
        """Convert this arrow to a cell."""
        raise NotImplementedError

    @override
    def amb(self) -> Arrow.n0:
        """The ambient category containing this arrow."""
        return self._ambient_category.as_zero_arrow()

    @override
    def compose(self, other: Self) -> Self:
        """Compose this morphism with another."""
        return self

    @override
    def apply(
            self,
            x: Annotated[Any, lambda self: isinstance(self, Arrow.m1)]
        ) -> Arrow.m1:
        """Apply this morphism to an element/object."""
        return self.underlying_data()(x)

    @override
    def is_surjective(self) -> BoolProof:
        """Check if this morphism is surjective."""
        return self._is_surjective

    @override
    def is_injective(self) -> BoolProof:
        """Check if this morphism is injective."""
        return self._is_injective

class Identity_One_Morphism(Singleton_One_Morphism, Arrow.n1_auto):
    """Identity morphism on a singleton object. Is both endo and auto."""
    _on_object: Singleton_Object  # Set in __init__, not by dataclass

    def __init__(
        self,
        _on_object: Singleton_Object,
    ):
        self._on_object = _on_object
        super().__init__(
            _underlying_data=lambda x: x,
            _domain=self._on_object,
            _codomain=self._on_object,
            _ambient_category=self._on_object.ambient_category(),
            _is_injective=BoolProof.true("Identity morphism is injective."),
            _is_surjective=BoolProof.true("Identity morphism is surjective.")
        )

    def is_unipotent(self) -> BoolProof:
        """Identity is unipotent: id^n = id for all n."""
        return BoolProof.true("Identity morphism is unipotent by definition.")

    def inverse(self) -> Self:
        """Inverse of identity is itself."""
        return self
    

@dataclass
class Singleton_Hom_wCategory(wCategory):
    # Hom_C(x, y) = {f} ≃ * for some category C and objects x,y.

    _base_category: wCategory  # The category C such that self = Hom_C(x,y)
    _domain: Arrow.n0
    _codomain: Arrow.n0
    _id_f: Identity_One_Morphism = field(init=False)  # The morphism id_f: f -> f

    def __post_init__(self) -> None:
        """Initialize the singleton morphism after dataclass init."""
        singleton_obj = Singleton_Object(
            _underlying_data=None,
            _ambient_category=self
        )
        self._id_f = Identity_One_Morphism(_on_object=singleton_obj)

    @override
    def objects(self) -> type[Singleton_Object]: 
        return Singleton_Object

    @override
    def morphisms(self) -> type[Singleton_Hom_wCategory]: 
        return type(self)

    def identity_one_morphism(self) -> Identity_One_Morphism:
        return self._id_f

    @override
    def hom_category(self, x: Any, y: Any) -> Singleton_Hom_wCategory | Empty_wCategory:
        # Terminal hom category only has one object
        return Singleton_Hom_wCategory(
            _base_category=self,
            _domain=self._domain,
            _codomain=self._codomain
        )

    @override
    def object_from(self, x: Any) -> Singleton_Object:
        """Create a singleton object from data."""
        return Singleton_Object(_underlying_data=x, _ambient_category=self)

@dataclass
class Terminal_wCategory(wCategory):

    _singleton_x: Singleton_Object  # C = {x} ≃ *.
    _end_x: Singleton_Hom_wCategory
    
    def __init__(self, _singleton_x: Any) -> None:
        self._singleton_x = Singleton_Object(
            _underlying_data=_singleton_x,
            _ambient_category=self
        )
        self._end_x = self.hom_category(self._singleton_x, self._singleton_x)

    def identity_one_morphism(self) -> Identity_One_Morphism:
        """The identity 1-morphism id_x: x -> x in C."""
        return Identity_One_Morphism(_on_object=self._singleton_x)

    def identity_two_morphism(self) -> Identity_One_Morphism:
        """The identity 2-morphism id_{id_x} in Hom_C(x,x)."""
        return self._end_x.identity_one_morphism()

    @override
    def objects(self) -> type[Singleton_Object]: 
        return Singleton_Object

    @override
    def morphisms(self) -> type[Terminal_wCategory]: 
        return type(self)

    @override
    def hom_category(self, x: Any, y: Any) -> Singleton_Hom_wCategory:
        return Singleton_Hom_wCategory(
            _base_category=self,
            _domain=x,
            _codomain=y
        )

    @override
    def object_from(self, x: Any) -> Singleton_Object:
        """Create a singleton object from data."""
        return Singleton_Object(_underlying_data=x, _ambient_category=self)