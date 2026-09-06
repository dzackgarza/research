r"""Invertible sheaves represented by rank-one affine module descent data."""

from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    Isomorphism,
)
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    FreeModule,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
    module_homset,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    FinitelyGeneratedFreeModules,
)
from dzack_research.preamble.categories.schemes.gluing import ModuleGluingDatum


def _rank_one_generator(module):
    labels = module.module_generating_set()
    if not labels.cardinality().is_finite() or int(labels.cardinality()) != 1:
        raise TypeError("an invertible sheaf requires rank-one local modules")
    return module.module_generator(next(iter(labels)))


def _rank_one_transition(source, target, unit):
    unit = target.base_ring()(unit)
    if not unit.is_unit():
        raise ValueError("an invertible-sheaf transition scalar must be a unit")
    source_generator = _rank_one_generator(source)
    target_generator = _rank_one_generator(target)
    forward = module_homset(source, target)(
        lambda _label: target.scalar_multiple(unit, target_generator)
    )
    inverse_unit = source.base_ring()(unit.inverse_of_unit())
    inverse = module_homset(target, source)(
        lambda _label: source.scalar_multiple(inverse_unit, source_generator)
    )
    return Isomorphism(forward, inverse)


class InvertibleSheaf(SageObject):
    r"""A line bundle represented by rank-one free descent on one affine cover."""

    def __init__(self, gluing_datum) -> None:
        if not isinstance(gluing_datum, ModuleGluingDatum):
            raise TypeError("an invertible sheaf requires represented module descent data")
        self._gluing_datum = gluing_datum
        self._transition_units = {}
        for module in gluing_datum.local_modules():
            ring = module.base_ring()
            if module not in FinitelyGeneratedFreeModules(ring) or int(module.module_rank()) != 1:
                raise TypeError(
                    "an invertible sheaf requires a rank-one finite free module on every chart"
                )
        for left in range(len(gluing_datum.local_modules())):
            for right in range(left + 1, len(gluing_datum.local_modules())):
                self._transition_units[left, right] = self._extract_transition_unit(
                    left,
                    right,
                )

    def gluing_datum(self):
        return self._gluing_datum

    def cover(self):
        return self.gluing_datum().cover()

    def scheme(self):
        return self.gluing_datum().scheme()

    ringed_space = scheme

    def sheaf(self):
        return self.gluing_datum().sheaf()

    def local_module(self, index):
        return self.gluing_datum().local_module(index)

    def local_trivialization(self, index):
        r"""Return the literal rank-one free chart module trivializing this sheaf."""

        module = self.local_module(index)
        identity = module_homset(module, module).identity()
        return Isomorphism(identity, identity)

    def _extract_transition_unit(self, source_index, target_index):
        transition = self.gluing_datum().transition(source_index, target_index).forward()
        source = transition.domain()
        target = transition.codomain()
        source_generator = _rank_one_generator(source)
        target_labels = target.module_generating_set()
        target_label = next(iter(target_labels))
        coefficients = module_coefficients(transition(source_generator), target)
        unit = (
            coefficients[target_label]
            if target_label in coefficients
            else target.base_ring().zero()
        )
        if not unit.is_unit():
            raise ValueError(
                "a rank-one descent transition must multiply the local basis by a unit"
            )
        return unit

    def transition_unit(self, source_index, target_index):
        r"""Return the unit ``u_ij`` with ``e_i |-> u_ij e_j`` on the overlap."""

        source_index = int(source_index)
        target_index = int(target_index)
        if source_index == target_index:
            raise ValueError("a transition unit is attached to two distinct charts")
        if source_index < target_index:
            return self._transition_units[source_index, target_index]
        return self._transition_units[target_index, source_index].inverse_of_unit()

    def global_sections(self):
        return self.gluing_datum().compatible_sections()

    sections = global_sections

    def morphism_to(self, target, local_maps):
        r"""Return the descent morphism represented by the supplied chart maps."""

        if not isinstance(target, InvertibleSheaf):
            raise TypeError("an invertible-sheaf morphism requires an invertible-sheaf target")
        if target.cover() is not self.cover():
            raise ValueError("invertible-sheaf descent morphisms require one affine cover")
        return self.gluing_datum().Mor(target.gluing_datum())(local_maps)

    @classmethod
    def _from_transition_units(cls, cover, transition_units):
        local_modules = tuple(
            FreeModule(open_subscheme.coordinate_algebra(), 1)
            for open_subscheme in cover.opens()
        )
        transitions = {}
        for left in range(len(local_modules)):
            for right in range(left + 1, len(local_modules)):
                source = cover.restrict_module(local_modules[left], left, right)
                target = cover.restrict_module(local_modules[right], right, left)
                transitions[left, right] = _rank_one_transition(
                    source,
                    target,
                    transition_units[left, right],
                )
        return cls(cover.glue_modules(local_modules, transitions))

    @classmethod
    def trivial(cls, cover):
        r"""Return ``O_X`` represented as the rank-one trivial bundle on ``cover``."""

        units = {
            (left, right): cover.overlap(left, right).coordinate_algebra().one()
            for left in range(len(cover.opens()))
            for right in range(left + 1, len(cover.opens()))
        }
        return cls._from_transition_units(cover, units)

    def tensor_product(self, other):
        r"""Tensor two line bundles by multiplying their transition units."""

        if not isinstance(other, InvertibleSheaf):
            raise TypeError("line-bundle tensor product requires two invertible sheaves")
        if other.cover() is not self.cover():
            raise ValueError("line-bundle tensor product currently requires one affine cover")
        units = {
            (left, right): self.transition_unit(left, right)
            * other.transition_unit(left, right)
            for left in range(len(self.cover().opens()))
            for right in range(left + 1, len(self.cover().opens()))
        }
        return self._from_transition_units(self.cover(), units)

    def tensor_power(self, exponent):
        r"""Return ``self^tensor exponent`` using powers of the transition units."""

        exponent = int(exponent)
        units = {}
        for left in range(len(self.cover().opens())):
            for right in range(left + 1, len(self.cover().opens())):
                unit = self.transition_unit(left, right)
                units[left, right] = (
                    unit**exponent
                    if exponent >= 0
                    else unit.inverse_of_unit() ** (-exponent)
                )
        return self._from_transition_units(self.cover(), units)

    def dual(self):
        r"""Return the dual line bundle, with transition units ``u_ij^{-1}``."""

        return self.tensor_power(-1)

    def _repr_(self):
        return f"Invertible sheaf on {self.scheme()} trivialized by {self.cover()}"


def TrivialInvertibleSheaf(cover):
    return InvertibleSheaf.trivial(cover)


__all__ = ["InvertibleSheaf", "TrivialInvertibleSheaf"]
