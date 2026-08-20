r"""Diagram, directed/inverse system, cone/cocone, and product/coproduct categories.

Hierarchical parameterized abstract categories over an ambient \(\mathbf{C}\):

- ``DiagramCategory(objects, morphisms)``: a diagram \(F:J\to\mathbf{C}\).
- ``DirectedSystem`` / ``InverseSystem``: indexed diagrams with directed order.
- ``Cone`` / ``Cocone``: a (co)apex with (co)structure morphisms over a system.
- ``Product`` / ``Coproduct``: (co)limits of discrete diagrams — factors / cofactors.

Each cone object carries ``structure_morphisms()`` (the projections);
each cocone object carries ``costructure_morphisms()`` (the injections).
"""

# The owned root, not Sage's: the preamble places every set in it, and a
# parent left in Sage's ``Sets()`` is not in the owned one, so a ``Hom`` out
# of it in the preamble's category is refused.
from dzack_research.preamble.categories.sets.owned_sets import Sets
from dzack_research.preamble.refine import refine
from collections.abc import Callable, Iterable, Iterator
from typing import Self, TYPE_CHECKING
if TYPE_CHECKING:
    from dzack_research.preamble.owned_category import ConstructionData
    from sage.structure.parent import ElementConstructorInput

from dzack_research.preamble.owned_category_bases import Category
# The category a diagram sits in is any category, and the objects that carry
# diagrams have joined categories -- so the ambient is typically a
# ``JoinCategory``, which is Sage's class and not an owned one.  Every
# ``ambient_category`` below is this type; the owned ``Category`` above is the
# base of the diagram categories themselves.
from sage.categories.category import Category as AmbientCategory
from sage.categories.morphism import Morphism
from sage.structure.element import Element
from sage.structure.parent import Parent

if TYPE_CHECKING:
    from typing import Protocol

    from dzack_research.preamble.categories.sets.cardinals import Cardinal

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
        assert isinstance(ambient_category, AmbientCategory)
        assert isinstance(objects, Iterable) and isinstance(morphisms, Iterable)
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
        assert isinstance(ambient_category, AmbientCategory)
        assert isinstance(objects, Iterable) and isinstance(morphisms, Iterable)
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
        assert isinstance(ambient_category, AmbientCategory)
        assert isinstance(objects, Iterable) and isinstance(morphisms, Iterable)
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
        return [DirectedSystem(self._ambient_category, self._index_set, self._diagram_objects, self._diagram_morphisms)]

    class ParentMethods:
        # Installed on the apex by the ``Cone`` constructor below: no Python
        # class holds the projections, so they are declared, not defined.
        _structure_morphisms: "tuple[Morphism, ...]"

        def structure_morphisms(self: Self) -> "tuple[Morphism, ...]":
            r"""Return the projections \(\pi_i:A\to X_i\)."""
            return self._structure_morphisms

        def structure_morphism(self: Self, i: "Integer") -> Morphism:
            r"""Return the \(i\)-th projection \(\pi_i:A\to X_i\)."""
            return self._structure_morphisms[i]

        def factors(self: "ConeParent") -> "tuple[Parent, ...]":
            r"""Return the factor objects \(X_i\) of the diagram."""
            return self.category().diagram_objects()

        def factor(self: "ConeParent", i: "Integer") -> Parent:
            r"""Return the \(i\)-th factor \(X_i\)."""
            return self.category().diagram_objects()[i]


class CoconeCategory(_IndexedDiagramParameters, Category):
    r"""A cocone under an inverse system: a coapex \(A\) with injections \(\iota_i:X_i\to A\)."""

    def _repr_(self) -> str:
        return f"Category of cocones under {self._diagram_objects} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [InverseSystem(self._ambient_category, self._index_set, self._diagram_objects, self._diagram_morphisms)]

    class ParentMethods:
        # Installed on the coapex by the ``Cocone`` constructor below.
        _costructure_morphisms: "tuple[Morphism, ...]"

        def costructure_morphisms(self: Self) -> "tuple[Morphism, ...]":
            r"""Return the injections \(\iota_i:X_i\to A\)."""
            return self._costructure_morphisms

        def costructure_morphism(self: Self, i: "Integer") -> Morphism:
            r"""Return the \(i\)-th injection \(\iota_i:X_i\to A\)."""
            return self._costructure_morphisms[i]

        def cofactors(self: "CoconeParent") -> "tuple[Parent, ...]":
            r"""Return the cofactor objects \(X_i\) of the diagram."""
            return self.category().diagram_objects()

        def cofactor(self: "CoconeParent", i: "Integer") -> Parent:
            r"""Return the \(i\)-th cofactor \(X_i\)."""
            return self.category().diagram_objects()[i]


class ProductCategory(_IndexedDiagramParameters, Category):
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
    ) -> "ProductCategory":
        # Sage reads this slot out of ``cls.__dict__`` and never inherits it,
        # so it is protocol plumbing; the mathematics is on the normalizer.
        ambient_category, factors = arguments
        assert isinstance(ambient_category, AmbientCategory)
        assert isinstance(factors, Iterable)
        constructed: ProductCategory = Category.__classcall__(
            cls, *ProductCategory._product_arguments(ambient_category, factors)
        )
        return constructed

    def __init__(self, ambient_category: AmbientCategory, factors: tuple) -> None:
        factors = tuple(factors)
        super().__init__(ambient_category, tuple(range(len(factors))), factors, ())

    def _repr_(self) -> str:
        return f"Category of products of {self._diagram_objects} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [ConeCategory(self._ambient_category, self._index_set, self._diagram_objects, self._diagram_morphisms)]


class CoproductCategory(_IndexedDiagramParameters, Category):
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
    ) -> "CoproductCategory":
        # Sage reads this slot out of ``cls.__dict__`` and never inherits it,
        # so it is protocol plumbing; the mathematics is on the normalizer.
        ambient_category, cofactors = arguments
        assert isinstance(ambient_category, AmbientCategory)
        assert isinstance(cofactors, Iterable)
        constructed: CoproductCategory = Category.__classcall__(
            cls, *CoproductCategory._coproduct_arguments(ambient_category, cofactors)
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
        assert isinstance(ambient_category, AmbientCategory)
        assert isinstance(factors, Iterable)
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
            ProductCategory(self._ambient_category, self._diagram_objects),
            CoproductCategory(self._ambient_category, self._diagram_objects),
        ]


# Direct sum is the additive synonym for biproduct.
DirectSumCategory = BiproductCategory


def Cone(structure_morphisms: "tuple[Morphism, ...]") -> Parent:
    r"""Construct a cone: an apex \(A\) with projections \(\pi_i:A\to X_i\)."""
    projections = tuple(structure_morphisms)
    assert all(isinstance(m, Morphism) for m in projections), (
        "the projections of a cone must be Morphisms"
    )
    assert len({m.domain() for m in projections}) == 1, (
        "the projections of a cone share one apex"
    )
    apex = projections[0].domain()
    apex._structure_morphisms = projections
    objects = tuple(m.codomain() for m in projections)
    index_set = tuple(range(len(projections)))
    refine(apex, apex.category().Cone(index_set, objects))
    constructed: Parent = apex
    return constructed


def Cocone(costructure_morphisms: "tuple[Morphism, ...]") -> Parent:
    r"""Construct a cocone: a coapex \(A\) with injections \(\iota_i:X_i\to A\)."""
    injections = tuple(costructure_morphisms)
    assert all(isinstance(m, Morphism) for m in injections), (
        "the injections of a cocone must be Morphisms"
    )
    assert len({m.codomain() for m in injections}) == 1, (
        "the injections of a cocone share one coapex"
    )
    coapex = injections[0].codomain()
    coapex._costructure_morphisms = injections
    objects = tuple(m.domain() for m in injections)
    index_set = tuple(range(len(injections)))
    refine(coapex, coapex.category().Cocone(index_set, objects))
    constructed: Parent = coapex
    return constructed


def Product(structure_morphisms: "tuple[Morphism, ...]") -> Parent:
    r"""Construct the product: a cone over a discrete diagram."""
    projections = tuple(structure_morphisms)
    assert all(isinstance(m, Morphism) for m in projections), (
        "the projections of a product must be Morphisms"
    )
    assert len({m.domain() for m in projections}) == 1, (
        "the projections of a product share one domain"
    )
    domain = projections[0].domain()
    domain._structure_morphisms = projections
    factors = tuple(m.codomain() for m in projections)
    refine(domain, domain.category().Product(factors))
    constructed: Parent = domain
    return constructed


def Coproduct(costructure_morphisms: "tuple[Morphism, ...]") -> Parent:
    r"""Construct the coproduct: a cocone under a discrete diagram."""
    injections = tuple(costructure_morphisms)
    assert all(isinstance(m, Morphism) for m in injections), (
        "the injections of a coproduct must be Morphisms"
    )
    assert len({m.codomain() for m in injections}) == 1, (
        "the injections of a coproduct share one codomain"
    )
    codomain = injections[0].codomain()
    codomain._costructure_morphisms = injections
    cofactors = tuple(m.domain() for m in injections)
    refine(codomain, codomain.category().Coproduct(cofactors))
    constructed: Parent = codomain
    return constructed


def Biproduct(
    structure_morphisms: "tuple[Morphism, ...]",
    costructure_morphisms: "tuple[Morphism, ...]",
) -> Parent:
    r"""Construct the biproduct: a product and coproduct with \(\pi_j\circ\iota_i=\delta_{ij}\).

    Both the projections and injections are stored on the object; the object
    is refined into ``Biproduct((X_i)_i)``.
    """
    projections = tuple(structure_morphisms)
    injections = tuple(costructure_morphisms)
    assert all(isinstance(m, Morphism) for m in projections), (
        "the projections of a biproduct must be Morphisms"
    )
    assert all(isinstance(m, Morphism) for m in injections), (
        "the injections of a biproduct must be Morphisms"
    )
    assert len({m.domain() for m in projections}) == 1, (
        "the projections of a biproduct share one domain"
    )
    assert len({m.codomain() for m in injections}) == 1, (
        "the injections of a biproduct share one codomain"
    )
    obj = projections[0].domain()
    coapex = injections[0].codomain()
    assert obj is coapex, (
        "the product domain and coproduct codomain of a biproduct coincide"
    )
    assert len(projections) == len(injections), (
        "a biproduct has as many projections as injections"
    )
    factors = tuple(m.codomain() for m in projections)
    assert tuple(m.domain() for m in injections) == factors, (
        "the projection codomains and injection domains are the same factors"
    )
    obj._structure_morphisms = projections
    obj._costructure_morphisms = injections
    refine(obj, obj.category().Biproduct(factors))
    constructed: Parent = obj
    return constructed


# Direct sum is the additive synonym for biproduct: in an additive category
# the product and the coproduct of a finite family agree, and ``DirectSum``
# is what that one object is called there.  The name goes to *this*
# operation, and not to declaring an object decomposed, because it is the
# construction: the universal property produces the object, so the name
# denotes the thing rather than a property of a thing already built.
# ``DirectSumDecomposition`` in ``direct_sum_objects`` is the other one.
DirectSum = Biproduct

def _is_known_empty(factor: "Parent") -> bool:
    r"""Whether ``factor`` is known to be empty, from its owned placement.

    Infinite or uncountable placement is nonemptiness; finite placement
    answers by exact cardinality; countable placement by a terminating
    first-element probe.  A parent with no placement deciding the question
    is refused by name — this is a helper of the product constructions,
    never a general ``is_empty`` on ``Sets().ParentMethods``.
    """
    from dzack_research.preamble.categories.sets.owned_sets import placement_of

    axioms = frozenset(placement_of(factor).axioms())
    if "Uncountable" in axioms or "Infinite" in axioms:
        return False
    if "Finite" in axioms:
        return bool(factor.cardinality() == 0)
    if "Countable" in axioms:
        for _ in factor:
            return False
        return True
    # No placement decides it, so ask the object.  A placement is one way to
    # know a set's size and not the only one: a set built through the chain
    # states its size from its factors, with no axiom stamped on it, and this
    # used to refuse such a set outright "for want of a placement".
    return bool(factor.cardinality() == 0)


def _cartesian_placement(factors: "tuple[Parent, ...]") -> Sets:
    r"""The owned ``Sets()`` placement of \(\prod_i X_i\).

    Finite when every factor is finite; countable when every factor is
    countable; uncountable when a factor is, else infinite when a factor
    is.  A product with a known-empty factor — and the empty product, the
    singleton — is finite, whatever the other factors are.
    """
    from dzack_research.preamble.categories.sets.owned_sets import placement_of

    if not factors or any(_is_known_empty(factor) for factor in factors):
        return Sets().Finite()
    axiom_families = [frozenset(placement_of(factor).axioms()) for factor in factors]
    placement = Sets()
    if all("Finite" in axioms for axioms in axiom_families):
        return placement.Finite()
    if all("Finite" in axioms or "Countable" in axioms for axioms in axiom_families):
        placement = placement.Countable()
    if any("Uncountable" in axioms for axioms in axiom_families):
        placement = placement.Uncountable()
    elif any("Infinite" in axioms for axioms in axiom_families):
        placement = placement.Infinite()
    return placement


def CartesianProductOfSets(factors: "Iterable[Parent]") -> "Parent":
    r"""The cartesian product \(U(X_1)\times\cdots\times U(X_n)\) of sets.

    The construction is the category: what a product of sets *is* — its
    factors, its cardinality, its enumeration, its projections, its elements —
    is declared once on ``Sets.CartesianProducts.ParentMethods``, and the
    object is that category's parent class carrying the one datum this level
    introduces.  What is left here is the placement rule (which axioms a
    product of these factors carries) and the public name.
    """
    from dzack_research.preamble.owned_category import object_of

    family = tuple(factors)
    return object_of(_cartesian_placement(family).CartesianProducts(), factors=family)


def cartesian_product_morphism(*maps: Morphism) -> Morphism:
    r"""The product morphism \(\prod_i f_i:\prod_i X_i\to\prod_i Y_i\).

    Componentwise on the products of the maps' own boundaries: the
    domain and codomain products are built from ``domain()`` and
    ``codomain()`` of the given maps.
    """
    from sage.categories.homset import Hom
    from sage.categories.morphism import SetMorphism
    from sage.categories.sets_cat import Sets as SageSets

    domain = CartesianProductOfSets(tuple(component.domain() for component in maps))
    codomain = CartesianProductOfSets(tuple(component.codomain() for component in maps))
    return SetMorphism(
        Hom(domain, codomain, SageSets()),
        lambda point: codomain(
            tuple(component(value) for component, value in zip(maps, point))
        ),
    )


class CoproductsOfSets(Category):
    r"""The coproduct \(\coprod_i X_i\) of sets, as the tagged disjoint union.

    An element is a pair \((i, x)\) with \(x\in X_i\).  The tag is what
    makes the union disjoint, and the \(i\)-th injection sends \(x\) to
    \((i, x)\).

    The one datum this level introduces is the family of cofactors, so it is
    the one argument its ``__init__`` consumes.
    """

    def _repr_object_names(self) -> str:
        return "coproducts of sets"

    def super_categories(self) -> list[Category]:
        return [Sets()]

    class ParentMethods:
        def __init__(
            self, cofactors: "Iterable[Parent]", **rest: "ConstructionData"
        ) -> None:
            self._cofactors = tuple(cofactors)
            super().__init__(**rest)

        def cofactors(self) -> "tuple[Parent, ...]":
            return self._cofactors

        def cardinality(self) -> "Cardinal":
            r"""Return ``sum(#X_i)`` for the cofactors ``X_i``."""
            from dzack_research.preamble.categories.sets.cardinals import Cardinalities

            return Cardinalities().sum(
                *(cofactor.cardinality() for cofactor in self._cofactors)
            )

        def __iter__(self) -> "Iterator[tuple[int, Element]]":
            r"""Fair enumeration, delegated to Sage's disjoint union.

            ``DisjointUnionEnumeratedSets`` with ``keepkey=True`` yields the
            tagged pairs fairly across infinite cofactors, which the naive
            cofactor-by-cofactor loop does not.
            """
            from sage.sets.disjoint_union_enumerated_sets import (
                DisjointUnionEnumeratedSets,
            )
            from sage.sets.family import Family

            return iter(
                DisjointUnionEnumeratedSets(
                    Family(list(self._cofactors)), keepkey=True
                )
            )

        def __contains__(self, tagged_element: tuple[int, Element]) -> bool:
            from sage.rings.integer import Integer as SageInteger

            if not isinstance(tagged_element, tuple) or len(tagged_element) != 2:
                return False
            index, element = tagged_element
            # Sage's disjoint-union enumeration tags with Sage integers; a
            # session writes python ints.  Both name the same index.
            if not isinstance(index, (int, SageInteger)):
                return False
            position = int(index)
            return 0 <= position < len(self._cofactors) and element in self._cofactors[position]

        def injection(self, index: int) -> Morphism:
            r"""The ``index``-th coproduct injection \(\iota_i:X_i\to\coprod_j X_j\)."""
            from sage.categories.homset import Hom
            from sage.categories.morphism import SetMorphism
            from sage.categories.sets_cat import Sets as SageSets

            assert 0 <= index < len(self._cofactors), (
                f"no coproduct cofactor has index {index}"
            )
            cofactor = self._cofactors[index]
            return SetMorphism(
                Hom(cofactor, self, SageSets()), lambda element: (index, element)
            )

        def _repr_(self) -> str:
            if not self._cofactors:
                return "Empty coproduct of sets"
            return " + ".join(str(cofactor) for cofactor in self._cofactors)


def CoproductOfSets(cofactors: "Iterable[Parent]") -> Parent:
    r"""The coproduct \(\coprod_i X_i\) of sets, as the tagged disjoint union.

    The construction is the category: what a coproduct of sets *is* -- its
    cofactors, its cardinality, its enumeration, its injections, its elements
    -- is declared once on ``CoproductsOfSets.ParentMethods``, and the object
    is that category's parent class carrying the one datum this level
    introduces.
    """
    from dzack_research.preamble.owned_category import object_of

    return object_of(CoproductsOfSets(), cofactors=tuple(cofactors))


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
        assert isinstance(ambient_category, AmbientCategory)
        assert isinstance(factors, Iterable)
        constructed: TensorProductCategory = Category.__classcall__(
            cls, *TensorProductCategory._tensor_product_arguments(ambient_category, factors)
        )
        return constructed

    def __init__(self, ambient_category: AmbientCategory, factors: tuple) -> None:
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
            return self.category()._tensor_factors

        def tensor_factor(self: "TensorProductParent", i: "Integer") -> "ModuleParent":
            r"""Return the \(i\)-th factor \(X_i\)."""
            return self.category()._tensor_factors[i]

        def cartesian_source(self: "TensorProductParent") -> Parent:
            r"""Return \(M\times N\), the object this cocone sits under."""
            source: Parent = self.category().diagram_objects()[0]
            return source

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
