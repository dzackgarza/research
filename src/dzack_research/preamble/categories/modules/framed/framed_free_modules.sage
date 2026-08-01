r"""Free modules on arbitrary sets.

``FreeModuleOnSet(R, S)`` realizes

\[
    F_R(S)=\{a:S\to R\mid \operatorname{supp}(a)\text{ is finite}\}.
\]

The set \(S\) is construction data.  It need not be finite, countable, or
ordered.  Finite ordered free modules are the specialization implemented by
``BasedFreeModule``.
"""

from typing import Any

from sage.categories.category_types import Category_over_base_ring
from sage.categories.sets_cat import Sets as SageSets
from sage.sets.set import Set
from sage.structure.element import ModuleElement
from sage.structure.parent import Parent
from sage.structure.richcmp import richcmp


class FramedFreeModules(Category_over_base_ring):
    r"""Free modules with a specified basis-indexing set."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "framed free modules"

    def super_categories(self) -> list:
        return [FreeModules(self.base_ring()), Modules(self.base_ring()).Framed()]

    class ParentMethods:
        def basis(self):
            r"""Return the basis as the image of the basis-indexing set."""
            return self.gens()

        def linear_combination(self: Any, terms: Any) -> Any:
            r"""Return the finite sum specified by ``label -> coefficient``."""
            match terms:
                case dict():
                    items = terms.items()
                case _:
                    items = terms
            total = self.zero()
            for label, coefficient in items:
                total += self.base_ring()(coefficient) * self.monomial(label)
            return total

        def hom(self: Any, images: Any, codomain: Any = None) -> Any:
            r"""Construct the map determined by its values on basis labels."""
            match images:
                case dict():
                    assert images, (
                        "an empty assignment does not determine its codomain; "
                        "construct it through M.Hom(N)"
                    )
                    target = next(iter(images.values())).parent()
                case _ if callable(images):
                    assert codomain is not None, (
                        "a basis-image function requires its codomain"
                    )
                    target = codomain
                case _:
                    raise TypeError(
                        "a map from a general free module is specified by a "
                        "dictionary or function on its basis-indexing set"
                    )
            return self.Hom(target)(images)

        def is_torsion_free(self: Any) -> bool:
            return True


class FreeModuleOnSetElement(ModuleElement):
    r"""A finitely supported function from the basis-indexing set to \(R\)."""

    def __init__(self, parent: Any, coefficients: Any) -> None:
        ModuleElement.__init__(self, parent)
        normalized = {}
        for label, coefficient in dict(coefficients).items():
            assert label in parent.basis_index_set(), (
                f"{label!r} does not index a basis element of {parent}"
            )
            coefficient = parent.base_ring()(coefficient)
            if coefficient != 0:
                normalized[label] = coefficient
        self._coefficients = normalized

    def coefficients(self) -> dict:
        return dict(self._coefficients)

    def _add_(self, other: Any) -> "FreeModuleOnSetElement":
        result = self.coefficients()
        for label, coefficient in other._coefficients.items():
            result[label] = result.get(label, self.parent().base_ring().zero()) + coefficient
            if result[label] == 0:
                del result[label]
        return self.parent().element_class(self.parent(), result)

    def _sub_(self, other: Any) -> "FreeModuleOnSetElement":
        return self._add_(-other)

    def _neg_(self) -> "FreeModuleOnSetElement":
        return self.parent().element_class(
            self.parent(),
            {label: -coefficient for label, coefficient in self._coefficients.items()},
        )

    def _lmul_(self, factor: Any) -> "FreeModuleOnSetElement":
        factor = self.parent().base_ring()(factor)
        return self.parent().element_class(
            self.parent(),
            {label: factor * coefficient for label, coefficient in self._coefficients.items()},
        )

    _rmul_ = _lmul_

    def _richcmp_(self, other: Any, op: int) -> bool:
        return richcmp(self._coefficients, other._coefficients, op)

    def __hash__(self) -> int:
        return hash(frozenset(self._coefficients.items()))

    def _repr_(self) -> str:
        if not self._coefficients:
            return "0"
        return " + ".join(
            f"{coefficient}*e[{label!r}]"
            for label, coefficient in self._coefficients.items()
        )


class FreeModuleOnSet(Parent):
    r"""The free \(R\)-module on the actual set ``basis_index_set``."""

    Element = FreeModuleOnSetElement

    def __init__(self, base_ring: Any, basis_index_set: Any) -> None:
        if not isinstance(basis_index_set, Parent):
            basis_index_set = Set(basis_index_set)
        self._basis_index_set = basis_index_set
        Parent.__init__(
            self,
            base=base_ring,
            category=FramedFreeModules(base_ring),
        )
        refine(self, FramedFreeModules(base_ring))
        self._framing_morphism = framing_morphism(
            self,
            self,
            lambda label: self.monomial(label)
        )

    def basis_index_set(self) -> Parent:
        return self._basis_index_set

    def framing_morphism(self) -> "FramingMorphism":
        return self._framing_morphism

    def monomial(self, label: Any) -> FreeModuleOnSetElement:
        assert label in self._basis_index_set, (
            f"{label!r} is not in the basis-indexing set {self._basis_index_set}"
        )
        return self.element_class(self, {label: self.base_ring().one()})

    def zero(self) -> FreeModuleOnSetElement:
        return self.element_class(self, {})

    def _element_constructor_(self, value: Any) -> FreeModuleOnSetElement:
        assert isinstance(value, FreeModuleOnSetElement) and value.parent() is self, (
            f"{value} is not an element of {self}"
        )
        return value

    def __contains__(self, value: Any) -> bool:
        return isinstance(value, FreeModuleOnSetElement) and value.parent() is self

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, FreeModuleOnSet)
            and self.base_ring() == other.base_ring()
            and self._basis_index_set == other._basis_index_set
        )

    def __hash__(self) -> int:
        return hash((type(self), self.base_ring(), self._basis_index_set))

    def _repr_(self) -> str:
        return f"Free {self.base_ring()}-module on {self._basis_index_set}"


def FreeModuleOn(base_ring: Any, basis_index_set: Any) -> FreeModuleOnSet:
    r"""Construct \(F_R(S)\), specializing to the finite ordered realization."""
    if not isinstance(basis_index_set, Parent):
        basis_index_set = Set(basis_index_set)
    if basis_index_set in SageSets().Finite():
        return BasedFreeModule(base_ring, finite_ordered_set(basis_index_set))
    return FreeModuleOnSet(base_ring, basis_index_set)
