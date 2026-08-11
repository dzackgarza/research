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
from sage_lattice_category_spike.objects.sets import Sets
from dzack_research.preamble.refine import refine
from typing import Any, Self, TYPE_CHECKING

from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.structure.parent import Parent

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from sage_lattice_category_spike.lexicon import OrderedSet


class DiagramCategory(Category):
    r"""A diagram \(F:J\to\mathbf{C}\): a family of objects and morphisms."""

    @staticmethod
    def __classcall_private__(
        cls: type,
        ambient_category: Category,
        objects: tuple,
        morphisms: tuple = (),
    ) -> "DiagramCategory":
        return super().__classcall__(
                cls, ambient_category, tuple(objects), tuple(morphisms)
            )

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
    def __classcall_private__(
        cls: type,
        ambient_category: Category,
        index_set: "OrderedSet",
        objects: tuple,
        morphisms: tuple = (),
    ) -> "DirectedSystem":
        return super().__classcall__(
                cls, ambient_category, index_set, tuple(objects), tuple(morphisms)
            )

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
    def __classcall_private__(
        cls: type,
        ambient_category: Category,
        index_set: "OrderedSet",
        objects: tuple,
        morphisms: tuple = (),
    ) -> "InverseSystem":
        return super().__classcall__(
                cls, ambient_category, index_set, tuple(objects), tuple(morphisms)
            )

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
        def structure_morphisms(self: Self) -> "tuple[Morphism, ...]":
            r"""Return the projections \(\pi_i:A\to X_i\)."""
            return self._structure_morphisms

        def structure_morphism(self: Self, i: "Integer") -> Morphism:
            r"""Return the \(i\)-th projection \(\pi_i:A\to X_i\)."""
            return self._structure_morphisms[i]

        def factors(self: Self) -> "tuple[Parent, ...]":
            r"""Return the factor objects \(X_i\) of the diagram."""
            return self.category()._diagram_objects

        def factor(self: Self, i: "Integer") -> Parent:
            r"""Return the \(i\)-th factor \(X_i\)."""
            return self.category()._diagram_objects[i]


class CoconeCategory(InverseSystem):
    r"""A cocone under an inverse system: a coapex \(A\) with injections \(\iota_i:X_i\to A\)."""

    def _repr_(self) -> str:
        return f"Category of cocones under {self._diagram_objects} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [InverseSystem(self._ambient_category, self._index_set, self._diagram_objects, self._diagram_morphisms)]

    class ParentMethods:
        def costructure_morphisms(self: Self) -> "tuple[Morphism, ...]":
            r"""Return the injections \(\iota_i:X_i\to A\)."""
            return self._costructure_morphisms

        def costructure_morphism(self: Self, i: "Integer") -> Morphism:
            r"""Return the \(i\)-th injection \(\iota_i:X_i\to A\)."""
            return self._costructure_morphisms[i]

        def cofactors(self: Self) -> "tuple[Parent, ...]":
            r"""Return the cofactor objects \(X_i\) of the diagram."""
            return self.category()._diagram_objects

        def cofactor(self: Self, i: "Integer") -> Parent:
            r"""Return the \(i\)-th cofactor \(X_i\)."""
            return self.category()._diagram_objects[i]


class ProductCategory(ConeCategory):
    r"""A product: a cone over a discrete diagram. Parameterized by factors."""

    @staticmethod
    def __classcall_private__(
        cls: type,
        ambient_category: Category,
        factors: tuple,
    ) -> "ProductCategory":
        return super().__classcall__(cls, ambient_category, tuple(factors))

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
    def __classcall_private__(
        cls: type,
        ambient_category: Category,
        cofactors: tuple,
    ) -> "CoproductCategory":
        return super().__classcall__(cls, ambient_category, tuple(cofactors))

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
    def __classcall_private__(
        cls: type,
        ambient_category: Category,
        factors: tuple,
    ) -> "BiproductCategory":
        return super().__classcall__(cls, ambient_category, tuple(factors))

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


Category.Diagram = lambda self, objects, morphisms=(): DiagramCategory(self, objects, morphisms)
Category.DirectedSystem = lambda self, index_set, objects, morphisms=(): DirectedSystem(self, index_set, objects, morphisms)
Category.InverseSystem = lambda self, index_set, objects, morphisms=(): InverseSystem(self, index_set, objects, morphisms)
Category.Cone = lambda self, index_set, objects, morphisms=(): ConeCategory(self, index_set, objects, morphisms)
Category.Cocone = lambda self, index_set, objects, morphisms=(): CoconeCategory(self, index_set, objects, morphisms)
Category.Product = lambda self, factors: ProductCategory(self, factors)
Category.Coproduct = lambda self, cofactors: CoproductCategory(self, cofactors)
Category.Biproduct = lambda self, factors: BiproductCategory(self, factors)
Category.DirectSum = lambda self, factors: DirectSumCategory(self, factors)


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
    return apex


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
    return coapex


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
    return domain


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
    return codomain


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
    assert obj is injections[0].codomain(), (
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
    return obj


# Direct sum is the additive synonym for biproduct: in an additive category
# the product and the coproduct of a finite family agree, and ``DirectSum``
# is what that one object is called there.  The name goes to *this*
# operation, and not to declaring an object decomposed, because it is the
# construction: the universal property produces the object, so the name
# denotes the thing rather than a property of a thing already built.
# ``DirectSumDecomposition`` in ``direct_sum_objects`` is the other one.
DirectSum = Biproduct

class CartesianProductOfSets(Parent):
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

    def __iter__(self) -> Any:
        from itertools import product as _product

        return iter(_product(*self._factors))

    def __contains__(self, element: Any) -> bool:
        return (
            isinstance(element, tuple)
            and len(element) == len(self._factors)
            and all(
                component.parent() is factor
                for component, factor in zip(element, self._factors)
            )
        )

    def _element_constructor_(self, element: Any) -> tuple:
        r"""Return the tuple as an element of this set.

        An element here is a tuple of elements of the factors and nothing
        more, so there is no element class to build; the constructor exists
        because every map out of this set coerces its argument through the
        domain before evaluating it.
        """
        element = tuple(element)
        assert element in self, (
            f"{element} is not a tuple of elements of the factors of {self}"
        )
        return element

    def __call__(self, element: Any) -> tuple:
        r"""Return the tuple, without Sage's default conversion.

        ``Parent.__call__`` routes through a conversion map declared to
        return an ``Element``, which a tuple is not.  The elements here are
        tuples -- that is what a product of sets has -- so the constructor
        is called directly.
        """
        return self._element_constructor_(element)

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
    def __classcall_private__(
        cls: type,
        ambient_category: Category,
        factors: tuple,
    ) -> "TensorProductCategory":
        return super().__classcall__(cls, ambient_category, tuple(factors))

    def __init__(self, ambient_category: Category, factors: tuple) -> None:
        factors = tuple(factors)
        self._tensor_factors = factors
        source = CartesianProductOfSets(factors)
        CoconeCategory.__init__(self, ambient_category, (0,), (source,), ())

    def _repr_(self) -> str:
        return (
            f"Category of tensor products of {self._tensor_factors} "
            f"in {self._ambient_category}"
        )

    class ParentMethods(CoconeCategory.ParentMethods):
        def tensor_factors(self: Any) -> "tuple[Parent, ...]":
            r"""Return the factors \(X_i\)."""
            return self.category()._tensor_factors

        def tensor_factor(self: Any, i: Any) -> Parent:
            r"""Return the \(i\)-th factor \(X_i\)."""
            return self.category()._tensor_factors[i]

        def cartesian_source(self: Any) -> Parent:
            r"""Return \(M\times N\), the object this cocone sits under."""
            return self.category()._diagram_objects[0]

        def universal_bilinear_map(self: Any) -> Morphism:
            r"""Return \(\otimes:M\times N\to M\otimes N\), the cocone's structure map."""
            return self.costructure_morphism(0)

        def pure_tensor(self: Any, *elements: Any) -> Any:
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
            return self._pure_tensor(*elements)

        def from_bilinear(self: Any, bilinear: Any, codomain: Any) -> Morphism:
            r"""Factor a bilinear map through \(\otimes\).

            For bilinear \(\beta:M\times N\to P\) there is a unique
            \(\bar\beta:M\otimes N\to P\) with
            \(\bar\beta(m\otimes n)=\beta(m,n)\).  This is the only source
            of morphisms out of a tensor product.
            """
            left, right = self.tensor_factors()
            return self.hom(
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


Category.TensorProduct = lambda self, factors: TensorProductCategory(self, factors)
