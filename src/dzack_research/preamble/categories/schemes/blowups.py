r"""Blowups of projective planes at represented rational points.

For a point ``p`` of ``P^2`` choose the two canonical linear forms obtained by
normalizing one nonzero homogeneous coordinate.  They form a regular sequence
cutting out ``p``.  The Rees construction is the graph closure

``Bl_p(P^2) <= P^2 x P^1``

cut out by ``f V - g U``.  This is the codimension-two regular-center blowup,
not a toric specialization.  The product projections retain the blowdown and
the second projective coordinate records the exceptional direction.
"""

from sage.misc.cachefunc import cached_method
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.divisors.picard_groups import (
    PicardGroups,
)
from dzack_research.preamble.categories.modules.pure.modules import BilinearMap
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    OwnedFields,
    _own_ring,
)
from dzack_research.preamble.categories.schemes.schemes import (
    ClosedSubschemes,
    ProjectiveSpaces,
    Schemes,
    _categorical_scheme_morphism,
    _refine_closed_subscheme,
    _refine_scheme,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)


def _integers():
    return _own_ring(SageZZ)


class _ProjectivePointBlowupConstruction(SageObject):
    r"""The selected Rees/graph data defining one represented point blowup."""

    def __init__(
        self,
        source,
        center,
        point,
        blowdown,
        graph_ambient,
        graph_relation,
        graph_section_space,
        source_coordinate_embedding,
        center_equations_in_graph_ring,
    ) -> None:
        self._source = source
        self._center = center
        self._point = point
        self._blowdown = blowdown
        self._graph_ambient = graph_ambient
        self._graph_relation = graph_relation
        self._graph_section_space = graph_section_space
        self._source_coordinate_embedding = source_coordinate_embedding
        self._center_equations_in_graph_ring = center_equations_in_graph_ring

    def source(self):
        return self._source

    def center(self):
        return self._center

    def point(self):
        return self._point

    def blowdown(self):
        return self._blowdown

    def graph_ambient(self):
        return self._graph_ambient

    def graph_relation(self):
        return self._graph_relation

    def graph_section_space(self):
        return self._graph_section_space

    def source_coordinate_embedding(self):
        return self._source_coordinate_embedding

    def center_equations_in_graph_ring(self):
        return self._center_equations_in_graph_ring


class _ProjectivePointBlowupCanonicalComparison(SageObject):
    r"""The line-bundle comparison ``omega_B ~= pi^*omega_P tensor O_B(E)``."""

    def __init__(self, blowup) -> None:
        canonical = blowup.graph_ambient_product().O(-2, -1).restrict_to(blowup)
        pulled = blowup.pullback_line_bundle(
            blowup.blowup_source().canonical_line_bundle()
        )
        exceptional = blowup.exceptional_line_bundle()
        target = pulled.tensor_product(exceptional)
        self._blowup = blowup
        self._canonical = canonical
        self._pulled = pulled
        self._exceptional = exceptional
        self._target = target
        self._isomorphism = canonical.canonical_isomorphism_to(target)

    def blowup(self):
        return self._blowup

    def canonical_line_bundle(self):
        return self._canonical

    def pulled_back_source_canonical_bundle(self):
        return self._pulled

    def exceptional_line_bundle(self):
        return self._exceptional

    def target_line_bundle(self):
        return self._target

    def isomorphism(self):
        return self._isomorphism

    def _repr_(self) -> str:
        return f"Canonical-bundle comparison for {self.blowup()}: {self.canonical_line_bundle()} ~= {self.target_line_bundle()}"



class ProjectivePointBlowups(OwnedCategoryOverBaseRing):
    r"""Blowups of ``P^2`` at one represented rational point."""

    def _repr_object_names(self):
        return f"projective-plane point blowups over {self.base_ring()}"

    def super_categories(self):
        return [Schemes(self.base_ring()).Projective().Smooth()]

    def an_object(self):
        plane = ProjectiveSpaces(self.base_ring())(2)
        return plane.point_blowup(
            plane.point_morphism((1, 1, 1))
        )

    class ParentMethods:
        def blowup_construction(self):
            r"""Return the selected Rees/graph datum defining this blowup."""
            return self._preamble_blowup_construction

        def blowup_source(self):
            return self.blowup_construction().source()

        def blowup_center(self):
            return self.blowup_construction().center()

        def blowup_point(self):
            return self.blowup_construction().point()

        def blowup_morphism(self):
            return self.blowup_construction().blowdown()

        blowdown = blowup_morphism

        def graph_ambient_product(self):
            return self.blowup_construction().graph_ambient()

        def graph_relation(self):
            return self.blowup_construction().graph_relation()

        def graph_section_space(self):
            return self.blowup_construction().graph_section_space()

        def source_coordinate_embedding(self):
            return self.blowup_construction().source_coordinate_embedding()

        def center_equations_in_graph_ring(self):
            return self.blowup_construction().center_equations_in_graph_ring()

        def _source_hypersurface_equation_in_graph_ring(self, hypersurface):
            if hypersurface not in ClosedSubschemes(self.scheme_base_ring()):
                raise TypeError("a transform starts from a represented closed hypersurface")
            if hypersurface.inclusion().codomain() is not self.blowup_source():
                raise ValueError("the transformed hypersurface belongs to a different source")
            equations = tuple(hypersurface.defining_equations())
            if len(equations) != 1:
                raise ValueError("the represented divisor transform currently requires one hypersurface equation")
            source_ring = self.source_coordinate_embedding().domain()
            raised = hypersurface.homogeneous_defining_equations(source_ring)
            return self.source_coordinate_embedding()(next(iter(raised)))

        def _closed_subscheme_from_graph_equations(self, equations, *, kind):
            r"""Cut a closed subobject of the blowup by equations in its graph ambient.

            The blowup itself is already the graph hypersurface inside the
            multiprojective ambient.  Adding equations there and retargeting
            the resulting closed immersion to the blowup gives the iterated
            closed subobject without pretending that the graph hypersurface is
            itself an ambient projective space.
            """
            equations = tuple(equations)
            ambient = self.graph_ambient_product()
            combined = (self.graph_relation(), *equations)
            nested = ambient.closed_subscheme(combined)
            nested._preamble_inclusion = _categorical_scheme_morphism(
                nested.embedding_morphism(),
                domain=nested,
                codomain=self,
            )
            nested = _refine_closed_subscheme(
                nested,
                self,
                defining_equations=equations,
            )
            nested._preamble_blowup_transform_kind = kind
            nested._preamble_blowup = self
            return nested

        @cached_method
        def exceptional_divisor(self):
            return self._closed_subscheme_from_graph_equations(
                self.center_equations_in_graph_ring(),
                kind="exceptional",
            )

        def scheme_theoretic_inverse_image(self, hypersurface):
            equation = self._source_hypersurface_equation_in_graph_ring(hypersurface)
            return self._closed_subscheme_from_graph_equations(
                (equation,),
                kind="inverse-image",
            )

        def total_transform(self, hypersurface):
            equation = self._source_hypersurface_equation_in_graph_ring(hypersurface)
            return self._closed_subscheme_from_graph_equations(
                (equation,),
                kind="total",
            )

        def strict_transform(self, hypersurface):
            ring = self.graph_relation().parent()
            equation = self._source_hypersurface_equation_in_graph_ring(hypersurface)
            total_ideal = ring.ideal(self.graph_relation(), equation)
            exceptional_ideal = ring.ideal(*tuple(self.center_equations_in_graph_ring()))
            saturated = total_ideal.saturation(exceptional_ideal)
            transform = self._closed_subscheme_from_graph_equations(
                tuple(saturated.ideal_generators()),
                kind="strict",
            )
            transform._preamble_blowup_saturated_ideal = saturated
            return transform

        def curve_multiplicity_at_center(self, curve):
            equations = tuple(curve.defining_equations())
            if len(equations) != 1:
                raise ValueError("curve multiplicity here requires one plane hypersurface equation")
            degree = int(equations[0].degree())
            bundle = self.blowup_source().O(degree)
            sections = bundle.global_sections()
            polynomial = next(
                iter(
                    curve.homogeneous_defining_equations(
                        sections.homogeneous_coordinate_ring()
                    )
                )
            )
            section = sections.section_from_homogeneous_polynomial(polynomial)
            multiplicity = 0
            for order in range(1, degree + 2):
                evaluation = bundle.jet_evaluation(self.blowup_point(), order)
                if evaluation(section) != evaluation.codomain().zero():
                    break
                multiplicity = order
            return _integers()(multiplicity)

        @cached_method
        def picard_group(self):
            module = _integers()._fresh_free_module_on(
                finite_ordered_set(("H", "E")),
            )
            return PicardGroups()(
                module,
                scheme=self,
                construction_data={
                    "blowup_hyperplane_label": "H",
                    "blowup_exceptional_label": "E",
                },
            )

        def hyperplane_picard_class(self):
            return self.picard_group().module_generator("H")

        def exceptional_picard_class(self):
            return self.picard_group().module_generator("E")

        @cached_method
        def source_picard_group(self):
            source = self.blowup_source()
            return source.picard_group(
                PicardGroups().trivial(source.base_scheme())
            )

        @cached_method
        def picard_pullback_morphism(self):
            source = self.source_picard_group()
            labels = tuple(source.module_generating_set())
            if len(labels) != 1:
                raise ArithmeticError("Pic(P^2) over a field must have one selected generator")
            return source.module_category().Mor(source, self.picard_group())(
                {labels[0]: self.hyperplane_picard_class()}
            )

        @cached_method
        def picard_intersection_pairing(self):
            picard = self.picard_group()
            values = _integers().regular_module()

            def value(left, right):
                if left == "H" and right == "H":
                    return _integers().one()
                if left == "E" and right == "E":
                    return -_integers().one()
                return _integers().zero()

            return BilinearMap(picard, picard, values, value)

        def curve_degree(self, curve):
            equations = tuple(curve.defining_equations())
            if len(equations) != 1:
                raise ValueError("the represented plane divisor class requires one equation")
            return _integers()(int(equations[0].degree()))

        def total_transform_picard_class(self, curve):
            return self.curve_degree(curve) * self.hyperplane_picard_class()

        def strict_transform_picard_class(self, curve):
            return (
                self.curve_degree(curve) * self.hyperplane_picard_class()
                - self.curve_multiplicity_at_center(curve)
                * self.exceptional_picard_class()
            )

        def pullback_line_bundle(self, source_bundle):
            from dzack_research.preamble.categories.divisors.invertible_sheaves import (
                ProjectiveSpaceLineBundle,
            )

            if not isinstance(source_bundle, ProjectiveSpaceLineBundle):
                raise TypeError("the represented blowup pullback currently starts from O(d) on P^2")
            if source_bundle.projective_space() is not self.blowup_source():
                raise ValueError("the line bundle belongs to a different blowup source")
            return self.graph_ambient_product().O(
                source_bundle.degree(),
                0,
            ).restrict_to(self)

        @cached_method
        def exceptional_line_bundle(self):
            r"""Return ``O_B(E)=O_{P^2 x P^1}(1,-1)|_B``."""
            return self.graph_ambient_product().O(1, -1).restrict_to(self)

        @cached_method
        def canonical_comparison(self):
            return _ProjectivePointBlowupCanonicalComparison(self)

        @cached_method
        def canonical_line_bundle(self):
            return self.canonical_comparison().canonical_line_bundle()

        canonical_bundle = canonical_line_bundle

        @cached_method
        def anticanonical_line_bundle(self):
            return self.canonical_line_bundle().dual_sheaf()

        anticanonical_bundle = anticanonical_line_bundle

        def is_del_pezzo(self) -> bool:
            return bool(self.anticanonical_line_bundle().is_ample())

        def del_pezzo_degree(self):
            if not self.is_del_pezzo():
                raise ValueError("the represented blowup is not del Pezzo")
            anticanonical = (
                3 * self.hyperplane_picard_class()
                - self.exceptional_picard_class()
            )
            return self.picard_intersection_pairing()(
                anticanonical,
                anticanonical,
            )


def _projective_point_blowup(projective_plane, point):
    r"""Return ``Bl_point(P^2)`` from its regular-center Rees graph in ``P^2 x P^1``."""
    base = projective_plane.scheme_base_ring()
    if base not in OwnedFields():
        raise TypeError("the represented projective point blowup requires a field base")
    if projective_plane not in ProjectiveSpaces(base) or int(projective_plane.relative_dimension()) != 2:
        raise TypeError("the represented projective point blowup requires P^2")
    if point.codomain() is not projective_plane or point.domain() is not projective_plane.base_scheme():
        raise ValueError("the blowup center must be a represented rational point of this P^2")

    direction = ProjectiveSpaces(base)(1, names=("U", "V"))
    product = projective_plane.scheme_category().product((projective_plane, direction))
    graph_sections = product.O(1, 1).global_sections()
    source_embedding = graph_sections.factor_coordinate_embedding(0)
    direction_embedding = graph_sections.factor_coordinate_embedding(1)
    source_ring = source_embedding.domain()
    source_labels = tuple(source_ring.algebra_generating_set())
    coordinates = tuple(point.point_coordinates())
    pivot = next(
        (index for index, coordinate in enumerate(coordinates) if coordinate != base.zero()),
        None,
    )
    if pivot is None:
        raise ValueError("projective point coordinates cannot all vanish")
    scalar_map = source_ring.algebra_structure_morphism()
    pivot_variable = source_ring.algebra_generator(source_labels[pivot])
    center_equations = tuple(
        scalar_map(coordinates[pivot]) * source_ring.algebra_generator(source_labels[index])
        - scalar_map(coordinates[index]) * pivot_variable
        for index in range(3)
        if index != pivot
    )
    center = projective_plane.closed_subscheme(center_equations)
    f, g = center_equations

    direction_ring = direction_embedding.domain()
    direction_labels = tuple(direction_ring.algebra_generating_set())
    U = direction_ring.algebra_generator(direction_labels[0])
    V = direction_ring.algebra_generator(direction_labels[1])
    graph_relation = (
        source_embedding(f) * direction_embedding(V)
        - source_embedding(g) * direction_embedding(U)
    )
    blowup = product.closed_subscheme(graph_relation)
    blowdown = product.projection(0) * blowup.inclusion()

    blowup._preamble_blowup_construction = _ProjectivePointBlowupConstruction(
        projective_plane,
        center,
        point,
        blowdown,
        product,
        graph_relation,
        graph_sections,
        source_embedding,
        tuple(source_embedding(equation) for equation in center_equations),
    )
    return _refine_scheme(
        blowup,
        base,
        [ProjectivePointBlowups(base)],
    )


__all__ = [
    "ProjectivePointBlowups",
]
