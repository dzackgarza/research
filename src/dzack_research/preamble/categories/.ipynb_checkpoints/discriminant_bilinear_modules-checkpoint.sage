r"""Discriminant bilinear modules."""

from typing import Any

from sage.categories.category import Category
from sage.categories.sets_cat import Sets


class DiscriminantBilinearModules(Category):
    r"""Category of discriminant bilinear modules.

    The category's ``gram_matrix`` is the bilinear Gram matrix. Quadratic
    discriminant modules expose their associated bilinear form through
    :meth:`associated_bilinear_form`.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "discriminant bilinear modules"

    def super_categories(self) -> list:
        return [Sets()]

    class ParentMethods:
        r"""Methods available on discriminant bilinear modules."""

        def invariants(self: Any) -> tuple[Any, ...]:
            r"""Return the invariant factors of the underlying finite group."""
            return self._invariants

        def source_lattice(self: Any) -> Any:
            r"""Return the lattice \(L\) whose discriminant group carries this form."""
            return self._source_lattice

        def gram_matrix(self: Any) -> Any:
            r"""Return the bilinear Gram matrix."""
            return self._gram_matrix


class DiscriminantBilinearForm:
    r"""Concrete object in :class:`DiscriminantBilinearModules`."""

    def __init__(self, invariants: Any, source_lattice: Any, gram_matrix: Any) -> None:
        self._invariants = tuple(invariants)
        self._source_lattice = source_lattice
        self._gram_matrix = gram_matrix
        refine(self, DiscriminantBilinearModules())
