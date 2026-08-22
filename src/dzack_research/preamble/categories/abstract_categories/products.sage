r"""Diagram, directed/inverse system, cone/cocone, and product/coproduct categories.

Hierarchical parameterized abstract categories over an ambient \(\mathbf{C}\):

- ``DiagramCategory(objects, morphisms)``: a diagram \(F:J\to\mathbf{C}\).
- ``DirectedSystem`` / ``InverseSystem``: indexed diagrams with directed order.
- ``Cone`` / ``Cocone``: a (co)apex with (co)structure morphisms over a system.
- ``Product`` / ``Coproduct``: (co)limits of discrete diagrams — factors / cofactors.

Each cone object carries ``structure_morphisms()`` (the projections);
each cocone object carries ``costructure_morphisms()`` (the injections).
"""

from __future__ import annotations

from dzack_research.preamble.owned_category import object_of
from collections.abc import Callable, Iterable, Iterator
from typing import Self, TYPE_CHECKING
if TYPE_CHECKING:
    from dzack_research.preamble.owned_category import ConstructionData
    from sage.structure.parent import ElementConstructorInput

from dzack_research.preamble.owned_category_bases import Category, CategoryWithParameters
from dzack_research.preamble.categories.abstract_categories.functor_images import (
    _FunctorImageParameters,
    ImageOfFunctor,
)
# The category a diagram sits in is any category, and the objects that carry
# diagrams have joined categories -- so the ambient is typically a
# ``JoinCategory``, which is Sage's class and not an owned one.  Every
# ``ambient_category`` below is this type; the owned ``Category`` above is the
# base of the diagram categories themselves.
from sage.categories.category import Category as AmbientCategory
from sage.misc.cachefunc import cached_method
from sage.sets.family import Family
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from typing import Protocol

    from dzack_research.preamble.categories.abstract_categories.hom_categories import (
        HomCategoryOf,
    )
    from dzack_research.preamble.categories.sets.cardinals import Cardinal

    type Morphism = HomCategoryOf.ElementMethods

    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from sage.categories.modules import Module
    from dzack_research.preamble.lexicon import OrderedSet

    # What an object gets from sitting in each of these categories.  Placement
    # is what supplies these, not the class an object was constructed from, so
    # the requirement is stated structurally and named after the objects.
    class ConeParent(Protocol):
        def category(self) -> "ConeCategory": ...

    class CoconeParent(Protocol):
        def category(self) -> "CoconeCategory": ...

    class ModuleParent(Protocol):
        r"""A factor of a tensor product: a module with a generating set."""

        def module_generating_set(self) -> "OrderedSet": ...
        def module_generator(self, label: Element) -> Element: ...

    class TensorProductParent(Protocol):
        r"""A tensor product object: a cocone apex that is itself a module and
        knows how to form \(x_1\otimes\cdots\otimes x_n\)."""

        def category(self) -> "TensorProductCategory": ...
        def costructure_morphism(self, i: "Integer") -> Morphism: ...
        def tensor_factors(self) -> "tuple[ModuleParent, ...]": ...
        def module_generating_set(self) -> "OrderedSet": ...
        def hom(self, images: dict, codomain: "Module" = ...) -> "ModuleMorphism": ...
        def _pure_tensor(self, *elements: Element) -> Element: ...


class _DiagramParameters:
    r"""The parameters a diagram category takes.

    They are the ambient category, the family of objects, and the family of
    morphisms.

    This is not a category.  Each category below states its place with
    ``super_categories()``.  A category class that inherits another states the
    class graph by hand instead, and then its methods class arrives twice in
    one set of bases, which no method resolution order can satisfy.
    """

    def __init__(
        self, ambient_category: AmbientCategory, objects: tuple, morphisms: tuple = ()
    ) -> None:
        from dzack_research.preamble.categories.abstract_categories.cat import Cat

        assert ambient_category in Cat()
        self._ambient_category = ambient_category
        self._diagram_objects = tuple(objects)
        self._diagram_morphisms = tuple(morphisms)
        super().__init__()

    def ambient_category(self) -> AmbientCategory:
        return self._ambient_category

    def diagram_objects(self) -> "tuple[Parent, ...]":
        return self._diagram_objects

    def diagram_morphisms(self) -> "tuple[Morphism, ...]":
        return self._diagram_morphisms


class _IndexedDiagramParameters(_DiagramParameters):
    r"""The parameters an indexed diagram category takes: a diagram and one
    index set.  Read :class:`_DiagramParameters` for why this is not a
    category."""

    def __init__(
        self,
        ambient_category: AmbientCategory,
        index_set: "OrderedSet",
        objects: tuple,
        morphisms: tuple = (),
    ) -> None:
        self._index_set = index_set
        super().__init__(ambient_category, objects, morphisms)

    def index_set(self) -> "OrderedSet":
        return self._index_set


class LimitsOfCategory(_FunctorImageParameters, CategoryWithParameters):
    r"""Chosen limits of diagrams, typed as objects of the codomain category."""

    def super_categories(self) -> list[AmbientCategory]:
        return [ImageOfFunctor(self.functor())]

    def _repr_(self) -> str:
        return f"Category of limits constructed by {self.functor()}"

    class ParentMethods:
        def diagram(self) -> Element:
            return self.preimage()

        @abstract_method
        def limit_cone(self) -> Element:
            pass

        @abstract_method
        def universal_morphism(self, cone: Element) -> Morphism:
            pass


class ColimitsOfCategory(_FunctorImageParameters, CategoryWithParameters):
    r"""Chosen colimits of diagrams, typed as objects of the codomain category."""

    def super_categories(self) -> list[AmbientCategory]:
        return [ImageOfFunctor(self.functor())]

    def _repr_(self) -> str:
        return f"Category of colimits constructed by {self.functor()}"

    class ParentMethods:
        def diagram(self) -> Element:
            return self.preimage()

        @abstract_method
        def colimit_cocone(self) -> Element:
            pass

        @abstract_method
        def universal_morphism(self, cocone: Element) -> Morphism:
            pass


class ProductsOfCategory(_FunctorImageParameters, CategoryWithParameters):
    r"""Chosen products of one fixed discrete diagram shape."""

    def super_categories(self) -> list[AmbientCategory]:
        return [LimitsOfCategory(self.functor())]

    def _repr_(self) -> str:
        return f"Category of products constructed by {self.functor()}"

    class ParentMethods:
        def index_category(self) -> AmbientCategory:
            return self.diagram().domain()

        def factors(self) -> Family:
            return Family(self.index_category().objects(), self.diagram())

        @abstract_method
        def projection(self, index: "ElementConstructorInput") -> Morphism:
            pass

        @cached_method
        def product_cone(self) -> Element:
            from dzack_research.preamble.categories.abstract_categories.functors import (
                ConstantDiagram,
                NaturalTransformation,
            )

            return NaturalTransformation(
                ConstantDiagram(
                    self.index_category(),
                    self.diagram().codomain(),
                    self,
                ),
                self.diagram(),
                self.projection,
            )

        def limit_cone(self) -> Element:
            return self.product_cone()


class CoproductsOfCategory(_FunctorImageParameters, CategoryWithParameters):
    r"""Chosen coproducts of one fixed discrete diagram shape."""

    def super_categories(self) -> list[AmbientCategory]:
        return [ColimitsOfCategory(self.functor())]

    def _repr_(self) -> str:
        return f"Category of coproducts constructed by {self.functor()}"

    class ParentMethods:
        def index_category(self) -> AmbientCategory:
            return self.diagram().domain()

        def cofactors(self) -> Family:
            return Family(self.index_category().objects(), self.diagram())

        @abstract_method
        def injection(self, index: "ElementConstructorInput") -> Morphism:
            pass

        @cached_method
        def coproduct_cocone(self) -> Element:
            from dzack_research.preamble.categories.abstract_categories.functors import (
                ConstantDiagram,
                NaturalTransformation,
            )

            return NaturalTransformation(
                self.diagram(),
                ConstantDiagram(
                    self.index_category(),
                    self.diagram().codomain(),
                    self,
                ),
                self.injection,
            )

        def colimit_cocone(self) -> Element:
            return self.coproduct_cocone()


class DiagramCategory(_DiagramParameters, Category):
    r"""A diagram \(F:J\to\mathbf{C}\): a family of objects and morphisms."""

    @staticmethod
    def _diagram_arguments(
        ambient_category: AmbientCategory,
        objects: "Iterable[Parent]",
        morphisms: "Iterable[Morphism]" = (),
    ) -> tuple:
        r"""Return the constructor arguments in the form the cache keys on."""
        return (ambient_category, tuple(objects), tuple(morphisms))

    @staticmethod
    def __classcall_private__(
        cls: type,
        *arguments: "ElementConstructorInput",
        **keywords: "ElementConstructorInput",
    ) -> "DiagramCategory":
        # Sage reads this slot out of ``cls.__dict__`` and never inherits it,
        # so it is protocol plumbing; the mathematics is on the normalizer.
        ambient_category, objects, *optional = arguments
        morphisms = optional[0] if optional else keywords.get("morphisms", ())
        constructed: DiagramCategory = Category.__classcall__(
            cls, *DiagramCategory._diagram_arguments(ambient_category, objects, morphisms)
        )
        return constructed

    def _repr_(self) -> str:
        return f"Category of diagrams on {self._diagram_objects} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [self._ambient_category]


class DirectedSystem(_IndexedDiagramParameters, Category):
    r"""A directed system: \((X_i)_{i\in I}\) with morphisms \(X_i\to X_j\) for \(i\le j\)."""

    @staticmethod
    def _directed_system_arguments(
        ambient_category: AmbientCategory,
        index_set: "OrderedSet",
        objects: "Iterable[Parent]",
        morphisms: "Iterable[Morphism]" = (),
    ) -> tuple:
        r"""Return the constructor arguments in the form the cache keys on."""
        return (ambient_category, index_set, tuple(objects), tuple(morphisms))

    @staticmethod
    def __classcall_private__(
        cls: type,
        *arguments: "ElementConstructorInput",
        **keywords: "ElementConstructorInput",
    ) -> "DirectedSystem":
        # Sage reads this slot out of ``cls.__dict__`` and never inherits it,
        # so it is protocol plumbing; the mathematics is on the normalizer.
        ambient_category, index_set, objects, *optional = arguments
        morphisms = optional[0] if optional else keywords.get("morphisms", ())
        constructed: DirectedSystem = Category.__classcall__(
            cls,
            *DirectedSystem._directed_system_arguments(ambient_category, index_set, objects, morphisms),
        )
        return constructed

    def _repr_(self) -> str:
        return f"Category of directed systems indexed by {self._index_set} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [DiagramCategory(self._ambient_category, self._diagram_objects, self._diagram_morphisms)]


class InverseSystem(_IndexedDiagramParameters, Category):
    r"""An inverse system: \((X_i)_{i\in I}\) with morphisms \(X_j\to X_i\) for \(i\le j\)."""

    @staticmethod
    def _inverse_system_arguments(
        ambient_category: AmbientCategory,
        index_set: "OrderedSet",
        objects: "Iterable[Parent]",
        morphisms: "Iterable[Morphism]" = (),
    ) -> tuple:
        r"""Return the constructor arguments in the form the cache keys on."""
        return (ambient_category, index_set, tuple(objects), tuple(morphisms))

    @staticmethod
    def __classcall_private__(
        cls: type,
        *arguments: "ElementConstructorInput",
        **keywords: "ElementConstructorInput",
    ) -> "InverseSystem":
        # Sage reads this slot out of ``cls.__dict__`` and never inherits it,
        # so it is protocol plumbing; the mathematics is on the normalizer.
        ambient_category, index_set, objects, *optional = arguments
        morphisms = optional[0] if optional else keywords.get("morphisms", ())
        constructed: InverseSystem = Category.__classcall__(
            cls,
            *InverseSystem._inverse_system_arguments(ambient_category, index_set, objects, morphisms),
        )
        return constructed

    def _repr_(self) -> str:
        return f"Category of inverse systems indexed by {self._index_set} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [DiagramCategory(self._ambient_category, self._diagram_objects, self._diagram_morphisms)]


class ConeCategory(_IndexedDiagramParameters, Category):
    r"""A cone over a directed system: an apex \(A\) with projections \(\pi_i:A\to X_i\)."""

    def _repr_(self) -> str:
        return f"Category of cones over {self._diagram_objects} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        from sage.categories.objects import Objects

        return [Objects()]

    class ParentMethods:
        _structure_morphisms: "tuple[Morphism, ...]"

        def __init__(
            self,
            structure_morphisms: "tuple[Morphism, ...]",
            apex: "Parent | None" = None,
            **rest: "ConstructionData",
        ) -> None:
            self._structure_morphisms = tuple(structure_morphisms)
            if apex is None:
                apex = self._structure_morphisms[0].domain()
            assert all(morphism.domain() is apex for morphism in self._structure_morphisms)
            self._apex = apex
            super().__init__(**rest)

        def apex(self) -> Parent:
            return self._apex

        def structure_morphisms(self: Self) -> "tuple[Morphism, ...]":
            r"""Return the projections \(\pi_i:A\to X_i\)."""
            return self._structure_morphisms

        def structure_morphism(self: Self, i: "Integer") -> Morphism:
            r"""Return the \(i\)-th projection \(\pi_i:A\to X_i\)."""
            return self._structure_morphisms[i]

        def factors(self: "ConeParent") -> "tuple[Parent, ...]":
            r"""Return the factor objects \(X_i\) of the diagram."""
            return tuple(
                morphism.codomain()
                for morphism in self.structure_morphisms()
            )

        def factor(self: "ConeParent", i: "Integer") -> Parent:
            r"""Return the \(i\)-th factor \(X_i\)."""
            return self.structure_morphism(i).codomain()


class CoconeCategory(_IndexedDiagramParameters, Category):
    r"""A cocone under an inverse system: a coapex \(A\) with injections \(\iota_i:X_i\to A\)."""

    def _repr_(self) -> str:
        return f"Category of cocones under {self._diagram_objects} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        from sage.categories.objects import Objects

        return [Objects()]

    class ParentMethods:
        _costructure_morphisms: "tuple[Morphism, ...]"

        def __init__(
            self,
            costructure_morphisms: "tuple[Morphism, ...]",
            apex: "Parent | None" = None,
            **rest: "ConstructionData",
        ) -> None:
            self._costructure_morphisms = tuple(costructure_morphisms)
            if apex is None:
                apex = self._costructure_morphisms[0].codomain()
            assert all(morphism.codomain() is apex for morphism in self._costructure_morphisms)
            self._apex = apex
            super().__init__(**rest)

        def apex(self) -> Parent:
            return self._apex

        def costructure_morphisms(self: Self) -> "tuple[Morphism, ...]":
            r"""Return the injections \(\iota_i:X_i\to A\)."""
            return self._costructure_morphisms

        def costructure_morphism(self: Self, i: "Integer") -> Morphism:
            r"""Return the \(i\)-th injection \(\iota_i:X_i\to A\)."""
            return self._costructure_morphisms[i]

        def cofactors(self: "CoconeParent") -> "tuple[Parent, ...]":
            r"""Return the cofactor objects \(X_i\) of the diagram."""
            return tuple(
                morphism.domain()
                for morphism in self.costructure_morphisms()
            )

        def cofactor(self: "CoconeParent", i: "Integer") -> Parent:
            r"""Return the \(i\)-th cofactor \(X_i\)."""
            return self.costructure_morphism(i).domain()


class ProductConeCategory(_IndexedDiagramParameters, Category):
    r"""A product: a cone over a discrete diagram. Parameterized by factors."""

    @staticmethod
    def _product_arguments(
        ambient_category: AmbientCategory, factors: "Iterable[Parent]"
    ) -> tuple:
        r"""Return the constructor arguments in the form the cache keys on."""
        return (ambient_category, tuple(factors))

    @staticmethod
    def __classcall_private__(
        cls: type,
        *arguments: "ElementConstructorInput",
        **keywords: "ElementConstructorInput",
    ) -> "ProductConeCategory":
        # Sage reads this slot out of ``cls.__dict__`` and never inherits it,
        # so it is protocol plumbing; the mathematics is on the normalizer.
        ambient_category, factors = arguments
        constructed: ProductConeCategory = Category.__classcall__(
            cls, *ProductConeCategory._product_arguments(ambient_category, factors)
        )
        return constructed

    def __init__(self, ambient_category: AmbientCategory, factors: tuple) -> None:
        factors = tuple(factors)
        super().__init__(ambient_category, tuple(range(len(factors))), factors, ())

    def _repr_(self) -> str:
        return f"Category of products of {self._diagram_objects} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [ConeCategory(self._ambient_category, self._index_set, self._diagram_objects, self._diagram_morphisms)]


class CoproductCoconeCategory(_IndexedDiagramParameters, Category):
    r"""A coproduct: a cocone under a discrete diagram. Parameterized by cofactors."""

    @staticmethod
    def _coproduct_arguments(
        ambient_category: AmbientCategory, cofactors: "Iterable[Parent]"
    ) -> tuple:
        r"""Return the constructor arguments in the form the cache keys on."""
        return (ambient_category, tuple(cofactors))

    @staticmethod
    def __classcall_private__(
        cls: type,
        *arguments: "ElementConstructorInput",
        **keywords: "ElementConstructorInput",
    ) -> "CoproductCoconeCategory":
        # Sage reads this slot out of ``cls.__dict__`` and never inherits it,
        # so it is protocol plumbing; the mathematics is on the normalizer.
        ambient_category, cofactors = arguments
        constructed: CoproductCoconeCategory = Category.__classcall__(
            cls, *CoproductCoconeCategory._coproduct_arguments(ambient_category, cofactors)
        )
        return constructed

    def __init__(self, ambient_category: AmbientCategory, cofactors: tuple) -> None:
        cofactors = tuple(cofactors)
        super().__init__(ambient_category, tuple(range(len(cofactors))), cofactors, ())

    def _repr_(self) -> str:
        return f"Category of coproducts of {self._diagram_objects} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [CoconeCategory(self._ambient_category, self._index_set, self._diagram_objects, self._diagram_morphisms)]


class BiproductCategory(_IndexedDiagramParameters, Category):
    r"""A biproduct: simultaneously a product and coproduct (additive setting).

    The projections \(\pi_i:A\to X_i\) and injections \(\iota_i:X_i\to A\)
    satisfy \(\pi_j\circ\iota_i = \delta_{ij}\).  Direct sum is the additive
    synonym.
    """

    @staticmethod
    def _biproduct_arguments(
        ambient_category: AmbientCategory, factors: "Iterable[Parent]"
    ) -> tuple:
        r"""Return the constructor arguments in the form the cache keys on."""
        return (ambient_category, tuple(factors))

    @staticmethod
    def __classcall_private__(
        cls: type,
        *arguments: "ElementConstructorInput",
        **keywords: "ElementConstructorInput",
    ) -> "BiproductCategory":
        # Sage reads this slot out of ``cls.__dict__`` and never inherits it,
        # so it is protocol plumbing; the mathematics is on the normalizer.
        ambient_category, factors = arguments
        constructed: BiproductCategory = Category.__classcall__(
            cls, *BiproductCategory._biproduct_arguments(ambient_category, factors)
        )
        return constructed

    def __init__(self, ambient_category: AmbientCategory, factors: tuple) -> None:
        factors = tuple(factors)
        super().__init__(ambient_category, tuple(range(len(factors))), factors, ())

    def _repr_(self) -> str:
        return f"Category of biproducts of {self._diagram_objects} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [
            ProductConeCategory(self._ambient_category, self._diagram_objects),
            CoproductCoconeCategory(self._ambient_category, self._diagram_objects),
        ]


# Direct sum is the additive synonym for biproduct.
DirectSumCategory = BiproductCategory


def ambient_category_of(objects: "Iterable[Parent]") -> "AmbientCategory":
    r"""Return the category these objects share, which a construction over
    them is taken in.

    The meet, so it is a fact about the objects and nothing else.  Read off
    the *result* of a construction instead, a second construction over the
    same objects asks for a cone over a category that is already that cone,
    and nests the construction inside itself -- which a cached result, a
    lattice among them, reaches on the second call.
    """
    ambient: "AmbientCategory" = AmbientCategory.meet(
        [obj.category() for obj in objects]
    )
    return ambient


def Cone(apex: Parent, structure_morphisms: "tuple[Morphism, ...]") -> Parent:
    r"""Construct a cone: an apex \(A\) with projections \(\pi_i:A\to X_i\)."""
    projections = tuple(structure_morphisms)
    assert all(
        morphism in apex.category().ArrowCategory()
        for morphism in projections
    )
    assert all(m.domain() is apex for m in projections)
    objects = tuple(m.codomain() for m in projections)
    category = ambient_category_of((apex, *objects))
    assert all(morphism in category.ArrowCategory() for morphism in projections)
    index_set = tuple(range(len(projections)))
    constructed = object_of(
        category.Cone(index_set, objects),
        apex=apex,
        structure_morphisms=projections,
    )
    return constructed


def Cocone(apex: Parent, costructure_morphisms: "tuple[Morphism, ...]") -> Parent:
    r"""Construct a cocone: a coapex \(A\) with injections \(\iota_i:X_i\to A\)."""
    injections = tuple(costructure_morphisms)
    assert all(
        morphism in apex.category().ArrowCategory()
        for morphism in injections
    )
    assert all(m.codomain() is apex for m in injections)
    objects = tuple(m.domain() for m in injections)
    category = ambient_category_of((apex, *objects))
    assert all(morphism in category.ArrowCategory() for morphism in injections)
    index_set = tuple(range(len(injections)))
    constructed = object_of(
        category.Cocone(index_set, objects),
        apex=apex,
        costructure_morphisms=injections,
    )
    return constructed


def Product(apex: Parent, structure_morphisms: "tuple[Morphism, ...]") -> Parent:
    r"""Construct the product: a cone over a discrete diagram."""
    projections = tuple(structure_morphisms)
    assert all(
        morphism in apex.category().ArrowCategory()
        for morphism in projections
    )
    assert all(m.domain() is apex for m in projections)
    factors = tuple(m.codomain() for m in projections)
    category = ambient_category_of((apex, *factors))
    assert all(morphism in category.ArrowCategory() for morphism in projections)
    constructed = object_of(
        category.Product(factors),
        apex=apex,
        structure_morphisms=projections,
    )
    return constructed


def Coproduct(apex: Parent, costructure_morphisms: "tuple[Morphism, ...]") -> Parent:
    r"""Construct the coproduct: a cocone under a discrete diagram."""
    injections = tuple(costructure_morphisms)
    assert all(
        morphism in apex.category().ArrowCategory()
        for morphism in injections
    )
    assert all(m.codomain() is apex for m in injections)
    cofactors = tuple(m.domain() for m in injections)
    category = ambient_category_of((apex, *cofactors))
    assert all(morphism in category.ArrowCategory() for morphism in injections)
    constructed = object_of(
        category.Coproduct(cofactors),
        apex=apex,
        costructure_morphisms=injections,
    )
    return constructed


def Biproduct(
    apex: Parent,
    structure_morphisms: "tuple[Morphism, ...]",
    costructure_morphisms: "tuple[Morphism, ...]",
) -> Parent:
    r"""Construct the biproduct: a product and coproduct with \(\pi_j\circ\iota_i=\delta_{ij}\).

    The returned cone stores both families of arrows.  Its apex remains an
    unchanged object of the base category.
    """
    projections = tuple(structure_morphisms)
    injections = tuple(costructure_morphisms)
    assert all(
        morphism in apex.category().ArrowCategory()
        for morphism in (*projections, *injections)
    )
    assert all(morphism.domain() is apex for morphism in projections)
    assert all(morphism.codomain() is apex for morphism in injections)
    assert len(projections) == len(injections), (
        "a biproduct has as many projections as injections"
    )
    factors = tuple(m.codomain() for m in projections)
    assert tuple(m.domain() for m in injections) == factors, (
        "the projection codomains and injection domains are the same factors"
    )
    category = ambient_category_of((apex, *factors))
    assert all(morphism in category.ArrowCategory() for morphism in projections)
    assert all(morphism in category.ArrowCategory() for morphism in injections)
    constructed = object_of(
        category.Biproduct(factors),
        apex=apex,
        structure_morphisms=projections,
        costructure_morphisms=injections,
    )
    return constructed


# Direct sum is the additive synonym for biproduct: in an additive category
# the product and the coproduct of a finite family agree, and ``DirectSum``
# is what that one object is called there.  The name goes to *this*
# operation, and not to declaring an object decomposed, because it is the
# construction: the universal property produces the object, so the name
# denotes the thing rather than a property of a thing already built.
# ``DirectSumDecomposition`` in ``direct_sum_objects`` is the other one.
DirectSum = Biproduct

class TensorProductCategory(_IndexedDiagramParameters, Category):
    r"""A tensor product \(X_1\otimes\cdots\otimes X_n\).

    A cocone -- an object *under* something -- and what it is under is the
    cartesian product \(M\times N\), not \(M\) or \(N\) separately.  The
    costructure morphism is the universal map
    \(\otimes:M\times N\to M\otimes N\), \((m,n)\mapsto m\otimes n\),
    which is bilinear and is a morphism of *sets*: it is not linear on
    \(M\oplus N\), which is why the cocone is taken in \(\mathbf{Set}\)
    and not in \(R\text{-}\mathbf{Mod}\).

    What does *not* exist is a canonical \(M\to M\otimes N\): sending
    \(m\mapsto m\otimes n\) requires choosing \(n\).  So this is a cocone
    under the product and not under either factor, and it is a product of
    nothing -- there are no projections \(M\otimes N\to M\).

    Universality: every bilinear \(\beta:M\times N\to P\) factors uniquely
    through \(\otimes\).  That factorization is ``from_bilinear``.
    """

    @staticmethod
    def _tensor_product_arguments(
        ambient_category: AmbientCategory, factors: "Iterable[Parent]"
    ) -> tuple:
        r"""Return the constructor arguments in the form the cache keys on."""
        return (ambient_category, tuple(factors))

    @staticmethod
    def __classcall_private__(
        cls: type,
        *arguments: "ElementConstructorInput",
        **keywords: "ElementConstructorInput",
    ) -> "TensorProductCategory":
        # Sage reads this slot out of ``cls.__dict__`` and never inherits it,
        # so it is protocol plumbing; the mathematics is on the normalizer.
        ambient_category, factors = arguments
        constructed: TensorProductCategory = Category.__classcall__(
            cls, *TensorProductCategory._tensor_product_arguments(ambient_category, factors)
        )
        return constructed

    def __init__(self, ambient_category: AmbientCategory, factors: tuple) -> None:
        from dzack_research.preamble.categories.sets.sets import CartesianProductOfSets

        factors = tuple(factors)
        self._tensor_factors: "tuple[ModuleParent, ...]" = factors
        source = CartesianProductOfSets(factors)
        super().__init__(ambient_category, (0,), (source,), ())

    def _repr_(self) -> str:
        return (
            f"Category of tensor products of {self._tensor_factors} "
            f"in {self._ambient_category}"
        )

    def super_categories(self) -> list[Category]:
        # A tensor product is a cocone under \(M\times N\), which is what
        # supplies the universal bilinear map read below as
        # ``costructure_morphism(0)``.
        return [
            CoconeCategory(
                self._ambient_category,
                self._index_set,
                self._diagram_objects,
                self._diagram_morphisms,
            )
        ]

    class ParentMethods:
        def tensor_factors(self: "TensorProductParent") -> "tuple[ModuleParent, ...]":
            r"""Return the factors \(X_i\)."""
            factors: "tuple[ModuleParent, ...]" = tuple(
                self.cartesian_source().factors()
            )
            return factors

        def tensor_factor(self: "TensorProductParent", i: "Integer") -> "ModuleParent":
            r"""Return the \(i\)-th factor \(X_i\)."""
            return self.tensor_factors()[i]

        def cartesian_source(self: "TensorProductParent") -> Parent:
            r"""Return \(M\times N\), the object this cocone sits under."""
            return self.costructure_morphism(0).domain()

        def universal_bilinear_map(self: "TensorProductParent") -> Morphism:
            r"""Return \(\otimes:M\times N\to M\otimes N\), the cocone's structure map."""
            tensor_map: Morphism = self.costructure_morphism(0)
            return tensor_map

        def pure_tensor(self: "TensorProductParent", *elements: Element) -> Element:
            r"""Return \(x_1\otimes\cdots\otimes x_n=\otimes(x_1,\dots,x_n)\).

            Every element of the tensor product is a *sum* of these; not
            every element is one of these.
            """
            factors = self.tensor_factors()
            assert len(elements) == len(factors), (
                f"a pure tensor needs one element per factor: "
                f"{len(factors)} expected, {len(elements)} given"
            )
            assert all(
                element in factor
                for element, factor in zip(elements, factors)
            ), "each element belongs to its own factor"
            tensor: Element = self._pure_tensor(*elements)
            return tensor

        def from_bilinear(
            self: "TensorProductParent",
            bilinear: "Callable[[Element, Element], Element]",
            codomain: Parent,
        ) -> Morphism:
            r"""Factor a bilinear map through \(\otimes\).

            For bilinear \(\beta:M\times N\to P\) there is a unique
            \(\bar\beta:M\otimes N\to P\) with
            \(\bar\beta(m\otimes n)=\beta(m,n)\).  This is the only source
            of morphisms out of a tensor product.
            """
            left, right = self.tensor_factors()
            factorization: Morphism = self.hom(
                {
                    label: bilinear(
                        left.module_generator(left_label), right.module_generator(right_label)
                    )
                    for label, (left_label, right_label) in zip(
                        self.module_generating_set(),
                        [
                            (a, b)
                            for a in left.module_generating_set()
                            for b in right.module_generating_set()
                        ],
                    )
                },
                codomain,
            )
            return factorization
