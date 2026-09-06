r"""Descent data for modules on represented distinguished affine covers."""

from itertools import combinations

from sage.structure.element import ModuleElement
from sage.structure.parent import Parent
from sage.structure.richcmp import op_EQ, op_NE
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalIsomorphism,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
    module_homset,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    Modules,
    restrict_scalars,
)


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


class ModuleGluingDatum(SageObject):
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

    def _repr_(self):
        return f"Module gluing datum on {self.cover()}"


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


def _rank_one_transition(source, target, unit):
    r"""``m |-> u m`` between two rank-one free modules on one overlap.

    A unit of the overlap's section ring gives an isomorphism because its
    inverse gives the inverse map; this is the only shape a transition of
    trivialized invertible sheaves takes.
    """
    from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
        Isomorphism,
    )

    source_generator = source.module_generator(next(iter(_finite_framing(source))))
    target_generator = target.module_generator(next(iter(_finite_framing(target))))
    forward = module_homset(source, target)(
        lambda _label: target.scalar_multiple(unit, target_generator)
    )
    inverse = module_homset(target, source)(
        lambda _label: source.scalar_multiple(unit.inverse_of_unit(), source_generator)
    )
    return Isomorphism(forward, inverse)


class InvertibleModuleSheaf(GluedModuleSheaf):
    r"""A rank-one locally free sheaf given by trivializations and transition units.

    On a distinguished affine cover ``{U_i}`` an invertible sheaf that is
    trivial on every chart is the free rank-one module on each chart glued by
    units ``u_ij`` of ``O(U_ij)``, and the cocycle condition on the transition
    isomorphisms is ``u_ik = u_jk u_ij`` on the triple overlaps: the datum is
    a Cech 1-cocycle with values in ``O_X^*`` and the sheaf is its class
    (Stacks, Tag 01X0).

    Tensoring two such sheaves multiplies their cocycles, so the tensor
    powers and the dual are the same cover carrying the units raised to an
    integer power, negative powers included.  That is exactly why the
    isomorphism classes form a group.
    """

    def __init__(self, gluing_datum, transition_units) -> None:
        super().__init__(gluing_datum)
        self._transition_units = dict(transition_units)

    def transition_units(self):
        r"""The 1-cocycle ``{u_ij}``, indexed by the pairs ``i < j``."""
        return dict(self._transition_units)

    def transition_unit(self, left_index, right_index):
        r"""``u_ij in O(U_ij)^*``, the unit the transition multiplies by."""
        left_index, right_index = int(left_index), int(right_index)
        if left_index < right_index:
            return self._transition_units[left_index, right_index]
        return self._transition_units[right_index, left_index].inverse_of_unit()

    def tensor_product(self, other):
        r"""``L tensor L'`` on the same cover: the cocycles multiply."""
        assert other.cover() is self.cover(), (
            "invertible sheaves are tensored on one cover; refine both to a common one first"
        )
        return glue_invertible_module(
            self.cover(),
            {
                pair: unit * other.transition_unit(*pair)
                for pair, unit in self._transition_units.items()
            },
        )

    def tensor_power(self, exponent):
        r"""``L^{tensor n}`` for any integer ``n``: the cocycle to the ``n``-th power.

        ``n = 0`` is the structure sheaf, whose cocycle is constant one, and
        a negative power inverts each unit, which is the dual sheaf.
        """
        exponent = int(exponent)
        return glue_invertible_module(
            self.cover(),
            {
                pair: (
                    unit**exponent
                    if exponent >= 0
                    else unit.inverse_of_unit() ** (-exponent)
                )
                for pair, unit in self._transition_units.items()
            },
        )

    def dual_sheaf(self):
        r"""``L^{-1} = Hom_{O_X}(L, O_X)``, the inverse of ``L`` in the Picard group."""
        return self.tensor_power(-1)

    def _repr_(self):
        return f"Invertible sheaf on {self.scheme()} from {self.cover()}"


def glue_invertible_module(cover, transition_units):
    r"""Glue the trivial rank-one sheaves on ``cover`` by a 1-cocycle of units."""
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
        FreeModule,
    )

    chart_count = len(cover.opens())
    units = {
        (int(left), int(right)): unit
        for (left, right), unit in transition_units.items()
    }
    expected = {
        (left, right)
        for left in range(chart_count)
        for right in range(left + 1, chart_count)
    }
    assert set(units) == expected, (
        f"an invertible sheaf on this cover needs one transition unit for each pair {sorted(expected)}"
    )
    local_modules = tuple(
        FreeModule(cover.open(index).coordinate_algebra(), 1)
        for index in range(chart_count)
    )
    transitions = {}
    for (left, right), unit in units.items():
        overlap_algebra = cover.intersection(left, right).coordinate_algebra()
        assert unit.parent() is overlap_algebra, (
            f"the transition unit for charts {left} and {right} must live on their overlap"
        )
        transitions[left, right] = _rank_one_transition(
            cover.restrict_module(local_modules[left], left, right),
            cover.restrict_module(local_modules[right], right, left),
            unit,
        )
    datum = cover.glue_modules(local_modules, transitions)
    return InvertibleModuleSheaf(datum, units)


__all__ = [
    "CompatibleLocalSectionsModule",
    "GluedModuleSheaf",
    "InvertibleModuleSheaf",
    "glue_invertible_module",
    "ModuleGluingDatum",
]
