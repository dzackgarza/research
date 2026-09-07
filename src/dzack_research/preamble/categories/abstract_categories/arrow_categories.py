r"""Arrow categories, commuting squares, cores, and slice-style categories."""

from typing import Any

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    CategoricalIsomorphism,
    HomCategoryConstruction,
    _category_homset,
)
from sage.categories.category import Category
from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.classcall_metaclass import typecall
from sage.misc.unknown import Unknown, UnknownClass
from sage.categories.sets_cat import Sets as SageSets
from sage.structure.parent import Parent
from sage.structure.dynamic_class import DynamicMetaclass
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.owned_category import OwnedCategoryMixin, object_of
from dzack_research.preamble.categories.sets.set_categories import Sets



class CommutativeSquare(Morphism):
    r"""A morphism between two arrow objects, i.e. a commuting square."""

    def __init__(
        self,
        parent: "ArrowHomset",
        left: Morphism,
        right: Morphism,
        *,
        verify: bool = True,
    ) -> None:
        Morphism.__init__(self, parent)
        source = self.domain().arrow()
        target = self.codomain().arrow()
        if left.domain() is not source.domain() or left.codomain() is not target.domain():
            raise ValueError("the left edge has the wrong square endpoints")
        if right.domain() is not source.codomain() or right.codomain() is not target.codomain():
            raise ValueError("the right edge has the wrong square endpoints")
        base = parent.arrow_category().base_category()
        if left not in _category_homset(base, source.domain(), target.domain()):
            raise ValueError("the left edge is not a morphism of the base category")
        if right not in _category_homset(base, source.codomain(), target.codomain()):
            raise ValueError("the right edge is not a morphism of the base category")
        if verify and (right * source == target * left) is not True:
            raise ValueError("the supplied edges do not establish a commuting square")
        self._left = left
        self._right = right

    def left(self) -> Morphism:
        return self._left

    def right(self) -> Morphism:
        return self._right

    def components(self):
        return self.left(), self.right()

    def __eq__(self, other) -> bool | UnknownClass:
        r"""Two commuting squares agree when both of their edges do."""
        if not isinstance(other, CommutativeSquare):
            return False
        if self is other:
            return True
        if self.parent() is not other.parent():
            return False
        equalities = (self.left() == other.left(), self.right() == other.right())
        if any(answer is False for answer in equalities):
            return False
        return True if all(answer is True for answer in equalities) else Unknown

    def __ne__(self, other) -> bool | UnknownClass:
        equal = self == other
        return Unknown if equal is Unknown else not equal

    def __hash__(self) -> int:
        return hash(id(self.parent()))

    def __mul__(self, other):
        if not isinstance(other, CommutativeSquare) or other.codomain() is not self.domain():
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


class ArrowHomset(CategoricalHomset):
    Element = CommutativeSquare

    def __init__(
        self,
        family: HomCategoryConstruction,
        source: Parent,
        target: Parent,
    ) -> None:
        CategoricalHomset.__init__(
            self, family, source, target
        )

    def arrow_category(self) -> "ArrowCategory":
        return self.base_category()

    def _element_constructor_(self, left, right=None):
        if isinstance(left, CommutativeSquare) and right is None:
            if left.parent() is self:
                return left
            if left.domain() is not self.domain() or left.codomain() is not self.codomain():
                raise ValueError("the square has the wrong arrow objects")
            left, right = left.left(), left.right()
        if right is None:
            left, right = left
        return CommutativeSquare(self, left, right)

    def _from_commuting_edges(self, left: Morphism, right: Morphism) -> CommutativeSquare:
        r"""Construct edges whose commutativity follows from their construction."""
        return self.element_class(self, left, right, verify=False)

    def identity(self) -> CommutativeSquare:
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on an endomorphism Hom-set")
        arrow = self.domain().arrow()
        category = self.arrow_category().base_category()
        return self._from_commuting_edges(
            _category_homset(category, arrow.domain(), arrow.domain()).identity(),
            _category_homset(category, arrow.codomain(), arrow.codomain()).identity(),
        )

    def identity_at(self, obj: Parent) -> CommutativeSquare:
        return self.arrow_category().Mor(obj, obj).identity()


class ArrowHomCategoryConstruction(HomCategoryConstruction):
    FixedCategoryClass = ArrowHomset


class ArrowCategory(OwnedCategory):
    r"""The category ``Arr(C)=Fun([1],C)``."""

    _HomCategory = ArrowHomCategoryConstruction

    def an_object(self) -> Parent:
        r"""The identity of an object of the base category, as an arrow."""
        base = self.base_category()
        witness = base.an_object()
        return self.object(_category_homset(base, witness, witness).identity())

    class ParentMethods:
        r"""A morphism of ``C`` regarded as an object of ``Arr(C)``."""

        def __init__(self, arrow: Morphism, **rest) -> None:
            self._arrow = arrow
            super().__init__(**rest)

        def arrow_category(self) -> "ArrowCategory":
            return self.category()

        def arrow(self) -> Morphism:
            return self._arrow

        def source_object(self) -> Parent:
            return self.arrow().domain()

        def target_object(self) -> Parent:
            return self.arrow().codomain()

        def _repr_(self) -> str:
            return f"Arrow object ({self.source_object()} -> {self.target_object()})"

    def __init__(self, base_category: Category) -> None:
        self._base_category = base_category
        self._arrow_objects = {}
        super().__init__()

    def _make_named_class_key(self, name):
        return self._base_category

    def base_category(self) -> Category:
        return self._base_category

    def super_categories(self):

        return [Sets()]

    def __contains__(self, candidate: Any) -> bool:
        if not isinstance(candidate, Parent):
            return False
        if not candidate.category().is_subcategory(ArrowCategory(self.base_category())):
            return False
        return self._accepts_arrow(candidate.arrow())

    def _accepts_arrow(self, arrow: Morphism) -> bool:
        r"""Whether this category's object predicate accepts the supplied arrow."""
        base = self.base_category()
        if arrow.domain() not in base or arrow.codomain() not in base:
            return False
        return arrow in _category_homset(base, arrow.domain(), arrow.codomain())

    def object(self, arrow: Morphism) -> Parent:
        if not isinstance(arrow, Morphism):
            raise TypeError("an arrow object is constructed from a morphism")
        if not self._accepts_arrow(arrow):
            raise TypeError("the supplied morphism is not an object of this arrow category")
        key = id(arrow)
        cached = self._arrow_objects.get(key)
        if cached is not None and cached.arrow() is arrow:
            return cached
        result = object_of(self, arrow=arrow)
        self._arrow_objects[key] = result
        return result

    __call__ = object

    def Mor(self, source: Parent, target: Parent) -> ArrowHomset:
        if source not in self or target not in self:
            raise TypeError("an arrow-category Hom requires two arrow objects")
        return self.HomCategory().Of(source, target)


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

    def _repr_(self) -> str:
        return f"Arrow category of {self.base_category()}"


class _EndofunctorAlgebraHomset(ArrowHomset):
    r"""Morphisms ``f`` with ``f a = b T(f)`` between ``T``-algebras.

    The ambient arrow category stores the commuting square. Here its left
    edge is not another chosen datum: it is forced to be ``T(f)`` by the
    endofunctor. Thus one underlying arrow determines one structured
    morphism, exactly as in ``Inserter(T, Id)``.
    """

    class Element(CommutativeSquare):
        r"""A structured map acting through its exact carrier morphism."""

        def underlying_morphism(self) -> Morphism:
            return self.right()

        def _call_(self, element):
            return self.underlying_morphism()(element)

    def _element_constructor_(self, left, right=None):
        category = self.arrow_category()
        if isinstance(left, CommutativeSquare) and right is None:
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
        return self.element_class(self, left, right)


class _EndofunctorAlgebraForgetfulFunctor(Functor):
    r"""The carrier functor ``Alg(T) -> C``."""

    _faithful = True

    def __init__(self, algebras: "_EndofunctorAlgebraCategory") -> None:
        self._algebras = algebras
        super().__init__(algebras, algebras.base_category())

    def _apply_object(self, algebra: Parent) -> Parent:
        return algebra.target_object()

    def _apply_morphism(self, morphism: Map) -> Map:
        return morphism.right()

    def _repr_(self) -> str:
        return f"Carrier functor {self.domain()} -> {self.codomain()}"


class _EndofunctorAlgebraHomCategory(HomCategoryConstruction):
    FixedCategoryClass = _EndofunctorAlgebraHomset


class _EndofunctorAlgebraCategory(Category):
    r"""The category of algebras of an endofunctor ``T : C -> C``.

    An object is the exact arrow ``a : T(X) -> X`` in ``C``. The existing
    arrow-object construction retains that arrow without rebuilding either
    endpoint, while this category cuts its Hom-sets down from arbitrary
    commuting squares to the squares whose left edge is ``T(f)``. Hence its
    objects and morphisms are precisely those of ``Inserter(T, Id_C)``.
    """

    _HomCategory = _EndofunctorAlgebraHomCategory

    def __init__(self, endofunctor: Functor) -> None:
        if not isinstance(endofunctor, Functor):
            raise TypeError("an endofunctor algebra requires a represented functor")
        if endofunctor.domain() is not endofunctor.codomain():
            raise ValueError("an endofunctor must have one common domain and codomain")
        self._endofunctor = endofunctor
        self._arrow_category = ArrowCategory(endofunctor.domain())
        super().__init__()

    def _make_named_class_key(self, name):
        return self._endofunctor._cache_key()

    def endofunctor(self) -> Functor:
        return self._endofunctor

    def base_category(self) -> Category:
        return self.endofunctor().domain()

    def arrow_category(self) -> ArrowCategory:
        return self._arrow_category

    def super_categories(self):
        return [self.arrow_category()]

    def __contains__(self, candidate: Any) -> bool:
        if candidate not in self.arrow_category():
            return False
        carrier = candidate.target_object()
        return (
            carrier in self.base_category()
            and candidate.source_object() is self.endofunctor()(carrier)
        )

    def algebra(self, carrier: Parent, structure: Morphism) -> Parent:
        r"""Return ``(carrier, structure : T(carrier) -> carrier)``.

        Both the supplied carrier and the supplied structure arrow are kept
        literally. In particular two different structure arrows on one
        carrier produce two different algebra objects whose carrier functor
        returns that same carrier object.
        """
        if carrier not in self.base_category():
            raise TypeError("the carrier is not an object of the endofunctor's category")
        if structure.domain() is not self.endofunctor()(carrier):
            raise ValueError("the structure morphism must start at T(carrier)")
        if structure.codomain() is not carrier:
            raise ValueError("the structure morphism must end at its exact supplied carrier")
        return self.arrow_category()(structure)

    def carrier(self, algebra: Parent) -> Parent:
        if algebra not in self:
            raise TypeError("the object is not an algebra of this endofunctor")
        return algebra.target_object()

    def structure(self, algebra: Parent) -> Morphism:
        if algebra not in self:
            raise TypeError("the object is not an algebra of this endofunctor")
        return algebra.arrow()

    def Mor(
        self,
        source: Parent,
        target: Parent,
    ) -> _EndofunctorAlgebraHomset:
        if source not in self or target not in self:
            raise TypeError("an endofunctor-algebra Hom requires two algebras of this endofunctor")
        return self.HomCategory().Of(source, target)

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

    def identity(self, algebra: Parent) -> CommutativeSquare:
        return self.Mor(algebra, algebra).identity()

    def compose(
        self,
        second: CommutativeSquare,
        first: CommutativeSquare,
    ) -> CommutativeSquare:
        if first.codomain() is not second.domain():
            raise ValueError("endofunctor-algebra morphisms are not composable")
        return second * first

    def _repr_(self) -> str:
        return f"Algebras of {self.endofunctor()}"


@cached_function(key=lambda endofunctor: id(endofunctor))
def EndofunctorAlgebras(endofunctor: Functor) -> _EndofunctorAlgebraCategory:
    r"""Return ``Inserter(T, Id)``, represented by exact arrow objects."""
    return _EndofunctorAlgebraCategory(endofunctor)


class SliceHomset(ArrowHomset):
    r"""Morphisms in a slice; the edge at the fixed codomain is the identity."""

    def _element_constructor_(self, factor, right=None):
        if isinstance(factor, CommutativeSquare) and right is None:
            if factor.parent() is self:
                return factor
            if factor.domain() is not self.domain() or factor.codomain() is not self.codomain():
                raise ValueError("the slice morphism has the wrong endpoints")
            factor, right = factor.left(), factor.right()
        fixed = self.domain().arrow().codomain()
        if self.codomain().arrow().codomain() is not fixed:
            raise ValueError("slice objects require one fixed codomain")
        identity = _category_homset(self.arrow_category().base_category(), fixed, fixed).identity()
        if right is not None:
            if (right == identity) is not True:
                raise ValueError("the fixed edge of a slice morphism is the identity")
        return CommutativeSquare(self, factor, identity)

    def canonical_morphism(self) -> CommutativeSquare:
        inclusion = self.domain().arrow()
        target_inclusion = self.codomain().arrow()
        return self(inclusion.factor_through(target_inclusion))


class SliceHomCategoryConstruction(HomCategoryConstruction):
    FixedCategoryClass = SliceHomset


class SliceCategory(ArrowCategory):
    r"""The slice category \(C/X\).

    Unverified specimens retain equal-but-distinct base sets and keep the
    slice and coslice fixed edges under nonidentity composition::

        sage: from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
        sage: from dzack_research.preamble.categories.functors.core import IdentityFunctor
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
        sage: hom = slice_category.Mor(obj, obj)
        sage: hom is slice_category.HomCategory().Of(obj, obj)
        True
        sage: square = hom(swap)
        sage: square * square == hom.identity()
        True
        sage: coslice = CosliceCategory(Sets(), one)
        sage: obj = coslice(Sets().Mor(one, points)(lambda point: "a"))
        sage: hom = coslice.Mor(obj, obj)
        sage: collapse = hom(Sets().Mor(points, points)(lambda point: "a"))
        sage: collapse * collapse == collapse
        True
        sage: hom.identity() * collapse == collapse
        True
        sage: algebras = EndofunctorAlgebras(IdentityFunctor(Sets()))
        sage: algebra = algebras.algebra(points, swap)
        sage: hom = algebras.Mor(algebra, algebra)
        sage: hom is algebras.HomCategory().Of(algebra, algebra)
        True
        sage: hom(swap) * hom(swap) == hom.identity()
        True
    """

    _HomCategory = SliceHomCategoryConstruction

    @staticmethod
    @cached_function(key=lambda cls, base_category, base_object: (cls, id(base_category), id(base_object)))
    def __classcall__(cls, base_category: Category, base_object: Parent):
        if isinstance(cls, DynamicMetaclass):
            return cls.__base__(base_category, base_object)
        return typecall(cls, base_category, base_object)

    def super_categories(self):
        return [ArrowCategory(self.base_category())]

    def __init__(self, base_category: Category, base_object: Parent) -> None:
        if base_object not in base_category:
            raise TypeError("the slice base must be an object of its base category")
        self._base_object = base_object
        super().__init__(base_category)

    def _make_named_class_key(self, name):
        return self.base_category(), id(self._base_object)

    def base_object(self) -> Parent:
        return self._base_object

    def an_object(self) -> Parent:
        r"""The identity of the fixed base object."""
        base_object = self.base_object()
        return self.object(
            _category_homset(self.base_category(), base_object, base_object).identity()
        )

    def _accepts_arrow(self, arrow: Morphism) -> bool:
        return arrow.codomain() is self.base_object() and super()._accepts_arrow(arrow)

    def Mor(self, source: Parent, target: Parent) -> SliceHomset:
        if source not in self or target not in self:
            raise TypeError("a slice Hom requires two arrows into the fixed base object")
        return self.HomCategory().Of(source, target)


    def _repr_(self) -> str:
        return f"Slice category {self.base_category()}/{self.base_object()}"


class CosliceHomset(ArrowHomset):
    r"""Morphisms in a coslice; the edge at the fixed domain is the identity."""

    def _element_constructor_(self, left, right=None):
        if isinstance(left, CommutativeSquare) and right is None:
            if left.parent() is self:
                return left
            if left.domain() is not self.domain() or left.codomain() is not self.codomain():
                raise ValueError("the coslice morphism has the wrong endpoints")
            left, right = left.left(), left.right()
        fixed = self.domain().arrow().domain()
        if self.codomain().arrow().domain() is not fixed:
            raise ValueError("coslice objects require one fixed domain")
        identity = _category_homset(self.arrow_category().base_category(), fixed, fixed).identity()
        if right is None:
            right = left
        elif (left == identity) is not True:
            raise ValueError("the fixed edge of a coslice morphism is the identity")
        return CommutativeSquare(self, identity, right)

    def identity(self) -> CommutativeSquare:
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on an endomorphism Hom-set")
        target = self.domain().target_object()
        source = self.domain().source_object()
        category = self.arrow_category().base_category()
        return self._from_commuting_edges(
            _category_homset(category, source, source).identity(),
            _category_homset(category, target, target).identity(),
        )


class CosliceHomCategoryConstruction(HomCategoryConstruction):
    FixedCategoryClass = CosliceHomset


class CosliceCategory(ArrowCategory):
    r"""The coslice category \(X/C\)."""

    _HomCategory = CosliceHomCategoryConstruction

    @staticmethod
    @cached_function(key=lambda cls, base_category, base_object: (cls, id(base_category), id(base_object)))
    def __classcall__(cls, base_category: Category, base_object: Parent):
        if isinstance(cls, DynamicMetaclass):
            return cls.__base__(base_category, base_object)
        return typecall(cls, base_category, base_object)

    def super_categories(self):
        return [ArrowCategory(self.base_category())]

    def __init__(self, base_category: Category, base_object: Parent) -> None:
        if base_object not in base_category:
            raise TypeError("the coslice base must be an object of its base category")
        self._base_object = base_object
        super().__init__(base_category)

    def _make_named_class_key(self, name):
        return self.base_category(), id(self._base_object)

    def base_object(self) -> Parent:
        return self._base_object

    def an_object(self) -> Parent:
        r"""The identity of the fixed base object."""
        base_object = self.base_object()
        return self.object(
            _category_homset(self.base_category(), base_object, base_object).identity()
        )

    def _accepts_arrow(self, arrow: Morphism) -> bool:
        return arrow.domain() is self.base_object() and super()._accepts_arrow(arrow)

    def Mor(self, source: Parent, target: Parent) -> CosliceHomset:
        if source not in self or target not in self:
            raise TypeError("a coslice Hom requires two arrows from the fixed base object")
        return self.HomCategory().Of(source, target)


    def _repr_(self) -> str:
        return f"Coslice category {self.base_object()}/{self.base_category()}"


def common_category(*objects: Parent) -> Category:
    r"""Return the greatest Sage category common to the stated objects."""
    if not objects:
        raise ValueError("a common category requires at least one object")
    return Category.meet([obj.category() for obj in objects])


class EndArrowCategory(ArrowCategory):
    r"""The full subcategory of ``Arr(C)`` on endomorphisms."""

    def super_categories(self):
        return [ArrowCategory(self.base_category())]

    def _accepts_arrow(self, arrow: Morphism) -> bool:
        return arrow.domain() is arrow.codomain() and super()._accepts_arrow(arrow)


class IsoArrowCategory(ArrowCategory):
    r"""The full subcategory of ``Arr(C)`` on explicitly represented isomorphisms."""

    def super_categories(self):
        return [ArrowCategory(self.base_category())]

    def _accepts_arrow(self, arrow: Morphism) -> bool:
        return isinstance(arrow, CategoricalIsomorphism) and super()._accepts_arrow(arrow)


class AutomorphismArrowCategory(IsoArrowCategory):
    r"""The full subcategory of the arrow category on automorphisms."""

    def super_categories(self):
        return [IsoArrowCategory(self.base_category()), EndArrowCategory(self.base_category())]

    def _accepts_arrow(self, arrow: Morphism) -> bool:
        return arrow.domain() is arrow.codomain() and super()._accepts_arrow(arrow)


class MonomorphismArrowCategory(ArrowCategory):
    r"""The full subcategory of the arrow category on represented monomorphisms.

    Which arrows are monic is the base category's own question, so this asks
    the mono family that category declares.  Injectivity is the answer in sets
    and modules and is the declared default there; it is neither necessary nor
    sufficient in every category, so it is not the definition used here.
    """

    def super_categories(self):
        return [ArrowCategory(self.base_category())]

    def _accepts_arrow(self, arrow: Morphism) -> bool:
        if not super()._accepts_arrow(arrow):
            return False
        from dzack_research.preamble.categories.abstract_categories.hom_categories import (
            category_packet,
        )

        return category_packet(self.base_category()).Monos().accepts(arrow)


class EpimorphismArrowCategory(ArrowCategory):
    r"""The full subcategory of the arrow category on represented epimorphisms.

    As for monomorphisms, the base category's declared epi family answers.
    """

    def super_categories(self):
        return [ArrowCategory(self.base_category())]

    def _accepts_arrow(self, arrow: Morphism) -> bool:
        if not super()._accepts_arrow(arrow):
            return False
        from dzack_research.preamble.categories.abstract_categories.hom_categories import (
            category_packet,
        )

        return category_packet(self.base_category()).Epis().accepts(arrow)


def _subobject_source(subobject):
    inclusion = subobject.inclusion()
    return inclusion.domain() if inclusion is subobject else subobject


class SubobjectMorphism(Morphism):
    r"""The unique commuting-triangle map between two represented subobjects."""

    def __init__(
        self,
        parent: "SubobjectHomset",
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
        if factor_morphism not in _category_homset(
            base, _subobject_source(self.domain()), _subobject_source(self.codomain())
        ):
            raise ValueError("the subobject factor is not a morphism of the base category")
        if verify:
            left = self.codomain().inclusion() * factor_morphism
            right = self.domain().inclusion()
            if (left == right) is not True:
                raise ValueError("the supplied factor does not establish the subobject triangle")
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
        return isinstance(other, SubobjectMorphism) and other.parent() is self.parent()

    def __ne__(self, other: Any) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(id(self.parent()))

    def __mul__(self, other):
        if not isinstance(other, SubobjectMorphism) or other.codomain() is not self.domain():
            return NotImplemented
        parent = self.parent().subobject_category().Mor(
            other.domain(), self.codomain()
        )
        # If j f = i and k g = j, then k (g f) = i.
        return SubobjectMorphism(
            parent, self.factor_morphism() * other.factor_morphism(), verify=False
        )


class SubobjectHomset(CategoricalHomset):
    Element = SubobjectMorphism

    def __init__(
        self,
        family: HomCategoryConstruction,
        domain: Parent,
        codomain: Parent,
    ) -> None:
        CategoricalHomset.__init__(
            self, family, domain, codomain
        )

    def subobject_category(self) -> "SubobjectCategory":
        return self.base_category()

    def _canonical_factor(self):
        return self.domain().inclusion().factor_through(self.codomain().inclusion())

    def has_morphism(self) -> bool:
        try:
            self._canonical_factor()
        except (TypeError, ValueError):
            return False
        return True

    def canonical_morphism(self) -> SubobjectMorphism:
        return SubobjectMorphism(self, self._canonical_factor(), verify=False)

    def _element_constructor_(self, factor_morphism=None):
        if isinstance(factor_morphism, SubobjectMorphism):
            if factor_morphism.parent() is self:
                return factor_morphism
            if factor_morphism.domain() is not self.domain() or factor_morphism.codomain() is not self.codomain():
                raise ValueError("the subobject morphism has the wrong endpoints")
            factor_morphism = factor_morphism.factor_morphism()
        if factor_morphism is None:
            return self.canonical_morphism()
        return SubobjectMorphism(self, factor_morphism)

    def identity(self) -> SubobjectMorphism:
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on an endomorphism Hom-set")
        source = _subobject_source(self.domain())
        base = self.subobject_category().base_category()
        return SubobjectMorphism(
            self, _category_homset(base, source, source).identity(), verify=False
        )


class SubobjectHomCategoryConstruction(HomCategoryConstruction):
    FixedCategoryClass = SubobjectHomset


class SubobjectCategory(OwnedCategoryMixin, Category):
    r"""The category of represented subobjects of one fixed object.

    An object is an object ``A`` of the base category equipped with its chosen
    monomorphism ``A.inclusion(): A -> X``.  Morphisms are the commuting
    triangles between those inclusions.

    Unverified specimen: a represented module subobject retains its selected
    inclusion when its fixed-base placement and its Hom are requested::

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
        sage: hom = category.Mor(submodule, submodule)
        sage: hom is category.HomCategory().Of(submodule, submodule)
        True
        sage: identity = hom.identity()
        sage: identity * identity == identity
        True
        sage: submodule.inclusion() is inclusion
        True
    """

    _HomCategory = SubobjectHomCategoryConstruction

    @staticmethod
    @cached_function(key=lambda cls, base_category, base_object: (cls, id(base_category), id(base_object)))
    def __classcall__(cls, base_category: Category, base_object: Parent):
        if isinstance(cls, DynamicMetaclass):
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

        What the subobject additionally carries is its chosen monomorphism into
        the fixed base object; forgetting that leaves an object of the base
        category, with every operation the base category owns.
        """
        return [self.base_category()]

    def slice_category(self) -> SliceCategory:
        r"""Return the ambient slice ``C/X`` in which subobjects are monomorphisms."""
        return SliceCategory(self.base_category(), self.base_object())

    def monomorphism_category(self) -> MonomorphismArrowCategory:
        r"""Return the monomorphism subcategory of the ambient arrow category."""
        return MonomorphismArrowCategory(self.base_category())

    def as_slice_object(self, subobject: Parent) -> Parent:
        if subobject not in self:
            raise TypeError("the object is not a represented subobject of the fixed base")
        return self.slice_category()(subobject.inclusion())

    def __contains__(self, candidate: Any) -> bool:
        # The constructor/refinement already owns a declared placement.
        # Rebuilding its inclusion here can ask for a Hom whose endpoint
        # membership is this very question; the category graph needs no arrow
        # construction to recognize an object already placed in it.
        if Category.__contains__(self, candidate):
            return True
        try:
            inclusion = candidate.inclusion()
        except AttributeError:
            return False
        represented_source = inclusion is candidate or inclusion.domain() is candidate
        if not represented_source or inclusion.codomain() is not self.base_object():
            return False
        try:
            slice_object = self.slice_category()(inclusion)
        except (TypeError, ValueError):
            return False
        return slice_object in self.monomorphism_category()

    def Mor(self, domain: Parent, codomain: Parent) -> SubobjectHomset:
        if domain not in self or codomain not in self:
            raise TypeError("both objects must be subobjects of the fixed base object")
        return self.HomCategory().Of(domain, codomain)


    def leq(self, left: Parent, right: Parent) -> bool:
        return self.Mor(left, right).has_morphism()

    def identity(self, subobject: Parent) -> SubobjectMorphism:
        return self.Mor(subobject, subobject).identity()

    def _repr_(self) -> str:
        return f"Subobjects of {self.base_object()}"


class SuperobjectCategory(CosliceCategory):
    r"""The category of represented quotient/superobjects of one object."""

    def super_categories(self):
        return [CosliceCategory(self.base_category(), self.base_object())]

    def _accepts_arrow(self, arrow: Morphism) -> bool:
        return super()._accepts_arrow(arrow) and EpimorphismArrowCategory(self.base_category())._accepts_arrow(arrow)

    def _repr_(self) -> str:
        return f"Superobjects of {self.base_object()}"


class WideSubcategory(Category):
    r"""A category with the same objects as ``C`` and a selected class of arrows."""

    def __init__(self, base_category: Category, arrow_category: ArrowCategory) -> None:
        if arrow_category.base_category() != base_category:
            raise ValueError("the selected arrows must belong to the stated base category")
        self._base_category = base_category
        self._arrow_category = arrow_category
        super().__init__()

    def _make_named_class_key(self, name):
        return self._base_category, self._arrow_category

    def base_category(self) -> Category:
        return self._base_category

    def arrow_category(self) -> ArrowCategory:
        return self._arrow_category

    def super_categories(self):
        return [self.base_category()]

    def __contains__(self, candidate: Any) -> bool:
        return candidate in self.base_category()

    def admits(self, arrow: Morphism) -> bool:
        try:
            arrow_object = self.arrow_category()(arrow)
        except (TypeError, ValueError):
            return False
        return arrow_object in self.arrow_category()

    def _repr_(self) -> str:
        return f"Wide subcategory of {self.base_category()} with arrows in {self.arrow_category()}"


class CoreHomset(CategoricalHomset):
    Element = CategoricalIsomorphism

    def __init__(
        self,
        family: HomCategoryConstruction,
        domain: Parent,
        codomain: Parent,
    ) -> None:
        CategoricalHomset.__init__(
            self, family, domain, codomain
        )

    def core_category(self) -> "CoreCategory":
        return self.base_category()

    def __contains__(self, candidate: Any) -> bool:
        if not isinstance(candidate, CategoricalIsomorphism):
            return False
        if candidate.domain() is not self.domain() or candidate.codomain() is not self.codomain():
            return False
        base = self.core_category().base_category()
        return (
            candidate.forward() in base.Mor(self.domain(), self.codomain())
            and candidate.inverse() in base.Mor(self.codomain(), self.domain())
        )

    def _element_constructor_(self, forward, inverse=None):
        if isinstance(forward, CategoricalIsomorphism) and inverse is None:
            if forward.parent() is self:
                return forward
            if forward not in self:
                raise ValueError("the isomorphism does not belong to this core Hom")
            return self._from_known_inverse_pair(forward.forward(), forward.inverse())
        if inverse is None:
            forward, inverse = forward
        self._require_base_morphisms(forward, inverse)
        return CategoricalIsomorphism(self, forward, inverse)

    def _require_base_morphisms(self, forward: Morphism, inverse: Morphism) -> None:
        base = self.core_category().base_category()
        if forward not in _category_homset(base, self.domain(), self.codomain()):
            raise ValueError("the forward map is not a morphism of the core's base category")
        if inverse not in _category_homset(base, self.codomain(), self.domain()):
            raise ValueError("the inverse map is not a morphism of the core's base category")

    def _from_known_inverse_pair(self, forward, inverse):
        r"""Construct an isomorphism from an inverse pair proved by its owner."""
        self._require_base_morphisms(forward, inverse)
        return CategoricalIsomorphism(self, forward, inverse, verify=False)

    def identity(self) -> CategoricalIsomorphism:
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on an endomorphism Hom-set")
        base = self.core_category().base_category()
        identity = _category_homset(base, self.domain(), self.domain()).identity()
        return self._from_known_inverse_pair(identity, identity)


class CoreHomCategoryConstruction(HomCategoryConstruction):
    FixedCategoryClass = CoreHomset


class CoreCategory(Category):
    r"""The maximal subgroupoid (core) of a represented category."""

    _HomCategory = CoreHomCategoryConstruction

    def __init__(self, base_category: Category) -> None:
        self._base_category = base_category
        super().__init__()

    def _make_named_class_key(self, name):
        return self._base_category

    def base_category(self) -> Category:
        return self._base_category

    def super_categories(self):
        return [self.base_category()]

    def __contains__(self, candidate: Any) -> bool:
        return candidate in self.base_category()

    def Mor(self, domain: Parent, codomain: Parent) -> CoreHomset:
        if domain not in self or codomain not in self:
            raise TypeError("the core Hom requires two base-category objects")
        return self.HomCategory().Of(domain, codomain)


    def identity(self, obj: Parent) -> CategoricalIsomorphism:
        return self.Mor(obj, obj).identity()

    def _repr_(self) -> str:
        return f"Core of {self.base_category()}"


def Core(base_category: Category) -> CoreCategory:
    return CoreCategory(base_category)


def SliceOver(base_category: Category, base_object: Parent) -> SliceCategory:
    return SliceCategory(base_category, base_object)


def CosliceUnder(base_category: Category, base_object: Parent) -> CosliceCategory:
    return CosliceCategory(base_category, base_object)


def SubobjectsOf(
    base_category: Category,
    base_object: Parent,
) -> SubobjectCategory:
    return SubobjectCategory(base_category, base_object)


def SuperobjectsOf(
    base_category: Category,
    base_object: Parent,
) -> SuperobjectCategory:
    return SuperobjectCategory(base_category, base_object)


def core_mor(domain: Parent, codomain: Parent) -> CoreHomset:
    r"""Return ``Hom`` in the core of the greatest category holding both objects."""
    return Core(common_category(domain, codomain)).Mor(domain, codomain)


def _isomorphism_from_known_inverse_pair(forward, inverse):
    r"""Transport a previously proved inverse pair without re-solving equality."""
    return core_mor(forward.domain(), forward.codomain())._from_known_inverse_pair(
        forward, inverse
    )


def Isomorphism(
    forward: Morphism,
    inverse: Morphism,
) -> CategoricalIsomorphism:
    r"""Return the isomorphism represented by mutually inverse arrows."""
    return core_mor(forward.domain(), forward.codomain())(forward, inverse)


__all__ = [
    "common_category",
    "core_mor",
    "Isomorphism",
    "IsoArrowCategory",
    "EndArrowCategory",
    "EndofunctorAlgebras",
    "AutomorphismArrowCategory",
    "ArrowCategory",
    "ArrowHomset",
    "CategoricalIsomorphism",
    "CommutativeSquare",
    "Core",
    "CoreCategory",
    "CoreHomset",
    "CosliceCategory",
    "CosliceUnder",
    "EpimorphismArrowCategory",
    "MonomorphismArrowCategory",
    "SliceCategory",
    "SliceOver",
    "SubobjectCategory",
    "SubobjectHomset",
    "SubobjectMorphism",
    "SubobjectsOf",
    "SuperobjectCategory",
    "SuperobjectsOf",
    "WideSubcategory",
]
