r"""Arrow categories, commuting squares, cores, and slice-style categories."""

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    CategoricalIsomorphism,
    HomCategoryConstruction,
)
from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.categories.sets_cat import Sets as SageSets
from sage.structure.parent import Parent
from dzack_research.preamble.categories.sets.set_categories import Sets


class ArrowObject(Parent):
    r"""A morphism of ``C`` regarded as an object of ``Arr(C)``."""

    def __init__(self, arrow_category, arrow) -> None:
        self._arrow_category = arrow_category
        self._arrow = arrow
        Parent.__init__(self, category=SageSets())

    def arrow_category(self):
        return self._arrow_category

    def arrow(self):
        return self._arrow

    def source_object(self):
        return self.arrow().domain()

    def target_object(self):
        return self.arrow().codomain()

    def _repr_(self) -> str:
        return f"Arrow object ({self.source_object()} -> {self.target_object()})"


class CommutativeSquare(Morphism):
    r"""A morphism between two arrow objects, i.e. a commuting square."""

    def __init__(self, parent, left, right) -> None:
        Morphism.__init__(self, parent)
        source = self.domain().arrow()
        target = self.codomain().arrow()
        if left.domain() is not source.domain() or left.codomain() is not target.domain():
            raise ValueError("the left edge has the wrong square endpoints")
        if right.domain() is not source.codomain() or right.codomain() is not target.codomain():
            raise ValueError("the right edge has the wrong square endpoints")
        if right * source != target * left:
            raise ValueError("the square does not commute")
        self._left = left
        self._right = right

    def left(self):
        return self._left

    def right(self):
        return self._right

    def components(self):
        return self.left(), self.right()

    def __eq__(self, other) -> bool:
        r"""Two commuting squares agree when both of their edges do."""
        if not isinstance(other, CommutativeSquare):
            return False
        if self is other:
            return True
        if self.parent() is not other.parent():
            return False
        return self.left() == other.left() and self.right() == other.right()

    def __ne__(self, other) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash((id(self.parent()), id(self.left()), id(self.right())))

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        category = self.parent().arrow_category()
        return category.Mor(other.domain(), self.codomain())(
            self.left() * other.left(),
            self.right() * other.right(),
        )

    def _repr_(self) -> str:
        return f"Commutative square from {self.domain()} to {self.codomain()}"


class ArrowHomset(CategoricalHomset):
    Element = CommutativeSquare

    def __init__(self, arrow_category, source, target) -> None:
        self._arrow_category = arrow_category
        CategoricalHomset.__init__(
            self, HomCategoryConstruction(arrow_category), source, target
        )

    def arrow_category(self):
        return self._arrow_category

    def _element_constructor_(self, left, right=None):
        if right is None:
            left, right = left
        return CommutativeSquare(self, left, right)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on an endomorphism Hom-set")
        arrow = self.domain().arrow()
        category = self.arrow_category().base_category()
        return self(
            category.Mor(arrow.domain(), arrow.domain()).identity(),
            category.Mor(arrow.codomain(), arrow.codomain()).identity(),
        )

    def identity_at(self, obj):
        return self.arrow_category().Mor(obj, obj).identity()


class ArrowCategory(Category):
    r"""The category ``Arr(C)=Fun([1],C)``."""

    def __init__(self, base_category) -> None:
        self._base_category = base_category
        self._arrow_objects = {}
        self._homsets = {}
        super().__init__()

    def _make_named_class_key(self, name):
        return self._base_category

    def base_category(self):
        return self._base_category

    def super_categories(self):

        return [Sets()]

    def __contains__(self, candidate) -> bool:
        return (
            isinstance(candidate, ArrowObject)
            and candidate.arrow_category().base_category() == self.base_category()
        )

    def object(self, arrow):
        if not isinstance(arrow, Morphism):
            raise TypeError("an arrow object is constructed from a morphism")
        if arrow.domain() not in self.base_category() or arrow.codomain() not in self.base_category():
            raise TypeError("the morphism endpoints lie outside the base category")
        key = id(arrow)
        cached = self._arrow_objects.get(key)
        if cached is not None and cached.arrow() is arrow:
            return cached
        result = ArrowObject(self, arrow)
        self._arrow_objects[key] = result
        return result

    __call__ = object

    def _homset(self, homset_class, source, target):
        key = (homset_class, id(source), id(target))
        cached = self._homsets.get(key)
        if cached is not None and cached.domain() is source and cached.codomain() is target:
            return cached
        result = homset_class(self, source, target)
        self._homsets[key] = result
        return result

    def Mor(self, source, target):
        if source not in self or target not in self:
            raise TypeError("an arrow-category Hom requires two arrow objects")
        return self._homset(ArrowHomset, source, target)


    def morphism(self, source, target, left, right):
        return self.Mor(source, target)(left, right)

    def identity(self, arrow_object):
        return self.Mor(arrow_object, arrow_object).identity()

    def compose(self, second, first):
        if first.codomain() is not second.domain():
            raise ValueError("arrow-category squares are not composable")
        return second * first

    def _repr_(self) -> str:
        return f"Arrow category of {self.base_category()}"


class SliceHomset(ArrowHomset):
    r"""Morphisms in a slice; the edge at the fixed codomain is the identity."""

    def _element_constructor_(self, factor, right=None):
        fixed = self.domain().arrow().codomain()
        if self.codomain().arrow().codomain() is not fixed:
            raise ValueError("slice objects require one fixed codomain")
        identity = self.arrow_category().base_category().Mor(fixed, fixed).identity()
        if right is not None:
            if right != identity:
                raise ValueError("the fixed edge of a slice morphism is the identity")
        return CommutativeSquare(self, factor, identity)

    def canonical_morphism(self):
        inclusion = self.domain()
        target_inclusion = self.codomain()
        return self(inclusion.factor_through(target_inclusion))


class SliceCategory(ArrowCategory):
    r"""The slice category \(C/X\)."""

    def __init__(self, base_category, base_object) -> None:
        if base_object not in base_category:
            raise TypeError("the slice base must be an object of its base category")
        self._base_object = base_object
        super().__init__(base_category)

    def _make_named_class_key(self, name):
        return self.base_category(), self._base_object

    def base_object(self):
        return self._base_object

    def __contains__(self, candidate) -> bool:
        return super().__contains__(candidate) and candidate.arrow().codomain() is self.base_object()

    def Mor(self, source, target):
        if source not in self or target not in self:
            raise TypeError("a slice Hom requires two arrows into the fixed base object")
        return self._homset(SliceHomset, source, target)


    def _repr_(self) -> str:
        return f"Slice category {self.base_category()}/{self.base_object()}"


class CosliceHomset(ArrowHomset):
    r"""Morphisms in a coslice; the edge at the fixed domain is the identity."""

    def _element_constructor_(self, factor, left=None):
        fixed = self.domain().arrow().domain()
        if self.codomain().arrow().domain() is not fixed:
            raise ValueError("coslice objects require one fixed domain")
        identity = self.arrow_category().base_category().Mor(fixed, fixed).identity()
        if left is not None:
            if left != identity:
                raise ValueError("the fixed edge of a coslice morphism is the identity")
        return CommutativeSquare(self, identity, factor)


class CosliceCategory(ArrowCategory):
    r"""The coslice category \(X/C\)."""

    def __init__(self, base_category, base_object) -> None:
        if base_object not in base_category:
            raise TypeError("the coslice base must be an object of its base category")
        self._base_object = base_object
        super().__init__(base_category)

    def _make_named_class_key(self, name):
        return self.base_category(), self._base_object

    def base_object(self):
        return self._base_object

    def __contains__(self, candidate) -> bool:
        return super().__contains__(candidate) and candidate.arrow().domain() is self.base_object()

    def Mor(self, source, target):
        if source not in self or target not in self:
            raise TypeError("a coslice Hom requires two arrows from the fixed base object")
        return self._homset(CosliceHomset, source, target)


    def _repr_(self) -> str:
        return f"Coslice category {self.base_object()}/{self.base_category()}"


def common_category(*objects):
    r"""Return the greatest Sage category common to the stated objects."""
    if not objects:
        raise ValueError("a common category requires at least one object")
    return Category.meet([obj.category() for obj in objects])


class EndArrowCategory(ArrowCategory):
    r"""The full subcategory of ``Arr(C)`` on endomorphisms."""

    def __contains__(self, candidate) -> bool:
        return super().__contains__(candidate) and (
            candidate.arrow().domain() is candidate.arrow().codomain()
        )


class IsoArrowCategory(ArrowCategory):
    r"""The full subcategory of ``Arr(C)`` on explicitly represented isomorphisms."""

    def __contains__(self, candidate) -> bool:
        return super().__contains__(candidate) and isinstance(
            candidate.arrow(), CategoricalIsomorphism
        )


class AutomorphismArrowCategory(IsoArrowCategory):
    r"""The full subcategory of the arrow category on automorphisms."""

    def __contains__(self, candidate) -> bool:
        return super().__contains__(candidate) and (
            candidate.arrow().domain() is candidate.arrow().codomain()
        )


class MonomorphismArrowCategory(ArrowCategory):
    r"""The full subcategory of the arrow category on represented monomorphisms.

    Which arrows are monic is the base category's own question, so this asks
    the mono family that category declares.  Injectivity is the answer in sets
    and modules and is the declared default there; it is neither necessary nor
    sufficient in every category, so it is not the definition used here.
    """

    def __contains__(self, candidate) -> bool:
        if not super().__contains__(candidate):
            return False
        from dzack_research.preamble.categories.abstract_categories.hom_categories import (
            category_packet,
        )

        return category_packet(self.base_category()).Monos().accepts(candidate.arrow())


class EpimorphismArrowCategory(ArrowCategory):
    r"""The full subcategory of the arrow category on represented epimorphisms.

    As for monomorphisms, the base category's declared epi family answers.
    """

    def __contains__(self, candidate) -> bool:
        if not super().__contains__(candidate):
            return False
        from dzack_research.preamble.categories.abstract_categories.hom_categories import (
            category_packet,
        )

        return category_packet(self.base_category()).Epis().accepts(candidate.arrow())


def _subobject_source(subobject):
    inclusion = subobject.inclusion()
    return inclusion.domain() if inclusion is subobject else subobject


class SubobjectMorphism(Morphism):
    r"""The unique commuting-triangle map between two represented subobjects."""

    def __init__(self, parent, factor_morphism) -> None:
        Morphism.__init__(self, parent)
        if factor_morphism.domain() is not _subobject_source(self.domain()):
            raise ValueError("the subobject factor has the wrong domain")
        if factor_morphism.codomain() is not _subobject_source(self.codomain()):
            raise ValueError("the subobject factor has the wrong codomain")
        left = self.codomain().inclusion() * factor_morphism
        right = self.domain().inclusion()
        if left != right:
            raise ValueError("the subobject factor does not commute with the inclusions")
        self._factor_morphism = factor_morphism

    def factor_morphism(self):
        return self._factor_morphism

    def __call__(self, element):
        return self.factor_morphism()(element)

    def _call_(self, element):
        return self.factor_morphism()(element)

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        return self.parent().subobject_category().Mor(
            other.domain(), self.codomain()
        )(self.factor_morphism() * other.factor_morphism())


class SubobjectHomset(CategoricalHomset):
    Element = SubobjectMorphism

    def __init__(self, subobject_category, domain, codomain) -> None:
        self._subobject_category = subobject_category
        CategoricalHomset.__init__(
            self, HomCategoryConstruction(subobject_category), domain, codomain
        )

    def subobject_category(self):
        return self._subobject_category

    def _canonical_factor(self):
        return self.domain().inclusion().factor_through(self.codomain().inclusion())

    def has_morphism(self) -> bool:
        try:
            self._canonical_factor()
        except (TypeError, ValueError):
            return False
        return True

    def canonical_morphism(self):
        return self(self._canonical_factor())

    def _element_constructor_(self, factor_morphism=None):
        if factor_morphism is None:
            factor_morphism = self._canonical_factor()
        return SubobjectMorphism(self, factor_morphism)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on an endomorphism Hom-set")
        return self(self.domain().inclusion().factor_through(self.domain().inclusion()))


class SubobjectCategory(Category):
    r"""The category of represented subobjects of one fixed object.

    An object is an object ``A`` of the base category equipped with its chosen
    monomorphism ``A.inclusion(): A -> X``.  Morphisms are the commuting
    triangles between those inclusions.
    """

    def __init__(self, base_category, base_object) -> None:
        if base_object not in base_category:
            raise TypeError("the subobject base must lie in its base category")
        self._base_category = base_category
        self._base_object = base_object
        self._homsets = {}
        super().__init__()

    def _make_named_class_key(self, name):
        return self._base_category, self._base_object

    def base_category(self):
        return self._base_category

    def base_object(self):
        return self._base_object

    def super_categories(self):

        return [Sets()]

    def slice_category(self):
        r"""Return the ambient slice ``C/X`` in which subobjects are monomorphisms."""
        return SliceCategory(self.base_category(), self.base_object())

    def monomorphism_category(self):
        r"""Return the monomorphism subcategory of the ambient arrow category."""
        return MonomorphismArrowCategory(self.base_category())

    def as_slice_object(self, subobject):
        if subobject not in self:
            raise TypeError("the object is not a represented subobject of the fixed base")
        return self.slice_category()(subobject.inclusion())

    def __contains__(self, candidate) -> bool:
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

    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("both objects must be subobjects of the fixed base object")
        key = (id(domain), id(codomain))
        cached = self._homsets.get(key)
        if cached is not None and cached.domain() is domain and cached.codomain() is codomain:
            return cached
        result = SubobjectHomset(self, domain, codomain)
        self._homsets[key] = result
        return result


    def leq(self, left, right) -> bool:
        return self.Mor(left, right).has_morphism()

    def identity(self, subobject):
        return self.Mor(subobject, subobject).identity()

    def _repr_(self) -> str:
        return f"Subobjects of {self.base_object()}"


class SuperobjectCategory(CosliceCategory):
    r"""The category of represented quotient/superobjects of one object."""

    def __contains__(self, candidate) -> bool:
        return (
            super().__contains__(candidate)
            and candidate in EpimorphismArrowCategory(self.base_category())
        )

    def _repr_(self) -> str:
        return f"Superobjects of {self.base_object()}"


class WideSubcategory(Category):
    r"""A category with the same objects as ``C`` and a selected class of arrows."""

    def __init__(self, base_category, arrow_category) -> None:
        if arrow_category.base_category() != base_category:
            raise ValueError("the selected arrows must belong to the stated base category")
        self._base_category = base_category
        self._arrow_category = arrow_category
        super().__init__()

    def _make_named_class_key(self, name):
        return self._base_category, self._arrow_category

    def base_category(self):
        return self._base_category

    def arrow_category(self):
        return self._arrow_category

    def super_categories(self):
        return [self.base_category()]

    def __contains__(self, candidate) -> bool:
        return candidate in self.base_category()

    def admits(self, arrow) -> bool:
        try:
            arrow_object = self.arrow_category()(arrow)
        except (TypeError, ValueError):
            return False
        return arrow_object in self.arrow_category()

    def _repr_(self) -> str:
        return f"Wide subcategory of {self.base_category()} with arrows in {self.arrow_category()}"


class CoreHomset(CategoricalHomset):
    Element = CategoricalIsomorphism

    def __init__(self, core_category, domain, codomain) -> None:
        self._core_category = core_category
        CategoricalHomset.__init__(
            self, HomCategoryConstruction(core_category), domain, codomain
        )

    def core_category(self):
        return self._core_category

    def __contains__(self, candidate) -> bool:
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
        if inverse is None:
            forward, inverse = forward
        return CategoricalIsomorphism(self, forward, inverse)

    def _from_known_inverse_pair(self, forward, inverse):
        r"""Construct an isomorphism from an inverse pair proved by its owner."""
        return CategoricalIsomorphism(self, forward, inverse, verify=False)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on an endomorphism Hom-set")
        base = self.core_category().base_category()
        identity = base.Mor(self.domain(), self.domain()).identity()
        return self(identity, identity)


class CoreCategory(Category):
    r"""The maximal subgroupoid (core) of a represented category."""

    def __init__(self, base_category) -> None:
        self._base_category = base_category
        self._homsets = {}
        super().__init__()

    def _make_named_class_key(self, name):
        return self._base_category

    def base_category(self):
        return self._base_category

    def super_categories(self):
        return [self.base_category()]

    def __contains__(self, candidate) -> bool:
        return candidate in self.base_category()

    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("the core Hom requires two base-category objects")
        key = (id(domain), id(codomain))
        cached = self._homsets.get(key)
        if cached is not None and cached.domain() is domain and cached.codomain() is codomain:
            return cached
        result = CoreHomset(self, domain, codomain)
        self._homsets[key] = result
        return result


    def identity(self, obj):
        return self.Mor(obj, obj).identity()

    def _repr_(self) -> str:
        return f"Core of {self.base_category()}"


def Core(base_category):
    return CoreCategory(base_category)


def SliceOver(base_category, base_object):
    return SliceCategory(base_category, base_object)


def CosliceUnder(base_category, base_object):
    return CosliceCategory(base_category, base_object)


def SubobjectsOf(base_category, base_object):
    return SubobjectCategory(base_category, base_object)


def SuperobjectsOf(base_category, base_object):
    return SuperobjectCategory(base_category, base_object)


def core_mor(domain, codomain):
    r"""Return ``Hom`` in the core of the greatest category holding both objects."""
    return Core(common_category(domain, codomain)).Mor(domain, codomain)


def _isomorphism_from_known_inverse_pair(forward, inverse):
    r"""Transport a previously proved inverse pair without re-solving equality."""
    return core_mor(forward.domain(), forward.codomain())._from_known_inverse_pair(
        forward, inverse
    )


def Isomorphism(forward, inverse):
    r"""Return the isomorphism represented by mutually inverse arrows."""
    return core_mor(forward.domain(), forward.codomain())(forward, inverse)


__all__ = [
    "common_category",
    "core_mor",
    "Isomorphism",
    "IsoArrowCategory",
    "EndArrowCategory",
    "AutomorphismArrowCategory",
    "ArrowCategory",
    "ArrowObject",
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
