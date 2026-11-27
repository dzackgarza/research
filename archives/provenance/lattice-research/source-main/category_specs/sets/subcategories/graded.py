r"""Axiomatic subcategory of graded sets."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Callable
from typing import TYPE_CHECKING, TypeVar, cast, final, override

from sage.categories.sets_with_grading import SetsWithGrading as SageSetsWithGrading
from sage.misc.abstract_method import abstract_method

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom

if TYPE_CHECKING:
    from ...types import Set, SetElement, SetGeneratingSeries

_MethodT = TypeVar("_MethodT", bound=Callable[..., object])


def _optional_abstractmethod[_MethodT: Callable[..., object]](method: _MethodT) -> _MethodT:  # noqa: E501
    return cast(_MethodT, abstract_method(optional=True)(method))


from .. import Sets  # noqa: E402
from ..homsets import SetHomCategory  # noqa: E402


class GradedSetsCategory(CategoryWithAxiom):
    r"""Sets equipped with a grading map to a grading set.

    Canonical chain: ``Sets().Graded()``.
    """

    _base_category_class_and_axiom = (Sets, "Graded")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "graded sets"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [Sets(), SageSetsWithGrading()]

    class ParentMethods:
        @abstractmethod
        def grading_set(self) -> Set:
            r"""Return the set of grades indexing the graded components."""
            ...

        @_optional_abstractmethod
        @abstractmethod
        def subset(self, grade: SetElement) -> Set:
            r"""Return the subset of elements with grade ``grade``."""
            ...

        @abstractmethod
        def graded_component(self, grade: SetElement) -> Set:
            r"""Return the component of elements of grade ``grade``."""
            ...

        @abstractmethod
        def grading(self, elt: SetElement) -> SetElement:
            r"""Return the grade of ``elt``."""
            ...

        @abstractmethod
        def generating_series(self) -> SetGeneratingSeries:
            r"""Return the generating series of graded-component cardinalities."""
            ...

    class ElementMethods: ...



GradedSetsObject = GradedSetsCategory.ParentMethods
GradedSetsElement = GradedSetsCategory.ElementMethods
GradedSetsMorphism = SetHomCategory.ElementMethods
