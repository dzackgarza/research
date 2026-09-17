r"""Toric varieties: schemes built from a fan in a cocharacter lattice.

A toric variety is a normal separated variety \(X\) containing a torus
\(T_N\) as a dense open subset, with the torus action on itself extending to
\(X\).  Every such \(X\) of finite type comes from a fan \(\Sigma\) in
\(N_{\mathbb R}\) (Cox--Little--Schenck, *Toric Varieties*, Cor. 3.1.8), and
the fan is the datum this layer constructs from.

Membership is a fact about how the object was built, never a recognition of
ray coordinates: an object of ``ToricSchemes(k)`` carries its fan, and the
standard identifications (``P^n``, ``P^1 x P^1``, a Hirzebruch surface, a
weighted projective space) are decided by an isomorphism of fans, which by
CLS Thm 3.3.4 is an isomorphism of the varieties.

The affine charts are constructed here, not read off a backend: the chart of
a cone is ``Spec`` of the semigroup algebra of \(S_\sigma=\sigma^\vee\cap M\),
and a face inclusion \(\tau\preceq\sigma\) is realized as the distinguished
open of the chart of \(\sigma\) at one monomial (CLS Prop. 1.3.16).  The
variety is the scheme glued from the charts of the maximal cones along the
transitions of their pairwise intersections, so what a session receives is an
owned glued scheme; Sage's ``ToricVariety`` stays as the private space the
fan-morphism construction computes in.

A transition is the content the charts do not already carry.  Two charts meet
in the chart of \(\gamma=\sigma\cap\tau\), presented on one side as
\(k[S_\sigma][1/\chi^{m_\sigma}]\) and on the other as
\(k[S_\tau][1/\chi^{m_\tau}]\).  Sending each chosen semigroup generator of
\(S_\tau\) to its character on the overlap gives a morphism into the whole
chart \(U_\tau\) that inverts \(\chi^{m_\tau}\), and the universal property of
the localization factors it uniquely through the open.  Reading a character of
\(S_\gamma\) inside \(k[S_\sigma][1/\chi^{m_\sigma}]\) uses
\(S_\gamma=S_\sigma+\mathbb Z_{\ge 0}(-m_\sigma)\), which is the same
Prop. 1.3.16.
"""

from itertools import combinations

from sage.matrix.constructor import matrix as _engine_matrix
from sage.misc.cachefunc import cached_function, cached_method
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ
from sage.schemes.toric.variety import ToricVariety as _SageToricVariety

from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedCategory,
)
from dzack_research.preamble.categories.algebras.semigroup_algebras import (
    AffineSemigroupAlgebras,
)
from dzack_research.preamble.categories.divisors.cartier_divisor_groups import (
    CartierDivisorGroups,
)
from dzack_research.preamble.categories.divisors.chow_groups import (
    ChowGroups,
    TorusInvariantCycleGroups,
    _CycleDegreeConstruction,
)
from dzack_research.preamble.categories.divisors.class_groups import ClassGroups
from dzack_research.preamble.categories.divisors.picard_groups import PicardGroups
from dzack_research.preamble.categories.divisors.weil_divisor_groups import (
    WeilDivisorGroups,
)
from dzack_research.preamble.categories.modules.pure.modules import BilinearMap
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    OwnedIntegralDomains,
    _engine_ring,
    _own_ring,
)
from dzack_research.preamble.categories.schemes.schemes import (
    SchemeMorphism,
    Schemes,
    _has_scheme_placement,
    _categorical_scheme_morphism,
    _refine_scheme,
)
from dzack_research.preamble.categories.schemes.toric.fans import (
    RationalPolyhedralFans,
    _engine_vector,
    _owned_vector,
)
from dzack_research.preamble.categories.schemes.varieties import (
    Curves,
    Surfaces,
    Varieties,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    FiniteOrderedSets,
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    finite_indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import NN


def _integers():
    return _own_ring(SageZZ)


def _ray_generator(ray):
    r"""The primitive generator ``u_rho`` in ``N`` of a one-dimensional cone."""
    return next(iter(ray.rays()))


def _pairing_on_ray(fan, character, ray):
    r"""``<m, u_rho>``, an integer, for a character and a ray of the fan."""
    return fan.character_cocharacter_value(character, _ray_generator(ray))


def _character_names(count):
    r"""Variable names for the semigroup generators of one chart."""
    return tuple(f"z{position}" for position in range(count))


def _semigroup_algebra(cone, base_ring):
    r"""The semigroup algebra ``k[S_sigma]`` of a cone (CLS Prop. 1.1.9).

    \(S_\sigma=\sigma^\vee\cap M\) is a finitely generated affine semigroup by
    Gordan's lemma, and choosing a generating set
    \(\mathcal A=(m_1,\dots,m_s)\) presents its algebra as
    \(k[z_1,\dots,z_s]/I_{\mathcal A}\) with \(I_{\mathcal A}\) the toric ideal
    of the integer matrix whose columns are the \(m_i\).  The toric ideal is
    computed by ``sage.schemes.toric.ideal.ToricIdeal``, whose matrix
    convention is exactly one column per variable.

    The result is an integral domain: \(k[S_\sigma]\) is the subalgebra of the
    group algebra \(k[M]\) spanned by the characters of \(S_\sigma\), and
    \(k[M]\) is a Laurent polynomial ring over a field, so the toric ideal is
    prime.  That placement is what lets a localization of a chart read a
    denominator as a power of the character it inverts, which is how the
    transition out of a face localization is written.
    """
    generators = cone.semigroup_generators()
    return AffineSemigroupAlgebras(base_ring)(
        (
            tuple(_engine_vector(cone.character_lattice(), generator))
            for generator in generators
        ),
        extra_categories=(OwnedIntegralDomains(),),
    )


def _face_supporting_generator_positions(face, cone):
    r"""The positions of the chosen generators of ``S_sigma`` vanishing on ``tau``.

    Those generators generate the face \(\sigma^\vee\cap\tau^\perp\) of
    \(\sigma^\vee\), so any character supported on exactly this selection cuts
    \(\tau\) out of \(\sigma\).
    """
    zero = _integers().zero()
    return tuple(
        position
        for position, generator in enumerate(cone.semigroup_generators())
        if all(value == zero for value in face.pair_with(generator))
    )


def _face_supporting_character(face, cone):
    r"""The character ``m`` with ``sigma cap m^perp = tau`` (CLS Prop. 1.3.16).

    The sum of the chosen semigroup generators of \(S_\sigma\) that vanish on
    \(\tau\): their sum lies in the relative interior of
    \(\sigma^\vee\cap\tau^\perp\), so \(\sigma\cap m^\perp=\tau\).  This is the
    lattice point whose character is inverted to reach \(U_\tau\) inside
    \(U_\sigma\), and ``_face_supporting_character_monomial`` is its monomial.
    """
    characters = cone.character_lattice()
    generators = cone.semigroup_generators()
    supporting = characters.zero()
    for position in _face_supporting_generator_positions(face, cone):
        supporting = supporting + generators[position]
    return supporting


def _face_supporting_character_monomial(face, cone, chart):
    r"""The monomial ``chi^m`` cutting ``face`` out of ``cone`` (CLS Prop. 1.3.16).

    ``m`` is ``_face_supporting_character(face, cone)``, a sum of chosen
    semigroup generators, so in \(k[S_\sigma]\) the character \(\chi^m\) is the
    product of the corresponding variables with no integer program to solve.
    """
    algebra = chart.coordinate_algebra()
    labels = tuple(algebra.algebra_generating_set())
    monomial = algebra.one()
    for position in _face_supporting_generator_positions(face, cone):
        monomial = monomial * algebra.algebra_generator(labels[position])
    return monomial


def _character_monomial(character, cone, chart):
    r"""The monomial ``chi^m`` in ``k[S_sigma]`` of a character of ``S_sigma``.

    ``m`` is a nonnegative integer combination of the chosen semigroup
    generators, and the cone reports one such family of multiplicities; the
    monomial is the corresponding product of variables.  Two expansions of one
    ``m`` differ by the toric ideal, so they name one element of
    \(k[S_\sigma]\) (CLS Prop. 1.1.9).
    """
    algebra = chart.coordinate_algebra()
    labels = tuple(algebra.algebra_generating_set())
    monomial = algebra.one()
    for position, multiplicity in enumerate(cone.semigroup_coefficients(character)):
        monomial = monomial * algebra.algebra_generator(labels[position]) ** int(
            multiplicity
        )
    return monomial


@cached_function
def _affine_chart(cone, base_ring):
    r"""``U_sigma = Spec k[S_sigma]``, one chart per cone and base (CLS Prop. 1.3.9).

    The chart depends on the cone and the base field alone, so it is shared by
    every construction that reaches it: the atlas a toric variety is glued from
    holds exactly the objects its ``affine_chart`` answers with.
    """
    return (_semigroup_algebra(cone, base_ring)).affine_spectrum(base_ring=base_ring)


def _face_localization(face, cone, base_ring):
    r"""``U_tau = D(chi^{m_sigma})`` inside ``U_sigma`` for a face ``tau`` of ``sigma``."""
    chart = _affine_chart(cone, base_ring)
    return chart.distinguished_open(
        _face_supporting_character_monomial(face, cone, chart)
    )


def _character_on_overlap(character, face, cone, base_ring):
    r"""``chi^m`` in ``k[S_sigma][1/chi^{m_sigma}]`` for ``m`` a character of ``S_tau``.

    For \(\tau=\sigma\cap m_\sigma^\perp\) one has
    \(S_\tau=S_\sigma+\mathbb Z_{\ge 0}(-m_\sigma)\) (CLS Prop. 1.3.16), so
    every character of \(S_\tau\) is \(m'=a-c\,m_\sigma\) with \(a\in S_\sigma\)
    and \(c\ge 0\).  Raising \(m'\) by \(m_\sigma\) until it lies in
    \(\sigma^\vee\) finds the least such \(c\), and the search terminates
    because some \(c\) works; the answer is then the monomial of \(a\) divided
    by that power of the inverted character.
    """
    chart = _affine_chart(cone, base_ring)
    localized = _face_localization(face, cone, base_ring).coordinate_algebra()
    supporting = _face_supporting_character(face, cone)
    assert face.dual_cone_contains(character), (
        "a character of the overlap is nonnegative on the common face"
    )
    shifted = character
    exponent = 0
    while not cone.dual_cone_contains(shifted):
        shifted = shifted + supporting
        exponent += 1
    inverse = localized.localization_map()(
        localized.inverted_element()
    ).inverse_of_unit()
    return localized.localization_map()(
        _character_monomial(shifted, cone, chart)
    ) * inverse**exponent


def _face_transition_morphism(face, source_cone, target_cone, base_ring):
    r"""``U_sigma cap U_tau -> U_tau cap U_sigma``, one direction of a transition.

    Both sides are the chart of the common face \(\gamma\), presented as a
    localization of a different semigroup algebra.  Sending each chosen
    semigroup generator of \(S_\tau\) to its character on the overlap is a ring
    morphism out of \(k[S_\tau]\), so a morphism \(U_\sigma\cap U_\tau\to
    U_\tau\); it carries \(\chi^{m_\tau}\) to a unit, so it factors uniquely
    through the open \(U_\tau\cap U_\sigma\).  That factorization is the
    universal property of the localization, taken on the schemes.
    """
    source_open = _face_localization(face, source_cone, base_ring)
    target_open = _face_localization(face, target_cone, base_ring)
    target_chart = _affine_chart(target_cone, base_ring)
    target_algebra = target_chart.coordinate_algebra()
    labels = tuple(target_algebra.algebra_generating_set())
    extension = target_algebra.Mor(source_open.coordinate_algebra())(
        {
            labels[position]: _character_on_overlap(
                generator, face, source_cone, base_ring
            )
            for position, generator in enumerate(target_cone.semigroup_generators())
        }
    )
    return target_open.corestriction(source_open.Mor(target_chart)(extension))


def _face_transition(source_cone, target_cone, base_ring):
    r"""The atlas transition between the charts of two cones of one fan.

    The overlap is the chart of \(\gamma=\sigma\cap\tau\), which is a face of
    each, so it is a distinguished open of both charts and the two directions
    are mutually inverse.  Both presentations invert a character exactly when
    \(\gamma\) is a proper face of each cone, which is what two distinct
    maximal cones of a fan give: a supporting character of \(\sigma\) in
    \(\sigma\) itself lies in \(\sigma^\perp\), where it is already a unit and
    localizing at it says nothing.
    """
    assert not source_cone.is_face_of(target_cone), (
        "a transition joins two cones neither of which is a face of the other"
    )
    assert not target_cone.is_face_of(source_cone), (
        "a transition joins two cones neither of which is a face of the other"
    )
    face = source_cone.intersection(target_cone)
    forward = _face_transition_morphism(face, source_cone, target_cone, base_ring)
    inverse = _face_transition_morphism(face, target_cone, source_cone, base_ring)
    return Schemes(base_ring).Core().Mor(forward.domain(), forward.codomain())(
        forward,
        inverse,
    )


def _pullback_character(character, lattice_morphism, domain_fan, codomain_fan):
    r"""Return ``phi^*(m)`` in the domain character lattice.

    If ``phi:N->N'`` is the cocharacter map, its dual is characterized by
    ``<phi^*m,n>=<m,phi(n)>``.  The chosen frames of the dual lattices make
    these pairings exactly the coordinates of the pulled-back character.
    """
    source_cocharacters = domain_fan.cocharacter_lattice()
    source_characters = domain_fan.character_lattice()
    target_pairing = codomain_fan.character_cocharacter_pairing()
    integers = _integers()
    return source_characters.linear_combination(
        {
            label: integers(
                target_pairing(
                    character,
                    lattice_morphism(source_cocharacters.module_generator(label)),
                )
            )
            for label in source_cocharacters.module_generating_set()
            if integers(
                target_pairing(
                    character,
                    lattice_morphism(source_cocharacters.module_generator(label)),
                )
            )
        }
    )


def _target_maximal_cone(engine_morphism, source_cone, codomain_fan):
    r"""Choose a maximal codomain cone containing the image of ``source_cone``."""
    image = codomain_fan._cone(
        engine_morphism.image_cone(source_cone._engine_cone())
    )
    for candidate in codomain_fan.maximal_cones():
        if image.is_face_of(candidate):
            return candidate
    raise ArithmeticError("a compatible fan morphism has no target cone for a source cone")


def _toric_chart_pullback(lattice_morphism, source_cone, target_cone, base_ring):
    r"""The affine pullback ``k[S_tau] -> k[S_sigma]`` induced by ``phi``.

    For ``phi(sigma) subset tau``, every ``m in S_tau`` pulls back to
    ``phi^*m in S_sigma``.  On the chosen semigroup generators this is the
    character monomial of that pulled-back lattice point.
    """
    source_chart = _affine_chart(source_cone, base_ring)
    target_chart = _affine_chart(target_cone, base_ring)
    source_algebra = source_chart.coordinate_algebra()
    target_algebra = target_chart.coordinate_algebra()
    target_labels = tuple(target_algebra.algebra_generating_set())
    target_generators = target_cone.semigroup_generators()
    domain_fan = source_cone.parent()
    codomain_fan = target_cone.parent()
    return target_algebra.Mor(source_algebra)(
        {
            target_labels[position]: _character_monomial(
                _pullback_character(
                    character,
                    lattice_morphism,
                    domain_fan,
                    codomain_fan,
                ),
                source_cone,
                source_chart,
            )
            for position, character in enumerate(target_generators)
        }
    )


class ToricSchemeMorphism(SchemeMorphism):
    r"""A toric scheme morphism retaining its lattice and affine-chart pullbacks."""

    def __init__(
        self,
        native_morphism,
        *,
        domain,
        codomain,
        lattice_morphism,
        chart_targets,
        chart_pullbacks,
    ) -> None:
        super().__init__(native_morphism, domain=domain, codomain=codomain)
        self._preamble_toric_lattice_morphism = lattice_morphism
        self._preamble_toric_chart_targets = dict(chart_targets)
        self._preamble_toric_chart_pullbacks = dict(chart_pullbacks)

    def lattice_morphism(self):
        return self._preamble_toric_lattice_morphism

    def chart_target(self, source_cone):
        return self._preamble_toric_chart_targets[source_cone]

    def chart_pullback(self, source_cone):
        r"""Return the pullback on the affine chart indexed by ``source_cone``."""
        return self._preamble_toric_chart_pullbacks[source_cone]

    def chart_morphism(self, source_cone):
        r"""Return the represented affine map into the selected target chart."""
        source_chart = self.domain().affine_chart(source_cone)
        target_chart = self.codomain().affine_chart(self.chart_target(source_cone))
        return source_chart.Mor(target_chart)(self.chart_pullback(source_cone))

    def pullback_divisor(self, divisor):
        r"""Pull back one represented torus-invariant Cartier divisor."""
        codomain = self.codomain()
        target_group = codomain.weil_divisor_group()
        divisor = target_group(divisor)
        if not codomain.is_cartier(divisor):
            raise ValueError("toric divisor pullback is represented for Cartier divisors")
        target_rays = codomain.fan().cones(1)
        target_coefficients = target_group.framing_coefficients(divisor)
        zero = _integers().zero()
        engine_divisor = codomain._toric_engine_variety().divisor(
            [int(target_coefficients.get(ray, zero)) for ray in target_rays]
        )
        pulled = self.native_morphism().pullback_divisor(engine_divisor)
        source = self.domain()
        source_group = source.weil_divisor_group()
        source_rays = source.fan().cones(1)
        return source_group.linear_combination(
            {
                ray: _integers()(pulled.coefficient(position))
                for position, ray in enumerate(source_rays)
                if pulled.coefficient(position)
            }
        )

    def pullback_line_bundle(self, bundle):
        r"""Return ``f^* O_Y(D) = O_X(f^*D)`` for a selected toric divisor bundle."""
        if bundle.scheme() is not self.codomain():
            raise ValueError("line-bundle pullback requires a bundle on the morphism codomain")
        return self.domain().invertible_sheaf_of_divisor(
            self.pullback_divisor(bundle.associated_divisor())
        )


def _glued_toric_scheme(fan, base_ring):
    r"""``X_Sigma`` glued from the charts of the maximal cones (CLS Thm. 3.1.5).

    The atlas is indexed by the maximal cones themselves, so a chart is asked
    for by the cone it belongs to, and the transitions are the face
    localizations of the pairwise intersections.
    """
    cones = tuple(fan.maximal_cones())
    return Schemes(base_ring).glue_affine_atlas(
        {cone: _affine_chart(cone, base_ring) for cone in cones},
        tuple(
            _face_transition(source_cone, target_cone, base_ring)
            for source_cone, target_cone in combinations(cones, 2)
        ),
    )


class ToricSchemes(OwnedCategoryOverBaseRing):
    r"""Toric varieties over the stated base field, each equipped with its fan."""

    def an_object(self):
        r"""The projective plane, as the toric variety of the fan of ``P^2``."""

        cocharacters = _integers().free_module(2)
        return RationalPolyhedralFans(cocharacters).projective_space_fan().toric_variety(
            self.base_ring()
        )

    def _repr_object_names(self):
        return f"toric varieties over {self.base_ring()}"

    def super_categories(self):
        return [
            Varieties(self.base_ring()),
            Schemes(self.base_ring()).Normal(),
        ]

    def __contains__(self, candidate) -> bool:
        return candidate in Schemes(self.base_ring()) and _has_scheme_placement(
            candidate, ToricSchemes
        )

    class ParentMethods:
        def fan(self):
            r"""The fan ``Sigma`` in ``N_R`` this variety was built from."""
            return self._preamble_toric_fan

        def toric_fixed_point_blowup(self, center_cone):
            r"""Blow up the torus-fixed point indexed by ``center_cone``."""
            from dzack_research.preamble.categories.schemes.toric.blowups import (
                _toric_fixed_point_blowup,
            )

            return _toric_fixed_point_blowup(self, center_cone)

        def cocharacter_lattice(self):
            r"""The lattice ``N`` of one-parameter subgroups of the torus."""
            return self.fan().cocharacter_lattice()

        def character_lattice(self):
            r"""The lattice ``M`` of characters of the torus."""
            return self.fan().character_lattice()

        def character_cocharacter_pairing(self):
            r"""The perfect pairing ``M ⊗ N -> ZZ``."""
            return self.fan().character_cocharacter_pairing()

        def is_toric(self) -> bool:
            r"""True: an object of this category was built from a fan."""
            return True

        def dimension(self):
            r"""The rank of ``N`` (CLS Thm. 3.1.19)."""
            return self.fan().dimension()

        def relative_dimension(self):
            r"""``dim X_Sigma`` over the base field, which is the rank of ``N``.

            The charts are the spectra of the semigroup algebras of the maximal
            cones, each of dimension ``dim N`` over a field, so the glued scheme
            has that relative dimension (CLS Thm. 3.1.19).
            """
            return self.dimension()

        def _toric_engine_variety(self):
            r"""The private Sage toric space this variety's fan morphisms compute in.

            Protected contract: the toric-morphism construction of this category
            reads it on itself and on the stated codomain, and no session
            receives it.  The variety a session holds is the glued scheme.
            """
            return self._preamble_toric_engine_variety

        def is_smooth(self) -> bool:
            r"""``X_Sigma`` is smooth exactly when every cone is smooth (CLS Thm. 3.1.19)."""
            return self.fan().is_smooth()

        def is_complete(self) -> bool:
            r"""``X_Sigma`` is complete exactly when ``Sigma`` is (CLS Thm. 3.4.1)."""
            return self.fan().is_complete()

        def is_orbifold(self) -> bool:
            r"""``X_Sigma`` has finite quotient singularities iff ``Sigma`` is simplicial."""
            return self.fan().is_simplicial()

        def is_normal(self) -> bool:
            r"""Every toric variety of a fan is normal (CLS Thm. 1.3.5)."""
            return True

        @cached_method
        def torus(self):
            r"""The dense torus ``T_N = Spec k[M]``, the chart of the zero cone."""
            trivial = RationalPolyhedralFans(self.cocharacter_lattice()).trivial_fan()
            return trivial.toric_variety(self.scheme_base_ring())

        def affine_chart(self, cone):
            r"""The affine chart ``U_sigma = Spec k[S_sigma]`` of one cone.

            This is the owned construction from the semigroup algebra, not a
            patch read back from a backend.  For a maximal cone it is the chart
            of the atlas this variety is glued from, the same object
            ``chart(cone)`` answers with.
            """
            assert cone in self.fan(), "an affine chart is taken of a cone of this fan"
            return _affine_chart(cone, self.scheme_base_ring())

        def affine_cover(self):
            r"""The charts of the maximal cones, which cover ``X_Sigma``."""
            return FiniteOrderedSets().from_indexed(
                self.fan().maximal_cones(),
                self.affine_chart,
                name="Affine toric charts",
            )

        def face_localization(self, face, cone):
            r"""The open immersion ``U_tau -> U_sigma`` of a face inclusion.

            For \(\tau\preceq\sigma\) one has \(S_\tau=S_\sigma+\mathbb Z(-m)\)
            for any \(m\in S_\sigma\) with \(\tau=\sigma\cap m^\perp\), so
            \(U_\tau\) is the distinguished open \(D(\chi^m)\subseteq U_\sigma\)
            (CLS Prop. 1.3.16).  These are the maps the charts are glued along.
            """
            assert face.is_face_of(cone), (
                "a face localization is indexed by a face of the cone"
            )
            return _face_localization(face, cone, self.scheme_base_ring())

        def torus_orbits(self, orbit_dimension):
            r"""The torus orbits of the stated dimension, as cones of the fan.

            The orbit-cone correspondence (CLS Thm. 3.2.6) is a bijection
            between the cones of ``Sigma`` and the orbits of the torus action,
            under which a cone of dimension ``k`` indexes an orbit of dimension
            ``n - k``.  The orbits are therefore returned as their cones.
            """
            return self.fan().cones(
                int(self.dimension()) - int(orbit_dimension)
            )

        @cached_method
        def torus_invariant_divisor_group(self):
            r"""``Div_T(X) = ⊕_rho ZZ D_rho``, free on the rays (CLS §4.1).

            The prime divisors are indexed by the rays themselves, which is the
            orbit-cone correspondence restricted to codimension one: ``D_rho``
            is the closure of the orbit of ``rho``.
            """
            module = _integers()._fresh_free_module_on(
                finite_ordered_set(tuple(self.fan().cones(1))),
            )
            return WeilDivisorGroups()(module)

        weil_divisor_group = torus_invariant_divisor_group

        @cached_method
        def cartier_divisor_group(self):
            r"""Return the represented Cartier divisor group in the smooth toric regime.

            On a smooth fan every torus-invariant Weil divisor is Cartier
            (CLS Prop. 4.2.6), hence the selected toric Cartier group has the
            same free presentation as ``Div_T(X)`` but remains a distinct
            divisor-role object.  For singular fans the proper Cartier
            subgroup is not yet represented as one common kernel, so individual
            divisors continue to use ``is_cartier``.
            """
            assert self.fan().is_smooth(), (
                "the represented Cartier divisor group is currently constructed "
                "for a smooth fan, where every invariant Weil divisor is Cartier"
            )
            return CartierDivisorGroups()(self.weil_divisor_group())

        @cached_method
        def cartier_to_weil_morphism(self):
            r"""The inclusion ``CDiv_T(X) -> Div_T(X)`` on a smooth toric variety."""
            cartier = self.cartier_divisor_group()
            weil = self.weil_divisor_group()
            return cartier.module_category().Mor(cartier, weil)(
                {
                    label: weil.module_generator(label)
                    for label in cartier.module_generating_set()
                }
            )

        def torus_invariant_prime_divisor(self, ray):
            r"""The prime divisor ``D_rho`` of one ray of the fan."""
            assert ray in self.fan(), "a torus-invariant prime divisor is indexed by a ray"
            return self.torus_invariant_divisor_group().module_generator(ray)

        def weil_multiplicity(self, divisor, ray):
            r"""Return the coefficient of ``D_rho`` in a torus-invariant Weil divisor."""
            if ray not in self.fan().cones(1):
                raise ValueError("a toric Weil multiplicity is indexed by a ray of the fan")
            group = self.weil_divisor_group()
            coefficients = group.framing_coefficients(group(divisor))
            return coefficients.get(ray, _integers().zero())

        def order_of_character_along_prime_divisor(self, character, ray):
            r"""Return ``ord_{D_rho}(chi^m)=<m,u_rho>`` (CLS Prop. 4.1.2)."""
            character = self.character_lattice()(character)
            if ray not in self.fan().cones(1):
                raise ValueError("a toric valuation is indexed by a ray of the fan")
            return _pairing_on_ray(self.fan(), character, ray)

        def principal_divisor_of_character(self, character):
            r"""Return ``div(chi^m)`` as an element of the represented Weil group."""
            return self.character_divisor_morphism()(self.character_lattice()(character))

        def torus_invariant_divisor_support_subscheme(self, divisor):
            r"""Return the reduced union of torus-invariant primes in an effective divisor.

            On ``U_sigma=Spec k[S_sigma]`` the invariant prime ``D_rho`` for
            ``rho <= sigma`` is generated by the semigroup monomials
            ``chi^m`` with ``<m,u_rho> > 0``.  Intersecting those prime ideals
            gives the scheme-theoretic union of the selected components; the
            common chartwise closed-subscheme owner then glues the result.
            """
            group = self.torus_invariant_divisor_group()
            divisor = group(divisor)
            coefficients = group.framing_coefficients(divisor)
            zero = _integers().zero()
            if any(coefficient < zero for coefficient in coefficients.values()):
                raise ValueError("divisor support here requires an effective torus-invariant divisor")
            selected = tuple(
                ray for ray in self.fan().cones(1)
                if coefficients.get(ray, zero) > zero
            )
            local_closed = {}
            for cone in self.gluing_datum().chart_indices():
                chart = self.affine_chart(cone)
                algebra = chart.coordinate_algebra()
                labels = tuple(algebra.algebra_generating_set())
                ideals = []
                cone_rays = tuple(cone.faces(1))
                for ray in selected:
                    if ray not in cone_rays:
                        continue
                    generators = tuple(
                        algebra.algebra_generator(labels[position])
                        for position, character in enumerate(cone.semigroup_generators())
                        if _pairing_on_ray(self.fan(), character, ray) > zero
                    )
                    ideals.append(algebra.ideal(*generators))
                if not ideals:
                    ideal = algebra.ideal(algebra.one())
                else:
                    ideal = ideals[0]
                    for component_ideal in ideals[1:]:
                        ideal = ideal.intersection(component_ideal)
                local_closed[cone] = chart.closed_subscheme(
                    tuple(ideal.ideal_generators())
                )
            support = self.chartwise_closed_subscheme(
                local_closed,
                name="Support of a torus-invariant divisor",
            )
            support._preamble_toric_support_divisor = divisor
            return support

        @cached_method
        def toric_boundary_divisor(self):
            r"""The toric boundary ``sum_rho D_rho``, the complement of the torus."""
            group = self.torus_invariant_divisor_group()
            return group.linear_combination(
                {ray: _integers().one() for ray in self.fan().cones(1)}
            )

        def canonical_divisor(self):
            r"""``K_X = -sum_rho D_rho`` (CLS Thm. 8.2.3)."""
            return -self.toric_boundary_divisor()

        @cached_method
        def canonical_line_bundle(self):
            r"""Return ``omega_X = O_X(K_X)`` in the represented toric Cartier regime."""
            return self.invertible_sheaf_of_divisor(self.canonical_divisor())

        canonical_bundle = canonical_line_bundle

        @cached_method
        def anticanonical_line_bundle(self):
            r"""Return ``omega_X^{-1} = O_X(-K_X)``."""
            return self.invertible_sheaf_of_divisor(-self.canonical_divisor())

        anticanonical_bundle = anticanonical_line_bundle

        @cached_method
        def character_divisor_morphism(self):
            r"""``M -> Div_T(X)``, ``m |-> div(chi^m)`` (CLS Thm. 4.1.3).

            The principal divisor of a character is
            \(\operatorname{div}(\chi^m)=\sum_\rho\langle m,u_\rho\rangle
            D_\rho\).  This is the map whose cokernel is the class group.
            """
            characters = self.character_lattice()
            group = self.torus_invariant_divisor_group()
            fan = self.fan()
            rays = fan.cones(1)

            def image(label):
                character = characters.module_generator(label)
                return group.linear_combination(
                    {
                        ray: self.order_of_character_along_prime_divisor(
                            character,
                            ray,
                        )
                        for ray in rays
                    }
                )

            return characters.module_category().Mor(characters, group)(image)

        def has_torus_factor(self) -> bool:
            r"""Whether ``X`` splits off a torus factor (CLS Prop. 3.3.9).

            ``X_Sigma`` has a torus factor exactly when the ray generators fail
            to span ``N_R``, and by CLS Thm. 4.1.3 that failure is exactly the
            failure of ``M -> Div_T(X)`` to be injective.
            """
            return not self.character_divisor_morphism().is_injective()

        @cached_method
        def class_group(self):
            r"""``Cl(X) = Div_T(X)/div(chi^M)`` (CLS Thm. 4.1.3).

            The sequence ``M -> Div_T(X) -> Cl(X) -> 0`` is exact for every
            fan, so the class group is this cokernel whether or not ``X`` has a
            torus factor; it is exact on the left exactly when ``X`` has none.
            """
            return ClassGroups()(self.character_divisor_morphism().cokernel())

        @cached_method
        def class_group_projection(self):
            r"""The quotient ``Div_T(X) ->> Cl(X)``.

            The class group is presented on the same prime divisors as
            ``Div_T(X)``, so the quotient sends each generator to the generator
            of the same name.
            """
            group = self.torus_invariant_divisor_group()
            classes = self.class_group()
            return group.module_category().Mor(group, classes)(
                {
                    label: classes.module_generator(label)
                    for label in group.module_generating_set()
                }
            )

        def divisor_class(self, divisor):
            r"""The class in ``Cl(X)`` of a torus-invariant divisor."""
            return self.class_group_projection()(divisor)

        @cached_method
        def local_divisor_group(self, cone):
            r"""``Div_T(U_sigma)``, free on the rays of one cone (CLS §4.1)."""
            return _integers()._fresh_free_module_on(
                finite_ordered_set(tuple(cone.faces(1))),
            )

        @cached_method
        def local_character_divisor_morphism(self, cone):
            r"""``M -> Div_T(U_sigma)``, the principal divisors on one chart."""
            characters = self.character_lattice()
            local = self.local_divisor_group(cone)
            fan = self.fan()
            rays = cone.faces(1)

            def image(label):
                character = characters.module_generator(label)
                return local.linear_combination(
                    {ray: _pairing_on_ray(fan, character, ray) for ray in rays}
                )

            return characters.module_category().Mor(characters, local)(image)

        def local_divisor_restriction(self, divisor, cone):
            r"""``sum_{rho in sigma(1)} -a_rho D_rho`` in ``Div_T(U_sigma)``.

            This is the right-hand side of the Cartier equations
            ``<m_sigma, u_rho> = -a_rho`` (CLS Thm. 4.2.8).
            """
            group = self.torus_invariant_divisor_group()
            coefficients = group.framing_coefficients(divisor)
            zero = _integers().zero()
            local = self.local_divisor_group(cone)
            return local.linear_combination(
                {ray: -coefficients.get(ray, zero) for ray in cone.faces(1)}
            )

        def is_cartier(self, divisor) -> bool:
            r"""Whether ``D = sum a_rho D_rho`` is Cartier (CLS Thm. 4.2.8).

            ``D`` is Cartier exactly when every maximal cone ``sigma`` admits
            ``m_sigma`` in ``M`` with ``<m_sigma, u_rho> = -a_rho`` for every
            ``rho`` in ``sigma(1)``; that is, exactly when the local
            coefficient divisor lies in the image of ``M -> Div_T(U_sigma)``.
            Membership in that image is decided by the cokernel of the map.
            """
            for cone in self.fan().maximal_cones():
                quotient = self.local_character_divisor_morphism(cone).cokernel()
                image = quotient.cokernel_projection()(
                    self.local_divisor_restriction(divisor, cone)
                )
                if image != quotient.zero():
                    return False
            return True

        def cartier_datum(self, divisor, cone):
            r"""``m_sigma`` in ``M`` with ``<m_sigma, u_rho> = -a_rho`` on ``sigma(1)``.

            This is the Cartier datum of ``D`` on the chart of ``sigma`` (CLS
            Thm. 4.2.8): the character whose principal divisor cancels ``D``
            there, so that ``D`` is cut out by ``chi^{-m_sigma}`` on
            ``U_sigma``.  It is a preimage under ``M -> Div_T(U_sigma)``, and
            it is unique when ``sigma`` is full-dimensional.
            """
            assert self.is_cartier(divisor), (
                "the Cartier datum of a divisor exists where the divisor is Cartier"
            )
            return self.local_character_divisor_morphism(cone).lift(
                self.local_divisor_restriction(divisor, cone)
            )

        def is_basepoint_free(self, divisor) -> bool:
            r"""Whether ``O_X(D)`` is generated by its global sections (CLS Thm. 6.1.7).

            On a complete fan this is convexity of the support function of a
            Cartier divisor: ``<m_sigma, u_rho> >= -a_rho`` for every maximal
            cone ``sigma`` and every ray ``rho`` of the fan.
            """
            assert self.fan().is_complete(), (
                "convexity of a support function is stated on a complete fan"
            )
            if not self.is_cartier(divisor):
                return False
            fan = self.fan()
            group = self.torus_invariant_divisor_group()
            coefficients = group.framing_coefficients(divisor)
            zero = _integers().zero()
            for cone in fan.maximal_cones():
                character = self.cartier_datum(divisor, cone)
                for ray in fan.cones(1):
                    if _pairing_on_ray(fan, character, ray) < -coefficients.get(
                        ray, zero
                    ):
                        return False
            return True

        def is_ample(self, divisor) -> bool:
            r"""Whether ``D`` is ample (CLS Thm. 6.1.14).

            On a complete fan this is strict convexity of the support function
            of a Cartier divisor: ``<m_sigma, u_rho> > -a_rho`` for every
            maximal cone ``sigma`` and every ray ``rho`` that is not a face of
            ``sigma``.
            """
            assert self.fan().is_complete(), (
                "strict convexity of a support function is stated on a complete fan"
            )
            if not self.is_cartier(divisor):
                return False
            fan = self.fan()
            group = self.torus_invariant_divisor_group()
            coefficients = group.framing_coefficients(divisor)
            zero = _integers().zero()
            for cone in fan.maximal_cones():
                character = self.cartier_datum(divisor, cone)
                for ray in fan.cones(1):
                    if ray.is_face_of(cone):
                        continue
                    if _pairing_on_ray(fan, character, ray) <= -coefficients.get(
                        ray, zero
                    ):
                        return False
            return True

        @cached_method
        def picard_group(self):
            r"""``Pic(X) = CDiv_T(X)/M`` (CLS Thm. 4.2.1).

            On a smooth fan every torus-invariant Weil divisor is Cartier (CLS
            Prop. 4.2.6), so ``CDiv_T(X) = Div_T(X)`` and the Picard group is
            the quotient this returns.  On a fan that is not smooth
            ``CDiv_T(X)`` is the proper subgroup that ``is_cartier`` decides one
            divisor at a time; constructing that subgroup is a kernel out of the
            free divisor group into a finitely presented cokernel, and the
            module layer represents kernels only between free modules.
            """
            assert self.fan().is_smooth(), (
                "the Picard group is constructed on a smooth fan, where every "
                "Weil divisor is Cartier; on a singular fan ask is_cartier of "
                "the divisors in question, since the group of torus-invariant "
                "Cartier divisors has no represented construction"
            )
            return PicardGroups()(self.character_divisor_morphism().cokernel())

        @cached_method
        def cartier_class_projection(self):
            r"""The quotient ``CDiv_T(X) ->> Pic(X)`` in the smooth toric regime."""
            cartier = self.cartier_divisor_group()
            picard = self.picard_group()
            return cartier.module_category().Mor(cartier, picard)(
                {
                    label: picard.module_generator(label)
                    for label in cartier.module_generating_set()
                }
            )

        @cached_method
        def picard_to_class_group_morphism(self):
            r"""The natural comparison ``Pic(X) -> Cl(X)`` for a smooth toric variety.

            Since every invariant Weil divisor is Cartier on a smooth fan, the
            comparison is an isomorphism.  The two quotient-role objects retain
            the same presentation; this map records the comparison rather than
            identifying them by object identity.
            """
            picard = self.picard_group()
            classes = self.class_group()
            forward = picard.module_category().Mor(picard, classes)(
                {
                    label: classes.module_generator(label)
                    for label in picard.module_generating_set()
                }
            )
            inverse = classes.module_category().Mor(classes, picard)(
                {
                    label: picard.module_generator(label)
                    for label in classes.module_generating_set()
                }
            )
            return picard.module_category().Core().Mor(picard, classes)(forward, inverse)

        def divisor_polytope(self, divisor):
            r"""``P_D = {m in M_R : <m,u_rho> >= -a_rho for all rho}`` (CLS (4.3.2)).

            For an ample divisor this is the polytope whose normal fan is
            ``Sigma``, so it recovers the polarizing polytope of a variety
            built from one.
            """
            from dzack_research.preamble.categories.schemes.polytopes import (
                ConvexPolytopes,
            )

            assert self.fan().is_complete(), (
                "the polytope of a divisor is bounded on a complete fan"
            )
            group = self.torus_invariant_divisor_group()
            coefficients = group.framing_coefficients(divisor)
            zero = _integers().zero()
            cocharacters = self.cocharacter_lattice()
            halfspaces = tuple(
                (
                    coefficients.get(ray, zero),
                    tuple(_engine_vector(cocharacters, _ray_generator(ray))),
                )
                for ray in self.fan().cones(1)
            )
            return ConvexPolytopes().from_halfspaces(
                halfspaces,
                lattice=self.character_lattice(),
            )

        @cached_method
        def polarizing_divisor(self):
            r"""Return the torus-invariant Cartier divisor whose polytope is the selected ``P``.

            If ``P`` has normal fan ``Sigma`` then its support numbers are
            ``a_rho=-min_{m in P}<m,u_rho>``.  Thus
            ``P=P_D`` for ``D=sum a_rho D_rho``.  This is the inverse direction
            to :meth:`divisor_polytope` for a toric variety constructed from a
            chosen lattice polytope.
            """
            if not self.is_polarized():
                raise ValueError("a polarizing divisor requires the polytope selected at construction")
            polytope = self.polarizing_polytope()
            characters = self.character_lattice()
            group = self.torus_invariant_divisor_group()
            coefficients = {}
            for ray in self.fan().cones(1):
                values = tuple(
                    _pairing_on_ray(self.fan(), characters(vertex), ray)
                    for vertex in polytope.vertices()
                )
                coefficients[ray] = -min(values)
            divisor = group.linear_combination(coefficients)
            if not self.is_cartier(divisor):
                raise ArithmeticError("the divisor reconstructed from a lattice polytope is not Cartier")
            return divisor

        def compatible_divisor_section(self, divisor, section, *, line_bundle=None):
            r"""Descend one character-basis section of ``O(D)`` to the toric affine atlas.

            On ``U_sigma`` the Cartier datum ``m_sigma`` trivializes ``O(D)``.
            Hence the global character ``chi^m`` has local coefficient
            ``chi^(m-m_sigma)``.  The common finite-atlas equalizer verifies
            these coefficients against the line-bundle transition functions.
            """
            divisor = self.torus_invariant_divisor_group()(divisor)
            if not self.is_cartier(divisor):
                raise ValueError("character-section descent requires a Cartier divisor")
            selected_line = self.invertible_sheaf_of_divisor(divisor) if line_bundle is None else line_bundle
            if selected_line.scheme() is not self:
                raise ValueError("the selected line bundle belongs to a different toric scheme")
            if selected_line.associated_divisor() != divisor:
                raise ValueError("the selected line bundle represents a different toric divisor")
            sections = self.divisor_section_space(divisor)
            section = sections(section)
            coefficients = sections.framing_coefficients(section)
            module_sheaf = selected_line.module_sheaf()
            local_components = {}
            for cone in self.gluing_datum().chart_indices():
                chart = self.affine_chart(cone)
                chart_ring = chart.coordinate_algebra()
                scalar_map = chart_ring.algebra_structure_morphism()
                cartier = self.cartier_datum(divisor, cone)
                local_coefficient = chart_ring.zero()
                for character, coefficient in coefficients.items():
                    shifted = self.character_lattice()(character) - cartier
                    if not cone.dual_cone_contains(shifted):
                        raise ArithmeticError("a global toric section is not regular in one Cartier trivialization")
                    local_coefficient += scalar_map(coefficient) * _character_monomial(
                        shifted,
                        cone,
                        chart,
                    )
                module = module_sheaf.sections_on_chart(cone)
                generator = module.module_generator(next(iter(module.module_generating_set())))
                local_components[cone] = module.scalar_multiple(local_coefficient, generator)
            return selected_line.compatible_sections()(local_components)

        def zero_subscheme_of_divisor_section(self, divisor, section, *, line_bundle=None):
            r"""Return the effective Cartier zero scheme of a represented toric section."""
            divisor = self.torus_invariant_divisor_group()(divisor)
            selected_line = self.invertible_sheaf_of_divisor(divisor) if line_bundle is None else line_bundle
            compatible = self.compatible_divisor_section(
                divisor,
                section,
                line_bundle=selected_line,
            )
            local_closed = {}
            for cone in self.gluing_datum().chart_indices():
                module = selected_line.module_sheaf().sections_on_chart(cone)
                label = next(iter(module.module_generating_set()))
                coefficient = module.framing_coefficients(compatible.component(cone)).get(
                    label,
                    module.base_ring().zero(),
                )
                local_closed[cone] = self.affine_chart(cone).closed_subscheme(coefficient)
            closed = self.chartwise_closed_subscheme(
                local_closed,
                name="Zero scheme of a toric divisor section",
            )
            closed._preamble_defining_toric_section = section
            closed._preamble_defining_toric_divisor = divisor
            closed._preamble_defining_line_bundle = selected_line
            return closed

        def divisor_section_characters(self, divisor):
            r"""The characters spanning ``H^0(X, O_X(D))`` (CLS Prop. 4.3.3).

            ``H^0(X,O_X(D))`` has the characters ``chi^m`` for ``m`` a lattice
            point of ``P_D`` as a basis, so the lattice points of the divisor
            polytope are returned as elements of ``M``.
            """
            characters = self.character_lattice()
            return FiniteOrderedSets().from_indexed(
                self.divisor_polytope(divisor).integral_points(),
                lambda point: _owned_vector(characters, point),
                name="Section characters",
            )

        @cached_method
        def divisor_section_space(self, divisor):
            r"""Return ``H^0(X,O_X(D))`` with the character basis of ``P_D cap M``.

            For a torus-invariant Cartier divisor on a complete toric variety,
            the characters ``chi^m`` with ``m`` a lattice point of ``P_D`` form
            a basis of global sections (CLS Prop. 4.3.3).  The represented
            vector space therefore uses those actual character-lattice elements
            as its basis labels rather than replacing them by positions.
            """
            if not self.is_cartier(divisor):
                raise ValueError("the represented section space requires a Cartier divisor")
            return self.scheme_base_ring().free_module(self.divisor_section_characters(divisor))

        def cox_monomial_of_section(self, divisor, character):
            r"""Return the Cox monomial representing ``chi^m`` as a section of ``O(D)``.

            For ``D=sum a_rho D_rho`` and ``m in P_D cap M``, the homogeneous
            Cox monomial is ``prod x_rho^(<m,u_rho>+a_rho)``.  Membership in
            ``P_D`` is exactly the nonnegativity of these exponents.
            """
            divisor = self.weil_divisor_group()(divisor)
            character = self.character_lattice()(character)
            sections = self.divisor_section_characters(divisor)
            if character not in sections:
                raise ValueError("the character is not a global section of the stated divisor")
            cox = self.cox_ring()
            coefficients = self.weil_divisor_group().framing_coefficients(divisor)
            zero = _integers().zero()
            monomial = cox.one()
            for label in cox.algebra_generating_set():
                ray = cox.cox_rays()[label]
                exponent = self.order_of_character_along_prime_divisor(character, ray)
                exponent += coefficients.get(ray, zero)
                if exponent < zero:
                    raise ArithmeticError("a divisor-polytope section produced a negative Cox exponent")
                monomial *= cox.algebra_generator(label) ** int(exponent)
            return monomial

        @cached_method
        def homogeneous_polynomial_section_space(self, divisor):
            r"""Return ``H^0(X,O(D))`` with its actual Cox monomials as basis labels."""
            divisor = self.weil_divisor_group()(divisor)
            characters = self.divisor_section_characters(divisor)
            monomials = FiniteOrderedSets().from_indexed(
                characters,
                lambda character: self.cox_monomial_of_section(divisor, character),
                name="Homogeneous Cox monomial sections",
            )
            return self.scheme_base_ring().free_module(monomials)

        @cached_method
        def section_homogeneous_polynomial_isomorphism(self, divisor):
            r"""Identify character sections with homogeneous Cox polynomials linearly."""
            divisor = self.weil_divisor_group()(divisor)
            source = self.divisor_section_space(divisor)
            target = self.homogeneous_polynomial_section_space(divisor)
            forward = source.module_category().Mor(source, target)(
                {
                    character: target.module_generator(
                        self.cox_monomial_of_section(divisor, character)
                    )
                    for character in source.module_generating_set()
                }
            )
            inverse = target.module_category().Mor(target, source)(
                {
                    monomial: source.module_generator(character)
                    for character, monomial in zip(
                        source.module_generating_set(),
                        target.module_generating_set(),
                        strict=True,
                    )
                }
            )
            return source.module_category().Core().Mor(source, target)(forward, inverse)

        def complete_linear_system(self, divisor):
            r"""Return ``|D|`` as the projectivization of the represented section space."""
            from dzack_research.preamble.categories.divisors.linear_systems import (
                _complete_linear_system,
            )

            return _complete_linear_system(
                self,
                self.weil_divisor_group()(divisor),
                self.divisor_section_space(divisor),
            )

        def _engine_toric_divisor(self, divisor):
            r"""Return Sage's private toric divisor with the same ray coefficients."""
            divisor = self.weil_divisor_group()(divisor)
            coefficients = [
                int(self.weil_multiplicity(divisor, ray))
                for ray in self.fan().cones(1)
            ]
            return self._toric_engine_variety().divisor(coefficients)

        def associated_projective_morphism(self, divisor):
            r"""Return the morphism ``phi_|D|: X -> |D|`` for a basepoint-free divisor.

            The monomial basis of ``H^0(X,O_X(D))`` indexed by ``P_D cap M``
            is the same basis used by Sage's toric divisor engine.  Evaluating
            those sections in homogeneous Cox coordinates gives the Kodaira
            map to the ambient projective space of the complete linear system.
            Basepoint-freeness is the exact condition ensuring this rational
            map is everywhere defined.
            """
            divisor = self.weil_divisor_group()(divisor)
            if not self.is_basepoint_free(divisor):
                raise ValueError(
                    "the associated projective map is a morphism only for a basepoint-free divisor"
                )
            system = self.complete_linear_system(divisor)
            sections = self._engine_toric_divisor(divisor).sections_monomials()
            native = self._toric_engine_variety().Hom(system)(list(sections))
            result = _categorical_scheme_morphism(
                native,
                domain=self,
                codomain=system,
            )
            return result

        def weight_cohomology_complex(self, divisor, weight):
            r"""Return the finite complex computing one toric line-bundle weight piece."""
            from dzack_research.preamble.categories.schemes.geometric_cohomology import (
                _toric_weight_cohomology_complex,
            )

            return _toric_weight_cohomology_complex(self, divisor, weight)

        def weight_cohomology(self, divisor, weight, degree):
            r"""Return one weight piece ``H^degree(X,O_X(D))_weight``."""
            from dzack_research.preamble.categories.schemes.geometric_cohomology import (
                _toric_weight_cohomology,
            )

            return _toric_weight_cohomology(self, divisor, weight, degree)

        def weight_scalar_cochain_map(self, divisor, weight, scalar):
            r"""Return scalar multiplication on the selected toric weight complex."""
            from dzack_research.preamble.categories.schemes.geometric_cohomology import (
                _toric_weight_scalar_cochain_map,
            )

            return _toric_weight_scalar_cochain_map(self, divisor, weight, scalar)

        def weight_scalar_cohomology_map(self, divisor, weight, degree, scalar):
            r"""Return the cohomology map induced by scalar multiplication on a weight complex."""
            from dzack_research.preamble.categories.schemes.geometric_cohomology import (
                _toric_weight_scalar_cohomology_map,
            )

            return _toric_weight_scalar_cohomology_map(
                self, divisor, weight, degree, scalar
            )

        @cached_method
        def line_bundle_cohomology(self, divisor, degree):
            r"""Return ``H^degree(X,O_X(D))`` from the represented toric weight complexes."""
            from dzack_research.preamble.categories.schemes.geometric_cohomology import (
                _toric_line_bundle_cohomology,
            )

            return _toric_line_bundle_cohomology(self, divisor, degree)

        def line_bundle_cohomology_dimensions(self, divisor):
            r"""Return the degree-indexed dimensions of represented ``H^i(X,O_X(D))``."""
            degrees = finite_ordered_set(
                tuple(NN(degree) for degree in range(int(self.dimension()) + 1))
            )
            return finite_indexed_family(
                degrees,
                lambda degree: NN(
                    self.line_bundle_cohomology(divisor, int(degree)).dimension()
                ),
                name=f"Line-bundle cohomology dimensions of {divisor}",
            )

        @cached_method
        def integral_singular_cohomology(self, degree):
            r"""Return ``H^degree(X(CC),ZZ)`` in the supported smooth complete toric ``QQ`` regime."""
            from dzack_research.preamble.categories.schemes.geometric_cohomology import (
                _toric_integral_singular_cohomology,
            )

            return _toric_integral_singular_cohomology(self, degree)

        @cached_method
        def cycle_class_isomorphism(self, codimension):
            r"""Return the integral cycle-class isomorphism in the supported toric complex realization."""
            from dzack_research.preamble.categories.schemes.geometric_cohomology import (
                _toric_cycle_class_isomorphism,
            )

            return _toric_cycle_class_isomorphism(self, codimension)

        @cached_method
        def picard_to_chow_isomorphism(self):
            r"""Return ``Pic(X) -> CH^1(X)`` in the represented smooth complete surface regime."""
            from dzack_research.preamble.categories.schemes.geometric_cohomology import (
                _toric_picard_to_chow_isomorphism,
            )

            return _toric_picard_to_chow_isomorphism(self)

        @cached_method
        def middle_cohomology_form(self):
            r"""Return the cup-product form on ``H^2(X(CC),ZZ)`` for a smooth complete toric surface."""
            from dzack_research.preamble.categories.schemes.geometric_cohomology import (
                _toric_middle_cohomology_form,
            )

            return _toric_middle_cohomology_form(self)

        @cached_method
        def fundamental_group(self, base_point_cone=None):
            r"""Return the pointed fundamental group of the supported complex realization."""
            from dzack_research.preamble.categories.schemes.geometric_cohomology import (
                _toric_fundamental_group,
            )

            return _toric_fundamental_group(self, base_point_cone)

        @cached_method
        def hodge_structure(self):
            r"""Return the pure Hodge-number data tied to the integral cohomology objects."""
            from dzack_research.preamble.categories.schemes.geometric_cohomology import (
                _toric_hodge_structure,
            )

            return _toric_hodge_structure(self)

        def invertible_sheaf_of_divisor(self, divisor):
            r"""Return ``O_X(D)`` from the Cartier characters on the toric atlas.

            If ``m_sigma`` is the selected Cartier datum on ``U_sigma``, then
            ``chi^{m_sigma}`` is the local generator of ``O_X(D)``.  Hence on
            ``U_sigma cap U_tau`` the transition is
            ``chi^(m_sigma-m_tau)``.  These differences vanish on the common
            face, so the characters are units on the overlap and satisfy the
            cocycle additively.
            """
            from dzack_research.preamble.categories.divisors.invertible_sheaves import (
                FiniteAtlasInvertibleSheaf,
            )

            divisor = self.weil_divisor_group()(divisor)
            if not self.is_cartier(divisor):
                raise ValueError("an associated invertible sheaf requires a Cartier divisor")
            datum = self.gluing_datum()
            units = {}
            for source_cone, target_cone in datum.transition_index_set():
                face = source_cone.intersection(target_cone)
                difference = self.cartier_datum(divisor, source_cone) - self.cartier_datum(
                    divisor,
                    target_cone,
                )
                units[source_cone, target_cone] = _character_on_overlap(
                    difference,
                    face,
                    source_cone,
                    self.scheme_base_ring(),
                )
            section_space = (
                self.divisor_section_space(divisor)
                if self.fan().is_complete()
                else None
            )
            return FiniteAtlasInvertibleSheaf(
                datum,
                units,
                section_space=section_space,
                associated_divisor=divisor,
            )

        @cached_method
        def hyperplane_divisor(self):
            r"""Return a torus-invariant hyperplane divisor on toric ``P^n``.

            Every ray divisor on the standard projective-space fan represents
            the positive generator of ``Pic(P^n)``.  Thus after the exact fan
            identification performed by ``is_projective_space``, selecting the
            first ray gives one distinguished representative of that class.
            """
            assert self.is_projective_space(), (
                "the hyperplane divisor constructor is supported on a toric projective space"
            )
            ray = next(iter(self.fan().cones(1)))
            return self.torus_invariant_prime_divisor(ray)

        @cached_method
        def hyperplane_line_bundle(self):
            r"""Return ``O_{P^n}(1)`` from the selected hyperplane divisor."""
            return self.invertible_sheaf_of_divisor(self.hyperplane_divisor())

        O1 = hyperplane_line_bundle

        def ample_divisor_self_intersection(self, divisor):
            r"""Return ``D^2`` from the normalized area of ``P_D``.

            On a smooth complete toric surface a nef divisor satisfies
            ``D^2 = Vol(P_D)`` for lattice-normalized volume.  The supported
            interface asks for ampleness, which implies nefness and is already
            decided by the toric support-function criterion above.
            """
            assert int(self.dimension()) == 2, (
                "this intersection-number specialization is for toric surfaces"
            )
            assert self.fan().is_smooth() and self.fan().is_complete(), (
                "polytope self-intersection is represented here on a smooth complete toric surface"
            )
            assert self.is_ample(divisor), (
                "the represented polytope intersection formula currently requires an ample divisor"
            )
            return self.divisor_polytope(divisor).normalized_volume()

        def ample_divisor_intersection(self, left, right):
            r"""Return ``left . right`` by polarization on a smooth complete toric surface."""
            group = self.weil_divisor_group()
            left = group(left)
            right = group(right)
            assert self.is_ample(left) and self.is_ample(right), (
                "the represented mixed intersection currently requires two ample Cartier divisors"
            )
            numerator = (
                self.ample_divisor_self_intersection(left + right)
                - self.ample_divisor_self_intersection(left)
                - self.ample_divisor_self_intersection(right)
            )
            quotient, remainder = numerator.quo_rem(_integers()(2))
            if remainder != _integers().zero():
                raise ArithmeticError("polarization of an integral intersection form was not even")
            return quotient

        def divisor_intersection(self, left, right):
            r"""Return ``left . right`` on a smooth complete toric surface.

            The private Sage toric cohomology ring computes the exact divisor
            classes and integration.  The public result is crossed back to the
            owned integer ring; smoothness guarantees integrality.
            """
            if int(self.dimension()) != 2:
                raise ValueError("the represented divisor intersection pairing is for surfaces")
            if not self.fan().is_smooth() or not self.fan().is_complete():
                raise ValueError("the represented divisor intersection requires a smooth complete toric surface")
            group = self.weil_divisor_group()
            left = group(left)
            right = group(right)
            rays = self.fan().cones(1)
            zero = _integers().zero()

            def engine_divisor(divisor):
                coefficients = group.framing_coefficients(divisor)
                return self._toric_engine_variety().divisor(
                    [int(coefficients.get(ray, zero)) for ray in rays]
                )

            engine = self._toric_engine_variety()
            cohomology = engine.cohomology_ring()
            value = engine.integrate(
                cohomology(engine_divisor(left)) * cohomology(engine_divisor(right))
            )
            return _integers()(value)

        @cached_method
        def picard_intersection_pairing(self):
            r"""Return the integral intersection pairing on ``Pic(X)`` for a smooth complete toric surface."""
            if int(self.dimension()) != 2:
                raise ValueError("the Picard intersection pairing is represented for surfaces")
            if not self.fan().is_smooth() or not self.fan().is_complete():
                raise ValueError("the Picard intersection pairing requires a smooth complete toric surface")
            picard = self.picard_group()
            weil = self.weil_divisor_group()
            integers = _integers()
            values = integers.regular_module()
            return BilinearMap(
                picard,
                picard,
                values,
                lambda left_label, right_label: self.divisor_intersection(
                    weil.module_generator(left_label),
                    weil.module_generator(right_label),
                ),
            )

        @cached_method
        def chow_group(self, cycle_dimension):
            r"""Return the integral Chow group ``A_k(X)`` in the selected degree.

            Orbit closures generate the full Chow group of a toric variety,
            and Sage's toric Chow implementation computes their exact rational-
            equivalence quotient, including integral torsion.  The backend
            returns a finitely generated ``ZZ``-module in invariant-factor
            form; crossing those invariants back through a diagonal owned
            presentation keeps the computation private while the public result
            remains an owned module carrying ``X`` and ``k``.
            """
            cycle_dimension = int(cycle_dimension)
            dimension = int(self.dimension())
            if cycle_dimension < 0 or cycle_dimension > dimension:
                raise ValueError("a Chow-group degree lies between zero and the scheme dimension")
            engine = self._toric_engine_variety().Chow_group().degree(cycle_dimension).module()
            invariants = tuple(int(value) for value in engine.invariants())
            integers = _integers()
            rank = len(invariants)
            free = integers.free_module(rank)
            relations = integers.free_module(rank)
            relation = relations.module_category().Mor(relations, free)(
                {
                    position: (
                        integers(invariant) * free.module_generator(position)
                        if invariant != 0
                        else free.zero()
                    )
                    for position, invariant in enumerate(invariants)
                }
            )

            module = relation.cokernel()
            return ChowGroups(module.base_ring())(
                module,
                self,
                cycle_dimension,
            )

        @cached_method
        def torus_invariant_cycle_group(self, cycle_dimension):
            r"""Return the free group on orbit closures of dimension ``cycle_dimension``."""
            cycle_dimension = int(cycle_dimension)
            dimension = int(self.dimension())
            if cycle_dimension < 0 or cycle_dimension > dimension:
                raise ValueError("a cycle degree lies between zero and the scheme dimension")
            cone_dimension = dimension - cycle_dimension
            return _integers()._fresh_free_module_on(
                self.fan().cones(cone_dimension),
                _extra_categories=(TorusInvariantCycleGroups(_integers()),),
                _extra_construction_data=(
                    (
                        "_cycle_degree_construction",
                        _CycleDegreeConstruction(self, cycle_dimension),
                    ),
                ),
            )

        @cached_method
        def torus_invariant_cycle_class_map(self, cycle_dimension):
            r"""Return the rational-equivalence quotient from invariant cycles to ``CH_k(X)``."""
            cycle_dimension = int(cycle_dimension)
            source = self.torus_invariant_cycle_group(cycle_dimension)
            target = self.chow_group(cycle_dimension)
            engine_chow = self._toric_engine_variety().Chow_group()
            engine_degree = engine_chow.degree(cycle_dimension).module()
            target_labels = tuple(target.module_generating_set())
            integers = _integers()

            def image(cone):
                coordinates = tuple(engine_degree(engine_chow(cone._engine_cone())).vector())
                if len(coordinates) != len(target_labels):
                    raise ArithmeticError("the Chow backend changed its invariant-factor coordinate rank")
                return target.linear_combination(
                    {
                        label: integers(coefficient)
                        for label, coefficient in zip(target_labels, coordinates, strict=True)
                        if coefficient
                    }
                )

            return source.module_category().Mor(source, target)(image)

        @cached_method
        def cox_ring(self):
            r"""Return the Cox homogeneous coordinate ring graded by ``Cl(X)``."""
            from dzack_research.preamble.categories.divisors.cox_rings import _cox_ring

            return _cox_ring(self)

        @cached_method
        def section_ring(self, divisor):
            r"""Return ``oplus_{n>=0} H^0(X,O_X(nD))`` as an owned graded algebra."""
            from dzack_research.preamble.categories.divisors.section_rings import (
                SectionRings,
            )

            return SectionRings(self.scheme_base_ring())(
                self,
                self.weil_divisor_group()(divisor),
            )

        def log_pair(self, boundary_divisor=None):
            r"""Return ``(X, Delta)`` for a torus-invariant boundary ``Delta``.

            With no boundary supplied, ``Delta`` is the full toric boundary
            ``sum_rho D_rho``.
            """
            from dzack_research.preamble.categories.schemes.log_pairs import (
                _toric_log_pair,
            )

            selected = (
                self.toric_boundary_divisor()
                if boundary_divisor is None
                else self.torus_invariant_divisor_group()(boundary_divisor)
            )
            return _toric_log_pair(self, selected)

        def is_polarized(self) -> bool:
            r"""Whether this variety was constructed from a polytope."""
            return self._preamble_toric_polarizing_polytope is not None

        def polarizing_polytope(self):
            r"""The lattice polytope ``P`` with ``X = X_P``.

            A projective toric variety admits many ample divisors and so many
            polytopes; this returns the one the construction was given, and
            asserts when the variety came from a bare fan.
            """
            assert self.is_polarized(), (
                "this toric variety was constructed from a fan, so no polytope "
                "was chosen; build it from a lattice polytope to carry one"
            )
            return self._preamble_toric_polarizing_polytope

        def is_isomorphic_to(self, other) -> bool:
            r"""Whether an isomorphism of fans identifies the two varieties.

            CLS Thm. 3.3.4: a lattice isomorphism carrying one fan onto the
            other induces an isomorphism of the toric varieties over any base.
            """
            assert self.scheme_base_ring() is other.scheme_base_ring(), (
                "an isomorphism of varieties is over one base"
            )
            return self.fan().is_isomorphic(other.fan())

        def is_projective_space(self) -> bool:
            r"""Whether ``X`` is ``P^n`` for ``n`` its own dimension."""
            comparison = RationalPolyhedralFans(
                self.cocharacter_lattice()
            ).projective_space_fan()
            return self.fan().is_isomorphic(comparison)

        def is_weighted_projective_space(self, weights) -> bool:
            r"""Whether ``X`` is ``P(q_0,...,q_n)`` for the stated weights."""
            comparison = RationalPolyhedralFans(
                self.cocharacter_lattice()
            ).weighted_projective_space_fan(weights)
            return self.fan().is_isomorphic(comparison)

        def is_hirzebruch_surface(self, twist) -> bool:
            r"""Whether ``X`` is the Hirzebruch surface ``F_a``."""
            comparison = RationalPolyhedralFans(
                self.cocharacter_lattice()
            ).hirzebruch_surface_fan(twist)
            return self.fan().is_isomorphic(comparison)

        def toric_morphism(self, lattice_morphism, codomain):
            r"""The toric morphism induced by a fan-compatible lattice map.

            A morphism ``phi: N -> N'`` is compatible with ``Sigma``, ``Sigma'``
            when every cone of ``Sigma`` maps into some cone of ``Sigma'``, and
            such a ``phi`` induces an equivariant morphism ``X_Sigma ->
            X_{Sigma'}`` (CLS Thm. 3.3.4).  Compatibility is decided by Sage's
            ``FanMorphism``, which owns the cone-containment search.
            """
            engine_morphism = _engine_fan_morphism(
                lattice_morphism,
                self.fan(),
                codomain.fan(),
            )
            chart_targets = {
                source_cone: _target_maximal_cone(
                    engine_morphism,
                    source_cone,
                    codomain.fan(),
                )
                for source_cone in self.fan().maximal_cones()
            }
            chart_pullbacks = {
                source_cone: _toric_chart_pullback(
                    lattice_morphism,
                    source_cone,
                    target_cone,
                    self.scheme_base_ring(),
                )
                for source_cone, target_cone in chart_targets.items()
            }
            native = self._toric_engine_variety().hom(
                engine_morphism,
                codomain._toric_engine_variety(),
            )
            return ToricSchemeMorphism(
                native,
                domain=self,
                codomain=codomain,
                lattice_morphism=lattice_morphism,
                chart_targets=chart_targets,
                chart_pullbacks=chart_pullbacks,
            )


def _engine_fan_morphism(lattice_morphism, domain_fan, codomain_fan):
    r"""Sage's fan morphism of a compatible lattice map, on row vectors.

    Sage's ``FanMorphism`` acts on rays written as row vectors from the right,
    so the matrix rows are the images of the chosen generators of ``N``.  Its
    constructor performs the cone-containment check and refuses an
    incompatible map.
    """
    from sage.geometry.fan_morphism import FanMorphism

    domain_lattice = domain_fan.cocharacter_lattice()
    codomain_lattice = codomain_fan.cocharacter_lattice()
    assert lattice_morphism.domain() is domain_lattice, (
        "a toric morphism is induced by a map out of the domain's lattice"
    )
    assert lattice_morphism.codomain() is codomain_lattice, (
        "a toric morphism is induced by a map into the codomain's lattice"
    )
    rows = _engine_matrix(
        SageZZ,
        [
            list(
                _engine_vector(
                    codomain_lattice,
                    lattice_morphism(domain_lattice.module_generator(label)),
                )
            )
            for label in domain_lattice.module_generating_set()
        ],
    )
    return FanMorphism(rows, domain_fan._engine_fan(), codomain_fan._engine_fan())


def _toric_variety(fan, base_ring, polarizing_polytope=None):
    r"""The toric variety ``X_Sigma`` of a fan over a field.

    ``X_Sigma`` is the scheme glued from the affine charts of the maximal cones
    along the face localizations of their pairwise intersections (CLS
    Thm. 3.1.5), and that glued scheme is what a session receives.  Sage's
    ``ToricVariety`` stays as the private space the fan-morphism construction
    computes in; it is not the object and it does not reach a session.
    """
    base = _own_ring(base_ring)
    assert fan in RationalPolyhedralFans(fan.cocharacter_lattice()), (
        "a toric variety is built from a rational polyhedral fan"
    )
    assert bool(_engine_ring(base).is_field()), (
        "the semigroup algebras of the charts are algebras over a field"
    )
    scheme = _glued_toric_scheme(fan, base)
    scheme._preamble_toric_engine_variety = _SageToricVariety(
        fan._engine_fan(), base_ring=_engine_ring(base)
    )
    scheme._preamble_toric_fan = fan
    scheme._preamble_toric_polarizing_polytope = polarizing_polytope
    dimension = int(fan.dimension())
    placements = [ToricSchemes(base)]
    if fan.is_smooth():
        placements.append(Schemes(base).Smooth())
    if dimension == 1:
        placements.append(Curves(base))
    if dimension == 2:
        placements.append(Surfaces(base))
    return _refine_scheme(scheme, base, placements)


__all__ = ["ToricSchemeMorphism", "ToricSchemes"]
