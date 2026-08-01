r"""Finitely presented modules over a base ring.

Defines ``FinitelyPresentedModules`` as the category of finitely presented modules over a base ring $R$,
declaring ``FinitelyGeneratedModules(R)`` in its supercategories.
"""

from typing import Any

from sage.categories.category_types import Category_over_base_ring
from sage.categories.homset import Hom
from sage.categories.morphism import SetMorphism
from sage.categories.sets_cat import Sets as SageSets
from sage.matrix.constructor import matrix
from sage.matrix.matrix0 import Matrix
from sage.modules.free_module_element import vector
from sage.rings.integer_ring import ZZ
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.structure.richcmp import richcmp


class FinitelyPresentedModules(Category_over_base_ring):
    r"""Category of finitely presented modules over a base ring $R$."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "finitely presented modules"

    def super_categories(self) -> list:
        return [FinitelyGeneratedModules(self.base_ring())]

    class ParentMethods:
        def is_finitely_presented(self: Any) -> bool:
            r"""Return whether this module is finitely presented."""
            return True


class FinitelyPresentedModuleElement(Element):
    r"""An element of a presented module, reduced modulo its relations."""

    def __init__(self, parent: Any, coordinates: Any) -> None:
        Element.__init__(self, parent)
        self._coordinates_ = parent._reduce(coordinates)

    def _coordinates(self) -> Any:
        return self._coordinates_

    def _lift(self) -> Any:
        return self._coordinates_

    def _add_(self, other: Any) -> "FinitelyPresentedModuleElement":
        return self.parent()._from_coordinates(self._coordinates_ + other._coordinates_)

    def _sub_(self, other: Any) -> "FinitelyPresentedModuleElement":
        return self.parent()._from_coordinates(self._coordinates_ - other._coordinates_)

    def _neg_(self) -> "FinitelyPresentedModuleElement":
        return self.parent()._from_coordinates(-self._coordinates_)

    def _lmul_(self, factor: Any) -> "FinitelyPresentedModuleElement":
        return self.parent()._from_coordinates(
            self.parent().base_ring()(factor) * self._coordinates_
        )

    _rmul_ = _lmul_

    def _richcmp_(self, other: Any, op: int) -> bool:
        return richcmp(self._coordinates_, other._coordinates_, op)

    def __hash__(self) -> int:
        return hash(tuple(self._coordinates_))


class FinitelyPresentedModule(Parent):
    r"""The cokernel of a morphism of finite free modules.

    The relation morphism may have arbitrary rank, so this includes free,
    torsion, and mixed finitely presented modules.  The rows of its matrix are
    relations on the named generators of the codomain.
    """

    Element = FinitelyPresentedModuleElement

    def __init__(self, presentation: Any) -> None:
        assert isinstance(presentation, (ModuleMorphism, FormMorphism)), (
            "a presentation is a morphism of framed modules"
        )
        codomain = presentation.codomain()
        base_ring = codomain.base_ring()
        relations = matrix(base_ring, presentation.matrix())
        assert relations.ncols() == codomain.generating_set().cardinality(), (
            "the presentation matrix does not have the codomain's number of "
            "distinguished generators as its number of columns"
        )
        Parent.__init__(
            self,
            base=base_ring,
            category=FinitelyPresentedModules(base_ring),
        )
        self._presentation = presentation
        self._relations = relations
        self._normal_form = (
            relations.hermite_form(include_zero_rows=False)
            if base_ring is ZZ
            else relations.echelon_form()
        )
        refine(self, FinitelyPresentedModules(base_ring))
        if base_ring is ZZ and self.is_torsion():
            refine(self, FinitelyPresentedTorsionModules(base_ring))
        source = _underlying_module(codomain)
        source_generator_morphism = source.generator_morphism()
        quotient_generator_morphism = SetMorphism(
            Hom(
                source_generator_morphism.domain(),
                self,
                SageSets(),
            ),
            lambda element_of_S: self._from_coordinates(
                _coordinate_vector(
                    source_generator_morphism(element_of_S)
                )
            ),
        )
        self._framing_morphism = framing_morphism(
            source,
            self,
            quotient_generator_morphism,
        )

    def framing_morphism(self) -> "FramingMorphism":
        return self._framing_morphism

    def presentation(self) -> Any:
        return self._presentation

    def relation_matrix(self) -> Matrix:
        return self._relations

    def ngens(self) -> int:
        return self._relations.ncols()

    def rank(self) -> Any:
        return ZZ(self.ngens() - self._relations.rank())

    def is_torsion(self) -> bool:
        return self.base_ring() is ZZ and self.rank() == 0

    def is_torsion_free(self) -> bool:
        if self.base_ring() is not ZZ:
            return True
        smith = self._relations.smith_form()[0]
        return all(abs(entry) == 1 for entry in smith.diagonal() if entry != 0)

    def is_zero(self) -> bool:
        return all(generator == self.zero() for generator in self.gens())

    def invariants(self) -> tuple:
        assert self.base_ring() is ZZ, "invariants are defined here over ZZ"
        smith = self._relations.smith_form()[0]
        return tuple(
            abs(entry) for entry in smith.diagonal() if abs(entry) > 1
        )

    def cardinality(self) -> Any:
        assert self.is_torsion(), "a module with positive rank is infinite"
        result = ZZ.one()
        for invariant in self.invariants():
            result *= invariant
        return result

    def exponent(self) -> Any:
        invariants = self.invariants()
        return invariants[-1] if invariants else ZZ.one()

    def zero(self) -> FinitelyPresentedModuleElement:
        return self._from_coordinates(
            [self.base_ring().zero()] * self.ngens()
        )

    def linear_combination(self, coefficients: Any) -> FinitelyPresentedModuleElement:
        match coefficients:
            case dict():
                coefficients = tuple(
                    coefficients.get(element_of_S, self.base_ring().zero())
                    for element_of_S in self.generating_set()
                )
            case _:
                coefficients = tuple(coefficients)
        assert len(coefficients) == self.ngens(), (
            f"this module has {self.ngens()} generators, got {len(coefficients)}"
        )
        return self._from_coordinates(coefficients)

    def _reduce(self, coordinates: Any) -> Any:
        result = vector(self.base_ring(), list(coordinates))
        assert len(result) == self.ngens(), (
            f"this module has {self.ngens()} coordinates, got {len(result)}"
        )
        for row in self._normal_form.rows():
            pivot = next((i for i, entry in enumerate(row) if entry != 0), None)
            if pivot is None:
                continue
            if self.base_ring() is ZZ:
                coefficient = result[pivot] // row[pivot]
            else:
                coefficient = result[pivot] / row[pivot]
            result -= coefficient * row
        return result

    def reduce(self, coordinates: Any) -> Any:
        r"""Return the canonical representative modulo the presentation."""
        return self._reduce(coordinates)

    def _from_coordinates(self, coordinates: Any) -> FinitelyPresentedModuleElement:
        return self.element_class(self, coordinates)

    def _element_constructor_(self, x: Any) -> FinitelyPresentedModuleElement:
        assert isinstance(x, FinitelyPresentedModuleElement) and x.parent() is self, (
            f"{x} is not an element of {self}; construct classes using this "
            "module's generators or linear_combination"
        )
        return x

    def __contains__(self, x: Any) -> bool:
        return isinstance(x, FinitelyPresentedModuleElement) and x.parent() is self

    def _repr_(self) -> str:
        return (
            f"Finitely presented module on {self.ngens()} generators over "
            f"{self.base_ring()}"
        )
