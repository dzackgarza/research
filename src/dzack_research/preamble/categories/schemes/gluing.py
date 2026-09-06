r"""Descent data for modules and algebras on represented distinguished affine covers."""

from itertools import combinations

from sage.categories.category import Category
from sage.categories.morphism import Morphism, SetMorphism
from sage.misc.classcall_metaclass import typecall
from sage.structure.element import ModuleElement
from sage.structure.parent import Parent
from sage.structure.richcmp import op_EQ, op_NE
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    CategoricalIsomorphism,
    CategoryPacketMethods,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.objects import Objects
from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    AlgebrasWithChosenFinitePresentation,
    CommutativeAlgebras,
)
from dzack_research.preamble.categories.algebras.restricted_scalars import (
    restrict_algebra_scalars,
)
from dzack_research.preamble.categories.functors.algebra_modules import (
    algebra_underlying_module_functor,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
    module_homset,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    Modules,
    restrict_scalars,
)
from dzack_research.preamble.categories.sets.set_categories import Sets


def _finite_framing(module):
    if not module.is_framed():
        raise TypeError("affine module descent currently requires finitely framed local modules")
    labels = module.module_generating_set()
    if not labels.cardinality().is_finite():
        raise TypeError("affine module descent currently requires finitely framed local modules")
    return labels


def _change_coefficients(element, source, target, ring_map):
    r"""Base-change one framed module element along ``ring_map``."""

    coefficients = module_coefficients(source(element), source)
    return target.linear_combination(
        {
            label: ring_map(coefficient)
            for label, coefficient in coefficients.items()
            if ring_map(coefficient) != target.base_ring().zero()
        }
    )


def _maps_agree_on_framing(left, right) -> bool:
    if left.domain() is not right.domain() or left.codomain() is not right.codomain():
        return False
    labels = _finite_framing(left.domain())
    return all(
        left(left.domain().module_generator(label))
        == right(right.domain().module_generator(label))
        for label in labels
    )


_MODULE_GLUING_DATA_CATEGORIES = {}


class ModuleGluingHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return ModuleGluingHomset


class ModuleGluingData(CategoryPacketMethods, Category):
    r"""Module descent data on one represented distinguished affine cover."""

    @staticmethod
    def __classcall__(category_class, cover):
        key = id(cover)
        cached = _MODULE_GLUING_DATA_CATEGORIES.get(key)
        if cached is not None and cached.cover() is cover:
            return cached
        category = typecall(category_class, cover)
        _MODULE_GLUING_DATA_CATEGORIES[key] = category
        return category

    def __init__(self, cover) -> None:
        self._cover = cover
        Category.__init__(self)

    def cover(self):
        return self._cover

    def super_categories(self):
        return [Objects()]

    def __contains__(self, candidate) -> bool:
        return (
            isinstance(candidate, ModuleGluingDatum)
            and candidate.cover() is self.cover()
        )

    def _repr_object_names(self):
        return f"module descent data on {self.cover()}"

    _HomCategory = ModuleGluingHomCategoryConstruction


class ModuleGluingDatum(Parent):
    r"""Finitely framed modules with descent isomorphisms on an affine cover."""

    def __init__(self, cover, local_modules, transitions) -> None:
        self._cover = cover
        self._local_modules = tuple(local_modules)
        if len(self._local_modules) != len(cover.opens()):
            raise ValueError("module gluing requires exactly one local module on each affine chart")
        for index, module in enumerate(self._local_modules):
            if module.base_ring() is not cover.open(index).coordinate_algebra():
                raise ValueError("each local module must be defined over its chart section ring")
            _finite_framing(module)

        expected = {
            (left, right)
            for left in range(len(self._local_modules))
            for right in range(left + 1, len(self._local_modules))
        }
        supplied = set(transitions)
        if supplied != expected:
            raise ValueError(
                f"module gluing requires one transition isomorphism for each pair {sorted(expected)}"
            )
        self._transitions = dict(transitions)
        self._restriction_maps = {}
        self._transition_restrictions = {}
        self._inverse_transitions = {}
        self._compatible_sections = None
        self._sheaf = None
        self._verify_pairwise_transitions()
        self._verify_cocycles()
        Parent.__init__(self, category=ModuleGluingData(cover))

    def cover(self):
        return self._cover

    def ringed_space(self):
        return self.cover().ambient_scheme()

    scheme = ringed_space

    def local_modules(self):
        return self._local_modules

    def local_module(self, index):
        return self.local_modules()[int(index)]

    def restricted_module(self, chart_index, *intersection_indices):
        return self.cover().restrict_module(
            self.local_module(chart_index),
            chart_index,
            *intersection_indices,
        )

    def transition(self, source_index, target_index):
        r"""Return the represented overlap isomorphism from one chart to another."""

        source_index = int(source_index)
        target_index = int(target_index)
        if source_index == target_index:
            raise ValueError("a transition isomorphism is requested between two distinct charts")
        if source_index < target_index:
            return self._transitions[source_index, target_index]
        key = (source_index, target_index)
        cached = self._inverse_transitions.get(key)
        if cached is not None:
            return cached
        original = self._transitions[target_index, source_index]
        from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
            Isomorphism,
        )

        cached = Isomorphism(original.inverse(), original.forward())
        self._inverse_transitions[key] = cached
        return cached

    def _verify_pairwise_transitions(self) -> None:
        for (left_index, right_index), transition in self._transitions.items():
            if not isinstance(transition, CategoricalIsomorphism):
                raise TypeError("module transition data must be represented categorical isomorphisms")
            source = self.restricted_module(left_index, left_index, right_index)
            target = self.restricted_module(right_index, left_index, right_index)
            forward = transition.forward()
            inverse = transition.inverse()
            if forward.domain() is not source or forward.codomain() is not target:
                raise ValueError("a module transition has the wrong overlap endpoints")
            if inverse.domain() is not target or inverse.codomain() is not source:
                raise ValueError("a module transition inverse has the wrong overlap endpoints")
            for label in _finite_framing(source):
                generator = source.module_generator(label)
                if inverse(forward(generator)) != generator:
                    raise ValueError("the stated module transition is not left-invertible on the overlap")
            for label in _finite_framing(target):
                generator = target.module_generator(label)
                if forward(inverse(generator)) != generator:
                    raise ValueError("the stated module transition is not right-invertible on the overlap")

    def restriction_map(self, chart_index, *intersection_indices):
        r"""Return ``M_i -> Res(M_i|U_I)`` over the chart restriction of scalars."""

        chart_index = int(chart_index)
        target_indices = self.cover().intersection_indices(
            chart_index,
            *intersection_indices,
        )
        return self.restriction_between_intersections(
            chart_index,
            (chart_index,),
            target_indices,
        )

    def restriction_between_intersections(
        self,
        chart_index,
        source_indices,
        target_indices,
    ):
        r"""Return ``M_i|U_I -> Res(M_i|U_J)`` for ``U_J subseteq U_I``."""

        chart_index = int(chart_index)
        source_indices = self.cover().intersection_indices(
            chart_index,
            *tuple(source_indices),
        )
        target_indices = self.cover().intersection_indices(
            chart_index,
            *tuple(target_indices),
        )
        if not set(source_indices).issubset(target_indices):
            raise ValueError("module restriction requires the target intersection to refine the source")
        key = (chart_index, source_indices, target_indices)
        cached = self._restriction_maps.get(key)
        if cached is not None:
            return cached
        source = self.restricted_module(chart_index, *source_indices)
        target = self.restricted_module(chart_index, *target_indices)
        if target is source:
            cached = module_homset(source, source).identity()
            self._restriction_maps[key] = cached
            return cached
        source_open = self.cover().intersection(source_indices)
        target_open = self.cover().intersection(target_indices)
        ring_map = self.scheme().structure_sheaf().restriction_map(source_open, target_open)
        restricted_target = restrict_scalars(target, ring_map)
        cached = module_homset(source, restricted_target)(
            lambda label: restricted_target.wrap(target.module_generator(label))
        )
        self._restriction_maps[key] = cached
        return cached

    def restrict_section(self, chart_index, section, *intersection_indices):
        r"""Restrict one local section to the selected cover intersection."""

        restriction = self.restriction_map(chart_index, *intersection_indices)
        image = restriction(self.local_module(chart_index)(section))
        underlying = getattr(image, "underlying_element", None)
        return image if underlying is None else underlying()

    def restrict_section_between_intersections(
        self,
        chart_index,
        section,
        source_indices,
        target_indices,
    ):
        r"""Restrict a section already living on one represented cover intersection."""

        restriction = self.restriction_between_intersections(
            chart_index,
            source_indices,
            target_indices,
        )
        source = self.restricted_module(chart_index, *tuple(source_indices))
        image = restriction(source(section))
        underlying = getattr(image, "underlying_element", None)
        return image if underlying is None else underlying()

    def transition_on_intersection(
        self,
        source_index,
        target_index,
        *intersection_indices,
    ):
        r"""Restrict a pairwise transition to a finer represented intersection."""

        source_index = int(source_index)
        target_index = int(target_index)
        indices = self.cover().intersection_indices(
            source_index,
            target_index,
            *intersection_indices,
        )
        key = (source_index, target_index, indices)
        cached = self._transition_restrictions.get(key)
        if cached is not None:
            return cached
        pair = tuple(sorted((source_index, target_index)))
        transition = self.transition(source_index, target_index).forward()
        if indices == pair:
            self._transition_restrictions[key] = transition
            return transition

        pair_open = self.cover().intersection(pair)
        target_open = self.cover().intersection(indices)
        ring_map = self.scheme().structure_sheaf().restriction_map(pair_open, target_open)
        pair_source = self.restricted_module(source_index, *pair)
        pair_target = self.restricted_module(target_index, *pair)
        source = self.restricted_module(source_index, *indices)
        target = self.restricted_module(target_index, *indices)

        def image(label):
            pair_image = transition(pair_source.module_generator(label))
            return _change_coefficients(pair_image, pair_target, target, ring_map)

        cached = module_homset(source, target)(image)
        self._transition_restrictions[key] = cached
        return cached

    def _verify_cocycles(self) -> None:
        for left_index, middle_index, right_index in combinations(
            range(len(self.local_modules())),
            3,
        ):
            indices = (left_index, middle_index, right_index)
            left_middle = self.transition_on_intersection(
                left_index,
                middle_index,
                *indices,
            )
            middle_right = self.transition_on_intersection(
                middle_index,
                right_index,
                *indices,
            )
            left_right = self.transition_on_intersection(
                left_index,
                right_index,
                *indices,
            )
            composite = middle_right * left_middle
            if not _maps_agree_on_framing(composite, left_right):
                raise ValueError("module transition isomorphisms fail the cocycle condition on a triple overlap")

    def compatible_sections(self):
        r"""Return the ``A``-module of local tuples agreeing under every transition."""

        if self._compatible_sections is None:
            self._compatible_sections = CompatibleLocalSectionsModule(self)
        return self._compatible_sections

    def sheaf(self):
        if self._sheaf is None:
            self._sheaf = GluedModuleSheaf(self)
        return self._sheaf

    def Mor(self, target):
        r"""Return the represented Hom category of descent morphisms to ``target``."""

        return self.category().Mor(self, target)

    def _repr_(self):
        return f"Module gluing datum on {self.cover()}"


class ModuleGluingMorphism(Morphism):
    r"""A morphism between module descent data on one represented affine cover."""

    def __init__(self, parent, local_maps) -> None:
        Morphism.__init__(self, parent)
        local_maps = tuple(local_maps)
        if len(local_maps) != len(self.domain().local_modules()):
            raise ValueError("a module descent morphism requires one local map on each affine chart")

        self._local_maps = tuple(
            module_homset(
                self.domain().local_module(index),
                self.codomain().local_module(index),
            )(local_map)
            for index, local_map in enumerate(local_maps)
        )
        self._restricted_local_maps = {}
        self._global_sections_map = None
        self._verify_overlap_compatibility()

    def cover(self):
        return self.domain().cover()

    def local_maps(self):
        return self._local_maps

    def local_map(self, index):
        return self.local_maps()[int(index)]

    def restricted_local_map(self, chart_index, *intersection_indices):
        r"""Restrict one chart map to the represented cover intersection."""

        chart_index = int(chart_index)
        indices = self.cover().intersection_indices(
            chart_index,
            *intersection_indices,
        )
        key = (chart_index, indices)
        cached = self._restricted_local_maps.get(key)
        if cached is not None:
            return cached

        local_map = self.local_map(chart_index)
        source = self.domain().restricted_module(chart_index, *indices)
        target = self.codomain().restricted_module(chart_index, *indices)
        if source is self.domain().local_module(chart_index):
            self._restricted_local_maps[key] = local_map
            return local_map

        source_open = self.cover().open(chart_index)
        target_open = self.cover().intersection(indices)
        ring_map = self.domain().scheme().structure_sheaf().restriction_map(
            source_open,
            target_open,
        )
        local_source = self.domain().local_module(chart_index)
        local_target = self.codomain().local_module(chart_index)

        def image(label):
            local_image = local_map(local_source.module_generator(label))
            return _change_coefficients(local_image, local_target, target, ring_map)

        cached = module_homset(source, target)(image)
        self._restricted_local_maps[key] = cached
        return cached

    def _verify_overlap_compatibility(self) -> None:
        for left_index, right_index in combinations(
            range(len(self.domain().local_modules())),
            2,
        ):
            source_transition = self.domain().transition(left_index, right_index).forward()
            target_transition = self.codomain().transition(left_index, right_index).forward()
            left_restriction = self.restricted_local_map(
                left_index,
                left_index,
                right_index,
            )
            right_restriction = self.restricted_local_map(
                right_index,
                left_index,
                right_index,
            )
            via_left = target_transition * left_restriction
            via_right = right_restriction * source_transition
            if not _maps_agree_on_framing(via_left, via_right):
                raise ValueError(
                    "module descent morphism is incompatible with transition maps on an overlap"
                )

    def global_sections_map(self):
        r"""Return the induced ambient-ring linear map on compatible global sections."""

        if self._global_sections_map is None:
            source_sections = self.domain().compatible_sections()
            target_sections = self.codomain().compatible_sections()

            def image(section):
                section = source_sections(section)
                return target_sections(
                    tuple(
                        self.local_map(index)(section.component(index))
                        for index in range(len(self.local_maps()))
                    )
                )

            self._global_sections_map = module_homset(
                source_sections,
                target_sections,
            ).elementwise(
                image,
                verify_linearity=False,
            )
        return self._global_sections_map

    def then(self, other):
        r"""Return ``other after self``."""

        if other.domain() is not self.codomain():
            raise ValueError("the first descent-morphism target must equal the second source")
        return other * self

    def __mul__(self, other):
        if not isinstance(other, ModuleGluingMorphism):
            return NotImplemented
        if other.codomain() is not self.domain():
            return NotImplemented
        return other.domain().Mor(self.codomain())(
            tuple(
                self.local_map(index) * other.local_map(index)
                for index in range(len(self.local_maps()))
            )
        )

    def _repr_(self):
        return f"Module descent morphism from {self.domain()} to {self.codomain()}"


class ModuleGluingHomset(CategoricalHomset):
    r"""The fixed Hom category between two module descent data on one cover."""

    Element = ModuleGluingMorphism

    def __init__(self, family, domain, codomain) -> None:
        if domain.cover() is not codomain.cover():
            raise ValueError("a module descent Hom requires one common affine cover")
        CategoricalHomset.__init__(self, family, domain, codomain)

    def _element_constructor_(self, local_maps):
        if isinstance(local_maps, ModuleGluingMorphism):
            if (
                local_maps.domain() is not self.domain()
                or local_maps.codomain() is not self.codomain()
            ):
                raise ValueError("the module descent morphism has the wrong endpoints")
            if local_maps.parent() is self:
                return local_maps
            local_maps = local_maps.local_maps()
        return self.element_class(self, local_maps)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to a descent endomorphism Hom")
        return self(
            tuple(
                module_homset(module, module).identity()
                for module in self.domain().local_modules()
            )
        )


_ALGEBRA_GLUING_DATA_CATEGORIES = {}


def _algebra_maps_agree_on_generators(left, right) -> bool:
    if left.domain() is not right.domain() or left.codomain() is not right.codomain():
        return False
    source = left.domain()
    labels = source.algebra_generating_set()
    if not labels.cardinality().is_finite():
        raise TypeError("affine algebra descent currently requires finite algebra framings")
    return all(
        left(source.algebra_generator(label)) == right(source.algebra_generator(label))
        for label in labels
    )


def _exact_algebra_map(source, target, morphism):
    homset = source.Mor(target)
    if (
        isinstance(morphism, Morphism)
        and morphism.domain() is source
        and morphism.codomain() is target
        and morphism.parent() is homset
    ):
        return morphism
    return homset(morphism)


class AlgebraGluingHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return AlgebraGluingHomset


class AlgebraGluingData(CategoryPacketMethods, Category):
    r"""Finite algebra descent data on one represented distinguished affine cover."""

    @staticmethod
    def __classcall__(category_class, cover):
        key = id(cover)
        cached = _ALGEBRA_GLUING_DATA_CATEGORIES.get(key)
        if cached is not None and cached.cover() is cover:
            return cached
        category = typecall(category_class, cover)
        _ALGEBRA_GLUING_DATA_CATEGORIES[key] = category
        return category

    def __init__(self, cover) -> None:
        self._cover = cover
        Category.__init__(self)

    def cover(self):
        return self._cover

    def super_categories(self):
        return [Objects()]

    def __contains__(self, candidate) -> bool:
        return (
            isinstance(candidate, AlgebraGluingDatum)
            and candidate.cover() is self.cover()
        )

    def _repr_object_names(self):
        return f"algebra descent data on {self.cover()}"

    _HomCategory = AlgebraGluingHomCategoryConstruction


class AlgebraGluingDatum(Parent):
    r"""Finite local algebras with algebra isomorphisms satisfying descent."""

    def __init__(self, cover, local_algebras, transitions) -> None:
        self._cover = cover
        self._local_algebras = tuple(local_algebras)
        if len(self._local_algebras) != len(cover.opens()):
            raise ValueError("algebra gluing requires exactly one local algebra on each affine chart")
        for index, algebra in enumerate(self._local_algebras):
            ring = cover.open(index).coordinate_algebra()
            if algebra.base_ring() is not ring:
                raise ValueError("each local algebra must be defined over its chart section ring")
            if algebra not in AlgebrasWithChosenFinitePresentation(ring):
                raise TypeError(
                    "affine algebra descent currently requires local algebras with chosen finite presentations"
                )
            _finite_framing(algebra)

        expected = {
            (left, right)
            for left in range(len(self._local_algebras))
            for right in range(left + 1, len(self._local_algebras))
        }
        supplied = set(transitions)
        if supplied != expected:
            raise ValueError(
                f"algebra gluing requires one transition isomorphism for each pair {sorted(expected)}"
            )
        self._transitions = dict(transitions)
        self._inverse_transitions = {}
        self._restriction_maps = {}
        self._transition_restrictions = {}
        self._compatible_sections = None
        self._sheaf = None
        self._verify_pairwise_transitions()
        self._verify_cocycles()
        self._module_gluing_datum = self._build_underlying_module_datum()
        Parent.__init__(self, category=AlgebraGluingData(cover))

    def cover(self):
        return self._cover

    def ringed_space(self):
        return self.cover().ambient_scheme()

    scheme = ringed_space

    def local_algebras(self):
        return self._local_algebras

    def local_algebra(self, index):
        return self.local_algebras()[int(index)]

    def restricted_algebra(self, chart_index, *intersection_indices):
        chart_index = int(chart_index)
        restricted = self.cover().restrict_algebra(
            self.local_algebra(chart_index),
            chart_index,
            *intersection_indices,
        )
        target = self.cover().intersection(
            chart_index,
            *intersection_indices,
        ).coordinate_algebra()
        if restricted not in Algebras(target):
            raise TypeError("algebra scalar extension did not preserve the algebra structure")
        if restricted not in AlgebrasWithChosenFinitePresentation(target):
            raise TypeError("algebra scalar extension did not preserve the chosen finite presentation")
        _finite_framing(restricted)
        return restricted

    def transition(self, source_index, target_index):
        source_index = int(source_index)
        target_index = int(target_index)
        if source_index == target_index:
            raise ValueError("an algebra transition isomorphism is requested between two distinct charts")
        if source_index < target_index:
            return self._transitions[source_index, target_index]
        key = (source_index, target_index)
        cached = self._inverse_transitions.get(key)
        if cached is not None:
            return cached
        original = self._transitions[target_index, source_index]
        from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
            Isomorphism,
        )

        cached = Isomorphism(original.inverse(), original.forward())
        self._inverse_transitions[key] = cached
        return cached

    def _verify_pairwise_transitions(self) -> None:
        for (left_index, right_index), transition in self._transitions.items():
            if not isinstance(transition, CategoricalIsomorphism):
                raise TypeError("algebra transition data must be represented categorical isomorphisms")
            source = self.restricted_algebra(left_index, left_index, right_index)
            target = self.restricted_algebra(right_index, left_index, right_index)
            forward = transition.forward()
            inverse = transition.inverse()
            if forward.domain() is not source or forward.codomain() is not target:
                raise ValueError("an algebra transition has the wrong overlap endpoints")
            if inverse.domain() is not target or inverse.codomain() is not source:
                raise ValueError("an algebra transition inverse has the wrong overlap endpoints")
            if forward.parent() is not source.Mor(target):
                raise TypeError("an algebra transition forward map must lie in the overlap algebra Hom")
            if inverse.parent() is not target.Mor(source):
                raise TypeError("an algebra transition inverse map must lie in the overlap algebra Hom")
            if not _algebra_maps_agree_on_generators(inverse * forward, source.Mor(source).identity()):
                raise ValueError("the stated algebra transition is not left-invertible on the overlap")
            if not _algebra_maps_agree_on_generators(forward * inverse, target.Mor(target).identity()):
                raise ValueError("the stated algebra transition is not right-invertible on the overlap")

    def restriction_between_intersections(
        self,
        chart_index,
        source_indices,
        target_indices,
    ):
        r"""Return the algebra restriction to a finer represented intersection."""

        chart_index = int(chart_index)
        source_indices = self.cover().intersection_indices(
            chart_index,
            *tuple(source_indices),
        )
        target_indices = self.cover().intersection_indices(
            chart_index,
            *tuple(target_indices),
        )
        if not set(source_indices).issubset(target_indices):
            raise ValueError("algebra restriction requires the target intersection to refine the source")
        key = (chart_index, source_indices, target_indices)
        cached = self._restriction_maps.get(key)
        if cached is not None:
            return cached
        source = self.restricted_algebra(chart_index, *source_indices)
        target = self.restricted_algebra(chart_index, *target_indices)
        if target is source:
            cached = source.Mor(source).identity()
            self._restriction_maps[key] = cached
            return cached
        source_open = self.cover().intersection(source_indices)
        target_open = self.cover().intersection(target_indices)
        ring_map = self.scheme().structure_sheaf().restriction_map(source_open, target_open)
        restricted_target = restrict_algebra_scalars(target, ring_map)
        cached = source.Mor(restricted_target)(
            lambda label: restricted_target(target.algebra_generator(label))
        )
        self._restriction_maps[key] = cached
        return cached

    def restriction_map(self, chart_index, *intersection_indices):
        chart_index = int(chart_index)
        target_indices = self.cover().intersection_indices(
            chart_index,
            *intersection_indices,
        )
        return self.restriction_between_intersections(
            chart_index,
            (chart_index,),
            target_indices,
        )

    def restrict_section_between_intersections(
        self,
        chart_index,
        section,
        source_indices,
        target_indices,
    ):
        source = self.restricted_algebra(chart_index, *tuple(source_indices))
        target = self.restricted_algebra(chart_index, *tuple(target_indices))
        image = self.restriction_between_intersections(
            chart_index,
            source_indices,
            target_indices,
        )(source(section))
        return target(image)

    def transition_on_intersection(
        self,
        source_index,
        target_index,
        *intersection_indices,
    ):
        r"""Restrict an algebra transition to a finer represented intersection."""

        source_index = int(source_index)
        target_index = int(target_index)
        indices = self.cover().intersection_indices(
            source_index,
            target_index,
            *intersection_indices,
        )
        key = (source_index, target_index, indices)
        cached = self._transition_restrictions.get(key)
        if cached is not None:
            return cached
        pair = tuple(sorted((source_index, target_index)))
        transition = self.transition(source_index, target_index).forward()
        if indices == pair:
            self._transition_restrictions[key] = transition
            return transition

        pair_source = self.restricted_algebra(source_index, *pair)
        source = self.restricted_algebra(source_index, *indices)
        target = self.restricted_algebra(target_index, *indices)
        target_restriction = self.restriction_between_intersections(
            target_index,
            pair,
            indices,
        )

        def image(label):
            pair_image = transition(pair_source.algebra_generator(label))
            return target(target_restriction(pair_image))

        cached = source.Mor(target)(image)
        self._transition_restrictions[key] = cached
        return cached

    def _verify_cocycles(self) -> None:
        for left_index, middle_index, right_index in combinations(
            range(len(self.local_algebras())),
            3,
        ):
            indices = (left_index, middle_index, right_index)
            left_middle = self.transition_on_intersection(
                left_index,
                middle_index,
                *indices,
            )
            middle_right = self.transition_on_intersection(
                middle_index,
                right_index,
                *indices,
            )
            left_right = self.transition_on_intersection(
                left_index,
                right_index,
                *indices,
            )
            if not _algebra_maps_agree_on_generators(
                middle_right * left_middle,
                left_right,
            ):
                raise ValueError("algebra transition isomorphisms fail the cocycle condition on a triple overlap")

    def _build_underlying_module_datum(self):
        from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
            Isomorphism,
        )

        transitions = {}
        for (left_index, right_index), transition in self._transitions.items():
            ring = self.cover().overlap(left_index, right_index).coordinate_algebra()
            forget = algebra_underlying_module_functor(ring)
            transitions[left_index, right_index] = Isomorphism(
                forget(transition.forward()),
                forget(transition.inverse()),
            )
        return ModuleGluingDatum(
            self.cover(),
            self.local_algebras(),
            transitions,
        )

    def underlying_module_datum(self):
        return self._module_gluing_datum

    def compatible_sections(self):
        if self._compatible_sections is None:
            self._compatible_sections = CompatibleLocalAlgebraSections(self)
        return self._compatible_sections

    def sheaf(self):
        if self._sheaf is None:
            self._sheaf = GluedAlgebraSheaf(self)
        return self._sheaf

    def Mor(self, target):
        return self.category().Mor(self, target)

    def _repr_(self):
        return f"Algebra gluing datum on {self.cover()}"


class AlgebraGluingMorphism(Morphism):
    r"""A compatible family of local algebra morphisms between descent data."""

    def __init__(self, parent, local_maps) -> None:
        Morphism.__init__(self, parent)
        local_maps = tuple(local_maps)
        if len(local_maps) != len(self.domain().local_algebras()):
            raise ValueError("an algebra descent morphism requires one local map on each affine chart")
        self._local_maps = tuple(
            _exact_algebra_map(
                self.domain().local_algebra(index),
                self.codomain().local_algebra(index),
                local_map,
            )
            for index, local_map in enumerate(local_maps)
        )
        module_maps = tuple(
            algebra_underlying_module_functor(
                self.cover().open(index).coordinate_algebra()
            )(local_map)
            for index, local_map in enumerate(self._local_maps)
        )
        self._underlying_module_morphism = self.domain().underlying_module_datum().Mor(
            self.codomain().underlying_module_datum()
        )(module_maps)
        self._global_sections_map = None

    def cover(self):
        return self.domain().cover()

    def local_maps(self):
        return self._local_maps

    def local_map(self, index):
        return self.local_maps()[int(index)]

    def underlying_module_morphism(self):
        return self._underlying_module_morphism

    def global_sections_map(self):
        if self._global_sections_map is None:
            source = self.domain().compatible_sections()
            target = self.codomain().compatible_sections()

            def image(section):
                section = source(section)
                return target(
                    tuple(
                        self.local_map(index)(section.component(index))
                        for index in range(len(self.local_maps()))
                    )
                )

            set_map = SetMorphism(Sets().Mor(source, target), image)
            self._global_sections_map = source.Mor(target)(set_map)
        return self._global_sections_map

    def then(self, other):
        if other.domain() is not self.codomain():
            raise ValueError("the first algebra descent-morphism target must equal the second source")
        return other * self

    def __mul__(self, other):
        if not isinstance(other, AlgebraGluingMorphism):
            return NotImplemented
        if other.codomain() is not self.domain():
            return NotImplemented
        return other.domain().Mor(self.codomain())(
            tuple(
                self.local_map(index) * other.local_map(index)
                for index in range(len(self.local_maps()))
            )
        )

    def _repr_(self):
        return f"Algebra descent morphism from {self.domain()} to {self.codomain()}"


class AlgebraGluingHomset(CategoricalHomset):
    Element = AlgebraGluingMorphism

    def __init__(self, family, domain, codomain) -> None:
        if domain.cover() is not codomain.cover():
            raise ValueError("an algebra descent Hom requires one common affine cover")
        CategoricalHomset.__init__(self, family, domain, codomain)

    def _element_constructor_(self, local_maps):
        if isinstance(local_maps, AlgebraGluingMorphism):
            if local_maps.domain() is not self.domain() or local_maps.codomain() is not self.codomain():
                raise ValueError("the algebra descent morphism has the wrong endpoints")
            if local_maps.parent() is self:
                return local_maps
            local_maps = local_maps.local_maps()
        return self.element_class(self, local_maps)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to an algebra descent endomorphism Hom")
        return self(
            tuple(
                algebra.Mor(algebra).identity()
                for algebra in self.domain().local_algebras()
            )
        )


class CompatibleLocalSectionElement(ModuleElement):
    def __init__(self, parent, components) -> None:
        ModuleElement.__init__(self, parent)
        self._components = tuple(components)

    def components(self):
        return self._components

    def component(self, index):
        return self.components()[int(index)]

    def _add_(self, other):
        return self.parent()(
            tuple(
                left + right
                for left, right in zip(self.components(), other.components(), strict=True)
            )
        )

    def _neg_(self):
        return self.parent()(tuple(-component for component in self.components()))

    def _lmul_(self, scalar):
        return self.parent().scalar_multiple(scalar, self)

    def _acted_upon_(self, actor, self_on_left):
        try:
            scalar = self.parent().base_ring()(actor)
        except (TypeError, ValueError):
            return None
        return self.parent().scalar_multiple(scalar, self)

    def _richcmp_(self, other, op):
        if op not in (op_EQ, op_NE):
            return NotImplemented
        equal = (
            isinstance(other, CompatibleLocalSectionElement)
            and other.parent() is self.parent()
            and all(
                left == right
                for left, right in zip(self.components(), other.components(), strict=True)
            )
        )
        return equal if op == op_EQ else not equal

    def _repr_(self):
        return f"compatible local sections {self.components()}"


class CompatibleLocalSectionsModule(Parent):
    r"""The equalizer module of local sections satisfying the descent equations."""

    Element = CompatibleLocalSectionElement

    def __init__(self, gluing_datum) -> None:
        self._gluing_datum = gluing_datum
        self._preamble_base_ring = gluing_datum.scheme().coordinate_algebra()
        Parent.__init__(self, category=Modules(self._preamble_base_ring))

    def gluing_datum(self):
        return self._gluing_datum

    def base_ring(self):
        return self._preamble_base_ring

    def base(self):
        return self.base_ring()

    def _element_constructor_(self, value):
        if isinstance(value, CompatibleLocalSectionElement) and value.parent() is self:
            return value
        components = tuple(value)
        datum = self.gluing_datum()
        if len(components) != len(datum.local_modules()):
            raise ValueError("a compatible section tuple needs one component on each affine chart")
        components = tuple(
            module(component)
            for module, component in zip(datum.local_modules(), components, strict=True)
        )
        for left_index, right_index in combinations(range(len(components)), 2):
            left = datum.restrict_section(
                left_index,
                components[left_index],
                left_index,
                right_index,
            )
            right = datum.restrict_section(
                right_index,
                components[right_index],
                left_index,
                right_index,
            )
            transition = datum.transition(left_index, right_index).forward()
            if transition(left) != right:
                raise ValueError("the local sections do not agree under the overlap transition")
        return self.element_class(self, components)

    def __call__(self, value):
        return self._element_constructor_(value)

    def __contains__(self, value) -> bool:
        return isinstance(value, CompatibleLocalSectionElement) and value.parent() is self

    def zero(self):
        return self(tuple(module.zero() for module in self.gluing_datum().local_modules()))

    def scalar_multiple(self, scalar, section):
        datum = self.gluing_datum()
        scalar = self.base_ring()(scalar)
        section = self(section)
        structure_sheaf = datum.scheme().structure_sheaf()
        components = []
        for index, module in enumerate(datum.local_modules()):
            local_scalar = structure_sheaf.restriction_map(
                datum.scheme(),
                datum.cover().open(index),
            )(scalar)
            components.append(module.scalar_multiple(local_scalar, section.component(index)))
        return self(tuple(components))

    def an_element(self):
        return self.zero()

    def _repr_(self):
        return f"Compatible local sections of {self.gluing_datum()}"


class CompatibleLocalAlgebraSectionElement(CompatibleLocalSectionElement):
    def _mul_(self, other):
        return self.parent().multiply(self, other)


class CompatibleLocalAlgebraSections(CompatibleLocalSectionsModule):
    r"""The ambient-ring algebra of compatible local algebra sections.

    The equalizer module need not carry a selected finite framing.  Its unit
    and multiplication are nevertheless exact componentwise operations; a
    represented tensor-product multiplication morphism is only available when
    the module layer can materialize that tensor product.
    """

    Element = CompatibleLocalAlgebraSectionElement

    def __init__(self, gluing_datum) -> None:
        self._algebra_gluing_datum = gluing_datum
        self._gluing_datum = gluing_datum.underlying_module_datum()
        self._preamble_base_ring = gluing_datum.scheme().coordinate_algebra()
        self._preamble_algebra_base_ring = self._preamble_base_ring
        self._preamble_is_commutative = all(
            algebra in CommutativeAlgebras(algebra.base_ring())
            for algebra in gluing_datum.local_algebras()
        )
        category = (
            CommutativeAlgebras(self._preamble_base_ring)
            if self._preamble_is_commutative
            else Algebras(self._preamble_base_ring)
        )
        Parent.__init__(self, category=category)

    def algebra_gluing_datum(self):
        return self._algebra_gluing_datum

    def is_commutative(self) -> bool:
        return self._preamble_is_commutative

    def one(self):
        return self(
            tuple(
                algebra.one()
                for algebra in self.algebra_gluing_datum().local_algebras()
            )
        )

    def multiply(self, left, right):
        left = self(left)
        right = self(right)
        return self(
            tuple(
                left_component * right_component
                for left_component, right_component in zip(
                    left.components(),
                    right.components(),
                    strict=True,
                )
            )
        )

    def _repr_(self):
        return f"Compatible local algebra sections of {self.algebra_gluing_datum()}"


class GluedModuleSheaf(SageObject):
    r"""The module sheaf represented by one finite affine descent datum."""

    def __init__(self, gluing_datum) -> None:
        self._gluing_datum = gluing_datum

    def gluing_datum(self):
        return self._gluing_datum

    def ringed_space(self):
        return self.gluing_datum().scheme()

    scheme = ringed_space

    def cover(self):
        return self.gluing_datum().cover()

    def sections_on_chart(self, index):
        return self.gluing_datum().local_module(index)

    def sections_on_intersection(self, chart_index, *intersection_indices):
        return self.gluing_datum().restricted_module(
            chart_index,
            *intersection_indices,
        )

    def restriction_map(self, chart_index, *intersection_indices):
        return self.gluing_datum().restriction_map(chart_index, *intersection_indices)

    def restriction_between_intersections(
        self,
        chart_index,
        source_indices,
        target_indices,
    ):
        return self.gluing_datum().restriction_between_intersections(
            chart_index,
            source_indices,
            target_indices,
        )

    def transition(self, source_index, target_index, *intersection_indices):
        return self.gluing_datum().transition_on_intersection(
            source_index,
            target_index,
            *intersection_indices,
        )

    def global_sections(self):
        return self.gluing_datum().compatible_sections()

    sections = global_sections

    def _repr_(self):
        return f"Glued module sheaf on {self.scheme()} from {self.cover()}"


class GluedAlgebraSheaf(SageObject):
    r"""The algebra sheaf represented by finite affine algebra descent data."""

    def __init__(self, gluing_datum) -> None:
        self._gluing_datum = gluing_datum

    def gluing_datum(self):
        return self._gluing_datum

    def ringed_space(self):
        return self.gluing_datum().scheme()

    scheme = ringed_space

    def cover(self):
        return self.gluing_datum().cover()

    def sections_on_chart(self, index):
        return self.gluing_datum().local_algebra(index)

    def sections_on_intersection(self, chart_index, *intersection_indices):
        return self.gluing_datum().restricted_algebra(
            chart_index,
            *intersection_indices,
        )

    def restriction_map(self, chart_index, *intersection_indices):
        return self.gluing_datum().restriction_map(chart_index, *intersection_indices)

    def restriction_between_intersections(
        self,
        chart_index,
        source_indices,
        target_indices,
    ):
        return self.gluing_datum().restriction_between_intersections(
            chart_index,
            source_indices,
            target_indices,
        )

    def transition(self, source_index, target_index, *intersection_indices):
        return self.gluing_datum().transition_on_intersection(
            source_index,
            target_index,
            *intersection_indices,
        )

    def global_sections(self):
        return self.gluing_datum().compatible_sections()

    sections = global_sections

    def underlying_module_sheaf(self):
        return self.gluing_datum().underlying_module_datum().sheaf()

    def _repr_(self):
        return f"Glued algebra sheaf on {self.scheme()} from {self.cover()}"


__all__ = [
    "AlgebraGluingData",
    "AlgebraGluingDatum",
    "AlgebraGluingHomset",
    "AlgebraGluingMorphism",
    "CompatibleLocalAlgebraSections",
    "CompatibleLocalSectionsModule",
    "GluedAlgebraSheaf",
    "GluedModuleSheaf",
    "ModuleGluingData",
    "ModuleGluingDatum",
    "ModuleGluingHomset",
    "ModuleGluingMorphism",
]
