r"""Higher direct images and monodromy for a sourced Legendre degeneration.

The selected family is the projective Legendre family

``E_t : y^2 z = x(x-z)(x-tz)``

over ``Spec QQ[t]``.  Its fibers at ``t=0`` and ``t=1`` are singular.  On the
analytic punctured disc ``0 < |t| < 3/4`` the family is smooth and proper, so
``R^1 pi_* ZZ`` is a rank-two integral local system and topological proper base
change identifies its stalk with ``H^1(E_t,ZZ)``.

For a positively oriented loop around ``t=0`` the sourced homology matrix is
``M_0=[[1,0],[-2,1]]`` in the standard symplectic basis.  The local system
here is cohomological, so in the dual basis its action is
``(M_0^{-1})^T=[[1,2],[0,1]]``.

The local system retains that basis convention and acts on the actual rank-two
formed module whose alternating pairing is the cup/intersection pairing.  Nearby/vanishing cycles are deliberately not inferred from proper
base change: the singular fiber is retained, but no specialization map is
created without its own comparison theorem.
"""

from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.functors.group_actions import GroupActionFunctor
from dzack_research.preamble.categories.group.groups import OwnedGroups
from dzack_research.preamble.categories.manifolds import ComplexManifolds
from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
    FormModules,
)
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.schemes.complete_intersections import (
    ProjectiveCompleteIntersections,
)
from dzack_research.preamble.categories.schemes.ringed_spaces import SheafObjects
from dzack_research.preamble.categories.schemes.schemes import (
    ProjectiveSpaces,
    Schemes,
)


class PointedAnalyticFundamentalGroup(SageObject):
    r"""A represented pointed ``pi_1`` with its actual group and base point."""

    def __init__(self, space, base_point, group, generator) -> None:
        if base_point.manifold() is not space:
            raise ValueError("a pointed fundamental group requires a point of its space")
        if generator.parent() is not group:
            raise ValueError("the loop generator belongs to the selected fundamental group")
        self._space = space
        self._base_point = base_point
        self._group = group
        self._generator = generator

    def space(self):
        return self._space

    def base_point(self):
        return self._base_point

    def group(self):
        return self._group

    def positive_loop_generator(self):
        return self._generator

    def _repr_(self) -> str:
        return f"pi_1({self.space()}, {self.base_point()}) = {self.group()}"



class IntegralLocalSystem(Parent):
    r"""A pointed integral local system represented by a ``pi_1`` action.

    On a connected pointed space, local systems of finitely generated modules
    are equivalent to representations of the pointed fundamental group.  This
    object retains both sides of that equivalence: the actual stalk module and
    the actual action functor ``B pi_1 -> FormMod_ZZ``.
    """

    def __init__(self, base, pointed_fundamental_group, stalk_module, action_functor) -> None:
        if pointed_fundamental_group.space() is not base:
            raise ValueError("the local system fundamental group belongs to a different base")
        if action_functor.group() is not pointed_fundamental_group.group():
            raise ValueError("the monodromy action has the wrong fundamental group")
        if action_functor.underlying_object() is not stalk_module:
            raise ValueError("the monodromy action must select the local-system stalk")
        self._base = base
        self._pointed_fundamental_group = pointed_fundamental_group
        self._stalk_module = stalk_module
        self._action_functor = action_functor
        Parent.__init__(self, category=SheafObjects(base))

    def base_space(self):
        return self._base

    def base_point(self):
        return self._pointed_fundamental_group.base_point()

    def pointed_fundamental_group(self):
        return self._pointed_fundamental_group

    def stalk(self, point):
        assert point is self.base_point(), (
            "this selected local-system model materializes the stalk at its chosen base point"
        )
        return self._stalk_module

    def monodromy_representation(self):
        return self._action_functor

    def is_locally_constant(self) -> bool:
        return True

    def rank(self):
        return self._stalk_module.module_rank()

    def monodromy_of(self, loop):
        group = self.pointed_fundamental_group().group()
        loop = group(loop)
        classifying = self.monodromy_representation().domain()
        point = classifying.an_object()
        return self.monodromy_representation()(classifying.Mor(point, point)(loop))

    def _repr_(self) -> str:
        return f"Integral local system of rank {self.rank()} on {self.base_space()} with stalk {self.stalk()}"



class HigherDirectImageSheaf(Parent):
    r"""A selected ``R^i pi_* ZZ`` with its smooth-stratum local system."""

    def __init__(self, family_data, degree, smooth_stratum, local_system) -> None:
        self._family_data = family_data
        self._degree = int(degree)
        self._smooth_stratum = smooth_stratum
        self._local_system = local_system
        if local_system.base_space() is not smooth_stratum:
            raise ValueError("the higher-direct-image restriction lives on the selected smooth stratum")
        Parent.__init__(self, category=SheafObjects(smooth_stratum))

    def family_data(self):
        return self._family_data

    def family_morphism(self):
        return self.family_data().family_morphism()

    def cohomological_degree(self):
        return self._degree

    def coefficients(self):
        return _own_ring(SageZZ)

    def smooth_stratum(self):
        return self._smooth_stratum

    def restriction_to_smooth_stratum(self):
        return self._local_system

    def stalk(self, point):
        return self.restriction_to_smooth_stratum().stalk(point)

    def stalk_to_fiber_comparison(self, point):
        r"""Topological proper-base-change comparison at the selected smooth point."""
        assert point is self.restriction_to_smooth_stratum().base_point(), (
            "the selected proper-base-change comparison is materialized at the chosen smooth base point"
        )
        if not self.family_data().proper_base_change_hypotheses_hold(point):
            raise ValueError("topological proper base change hypotheses do not hold at this point")
        stalk = self.stalk(point)
        fiber = self.family_data().fiber_cohomology(point)
        forward = stalk.Mor(fiber).identity() if stalk is fiber else stalk.Mor(fiber)(
            stalk.module_category().Mor(stalk, fiber)(
                {
                    label: fiber.module_generator(label)
                    for label in stalk.module_generating_set()
                }
            )
        )
        inverse = fiber.Mor(stalk).identity() if stalk is fiber else fiber.Mor(stalk)(
            fiber.module_category().Mor(fiber, stalk)(
                {
                    label: stalk.module_generator(label)
                    for label in fiber.module_generating_set()
                }
            )
        )
        return stalk.module_category().Core().Mor(stalk, fiber)(forward, inverse)

    def _repr_(self) -> str:
        return f"R^{self.cohomological_degree()} of {self.family_morphism()} on {self.smooth_stratum()}"



class LegendreMonodromyFamily(SageObject):
    r"""The Legendre degeneration together with ``R^1 pi_* ZZ`` on a punctured disc."""

    def __init__(self) -> None:
        rationals = _own_ring(SageQQ)
        integers = _own_ring(SageZZ)
        parameter = rationals.polynomial_ring("t")
        t = parameter.algebra_generator("t")
        ambient = ProjectiveSpaces(parameter)(2, names=("x", "y", "z"))
        section_ring = ambient.O(3).global_sections().homogeneous_coordinate_ring()
        x = section_ring.algebra_generator("x")
        y = section_ring.algebra_generator("y")
        z = section_ring.algebra_generator("z")
        scalar_t = section_ring.algebra_structure_morphism()(t)
        equation = y**2 * z - x * (x - z) * (x - scalar_t * z)
        family = ProjectiveCompleteIntersections(ambient.scheme_base_ring())(ambient.closed_subscheme(equation))

        at_zero = parameter.Mor(rationals)({"t": rationals.zero()})
        at_half = parameter.Mor(rationals)({"t": rationals(1) / rationals(2)})
        singular_fiber = family.base_change(at_zero)
        smooth_fiber = family.base_change(at_half)

        analytic_line = ComplexManifolds().affine_space(
            1,
            name="Legendre_parameter_line",
            coordinate_names=("t",),
        )
        analytic_t = analytic_line.atlas()["standard"].coordinate(0)
        smooth_stratum = ComplexManifolds().open_submanifold(
            analytic_line,
            "Legendre_punctured_disc",
            (abs(analytic_t) < 0.75, analytic_t != 0),
        )
        smooth_stratum._preamble_disc_radius = 0.75
        base_point = smooth_stratum.point((0.5,))

        pi_one = OwnedGroups().Free(1, names="gamma0")
        generator = next(iter(pi_one.group_generators()))
        pointed_pi_one = PointedAnalyticFundamentalGroup(
            smooth_stratum,
            base_point,
            pi_one,
            generator,
        )

        cohomology = integers.free_module(2).equip_bilinear_form(integers, [[0, 1], [-1, 0]])
        labels = tuple(cohomology.module_generating_set())
        alpha_dual = cohomology.module_generator(labels[0])
        beta_dual = cohomology.module_generator(labels[1])
        forward_linear = cohomology.module_category().Mor(cohomology, cohomology)(
            {
                labels[0]: alpha_dual,
                labels[1]: 2 * alpha_dual + beta_dual,
            }
        )
        inverse_linear = cohomology.module_category().Mor(cohomology, cohomology)(
            {
                labels[0]: alpha_dual,
                labels[1]: -2 * alpha_dual + beta_dual,
            }
        )
        forward = cohomology.Mor(cohomology)(forward_linear)
        inverse = cohomology.Mor(cohomology)(inverse_linear)

        def loop_action(loop):
            loop = pi_one(loop)
            result = cohomology.Mor(cohomology).identity()
            for letter in loop.Tietze():
                if letter == 1:
                    result = forward * result
                elif letter == -1:
                    result = inverse * result
                else:
                    raise ArithmeticError("the punctured-disc fundamental group has one signed generator")
            return result

        action_functor = GroupActionFunctor(
            pi_one,
            FormModules(integers),
            cohomology,
            loop_action,
        )
        local_system = IntegralLocalSystem(
            smooth_stratum,
            pointed_pi_one,
            cohomology,
            action_functor,
        )
        higher_direct_image = HigherDirectImageSheaf(
            self,
            1,
            smooth_stratum,
            local_system,
        )

        self._parameter_algebra = parameter
        self._family = family
        self._singular_fiber = singular_fiber
        self._smooth_fiber = smooth_fiber
        self._smooth_stratum = smooth_stratum
        self._base_point = base_point
        self._pointed_pi_one = pointed_pi_one
        self._fiber_h1 = cohomology
        self._positive_monodromy = forward
        self._negative_monodromy = inverse
        self._local_system = local_system
        self._higher_direct_image = higher_direct_image

    def parameter_algebra(self):
        return self._parameter_algebra

    def family_scheme(self):
        return self._family

    def family_morphism(self):
        return self.family_scheme().family_morphism()

    def singular_parameter(self):
        return self.parameter_algebra().zero()

    def singular_fiber(self):
        return self._singular_fiber

    def smooth_reference_fiber(self):
        return self._smooth_fiber

    def smooth_stratum(self):
        return self._smooth_stratum

    def base_point(self):
        return self._base_point

    def pointed_fundamental_group(self):
        return self._pointed_pi_one

    def fiber_cohomology(self, point):
        assert point is self.base_point(), (
            "the represented Legendre H^1 module is materialized at t=1/2"
        )
        return self._fiber_h1

    def higher_direct_image(self):
        return self._higher_direct_image

    def local_system(self):
        return self._local_system

    def monodromy_representation(self):
        return self.local_system().monodromy_representation()

    def positive_monodromy(self):
        return self._positive_monodromy

    def monodromy_preserves_pairing(self) -> bool:
        module = self.fiber_cohomology(self.base_point())
        action = self.positive_monodromy()
        generators = tuple(module.module_generators())
        return all(
            module.pairing(action(left), action(right)) == module.pairing(left, right)
            for left in generators
            for right in generators
        )

    def proper_base_change_hypotheses_hold(self, point) -> bool:
        return (
            point is self.base_point()
            and self.family_scheme() in Schemes(self.parameter_algebra()).Projective()
        )

    def stalk_to_fiber_comparison(self):
        return self.higher_direct_image().stalk_to_fiber_comparison(self.base_point())

    def _repr_(self) -> str:
        return f"Legendre monodromy family over {self.parameter_algebra()} with smooth stratum {self.smooth_stratum()}"



def legendre_monodromy_family():
    return LegendreMonodromyFamily()


__all__ = [
    "HigherDirectImageSheaf",
    "IntegralLocalSystem",
    "LegendreMonodromyFamily",
    "PointedAnalyticFundamentalGroup",
    "legendre_monodromy_family",
]
