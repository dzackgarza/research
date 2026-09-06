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

What this file adds is the decomposition as one object, both halves of that
isomorphism -- the restriction morphisms ``O(L,f) -> O(L^f)`` and
``O(L,f) -> O((L^f)^perp)`` forwards, and ``centralizer_element`` back -- and
the cyclotomic summands ``ker Phi_d(f)`` of a finite-order isometry.
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
        assert lattice.module_rank().is_finite() and lattice.is_nondegenerate(), (
            "the invariant and coinvariant lattices span L only when L is a "
            "finite nondegenerate lattice"
        )
        invariant = isometry.invariant_lattice()
        coinvariant = isometry.formed_coinvariants()
        assert invariant.module_rank() + coinvariant.module_rank() == lattice.module_rank(), (
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

    @cached_method
    def orthogonal_sum_inclusion(self):
        r"""Return the finite-index inclusion ``L^f + (L^f)^perp -> L``.

        The two summands are orthogonal of complementary rank, so their
        orthogonal sum is a lattice in its own right and this arrow is the
        primitive extension the class is named for.  Its cokernel has order
        :meth:`index`, so that scalar carries every vector of ``L`` into the
        image: an isometry of the two summands is read on ``L`` by clearing
        that one denominator.
        """
        invariant_inclusion = self.invariant.inclusion()
        coinvariant_inclusion = self.coinvariant.inclusion()
        invariant_summand = invariant_inclusion.domain()
        coinvariant_summand = coinvariant_inclusion.domain()
        summands = invariant_summand + coinvariant_summand
        return summands.Emb(self.lattice)(
            tuple(
                invariant_inclusion(generator)
                for generator in invariant_summand.module_generators()
            )
            + tuple(
                coinvariant_inclusion(generator)
                for generator in coinvariant_summand.module_generators()
            )
        )

    def glue_graph(self):
        r"""Return the graph of ``gamma`` inside ``A_{L^f} x A_{(L^f)^perp}(-1)``.

        Nikulin presents ``L`` by the subgroup ``L/(L^f + (L^f)^perp)``, which
        sits in the sum of the two discriminant forms as the graph of the
        anti-isometry ``gamma``.  The graph is a finite group of order
        :meth:`index`, and it is what an isometry of the two summands has to
        preserve in order to be an isometry of ``L``.
        """
        glue = self.glue()
        gluing = glue.domain()
        into_invariant = gluing.inclusion()
        into_coinvariant = glue.codomain().inclusion()
        return tuple(
            (into_invariant(element), into_coinvariant(glue(element)))
            for element in gluing.elements()
        )

    def _discriminant_action(self, automorphism, ambient, element):
        r"""Return the image of a class of ``ambient`` under ``Disc(automorphism)``.

        An automorphism of a summand induces an automorphism of that summand's
        discriminant module, and that module is what underlies whichever
        finite form the glue map put the graph in: the discriminant module
        itself, its bilinear reading when an even summand sits inside an odd
        ``L``, or the twist ``A_R(-1)``.  Polarizing and rescaling both leave
        the underlying map alone -- an isometry of ``q`` is an isometry of its
        polar form and of any rescaling of either -- so the action is read by
        forgetting the ambient form, applying the induced automorphism, and
        equipping the ambient form again.
        """
        return ambient.equip_form_morphism()(
            automorphism.discriminant_morphism()(
                ambient.forget_form_morphism()(element)
            )
        )

    def pair_preserves_glue_graph(self, invariant_part, coinvariant_part) -> bool:
        r"""Return whether ``(g_+, g_-)`` carries the graph of ``gamma`` onto itself.

        The pair acts on the sum of the two discriminant forms by its induced
        discriminant automorphisms ``Disc(g_+)`` and ``Disc(g_-)``, the second
        read on the twist ``A_{(L^f)^perp}(-1)`` in which ``gamma`` lands.  It
        extends to an isometry of ``L`` exactly when that action preserves the
        graph, which is Nikulin's criterion for a primitive extension.  Both
        maps are automorphisms of finite forms, so preserving the graph
        setwise is the same as permuting it.

        The criterion reads the same in either parity of ``L``; only the
        finite forms the graph lives in change, and which ones those are is
        settled once, by ``glue_map``, from the parity of ``L``.  An even
        ``L`` glues its quadratic discriminant forms and an odd one its
        bilinear forms, so the two ambients are taken from the endpoints of
        the glue arrow rather than chosen a second time here.
        """
        invariant_ambient = self.glue().domain().inclusion().codomain()
        coinvariant_ambient = self.glue().codomain().inclusion().codomain()
        graph = self.glue_graph()
        return all(
            (
                self._discriminant_action(
                    invariant_part, invariant_ambient, invariant_class
                ),
                self._discriminant_action(
                    coinvariant_part, coinvariant_ambient, coinvariant_class
                ),
            )
            in graph
            for invariant_class, coinvariant_class in graph
        )

    def centralizer_element(self, invariant_part, coinvariant_part):
        r"""Assemble ``g`` in ``O(L,f)`` from a compatible pair of restrictions.

        This is the inverse of :meth:`invariant_restriction` and
        :meth:`coinvariant_restriction`.  A pair ``(g_+, g_-)`` in
        ``O(L^f) x O((L^f)^perp)`` is an element of ``O(L,f)`` under two
        conditions.  It has to extend to ``L``, which is
        :meth:`pair_preserves_glue_graph`.  It then has to commute with ``f``,
        and since ``f`` is the identity on ``L^f`` that is the single
        condition that ``g_-`` commutes with ``f`` restricted to
        ``(L^f)^perp``.

        The extension itself is one denominator.  The orthogonal sum has index
        ``m`` in ``L``, so ``m x`` lies in the sum for every ``x`` in ``L``;
        applying the pair there and dividing by ``m`` again gives ``g x``, and
        the division is exact because the pair preserves the graph.  The
        returned arrow is built in ``O(L)``, whose constructor is what proves
        the assembled map preserves the form and is bijective.
        """
        lattice = self.lattice
        invariant_inclusion = self.invariant.inclusion()
        coinvariant_inclusion = self.coinvariant.inclusion()
        invariant_summand = invariant_inclusion.domain()
        coinvariant_summand = coinvariant_inclusion.domain()
        assert invariant_part.parent() is invariant_summand.Aut(), (
            "the invariant half of the pair is an element of O(L^f)"
        )
        assert coinvariant_part.parent() is coinvariant_summand.Aut(), (
            "the coinvariant half of the pair is an element of O((L^f)^perp)"
        )
        coinvariant_isometry = self.coinvariant_restriction(self.isometry)
        assert (
            coinvariant_part * coinvariant_isometry
            == coinvariant_isometry * coinvariant_part
        ), (
            "an element of O(L,f) restricts on (L^f)^perp to the centralizer "
            "of f there; the stated g_- does not commute with f"
        )
        assert self.pair_preserves_glue_graph(invariant_part, coinvariant_part), (
            "the stated pair does not preserve the graph of the glue "
            "anti-isometry, so it is an isometry of L^f + (L^f)^perp that does "
            "not extend to L"
        )

        ring = lattice.base_ring()
        scalar = ring(int(self.index().finite_value()))
        inclusion = self.orthogonal_sum_inclusion()
        summands = inclusion.domain()
        moved = module_homset(summands, lattice)(
            tuple(
                invariant_inclusion(invariant_part(generator))
                for generator in invariant_summand.module_generators()
            )
            + tuple(
                coinvariant_inclusion(coinvariant_part(generator))
                for generator in coinvariant_summand.module_generators()
            )
        )
        scaling = module_homset(lattice, lattice)(
            tuple(
                lattice.scalar_multiple(scalar, generator)
                for generator in lattice.module_generators()
            )
        )

        def image(label):
            scaled = lattice.scalar_multiple(scalar, lattice.module_generator(label))
            return scaling.lift(moved(inclusion.lift(scaled)))

        return lattice.O()(image)

    def equivariant_vector_orbit_representatives(self, square):
        r"""Return ``O(L,f)``-orbit representatives of the vectors of ``square``.

        The centralizer is a subgroup of ``O(L)`` cut out by a predicate and
        not by a character, so the finite-character quotient that splits an
        ``O(L)`` orbit does not describe it.  What describes it is the group
        itself, and acting with it is a finite computation exactly when
        ``O(L)`` is finite, which for a lattice is definiteness; the
        assertion in the owning subgroup operation states that hypothesis.
        For the orbits under the full ``O(L)`` use
        ``L.O().vector_orbit_representatives(square)``.
        """
        return self.centralizer_group().vector_orbit_representatives(square)

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
