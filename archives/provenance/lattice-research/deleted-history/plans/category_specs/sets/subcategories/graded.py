r"""Axiomatic subcategory of graded sets."""

from __future__ import annotations

from typing import TYPE_CHECKING, final, override

from sage.categories.sets_with_grading import SetsWithGrading as SageSetsWithGrading
from sage.misc.abstract_method import abstract_method

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom

if TYPE_CHECKING:
    from ...types import GradedSet, Set, SetElement, SetGeneratingSeries

from .. import Sets


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
        @abstract_method
        def grading_set(self) -> Set:
            r"""Return the set of grades indexing the graded components."""
            ...

        @abstract_method(optional=True)
        def subset(self, grade: SetElement) -> Set:
            r"""Return the subset of elements with grade ``grade``."""
            ...

        @abstract_method
        def graded_component(self, grade: SetElement) -> Set:
            r"""Return the component of elements of grade ``grade``."""
            ...

        @abstract_method
        def grading(self, elt: SetElement) -> SetElement:
            r"""Return the grade of ``elt``."""
            ...

        @abstract_method
        def generating_series(self) -> SetGeneratingSeries:
            r"""Return the generating series of graded-component cardinalities."""
            ...

    class ElementMethods: ...
    class MorphismMethods: ...


GradedSetsObject = GradedSetsCategory.ParentMethods
GradedSetsElement = GradedSetsCategory.ElementMethods
GradedSetsMorphism = GradedSetsCategory.MorphismMethods
