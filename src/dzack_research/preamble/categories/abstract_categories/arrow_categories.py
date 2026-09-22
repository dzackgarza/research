r"""Arrow categories, commuting squares, cores, and slice-style categories.

The arrow category of ``C`` is the functor category out of the walking arrow,

.. MATH::

    \mathrm{Ar}(C) = [[1], C], \qquad [1] = \mathtt{FiniteOrdinalCategory(2)},

reached as ``C.ArrowCategory()``, which is ``Cat().Mor(FiniteOrdinalCategory(2), C)``.
An arrow ``f`` of ``C`` is the functor ``[1] -> C`` sending ``0 -> 1`` to
``f``, and a morphism of arrows is a natural transformation between two such
functors: its components at ``0`` and ``1`` are the two edges of a commuting
square.  The slice, coslice, endomorphism, isomorphism, automorphism,
monomorphism, epimorphism and endofunctor-algebra categories are subcategories
of ``Ar(C)``: each declares it and states only its condition on arrows.
"""

from __future__ import annotations

from typing import Any

from sage.categories.category import Category
from sage.categories.mor import Mor as SageMor
from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.classcall_metaclass import typecall
from sage.misc.unknown import Unknown, UnknownClass
from sage.structure.dynamic_class import DynamicMetaclass
from sage.structure.element import parent
from sage.structure.parent import Parent

from dzack_research.preamble.categories.abstract_categories.cat import (
    Cat,
    CategoryFunctorMorphism,
    NaturalTransformationMor,
    NaturalTransformationMorphism,
    _FunctorCategory,
)
from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    CategoricalIsomorphism,
    FixedRestrictedMorCategory,
    MorCategories,
    MorCategoryConstruction,
    _RestrictedMorCategoryOf,
    _category_accepts_morphism,
    _category_mor_parent,
    _precomposable,
)
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.functors.core import Functor, NaturalTransformation
from dzack_research.preamble.categories.sets.indexed_families import IndexedFamily, indexed_family
from dzack_research.preamble.owned_category import _object_of
from dzack_research.preamble.owned_category_bases import Category as OwnedCategoryBase


class _ArrowAsFunctor(Functor):
    r"""The functor ``[1] -> C`` sending the arrow ``0 -> 1`` to one morphism of ``C``."""

    def __init__(self, base_category: Category, arrow: Morphism) -> None:
        from dzack_research.preamble.categories.abstract_categories.products import (
            FiniteOrdinalCategory,
        )

        self._arrow = arrow
        super().__init__(FiniteOrdinalCategory(2), base_category)

    def arrow(self) -> Morphism:
        return self._arrow

    def _apply_object(self, obj: Parent) -> Parent:
        match obj.position():
            case 0:
                return self.arrow().domain()
            case 1:
                return self.arrow().codomain()
            case _:
                raise ValueError("the walking-arrow category has exactly two objects")

    def _apply_morphism(self, morphism: Map) -> Map:
        left = morphism.domain().position()
        right = morphism.codomain().position()
        if left == right:
            endpoint = self.arrow().domain() if left == 0 else self.arrow().codomain()
            return _category_mor_parent(self.codomain(), endpoint, endpoint).identity()
        if left == 0 and right == 1:
            return self.arrow()
        raise ValueError("the walking-arrow category has no decreasing morphism")


@cached_function(key=lambda category, arrow: (id(category), id(arrow)))
def _walking_arrow_functor(category: Category, arrow: Morphism) -> _ArrowAsFunctor:
    r"""The functor ``[1] -> category`` picking out ``arrow``, one for each arrow.

    It is the defining datum an arrow determines, so an arrow category's entry
    receives the same functor each time it is handed the same arrow, and
    builds one object for it.
    """
    return _ArrowAsFunctor(category, arrow)


class CommutativeSquare(NaturalTransformationMorphism):
    r"""A morphism of ``Ar(C)``: a natural transformation between two arrows.

    For arrows ``f: A -> B`` and ``g: A' -> B'`` of ``C``, read as functors out
    of the walking arrow, the components at ``0`` and ``1`` are the left edge
    ``A -> A'`` and the right edge ``B -> B'``, and naturality at ``0 -> 1`` is
    the square ``g left = right f``.
    """

    def _walking_arrow(self) -> Category:
        return self.domain().functor().domain()

    def left(self) -> Morphism:
        r"""The component at ``0``: the edge between the sources."""
        return self.component(self._walking_arrow()(0))

    def right(self) -> Morphism:
        r"""The component at ``1``: the edge between the targets."""
        return self.component(self._walking_arrow()(1))

    def components(self):
        r"""The two natural-transformation components in their owned product."""
        product = Sets().product((self.left().parent(), self.right().parent()))
        return product((self.left(), self.right()))

    def __eq__(self, other: Any) -> bool | UnknownClass:
        r"""Two squares between the same arrows agree when both of their edges do."""
        if self is other:
            return True
        if parent(other) is not self.parent():
            return False
        equalities = (self.left() == other.left(), self.right() == other.right())
        if any(answer is False for answer in equalities):
            return False
        return True if all(answer is True for answer in equalities) else Unknown

    def __ne__(self, other: Any) -> bool | UnknownClass:
        equal = self == other
        return Unknown if equal is Unknown else not equal

    def __hash__(self) -> int:
        return hash(id(self.parent()))

    def __mul__(self, other):
        if not _precomposable(self, other):
            return NotImplemented
        category = self.parent().arrow_category()
        other = category.Mor(other.domain(), other.codomain())(other)
        # If r f = g l and s g = h m, then (s r) f = h (m l).
        return category.Mor(other.domain(), self.codomain())._from_commuting_edges(
            self.left() * other.left(),
            self.right() * other.right(),
        )

    def _repr_(self) -> str:
        return f"Commutative square from {self.domain()} to {self.codomain()}"


class ArrowMor(NaturalTransformationMor):
    r"""The Mor of ``Ar(C)``, or of a subcategory of it, written by its two edges."""

    Element = CommutativeSquare

    def arrow_category(self) -> Category:
        return self.base_category()

    def _edge_category(self) -> Category:
        r"""``C``, the category whose morphisms the edges are."""
        return self.source().codomain()

    def _element_constructor_(self, left, right=None):
        match left:
            case CommutativeSquare() if right is None:
                if left.parent() is self:
                    return left
                if left.domain() is not self.domain() or left.codomain() is not self.codomain():
                    raise ValueError("the square has the wrong arrow objects")
                left, right = left.left(), left.right()
            case NaturalTransformation() if right is None:
                walking_arrow = left.source().domain()
                left, right = left.component(walking_arrow(0)), left.component(walking_arrow(1))
        if right is None:
            left, right = left
        return self._square(left, right, verify=True)

    def _square(
        self,
        left: Morphism,
        right: Morphism,
        *,
        verify: bool,
        element_class=None,
        construction_data=None,
    ) -> CommutativeSquare:
        r"""The transformation with these two edges, after checking they bound a square here."""
        source = self.domain().arrow()
        target = self.codomain().arrow()
        if left.domain() is not source.domain() or left.codomain() is not target.domain():
            raise ValueError("the left edge has the wrong square endpoints")
        if right.domain() is not source.codomain() or right.codomain() is not target.codomain():
            raise ValueError("the right edge has the wrong square endpoints")
        base = self._edge_category()
        if not _category_accepts_morphism(base, source.domain(), target.domain(), left):
            raise ValueError("the left edge is not a morphism of the base category")
        if not _category_accepts_morphism(base, source.codomain(), target.codomain(), right):
            raise ValueError("the right edge is not a morphism of the base category")
        if verify and (right * source == target * left) is not True:
            raise ValueError("the supplied edges do not establish a commuting square")
        edges = {0: left, 1: right}
        transformation = NaturalTransformation(
            self.source(),
            self.target(),
            lambda obj: edges[obj.position()],
        )
        selected = self.element_class if element_class is None else element_class
        return selected(self, transformation, **dict(construction_data or {}))

    def _from_commuting_edges(self, left: Morphism, right: Morphism) -> CommutativeSquare:
        r"""Construct edges whose commutativity follows from their construction."""
        return self._square(left, right, verify=False)

    def identity(self) -> CommutativeSquare:
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on an endomorphism Mor object")
        arrow = self.domain().arrow()
        category = self._edge_category()
        return self._from_commuting_edges(
            _category_mor_parent(category, arrow.domain(), arrow.domain()).identity(),
            _category_mor_parent(category, arrow.codomain(), arrow.codomain()).identity(),
        )

    def identity_at(self, obj: Parent) -> CommutativeSquare:
        return self.arrow_category().Mor(obj, obj).identity()


class ArrowMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = ArrowMor


class _WalkingArrowFunctorCategory(_FunctorCategory):
    r"""``Ar(C) = [[1], C]``, the functor category out of the walking arrow.

    This is ``Cat().Mor(FiniteOrdinalCategory(2), C)``: ``Cat``'s Mor family
    selects this realization for the walking arrow, so there is one category
    object, and ``C.ArrowCategory()`` names it.  Its objects are functors built
    by the entry of ``[J, C]`` and its morphisms are natural transformations;
    what it adds is the vocabulary the shape ``[1]`` names -- the arrow a
    functor picks out, its source and target, the two edges of a square -- and
    the entry that reads an arrow of ``C`` as the functor it determines.
    """

    _MorCategory = ArrowMorCategoryConstruction

    class ParentMethods:
        r"""A functor ``[1] -> C``, read as the arrow of ``C`` it picks out."""

        def arrow(self) -> Morphism:
            r"""The image of the arrow ``0 -> 1`` of the walking arrow."""
            walking_arrow = self.functor().domain()
            return self.functor()(walking_arrow.Mor(walking_arrow(0), walking_arrow(1)).unique())

        def source_object(self):
            return self.functor()(self.functor().domain()(0))

        def target_object(self):
            return self.functor()(self.functor().domain()(1))

        def arrow_category(self) -> Category:
            return self.functor_category()

        def _repr_(self) -> str:
            return f"Arrow object ({self.source_object()} -> {self.target_object()})"

    def an_object(self):
        r"""The identity of an object of ``C``, as an arrow."""
        base = self.codomain_category()
        witness = base.an_object()
        return self.object(_category_mor_parent(base, witness, witness).identity())

    def admits_arrow(self, arrow: Morphism) -> bool:
        r"""Whether ``arrow`` is an arrow of ``C``."""
        base = self.codomain_category()
        return (
            arrow.domain() in base
            and arrow.codomain() in base
            and _category_accepts_morphism(base, arrow.domain(), arrow.codomain(), arrow)
        )

    def object(self, value: Functor | Morphism):
        r"""The object of ``[[1], C]`` on a functor out of the walking arrow, or on an arrow of ``C``.

        The functor is the defining datum.  An arrow ``f`` of ``C`` determines
        the functor sending ``0 -> 1`` to ``f``, and that functor is handed to
        the one entry of ``[[1], C]``.  In particular a morphism of ``Cat``
        entering ``Ar(Cat)`` is an arrow of the base, not its underlying
        functor reinterpreted as a walking-arrow diagram.
        """
        match value:
            case Functor():
                return super().object(value)
        if not self.admits_arrow(value):
            raise TypeError("the supplied morphism is not an object of this arrow category")
        return super().object(_walking_arrow_functor(self.codomain_category(), value))

    __call__ = object

    def morphism(
        self,
        source: Parent,
        target: Parent,
        left: Morphism,
        right: Morphism,
    ) -> CommutativeSquare:
        return self.Mor(source, target)(left, right)

    def compose(
        self,
        second: CommutativeSquare,
        first: CommutativeSquare,
    ) -> CommutativeSquare:
        if first.codomain() is not second.domain():
            raise ValueError("arrow-category squares are not composable")
        return second * first

    def _repr_(self) -> str:
        return f"Arrow category of {self.codomain_category()}"


class _SubcategoryOfArrows(OwnedCategory):
    r"""A subcategory of ``Ar(C)`` whose objects are the arrows of ``C`` satisfying a condition.

    It declares ``Ar(C)``, or a subcategory of it, and states only its
    condition, :meth:`admits_arrow`.  Its entry reads an arrow as the functor
    out of the walking arrow it determines and builds the object on that
    functor, so the object is placed here and threads through ``Ar(C)``.  An
    object of the declared categories whose arrow satisfies the condition lies
    here as well.  A subcategory whose morphisms are all the squares between
    its objects declares no Mor family and has the Mor of ``Ar(C)``.
    """

    @abstract_method
    def base_category(self) -> Category:
        r"""``C``, whose arrows the objects of this category are."""

    def admits_arrow(self, arrow: Morphism) -> bool:
        r"""Whether ``arrow`` is the arrow of an object of this category."""
        base = self.base_category()
        return (
            arrow.domain() in base
            and arrow.codomain() in base
            and _category_accepts_morphism(base, arrow.domain(), arrow.codomain(), arrow)
        )

    def an_object(self):
        r"""The identity of an object of ``C``, as an arrow."""
        base = self.base_category()
        witness = base.an_object()
        return self.object(_category_mor_parent(base, witness, witness).identity())

    def object(self, arrow: Morphism) -> Parent:
        if not self.admits_arrow(arrow):
            raise TypeError("the supplied morphism is not an object of this arrow category")
        return self._object_on(_walking_arrow_functor(self.base_category(), arrow))

    __call__ = object

    @cached_method(key=lambda self, functor: id(functor))
    def _object_on(self, functor: Functor):
        return _object_of(self, functor=functor)

    def __contains__(self, candidate: Any) -> bool:
        r"""Placement, or an object of the declared categories whose arrow satisfies the condition."""
        match candidate:
            case _ if super().__contains__(candidate):
                return True
            case _ if all(candidate in category for category in self.super_categories()):
                return self.admits_arrow(candidate.arrow())
            case _:
                return False

    def Mor(self, source: Parent, target: Parent) -> ArrowMor:
        if source not in self or target not in self:
            raise TypeError("a Mor here requires two arrow objects of this category")
        return self.MorCategory().Of(source, target)

    def morphism(
        self,
        source: Parent,
        target: Parent,
        left: Morphism,
        right: Morphism,
    ) -> CommutativeSquare:
        return self.Mor(source, target)(left, right)

    def identity(self, arrow_object: Parent) -> CommutativeSquare:
        return self.Mor(arrow_object, arrow_object).identity()

    def compose(
        self,
        second: CommutativeSquare,
        first: CommutativeSquare,
    ) -> CommutativeSquare:
        if first.codomain() is not second.domain():
            raise ValueError("arrow-category squares are not composable")
        return second * first


class _EndofunctorAlgebraMor(ArrowMor):
    r"""Morphisms ``f`` with ``f a = b T(f)`` between ``T``-algebras.

    A morphism of the arrow category is a commuting square.  Here its left
    edge is not another chosen datum: it is forced to be ``T(f)`` by the
    endofunctor.  Thus one underlying arrow determines one structured
    morphism, exactly as in ``Inserter(T, Id)``.
    """

    class Element(CommutativeSquare):
        r"""A structured map acting through its underlying morphism."""

        def underlying_morphism(self) -> Morphism:
            return self.right()

        def _call_(self, element):
            return self.underlying_morphism()(element)

    def _element_constructor_(self, left, right=None):
        category = self.arrow_category()
        match left:
            case CommutativeSquare() if right is None:
                if left.parent() is self:
                    return left
                if left.domain() is not self.domain() or left.codomain() is not self.codomain():
                    raise ValueError("the algebra morphism has the wrong endpoints")
                left, right = left.left(), left.right()
        if right is None:
            right = left
            left = category.endofunctor()(right)
        else:
            expected = category.endofunctor()(right)
            if (left == expected) is not True:
                raise ValueError(
                    "the left edge of an endofunctor-algebra map must be the image of its underlying morphism"
                )
            left = expected
        return self._square(left, right, verify=True)


class _EndofunctorAlgebraForgetfulFunctor(Functor):
    r"""The forgetful functor ``Alg(T) -> C``, ``(X, a) |-> X``."""

    _faithful = True

    def __init__(self, algebras: _EndofunctorAlgebraCategory) -> None:
        self._algebras = algebras
        super().__init__(algebras, algebras.base_category())

    def _apply_object(self, algebra: Parent) -> Parent:
        return algebra.target_object()

    def _apply_morphism(self, morphism: Map) -> Map:
        return morphism.right()

    def _repr_(self) -> str:
        return f"Forgetful functor {self.domain()} -> {self.codomain()}"


class _EndofunctorAlgebraMorCategory(MorCategoryConstruction):
    FixedCategoryClass = _EndofunctorAlgebraMor


class _EndofunctorAlgebraCategory(_SubcategoryOfArrows):
    r"""The category of algebras of an endofunctor ``T : C -> C``.

    An object is an arrow ``a : T(X) -> X`` of ``C``, built as an object of
    ``Ar(C)`` on that exact arrow, so neither endpoint is rebuilt.  Its Mors
    are cut down from all commuting squares to the squares whose left edge is
    ``T(f)``; hence its objects and morphisms are those of ``Inserter(T, Id_C)``.
    """

    _MorCategory = _EndofunctorAlgebraMorCategory

    def __init__(self, endofunctor: Functor) -> None:
        if endofunctor.domain() is not endofunctor.codomain():
            raise ValueError("an endofunctor must have one common domain and codomain")
        self._endofunctor = endofunctor
        super().__init__()

    def _make_named_class_key(self, name):
        return self._endofunctor._cache_key()

    def endofunctor(self) -> Functor:
        return self._endofunctor

    def base_category(self) -> Category:
        return self.endofunctor().domain()

    def arrow_category(self) -> Category:
        return self.base_category().ArrowCategory()

    def super_categories(self):
        from dzack_research.preamble.categories.abstract_categories.products import (
            FiniteOrdinalCategory,
        )

        return [Cat().Mor(FiniteOrdinalCategory(2), self.base_category())]

    def admits_arrow(self, arrow: Morphism) -> bool:
        r"""An algebra structure on its target: an arrow ``T(X) -> X``."""
        return super().admits_arrow(arrow) and arrow.domain() is self.endofunctor()(arrow.codomain())

    def algebra(self, underlying_object: Parent, structure: Morphism):
        r"""Return ``(X, structure : T(X) -> X)`` for the object ``X`` of ``C``.

        Both the supplied object and the supplied structure arrow are kept
        literally. In particular two different structure arrows on one object
        produce two different algebra objects whose forgetful image is that
        same object.
        """
        if underlying_object not in self.base_category():
            raise TypeError("the underlying object is not an object of the endofunctor's category")
        if structure.domain() is not self.endofunctor()(underlying_object):
            raise ValueError("the structure morphism must start at T(X)")
        if structure.codomain() is not underlying_object:
            raise ValueError("the structure morphism must end at its exact supplied object")
        return self.object(structure)

    def underlying_object(self, algebra: Parent):
        if algebra not in self:
            raise TypeError("the object is not an algebra of this endofunctor")
        return algebra.target_object()

    def structure(self, algebra: Parent) -> Morphism:
        if algebra not in self:
            raise TypeError("the object is not an algebra of this endofunctor")
        return algebra.arrow()

    def homomorphism(
        self,
        source: Parent,
        target: Parent,
        underlying_morphism: Morphism,
    ) -> CommutativeSquare:
        r"""Equip ``f`` with its forced commuting square ``(T(f), f)``."""
        return self.Mor(source, target)(underlying_morphism)

    @cached_method
    def forgetful(self) -> Functor:
        return _EndofunctorAlgebraForgetfulFunctor(self)

    def _repr_(self) -> str:
        return f"Algebras of {self.endofunctor()}"


class SliceMor(ArrowMor):
    r"""Morphisms in a slice; the edge at the fixed codomain is the identity."""

    def _element_constructor_(self, factor, right=None):
        match factor:
            case CommutativeSquare() if right is None:
                if factor.parent() is self:
                    return factor
                if factor.domain() is not self.domain() or factor.codomain() is not self.codomain():
                    raise ValueError("the slice morphism has the wrong endpoints")
                factor, right = factor.left(), factor.right()
        fixed = self.domain().arrow().codomain()
        if self.codomain().arrow().codomain() is not fixed:
            raise ValueError("slice objects require one fixed codomain")
        identity = _category_mor_parent(self._edge_category(), fixed, fixed).identity()
        if right is not None and (right == identity) is not True:
            raise ValueError("the fixed edge of a slice morphism is the identity")
        return self._square(factor, identity, verify=True)

    def canonical_morphism(self) -> CommutativeSquare:
        inclusion = self.domain().arrow()
        target_inclusion = self.codomain().arrow()
        return self(inclusion.factor_through(target_inclusion))


class SliceMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = SliceMor


class SliceCategory(_SubcategoryOfArrows):
    r"""The slice category \(C/X\): arrows into ``X``, with squares whose right edge is ``id_X``.

    Unverified specimens retain equal-but-distinct base sets and keep the
    slice and coslice fixed edges under nonidentity composition::

        sage: from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
        sage: from dzack_research.preamble.categories.functors.core import IdentityFunctor
        sage: from dzack_research.preamble.categories.sets.set_categories import Sets
        sage: points = finite_ordered_set(("a", "b"))
        sage: other_points = finite_ordered_set(("a", "b"))
        sage: points == other_points and points is not other_points
        True
        sage: SliceCategory(Sets(), points).base_object() is points
        True
        sage: SliceCategory(Sets(), other_points).base_object() is other_points
        True
        sage: CosliceCategory(Sets(), other_points).base_object() is other_points
        True
        sage: SubobjectCategory(Sets(), other_points).base_object() is other_points
        True
        sage: one = finite_ordered_set(("*",))
        sage: swap = Sets().Mor(points, points)(lambda point: "b" if point == "a" else "a")
        sage: slice_category = SliceCategory(Sets(), one)
        sage: obj = slice_category(Sets().Mor(points, one)(lambda point: "*"))
        sage: obj in Sets().ArrowCategory()
        True
        sage: Mor = slice_category.Mor(obj, obj)
        sage: Mor is slice_category.MorCategory().Of(obj, obj)
        True
        sage: square = Mor(swap)
        sage: square * square == Mor.identity()
        True
        sage: coslice = CosliceCategory(Sets(), one)
        sage: obj = coslice(Sets().Mor(one, points)(lambda point: "a"))
        sage: Mor = coslice.Mor(obj, obj)
        sage: collapse = Mor(Sets().Mor(points, points)(lambda point: "a"))
        sage: collapse * collapse == collapse
        True
        sage: Mor.identity() * collapse == collapse
        True
        sage: algebras = IdentityFunctor(Sets()).algebras()
        sage: algebra = algebras.algebra(points, swap)
        sage: Mor = algebras.Mor(algebra, algebra)
        sage: Mor is algebras.MorCategory().Of(algebra, algebra)
        True
        sage: Mor(swap) * Mor(swap) == Mor.identity()
        True
    """

    _MorCategory = SliceMorCategoryConstruction

    @staticmethod
    @cached_function(key=lambda cls, base_category, base_object: (cls, id(base_category), id(base_object)))
    def __classcall__(cls, base_category: Category, base_object: Parent):
        match cls:
            case DynamicMetaclass():
                return cls.__base__(base_category, base_object)
        return typecall(cls, base_category, base_object)

    def __init__(self, base_category: Category, base_object: Parent) -> None:
        if base_object not in base_category:
            raise TypeError("the slice base must be an object of its base category")
        self._base_category = base_category
        self._base_object = base_object
        super().__init__()

    def _make_named_class_key(self, name):
        return self._base_category, id(self._base_object)

    def base_category(self) -> Category:
        return self._base_category

    def base_object(self) -> Parent:
        return self._base_object

    def object(
        self,
        arrow: Morphism,
        *,
        _engine=None,
        construction_data=None,
    ) -> Parent:
        r"""Construct an object of ``C/X``, optionally with a private realization."""
        if not self.admits_arrow(arrow):
            raise TypeError("the supplied morphism is not an object of this slice")
        functor = _walking_arrow_functor(self.base_category(), arrow)
        if _engine is None and construction_data is None:
            return self._object_on(functor)
        return _object_of(
            self,
            _engine=None if _engine is None else (self, _engine, None),
            functor=functor,
            **dict(construction_data or {}),
        )

    __call__ = object

    def super_categories(self):
        from dzack_research.preamble.categories.abstract_categories.products import (
            FiniteOrdinalCategory,
        )

        return [Cat().Mor(FiniteOrdinalCategory(2), self.base_category())]

    def an_object(self):
        r"""The identity of the fixed base object."""
        base_object = self.base_object()
        return self.object(
            _category_mor_parent(self.base_category(), base_object, base_object).identity()
        )

    def admits_arrow(self, arrow: Morphism) -> bool:
        r"""An arrow into the fixed base object."""
        return arrow.codomain() is self.base_object() and super().admits_arrow(arrow)

    def _repr_(self) -> str:
        return f"Slice category {self.base_category()}/{self.base_object()}"


class CosliceMor(ArrowMor):
    r"""Morphisms in a coslice; the edge at the fixed domain is the identity."""

    def _element_constructor_(self, left, right=None):
        match left:
            case CommutativeSquare() if right is None:
                if left.parent() is self:
                    return left
                if left.domain() is not self.domain() or left.codomain() is not self.codomain():
                    raise ValueError("the coslice morphism has the wrong endpoints")
                left, right = left.left(), left.right()
        fixed = self.domain().arrow().domain()
        if self.codomain().arrow().domain() is not fixed:
            raise ValueError("coslice objects require one fixed domain")
        identity = _category_mor_parent(self._edge_category(), fixed, fixed).identity()
        if right is None:
            right = left
        elif (left == identity) is not True:
            raise ValueError("the fixed edge of a coslice morphism is the identity")
        return self._square(identity, right, verify=True)

    def identity(self) -> CommutativeSquare:
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on an endomorphism Mor object")
        target = self.domain().target_object()
        source = self.domain().source_object()
        category = self._edge_category()
        return self._from_commuting_edges(
            _category_mor_parent(category, source, source).identity(),
            _category_mor_parent(category, target, target).identity(),
        )


class CosliceMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = CosliceMor


class CosliceCategory(_SubcategoryOfArrows):
    r"""The coslice category \(X/C\): arrows out of ``X``, with squares whose left edge is ``id_X``."""

    _MorCategory = CosliceMorCategoryConstruction

    @staticmethod
    @cached_function(key=lambda cls, base_category, base_object: (cls, id(base_category), id(base_object)))
    def __classcall__(cls, base_category: Category, base_object: Parent):
        match cls:
            case DynamicMetaclass():
                return cls.__base__(base_category, base_object)
        return typecall(cls, base_category, base_object)

    def __init__(self, base_category: Category, base_object: Parent) -> None:
        if base_object not in base_category:
            raise TypeError("the coslice base must be an object of its base category")
        self._base_category = base_category
        self._base_object = base_object
        super().__init__()

    def _make_named_class_key(self, name):
        return self._base_category, id(self._base_object)

    def base_category(self) -> Category:
        return self._base_category

    def base_object(self) -> Parent:
        return self._base_object

    def super_categories(self):
        from dzack_research.preamble.categories.abstract_categories.products import (
            FiniteOrdinalCategory,
        )

        return [Cat().Mor(FiniteOrdinalCategory(2), self.base_category())]

    def an_object(self):
        r"""The identity of the fixed base object."""
        base_object = self.base_object()
        return self.object(
            _category_mor_parent(self.base_category(), base_object, base_object).identity()
        )

    def admits_arrow(self, arrow: Morphism) -> bool:
        r"""An arrow out of the fixed base object."""
        return arrow.domain() is self.base_object() and super().admits_arrow(arrow)

    def _repr_(self) -> str:
        return f"Coslice category {self.base_object()}/{self.base_category()}"


class _FullSubcategoryOfArrows(_SubcategoryOfArrows):
    r"""A full subcategory of ``Ar(C)`` cut out by a property of its arrows.

    Parameterized by ``C`` alone; each category of this shape states its own
    declaration, so the declared graph reads it at the category.
    """

    def __init__(self, base_category: Category) -> None:
        self._base_category = base_category
        super().__init__()

    def _make_named_class_key(self, name):
        return self._base_category

    def base_category(self) -> Category:
        return self._base_category


class _EndArrowCategory(_FullSubcategoryOfArrows):
    r"""The full subcategory of ``Ar(C)`` on endomorphisms."""

    def super_categories(self):
        from dzack_research.preamble.categories.abstract_categories.products import (
            FiniteOrdinalCategory,
        )

        return [Cat().Mor(FiniteOrdinalCategory(2), self.base_category())]

    def admits_arrow(self, arrow: Morphism) -> bool:
        return arrow.domain() is arrow.codomain() and super().admits_arrow(arrow)

    def _repr_(self) -> str:
        return f"Endomorphism arrows of {self.base_category()}"


class _IsoArrowCategory(_FullSubcategoryOfArrows):
    r"""The full subcategory of ``Ar(C)`` on isomorphisms.

    Which arrows are isomorphisms is the core's question: an arrow lies here
    when it is an arrow of ``Core(C)``.
    """

    def super_categories(self):
        from dzack_research.preamble.categories.abstract_categories.products import (
            FiniteOrdinalCategory,
        )

        return [Cat().Mor(FiniteOrdinalCategory(2), self.base_category())]

    def admits_arrow(self, arrow: Morphism) -> bool:
        return super().admits_arrow(arrow) and arrow in self.base_category().Core().Mor(
            arrow.domain(), arrow.codomain()
        )

    def _repr_(self) -> str:
        return f"Isomorphism arrows of {self.base_category()}"


class _AutomorphismArrowCategory(_IsoArrowCategory):
    r"""The full subcategory of the arrow category on automorphisms."""

    def super_categories(self):
        return [
            _IsoArrowCategory(self.base_category()),
            _EndArrowCategory(self.base_category()),
        ]

    def admits_arrow(self, arrow: Morphism) -> bool:
        return arrow.domain() is arrow.codomain() and super().admits_arrow(arrow)

    def _repr_(self) -> str:
        return f"Automorphism arrows of {self.base_category()}"


class _MonomorphismArrowCategory(_FullSubcategoryOfArrows):
    r"""The full subcategory of the arrow category on represented monomorphisms.

    Which arrows are monic is the base category's own question, so this asks
    the mono family that category declares.  Injectivity is the answer in sets
    and modules and is the declared default there; it is neither necessary nor
    sufficient in every category, so it is not the definition used here.
    """

    def super_categories(self):
        from dzack_research.preamble.categories.abstract_categories.products import (
            FiniteOrdinalCategory,
        )

        return [Cat().Mor(FiniteOrdinalCategory(2), self.base_category())]

    def admits_arrow(self, arrow: Morphism) -> bool:
        return super().admits_arrow(arrow) and self.base_category().category_packet().Monos().accepts(arrow)

    def _repr_(self) -> str:
        return f"Monomorphism arrows of {self.base_category()}"


class _EpimorphismArrowCategory(_FullSubcategoryOfArrows):
    r"""The full subcategory of the arrow category on represented epimorphisms.

    As for monomorphisms, the base category's declared epi family answers.
    """

    def super_categories(self):
        from dzack_research.preamble.categories.abstract_categories.products import (
            FiniteOrdinalCategory,
        )

        return [Cat().Mor(FiniteOrdinalCategory(2), self.base_category())]

    def admits_arrow(self, arrow: Morphism) -> bool:
        return super().admits_arrow(arrow) and self.base_category().category_packet().Epis().accepts(arrow)

    def _repr_(self) -> str:
        return f"Epimorphism arrows of {self.base_category()}"


def _subobject_source(subobject):
    inclusion = subobject.inclusion()
    return inclusion.domain() if inclusion is subobject else subobject


class SubobjectMorphism(Morphism):
    r"""The unique commuting-triangle map between two represented subobjects."""

    def __init__(
        self,
        parent: SubobjectMor,
        factor_morphism: Morphism,
        *,
        verify: bool = True,
    ) -> None:
        Morphism.__init__(self, parent)
        if factor_morphism.domain() is not _subobject_source(self.domain()):
            raise ValueError("the subobject factor has the wrong domain")
        if factor_morphism.codomain() is not _subobject_source(self.codomain()):
            raise ValueError("the subobject factor has the wrong codomain")
        base = parent.subobject_category().base_category()
        if not _category_accepts_morphism(
            base,
            _subobject_source(self.domain()),
            _subobject_source(self.codomain()),
            factor_morphism,
        ):
            raise ValueError("the subobject factor is not a morphism of the base category")
        if verify:
            parent._slice_mor()(factor_morphism)
        self._factor_morphism = factor_morphism

    def factor_morphism(self) -> Morphism:
        return self._factor_morphism

    def __call__(self, element):
        return self.factor_morphism()(element)

    def _call_(self, element):
        return self.factor_morphism()(element)

    def __eq__(self, other: Any) -> bool:
        # A monomorphism cancels on the left: there is at most one factor
        # commuting with the two chosen inclusions.
        return parent(other) is self.parent()

    def __ne__(self, other: Any) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(id(self.parent()))

    def __mul__(self, other):
        if not _precomposable(self, other):
            return NotImplemented
        parent_mor = self.parent().subobject_category().Mor(
            other.domain(), self.codomain()
        )
        # If j f = i and k g = j, then k (g f) = i.
        return SubobjectMorphism(
            parent_mor, self.factor_morphism() * other.factor_morphism(), verify=False
        )


class SubobjectMor(CategoricalMor):
    Element = SubobjectMorphism

    def __init__(
        self,
        family: MorCategoryConstruction,
        domain: Parent,
        codomain: Parent,
    ) -> None:
        CategoricalMor.__init__(
            self, family, domain, codomain
        )

    def subobject_category(self) -> SubobjectCategory:
        return self.base_category()

    @cached_method
    def _slice_mor(self):
        r"""The slice Mor whose fixed-edge square is this subobject Mor's triangle."""
        category = self.subobject_category()
        return category.slice_category().Mor(
            category.as_slice_object(self.domain()),
            category.as_slice_object(self.codomain()),
        )

    def _canonical_factor(self):
        factor = self.domain().inclusion().factor_through_or_none(
            self.codomain().inclusion()
        )
        if factor is None:
            raise ValueError("the first subobject is not contained in the second")
        return factor

    def has_morphism(self) -> bool:
        return (
            self.domain().inclusion().factor_through_or_none(
                self.codomain().inclusion()
            )
            is not None
        )

    def canonical_morphism(self) -> SubobjectMorphism:
        return SubobjectMorphism(self, self._canonical_factor(), verify=False)

    def _element_constructor_(self, factor_morphism=None):
        match factor_morphism:
            case SubobjectMorphism():
                if factor_morphism.parent() is self:
                    return factor_morphism
                if factor_morphism.domain() is not self.domain() or factor_morphism.codomain() is not self.codomain():
                    raise ValueError("the subobject morphism has the wrong endpoints")
                factor_morphism = factor_morphism.factor_morphism()
            case None:
                return self.canonical_morphism()
        return SubobjectMorphism(self, factor_morphism)

    def identity(self) -> SubobjectMorphism:
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on an endomorphism Mor object")
        return SubobjectMorphism(self, self._slice_mor().identity().left(), verify=False)


class SubobjectMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = SubobjectMor


class SubobjectCategory(OwnedCategoryBase):
    r"""The category of represented subobjects of one fixed object.

    An object is an object ``A`` of the base category equipped with its chosen
    monomorphism ``A.inclusion(): A -> X``.  Morphisms are the commuting
    triangles between those inclusions.

    Unverified specimen: a represented module subobject retains its selected
    inclusion when its fixed-base placement and its Mor are requested::

        sage: from dzack_research.preamble.all import Modules, ZZ
        sage: from dzack_research.preamble.refine import refine
        sage: submodule = ZZ.ideal(2)
        sage: inclusion = submodule.inclusion()
        sage: category = SubobjectCategory(Modules(ZZ), inclusion.codomain())
        sage: submodule in category
        True
        sage: _ = refine(submodule, category)
        sage: submodule in category
        True
        sage: Mor = category.Mor(submodule, submodule)
        sage: Mor is category.MorCategory().Of(submodule, submodule)
        True
        sage: identity = Mor.identity()
        sage: identity * identity == identity
        True
        sage: submodule.inclusion() is inclusion
        True
    """

    _MorCategory = SubobjectMorCategoryConstruction

    @staticmethod
    @cached_function(key=lambda cls, base_category, base_object: (cls, id(base_category), id(base_object)))
    def __classcall__(cls, base_category: Category, base_object: Parent):
        match cls:
            case DynamicMetaclass():
                return cls.__base__(base_category, base_object)
        return typecall(cls, base_category, base_object)

    def __init__(self, base_category: Category, base_object: Parent) -> None:
        if base_object not in base_category:
            raise TypeError("the subobject base must lie in its base category")
        self._base_category = base_category
        self._base_object = base_object
        super().__init__()

    def _make_named_class_key(self, name):
        return self._base_category, id(self._base_object)

    def base_category(self) -> Category:
        return self._base_category

    def base_object(self) -> Parent:
        return self._base_object

    def super_categories(self):
        r"""A subobject of an object of ``C`` is an object of ``C``.

        What the subobject additionally has is its chosen monomorphism into
        the fixed base object; forgetting that leaves an object of the base
        category, with every operation the base category owns.
        """
        return [self.base_category()]

    def slice_category(self) -> SliceCategory:
        r"""Return the slice ``C/X`` in which subobjects are monomorphisms."""
        return SliceCategory(self.base_category(), self.base_object())

    def monomorphism_category(self) -> _MonomorphismArrowCategory:
        r"""Return the monomorphism subcategory of the arrow category of ``C``."""
        return self.base_category().MonomorphismArrowCategory()

    @cached_method(key=lambda self, subobject: id(subobject))
    def as_slice_object(self, subobject: Parent) -> Parent:
        if subobject not in self:
            raise TypeError("the object is not a represented subobject of the fixed base")
        return self.slice_category()(subobject.inclusion())

    def __contains__(self, candidate: Any) -> bool:
        r"""Whether construction placed the object among these fixed-base subobjects."""
        return super().__contains__(candidate)

    def Mor(self, domain: Parent, codomain: Parent) -> SubobjectMor:
        if domain not in self or codomain not in self:
            raise TypeError("both objects must be subobjects of the fixed base object")
        return self.MorCategory().Of(domain, codomain)

    def leq(self, left: Parent, right: Parent) -> bool:
        return self.Mor(left, right).has_morphism()

    def identity(self, subobject: Parent) -> SubobjectMorphism:
        return self.Mor(subobject, subobject).identity()

    def _repr_(self) -> str:
        return f"Subobjects of {self.base_object()}"


class SetSubobjectCategory(SliceCategory):
    r"""The represented subset inclusions ``A -> X`` as the monic objects of ``Set/X``.

    Sets are the case where the subobject itself is naturally represented by
    its inclusion morphism rather than by a separately structured source
    parent.  Reuse the ordinary slice object's walking-arrow representation:
    no second subset wrapper or arrow registry is introduced.
    """

    def super_categories(self):
        return [
            SliceCategory(self.base_category(), self.base_object()),
            self.base_category().MonomorphismArrowCategory(),
        ]

    def admits_arrow(self, arrow: Morphism) -> bool:
        return (
            SliceCategory.admits_arrow(self, arrow)
            and self.base_category().MonomorphismArrowCategory().admits_arrow(arrow)
        )

    def object(
        self,
        arrow: Morphism,
        *,
        categories=(),
        construction_data=None,
        _engine=None,
    ):
        r"""Construct this represented subset, optionally with stronger owned structure or a private realization."""
        if not self.admits_arrow(arrow):
            raise TypeError("the supplied morphism is not a monomorphism into this base set")
        category = Cat().meet((self, *tuple(categories)))
        return _object_of(
            category,
            _engine=None if _engine is None else (self, _engine, None),
            functor=_walking_arrow_functor(self.base_category(), arrow),
            **dict(construction_data or {}),
        )

    __call__ = object

    def cardinality(self):
        r"""The number of represented subsets of the fixed base set."""
        return self.base_object().power_set().cardinality()

    class ParentMethods:
        def inclusion(self):
            return self.arrow()

        def underlying_set(self):
            return self.source_object()

        def domain(self):
            return self.source_object()

        def codomain(self):
            return self.target_object()

        def __contains__(self, member):
            return member in self.inclusion()

        def __iter__(self):
            return iter(self.underlying_set())

        def cardinality(self):
            return self.underlying_set().cardinality()

        def characteristic_morphism(self):
            return self.inclusion().characteristic_morphism()

        def factor_through_or_none(self, target):
            return self.inclusion().factor_through_or_none(target.inclusion())

        def factor_through(self, target):
            return self.inclusion().factor_through(target.inclusion())

        def _set_subobject_category(self):
            from dzack_research.preamble.categories.sets.set_categories import Sets

            return Sets().Subobjects(self.codomain())

        def __le__(self, other):
            return self.inclusion() <= other.inclusion()

        def union(self, other):
            return self._set_subobject_category()(self.inclusion().union(other.inclusion()))

        def intersection(self, other):
            return self._set_subobject_category()(self.inclusion().intersection(other.inclusion()))

        def difference(self, other):
            return self._set_subobject_category()(self.inclusion().difference(other.inclusion()))

        def symmetric_difference(self, other):
            return self._set_subobject_category()(self.inclusion().symmetric_difference(other.inclusion()))

        def complement(self):
            return self._set_subobject_category()(self.inclusion().complement())

        def __or__(self, other):
            return self.union(other)

        def __eq__(self, other):
            return other in self._set_subobject_category() and self.inclusion() == other.inclusion()

        __hash__ = None

        def _repr_(self):
            return repr(self.inclusion())


class SuperobjectCategory(CosliceCategory):
    r"""The category of represented superobjects ``X -> B`` that are monic."""

    def super_categories(self):
        return [CosliceCategory(self.base_category(), self.base_object())]

    def admits_arrow(self, arrow: Morphism) -> bool:
        return super().admits_arrow(arrow) and self.base_category().MonomorphismArrowCategory().admits_arrow(arrow)

    def _repr_(self) -> str:
        return f"Superobjects of {self.base_object()}"


class CoveringObjectCategory(SliceCategory):
    r"""The category of covering objects ``A -> X`` that are epic."""

    def super_categories(self):
        return [SliceCategory(self.base_category(), self.base_object())]

    def admits_arrow(self, arrow: Morphism) -> bool:
        return super().admits_arrow(arrow) and self.base_category().EpimorphismArrowCategory().admits_arrow(arrow)

    def _repr_(self) -> str:
        return f"Covering objects of {self.base_object()}"


class CoveredObjectCategory(CosliceCategory):
    r"""The category of covered objects ``X -> B`` that are epic."""

    def super_categories(self):
        return [CosliceCategory(self.base_category(), self.base_object())]

    def admits_arrow(self, arrow: Morphism) -> bool:
        return super().admits_arrow(arrow) and self.base_category().EpimorphismArrowCategory().admits_arrow(arrow)

    def _repr_(self) -> str:
        return f"Covered objects of {self.base_object()}"


class FixedWideMorCategory(FixedRestrictedMorCategory):
    r"""The selected arrows in one existing Mor of the underlying category."""

    def arrow_set(self) -> SageMor:
        return _category_mor_parent(
            self.base_category().base_category(),
            self.domain_object(),
            self.codomain_object(),
        )

    underlying_mor = arrow_set

    def super_categories(self) -> list[Category]:
        return [
            self.base_category().base_category().category_packet().Mors().Of(
                self.domain_object(),
                self.codomain_object(),
            )
        ]


class WideMorCategoryConstruction(_RestrictedMorCategoryOf):
    r"""Mor categories cut out by a wide subcategory's arrow predicate."""

    FixedCategoryClass = FixedWideMorCategory

    def _inherits_morphisms_from(
        self, supercategory: Category, domain: Parent, codomain: Parent
    ) -> bool:
        # The object sets agree, but the supplied predicate changes the arrows.
        # Sharing the underlying Mor does not make the inclusion full.
        return False

    def accepts(self, arrow: Morphism) -> bool:
        return self.base_category().admits(arrow)


class _WideSubcategory(OwnedCategoryBase):
    r"""A category with the same objects as ``C`` and a selected class of arrows.

    The selected arrows must include every identity and be closed under
    composition. These are hypotheses on the supplied mathematical class,
    not properties decidable by enumerating an arbitrary category.
    Each fixed Mor retains that class's predicate and the original arrow parent.

    Unverified specimens: injections form a wide subcategory of sets. A
    noninjective map is an underlying set map, but is not an arrow here::

        sage: from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
        sage: from dzack_research.preamble.categories.functors.core import IdentityFunctor, NaturalTransformation
        sage: from dzack_research.preamble.categories.sets.set_categories import Sets
        sage: points = finite_ordered_set(("a", "b"))
        sage: injections = Sets().WideSubcategory(Sets().MonomorphismArrowCategory())
        sage: maps = Sets().Mor(points, points)
        sage: Mor = injections.Mor(points, points)
        sage: Mor is injections.MorCategory().Of(points, points)
        True
        sage: points.Mor(points, category=injections) is Mor
        True
        sage: Mor.arrow_set() is maps
        True
        sage: swap = maps(lambda point: {"a": "b", "b": "a"}[point])
        sage: collapse = maps(lambda point: "a")
        sage: swap in Mor, collapse in maps, collapse in Mor
        (True, True, False)
        sage: Mor.object(swap).arrow() is swap
        True
        sage: injections.compose(swap, swap) == injections.identity(points)
        True
        sage: identity = IdentityFunctor(injections)
        sage: identity(swap) is swap
        True
        sage: identity(collapse)
        Traceback (most recent call last):
        ...
        TypeError: the supplied map is not a morphism of the functor's domain
        sage: eta = NaturalTransformation(identity, identity, lambda obj: collapse)
        sage: eta.component(points)
        Traceback (most recent call last):
        ...
        TypeError: the component is not a morphism of the common codomain category
        sage: arrows = injections.ArrowCategory()
        sage: obj = arrows(injections.identity(points))
        sage: arrows.Mor(obj, obj)(swap, swap).left() is swap
        True
        sage: arrows.Mor(obj, obj)(collapse, collapse)
        Traceback (most recent call last):
        ...
        ValueError: the left edge is not a morphism of the base category

    An underlying bijection still has to lie in the selected Mor; creating a
    runtime parent never replaces this admission check.
    """

    _MorCategory = WideMorCategoryConstruction

    @staticmethod
    @cached_function(key=lambda cls, base_category, arrow_category: (cls, id(base_category), id(arrow_category)))
    def __classcall__(cls, base_category: Category, arrow_category: _SubcategoryOfArrows):
        match cls:
            case DynamicMetaclass():
                return cls.__base__(base_category, arrow_category)
        return typecall(cls, base_category, arrow_category)

    def __init__(self, base_category: Category, arrow_category: _SubcategoryOfArrows) -> None:
        if arrow_category.base_category() != base_category:
            raise ValueError("the selected arrows must belong to the stated base category")
        self._base_category = base_category
        self._arrow_category = arrow_category
        super().__init__()

    def _make_named_class_key(self, name):
        return self._base_category, self._arrow_category

    def base_category(self) -> Category:
        return self._base_category

    def arrow_category(self) -> _SubcategoryOfArrows:
        return self._arrow_category

    def super_categories(self):
        return [self.base_category()]

    def __contains__(self, candidate: Any) -> bool:
        return candidate in self.base_category()

    def admits(self, arrow: Morphism) -> bool:
        r"""Whether ``arrow`` is one of the selected arrows."""
        return self.arrow_category().admits_arrow(arrow)

    def identity(self, obj: Parent) -> Morphism:
        identity = _category_mor_parent(self.base_category(), obj, obj).identity()
        if identity not in self.Mor(obj, obj):
            raise ValueError("the selected arrow class omits an identity")
        return identity

    def compose(self, second: Morphism, first: Morphism) -> Morphism:
        if first.codomain() is not second.domain():
            raise ValueError("the arrows are not composable")
        if first not in self.Mor(first.domain(), first.codomain()):
            raise ValueError("the first arrow is outside this wide subcategory")
        if second not in self.Mor(second.domain(), second.codomain()):
            raise ValueError("the second arrow is outside this wide subcategory")
        composite = second * first
        if composite not in self.Mor(first.domain(), second.codomain()):
            raise ValueError("the selected arrow class is not closed under this composition")
        return composite

    def _repr_(self) -> str:
        return f"Wide subcategory of {self.base_category()} with arrows in {self.arrow_category()}"


class CoreMor(CategoricalMor):
    Element = CategoricalIsomorphism

    def __init__(
        self,
        family: MorCategoryConstruction,
        domain: Parent,
        codomain: Parent,
    ) -> None:
        CategoricalMor.__init__(
            self, family, domain, codomain
        )

    def core_category(self) -> _CoreCategory:
        return self.base_category()

    def __contains__(self, candidate: Any) -> bool:
        r"""Whether ``candidate`` is an isomorphism between these objects.

        Only a represented isomorphism is an arrow of the core; it is one of
        these when its forward and inverse maps are arrows of the base category.
        """
        match candidate:
            case CategoricalIsomorphism() if (
                candidate.domain() is self.domain() and candidate.codomain() is self.codomain()
            ):
                base = self.core_category().base_category()
                return (
                    candidate.forward() in base.Mor(self.domain(), self.codomain())
                    and candidate.inverse() in base.Mor(self.codomain(), self.domain())
                )
            case _:
                return False

    def _element_constructor_(self, forward, inverse=None):
        match forward:
            case CategoricalIsomorphism() if inverse is None:
                if forward.parent() is self:
                    return forward
                if forward not in self:
                    raise ValueError("the isomorphism does not belong to this core Mor")
                return self._from_known_inverse_pair(forward.forward(), forward.inverse())
        if inverse is None:
            forward, inverse = forward
        self._require_base_morphisms(forward, inverse)
        return CategoricalIsomorphism(self, forward, inverse)

    def _require_base_morphisms(self, forward: Morphism, inverse: Morphism) -> None:
        base = self.core_category().base_category()
        if not _category_accepts_morphism(base, self.domain(), self.codomain(), forward):
            raise ValueError("the forward map is not a morphism of the core's base category")
        if not _category_accepts_morphism(base, self.codomain(), self.domain(), inverse):
            raise ValueError("the inverse map is not a morphism of the core's base category")

    def _from_known_inverse_pair(self, forward, inverse):
        r"""Construct an isomorphism from an inverse pair proved by its owner."""
        self._require_base_morphisms(forward, inverse)
        return CategoricalIsomorphism(self, forward, inverse, verify=False)

    def identity(self) -> CategoricalIsomorphism:
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on an endomorphism Mor object")
        base = self.core_category().base_category()
        identity = _category_mor_parent(base, self.domain(), self.domain()).identity()
        return self._from_known_inverse_pair(identity, identity)


class CoreMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = CoreMor


class _CoreCategory(OwnedCategoryBase):
    r"""The maximal subgroupoid (core) of a represented category."""

    _MorCategory = CoreMorCategoryConstruction

    def __init__(self, base_category: Category) -> None:
        self._base_category = base_category
        super().__init__()

    def _make_named_class_key(self, name):
        return self._base_category

    def base_category(self) -> Category:
        return self._base_category

    def Core(self) -> Category:
        r"""A core is already a groupoid, so taking its core changes nothing."""
        return self

    def super_categories(self):
        return [self.base_category()]

    def __contains__(self, candidate: Any) -> bool:
        r"""The core has the objects of its base category."""
        return candidate in self.base_category()

    def Mor(self, domain: Parent, codomain: Parent) -> CoreMor:
        if domain not in self or codomain not in self:
            raise TypeError("the core Mor requires two base-category objects")
        return self.MorCategory().Of(domain, codomain)

    def identity(self, obj: Parent) -> CategoricalIsomorphism:
        return self.Mor(obj, obj).identity()

    def _repr_(self) -> str:
        return f"Core of {self.base_category()}"


def _core_mor(
    domain: Parent,
    codomain: Parent,
    *,
    base_category: Category | None = None,
) -> CoreMor:
    r"""Return the core Mor in the stated arrow category.

    Endpoint categories can be joins carrying several independent structures
    whose morphism theories are intentionally not identified.  When an arrow
    already names its mathematical Mor owner, use that owner rather than
    reconstructing a Mor theory from the endpoints alone.
    """
    if base_category is None:
        category = Cat().join((domain.category(), codomain.category()))
    else:
        category = base_category
    return category.Core().Mor(domain, codomain)


def _represented_morphism_category(forward: Morphism, inverse: Morphism) -> Category | None:
    r"""Return the common category whose Mor categories hold both arrows, if they share one."""
    homs = (forward.parent(), inverse.parent())
    match homs:
        case (forward_mor, inverse_mor) if (
            forward_mor in MorCategories()
            and inverse_mor in MorCategories()
            and forward_mor.base_category() is inverse_mor.base_category()
        ):
            return forward_mor.base_category()
        case _:
            return None


def _isomorphism_from_known_inverse_pair(
    forward, inverse, *, base_category: Category | None = None
):
    r"""Transport a previously proved inverse pair in the selected arrow theory.

    An induced Aut functor supplies its target category: its image arrows may
    retain stronger parents, which must not choose a different target core.
    Without a selected target, use the pair's common represented Mor theory.
    The selected core still admits both arrows; this parameter changes their
    mathematical ambient category, not their admission obligations.
    """
    match base_category:
        case None:
            base_category = _represented_morphism_category(forward, inverse)
    return _core_mor(
        forward.domain(),
        forward.codomain(),
        base_category=base_category,
    )._from_known_inverse_pair(forward, inverse)


__all__ = [
    "ArrowMor",
    "CategoricalIsomorphism",
    "CommutativeSquare",
    "CoreMor",
    "CosliceCategory",
    "CoveredObjectCategory",
    "CoveringObjectCategory",
    "SliceCategory",
    "SubobjectCategory",
    "SetSubobjectCategory",
    "SubobjectMor",
    "SubobjectMorphism",
    "SuperobjectCategory",
]
