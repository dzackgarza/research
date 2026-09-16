r"""Relative cyclic covers of an affine scheme, with their deck action.

Let ``X = Spec(A)``, let ``L`` be an invertible ``O_X``-module, let ``n >= 1``
and let ``s`` be a section of ``L^n``.  The cyclic cover of degree ``n``
branched along ``s`` is the relative spectrum of the ``O_X``-algebra
``⊕_{i=0}^{n-1} L^{-i}``, whose multiplication
``L^{-i} ⊗ L^{-j} -> L^{-(i+j)}`` is the identity when ``i + j < n`` and is
multiplication by ``s`` when ``i + j >= n`` (Barth, Hulek, Peters and Van de
Ven, *Compact Complex Surfaces*, I.17).

That algebra is owned by ``CyclicCoverAlgebra``, which builds it for any
invertible sheaf represented by rank-one descent on an affine cover: on each
chart it is the trivialized algebra returned by
``R.cyclic_cover_presentation(f, n)``, and
the charts are glued by the transition units of ``L``.  One construction
therefore supplies the multiplication, the underlying finite module on
``1, z, ..., z^{n-1}``, the local equation ``z^n - f`` and every scalar change
of it, on the charts and here alike.

The covers constructed in this category are the globally trivialized ones,
``L = O_X`` on the affine ``X = Spec(A)``: the section is an element ``f`` of
``A``, the descent is vacuous, and the cover algebra is the single chart
algebra ``A[z]/(z^n - f)``.  The graded summand ``A z^i`` is the
trivialization of ``L^{-i}``.

The deck group is always the group scheme ``mu_n``, acting through the scheme
morphism whose coordinate pullback sends ``z`` to ``u z``.  When the scalars
contain a primitive ``n``-th root of unity ``zeta`` and ``n`` is invertible,
this action also has the familiar constant ``C_n`` realization
``z -> zeta z``.  The two notions are kept separate: the constant action is an
additional identification, never a replacement for ``mu_n``.

The quotient by the deck action is ``X`` again: the ``mu_n``-coaction gives
the summand ``A z^i`` weight ``i`` modulo ``n``, so the invariant subalgebra is
the degree-zero part ``A``.  This is a theorem about the grading, not an
invariant-ring computation, and it does not require a primitive root of unity.

For nontrivial ``L``, relative ``Spec`` is assembled from the affine spectra
of the local algebras.  Above a base overlap ``U_i cap U_j`` the cover chart is
the distinguished open of ``Spec(B_i)`` obtained by inverting the image of the
other base-chart denominator.  The finite-free basis ``1,z,...,z^(n-1)`` and
the line-bundle transition ``z_i = u_ij^-1 z_j`` determine the overlap
isomorphism, so the existing finite scheme-gluing owner constructs the global
cover and its map to ``X`` without turning compatible global sections into a
fictional affine coordinate ring.

The canonical-bundle formula and the smoothness criteria of a cover are also
not constructed here: both read the module of differentials of the cover
algebra against the invertible sheaves of the divisor layer.
"""

from sage.categories.category import Category
from sage.misc.cachefunc import cached_method
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.algebras.algebras import Algebras
from dzack_research.preamble.categories.algebras.cyclic_cover_algebras import (
    CYCLIC_COVER_VARIABLE,
    CyclicCoverAlgebra,
)
from dzack_research.preamble.categories.group.groups import OwnedGroups
from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_ring,
    _own_ring,
)
from dzack_research.preamble.categories.schemes.group_schemes import (
    AffineGroupSchemes,
    AffineGroupSchemeActions,
)
from dzack_research.preamble.categories.schemes.schemes import (
    AffineGSchemes,
    Schemes,
    _affine_morphism_from_pullback,
    _affine_spec_morphism,
)
from dzack_research.preamble.refine import refine

_ROOT_OF_UNITY_VARIABLE = "t"


def _relative_cyclic_cover(cyclic_algebra):
    r"""Return the cyclic cover through the general relative-Spec owner."""
    if not isinstance(cyclic_algebra, CyclicCoverAlgebra):
        raise TypeError("relative cyclic cover requires cyclic-cover algebra descent data")
    relative = cyclic_algebra.gluing_datum().relative_spectrum()
    glued = relative.arrow().domain()
    glued._preamble_cyclic_cover_algebra = cyclic_algebra
    glued._preamble_cyclic_cover_morphism = relative.arrow()
    return relative


def _relative_cover_chart(cyclic_algebra, chart_index):
    line_bundle = cyclic_algebra.line_bundle()
    cover = cyclic_algebra.cover()
    from dzack_research.preamble.categories.divisors.invertible_sheaves import (
        FiniteAtlasInvertibleSheaf,
    )

    if isinstance(line_bundle, FiniteAtlasInvertibleSheaf):
        return cover.chart(chart_index)
    return cover.open(chart_index)


def _relative_cover_chart_indices(cyclic_algebra):
    line_bundle = cyclic_algebra.line_bundle()
    cover = cyclic_algebra.cover()
    from dzack_research.preamble.categories.divisors.invertible_sheaves import (
        FiniteAtlasInvertibleSheaf,
    )

    if isinstance(line_bundle, FiniteAtlasInvertibleSheaf):
        return cover.chart_indices()
    return cover.atlas()


def _local_relative_cyclic_deck_action(cyclic_algebra, chart_index):
    r"""Return the canonical ``mu_n`` action on one affine chart of a relative cyclic cover."""
    if not isinstance(cyclic_algebra, CyclicCoverAlgebra):
        raise TypeError("a local cyclic deck action requires cyclic-cover algebra data")
    cover = cyclic_algebra.cover()
    if hasattr(cover, "normalize_chart_index"):
        chart_index = cover.normalize_chart_index(chart_index)
    else:
        chart_index = cover.chart_label(chart_index)
    local_base = _relative_cover_chart(cyclic_algebra, chart_index).coordinate_algebra()
    local_algebra = cyclic_algebra.local_algebra(chart_index)
    local_scheme = (local_algebra).affine_spectrum()
    group_scheme = AffineGroupSchemes(local_base).roots_of_unity(
        int(cyclic_algebra.degree())
    )
    product = local_scheme.scheme_category().product((group_scheme.scheme(), local_scheme))
    product_algebra = product.coordinate_algebra()
    group_pullback = product.projection(0).coordinate_algebra_morphism()
    cover_pullback = product.projection(1).coordinate_algebra_morphism()
    group_coordinate = group_scheme.scheme().coordinate_algebra().algebra_generator("u")
    local_z = local_algebra.algebra_generator(CYCLIC_COVER_VARIABLE)
    action_pullback = local_algebra.Mor(product_algebra)(
        {
            CYCLIC_COVER_VARIABLE: (
                group_pullback(group_coordinate) * cover_pullback(local_z)
            )
        }
    )
    action_morphism = _affine_morphism_from_pullback(
        product,
        local_scheme,
        action_pullback,
    )
    return AffineGroupSchemeActions(group_scheme)(local_scheme, action_morphism)


def _relative_cyclic_local_deck_transformation(
    cyclic_algebra, chart_index, root_of_unity
):
    r"""Return ``z_i |-> root*z_i`` on one affine chart of a relative cover."""
    scalar_ring = cyclic_algebra.scheme().scheme_base_ring()
    root = scalar_ring(root_of_unity)
    if root ** int(cyclic_algebra.degree()) != scalar_ring.one():
        raise ValueError("a deck scalar must be an n-th root of unity")
    local_algebra = cyclic_algebra.local_algebra(chart_index)
    local_base = _relative_cover_chart(cyclic_algebra, chart_index).coordinate_algebra()
    scalar = local_algebra.algebra_structure_morphism()(local_base(root))
    z = local_algebra.algebra_generator(CYCLIC_COVER_VARIABLE)
    pullback = local_algebra.Mor(local_algebra)(
        {CYCLIC_COVER_VARIABLE: scalar * z}
    )
    local_scheme = cyclic_algebra.relative_spectrum().arrow().domain().chart(chart_index)
    return _affine_morphism_from_pullback(local_scheme, local_scheme, pullback)


def _relative_cyclic_deck_transformation(cyclic_algebra, root_of_unity):
    r"""Glue the chart automorphisms ``z_i -> zeta z_i`` on the relative cover."""
    if not isinstance(cyclic_algebra, CyclicCoverAlgebra):
        raise TypeError("a relative deck transformation requires cyclic-cover algebra data")
    scalar_ring = cyclic_algebra.scheme().scheme_base_ring()
    root = scalar_ring(root_of_unity)
    if root ** int(cyclic_algebra.degree()) != scalar_ring.one():
        raise ValueError("a deck scalar must be an n-th root of unity")

    relative = cyclic_algebra.relative_spectrum()
    glued = relative.arrow().domain()
    local_maps = {}
    for index in _relative_cover_chart_indices(cyclic_algebra):
        local_automorphism = cyclic_algebra.local_deck_transformation(index, root)
        local_maps[index] = glued.chart_embedding(index) * local_automorphism
    automorphism = glued.Mor(glued)(local_maps)
    if any(
        relative.arrow().local_map(index)
        * cyclic_algebra.local_deck_transformation(index, root)
        != relative.arrow().local_map(index)
        for index in _relative_cover_chart_indices(cyclic_algebra)
    ):
        raise ArithmeticError("the deck transformation does not lie over the cyclic-cover base")
    return automorphism


def _cyclic_cover_base_change(cyclic_algebra, ring_map):
    return CyclicCoverBaseChangeComparison(cyclic_algebra, ring_map)


class CyclicCoverBaseChangeComparison(SageObject):
    r"""Scalar change of a finite-atlas cyclic cover with its actual projection."""

    def __init__(self, cyclic_algebra, ring_map) -> None:
        self._source = cyclic_algebra
        self._ring_map = ring_map
        line_bundle = cyclic_algebra.line_bundle()
        branch_power = cyclic_algebra.branch_power()
        changed_line_bundle = line_bundle.base_change(ring_map)
        changed_branch_power = branch_power.base_change(ring_map)
        global_branch = cyclic_algebra.branch_section().global_source_section()
        if global_branch is None:
            raise NotImplementedError(
                "cyclic-cover scalar change currently requires a represented global branch section"
            )
        source_sections = branch_power.global_sections()
        unit = source_sections.base_change_adjunction(ring_map).unit(source_sections)
        extended_branch = unit(global_branch).underlying_element()
        changed_global_branch = (
            changed_branch_power.section_base_change_comparison().forward()(
                extended_branch
            )
        )
        changed_branch = changed_branch_power.compatible_section(changed_global_branch)
        changed_cyclic = type(cyclic_algebra)(
            changed_line_bundle,
            changed_branch,
            cyclic_algebra.degree(),
        )

        source_relative = cyclic_algebra.relative_spectrum()
        changed_relative = changed_cyclic.relative_spectrum()
        source_cover = source_relative.arrow().domain()
        changed_cover = changed_relative.arrow().domain()
        source_atlas = line_bundle.gluing_datum()
        changed_atlas = changed_line_bundle.gluing_datum()
        base_projection = changed_line_bundle.base_change_projection()
        local_projections = {}
        local_maps_to_cover = {}
        for source_index in cyclic_algebra.chart_index_set():
            changed_index = changed_atlas.normalize_chart_index(source_index)
            changed_chart = changed_atlas.chart(changed_index)
            into_source_base = base_projection * changed_atlas.chart_embedding(changed_index)
            chart_projection = source_atlas.chart(source_index).corestriction(
                into_source_base
            )
            base_pullback = chart_projection.coordinate_algebra_morphism()
            source_local = cyclic_algebra.local_algebra(source_index)
            changed_local = changed_cyclic.local_algebra(changed_index)
            source_labels = source_local.module_generating_set()
            changed_labels = changed_local.module_generating_set()
            source_rank = source_labels.ranking_map()

            def image(
                element,
                *,
                source_algebra=source_local,
                target_algebra=changed_local,
                coefficient_map=base_pullback,
                source_ranking=source_rank,
                target_labels=changed_labels,
            ):
                coefficients = source_algebra.framing_coefficients(source_algebra(element))
                result = target_algebra.zero()
                for label, coefficient in coefficients.items():
                    position = int(source_ranking(label))
                    result += target_algebra.scalar_multiple(
                        coefficient_map(coefficient),
                        target_algebra.module_generator(target_labels[position]),
                    )
                return result

            algebra_map = source_local.Mor(changed_local)(image)
            local_projection = _affine_spec_morphism(algebra_map)
            local_projections[source_index] = local_projection
            local_maps_to_cover[source_index] = (
                source_cover.chart_embedding(source_index) * local_projection
            )
        projection = changed_cover.Mor(source_cover)(local_maps_to_cover)
        if any(
            source_relative.arrow().local_map(source_index)
            * local_projections[source_index]
            != base_projection
            * changed_relative.arrow().local_map(
                changed_atlas.normalize_chart_index(source_index)
            )
            for source_index in cyclic_algebra.chart_index_set()
        ):
            raise ArithmeticError(
                "the scalar-changed cyclic-cover projection does not commute with the base projection"
            )
        self._changed_line_bundle = changed_line_bundle
        self._changed_branch_power = changed_branch_power
        self._changed_global_branch = changed_global_branch
        self._changed_cyclic = changed_cyclic
        self._base_projection = base_projection
        self._projection = projection
        from dzack_research.preamble.categories.sets.indexed_families import (
            finite_indexed_family,
        )

        self._local_projections = finite_indexed_family(
            cyclic_algebra.chart_index_set(),
            lambda index: local_projections[index],
            name="Local projections of a scalar-changed cyclic cover",
        )

    def source_cyclic_algebra(self):
        return self._source

    def ring_map(self):
        return self._ring_map

    def changed_line_bundle(self):
        return self._changed_line_bundle

    def changed_branch_power(self):
        return self._changed_branch_power

    def changed_global_branch(self):
        return self._changed_global_branch

    def changed_cyclic_algebra(self):
        return self._changed_cyclic

    def base_projection(self):
        return self._base_projection

    def projection(self):
        return self._projection

    def cover_square_commutes(self) -> bool:
        source = self.source_cyclic_algebra()
        changed = self.changed_cyclic_algebra()
        source_relative = source.relative_spectrum()
        changed_relative = changed.relative_spectrum()
        changed_atlas = self.changed_line_bundle().gluing_datum()
        return all(
            source_relative.arrow().local_map(index) * self.local_projection(index)
            == self.base_projection()
            * changed_relative.arrow().local_map(
                changed_atlas.normalize_chart_index(index)
            )
            for index in source.chart_index_set()
        )

    def local_projection(self, index):
        return self._local_projections[
            self.source_cyclic_algebra().chart_index_set()(index)
        ]

    def lift_commutes(self, source_lift, changed_lift) -> bool:
        if source_lift.cyclic_algebra() is not self.source_cyclic_algebra():
            raise ValueError("the source lift belongs to a different cyclic cover")
        if changed_lift.cyclic_algebra() is not self.changed_cyclic_algebra():
            raise ValueError("the changed lift belongs to a different cyclic cover")
        return all(
            source_lift.local_automorphism(index) * self.local_projection(index)
            == self.local_projection(index) * changed_lift.local_automorphism(index)
            for index in self.source_cyclic_algebra().chart_index_set()
        )

    def deck_commutes(self, root_of_unity) -> bool:
        source = self.source_cyclic_algebra()
        changed = self.changed_cyclic_algebra()
        changed_root = self.ring_map()(
            source.scheme().scheme_base_ring()(root_of_unity)
        )
        return all(
            source.local_deck_transformation(index, root_of_unity)
            * self.local_projection(index)
            == self.local_projection(index)
            * changed.local_deck_transformation(index, changed_root)
            for index in source.chart_index_set()
        )

    def _repr_(self) -> str:
        return f"Cyclic-cover base change along {self.ring_map()} for {self.source_cyclic_algebra()}"



class RelativeCyclicCoverLift(SageObject):
    r"""One lift of a base automorphism through a represented relative cyclic cover."""

    def __init__(
        self,
        cyclic_algebra,
        linearization,
        group_element,
        base_automorphism,
        local_automorphisms,
        automorphism,
    ) -> None:
        self._cyclic_algebra = cyclic_algebra
        self._linearization = linearization
        self._group_element = linearization.acting_group()(group_element)
        self._base_automorphism = base_automorphism
        self._local_automorphisms = local_automorphisms
        self._automorphism = automorphism
        self._fixed_subscheme = None

    def cyclic_algebra(self):
        return self._cyclic_algebra

    def linearization(self):
        return self._linearization

    def group_element(self):
        return self._group_element

    def base_automorphism(self):
        return self._base_automorphism

    def automorphism(self):
        return self._automorphism

    def local_automorphisms(self):
        return self._local_automorphisms

    def local_automorphism(self, index):
        return self.local_automorphisms()[self.cyclic_algebra().chart_index_set()(index)]

    def fiber_scalar(self):
        return self.linearization().character_value(self.group_element()).inverse_of_unit()

    def top_form_scalar(self):
        index = next(iter(self.cyclic_algebra().chart_index_set()))
        determinant = self.linearization().local_jacobian_scalar(
            self.group_element(), index
        )
        return determinant * self.fiber_scalar().inverse_of_unit()

    def fixed_subscheme(self):
        if self._fixed_subscheme is None:
            cover = self.cyclic_algebra().relative_spectrum().arrow().domain()
            self._fixed_subscheme = cover.chartwise_fixed_subscheme(
                self.local_automorphisms()
            )
        return self._fixed_subscheme

    def is_fixed_point_free(self) -> bool:
        return all(
            self.local_automorphism(index).fixed_subscheme().is_empty()
            for index in self.cyclic_algebra().chart_index_set()
        )

    def has_order_two(self) -> bool:
        return all(
            (
                self.local_automorphism(index) * self.local_automorphism(index)
                == self.local_automorphism(index).domain().categorical_identity_morphism()
            )
            for index in self.cyclic_algebra().chart_index_set()
        )

    def _repr_(self) -> str:
        return f"Lift of {self.group_element()} to {self.cyclic_algebra()} over {self.base_automorphism()}"



def _relative_cyclic_cover_lift(cyclic_algebra, linearization, group_element):
    r"""Lift one line-bundle-linearized base automorphism to the cyclic cover.

    If ``lambda_g:g^*L -> L`` is the selected linearization, the generator of
    ``L^{-1}`` transforms through ``lambda_g^{-1}``.  On every chart the ring
    pullback therefore sends ``z`` to ``lambda_g^{-1} z`` and acts on the base
    coefficients through the represented chart automorphism.  The branch
    equation is checked before the local maps are glued.
    """
    if linearization.line_bundle() is not cyclic_algebra.line_bundle():
        raise ValueError("a cyclic-cover lift requires a linearization of its defining line bundle")
    group_element = linearization.acting_group()(group_element)
    base_automorphism = linearization.scheme_action_of(group_element)
    relative = cyclic_algebra.relative_spectrum()
    cover = relative.arrow().domain()
    fiber_scalar = linearization.character_value(group_element).inverse_of_unit()
    local_lifts = {}
    for index in cyclic_algebra.chart_index_set():
        local_base_automorphism = linearization.local_chart_automorphism(
            group_element, index
        )
        base_pullback = local_base_automorphism.coordinate_algebra_morphism()
        local_algebra = cyclic_algebra.local_algebra(index)
        local_base = local_algebra.base_ring()
        scalar = local_base.algebra_structure_morphism()(fiber_scalar)
        branch = cyclic_algebra.local_branch_coefficient(index)
        if base_pullback(branch) != scalar ** int(cyclic_algebra.degree()) * branch:
            raise ValueError(
                "the selected line-bundle lift does not preserve the cyclic-cover branch equation"
            )
        basis_labels = local_algebra.module_generating_set()
        ranking = basis_labels.ranking_map()

        def image(
            element,
            *,
            algebra=local_algebra,
            pullback=base_pullback,
            scale=scalar,
            rank=ranking,
        ):
            coefficients = algebra.framing_coefficients(algebra(element))
            result = algebra.zero()
            for label, coefficient in coefficients.items():
                exponent = int(rank(label))
                result += algebra.scalar_multiple(
                    pullback(coefficient) * scale**exponent,
                    algebra.module_generator(label),
                )
            return result

        pullback = local_algebra.Mor(local_algebra)(image)
        local_scheme = cover.chart(index)
        local_lifts[index] = _affine_morphism_from_pullback(
            local_scheme, local_scheme, pullback
        )
    from dzack_research.preamble.categories.sets.indexed_families import finite_indexed_family

    local_family = finite_indexed_family(
        cyclic_algebra.chart_index_set(),
        lambda index: local_lifts[index],
        name="Local automorphisms of a relative cyclic-cover lift",
    )
    automorphism = cover.Mor(cover)(
        {
            index: cover.chart_embedding(index) * local_family[index]
            for index in cyclic_algebra.chart_index_set()
        }
    )
    if any(
        relative.arrow().local_map(index) * local_family[index]
        != base_automorphism * relative.arrow().local_map(index)
        for index in cyclic_algebra.chart_index_set()
    ):
        raise ArithmeticError("the cyclic-cover lift does not commute with the cover morphism")
    return RelativeCyclicCoverLift(
        cyclic_algebra,
        linearization,
        group_element,
        base_automorphism,
        local_family,
        automorphism,
    )


def _primitive_root_of_unity(scalars, degree):
    r"""Return a primitive ``degree``-th root of unity in ``scalars``.

    The roots of ``t^n - 1`` are computed in the scalars' own polynomial ring
    and one of exact multiplicative order ``n`` is selected.  A primitive root
    exists exactly when the constant group ``C_n`` can act on the cover by
    scaling ``z``; where it does not, the deck group is the group scheme
    ``mu_n`` and this states that rather than substituting a weaker action.
    """
    engine = _engine_ring(scalars)
    assert engine.is_field(), (
        f"{scalars} is not a field, so the roots of unity acting on a cyclic "
        "cover are not selected by this construction"
    )
    characteristic = int(engine.characteristic())
    assert characteristic == 0 or degree % characteristic != 0, (
        f"the characteristic {characteristic} divides the degree {degree}, so "
        "the cover is inseparable and its deck group scheme mu_n is not the "
        "constant group C_n"
    )
    polynomials = engine[_ROOT_OF_UNITY_VARIABLE]
    variable = polynomials.gen()
    primitive = [
        root
        for root, _multiplicity in (variable**degree - polynomials.one()).roots()
        if int(root.multiplicative_order()) == degree
    ]
    assert primitive, (
        f"{scalars} holds no primitive {degree}-th root of unity, so the deck "
        f"group of a degree-{degree} cyclic cover over it is the group scheme "
        "mu_n, which the preamble does not own"
    )
    return scalars._from_engine_element(primitive[0])


class CyclicCovers(OwnedCategory):
    r"""Degree-``n`` cyclic covers of ``Spec(A)``, with their deck action.

    An object is the affine ``A``-scheme ``Spec(A[z]/(z^n - f))`` equipped with
    the deck action of ``C_n``; its structure morphism to the terminal affine
    ``A``-scheme is the finite cover morphism, so a cover is an object of
    ``Sch/Spec(A)`` with no further construction.  The category is a
    subcategory of the affine ``C_n``-schemes over ``A``, which is where the
    common fixed locus and the quotient of an action are already owned; the
    deck fixed locus is the ramification subscheme ``V(z)``, because the
    generator's fixed ideal is generated by ``(zeta - 1) z`` and ``zeta - 1``
    is a unit.
    """

    @staticmethod
    def __classcall__(cls, base_algebra, degree):
        return Category.__classcall__(cls, _own_ring(base_algebra), int(degree))

    def __init__(self, base_algebra, degree) -> None:
        assert degree >= 1, "a cyclic cover has degree at least one"
        self._base_algebra = base_algebra
        self._degree = degree
        OwnedCategory.__init__(self)

    def base_algebra(self):
        r"""Return ``A``, the coordinate algebra of the base."""
        return self._base_algebra

    def base_scheme(self):
        r"""Return ``X = Spec(A)`` as the terminal affine ``A``-scheme."""
        algebra = self.base_algebra()
        return (algebra).affine_spectrum(base_ring=algebra)

    def cover_degree(self):
        r"""Return ``n``, the degree of the covers in this category."""
        return self._degree

    @cached_method
    def deck_group(self):
        r"""Return the canonical deck group scheme ``mu_n``."""
        return AffineGroupSchemes(self.base_algebra()).roots_of_unity(
            self.cover_degree()
        )

    @cached_method
    def deck_group_scheme(self):
        r"""Return the canonical deck group scheme ``mu_n``."""
        return self.deck_group()

    @cached_method
    def constant_deck_group(self):
        r"""Return the abstract cyclic group ``C_n`` for a chosen constant realization."""
        self.deck_root_of_unity()
        return OwnedGroups().C(self.cover_degree())

    @cached_method
    def deck_root_of_unity(self):
        r"""Return the primitive ``n``-th root of unity the deck generator scales by."""
        return _primitive_root_of_unity(
            self.base_algebra().base_ring(),
            self.cover_degree(),
        )

    def super_categories(self):
        return [Schemes(self.base_algebra()).Affine()]

    def _repr_object_names(self):
        return (
            f"degree-{self.cover_degree()} cyclic covers of {self.base_scheme()}"
        )

    def an_object(self):
        r"""The trivial cover ``z^n = 1``, the ``mu_n``-torsor over ``X``."""
        return self(self.base_algebra().one())

    def _call_(self, branch_section):
        r"""Return the cyclic cover branched along ``branch_section``."""
        algebra = self.base_algebra()
        section = algebra(branch_section)
        degree = self.cover_degree()

        cover_algebra = algebra.cyclic_cover_presentation(section, degree)
        cover = (cover_algebra).affine_spectrum()
        image = cover_algebra.algebra_generator(CYCLIC_COVER_VARIABLE)
        group_scheme = self.deck_group_scheme()
        product = cover.scheme_category().product((group_scheme.scheme(), cover))
        product_algebra = product.coordinate_algebra()
        group_pullback = product.projection(0).coordinate_algebra_morphism()
        cover_pullback = product.projection(1).coordinate_algebra_morphism()
        group_coordinate = group_scheme.scheme().coordinate_algebra().algebra_generator("u")
        action_pullback = cover_algebra.Mor(product_algebra)(
            {
                CYCLIC_COVER_VARIABLE: (
                    group_pullback(group_coordinate) * cover_pullback(image)
                )
            }
        )
        action_morphism = _affine_morphism_from_pullback(
            product,
            cover,
            action_pullback,
        )
        group_scheme_action = AffineGroupSchemeActions(group_scheme)(
            cover,
            action_morphism,
        )

        cover._preamble_cyclic_branch_section = section
        cover._preamble_cyclic_cover_degree = degree
        cover._preamble_deck_group_scheme_action = group_scheme_action
        return refine(cover, self)

    class ParentMethods:
        def cover_degree(self):
            r"""Return ``n``: the cover is finite locally free of this rank."""
            return self._preamble_cyclic_cover_degree

        def branch_section(self):
            r"""Return ``f``, the section of ``L^n = O_X`` the cover is branched along."""
            return self._preamble_cyclic_branch_section

        def deck_root_of_unity(self):
            r"""Return a primitive root identifying ``mu_n`` with the constant ``C_n`` here."""
            return CyclicCovers(
                self.scheme_base_ring(),
                self.cover_degree(),
            ).deck_root_of_unity()

        def deck_group_scheme(self):
            r"""Return the canonical deck group scheme ``mu_n``."""
            return CyclicCovers(
                self.scheme_base_ring(),
                self.cover_degree(),
            ).deck_group_scheme()

        def deck_group_scheme_action(self):
            r"""Return the canonical action ``mu_n x X -> X``."""
            return self._preamble_deck_group_scheme_action

        def constant_deck_action(self):
            r"""Return the constant ``C_n`` action selected by a primitive root of unity.

            This is defined precisely when ``deck_root_of_unity()`` succeeds;
            the underlying ``mu_n`` action exists independently of that choice.
            """
            group = CyclicCovers(
                self.scheme_base_ring(),
                self.cover_degree(),
            ).constant_deck_group()
            return AffineGSchemes(group, self.scheme_base_ring())(
                self,
                self.constant_deck_transformation,
            )

        def constant_deck_transformation(self, group_element):
            r"""Return the selected constant deck automorphism of this cover."""
            root_of_unity = self.deck_root_of_unity()
            group = CyclicCovers(
                self.scheme_base_ring(),
                self.cover_degree(),
            ).constant_deck_group()
            generator = group.group_generators()[0]
            degree = self.cover_degree()
            exponents = {}
            element = group.one()
            for exponent in range(degree):
                exponents[element] = exponent
                element = element * generator
            cover_algebra = self.coordinate_algebra()
            scaling = cover_algebra(root_of_unity ** exponents[group_element])
            return Algebras(self.scheme_base_ring()).Associative().Unital().Commutative().spectrum()(
                cover_algebra.Mor(cover_algebra)(
                    {CYCLIC_COVER_VARIABLE: scaling * self.cover_variable()}
                )
            )

        def cover_variable(self):
            r"""Return ``z``, whose ``n``-th power is the branch section."""
            return self.coordinate_algebra().algebra_generator(CYCLIC_COVER_VARIABLE)

        @cached_method
        def branch_subscheme(self):
            r"""Return the branch subscheme ``V(f)`` of the base.

            The cover is étale over the complement of ``V(f)`` and the deck
            action is free there; the ramification subscheme upstairs is the
            deck fixed locus ``V(z)``, which maps isomorphically onto ``V(f)``
            when ``n`` is invertible.
            """
            return self.base_scheme().closed_subscheme(self.branch_section())

        def _require_separable_degree(self):
            characteristic = int(self.scheme_base_ring().characteristic())
            if characteristic != 0 and self.cover_degree() % characteristic == 0:
                raise NotImplementedError(
                    "the represented ramification comparison requires the cyclic degree to be invertible on the base"
                )

        @cached_method
        def ramification_subscheme(self):
            r"""Return the Fitting ramification scheme ``V(n z^(n-1))`` upstairs.

            The cover algebra is ``B=A[z]/(z^n-f)``.  Hence
            ``Omega_{B/A}`` is generated by ``dz`` with relation
            ``n z^(n-1) dz=0``.  In relative dimension zero its nonsmooth
            scheme is therefore ``V(Fitt_0 Omega_{B/A})``.  When ``n`` is a
            unit this has support ``V(z)`` and retains the expected
            ``(n-1)``-fold different for ``n>2``.
            """
            self._require_separable_degree()
            return self.differential_rank_drop_subscheme(0)

        @cached_method
        def ramification_support_subscheme(self):
            r"""Return the reduced-support model ``V(z)`` of the ramification locus."""
            self._require_separable_degree()
            return self.closed_subscheme(self.cover_variable())

        @cached_method
        def ramification_to_branch_morphism(self):
            r"""Return the map from the ramification support to ``V(f)`` downstairs."""
            ramification = self.ramification_support_subscheme()
            branch = self.branch_subscheme()
            into_base = self.structure_morphism() * ramification.inclusion()
            return branch.corestriction(into_base)

        def is_etale_cover(self) -> bool:
            r"""Return whether the supported finite cyclic cover is everywhere étale."""
            ramification = self.ramification_subscheme()
            ideal = ramification.defining_ideal_owned()
            return ideal.contains_ambient_element(self.coordinate_algebra().one())

        def invariant_algebra(self):
            r"""Return ``A``: the deck invariants are the degree-zero summand.

            The ``mu_n``-coaction gives ``A z^i`` weight ``i`` modulo ``n``;
            its invariants are therefore the degree-zero summand ``A``.  No
            primitive root of unity is required, and no invariant-ring
            computation is involved.
            """
            return self.scheme_base_ring()

        def invariant_algebra_inclusion(self):
            r"""Return ``A -> A[z]/(z^n - f)``, the algebra structure morphism."""
            return self.coordinate_algebra().algebra_structure_morphism()

        def affine_quotient(self):
            r"""Return ``X``: a cyclic cover is the quotient map onto its base."""
            return self.base_scheme()

        def quotient_morphism(self):
            r"""Return the cover morphism, which is the deck quotient map."""
            return self.structure_morphism()


__all__ = [
    "CyclicCoverBaseChangeComparison",
    "CyclicCovers",
    "RelativeCyclicCoverLift",
]
