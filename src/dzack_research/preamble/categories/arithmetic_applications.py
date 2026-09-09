r"""Owned assembly of the three arithmetic lattice research constructions.

The point of this module is not to introduce new arithmetic algorithms.  It
collects the maps already owned by the lattice, cusp, gluing and equivariant
layers into the three research objects named by the repository plan, so their
applications retain the actual inclusions, quotient maps, arithmetic groups
and transporters instead of being reconstructed ad hoc in notebooks.
"""

from sage.misc.cachefunc import cached_method
from sage.structure.sage_object import SageObject

from dzack_research.preamble.catalogue import Involutions, NamedLattices
from dzack_research.preamble.categories.isotropic_orbits import (
    cusps,
    tits_building_incidence,
)


class LorentzianE10Application(SageObject):
    r"""The cusp package for the Lorentzian lattice ``U + E8(-1)``."""

    def lattice(self):
        return NamedLattices.E10

    def orthogonal_group(self):
        return self.lattice().O()

    def positive_cone_subgroup(self):
        return self.lattice().positive_cone_subgroup()

    @cached_method
    def cusp(self):
        return cusps(self.lattice(), 1)[0]

    def isotropic_line(self):
        return self.cusp().representative()

    @cached_method
    def reduction_lattice(self):
        return self.isotropic_line().isotropic_reduction()

    def parabolic_subgroup(self):
        return self.reduction_lattice().parabolic_subgroup()

    def unipotent_radical(self):
        return self.reduction_lattice().unipotent_kernel()

    def levi_action(self):
        r"""Return the actual map ``P_I -> O(I^perp/I)``."""
        return self.reduction_lattice().levi_action()

    def lift_reduction_isometry(self, isometry):
        r"""Lift a represented reduction isometry through the retained splitting."""
        return self.reduction_lattice().lift_isometry(isometry)


class EnriquesHigherWittApplication(SageObject):
    r"""The line/plane boundary arithmetic of ``T_En`` with glue-compatible group."""

    @cached_method
    def primitive_extension(self):
        return Involutions.I_En.primitive_extension()

    def lattice(self):
        return self.primitive_extension().coinvariant.inclusion().domain()

    @cached_method
    def arithmetic_group(self):
        r"""The glue-compatible finite-character preimage in ``O(T_En)``."""
        return self.primitive_extension().coinvariant_extension_subgroup()

    @cached_method
    def line_cusps(self):
        return self.arithmetic_group().cusps(1)

    @cached_method
    def plane_cusps(self):
        return self.arithmetic_group().cusps(2)

    @cached_method
    def tits_building_incidence(self):
        return self.arithmetic_group().tits_building_incidence()

    def full_orthogonal_line_cusps(self):
        return cusps(self.lattice(), 1)

    def full_orthogonal_plane_cusps(self):
        return cusps(self.lattice(), 2)

    def full_orthogonal_tits_building_incidence(self):
        return tits_building_incidence(self.lattice())


class EnriquesEquivariantK3Application(SageObject):
    r"""The K3 lattice with the Enriques involution and a chosen invariant polarization."""

    def lattice(self):
        return NamedLattices.LK3

    def involution(self):
        return Involutions.I_En

    @cached_method
    def primitive_extension(self):
        return self.involution().primitive_extension()

    def invariant_lattice(self):
        return self.primitive_extension().invariant

    def anti_invariant_lattice(self):
        return self.primitive_extension().coinvariant

    def centralizer_group(self):
        return self.primitive_extension().centralizer_group()

    @cached_method
    def polarization(self):
        r"""Return the selected non-isotropic invariant vector used by the application."""
        invariant = self.invariant_lattice()
        inclusion = invariant.inclusion()
        labels = invariant.module_generating_set()
        if len(labels) < 2:
            raise ArithmeticError("the represented invariant lattice has no two-generator polarization specimen")
        vector = inclusion(invariant.module_generator(labels[0])) + inclusion(
            invariant.module_generator(labels[1])
        )
        if vector.q() == 0 or self.involution()(vector) != vector:
            raise ArithmeticError("the selected polarization is not a non-isotropic invariant vector")
        return vector

    @cached_method
    def polarized_equivariant_lattice(self):
        return self.lattice().with_isometry(self.involution()).polarized(
            self.polarization()
        )

    def polarization_stabilizer(self):
        return self.polarized_equivariant_lattice().polarization_stabilizer()

    def polarized_group(self):
        r"""Return ``Z_{O(L_K3)}(iota) cap Stab(h)``."""
        return self.polarized_equivariant_lattice().polarized_group()

    @cached_method
    def anti_invariant_arithmetic_group(self):
        return self.primitive_extension().coinvariant_extension_subgroup()

    def anti_invariant_line_cusps(self):
        return self.anti_invariant_arithmetic_group().cusps(1)

    def anti_invariant_plane_cusps(self):
        return self.anti_invariant_arithmetic_group().cusps(2)

    @cached_method
    def anti_invariant_tits_building_incidence(self):
        r"""Return the glue-compatible line/plane incidence in the anti-invariant lattice.

        The acting group is the arithmetic subgroup inherited from the integral
        K3 gluing, not the full orthogonal group of ``T_En``.  Consequently the
        returned incidence records retain transporters in that same arithmetic
        subgroup.
        """
        return self.anti_invariant_arithmetic_group().tits_building_incidence()


def lorentzian_e10_application():
    return LorentzianE10Application()


def enriques_higher_witt_application():
    return EnriquesHigherWittApplication()


def enriques_equivariant_k3_application():
    return EnriquesEquivariantK3Application()


__all__ = [
    "EnriquesEquivariantK3Application",
    "EnriquesHigherWittApplication",
    "LorentzianE10Application",
    "enriques_equivariant_k3_application",
    "enriques_higher_witt_application",
    "lorentzian_e10_application",
]
