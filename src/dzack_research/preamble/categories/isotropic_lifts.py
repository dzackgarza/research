r"""Marked rank-one reduction lifts as kernel-group torsors.

The defining map fixes a chosen isotropic vector and induces the specified
isometry on its perpendicular quotient. A rational Witt splitting supplies
one lift. Its left translates by the target reduction kernel are all lifts.
The additive coordinates evaluate by Eichler transvections, not by affine
combinations of matrices (Gritsenko--Hulek--Sankaran, section 3.1, (4)--(5)).
"""

from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.group.g_objects import GObjects
from dzack_research.preamble.categories.group.g_sets import TrivializedTorsors
from dzack_research.preamble.categories.lattices import IsotropicReductions, Lattices
from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.rings.ring_foundation import OwnedCategoryOverBaseRing
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.owned_category import _object_of, owned_category_join


def _vector_denominator(vector, integral_module):
    r"""The denominator ideal of the map taking 1 to this vector."""
    ring = integral_module.base_ring()
    field_map = ring.fraction_field_map()
    line = ring.regular_module()
    arrow = Modules(field_map.codomain()).Mor(line.base_change(field_map), vector.parent())(
        lambda label: vector
    )
    (denominator,) = tuple(arrow.denominator_ideal(line, integral_module).ideal_generators())
    return denominator


def _rational_splitting(reduction, plane):
    r"""Present the reduction's retained quotient as the orthogonal summand."""
    witt = reduction.rational_witt_decomposition()
    ambient = witt.rational_lattice()
    rational_reduction = reduction.vector_space()
    e, f = witt.isotropic_vector(), witt.dual_isotropic_vector()
    integral_ambient = reduction.isotropic_embedding().codomain()
    rationalize = integral_ambient.generic_fibre_map()
    perpendicular = reduction.orthogonal_complement().inclusion()

    def section_image(label):
        lift = rationalize(perpendicular(reduction.coordinate_frame()[label])).underlying_element()
        return lift - ambient.scalar_multiple(lift.b(f), e)

    section = rational_reduction.Mor(ambient)(section_image)
    plane_embedding = plane.Mor(ambient)((e, f))
    splitting = ambient.orthogonal_decomposition((plane_embedding, section))
    return witt, section, splitting


class IsotropicReductionLiftTorsors(OwnedCategoryOverBaseRing):
    r"""Rational isometry lifts preserving the marked generators of isotropic lines.

    The reduction of a hyperbolic plane along a primitive null line has rank
    zero; its marked-line lift torsor therefore has a rank-zero parameter
    space, and its selected point already descends to the integral lattice.

    EXAMPLES::

        sage: U = Lattices(ZZ)("U")
        sage: R = U.basis_vector(0).isotropic_reduction()
        sage: lifts = R.rational_lifts(R, R.Isom(R).identity())
        sage: lifts.parameter_space().module_rank() == 0
        True
        sage: lifts.integral_base_point().integral_restriction(U, U) is not None
        True
    """

    def super_categories(self):
        return [Sets()]

    def _call_(self, source, target, reduction_isometry):
        ring = self.base_ring()
        for reduction in (source, target):
            if reduction not in IsotropicReductions(ring):
                raise ValueError("both endpoints must be isotropic reductions over the same ring")
            if reduction.isotropic_sublattice().module_rank() != 1:
                raise ValueError("this lift torsor requires marked isotropic lines")
            if not reduction.isotropic_embedding().codomain().is_nondegenerate():
                raise ValueError("the marked-line transvection torsor requires nondegenerate ambient forms")
        field_map = ring.fraction_field_map()
        if reduction_isometry.domain() is source and reduction_isometry.codomain() is target:
            reduction_isometry = reduction_isometry.base_change(field_map)
        if reduction_isometry.domain() is not source.vector_space() or reduction_isometry.codomain() is not target.vector_space():
            raise ValueError("the reduction isometry must have the given rational reduction endpoints")
        plane = Lattices(field_map.codomain())("U")
        source_witt, source_section, source_split = _rational_splitting(source, plane)
        target_witt, target_section, target_split = _rational_splitting(target, plane)
        source_sum, target_sum = source_split.codomain(), target_split.codomain()
        diagonal = source_sum.Isom(target_sum)(source_sum.from_summands(
            target_sum.injection(0),
            target_sum.injection(1) * reduction_isometry,
        ))
        base = target_split.inverse() * diagonal * source_split
        source_ambient, target_ambient = base.domain(), base.codomain()
        source_e = source_witt.isotropic_vector()
        target_e = target_witt.isotropic_vector()
        target_line = target_ambient.subobject_on((target_e,)).inclusion()
        source_labels = tuple(source.vector_space().module_generating_set())
        target_vectors = tuple(target_section(v) for v in target.vector_space().module_generators())

        kernel = target_ambient.Aut().predicate_subgroup(
            lambda g: g(target_e) == target_e and all(
                target_line.is_in_image(g(v) - v) for v in target_vectors
            ),
            "the kernel of the marked-line reduction action",
        )
        points = source_ambient.Isom(target_ambient).condition_set(
            lambda g: g(source_e) == target_e and all(
                target_line.is_in_image(
                    g(source_section(source.vector_space().module_generator(label)))
                    - target_section(reduction_isometry(source.vector_space().module_generator(label)))
                ) for label in source_labels
            )
        )
        forward = Sets().Mor(kernel, points)(lambda g: points(g * base))
        backward = Sets().Mor(points, kernel)(lambda g: kernel(g * base.inverse()))
        # Multiplication by base and by its inverse give the two inverse
        # maps of the fibre of the reduction action.
        trivialization = Sets().Core().Mor(kernel, points)._from_known_inverse_pair(forward, backward)
        return _object_of(
            owned_category_join((self, TrivializedTorsors(kernel))),
            trivialization=trivialization,
            source_reduction=source, target_reduction=target,
            reduction_isometry=reduction_isometry,
            source_splitting=source_split, target_splitting=target_split,
            target_section=target_section, target_witt=target_witt,
        )

    class ParentMethods:
        def __init__(self, source_reduction, target_reduction, reduction_isometry,
                     source_splitting, target_splitting, target_section, target_witt, **rest):
            self._source_reduction = source_reduction
            self._target_reduction = target_reduction
            self._reduction_isometry = reduction_isometry
            self._source_splitting = source_splitting
            self._target_splitting = target_splitting
            self._target_section = target_section
            self._target_witt = target_witt
            super().__init__(**rest)

        def source_reduction(self):
            return self._source_reduction

        def target_reduction(self):
            return self._target_reduction

        def reduction_isometry(self):
            return self._reduction_isometry

        def source_splitting(self):
            return self._source_splitting

        def target_splitting(self):
            return self._target_splitting

        def parameter_space(self):
            return self.target_reduction().vector_space()

        @cached_method
        def parameterization(self):
            r"""The chosen additive coordinates, evaluated by transvections.

            On U + <2>, t*a sends f to f+t*a-t^2*e. The parameter
            dimension is the rank of the reduction, hence ambient rank - 2.
            """
            parameters = self.parameter_space()
            witt = self._target_witt
            ambient = witt.rational_lattice()
            base = self.base_point()
            forward = Sets().Mor(parameters, self)(
                lambda a: self(ambient.eichler_transvection(witt.isotropic_vector(), self._target_section(a)) * base)
            )
            projection = self.target_splitting().codomain().projection(1) * self.target_splitting()
            backward = Sets().Mor(self, parameters)(
                lambda lift: projection((lift * base.inverse())(witt.dual_isotropic_vector()) - witt.dual_isotropic_vector())
            )
            return Sets().Core().Mor(parameters, self)._from_known_inverse_pair(forward, backward)

        @cached_method
        def integral_members(self):
            r"""The integral lift locus with its integral-kernel action.

            This locus can be empty. Its definition does not infer emptiness
            from the failure of one chosen rational lift to be integral.
            """
            source = self.source_reduction().isotropic_embedding().codomain()
            target = self.target_reduction().isotropic_embedding().codomain()
            points = self.point_set().condition_set(
                lambda lift: lift.integral_restriction(source, target) is not None
            )
            integral_kernel = self.acting_group().predicate_subgroup(
                lambda g: g.integral_restriction(target, target) is not None,
                "integral automorphisms in the marked-line reduction kernel",
            )
            return GObjects(integral_kernel, Sets()).on_set(
                points, lambda g, lift: g * lift, orbit_relation=lambda left, right: True
            )

        @cached_method
        def integral_parameter_quotient(self):
            r"""Retain a finite quotient containing every integral lift parameter class.

            Write ``x=base^-1(f_target)`` and choose D with Dx integral.
            Every integral lift has parameter in ``P=projection(E)/D``.
            If e has denominator A and the section of P has denominator B,
            then ``m=2AB`` makes the section of mP lie in ``2A*E``.
            The Eichler formula and its inverse are integral for these
            parameters. Thus integrality is constant on cosets of mP in P.
            This quotient is a finite search presentation, not an assertion
            that mP is the entire integral kernel.
            """
            source = self.source_reduction().isotropic_embedding().codomain()
            target = self.target_reduction().isotropic_embedding().codomain()
            ring = source.base_ring()
            field_map = ring.fraction_field_map()
            field = field_map.codomain()
            parameters = self.parameter_space()
            restricted_parameters = parameters.restrict_scalars(field_map)
            witt = self._target_witt
            rational_target = witt.rational_lattice()
            source_vector = self.base_point().inverse()(witt.dual_isotropic_vector())
            denominator = _vector_denominator(source_vector, source)
            projection = self.target_splitting().codomain().projection(1) * self.target_splitting()
            rationalize = target.generic_fibre_map()
            parameter_lattice = restricted_parameters.subobject_on(tuple(
                restricted_parameters(parameters.scalar_multiple(
                    field.one() / field_map(denominator),
                    projection(rationalize(vector).underlying_element()),
                )) for vector in target.module_generators()
            ))
            section = Modules(field).Mor(parameter_lattice.base_change(field_map), rational_target)(
                lambda label: self._target_section(
                    parameter_lattice.inclusion()(parameter_lattice.module_generator(label)).underlying_element()
                )
            )
            (section_denominator,) = tuple(section.denominator_ideal(parameter_lattice, target).ideal_generators())
            isotropic_denominator = _vector_denominator(witt.isotropic_vector(), target)
            period = ring(2) * isotropic_denominator * section_denominator
            multiplication = Modules(ring).Mor(parameter_lattice, parameter_lattice)(
                lambda label: parameter_lattice.scalar_multiple(period, parameter_lattice.module_generator(label))
            )
            return multiplication.cokernel_projection()

        @cached_method
        def integral_parameter_classes(self):
            r"""The complete finite residue locus for integral isometry lifts."""
            quotient = self.integral_parameter_quotient()
            lattice = quotient.domain()
            source = self.source_reduction().isotropic_embedding().codomain()
            target = self.target_reduction().isotropic_embedding().codomain()

            def integral(residue):
                parameter = lattice.inclusion()(quotient.preimage(residue)).underlying_element()
                lift = self.parameterization()(parameter)
                return lift.integral_restriction(source, target) is not None

            return quotient.codomain().condition_set(integral)

        @cached_method
        def integral_base_point(self):
            r"""Select an integral lift, or raise when the integral lift locus is empty."""
            quotient = self.integral_parameter_quotient()
            for residue in self.integral_parameter_classes():
                parameter = quotient.domain().inclusion()(quotient.preimage(residue)).underlying_element()
                return self.parameterization()(parameter)
            raise ValueError("the integral reduction-lift locus is empty")

        @cached_method
        def integral_torsor(self):
            r"""Trivialize the integral lift locus under its full integral kernel.

            EXAMPLES::

                sage: L = Lattices(ZZ)("U") + Lattices(ZZ)([[2]])
                sage: R = L.basis_vector(0).isotropic_reduction()
                sage: T = R.rational_lifts(R, R.Isom(R).identity())
                sage: a = T.parameter_space().module_generators()[0]
                sage: lift = T.parameterization()(a)
                sage: torsor = T.integral_torsor()
                sage: coordinate = torsor.trivialization().inverse()(lift)
                sage: coordinate != torsor.acting_group().one()
                True
                sage: torsor.trivialization()(coordinate) == lift
                True
            """
            from dzack_research.preamble.categories.group.g_sets import Torsors

            members = self.integral_members()
            group = members.acting_group()
            points = members.point_set()
            chosen = self.integral_base_point()
            forward = Sets().Mor(group, points)(lambda g: points(g * chosen))
            backward = Sets().Mor(points, group)(lambda lift: group(lift * chosen.inverse()))
            trivialization = Sets().Core().Mor(group, points)._from_known_inverse_pair(forward, backward)
            return Torsors(group).from_trivialization(trivialization)
