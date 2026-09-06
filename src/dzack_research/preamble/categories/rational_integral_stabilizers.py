r"""Integral stabilizers of a commensurability class under a rational group.

Let ``V`` be a finite-dimensional vector space over ``QQ`` and let ``G`` be a
finitely generated subgroup of ``GL(V)``.  Two lattices ``L`` and ``M`` in
``V`` are commensurable when ``d M <= L <= M`` for some positive integer
``d``.  The integral stabilizer is

``G_L = G ∩ GL(L) = {g in G : g(L) = L}``,

which is the definition; the computation goes through the finite quotient
``F_M = M / dM``.  Every element of ``G`` that preserves ``M`` acts on
``F_M``, so there is a morphism ``rho : G -> Aut(F_M)`` with finite image, and
``L`` becomes the subgroup ``S_L = L / dM`` of ``F_M``.  Then

``G_L = rho^{-1}(Stab_{rho(G)}(S_L))``,

the orbit of ``S_L`` under the finite group ``rho(G)`` indexes the right
cosets ``G_L \\ G``, a transporter between two commensurable lattices is a
preimage of an element carrying one subgroup to the other, and a double coset
space ``V \\ G / G_L`` is computed in that finite image.  One finite quotient
therefore carries the three answers that would otherwise be a search in an
infinite group; the stabilizer itself is a predicate and needs no search.

The objects are formed by restriction of scalars.  ``V`` is a module over
``QQ``; ``restrict_scalars(V, ZZ.Mor(QQ)(...))`` in
``modules/pure/modules.py`` reads the same additive group as a module over
``ZZ``, and that view accepts subobject data and joins ``ModuleSubobjects``,
so a lattice in ``V`` is an honest monomorphism ``L -> Res(V)`` with one base
ring on both sides.  The relation ``d M <= L <= M`` is three such
monomorphisms inside one restricted module, and ``F_M`` is a quotient of two
of them.  Nothing about a lattice in a rational space is unsayable here.

What is missing is two things, and neither is the object.

The first is the morphism half of the restriction functor for this ring map.
``RestrictionOfScalarsFunctor`` in ``functors/scalar_change.py`` materializes
``Res(g)`` by naming images of a framing, and refuses without one; the view
carries a framing only when the extension ring is a finitely generated free
module over the base ring.  ``QQ`` is not that over ``ZZ``, so ``Res(V)`` has
no framing and ``Res(g)`` cannot be formed.  Until it can, ``g(L) = L`` has no
owned composite to be stated as, even though every object in it exists.  That
is the module Hom surface's to supply, and it is also what the
scalar-extension adjunction's ``unit`` guards on.

The second is the algorithm.  ``polyhedral_common`` carries it as
``01_RatIntAutomorphy``, the rational matrix group integralization, and
``sage-indefinite-port`` is the port that will supply it through the
capability layer.  Note which of the four rows needs it: once ``Res(g)``
exists, ``integral_stabilizer`` is definitional, a predicate subgroup cut out
by ``Res(g)(L) = L`` decided on the finite generators of ``L``, with no engine
called at all.  The transporter, the right cosets and the double cosets are
the ones that need the finite quotient computed, because deciding emptiness or
enumerating a transversal is a search in a group that is infinite.

A third gap bounds the argument the operations take.  The preamble names no
general linear group of a module: ``module_homset(V, V)`` is the endomorphism
set, and the group of its units is not an owned object.  A rational group
here is therefore a subgroup of ``V.Aut()`` for a rational lattice
(``rational_lattices.py``), which is the arithmetic case this program uses,
and not the full ``GL(V)`` the rows are stated over.

What *is* owned, so a caller does not come here for it:

- the stabilizer of a subobject inside one lattice, as a predicate subgroup of
  ``O(L)``: ``I.parabolic_subgroup()`` for a primitive isotropic subobject,
  and ``predicate_subgroup`` for any other stabilizing condition;
- the splitting of a full-``O(L)`` orbit into the orbits of a finite-index
  subgroup, through the finite character quotient of
  ``orthogonal_quotients``, which is the same finite-quotient argument for
  the discriminant, determinant and spinor characters rather than for a
  commensurability class;
- base change of a lattice along ``ZZ -> QQ``, through
  ``L.base_change(ring_map)``.
"""

_ABSENCE = (
    "the objects exist -- a lattice in V is a monomorphism L -> Res_ZZ(V) "
    "through restriction of scalars, and d M <= L <= M is three of them in "
    "one restricted module -- but Res(g) does not: the restriction functor "
    "materializes a morphism by naming images of a framing, and Res_ZZ(V) "
    "carries none because QQ is not a finitely generated free ZZ-module.  "
    "Supplying that morphism is the module Hom surface's, and it is what "
    "g(L) = L needs to be stated as an owned composite.  The computation on "
    "top of it is polyhedral_common's 01_RatIntAutomorphy, arriving through "
    "sage-indefinite-port and the capability layer.  For a stabilizer inside "
    "one lattice use the predicate subgroups of O(L); for the orbit splitting "
    "of a finite-index subgroup of O(L) use the finite character quotient of "
    "orthogonal_quotients"
)


def integral_stabilizer(rational_group, lattice):
    r"""Return ``G ∩ GL(L)`` for a rational matrix group and a lattice in its space."""
    assert False, (
        f"the integral stabilizer of {lattice} in {rational_group} is not "
        f"stated: {_ABSENCE}"
    )


def integral_transporter(rational_group, source_lattice, target_lattice):
    r"""Return one ``g`` in ``G`` with ``g(L_1) = L_2``, or the empty transporter."""
    assert False, (
        f"an integral transporter in {rational_group} from {source_lattice} to "
        f"{target_lattice} is not computed: {_ABSENCE}"
    )


def integral_right_cosets(rational_group, lattice):
    r"""Return a transversal of the right cosets of ``G_L`` in ``G``."""
    assert False, (
        f"the right cosets of the {rational_group}-stabilizer of {lattice} are not "
        f"computed: {_ABSENCE}"
    )


def integral_double_cosets(subgroup, rational_group, lattice):
    r"""Return a transversal of ``V \\ G / G_L`` on the finite quotient of ``M``."""
    assert False, (
        f"the double cosets of {subgroup} in {rational_group} and the integral "
        f"stabilizer of {lattice} are not computed: {_ABSENCE}"
    )


__all__ = [
    "integral_double_cosets",
    "integral_right_cosets",
    "integral_stabilizer",
    "integral_transporter",
]
