r"""Free modules on arbitrary sets.

``FreeModuleOnSet(R, S)`` realizes

\[
    F_R(S)=\{a:S\to R\mid \operatorname{supp}(a)\text{ is finite}\}.
\]

The set \(S\) is construction data.  It need not be finite, countable, or
ordered.  Finite ordered free modules are the specialization implemented by
``BasedFreeModule``.
"""


from dzack_research.preamble.categories.rings.rings import OwnedBaseRing
from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing
from typing import Self, TYPE_CHECKING

from sage.categories.homset import Hom
from sage.categories.morphism import SetMorphism
from sage.structure.element import ModuleElement
from sage.structure.parent import Parent
from sage.structure.richcmp import richcmp

from sage_lattice_category_spike.objects.sets import Sets
from sage_lattice_category_spike.objects.underlying_sets import UnderlyingSet

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from sage_lattice_category_spike.lexicon import OrderedSet


class FramedFreeModules(OwnedCategoryOverBaseRing):
    r"""Free modules equipped with the canonical map \(S\to U(F_R(S))\)."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "framed free modules"

    def super_categories(self) -> list:
        return [FreeModules(self.base_ring()), Modules(self.base_ring()).Framed()]

    class ParentMethods:
        def module_generator_morphism(self: Self) -> SetMorphism:
            r"""Return the canonical set morphism \(S\to U(F_R(S))\)."""
            morphism = self.__dict__.get("_free_module_generator_morphism")
            if morphism is None:
                module_generating_set = self.__dict__.get("_module_generating_set")
                assert (
                    module_generating_set is not None
                ), "a framed free module stores its framing set"
                morphism = SetMorphism(
                    Hom(module_generating_set, UnderlyingSet(self), Sets()),
                    self._module_generator_element,
                )
                self._free_module_generator_morphism = morphism
            return morphism

        def hom(self: Self, images: dict, codomain: "Module" = None) -> "ModuleMorphism":
            r"""Extend a set morphism \(S\to U(N)\) \(R\)-linearly."""
            match images:
                case SetMorphism():
                    assert isinstance(images.codomain(), UnderlyingSet), (
                        "a generator morphism lands in the underlying set of "
                        "its module codomain"
                    )
                    target = images.codomain().structured_parent()
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
                    assert False, (
                        "a map from a general free module is specified by a "
                        "set morphism from its generating set"
                    )
            return self.Hom(target)(images)

        def is_torsion_free(self: Self) -> bool:
            return True


class FreeModuleOnSetElement(ModuleElement):
    r"""A finitely supported coefficient function on the set \(S\)."""

    def __init__(self, parent: "Parent", coefficients: dict) -> None:
        ModuleElement.__init__(self, parent)
        coefficients = dict(coefficients)
        assert all(
            element_of_S in parent.module_generating_set()
            for element_of_S in coefficients
        ), f"the coefficient function is not supported on {parent.module_generating_set()}"
        self._coefficients = {
            element_of_S: coefficient
            for element_of_S, value in coefficients.items()
            if (coefficient := parent.base_ring()(value)) != 0
        }

    def coefficients(self) -> dict:
        return dict(self._coefficients)

    def _add_(self, other: object) -> "FreeModuleOnSetElement":
        zero = self.parent().base_ring().zero()
        support = self._coefficients.keys() | other._coefficients.keys()
        return self.parent().element_class(
            self.parent(),
            {
                element_of_S: (
                    self._coefficients.get(element_of_S, zero)
                    + other._coefficients.get(element_of_S, zero)
                )
                for element_of_S in support
            },
        )

    def _sub_(self, other: object) -> "FreeModuleOnSetElement":
        return self._add_(-other)

    def _neg_(self) -> "FreeModuleOnSetElement":
        return self.parent().element_class(
            self.parent(),
            {
                element_of_S: -coefficient
                for element_of_S, coefficient in self._coefficients.items()
            },
        )

    def _lmul_(self, factor: "RingElement") -> "FreeModuleOnSetElement":
        factor = self.parent().base_ring()(factor)
        return self.parent().element_class(
            self.parent(),
            {
                element_of_S: factor * coefficient
                for element_of_S, coefficient in self._coefficients.items()
            },
        )

    _rmul_ = _lmul_

    def _richcmp_(self, other: object, op: int) -> bool:
        return richcmp(self._coefficients, other._coefficients, op)

    def __hash__(self) -> int:
        return hash(frozenset(self._coefficients.items()))

    def underlying_set_element(self) -> "Element":
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


class FreeModuleOnSet(OwnedBaseRing, Parent):
    r"""The free \(R\)-module on the actual set \(S\)."""

    Element = FreeModuleOnSetElement

    def __init__(
        self,
        base_ring: "Ring",
        module_generating_set: "OrderedSet",
        category: "Category" = None,
    ) -> None:
        r"""Frame a free module on ``module_generating_set``.

        ``category`` is what a subclass already knows itself to be: a free
        algebra is one at construction, not after a later refinement, and
        Sage installs a parent's structural surface -- the coercion from the
        base ring among it -- from the category ``Parent.__init__`` is given.
        """
        # Intake: the module is built over the ring the engine computes in,
        # whichever of the two names for it arrived.  A module over the owned
        # view would carry a base its category, its matrices and its Smith
        # forms do not share.  ``base_ring`` reports the name back.
        base_ring = engine_ring(base_ring)
        module_generating_set = _as_set(module_generating_set)
        self._module_generating_set = module_generating_set
        if category is None:
            category = FramedFreeModules(base_ring)
        Parent.__init__(self, base=base_ring, category=category)
        refine(self, category)
        if module_generating_set in Sets().Finite():
            refine(self, FinitelyGeneratedFreeModules(base_ring))
        self._framing_morphism = framing_morphism(
            self,
            self,
            self._module_generator_element,
        )

    def module_generating_set(self) -> Parent:
        return self._module_generating_set

    def framing_morphism(self) -> "FramingMorphism":
        return self._framing_morphism

    def _module_generator_element(self, element_of_S: "Element") -> FreeModuleOnSetElement:
        assert element_of_S in self._module_generating_set, (
            f"{element_of_S!r} is not in {self._module_generating_set}"
        )
        return self.element_class(
            self,
            {element_of_S: self.base_ring().one()},
        )

    def zero(self) -> FreeModuleOnSetElement:
        return self.element_class(self, {})

    def _element_constructor_(self, value: "Element") -> FreeModuleOnSetElement:
        assert isinstance(value, FreeModuleOnSetElement) and value.parent() is self, (
            f"{value} is not an element of {self}"
        )
        return value

    def __contains__(self, value: "Element") -> bool:
        return isinstance(value, FreeModuleOnSetElement) and value.parent() is self

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, FreeModuleOnSet)
            and self.base_ring() == other.base_ring()
            and self._module_generating_set == other._module_generating_set
        )

    def __hash__(self) -> int:
        return hash((type(self), self.base_ring(), self._module_generating_set))

    def _repr_(self) -> str:
        return f"Free {self.base_ring()}-module on {self._module_generating_set}"


def FreeModuleOn(base_ring: "Ring", module_generating_set: "OrderedSet") -> FreeModuleOnSet:
    r"""Construct \(F_R(S)\) on the supplied set \(S\)."""
    module_generating_set = _as_set(module_generating_set)
    set_category = module_generating_set.category()
    match (
        set_category.is_subcategory(Sets().Finite()),
        set_category.is_subcategory(Sets().TotallyOrdered()),
    ):
        case (True, True):
            return BasedFreeModule(base_ring, module_generating_set)
        case (True, False) | (False, True) | (False, False):
            return FreeModuleOnSet(base_ring, module_generating_set)
