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

The affine charts are constructed here, not read off the backend: the chart
of a cone is ``Spec`` of the semigroup algebra of \(S_\sigma=\sigma^\vee\cap
M\), and a face inclusion \(\tau\preceq\sigma\) is realized as the
distinguished open of the chart of \(\sigma\) at one monomial (CLS
Prop. 1.3.16).  Sage's ``ToricVariety`` is the backend realization of the
glued scheme itself, adopted the way the other non-affine schemes in this
package are adopted.
"""

from sage.matrix.constructor import matrix as _engine_matrix
from sage.misc.cachefunc import cached_method
from sage.rings.integer_ring import ZZ as SageZZ
from sage.schemes.toric.ideal import ToricIdeal as _SageToricIdeal
from sage.schemes.toric.variety import ToricVariety as _SageToricVariety

from dzack_research.preamble.categories.algebras.free_algebras import (
    FinitelyPresentedAlgebra,
    PolynomialRing,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _engine_ring,
    _own_ring,
)
from dzack_research.preamble.categories.schemes.schemes import (
    NormalSchemes,
    Schemes,
    SmoothSchemes,
    Spec,
    _has_scheme_placement,
    refine_scheme,
    refine_scheme_morphism,
)
from dzack_research.preamble.categories.schemes.toric.fans import (
    RationalPolyhedralFans,
    _engine_vector,
)
from dzack_research.preamble.categories.schemes.varieties import (
    Curves,
    Surfaces,
    Varieties,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_image,
    finite_ordered_set,
)


def _integers():
    return _own_ring(SageZZ)


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
    """
    generators = cone.semigroup_generators()
    names = _character_names(int(generators.cardinality()))
    presentation = PolynomialRing(base_ring, names)
    engine_presentation = _engine_ring(presentation)
    columns = _engine_matrix(
        SageZZ,
        [
            list(_engine_vector(cone.character_lattice(), generator))
            for generator in generators
        ],
    ).transpose()
    engine_ideal = _SageToricIdeal(
        columns,
        names=names,
        base_ring=_engine_ring(base_ring),
    )
    relations = tuple(
        presentation._from_engine_element(engine_presentation(relation))
        for relation in engine_ideal.gens()
    )
    return FinitelyPresentedAlgebra(presentation, relations)


def _face_supporting_character_monomial(face, cone, chart):
    r"""The monomial ``chi^m`` cutting ``face`` out of ``cone`` (CLS Prop. 1.3.16).

    Take ``m`` to be the sum of the chosen semigroup generators of
    \(S_\sigma\) that vanish on \(\tau\).  Those generators generate the face
    \(\sigma^\vee\cap\tau^\perp\) of \(\sigma^\vee\), so their sum lies in its
    relative interior, and therefore \(\sigma\cap m^\perp=\tau\).  In
    \(k[S_\sigma]\) the character \(\chi^m\) is then the product of the
    corresponding variables, with no integer program to solve.
    """
    zero = _integers().zero()
    algebra = chart.coordinate_algebra()
    labels = tuple(algebra.algebra_generating_set())
    monomial = algebra.one()
    for position, generator in enumerate(cone.semigroup_generators()):
        if all(value == zero for value in face.pair_with(generator)):
            monomial = monomial * algebra.algebra_generator(labels[position])
    return monomial


class ToricSchemes(OwnedCategoryOverBaseRing):
    r"""Toric varieties over the stated base field, each equipped with its fan."""

    def an_object(self):
        r"""The projective plane, as the toric variety of the fan of ``P^2``."""
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
            BasedFreeModule,
        )

        cocharacters = BasedFreeModule(_integers(), 2)
        return RationalPolyhedralFans(cocharacters).projective_space_fan().toric_variety(
            self.base_ring()
        )

    def _repr_object_names(self):
        return f"toric varieties over {self.base_ring()}"

    def super_categories(self):
        return [
            Varieties(self.base_ring()),
            NormalSchemes(self.base_ring()),
        ]

    def __contains__(self, candidate) -> bool:
        return candidate in Schemes(self.base_ring()) and _has_scheme_placement(
            candidate, ToricSchemes
        )

    class ParentMethods:
        def fan(self):
            r"""The fan ``Sigma`` in ``N_R`` this variety was built from."""
            return self._preamble_toric_fan

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

        @cached_method
        def affine_chart(self, cone):
            r"""The affine chart ``U_sigma = Spec k[S_sigma]`` of one cone.

            This is the owned construction from the semigroup algebra, not a
            patch read back from the backend.
            """
            assert cone in self.fan(), "an affine chart is taken of a cone of this fan"
            return Spec(
                _semigroup_algebra(cone, self.scheme_base_ring()),
                base_ring=self.scheme_base_ring(),
            )

        def affine_cover(self):
            r"""The charts of the maximal cones, which cover ``X_Sigma``."""
            return finite_ordered_image(
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
            chart = self.affine_chart(cone)
            return chart.distinguished_open(
                _face_supporting_character_monomial(face, cone, chart)
            )

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
            return refine_scheme_morphism(
                self.hom(engine_morphism, codomain),
                self.scheme_base_ring(),
                domain=self,
                codomain=codomain,
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


def ToricVariety(fan, base_ring, polarizing_polytope=None):
    r"""The toric variety ``X_Sigma`` of a fan over a field.

    The glued scheme is realized by Sage's ``ToricVariety``, which is the
    backend for the underlying space and its coordinate data; the fan, the
    charts, and the face localizations are the owned mathematics around it.
    """
    base = _own_ring(base_ring)
    assert fan in RationalPolyhedralFans(fan.cocharacter_lattice()), (
        "a toric variety is built from a rational polyhedral fan"
    )
    assert bool(_engine_ring(base).is_field()), (
        "the represented toric-variety backend is defined over a field"
    )
    scheme = _SageToricVariety(fan._engine_fan(), base_ring=_engine_ring(base))
    scheme._preamble_toric_fan = fan
    scheme._preamble_toric_polarizing_polytope = polarizing_polytope
    dimension = int(fan.dimension())
    placements = [ToricSchemes(base)]
    if fan.is_smooth():
        placements.append(SmoothSchemes(base))
    if dimension == 1:
        placements.append(Curves(base))
    if dimension == 2:
        placements.append(Surfaces(base))
    return refine_scheme(scheme, base, placements)


__all__ = ["ToricSchemes", "ToricVariety"]
