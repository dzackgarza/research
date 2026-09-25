r"""Categories of chosen truncated projective resolutions.

For a category C, a projective class P <= C and n >= 0, Resolutions(C, P, n)
is a category of chosen data over objects of C.  Its objects are augmented
simplicial resolutions through degree n whose resolved levels lie in P; its
morphisms are maps of the augmented truncated simplicial objects.  The target
projection remembers only the augmentation target.  Hence this is not a
subcategory of C: several resolution objects can lie over the same object.

The common owner supplies three constructions whose acyclicity follows from
the construction itself: a projective-source epimorphism in truncation zero,
the constant length-zero resolution of a projective object, and the standard
comonadic bar resolution attached to an adjunction F left adjoint to U.
Additive specializations may represent the same datum by a chain complex.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping

from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_method
from sage.misc.unknown import Unknown
from sage.rings.infinity import Infinity
from sage.structure.parent import Parent

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    MorCategoryConstruction,
    _category_accepts_morphism,
    _category_mor_parent,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    Objects,
    OwnedCategory,
)
from dzack_research.preamble.categories.functors.core import Adjunction, Functor
from dzack_research.preamble.owned_category import _object_of


def _normalize_truncation(truncation):
    match truncation:
        case _ if truncation is Infinity:
            return Infinity
        case _:
            value = int(truncation)
            match value < 0:
                case True:
                    raise ValueError(
                        f"a resolution truncation is a nonnegative degree, but got {truncation}"
                    )
                case False:
                    return value


def _iterate_functor(functor: Functor, value, count: int):
    result = value
    for _ in range(int(count)):
        result = functor(result)
    return result


def _component_function(components):
    match components:
        case Mapping():
            return components.__getitem__
        case _ if callable(components):
            return components
        case _:
            raise TypeError(
                "a morphism of resolutions needs its degree components as a mapping or callable"
            )


class ResolutionMorphism(Morphism):
    r"""A map of chosen truncated resolutions."""

    def __init__(self, parent, components, *, target_morphism=None) -> None:
        Morphism.__init__(self, parent)
        source = self.domain()
        target = self.codomain()
        category = source.resolution_category()
        match target.resolution_category() is category:
            case False:
                raise ValueError(
                    f"a resolution morphism needs one resolution category, but {source} lies in "
                    f"{category} and {target} lies in {target.resolution_category()}"
                )
            case True:
                pass
        base = category.base_category()
        match target_morphism:
            case None:
                match source.target() is target.target():
                    case False:
                        raise ValueError(
                            f"a resolution map {source} -> {target} over different targets needs a base morphism "
                            f"{source.target()} -> {target.target()}"
                        )
                    case True:
                        target_morphism = _category_mor_parent(
                            base, source.target(), target.target()
                        ).identity()
            case _:
                pass
        match _category_accepts_morphism(
            base, source.target(), target.target(), target_morphism
        ):
            case False:
                raise TypeError(
                    f"the map below a resolution morphism {source} -> {target} must be a morphism "
                    f"{source.target()} -> {target.target()} of {base}, but it is {target_morphism}"
                )
            case True:
                pass
        self._target_morphism = target_morphism
        self._component_function = _component_function(components)
        source._validate_resolution_morphism_to(
            target,
            self._target_morphism,
            self._component_function,
        )

    def target_morphism(self):
        return self._target_morphism

    base_morphism = target_morphism

    def component(self, degree: int):
        degree = int(degree)
        match 0 <= degree <= self.domain().truncation():
            case False:
                raise ValueError(
                    f"the resolution map {self} has components only in degrees 0 through "
                    f"{self.domain().truncation()}, but degree {degree} was requested"
                )
            case True:
                return self._component_function(degree)

    def __mul__(self, other):
        match other:
            case ResolutionMorphism() if other.codomain() is self.domain():
                category = self.domain().resolution_category()
                return category.Mor(other.domain(), self.codomain())(
                    lambda degree: self.component(degree) * other.component(degree),
                    target_morphism=self.target_morphism()
                    * other.target_morphism(),
                )
            case _:
                return NotImplemented

    def __eq__(self, other):
        match self is other:
            case True:
                return True
            case False:
                pass
        match (
            isinstance(other, ResolutionMorphism)
            and self.domain() is other.domain()
            and self.codomain() is other.codomain()
        ):
            case False:
                return False
            case True:
                pass
        target_equal = self.target_morphism() == other.target_morphism()
        match target_equal:
            case False:
                return False
            case _ if target_equal is Unknown:
                return Unknown
            case True:
                pass
        match self.domain().truncation():
            case _ if self.domain().truncation() is Infinity:
                return Unknown
            case truncation:
                component_equalities = tuple(
                    self.component(degree) == other.component(degree)
                    for degree in range(truncation + 1)
                )
                match any(answer is False for answer in component_equalities):
                    case True:
                        return False
                    case False:
                        match all(
                            answer is True for answer in component_equalities
                        ):
                            case True:
                                return True
                            case False:
                                return Unknown

    def __ne__(self, other):
        equal = self == other
        match equal:
            case _ if equal is Unknown:
                return Unknown
            case _:
                return not equal

    def _repr_(self) -> str:
        return (
            f"Resolution morphism {self.domain()} -> {self.codomain()} over "
            f"{self.target_morphism()}"
        )


class ResolutionMor(CategoricalMor):
    r"""The Mor object between two chosen truncated resolutions."""

    Element = ResolutionMorphism

    def _element_constructor_(self, components, *, target_morphism=None):
        match components:
            case ResolutionMorphism() as morphism:
                match (
                    morphism.domain() is self.domain()
                    and morphism.codomain() is self.codomain()
                ):
                    case False:
                        raise ValueError(
                            f"cannot view {morphism} as a resolution morphism {self.domain()} -> "
                            f"{self.codomain()}: its endpoints are {morphism.domain()} -> "
                            f"{morphism.codomain()}"
                        )
                    case True:
                        pass
                match morphism.parent() is self:
                    case True:
                        return morphism
                    case False:
                        match self.domain().truncation():
                            case _ if self.domain().truncation() is Infinity:
                                components = morphism.component
                            case truncation:
                                components = {
                                    degree: morphism.component(degree)
                                    for degree in range(truncation + 1)
                                }
                        return self.element_class(
                            self,
                            components,
                            target_morphism=morphism.target_morphism(),
                        )
            case _:
                return self.element_class(
                    self,
                    components,
                    target_morphism=target_morphism,
                )

    @cached_method
    def identity(self):
        match self.domain() is self.codomain():
            case False:
                raise ValueError(
                    f"the identity resolution morphism exists only on Mor(P, P), but this is "
                    f"Mor({self.domain()}, {self.codomain()})"
                )
            case True:
                pass
        resolution = self.domain()
        base = resolution.base_category()
        return self(
            lambda degree: _category_mor_parent(
                base, resolution.level(degree), resolution.level(degree)
            ).identity(),
            target_morphism=_category_mor_parent(
                base, resolution.target(), resolution.target()
            ).identity(),
        )


class ResolutionMorCategoryConstruction(MorCategoryConstruction):
    r"""The Mor family of chosen truncated resolutions."""

    def fixed_category_class(self):
        return ResolutionMor


class _ResolutionTargetFunctor(Functor):
    r"""The target projection from a resolution category to its base."""

    def __init__(self, resolution_category) -> None:
        self._resolution_category = resolution_category
        super().__init__(
            resolution_category,
            resolution_category.base_category(),
        )

    def _apply_object(self, resolution: Parent):
        return resolution.target()

    def _apply_morphism(self, morphism: ResolutionMorphism):
        return morphism.target_morphism()

    def _repr_(self) -> str:
        return f"Target projection from {self.domain()}"


class _DegreeZeroResolutionTransport(Functor):
    r"""Transport degree-zero resolutions along a functor preserving the datum."""

    def __init__(self, source, target, functor: Functor) -> None:
        match (source.truncation(), target.truncation()):
            case (0, 0):
                pass
            case _:
                raise ValueError(
                    "generic resolution transport is defined here for degree-zero resolutions; "
                    f"the source and target truncations are {source.truncation()} and "
                    f"{target.truncation()}"
                )
        match functor.domain() == source.base_category():
            case False:
                raise ValueError(
                    f"transport from {source} needs a functor with domain {source.base_category()}, "
                    f"but {functor} starts at {functor.domain()}"
                )
            case True:
                pass
        match functor.codomain() == target.base_category():
            case False:
                raise ValueError(
                    f"transport to {target} needs a functor with codomain {target.base_category()}, "
                    f"but {functor} ends at {functor.codomain()}"
                )
            case True:
                pass
        self._transported_functor = functor
        super().__init__(source, target)

    def transported_functor(self) -> Functor:
        return self._transported_functor

    def _apply_object(self, resolution: Parent):
        return self.codomain().degree_zero(
            self.transported_functor()(resolution.augmentation()),
            length=resolution.length(),
        )

    def _apply_morphism(self, morphism: ResolutionMorphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        return self.codomain().Mor(source, target)(
            {0: self.transported_functor()(morphism.component(0))},
            target_morphism=self.transported_functor()(
                morphism.target_morphism()
            ),
        )

    def _repr_(self) -> str:
        return f"Degree-zero resolution transport along {self.transported_functor()}"


class Resolutions(OwnedCategory):
    r"""The category of chosen n-truncated resolutions with levels in P."""

    _MorCategory = ResolutionMorCategoryConstruction

    @staticmethod
    def __classcall__(
        cls,
        base_category: Category,
        projective_class: Category,
        truncation=0,
        level_category=None,
    ):
        match level_category:
            case None:
                level_category = projective_class
            case _:
                pass
        return Category.__classcall__(
            cls,
            base_category,
            projective_class,
            _normalize_truncation(truncation),
            level_category,
        )

    def __init__(
        self,
        base_category: Category,
        projective_class: Category,
        truncation=0,
        level_category=None,
    ) -> None:
        truncation = _normalize_truncation(truncation)
        match level_category:
            case None:
                level_category = projective_class
            case _:
                pass
        match projective_class.is_subcategory(base_category):
            case False:
                raise TypeError(
                    f"the projective class of a resolution category over {base_category} must be a "
                    f"subcategory of it, but {projective_class} is not"
                )
            case True:
                pass
        match level_category.is_subcategory(projective_class):
            case False:
                raise TypeError(
                    f"the allowed resolution levels in {level_category} must lie in the projective class "
                    f"{projective_class}, but that subcategory relation is not declared"
                )
            case True:
                pass
        self._base_category = base_category
        self._projective_class = projective_class
        self._level_category = level_category
        self._truncation = truncation
        super().__init__()

    def base_category(self) -> Category:
        return self._base_category

    def projective_class(self) -> Category:
        return self._projective_class

    def level_category(self) -> Category:
        r"""Return the category imposed levelwise on this chosen truncation."""
        return self._level_category

    def truncation(self):
        return self._truncation

    def super_categories(self):
        return [Objects()]

    def _repr_(self) -> str:
        return (
            f"{self.truncation()}-truncated resolutions in {self.base_category()} "
            f"with projective class {self.projective_class()} and levels in {self.level_category()}"
        )

    def an_object(self):
        return self.constant(self.level_category().an_object())

    @cached_method
    def target_functor(self) -> Functor:
        r"""Return the target projection to the base category."""
        return _ResolutionTargetFunctor(self)

    def _object(
        self,
        target,
        level_function,
        augmentation,
        *,
        face_function=None,
        degeneracy_function=None,
        length=Unknown,
        model="simplicial",
        **construction_data,
    ):
        match target in self.base_category():
            case False:
                raise TypeError(
                    f"a resolution in {self} must resolve an object of {self.base_category()}, "
                    f"but {target} is not one"
                )
            case True:
                pass
        match self.truncation():
            case _ if self.truncation() is Infinity:
                pass
            case truncation:
                for degree in range(truncation + 1):
                    term = level_function(degree)
                    match term in self.level_category():
                        case False:
                            raise TypeError(
                                f"degree {degree} of a resolution in {self} must lie in "
                                f"{self.level_category()}, but it is {term}"
                            )
                        case True:
                            pass
        level_zero = level_function(0)
        match _category_accepts_morphism(
            self.base_category(), level_zero, target, augmentation
        ):
            case False:
                raise TypeError(
                    f"the augmentation of a resolution in {self} must be a morphism "
                    f"{level_zero} -> {target} of {self.base_category()}, but it is "
                    f"{augmentation}"
                )
            case True:
                pass
        return _object_of(
            self,
            resolution_target=target,
            resolution_level_function=level_function,
            resolution_augmentation=augmentation,
            resolution_face_function=face_function,
            resolution_degeneracy_function=degeneracy_function,
            resolution_length=length,
            resolution_model=model,
            **construction_data,
        )

    def degree_zero(self, augmentation, *, length=Unknown):
        r"""Return the truncation-zero resolution represented by an epimorphism."""
        match self.truncation():
            case 0:
                pass
            case _:
                raise ValueError(
                    f"a bare generating epimorphism belongs to truncation zero, but {self} has "
                    f"truncation {self.truncation()}"
                )
        match self.base_category().Epi(
            augmentation.domain(), augmentation.codomain()
        ).accepts(augmentation):
            case False:
                raise ValueError(
                    f"{augmentation} is not a represented epimorphism of {self.base_category()}; "
                    "use a theorem-backed constructor for a generating epimorphism whose epi structure "
                    "is known by construction"
                )
            case True:
                pass
        return self._object(
            augmentation.codomain(),
            lambda degree: augmentation.domain(),
            augmentation,
            length=length,
            model="degree-zero",
        )

    def from_selected_framing(self, target, owner):
        r"""Use an existing selected free-source epimorphism as truncation zero.

        This is the property-to-data bridge required while the legacy selected
        framing store is being migrated to resolution objects.  Its defining
        datum is already a chosen epimorphism; no categorical epi predicate is
        guessed from an arbitrary morphism.
        """
        match self.truncation():
            case 0:
                pass
            case _:
                raise ValueError(
                    f"a selected generating epimorphism supplies truncation zero, but {self} has "
                    f"truncation {self.truncation()}"
                )
        match target in self.base_category():
            case False:
                raise TypeError(
                    f"{target} is not an object of the base category {self.base_category()}"
                )
            case True:
                pass
        augmentation = target.selected_framing_morphism(owner)
        return self._object(
            target,
            lambda degree: augmentation.domain(),
            augmentation,
            length=Unknown,
            model="selected-framing",
        )

    def constant(self, projective_object):
        r"""Return the length-zero constant resolution of a projective object."""
        match projective_object in self.level_category():
            case False:
                raise TypeError(
                    f"a constant resolution in {self} needs an object of "
                    f"{self.level_category()}, but {projective_object} is not one"
                )
            case True:
                pass
        base = self.base_category()

        def identity():
            return _category_mor_parent(
                base, projective_object, projective_object
            ).identity()

        return self._object(
            projective_object,
            lambda degree: projective_object,
            identity(),
            face_function=lambda degree, index: identity(),
            degeneracy_function=lambda degree, index: identity(),
            length=0,
            model="constant",
        )

    def comonadic(self, adjunction: Adjunction, target):
        r"""Return the selected truncated comonadic bar resolution of target."""
        left = adjunction.left_adjoint()
        right = adjunction.right_adjoint()
        match left.codomain() == self.base_category():
            case False:
                raise ValueError(
                    f"the left adjoint defining a resolution in {self} must land in "
                    f"{self.base_category()}, but {left} lands in {left.codomain()}"
                )
            case True:
                pass
        match right.domain() == self.base_category():
            case False:
                raise ValueError(
                    f"the right adjoint defining a resolution in {self} must start in "
                    f"{self.base_category()}, but {right} starts in {right.domain()}"
                )
            case True:
                pass
        match target in self.base_category():
            case False:
                raise TypeError(
                    f"the comonadic resolution in {self} resolves an object of "
                    f"{self.base_category()}, but {target} is not one"
                )
            case True:
                pass
        comonad = right.then(left)

        def level(degree):
            return _iterate_functor(comonad, target, int(degree) + 1)

        def comultiplication(obj):
            return left(adjunction.unit(right(obj)))

        def face(degree, index):
            degree = int(degree)
            index = int(index)
            tail = _iterate_functor(comonad, target, degree - index)
            return _iterate_functor(
                comonad,
                adjunction.counit(tail),
                index,
            )

        def degeneracy(degree, index):
            degree = int(degree)
            index = int(index)
            tail = _iterate_functor(comonad, target, degree - index)
            return _iterate_functor(
                comonad,
                comultiplication(tail),
                index,
            )

        return self._object(
            target,
            level,
            adjunction.counit(target),
            face_function=face,
            degeneracy_function=degeneracy,
            length=Infinity,
            model="comonadic",
        )

    def transport_degree_zero(self, functor: Functor, target_resolutions) -> Functor:
        r"""Transport truncation-zero data when the target owner admits the image.

        The target resolution category is explicit because preservation of
        projectivity and epimorphisms is a theorem about the selected functor,
        not a property of arbitrary functors.  The target constructor performs
        its own admission check on every transported augmentation.
        """
        return _DegreeZeroResolutionTransport(self, target_resolutions, functor)

    def dold_kan_image(self):
        r"""Return the augmented-chain realization when the base is a module category."""
        from dzack_research.preamble.categories.modules.pure.modules import Modules
        from dzack_research.preamble.categories.modules.resolutions import (
            ModuleResolutions,
        )

        base = self.base_category()
        match base:
            case Modules():
                return ModuleResolutions(self)
            case _:
                raise TypeError(
                    f"Dold--Kan chain realization is defined here for module resolutions, "
                    f"but {self} is over {base}"
                )

    class ParentMethods:
        r"""One chosen truncated resolution."""

        def __init__(
            self,
            resolution_target,
            resolution_level_function: Callable[[int], Parent],
            resolution_augmentation,
            resolution_face_function=None,
            resolution_degeneracy_function=None,
            resolution_length=Unknown,
            resolution_model="simplicial",
            **rest,
        ) -> None:
            self._resolution_target = resolution_target
            self._resolution_level_function = resolution_level_function
            self._resolution_augmentation = resolution_augmentation
            self._resolution_face_function = resolution_face_function
            self._resolution_degeneracy_function = resolution_degeneracy_function
            self._resolution_length = resolution_length
            self._resolution_model = resolution_model
            super().__init__(**rest)

        def resolution_category(self) -> Category:
            return self.category()

        def base_category(self) -> Category:
            return self.resolution_category().base_category()

        def projective_class(self) -> Category:
            return self.resolution_category().projective_class()

        def level_category(self) -> Category:
            return self.resolution_category().level_category()

        def truncation(self):
            return self.resolution_category().truncation()

        def target(self):
            return self._resolution_target

        resolved_object = target

        def level(self, degree: int):
            degree = int(degree)
            match 0 <= degree <= self.truncation():
                case False:
                    raise ValueError(
                        f"{self} is chosen only through resolution degree "
                        f"{self.truncation()}, so degree {degree} is not part of its datum"
                    )
                case True:
                    return self._resolution_level_function(degree)

        term = level

        def augmentation(self):
            return self._resolution_augmentation

        def length(self):
            r"""Return the resolution length, independently of truncation."""
            return self._resolution_length

        resolution_length = length

        def model(self) -> str:
            return self._resolution_model

        def face(self, degree: int, index: int):
            degree = int(degree)
            index = int(index)
            match 1 <= degree <= self.truncation():
                case False:
                    raise ValueError(
                        f"faces of {self} occur in represented degrees 1 through "
                        f"{self.truncation()}, but degree {degree} was requested"
                    )
                case True:
                    pass
            match 0 <= index <= degree:
                case False:
                    raise ValueError(
                        f"a degree-{degree} simplicial object has faces indexed 0 through "
                        f"{degree}, but index {index} was requested"
                    )
                case True:
                    pass
            match self._resolution_face_function:
                case None:
                    raise TypeError(
                        f"{self} is represented by the {self.model()} model, not by explicit "
                        "simplicial face maps"
                    )
                case face_function:
                    return face_function(degree, index)

        def degeneracy(self, degree: int, index: int):
            degree = int(degree)
            index = int(index)
            match 0 <= degree < self.truncation():
                case False:
                    raise ValueError(
                        f"degeneracies of {self} occur in degrees 0 through "
                        f"{self.truncation() - 1}, but degree {degree} was requested"
                    )
                case True:
                    pass
            match 0 <= index <= degree:
                case False:
                    raise ValueError(
                        f"a degree-{degree} simplicial object has degeneracies indexed 0 "
                        f"through {degree}, but index {index} was requested"
                    )
                case True:
                    pass
            match self._resolution_degeneracy_function:
                case None:
                    raise TypeError(
                        f"{self} is represented by the {self.model()} model, not by explicit "
                        "simplicial degeneracies"
                    )
                case degeneracy_function:
                    return degeneracy_function(degree, index)

        def is_acyclic_through_truncation(self) -> bool:
            return True

        def _validate_resolution_morphism_to(
            self,
            target,
            target_morphism,
            component_function,
        ) -> None:
            match self.truncation():
                case _ if self.truncation() is Infinity:
                    # As for a natural transformation on an infinite source
                    # category, the component family is theorem-backed data:
                    # there is no finite admission loop that can establish all
                    # simplicial identities.  Individual components remain
                    # owned morphisms when accessed.
                    return
                case _:
                    pass
            base = self.base_category()
            for degree in range(self.truncation() + 1):
                component = component_function(degree)
                match _category_accepts_morphism(
                    base,
                    self.level(degree),
                    target.level(degree),
                    component,
                ):
                    case False:
                        raise TypeError(
                            f"degree {degree} of a resolution morphism {self} -> {target} "
                            f"must be a morphism {self.level(degree)} -> "
                            f"{target.level(degree)} of {base}, but it is {component}"
                        )
                    case True:
                        pass
            match (
                target.augmentation() * component_function(0)
                == target_morphism * self.augmentation()
            ):
                case False:
                    raise ValueError(
                        f"the degree-zero component of a resolution morphism {self} -> "
                        f"{target} does not commute with the augmentations"
                    )
                case True:
                    pass
            for degree in range(1, self.truncation() + 1):
                for index in range(degree + 1):
                    match (
                        target.face(degree, index) * component_function(degree)
                        == component_function(degree - 1)
                        * self.face(degree, index)
                    ):
                        case False:
                            raise ValueError(
                                f"the resolution morphism {self} -> {target} does not commute "
                                f"with face {index} in degree {degree}"
                            )
                        case True:
                            pass
            for degree in range(self.truncation()):
                for index in range(degree + 1):
                    match (
                        target.degeneracy(degree, index)
                        * component_function(degree)
                        == component_function(degree + 1)
                        * self.degeneracy(degree, index)
                    ):
                        case False:
                            raise ValueError(
                                f"the resolution morphism {self} -> {target} does not commute "
                                f"with degeneracy {index} in degree {degree}"
                            )
                        case True:
                            pass


__all__ = [
    "ResolutionMorphism",
    "Resolutions",
]
