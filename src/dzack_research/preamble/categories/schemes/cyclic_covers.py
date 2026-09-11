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
chart it is the trivialized algebra ``cyclic_cover_presentation`` returns, and
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

from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    Isomorphism,
)
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.algebras.cyclic_cover_algebras import (
    CYCLIC_COVER_VARIABLE,
    CyclicCoverAlgebra,
    cyclic_cover_presentation,
)
from dzack_research.preamble.categories.group.groups import OwnedGroups
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_ring,
    _own_ring,
    ring_morphism,
)
from dzack_research.preamble.categories.schemes.affine_spec import SpecFunctor
from dzack_research.preamble.categories.schemes.group_schemes import (
    AffineGroupSchemeActions,
    roots_of_unity_group_scheme,
)
from dzack_research.preamble.categories.schemes.schemes import (
    AffineGSchemes,
    AffineSchemes,
    Schemes,
    Spec,
    _affine_morphism_from_pullback,
    affine_spec_morphism,
    scheme_product,
)
from dzack_research.preamble.refine import refine

_ROOT_OF_UNITY_VARIABLE = "t"


def _cover_overlap(cyclic_algebra, source_index, target_index):
    r"""Return the distinguished overlap in ``Spec(B_source)`` above ``U_source∩U_target``."""
    cover = cyclic_algebra.cover()
    source_index = cover.chart_label(source_index)
    target_index = cover.chart_label(target_index)
    source_base = cover.open(source_index).coordinate_algebra()
    source_algebra = cyclic_algebra.local_algebra(source_index)
    source_scheme = Spec(source_algebra)
    ambient_element = cover.defining_element(target_index)
    source_element = source_base.localization_map()(ambient_element)
    lifted = source_algebra.algebra_structure_morphism()(source_element)
    return source_scheme.distinguished_open(lifted)


def _overlap_base_to_cover_overlap(
    cyclic_algebra,
    source_index,
    target_index,
    source_open,
):
    r"""Map ``O(U_source∩U_target)`` into the source cover-overlap algebra."""
    cover = cyclic_algebra.cover()
    source_index = cover.chart_label(source_index)
    target_index = cover.chart_label(target_index)
    ambient = cover.ambient_scheme().coordinate_algebra()
    source_base = cover.open(source_index).coordinate_algebra()
    source_algebra = cyclic_algebra.local_algebra(source_index)
    source_open_algebra = source_open.coordinate_algebra()
    ambient_to_source = (
        source_open_algebra.localization_map()
        * source_algebra.algebra_structure_morphism()
        * source_base.localization_map()
    )
    overlap_base = cover.overlap(source_index, target_index).coordinate_algebra()

    def image(element):
        numerator, denominator = overlap_base.localization_fraction_data(element)
        return (
            ambient_to_source(ambient(numerator))
            * ambient_to_source(ambient(denominator)).inverse_of_unit()
        )

    return ring_morphism(overlap_base, source_open_algebra, image)


def _cyclic_cover_transition_morphism(cyclic_algebra, source_index, target_index):
    r"""Return the scheme transition from one cyclic-cover overlap to the other."""
    cover = cyclic_algebra.cover()
    source_index = cover.chart_label(source_index)
    target_index = cover.chart_label(target_index)
    source_open = _cover_overlap(cyclic_algebra, source_index, target_index)
    target_open = _cover_overlap(cyclic_algebra, target_index, source_index)
    source_open_algebra = source_open.coordinate_algebra()
    target_open_algebra = target_open.coordinate_algebra()
    source_algebra = cyclic_algebra.local_algebra(source_index)
    target_algebra = cyclic_algebra.local_algebra(target_index)
    source_z = source_open_algebra.localization_map()(
        source_algebra.algebra_generator(CYCLIC_COVER_VARIABLE)
    )
    overlap_to_source = _overlap_base_to_cover_overlap(
        cyclic_algebra,
        source_index,
        target_index,
        source_open,
    )
    target_base_to_source = overlap_to_source * cover.structure_sheaf_restriction(
        target_index,
        source_index,
    )
    unit = cyclic_algebra.line_bundle().transition_unit(source_index, target_index)
    unit_in_source = overlap_to_source(unit)

    def target_algebra_image(element):
        coefficients = module_coefficients(target_algebra(element), target_algebra)
        result = source_open_algebra.zero()
        for label, coefficient in coefficients.items():
            result += (
                target_base_to_source(coefficient)
                * (unit_in_source * source_z) ** int(label)
            )
        return result

    def target_open_image(element):
        numerator, denominator = target_open_algebra.localization_fraction_data(element)
        return (
            target_algebra_image(numerator)
            * target_algebra_image(denominator).inverse_of_unit()
        )

    pullback = ring_morphism(
        target_open_algebra,
        source_open_algebra,
        target_open_image,
    )
    return _affine_morphism_from_pullback(source_open, target_open, pullback)


def _cyclic_cover_transition(cyclic_algebra, left_index, right_index):
    return Isomorphism(
        _cyclic_cover_transition_morphism(cyclic_algebra, left_index, right_index),
        _cyclic_cover_transition_morphism(cyclic_algebra, right_index, left_index),
    )


def relative_cyclic_cover(cyclic_algebra):
    r"""Return ``Spec_X(⊕ L^{-i}) -> X`` from cyclic algebra descent data."""
    if not isinstance(cyclic_algebra, CyclicCoverAlgebra):
        raise TypeError("relative cyclic cover requires cyclic-cover algebra descent data")
    cover = cyclic_algebra.cover()
    indices = tuple(cover.atlas())
    base_scheme = cyclic_algebra.scheme()
    base_ring = base_scheme.scheme_base_ring()
    charts = {
        index: Spec(cyclic_algebra.local_algebra(index))
        for index in indices
    }
    transitions = {
        (left, right): _cyclic_cover_transition(cyclic_algebra, left, right)
        for position, left in enumerate(indices)
        for right in indices[position + 1 :]
    }
    glued = Schemes(base_ring).glue_affine_atlas(charts, transitions)
    local_maps = {}
    for index in indices:
        local_to_base_chart = affine_spec_morphism(
            cyclic_algebra.local_algebra(index).algebra_structure_morphism()
        )
        local_maps[index] = cover.open(index).inclusion() * local_to_base_chart
    cover_morphism = glued.Mor(base_scheme)(local_maps)
    glued._preamble_cyclic_cover_algebra = cyclic_algebra
    glued._preamble_cyclic_cover_morphism = cover_morphism
    return glued.scheme_category().SliceOver(base_scheme)(cover_morphism)


def local_relative_cyclic_deck_action(cyclic_algebra, chart_index):
    r"""Return the canonical ``mu_n`` action on one affine chart of a relative cyclic cover."""
    if not isinstance(cyclic_algebra, CyclicCoverAlgebra):
        raise TypeError("a local cyclic deck action requires cyclic-cover algebra data")
    cover = cyclic_algebra.cover()
    chart_index = cover.chart_label(chart_index)
    local_base = cover.open(chart_index).coordinate_algebra()
    local_algebra = cyclic_algebra.local_algebra(chart_index)
    local_scheme = Spec(local_algebra)
    group_scheme = roots_of_unity_group_scheme(local_base, int(cyclic_algebra.degree()))
    product = scheme_product(group_scheme.scheme(), local_scheme)
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


def relative_cyclic_deck_transformation(cyclic_algebra, root_of_unity):
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
    for index in cyclic_algebra.cover().atlas():
        local_algebra = cyclic_algebra.local_algebra(index)
        local_scheme = glued.chart(index)
        local_base = cyclic_algebra.cover().open(index).coordinate_algebra()
        scalar = local_algebra.algebra_structure_morphism()(local_base(root))
        z = local_algebra.algebra_generator(CYCLIC_COVER_VARIABLE)
        pullback = local_algebra.Mor(local_algebra)(
            {CYCLIC_COVER_VARIABLE: scalar * z}
        )
        local_automorphism = affine_spec_morphism(pullback)
        local_maps[index] = glued.chart_embedding(index) * local_automorphism
    automorphism = glued.Mor(glued)(local_maps)
    if relative.arrow() * automorphism != relative.arrow():
        raise ArithmeticError("the deck transformation does not lie over the cyclic-cover base")
    return automorphism


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
        return Spec(algebra, base_ring=algebra)

    def cover_degree(self):
        r"""Return ``n``, the degree of the covers in this category."""
        return self._degree

    @cached_method
    def deck_group(self):
        r"""Return the canonical deck group scheme ``mu_n``."""
        return roots_of_unity_group_scheme(
            self.base_algebra(),
            self.cover_degree(),
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
        return [AffineSchemes(self.base_algebra())]

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

        cover_algebra = cyclic_cover_presentation(algebra, section, degree)
        cover = Spec(cover_algebra)
        image = cover_algebra.algebra_generator(CYCLIC_COVER_VARIABLE)
        group_scheme = self.deck_group_scheme()
        product = scheme_product(group_scheme.scheme(), cover)
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
            return SpecFunctor(self.scheme_base_ring())(
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


__all__ = ["CyclicCovers"]
