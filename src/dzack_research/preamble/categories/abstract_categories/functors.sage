r"""Functors and natural transformations as arrows in the Cat type tower."""

from typing import TYPE_CHECKING

from sage.categories.category import Category as SageCategory
from sage.misc.cachefunc import cached_method
from sage.structure.element import Element as SageElement

from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    Isomorphism,
)
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    HomCategoryConstruction,
)
from dzack_research.preamble.owned_category_bases import (
    Category as OwnedCategory,
    CategoryWithParameters,
)

if TYPE_CHECKING:
    from collections.abc import Callable

    from sage.categories.category import Category
    from sage.categories.morphism import Morphism
    from sage.structure.parent import Parent
    from sage.structure.parent import MembershipInput

    from dzack_research.preamble.categories.abstract_categories.hom_categories import (
        HomCategoryOf,
    )

    type ObjectOfCategory = Parent | Category | SageElement


class _OnObjectSet:
    r"""The set of objects of a discrete category."""

    def __init__(self, object_set: "Parent") -> None:
        from dzack_research.preamble.categories.sets.owned_sets import Sets

        assert object_set in Sets()
        self._object_set = object_set
        super().__init__()

    def object_set(self) -> "Parent":
        return self._object_set

    def _make_named_class_key(self, name: str) -> SageCategory:
        return self._object_set.category()


class DiscreteCategories(OwnedCategory):
    r"""The full subcategory of :math:`\mathbf{Cat}` on discrete categories."""

    def super_categories(self) -> list[SageCategory]:
        return [Cat()]

    def __contains__(self, candidate: "MembershipInput") -> bool:
        match candidate:
            case DiscreteCategory():
                return True
            case _:
                return False


class DiscreteCategory(_OnObjectSet, CategoryWithParameters):
    r"""The discrete category on one set."""

    @property
    def ObjectType(self) -> type:
        return self._object_set.ElementType

    def objects(self) -> "Parent":
        return self._object_set

    def super_categories(self) -> list[SageCategory]:
        from sage.categories.objects import Objects

        return [Objects()]

    def __contains__(self, candidate: "MembershipInput") -> bool:
        return candidate in self._object_set

    def _repr_(self) -> str:
        return f"Discrete category on {self._object_set}"

    class _HomCategory(HomCategoryConstruction):
        r"""Identity arrows of a discrete category."""

        class ParentMethods:
            def identity(self) -> "DiscreteCategory.EndArrowType":
                assert self.domain() is self.codomain()
                return self.ObjectType(hom_category=self)

            def compose(
                self,
                second: "DiscreteCategory.ArrowType",
                first: "DiscreteCategory.ArrowType",
            ) -> "DiscreteCategory.ArrowType":
                assert first.codomain() is second.domain()
                assert self.domain() is first.domain()
                assert self.codomain() is second.codomain()
                return self.identity()

        class ElementMethods:
            def __init__(self, hom_category: SageCategory) -> None:
                super().__init__(hom_category=hom_category)


class Functor(Cat().ArrowType):
    r"""A functor, as an object of \(\operatorname{Hom}_{\mathbf{Cat}}(C,D)\)."""

    def __init__(
        self,
        domain: "Category",
        codomain: "Category",
        hom_category: "Category | None" = None,
    ) -> None:
        parent = Cat().Hom(domain, codomain) if hom_category is None else hom_category
        assert parent.domain() is domain
        assert parent.codomain() is codomain
        super().__init__(hom_category=parent)

    def _image_category(self) -> SageCategory:
        from dzack_research.preamble.categories.abstract_categories.functor_images import (
            ImageOfFunctor,
        )

        return ImageOfFunctor(self)

    @cached_method
    def Image(self) -> SageCategory:
        r"""Return the category of outputs with their chosen preimages."""
        return self._image_category()


class ImageInclusionFunctor(Functor):
    r"""The inclusion of a functor image into its codomain."""

    _faithful = True

    def __init__(self, image: SageCategory) -> None:
        self._image = image
        Functor.__init__(self, image, image.functor().codomain())

    def _apply_functor(self, obj: "ObjectOfCategory") -> "ObjectOfCategory":
        return obj

    def _apply_functor_to_morphism(self, morphism: "Morphism") -> "Morphism":
        return morphism

    def _repr_(self) -> str:
        return f"Inclusion of {self._image} into {self.codomain()}"


class IdentityFunctor(Functor):
    r"""The identity arrow of a category in \(\mathbf{Cat}\)."""

    _faithful = True

    def __init__(
        self,
        category: "Category",
        hom_category: "Category | None" = None,
    ) -> None:
        parent = Cat().Hom(category, category) if hom_category is None else hom_category
        Functor.__init__(self, category, category, hom_category=parent)

    def _apply_functor(
        self,
        obj: "ObjectOfCategory",
    ) -> "ObjectOfCategory":
        return obj

    def _apply_functor_to_morphism(self, morphism: "Morphism") -> "Morphism":
        return morphism

    def factors(self) -> tuple[Functor, ...]:
        return ()

    def _repr_(self) -> str:
        return f"Identity functor of {self.domain()}"


def compose_functors(
    second: Functor,
    first: Functor,
    hom_category: "Category | None" = None,
) -> Functor:
    r"""Return the flattened composite ``second`` after ``first``."""
    assert first.codomain() is second.domain(), (
        "functors compose only when their middle category agrees"
    )
    factors = first.factors() + second.factors()
    if not factors:
        return IdentityFunctor(first.domain(), hom_category=hom_category)
    if len(factors) == 1:
        return factors[0]
    return ComposedFunctor(factors, hom_category=hom_category)


class ComposedFunctor(Functor):
    r"""A flattened nonempty sequence of composable functors."""

    def __init__(
        self,
        factors: tuple[Functor, ...],
        hom_category: "Category | None" = None,
    ) -> None:
        assert factors
        for early, late in zip(factors, factors[1:]):
            assert early.codomain() is late.domain(), (
                "functors compose only when their middle category agrees"
            )
        self._factors = factors
        Functor.__init__(
            self,
            factors[0].domain(),
            factors[-1].codomain(),
            hom_category=hom_category,
        )

    def factors(self) -> tuple[Functor, ...]:
        return self._factors

    def is_faithful(self) -> bool:
        return all(factor.is_faithful() for factor in self._factors)

    def _apply_functor(
        self,
        obj: "ObjectOfCategory",
    ) -> "ObjectOfCategory":
        result = obj
        for factor in self._factors:
            result = factor(result)
        return result

    def _apply_functor_to_morphism(self, morphism: "Morphism") -> "Morphism":
        result = morphism
        for factor in self._factors:
            result = factor(result)
        return result

    def _repr_(self) -> str:
        return " . ".join(str(factor) for factor in reversed(self._factors))


class DiscreteDiagram(Functor):
    r"""A functor from a discrete category, given by its object family."""

    def __init__(
        self,
        index_category: DiscreteCategory,
        codomain: SageCategory,
        values: "Callable[[SageElement], ObjectOfCategory]",
    ) -> None:
        assert index_category in DiscreteCategories()
        self._values = values
        Functor.__init__(self, index_category, codomain)

    def diagram_objects(self) -> "Callable[[SageElement], ObjectOfCategory]":
        return self._values

    def _apply_functor(self, index: SageElement) -> "ObjectOfCategory":
        return self._values(index)

    def _apply_functor_to_morphism(self, morphism: "Morphism") -> "Morphism":
        return self.codomain().identity(self(morphism.domain()))

    def _repr_(self) -> str:
        return f"Discrete diagram in {self.codomain()} indexed by {self.domain()}"


class ConstantDiagram(Functor):
    r"""The constant diagram at one object."""

    def __init__(
        self,
        index_category: SageCategory,
        codomain: SageCategory,
        value: "ObjectOfCategory",
    ) -> None:
        assert index_category in Cat()
        assert value in codomain
        self._value = value
        Functor.__init__(self, index_category, codomain)

    def constant_value(self) -> "ObjectOfCategory":
        return self._value

    def _apply_functor(self, index: "ObjectOfCategory") -> "ObjectOfCategory":
        return self._value

    def _apply_functor_to_morphism(self, morphism: "Morphism") -> "Morphism":
        return self.codomain().identity(self._value)

    def _repr_(self) -> str:
        return f"Constant diagram at {self._value}"


class DiagonalFunctor(Functor):
    r"""The diagonal functor from a category to diagrams of one shape."""

    def __init__(self, category: SageCategory, index_category: SageCategory) -> None:
        assert index_category in Cat()
        self._index_category = index_category
        Functor.__init__(self, category, category.Diagram(index_category))

    def _apply_functor(self, obj: "ObjectOfCategory") -> ConstantDiagram:
        return ConstantDiagram(self._index_category, self.domain(), obj)

    def _apply_functor_to_morphism(
        self,
        morphism: "Morphism",
    ) -> "HomCategoryOf.ElementMethods":
        source = self._apply_functor(morphism.domain())
        target = self._apply_functor(morphism.codomain())
        return NaturalTransformation(source, target, lambda index: morphism)

    def _repr_(self) -> str:
        return f"Diagonal functor from {self.domain()} to {self.codomain()}"


class LimitFunctor(Functor):
    r"""A chosen limit functor on diagrams of one fixed shape."""

    def __init__(self, codomain: SageCategory, index_category: SageCategory) -> None:
        assert index_category in Cat()
        self._index_category = index_category
        Functor.__init__(self, codomain.Diagram(index_category), codomain)

    def index_category(self) -> SageCategory:
        return self._index_category

    def _image_category(self) -> SageCategory:
        from dzack_research.preamble.categories.abstract_categories.products import (
            LimitsOfCategory,
        )

        return LimitsOfCategory(self)

    def _apply_functor_to_morphism(
        self,
        transformation: "HomCategoryOf.ElementMethods",
    ) -> "Morphism":
        source_limit = self(transformation.domain())
        target_limit = self(transformation.codomain())
        source_cone = source_limit.limit_cone()
        cone = NaturalTransformation(
            source_cone.domain(),
            transformation.codomain(),
            lambda index: self.codomain().compose(
                transformation.component(index),
                source_cone.component(index),
            ),
        )
        return target_limit.universal_morphism(cone)


class ColimitFunctor(Functor):
    r"""A chosen colimit functor on diagrams of one fixed shape."""

    def __init__(self, codomain: SageCategory, index_category: SageCategory) -> None:
        assert index_category in Cat()
        self._index_category = index_category
        Functor.__init__(self, codomain.Diagram(index_category), codomain)

    def index_category(self) -> SageCategory:
        return self._index_category

    def _image_category(self) -> SageCategory:
        from dzack_research.preamble.categories.abstract_categories.products import (
            ColimitsOfCategory,
        )

        return ColimitsOfCategory(self)

    def _apply_functor_to_morphism(
        self,
        transformation: "HomCategoryOf.ElementMethods",
    ) -> "Morphism":
        source_colimit = self(transformation.domain())
        target_colimit = self(transformation.codomain())
        target_cocone = target_colimit.colimit_cocone()
        cocone = NaturalTransformation(
            transformation.domain(),
            target_cocone.codomain(),
            lambda index: self.codomain().compose(
                target_cocone.component(index),
                transformation.component(index),
            ),
        )
        return source_colimit.universal_morphism(cocone)


class ProductFunctor(LimitFunctor):
    r"""A chosen product functor on discrete diagrams."""

    def __init__(
        self,
        codomain: SageCategory,
        index_category: DiscreteCategory,
    ) -> None:
        assert index_category in DiscreteCategories()
        LimitFunctor.__init__(self, codomain, index_category)

    def _image_category(self) -> SageCategory:
        from dzack_research.preamble.categories.abstract_categories.products import (
            ProductsOfCategory,
        )

        return ProductsOfCategory(self)


class CoproductFunctor(ColimitFunctor):
    r"""A chosen coproduct functor on discrete diagrams."""

    def __init__(
        self,
        codomain: SageCategory,
        index_category: DiscreteCategory,
    ) -> None:
        assert index_category in DiscreteCategories()
        ColimitFunctor.__init__(self, codomain, index_category)

    def _image_category(self) -> SageCategory:
        from dzack_research.preamble.categories.abstract_categories.products import (
            CoproductsOfCategory,
        )

        return CoproductsOfCategory(self)


def NaturalTransformations(source: Functor, target: Functor) -> "Category":
    r"""Return the Hom category of natural transformations \(F\Rightarrow G\)."""
    assert source.parent() is target.parent(), (
        "natural transformations require parallel functors"
    )
    return source.parent().Hom(source, target)


def NaturalTransformation(
    source: Functor,
    target: Functor,
    components: "Callable[[ObjectOfCategory], HomCategoryOf.ElementMethods]",
) -> "HomCategoryOf.ElementMethods":
    r"""Construct a natural transformation from its declared components."""
    return NaturalTransformations(source, target)(components)


def NaturalIsomorphism(
    source: Functor,
    target: Functor,
    components: "Callable[[ObjectOfCategory], HomCategoryOf.ElementMethods]",
    inverse_components: "Callable[[ObjectOfCategory], HomCategoryOf.ElementMethods]",
) -> "HomCategoryOf.ElementMethods":
    r"""Construct a natural isomorphism from mutually inverse components."""
    forward = NaturalTransformation(source, target, components)
    backward = NaturalTransformation(target, source, inverse_components)
    return Isomorphism(forward, backward)
