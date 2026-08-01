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
from sage.categories.homset import Hom
from sage.categories.morphism import SetMorphism
from sage.categories.sets_cat import Sets as SageSets
from sage.sets.set import Set
from sage.structure.element import ModuleElement
from sage.structure.parent import Parent
from sage.structure.richcmp import richcmp


class FramedFreeModules(Category_over_base_ring):
    r"""Free modules equipped with the canonical map \(S\to U(F_R(S))\)."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "framed free modules"

    def super_categories(self) -> list:
        return [FreeModules(self.base_ring()), Modules(self.base_ring()).Framed()]

    class ParentMethods:
        def generator_morphism(self: Any) -> SetMorphism:
            r"""Return the canonical set morphism \(S\to U(F_R(S))\)."""
            morphism = self._free_generator_morphism
            assert isinstance(morphism, SetMorphism), (
                "a framed free module stores its canonical generator morphism"
            )
            assert morphism.codomain() is self, (
                "the canonical generator morphism has the wrong codomain"
            )
            return morphism

        def basis(self):
            r"""Return the image of the canonical generator morphism."""
            return self.gens()

        def linear_combination(self: Any, terms: Any) -> Any:
            r"""Return the specified finite \(R\)-linear combination."""
            match terms:
                case dict():
                    items = terms.items()
                case _:
                    items = terms
            total = self.zero()
            for element_of_S, coefficient in items:
                total += (
                    self.base_ring()(coefficient)
                    * self.generator(element_of_S)
                )
            return total

        def hom(self: Any, images: Any, codomain: Any = None) -> Any:
            r"""Extend a set morphism \(S\to U(N)\) \(R\)-linearly."""
            match images:
                case SetMorphism():
                    target = images.codomain()
                case dict():
                    assert images, (
                        "an empty assignment does not determine its codomain; "
                        "construct it through M.Hom(N)"
                    )
                    target = next(iter(images.values())).parent()
                case _ if callable(images):
                    assert codomain is not None, (
                        "a generator function requires its codomain"
                    )
                    target = codomain
                case _:
                    raise TypeError(
                        "a map from a general free module is specified by a "
                        "set morphism from its generating set"
                    )
            return self.Hom(target)(images)

        def is_torsion_free(self: Any) -> bool:
            return True


class FreeModuleOnSetElement(ModuleElement):
    r"""A finitely supported coefficient function on the set \(S\)."""

    def __init__(self, parent: Any, coefficients: Any) -> None:
        ModuleElement.__init__(self, parent)
        normalized = {}
        for element_of_S, coefficient in dict(coefficients).items():
            assert element_of_S in parent.generating_set(), (
                f"{element_of_S!r} is not in {parent.generating_set()}"
            )
            coefficient = parent.base_ring()(coefficient)
            if coefficient != 0:
                normalized[element_of_S] = coefficient
        self._coefficients = normalized

    def coefficients(self) -> dict:
        return dict(self._coefficients)

    def _add_(self, other: Any) -> "FreeModuleOnSetElement":
        result = self.coefficients()
        for element_of_S, coefficient in other._coefficients.items():
            result[element_of_S] = (
                result.get(element_of_S, self.parent().base_ring().zero())
                + coefficient
            )
            if result[element_of_S] == 0:
                del result[element_of_S]
        return self.parent().element_class(self.parent(), result)

    def _sub_(self, other: Any) -> "FreeModuleOnSetElement":
        return self._add_(-other)

    def _neg_(self) -> "FreeModuleOnSetElement":
        return self.parent().element_class(
            self.parent(),
            {
                element_of_S: -coefficient
                for element_of_S, coefficient in self._coefficients.items()
            },
        )

    def _lmul_(self, factor: Any) -> "FreeModuleOnSetElement":
        factor = self.parent().base_ring()(factor)
        return self.parent().element_class(
            self.parent(),
            {
                element_of_S: factor * coefficient
                for element_of_S, coefficient in self._coefficients.items()
            },
        )

    _rmul_ = _lmul_

    def _richcmp_(self, other: Any, op: int) -> bool:
        return richcmp(self._coefficients, other._coefficients, op)

    def __hash__(self) -> int:
        return hash(frozenset(self._coefficients.items()))

    def underlying_set_element(self) -> Any:
        r"""Recover \(s\) when this element is the canonical generator \([s]\)."""
        assert len(self._coefficients) == 1, (
            "only an element in the image of the canonical generator morphism "
            "has one underlying element of S"
        )
        element_of_S, coefficient = next(iter(self._coefficients.items()))
        assert coefficient == self.parent().base_ring().one(), (
            "only an element in the image of the canonical generator morphism "
            "has one underlying element of S"
        )
        return element_of_S

    def _repr_(self) -> str:
        if not self._coefficients:
            return "0"
        return " + ".join(
            f"{coefficient}*[{element_of_S!r}]"
            for element_of_S, coefficient in self._coefficients.items()
        )


class FreeModuleOnSet(Parent):
    r"""The free \(R\)-module on the actual set \(S\)."""

    Element = FreeModuleOnSetElement

    def __init__(self, base_ring: Any, generating_set: Any) -> None:
        if not isinstance(generating_set, Parent):
            generating_set = Set(generating_set)
        self._generating_set = generating_set
        Parent.__init__(
            self,
            base=base_ring,
            category=FramedFreeModules(base_ring),
        )
        refine(self, FramedFreeModules(base_ring))
        self._free_generator_morphism = SetMorphism(
            Hom(generating_set, self, SageSets()),
            self._generator_element,
        )
        self._framing_morphism = framing_morphism(
            self,
            self,
            self._free_generator_morphism,
        )

    def generating_set(self) -> Parent:
        return self._generating_set

    def framing_morphism(self) -> "FramingMorphism":
        return self._framing_morphism

    def _generator_element(self, element_of_S: Any) -> FreeModuleOnSetElement:
        assert element_of_S in self._generating_set, (
            f"{element_of_S!r} is not in {self._generating_set}"
        )
        return self.element_class(
            self,
            {element_of_S: self.base_ring().one()},
        )

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
            and self._generating_set == other._generating_set
        )

    def __hash__(self) -> int:
        return hash((type(self), self.base_ring(), self._generating_set))

    def _repr_(self) -> str:
        return f"Free {self.base_ring()}-module on {self._generating_set}"


def FreeModuleOn(base_ring: Any, generating_set: Any) -> FreeModuleOnSet:
    r"""Construct \(F_R(S)\) on the supplied set \(S\)."""
    if not isinstance(generating_set, Parent):
        generating_set = Set(generating_set)
    set_category = generating_set.category()
    match (
        set_category.is_subcategory(SageSets().Finite()),
        set_category.is_subcategory(OrderedSets().TotallyOrdered()),
    ):
        case (True, True):
            return BasedFreeModule(base_ring, generating_set)
        case (True, False) | (False, True) | (False, False):
            return FreeModuleOnSet(base_ring, generating_set)
