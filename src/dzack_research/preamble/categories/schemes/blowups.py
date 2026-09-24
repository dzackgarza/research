r"""Blowups of projective planes at represented rational points.

For a point ``p`` of ``P^2`` choose the two canonical linear forms obtained by
normalizing one nonzero homogeneous coordinate.  They form a regular sequence
cutting out ``p``.  The Rees construction is the graph closure

``Bl_p(P^2) <= P^2 x P^1``

cut out by ``f V - g U``.  This is the codimension-two regular-center blowup,
not a toric specialization.  The blowup is constructed by the closed-subscheme
construction of ``P^2 x P^1`` with the placement ``ProjectivePointBlowups(R)``,
whose level data are the point ``p``, the center ``V(f, g) <= P^2`` and the
bihomogeneous coordinate datum the graph relation is written in.  The blowdown
is the first product projection restricted along the inclusion.
"""

from sage.misc.cachefunc import cached_method
from sage.rings.integer_ring import ZZ as SageZZ

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
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)


def _integers():
    return _own_ring(SageZZ)


class ProjectivePointBlowups(OwnedCategoryOverBaseRing):
    r"""Blowups ``Bl_p(P^2)`` of the projective plane at one rational point ``p``."""

    def _repr_object_names(self):
        return f"projective-plane point blowups over {self.base_ring()}"

    def super_categories(self):
        return [Schemes(self.base_ring()).Projective().Smooth()]

    def an_object(self):
        plane = ProjectiveSpaces(self.base_ring())(2)
        return self(plane.point_morphism((1, 1, 1)))

    def _call_(self, point):
        r"""``Bl_p(P^2)`` for a rational point ``p: Spec R -> P^2_R``."""
        assert point.codomain().scheme_base_ring() is self.base_ring(), (
            f"cannot blow up at {point} in {self}: the plane {point.codomain()} lies over "
            f"{point.codomain().scheme_base_ring()}, not over {self.base_ring()}"
        )
        return _projective_point_blowup(point.codomain(), point)

    class ParentMethods:
        def __init__(self, blowup_point, blowup_center, graph_section_space, **rest) -> None:
            self._blowup_point = blowup_point
            self._blowup_center = blowup_center
            self._graph_section_space = graph_section_space
            super().__init__(**rest)

        def blowup_point(self):
            r"""The rational point ``p: Spec R -> P^2`` that is blown up."""
            return self._blowup_point

        def blowup_source(self):
            r"""The projective plane ``P^2`` that is blown up."""
            return self.blowup_point().codomain()

        def blowup_center(self):
            r"""The center ``V(f, g) <= P^2`` cut out by the selected regular sequence."""
            return self._blowup_center

        def graph_ambient_product(self):
            r"""``P^2 x P^1``, the codomain of the graph inclusion."""
            return self.inclusion().codomain()

        @cached_method
        def blowup_morphism(self):
            r"""The blowdown ``Bl_p(P^2) -> P^2``: the first projection along the inclusion."""
            return self.graph_ambient_product().projection(0) * self.inclusion()

        def blowdown(self, *args, **kwargs):
            return self.blowup_morphism(*args, **kwargs)

        def graph_relation(self):
            r"""The bihomogeneous equation ``f V - g U`` cutting the blowup out."""
            return next(iter(self.defining_equations()))

        def graph_section_space(self):
            r"""The sections of ``O(1, 1)`` whose coordinate ring the graph relation is written in."""
            return self._graph_section_space

        def source_coordinate_embedding(self):
            r"""The homogeneous coordinate ring of ``P^2`` inside the bihomogeneous one."""
            return self.graph_section_space().factor_coordinate_embedding(0)

        def center_equations_in_graph_ring(self):
            r"""The center equations ``f, g`` written in the bihomogeneous coordinate ring."""
            embedding = self.source_coordinate_embedding()
            return tuple(embedding(equation) for equation in self.blowup_center().defining_equations())

        def _source_hypersurface_equation_in_graph_ring(self, hypersurface):
            assert hypersurface in ClosedSubschemes(self.scheme_base_ring()), (
                f"the transform under the blowup {self} needs a closed subscheme of "
                f"{self.blowup_source()}, but {hypersurface} is in {hypersurface.category()}"
            )
            assert hypersurface.inclusion().codomain() is self.blowup_source(), (
                f"{hypersurface} is a closed subscheme of {hypersurface.inclusion().codomain()}, "
                f"not of the blown-up plane {self.blowup_source()}"
            )
            equations = hypersurface.defining_equations()
            assert int(equations.cardinality()) == 1, (
                f"the transform under {self} is computed only for a hypersurface V(f) cut out by "
                f"one equation, but {hypersurface} has {equations.cardinality()} defining equations"
            )
            source_ring = self.source_coordinate_embedding().domain()
            raised = hypersurface.homogeneous_defining_equations(source_ring)
            return self.source_coordinate_embedding()(next(iter(raised)))

        @cached_method
        def exceptional_divisor(self):
            r"""``E = pi^{-1}(p)``, cut out in the blowup by the center equations."""
            return self.closed_subscheme(self.center_equations_in_graph_ring())

        def scheme_theoretic_inverse_image(self, hypersurface):
            r"""``pi^{-1}(C)``, cut out in the blowup by the pulled-back equation of ``C``."""
            return self.closed_subscheme(self._source_hypersurface_equation_in_graph_ring(hypersurface))

        def total_transform(self, hypersurface):
            r"""The total transform ``pi^*C``, cut out by the pulled-back equation of ``C``."""
            return self.closed_subscheme(self._source_hypersurface_equation_in_graph_ring(hypersurface))

        def strict_transform(self, hypersurface):
            r"""The strict transform: the saturation of ``(f V - g U, pi^* h)`` by the center ideal."""
            ring = self.graph_relation().parent()
            equation = self._source_hypersurface_equation_in_graph_ring(hypersurface)
            total_ideal = ring.ideal(self.graph_relation(), equation)
            exceptional_ideal = ring.ideal(*self.center_equations_in_graph_ring())
            saturated = total_ideal.saturation(exceptional_ideal)
            return self.closed_subscheme(tuple(saturated.ideal_generators()))

        def curve_multiplicity_at_center(self, curve):
            equations = curve.defining_equations()
            assert int(equations.cardinality()) == 1, (
                f"the multiplicity of {curve} at the center of {self} is computed only for a plane "
                f"curve V(f) cut out by one equation, but it has {equations.cardinality()} "
                "defining equations"
            )
            degree = int(next(iter(equations)).degree())
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
            return PicardGroups()(module, scheme=self)

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
            labels = source.module_generating_set()
            assert int(labels.cardinality()) == 1, (
                f"Pic(P^2) = ZZ H should have one module generator, but {source} has "
                f"{labels.cardinality()}"
            )
            return source.module_category().Mor(source, self.picard_group())(
                {next(iter(labels)): self.hyperplane_picard_class()}
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
            equations = curve.defining_equations()
            assert int(equations.cardinality()) == 1, (
                f"the degree of {curve} as a plane divisor is computed only for a curve V(f) cut "
                f"out by one equation, but it has {equations.cardinality()} defining equations"
            )
            return _integers()(int(next(iter(equations)).degree()))

        def total_transform_picard_class(self, curve):
            return self.curve_degree(curve) * self.hyperplane_picard_class()

        def strict_transform_picard_class(self, curve):
            return (
                self.curve_degree(curve) * self.hyperplane_picard_class()
                - self.curve_multiplicity_at_center(curve)
                * self.exceptional_picard_class()
            )

        def pullback_line_bundle(self, source_bundle):
            r"""``pi^* O_{P^2}(d) = O_{P^2 x P^1}(d, 0)|_B``."""
            assert source_bundle.projective_space() is self.blowup_source(), (
                f"{source_bundle} is not a line bundle O(d) on the blown-up plane "
                f"{self.blowup_source()}; it lives on {source_bundle.projective_space()}"
            )
            return self.graph_ambient_product().O(
                source_bundle.degree(),
                0,
            ).restrict_to(self)

        @cached_method
        def exceptional_line_bundle(self):
            r"""Return ``O_B(E)=O_{P^2 x P^1}(1,-1)|_B``."""
            return self.graph_ambient_product().O(1, -1).restrict_to(self)

        @cached_method
        def pulled_back_source_canonical_bundle(self):
            r"""``pi^* omega_{P^2} = O_{P^2 x P^1}(-3, 0)|_B``."""
            return self.pullback_line_bundle(self.blowup_source().canonical_line_bundle())

        @cached_method
        def canonical_comparison(self):
            r"""The isomorphism ``omega_B ~= pi^* omega_{P^2} tensor O_B(E)``.

            Its domain is ``omega_B = O_{P^2 x P^1}(-2, -1)|_B`` and its codomain
            is the tensor product of the pulled-back canonical bundle with the
            exceptional line bundle.
            """
            canonical = self.graph_ambient_product().O(-2, -1).restrict_to(self)
            target = self.pulled_back_source_canonical_bundle().tensor_product(
                self.exceptional_line_bundle()
            )
            return canonical.canonical_isomorphism_to(target)

        def canonical_line_bundle(self):
            return self.canonical_comparison().domain()

        canonical_bundle = canonical_line_bundle

        @cached_method
        def anticanonical_line_bundle(self):
            return self.canonical_line_bundle().dual_sheaf()

        def anticanonical_bundle(self, *args, **kwargs):
            return self.anticanonical_line_bundle(*args, **kwargs)

        def is_del_pezzo(self) -> bool:
            return bool(self.anticanonical_line_bundle().is_ample())

        def del_pezzo_degree(self):
            r"""``(-K_B)^2 = (3H - E)^2``."""
            assert self.is_del_pezzo(), (
                f"the degree (-K)^2 of a del Pezzo surface is undefined for {self}: its "
                "anticanonical bundle is not ample"
            )
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
    assert base in OwnedFields(), (
        f"the blowup of {projective_plane} at a point is implemented only over a field, but "
        f"its base ring {base} is not a field"
    )
    assert projective_plane in ProjectiveSpaces(base) and int(projective_plane.relative_dimension()) == 2, (
        f"the blowup at a point is implemented only for the projective plane P^2, but "
        f"{projective_plane} is not P^2 over {base}"
    )
    assert point.codomain() is projective_plane and point.domain() is projective_plane.base_scheme(), (
        f"the blowup center {point} must be a rational point Spec {base} -> {projective_plane}, "
        f"but it is a morphism {point.domain()} -> {point.codomain()}"
    )

    direction = ProjectiveSpaces(base)(1, names=("U", "V"))
    product = projective_plane.scheme_category().product((projective_plane, direction))
    graph_sections = product.O(1, 1).global_sections()
    source_embedding = graph_sections.factor_coordinate_embedding(0)
    direction_embedding = graph_sections.factor_coordinate_embedding(1)
    source_ring = source_embedding.domain()
    source_labels = tuple(source_ring.algebra_generating_set())
    coordinates = tuple(point.point_coordinates())
    nonzero = tuple(index for index, coordinate in enumerate(coordinates) if coordinate != base.zero())
    assert nonzero, (
        f"the point {point} has all coordinates {coordinates} zero, so it is not a point of "
        f"{projective_plane}"
    )
    pivot = nonzero[0]
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
    return product.closed_subscheme(
        graph_relation,
        placements=(ProjectivePointBlowups(base),),
        blowup_point=point,
        blowup_center=center,
        graph_section_space=graph_sections,
    )


__all__ = [
    "ProjectivePointBlowups",
]
