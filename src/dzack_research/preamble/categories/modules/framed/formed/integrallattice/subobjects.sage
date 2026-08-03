r"""Subobjects represented by monomorphisms.

A subobject is the pair \((A,\iota:A\hookrightarrow B)\).  The construction
does not mutate \(A\): the same object may occur in several slice objects
through different monomorphisms.
"""

from typing import Any

from sage.categories.category import Category
from sage.structure.parent import Parent

from sage_lattice_category_spike.objects.sets import Sets


class Subobjects(Category):
    r"""Objects of a slice category represented by a chosen monomorphism."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "subobjects"

    def super_categories(self) -> list:
        return [Sets()]

    class ParentMethods:
        def underlying_object(self: Any) -> Any:
            return self._underlying_object

        def embedding(self: Any) -> Any:
            return self._embedding

        def embedding_codomain(self: Any) -> Any:
            return self._embedding.codomain()

        def index(self: Any) -> Any:
            return self._embedding.index()

        def gens(self: Any) -> Any:
            return self._underlying_object.gens()

        def generating_set(self: Any) -> Any:
            return self._underlying_object.generating_set()

        def generator_morphism(self: Any) -> Any:
            return self._underlying_object.generator_morphism()

        def generator(self: Any, element_of_S: Any) -> Any:
            return self.generator_morphism()(element_of_S)

        def rank(self: Any) -> Any:
            return self._underlying_object.rank()

        def basis(self: Any) -> Any:
            return self._underlying_object.basis()

        def zero(self: Any) -> Any:
            return self._underlying_object.zero()

        def is_zero(self: Any) -> bool:
            return self._underlying_object.is_zero()

        def linear_combination(self: Any, coefficients: Any) -> Any:
            return self._underlying_object.linear_combination(coefficients)

        def gram_matrix(self: Any) -> Any:
            return self._underlying_object.gram_matrix()

        def form(self: Any) -> Any:
            return self._underlying_object.form()

        def forget_form(self: Any) -> Any:
            return self._underlying_object.forget_form()

        def group(self: Any) -> Any:
            return self._underlying_object.group()

        def action(self: Any) -> Any:
            return self._underlying_object.action()

        def embedded_gens(self: Any) -> Any:
            return finite_ordered_set(
                tuple(
                    self._embedding(generator)
                    for generator in self._underlying_object.gens()
                )
            )

        embedded_elements = embedded_gens

        def isotropic_reduction(self: Any) -> Any:
            assert self.gram_matrix().is_zero(), (
                "isotropic reduction requires the form to vanish on the subobject"
            )
            codomain = self.embedding_codomain()
            perpendicular = self.embedding().orthogonal_complement()
            inclusion = perpendicular.embedding()
            relations = matrix(
                ZZ,
                [
                    _coordinate_vector(
                        inclusion.lift(image)
                    )
                    for image in self.embedded_gens()
                ],
            )
            lifts = _free_quotient_lifts(perpendicular.rank(), relations)
            generators = tuple(
                perpendicular.linear_combination(lift)
                for lift in lifts
            )
            gram = matrix(
                ZZ,
                [
                    [
                        left.b(right)
                        for right in generators
                    ]
                    for left in generators
                ],
            )
            return codomain._sub_form_module(
                gram,
                finite_ordered_set(generators),
            )


class SubobjectObject(Parent):
    r"""The slice object \((A,\iota:A\hookrightarrow B)\)."""

    def __init__(self, embedding: Any) -> None:
        self._underlying_object = embedding.domain()
        self._embedding = embedding
        Parent.__init__(
            self,
            base=self._underlying_object.base_ring(),
            category=Subobjects(),
        )

    def __contains__(self, element: Any) -> bool:
        return element in self._underlying_object

    def _repr_(self) -> str:
        return (
            f"Subobject ({self._underlying_object}, "
            f"{self._embedding}) of {self._embedding.codomain()}"
        )


def _free_quotient_lifts(rank: Any, relations: Matrix) -> list:
    from sage.modules.free_module import FreeModule as _sage_free_module

    free = _sage_free_module(ZZ, rank)
    quotient = free / free.submodule(matrix(ZZ, relations).rows())
    return [generator.lift() for generator in quotient.gens()]


def Subobject(embedding: Any) -> SubobjectObject:
    r"""Construct the slice object represented by ``embedding``."""
    assert isinstance(embedding, (ModuleMorphism, FormMorphism)), (
        "a module subobject is represented by a module or form morphism"
    )
    assert embedding.is_injective(), (
        "the structure morphism of a subobject must be a monomorphism"
    )
    return SubobjectObject(embedding)
