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

from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.structure.element import Element
from sage.structure.parent import Parent

if TYPE_CHECKING:
    from typing import Protocol

    from dzack_research.preamble.categories.sets.cardinals import Cardinal

    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import Module, OrderedSet

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


class DiagramCategory(Category):
    r"""A diagram \(F:J\to\mathbf{C}\): a family of objects and morphisms."""

    @staticmethod
    def _diagram_arguments(
        ambient_category: Category,
        objects: "Iterable[Parent]",
        morphisms: "Iterable[Morphism]" = (),
    ) -> tuple:
        r"""Return the constructor arguments in the form the cache keys on."""
        return (ambient_category, tuple(objects), tuple(morphisms))

    @staticmethod
    def __classcall_private__(
        cls: type, *arguments: object, **keywords: object
    ) -> "DiagramCategory":
        # Sage reads this slot out of ``cls.__dict__`` and never inherits it,
        # so it is protocol plumbing; the mathematics is on the normalizer.
        ambient_category, objects, *optional = arguments
        morphisms = optional[0] if optional else keywords.get("morphisms", ())
        assert isinstance(ambient_category, Category)
        assert isinstance(objects, Iterable) and isinstance(morphisms, Iterable)
        constructed: DiagramCategory = Category.__classcall__(
            cls, *DiagramCategory._diagram_arguments(ambient_category, objects, morphisms)
        )
        return constructed

    def __init__(self, ambient_category: Category, objects: tuple, morphisms: tuple = ()) -> None:
        self._ambient_category = ambient_category
        self._diagram_objects = tuple(objects)
        self._diagram_morphisms = tuple(morphisms)
        Category.__init__(self)

    def _repr_(self) -> str:
        return f"Category of diagrams on {self._diagram_objects} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [self._ambient_category]

    def diagram_objects(self) -> "tuple[Parent, ...]":
        return self._diagram_objects

    def diagram_morphisms(self) -> "tuple[Morphism, ...]":
        return self._diagram_morphisms


class DirectedSystem(DiagramCategory):
    r"""A directed system: \((X_i)_{i\in I}\) with morphisms \(X_i\to X_j\) for \(i\le j\)."""

    @staticmethod
    def _directed_system_arguments(
        ambient_category: Category,
        index_set: "OrderedSet",
        objects: "Iterable[Parent]",
        morphisms: "Iterable[Morphism]" = (),
    ) -> tuple:
        r"""Return the constructor arguments in the form the cache keys on."""
        return (ambient_category, index_set, tuple(objects), tuple(morphisms))

    @staticmethod
    def __classcall_private__(
        cls: type, *arguments: object, **keywords: object
    ) -> "DirectedSystem":
        # Sage reads this slot out of ``cls.__dict__`` and never inherits it,
        # so it is protocol plumbing; the mathematics is on the normalizer.
        ambient_category, index_set, objects, *optional = arguments
        morphisms = optional[0] if optional else keywords.get("morphisms", ())
        assert isinstance(ambient_category, Category)
        assert isinstance(objects, Iterable) and isinstance(morphisms, Iterable)
        constructed: DirectedSystem = Category.__classcall__(
            cls,
            *DirectedSystem._directed_system_arguments(ambient_category, index_set, objects, morphisms),
        )
        return constructed

    def __init__(self, ambient_category: Category, index_set: "OrderedSet", objects: tuple, morphisms: tuple = ()) -> None:
        self._index_set = index_set
        DiagramCategory.__init__(self, ambient_category, objects, morphisms)

    def _repr_(self) -> str:
        return f"Category of directed systems indexed by {self._index_set} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [DiagramCategory(self._ambient_category, self._diagram_objects, self._diagram_morphisms)]

    def index_set(self) -> "OrderedSet":
        return self._index_set


class InverseSystem(DiagramCategory):
    r"""An inverse system: \((X_i)_{i\in I}\) with morphisms \(X_j\to X_i\) for \(i\le j\)."""

    @staticmethod
    def _inverse_system_arguments(
        ambient_category: Category,
        index_set: "OrderedSet",
        objects: "Iterable[Parent]",
        morphisms: "Iterable[Morphism]" = (),
    ) -> tuple:
        r"""Return the constructor arguments in the form the cache keys on."""
        return (ambient_category, index_set, tuple(objects), tuple(morphisms))

    @staticmethod
    def __classcall_private__(
        cls: type, *arguments: object, **keywords: object
    ) -> "InverseSystem":
        # Sage reads this slot out of ``cls.__dict__`` and never inherits it,
        # so it is protocol plumbing; the mathematics is on the normalizer.
        ambient_category, index_set, objects, *optional = arguments
        morphisms = optional[0] if optional else keywords.get("morphisms", ())
        assert isinstance(ambient_category, Category)
        assert isinstance(objects, Iterable) and isinstance(morphisms, Iterable)
        constructed: InverseSystem = Category.__classcall__(
            cls,
            *InverseSystem._inverse_system_arguments(ambient_category, index_set, objects, morphisms),
        )
        return constructed

    def __init__(self, ambient_category: Category, index_set: "OrderedSet", objects: tuple, morphisms: tuple = ()) -> None:
        self._index_set = index_set
        DiagramCategory.__init__(self, ambient_category, objects, morphisms)

    def _repr_(self) -> str:
        return f"Category of inverse systems indexed by {self._index_set} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [DiagramCategory(self._ambient_category, self._diagram_objects, self._diagram_morphisms)]

    def index_set(self) -> "OrderedSet":
        return self._index_set


class ConeCategory(DirectedSystem):
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


class CoconeCategory(InverseSystem):
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


class ProductCategory(ConeCategory):
    r"""A product: a cone over a discrete diagram. Parameterized by factors."""

    @staticmethod
    def _product_arguments(
        ambient_category: Category, factors: "Iterable[Parent]"
    ) -> tuple:
        r"""Return the constructor arguments in the form the cache keys on."""
        return (ambient_category, tuple(factors))

    @staticmethod
    def __classcall_private__(
        cls: type, *arguments: object, **keywords: object
    ) -> "ProductCategory":
        # Sage reads this slot out of ``cls.__dict__`` and never inherits it,
        # so it is protocol plumbing; the mathematics is on the normalizer.
        ambient_category, factors = arguments
        assert isinstance(ambient_category, Category)
        assert isinstance(factors, Iterable)
        constructed: ProductCategory = Category.__classcall__(
            cls, *ProductCategory._product_arguments(ambient_category, factors)
        )
        return constructed

    def __init__(self, ambient_category: Category, factors: tuple) -> None:
        factors = tuple(factors)
        index_set = tuple(range(len(factors)))
        ConeCategory.__init__(self, ambient_category, index_set, factors, ())

    def _repr_(self) -> str:
        return f"Category of products of {self._diagram_objects} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [ConeCategory(self._ambient_category, self._index_set, self._diagram_objects, self._diagram_morphisms)]


class CoproductCategory(CoconeCategory):
    r"""A coproduct: a cocone under a discrete diagram. Parameterized by cofactors."""

    @staticmethod
    def _coproduct_arguments(
        ambient_category: Category, cofactors: "Iterable[Parent]"
    ) -> tuple:
        r"""Return the constructor arguments in the form the cache keys on."""
        return (ambient_category, tuple(cofactors))

    @staticmethod
    def __classcall_private__(
        cls: type, *arguments: object, **keywords: object
    ) -> "CoproductCategory":
        # Sage reads this slot out of ``cls.__dict__`` and never inherits it,
        # so it is protocol plumbing; the mathematics is on the normalizer.
        ambient_category, cofactors = arguments
        assert isinstance(ambient_category, Category)
        assert isinstance(cofactors, Iterable)
        constructed: CoproductCategory = Category.__classcall__(
            cls, *CoproductCategory._coproduct_arguments(ambient_category, cofactors)
        )
        return constructed

    def __init__(self, ambient_category: Category, cofactors: tuple) -> None:
        cofactors = tuple(cofactors)
        index_set = tuple(range(len(cofactors)))
        CoconeCategory.__init__(self, ambient_category, index_set, cofactors, ())

    def _repr_(self) -> str:
        return f"Category of coproducts of {self._diagram_objects} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [CoconeCategory(self._ambient_category, self._index_set, self._diagram_objects, self._diagram_morphisms)]


class BiproductCategory(ProductCategory, CoproductCategory):
    r"""A biproduct: simultaneously a product and coproduct (additive setting).

    The projections \(\pi_i:A\to X_i\) and injections \(\iota_i:X_i\to A\)
    satisfy \(\pi_j\circ\iota_i = \delta_{ij}\).  Direct sum is the additive
    synonym.
    """

    @staticmethod
    def _biproduct_arguments(
        ambient_category: Category, factors: "Iterable[Parent]"
    ) -> tuple:
        r"""Return the constructor arguments in the form the cache keys on."""
        return (ambient_category, tuple(factors))

    @staticmethod
    def __classcall_private__(
        cls: type, *arguments: object, **keywords: object
    ) -> "BiproductCategory":
        # Sage reads this slot out of ``cls.__dict__`` and never inherits it,
        # so it is protocol plumbing; the mathematics is on the normalizer.
        ambient_category, factors = arguments
        assert isinstance(ambient_category, Category)
        assert isinstance(factors, Iterable)
        constructed: BiproductCategory = Category.__classcall__(
            cls, *BiproductCategory._biproduct_arguments(ambient_category, factors)
        )
        return constructed

    class ParentMethods(ConeCategory.ParentMethods, CoconeCategory.ParentMethods):
        r"""A biproduct object carries both the projections and the injections."""

    def __init__(self, ambient_category: Category, factors: tuple) -> None:
        ProductCategory.__init__(self, ambient_category, factors)

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

if TYPE_CHECKING:
    # Its elements are tuples, not ``Element``s -- see the class docstring.
    # ``Parent`` is a cython extension type, not subscriptable at runtime.
    CartesianProductParent = Parent[tuple[Element, ...]]
else:
    CartesianProductParent = Parent


class CartesianProductOfSets(CartesianProductParent):
    r"""The cartesian product \(U(X_1)\times\cdots\times U(X_n)\) of underlying sets.

    A *set*, not a module.  The module-level product of \(M\) and \(N\) is
    their biproduct \(M\oplus N\); this is the different object whose
    elements are pairs and out of which bilinear maps are defined.  The two
    have the same elements and different structure, and conflating them is
    what makes the tensor product's universal property unstatable.

    The factors stored are the objects \(X_i\) themselves, since \(U(X_i)\)
    has exactly the elements of \(X_i\): membership is read as
    ``component.parent() is X_i``, which is what \(U\) forgetting to is.
    """

    def __init__(self, factors: tuple) -> None:
        self._factors = tuple(factors)
        Parent.__init__(self, category=Sets())

    def factors(self) -> "tuple[Parent, ...]":
        return self._factors

    def cardinality(self) -> "Cardinal":
        r"""Return ``prod(#X_i)`` for the factors ``X_i``."""
        from dzack_research.preamble.categories.sets.cardinals import (
            Cardinalities,
        )

        return Cardinalities().product(
            *(factor.cardinality() for factor in self._factors)
        )

    def __iter__(self) -> "Iterator[tuple[Element, ...]]":
        from itertools import product as _product

        return iter(_product(*self._factors))

    def __contains__(self, element: object) -> bool:
        return (
            isinstance(element, tuple)
            and len(element) == len(self._factors)
            and all(
                component.parent() is factor
                for component, factor in zip(element, self._factors)
            )
        )

    def _element_constructor_(self, element: "Iterable[Element]") -> "tuple[Element, ...]":
        r"""Return the tuple as an element of this set.

        An element here is a tuple of elements of the factors and nothing
        more, so there is no element class to build; the constructor exists
        because every map out of this set coerces its argument through the
        domain before evaluating it.
        """
        components = tuple(element)
        assert components in self, (
            f"{components} is not a tuple of elements of the factors of {self}"
        )
        return components

    def __call__(
        self, x: object = (), *arguments: object, **keywords: object
    ) -> "tuple[Element, ...]":
        r"""Return the tuple, without Sage's default conversion.

        ``Parent.__call__`` routes through a conversion map declared to
        return an ``Element``, which a tuple is not.  The elements here are
        tuples -- that is what a product of sets has -- so the constructor
        is called directly.
        """
        assert isinstance(x, Iterable), "an element here is a tuple of factor elements"
        return self._element_constructor_(x)

    def _repr_(self) -> str:
        return " x ".join(str(factor) for factor in self._factors)


class TensorProductCategory(CoconeCategory):
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
        ambient_category: Category, factors: "Iterable[Parent]"
    ) -> tuple:
        r"""Return the constructor arguments in the form the cache keys on."""
        return (ambient_category, tuple(factors))

    @staticmethod
    def __classcall_private__(
        cls: type, *arguments: object, **keywords: object
    ) -> "TensorProductCategory":
        # Sage reads this slot out of ``cls.__dict__`` and never inherits it,
        # so it is protocol plumbing; the mathematics is on the normalizer.
        ambient_category, factors = arguments
        assert isinstance(ambient_category, Category)
        assert isinstance(factors, Iterable)
        constructed: TensorProductCategory = Category.__classcall__(
            cls, *TensorProductCategory._tensor_product_arguments(ambient_category, factors)
        )
        return constructed

    def __init__(self, ambient_category: Category, factors: tuple) -> None:
        factors = tuple(factors)
        self._tensor_factors: "tuple[ModuleParent, ...]" = factors
        source = CartesianProductOfSets(factors)
        CoconeCategory.__init__(self, ambient_category, (0,), (source,), ())

    def _repr_(self) -> str:
        return (
            f"Category of tensor products of {self._tensor_factors} "
            f"in {self._ambient_category}"
        )

    class ParentMethods(CoconeCategory.ParentMethods):
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
                element.parent() is factor
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
