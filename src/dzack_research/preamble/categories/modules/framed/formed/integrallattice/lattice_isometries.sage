r"""Isometries of integral lattices."""

from typing import Any

from sage.categories.category import Category
from sage.matrix.special import identity_matrix


class LatticeIsometries(Category):
    r"""Invertible lattice homomorphisms."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "lattice isometries"

    def super_categories(self) -> list:
        return [LatticeHomomorphisms()]

    class ParentMethods:
        def __call__(self: Any, images: Any, *args: Any, **kwargs: Any) -> Any:
            morphism = LatticeHomomorphisms.ParentMethods.__call__(
                self,
                images,
            )
            determinant = morphism.matrix().det()
            assert determinant in (ZZ.one(), -ZZ.one()), (
                f"an integral isometry has unit determinant, got {determinant}"
            )
            return refine(morphism, LatticeIsometries())

        def one(self: Any) -> Any:
            return self(
                {
                    label: self.domain().generator(label)
                    for label in self.domain().generating_set()
                }
            )

        def subgroup(self: Any, generators: Any) -> Any:
            generators = tuple(generators)
            assert all(generator in self for generator in generators), (
                "each subgroup generator must belong to this isometry group"
            )
            return LatticeIsometrySubgroup(self, generators)

    class MorphismMethods:
        def to_matrix(self: Any) -> Any:
            return self.matrix()

        def is_identity(self: Any) -> bool:
            matrix_ = self.matrix()
            return bool(
                matrix_
                == identity_matrix(ZZ, matrix_.nrows())
            )

        def is_involution(self: Any) -> bool:
            return (self * self).is_identity()

        def __mul__(self: Any, other: Any) -> Any:
            assert (
                isinstance(other, FormMorphism)
                and other.parent() is self.parent()
            ), "composition is internal to one isometry group"
            return self.parent()(
                {
                    label: self(other.domain().generator(label))
                    for label in other.domain().generating_set()
                }
            )

        def inverse(self: Any) -> Any:
            inverse_matrix = self.matrix().inverse()
            return self.parent()(
                {
                    label: self.domain().linear_combination(row)
                    for label, row in zip(
                        self.domain().generating_set(),
                        inverse_matrix.rows(),
                    )
                }
            )

        def cyclic_subgroup(self: Any) -> Any:
            return self.parent().subgroup([self])


class LatticeIsometrySubgroup(FormAutomorphismGroup):
    r"""A finite literal subgroup of \(O(L)\)."""

    def __init__(self, supergroup: Any, generators: Any) -> None:
        lattice = supergroup.domain()
        assert supergroup.codomain() is lattice, (
            "an isometry group is an endomorphism homset"
        )
        FormAutomorphismGroup.__init__(self, lattice)
        refine(self, [LatticeHomomorphisms(), LatticeIsometries()])
        supplied = tuple(generators)
        assert supplied, "a generated subgroup needs a generator"
        assert all(generator.parent() is supergroup for generator in supplied), (
            "each subgroup generator must belong to the stated isometry group"
        )
        self._generators = tuple(
            self(
                {
                    label: generator(lattice.generator(label))
                    for label in lattice.generating_set()
                }
            )
            for generator in supplied
        )
        self._elements = self._close()

    def gens(self) -> tuple:
        return self._generators

    def is_finite(self) -> bool:
        return True

    def order(self) -> int:
        return len(self._elements)

    def __iter__(self):
        return iter(self._elements)

    def __contains__(self, element: Any) -> bool:
        return isinstance(element, FormMorphism) and element.parent() is self

    def _close(self) -> tuple:
        identity = self.one()
        elements = {identity}
        frontier = [identity]
        steps = 0
        while frontier:
            current = frontier.pop()
            for generator in self._generators:
                for factor in (generator, generator.inverse()):
                    candidate = current * factor
                    if candidate in elements:
                        continue
                    elements.add(candidate)
                    frontier.append(candidate)
                    steps += 1
                    assert steps <= 100000, (
                        "the proposed isometry subgroup did not close finitely"
                    )
        return tuple(elements)

    def _repr_(self) -> str:
        return f"Subgroup of O({self.domain()}) of order {self.order()}"
