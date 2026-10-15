r"""Topological spaces under a fixed space, and the homotopy groups of pointed spaces."""

from dzack_research.preamble.categories.abstract_categories.arrow_categories import CosliceCategory


class TopologicalSpaceCoslices(CosliceCategory):
    r"""``X/Top``: topological spaces ``B`` with a chosen continuous map ``i: X -> B``.

    For ``X`` the one-point space this is the category ``*/Top`` of pointed
    spaces: an object is a space ``B`` with the base point ``b = i(*)``, and a
    morphism is a continuous map preserving base points (Hatcher, *Algebraic
    Topology*, §4.1).  ``CosliceUnder(X)`` on ``TopologicalSpaces()`` selects
    this class through the ``Coslices`` declaration of that category.
    """

    def homotopy_groups_functor(self):
        r"""``pi_* : */Top -> [Disc(ZZ_{>=1}), Groups]``.

        The value at ``(B, b)`` is the family ``n |-> pi_n(B, b) = [(S^n, s), (B, b)]_*``
        of pointed homotopy classes, a functor from the discrete category on
        the positive integers into groups; ``pi_n`` is abelian for ``n >= 2``.
        ``pi_0`` is a pointed set, not a group, so degree 0 is not indexed.
        A pointed map induces the family of homomorphisms ``f_*`` (Hatcher,
        op. cit., §4.1).  The functor is defined on ``*/Top``, so the fixed
        space of this coslice must be the one-point space.
        """
        assert False, "homotopy_groups_functor on TopologicalSpaceCoslices: not implemented"

    class ParentMethods(CosliceCategory.ParentMethods):
        r"""A space ``B`` with its chosen map from the fixed space; for ``*/Top``, a pointed space."""

        def homotopy_groups(self):
            r"""``pi_*(B, b)``: the value of ``homotopy_groups_functor()`` at this pointed space.

            An object of ``[Disc(ZZ_{>=1}), Groups]`` whose degree-``n`` value is
            ``pi_n(B, b)``, with ``pi_1`` at degree 1.  Defined when the fixed
            space of the coslice is the one-point space.
            """
            assert False, "homotopy_groups on TopologicalSpaceCoslices: not implemented"

        def fundamental_group(self):
            r"""``pi_1(B, b)``: the degree-1 value of ``homotopy_groups()``, an object of ``Groups``."""
            assert False, "fundamental_group on TopologicalSpaceCoslices: not implemented"

        def whitehead_product(self, alpha, beta):
            r"""``[alpha, beta] in pi_{p+q-1}(B, b)`` for ``alpha in pi_p``, ``beta in pi_q``, ``p, q >= 1``.

            The class of ``S^{p+q-1} -> S^p v S^q -> B``, the attaching map of the
            top cell of ``S^p x S^q`` followed by ``alpha v beta`` (Whitehead,
            Ann. of Math. 42 (1941)).  For
            ``p = q = 1`` it is the commutator in ``pi_1``.
            """
            assert False, "whitehead_product on TopologicalSpaceCoslices: not implemented"

        def rational_homotopy_lie_algebra(self):
            r"""``pi_{*+1}(B, b) tensor QQ`` under the Whitehead product, an object of ``GradedLieAlgebras(QQ)``.

            Degree ``n`` holds ``pi_{n+1}(B, b) tensor QQ``; the shift makes the
            Whitehead product a degree-zero graded Lie bracket, isomorphic to
            the Samelson bracket on ``pi_*(Omega B) tensor QQ`` up to sign.
            Hypothesis: ``B`` is simply connected, so every ``pi_{n+1}`` with
            ``n >= 1`` is abelian (Felix, Halperin and Thomas, *Rational
            Homotopy Theory*, GTM 205, §21).
            """
            assert False, "rational_homotopy_lie_algebra on TopologicalSpaceCoslices: not implemented"


__all__ = ["TopologicalSpaceCoslices"]
