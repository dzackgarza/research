r"""The primitive extension cut out by a lattice isometry, and its centralizer.

For an isometry ``f`` of a nondegenerate lattice ``L`` the invariant lattice
``L^f`` and its orthogonal complement are primitive sublattices whose
orthogonal sum sits in ``L`` with finite index.  Nikulin's correspondence
presents that primitive extension by the anti-isometry

``gamma : H_+ -> H_-(-1)``,   ``H_+ <= A_{L^f}``,  ``H_- <= A_{(L^f)^perp}``,

whose graph is ``L/(L^f + (L^f)^perp)``.  The centralizer ``O(L,f)`` is then
the group of pairs ``(g_+, g_-)`` in ``O(L^f) x O((L^f)^perp)`` whose induced
discriminant automorphisms commute with ``gamma``, equivalently which carry
the graph onto itself.

This object is the isometry-cut sibling of ``VectorPrimitiveExtension``, which
records the same primitive-extension data for the decomposition cut out by one
anisotropic vector.  The two share the owned pieces they stand on: the
invariant lattice and formed coinvariants of the isometry, ``glue_map`` for
the anti-isometry, and ``centralizer`` for the subgroup.

What this file adds is the decomposition as one object, the two restriction
morphisms ``O(L,f) -> O(L^f)`` and ``O(L,f) -> O((L^f)^perp)`` carrying the
forward half of that isomorphism, and the cyclotomic summands
``ker Phi_d(f)`` of a finite-order isometry.  Assembling an element of
``O(L,f)`` from a compatible pair is the inverse half and is not implemented
here; the obstruction is stated on ``centralizer_element``.
"""

from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_homset,
)


class IsometryPrimitiveExtension:
    r"""The primitive extension ``L^f + (L^f)^perp -> L`` cut out by ``f``.

    Every field below is an owned object: the two primitive sublattices with
    their inclusions, the finite index of their orthogonal sum, and the glue
    anti-isometry presenting the extension.
    """

    def __init__(self, isometry) -> None:
        lattice = isometry.domain()
        assert isometry.codomain() is lattice, (
            "a primitive extension is cut out by an automorphism of one lattice"
        )
        assert lattice.is_finite_rank() and lattice.is_nondegenerate(), (
            "the invariant and coinvariant lattices span L only when L is a "
            "finite nondegenerate lattice"
        )
        invariant = isometry.invariant_lattice()
        coinvariant = isometry.formed_coinvariants()
        assert invariant.rank() + coinvariant.rank() == lattice.rank(), (
            "the invariant lattice and its orthogonal complement do not have "
            "complementary rank; f is not of finite order on this lattice"
        )

        self.isometry = isometry
        self.lattice = lattice
        self.invariant = invariant
        self.coinvariant = coinvariant

    @cached_method
    def glue(self):
        r"""Return the Nikulin anti-isometry ``H_+ -> H_-(-1)`` of this extension."""
        return self.lattice.glue_map(self.invariant, self.coinvariant)

    def gluing_subgroup(self):
        r"""Return ``H_+ = L/(L^f + (L^f)^perp)`` seen inside ``A_{L^f}``."""
        return self.glue().domain()

    @cached_method
    def index(self):
        r"""Return ``[L : L^f + (L^f)^perp]``, the order of the glue subgroup."""
        return self.invariant.sum(self.coinvariant).index()

    def centralizer_group(self):
        r"""Return ``O(L,f) = Z_{O(L)}(f)`` as a predicate subgroup of ``O(L)``."""
        from dzack_research.preamble.categories.group.predicate_subgroups import (
            centralizer,
        )

        return centralizer(self.lattice.Aut(), self.isometry)

    def centralizer_discriminant_image(self):
        r"""Return ``rho_L(O(L,f)) <= O(A_L)``, the finite image of the centralizer."""
        return self.isometry.centralizer_discriminant_image()

    def _restriction(self, automorphism, subobject):
        assert automorphism.domain() is self.lattice, (
            "a restriction of the centralizer is taken of an automorphism of L"
        )
        assert automorphism * self.isometry == self.isometry * automorphism, (
            "restriction along this decomposition is defined on O(L,f); the "
            "stated automorphism does not commute with f"
        )
        inclusion = subobject.inclusion()
        summand = inclusion.domain()
        return summand.Aut()(
            {
                label: inclusion.lift(
                    automorphism(inclusion(summand.module_generator(label)))
                )
                for label in summand.module_generating_set()
            }
        )

    def invariant_restriction(self, automorphism):
        r"""Return ``g|_{L^f}`` in ``O(L^f)`` for ``g`` in the centralizer.

        An element of ``O(L,f)`` commutes with ``f``, so it preserves the
        fixed lattice and, being an isometry of ``L``, its orthogonal
        complement.  Restriction is therefore defined and lands in the
        orthogonal group of the summand.
        """
        return self._restriction(automorphism, self.invariant)

    def coinvariant_restriction(self, automorphism):
        r"""Return ``g|_{(L^f)^perp}`` in ``O((L^f)^perp)`` for ``g`` in the centralizer."""
        return self._restriction(automorphism, self.coinvariant)

    def acts_as_negation_on_coinvariants(self) -> bool:
        r"""Return whether ``f`` restricts to ``-1`` on ``(L^f)^perp``.

        This holds exactly when ``f`` is an involution: then ``(L^f)^perp`` is
        ``ker(f + 1)``, which is the statement the eigenspace decomposition
        ``V_pm = ker(f -+ 1)`` makes.
        """
        inclusion = self.coinvariant.inclusion()
        return all(
            self.isometry(inclusion(generator)) == -inclusion(generator)
            for generator in inclusion.domain().module_generators()
        )

    def centralizer_element(self, invariant_part, coinvariant_part):
        r"""Assemble ``g`` in ``O(L,f)`` from a compatible pair of restrictions."""
        assert False, (
            "assembling an element of O(L,f) from a pair (g_+, g_-) is the "
            "inverse of invariant_restriction and coinvariant_restriction.  It "
            "requires the pair's induced discriminant automorphisms to be "
            "carried across the glue anti-isometry, so the composite "
            "gamma . Disc(g_+) . gamma^{-1} has to be formed on the glue "
            "subgroups H_+ <= A_{L^f} and H_- <= A_{(L^f)^perp}(-1); the twist "
            "on the codomain means Disc(g_-) and gamma are not currently "
            "composable as owned morphisms.  The missing operation is one "
            "named arrow: twist(scalar) in "
            "modules/framed/formed/torsion_form_modules.py builds A(-1) as a "
            "new parent on the same underlying presented module but has no "
            "action on morphisms, so an automorphism of A is carried to none "
            "of A(-1).  Giving the twist that action -- it is the identity on "
            "the underlying module -- makes the composite above an ordinary "
            "composition of owned morphisms"
        )

    def equivariant_vector_orbit_representatives(self, square):
        r"""Return ``O(L,f)``-orbit representatives of the vectors of ``square``."""
        assert False, (
            f"the O(L,f)-orbits of the vectors of square {square} in "
            f"{self.lattice} are not computed.  The owned subgroup-orbit route "
            "splits a full O(L) orbit through the finite quotient of a "
            "character of O(L) -- discriminant, determinant or real spinor "
            "norm -- and the centralizer of an isometry is not cut out by such "
            "a character, so that route does not describe it.  The "
            "equivariant orbits are read off the pair description instead: a "
            "vector of L is a pair of vectors of L^f and (L^f)^perp glued "
            "across gamma, and its orbit is the orbit of that pair under the "
            "subgroup of O(L^f) x O((L^f)^perp) preserving the glue.  The "
            "forward half of that description is invariant_restriction and "
            "coinvariant_restriction; the missing half is the one stated on "
            "centralizer_element, an action on morphisms for twist(scalar) in "
            "modules/framed/formed/torsion_form_modules.py.  For the orbits "
            "under the full O(L) use "
            "L.O().vector_orbit_representatives(square)"
        )

    def __repr__(self) -> str:
        return f"Primitive extension of {self.lattice} cut out by {self.isometry}"


def cyclotomic_summand(isometry, order):
    r"""Return ``ker Phi_d(f)`` as a primitive sublattice of the isometry's lattice.

    ``Phi_d`` is the ``d``-th cyclotomic polynomial and ``d`` is ``order``.
    The kernel of a module morphism into a torsion-free module is saturated,
    so the result is a primitive sublattice with no separate saturation step.
    For ``f`` of finite order ``n`` these summands, over the divisors ``d`` of
    ``n``, span a finite-index sublattice of ``L``; each is the intersection
    of ``L`` with the rational subspace ``V_{Phi_d}``.
    """
    lattice = isometry.domain()
    assert isometry.codomain() is lattice, (
        "a cyclotomic summand is cut out by an automorphism of one lattice"
    )
    ring = lattice.base_ring()
    from sage.rings.polynomial.cyclotomic import cyclotomic_coeffs

    coefficients = cyclotomic_coeffs(int(order))

    def image(label):
        iterate = lattice.module_generator(label)
        total = lattice.zero()
        for coefficient in coefficients:
            total = total + lattice.scalar_multiple(ring(int(coefficient)), iterate)
            iterate = isometry(iterate)
        return total

    evaluated = module_homset(lattice, lattice)(
        {label: image(label) for label in lattice.module_generating_set()}
    )
    return evaluated.kernel()


def isometry_primitive_extension(isometry) -> IsometryPrimitiveExtension:
    r"""Return the primitive extension of ``L`` cut out by the isometry ``f``."""
    return IsometryPrimitiveExtension(isometry)


__all__ = [
    "IsometryPrimitiveExtension",
    "cyclotomic_summand",
    "isometry_primitive_extension",
]
