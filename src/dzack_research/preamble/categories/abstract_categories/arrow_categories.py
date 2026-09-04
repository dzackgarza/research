r"""Arrow categories, commuting squares, cores, and slice-style categories."""

from dzack_research.preamble.categories.abstract_categories.hom_foundation import OwnedHomset
from sage.categories.category import Category
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets
from sage.categories.homset import Hom, Homset
from sage.categories.morphism import Morphism
from sage.categories.sets_cat import Sets as SageSets
from dzack_research.preamble.categories.sets.set_categories import Sets as _OwnedSets
from sage.structure.parent import Parent


def _morphisms_agree(left, right) -> bool:
    r"""Decide equality through the morphism/Hom owner when represented."""
    if left.domain() is not right.domain() or left.codomain() is not right.codomain():
        return False
    if left is right:
        return True

    if isinstance(left, CommutativeSquare) and isinstance(right, CommutativeSquare):
        return _morphisms_agree(left.left(), right.left()) and _morphisms_agree(
            left.right(), right.right()
        )

    element_decider = getattr(left, "morphisms_agree", None)
    if callable(element_decider):
        return bool(element_decider(right))

    left_parent = left.parent()
    if left_parent is right.parent():
        parent_decider = getattr(left_parent, "morphisms_agree", None)
        if callable(parent_decider):
            return bool(parent_decider(left, right))

    # Ordinary equality may already be exact for the represented morphism
    # family.  A false result is not enough for generic Sage SetMorphism,
    # whose equality is intensional, so finite sets retain their extensional
    # category-level decision below.
    try:
        if left == right:
            return True
    except NotImplementedError:
        pass

    domain = left.domain()
    if domain in FiniteEnumeratedSets():
        return all(left(element) == right(element) for element in domain)

    raise NotImplementedError(
        f"equality of represented morphisms out of {domain} has no active decision procedure"
    )


def _identity_morphism_in_theory(arrow, obj):
    r"""Return the identity of ``obj`` in the Hom theory containing ``arrow``."""
    parent = arrow.parent()
    family = getattr(parent, "hom_family", None)
    if callable(family):
        fixed = family().Of(obj, obj)
        identity = getattr(fixed, "identity", None)
        if callable(identity):
            return identity()
        identity = getattr(fixed, "identity_endomorphism", None)
        if callable(identity):
            return identity()
    return _identity_morphism(obj)


def _identity_morphism(obj):
    r"""Return the identity arrow through the object's public Hom surface."""
    if isinstance(obj, ArrowObject):
        return obj.arrow_category().hom(obj, obj).identity()
    categorical_identity = getattr(obj, "categorical_identity_morphism", None)
    if categorical_identity is not None:
        return categorical_identity()
    try:
        return Hom(obj, obj).identity()
    except (TypeError, ValueError):
        return _OwnedSets().hom(obj, obj).identity()


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
        if not _morphisms_agree(right * source, target * left):
            raise ValueError("the square does not commute")
        self._left = left
        self._right = right

    def left(self):
        return self._left

    def right(self):
        return self._right

    def components(self):
        return self.left(), self.right()

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        category = self.parent().arrow_category()
        return category.hom(other.domain(), self.codomain())(
            self.left() * other.left(),
            self.right() * other.right(),
        )

    def _repr_(self) -> str:
        return f"Commutative square from {self.domain()} to {self.codomain()}"


class ArrowHomset(OwnedHomset):
    Element = CommutativeSquare

    def __init__(self, arrow_category, source, target) -> None:
        self._arrow_category = arrow_category
        Homset.__init__(self, source, target, category=SageSets())

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
        return self(
            _identity_morphism(arrow.domain()),
            _identity_morphism(arrow.codomain()),
        )


class ArrowCategory(Category):
    r"""The category ``Arr(C)=Fun([1],C)``."""

    def __init__(self, base_category) -> None:
        self._base_category = base_category
        self._arrow_objects = {}
        super().__init__()

    def _make_named_class_key(self, name):
        return self._base_category

    def base_category(self):
        return self._base_category

    def super_categories(self):
        from dzack_research.preamble.categories.sets.set_categories import Sets

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

    def hom(self, source, target):
        if source not in self or target not in self:
            raise TypeError("an arrow-category Hom requires two arrow objects")
        return ArrowHomset(self, source, target)

    Hom = hom

    def morphism(self, source, target, left, right):
        return self.hom(source, target)(left, right)

    def identity(self, arrow_object):
        return self.hom(arrow_object, arrow_object).identity()

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
        if right is not None:
            if not _morphisms_agree(right, _identity_morphism(fixed)):
                raise ValueError("the fixed edge of a slice morphism is the identity")
        return CommutativeSquare(self, factor, _identity_morphism(fixed))

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

    def hom(self, source, target):
        if source not in self or target not in self:
            raise TypeError("a slice Hom requires two arrows into the fixed base object")
        return self._homset(SliceHomset, source, target)

    Hom = hom

    def _repr_(self) -> str:
        return f"Slice category {self.base_category()}/{self.base_object()}"


class CosliceHomset(ArrowHomset):
    r"""Morphisms in a coslice; the edge at the fixed domain is the identity."""

    def _element_constructor_(self, factor, left=None):
        fixed = self.domain().arrow().domain()
        if self.codomain().arrow().domain() is not fixed:
            raise ValueError("coslice objects require one fixed domain")
        if left is not None:
            if not _morphisms_agree(left, _identity_morphism(fixed)):
                raise ValueError("the fixed edge of a coslice morphism is the identity")
        return CommutativeSquare(self, _identity_morphism(fixed), factor)


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

    def hom(self, source, target):
        if source not in self or target not in self:
            raise TypeError("a coslice Hom requires two arrows from the fixed base object")
        return self._homset(CosliceHomset, source, target)

    Hom = hom

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
    r"""The full subcategory of the arrow category on represented monomorphisms."""

    def __contains__(self, candidate) -> bool:
        if not super().__contains__(candidate):
            return False
        try:
            return candidate.arrow().is_injective() is True
        except (AttributeError, NotImplementedError):
            return False


class EpimorphismArrowCategory(ArrowCategory):
    r"""The full subcategory of the arrow category on represented epimorphisms."""

    def __contains__(self, candidate) -> bool:
        if not super().__contains__(candidate):
            return False
        try:
            return candidate.arrow().is_surjective() is True
        except (AttributeError, NotImplementedError):
            return False


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
        if not _morphisms_agree(left, right):
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
        return self.parent().subobject_category().hom(
            other.domain(), self.codomain()
        )(self.factor_morphism() * other.factor_morphism())


class SubobjectHomset(OwnedHomset):
    Element = SubobjectMorphism

    def __init__(self, subobject_category, domain, codomain) -> None:
        self._subobject_category = subobject_category
        Homset.__init__(self, domain, codomain, category=SageSets())

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
        super().__init__()

    def _make_named_class_key(self, name):
        return self._base_category, self._base_object

    def base_category(self):
        return self._base_category

    def base_object(self):
        return self._base_object

    def super_categories(self):
        from dzack_research.preamble.categories.sets.set_categories import Sets

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

    def hom(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("both objects must be subobjects of the fixed base object")
        return SubobjectHomset(self, domain, codomain)

    Hom = hom

    def leq(self, left, right) -> bool:
        return self.hom(left, right).has_morphism()

    def identity(self, subobject):
        return self.hom(subobject, subobject).identity()

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


class CategoricalIsomorphism(Morphism):
    r"""An isomorphism represented by mutually inverse arrows."""

    def __init__(self, parent, forward, inverse, *, verify=True) -> None:
        Morphism.__init__(self, parent)
        if forward.domain() is not self.domain() or forward.codomain() is not self.codomain():
            raise ValueError("the forward map has the wrong endpoints")
        if inverse.domain() is not self.codomain() or inverse.codomain() is not self.domain():
            raise ValueError("the inverse map has the wrong endpoints")
        if verify:
            if not _morphisms_agree(
                inverse * forward,
                _identity_morphism_in_theory(forward, self.domain()),
            ):
                raise ValueError("the stated inverse is not a left inverse")
            if not _morphisms_agree(
                forward * inverse,
                _identity_morphism_in_theory(forward, self.codomain()),
            ):
                raise ValueError("the stated inverse is not a right inverse")
        self._forward = forward
        self._inverse = inverse

    def forward(self):
        return self._forward

    def inverse(self):
        return self._inverse

    def __call__(self, element):
        return self.forward()(element)

    def _call_(self, element):
        return self.forward()(element)

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        return CoreHomset(other.domain(), self.codomain())(
            self.forward() * other.forward(),
            other.inverse() * self.inverse(),
        )


class CoreHomset(OwnedHomset):
    Element = CategoricalIsomorphism

    def __init__(self, domain, codomain) -> None:
        Homset.__init__(self, domain, codomain, category=SageSets())

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
        identity = _identity_morphism(self.domain())
        return self(identity, identity)


class CoreCategory(Category):
    r"""The maximal subgroupoid (core) of a represented category."""

    def __init__(self, base_category) -> None:
        self._base_category = base_category
        super().__init__()

    def _make_named_class_key(self, name):
        return self._base_category

    def base_category(self):
        return self._base_category

    def super_categories(self):
        return [self.base_category()]

    def __contains__(self, candidate) -> bool:
        return candidate in self.base_category()

    def hom(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("the core Hom requires two base-category objects")
        return CoreHomset(domain, codomain)

    Hom = hom

    def identity(self, obj):
        return self.hom(obj, obj).identity()

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


def _isomorphism_from_known_inverse_pair(forward, inverse):
    r"""Transport a previously proved inverse pair without re-solving equality."""
    return CoreHomset(forward.domain(), forward.codomain())._from_known_inverse_pair(
        forward, inverse
    )


def Isomorphism(forward, inverse):
    r"""Return the isomorphism represented by mutually inverse arrows."""
    return CoreHomset(forward.domain(), forward.codomain())(forward, inverse)


__all__ = [
    "common_category",
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
