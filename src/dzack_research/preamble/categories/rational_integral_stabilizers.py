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
space ``V \\ G / G_L`` is computed in that finite image.  This is why the
whole family is one computation: the finite quotient carries all four
answers.

None of it is computed here, and the obstruction is not the algorithm.  The
preamble has no object for a ``ZZ``-lattice sitting inside a ``QQ``-vector
space: a module morphism is required to have one base ring for its domain and
codomain, so the inclusion ``L -> V`` that the commensurability relation
``d M <= L <= M`` is made of cannot be formed, and neither can ``F_M``, which
is a quotient of two of these.  Base change carries a lattice to
``L tensor QQ`` and back along a stated ring morphism, but it does not make
two different lattices subobjects of one rational space, which is what
commensurability compares.  Until that object exists there is nothing here for
an engine to compute against.

The algorithm itself is owned upstream: ``polyhedral_common`` carries it as
``01_RatIntAutomorphy``, the rational matrix group integralization, and
``sage-indefinite-port`` is the port that will supply it to this preamble
through the capability layer.  When it arrives it will be one capability
whose four entry points are the four operations named below.

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
    "the preamble owns no ZZ-lattice inside a QQ-vector space, so the "
    "commensurability relation d M <= L <= M this operation is stated on "
    "cannot be formed: a module morphism requires one base ring, which makes "
    "the inclusion L -> V and the finite quotient M/dM both unsayable.  The "
    "algorithm is polyhedral_common's 01_RatIntAutomorphy, whose port in "
    "sage-indefinite-port would supply it once that object exists.  For a "
    "stabilizer inside one lattice use the predicate subgroups of O(L); for "
    "the orbit splitting of a finite-index subgroup of O(L) use the finite "
    "character quotient of orthogonal_quotients"
)


def integral_stabilizer(rational_group, lattice):
    r"""Return ``G ∩ GL(L)`` for a rational matrix group and a lattice in its space."""
    assert False, (
        f"the integral stabilizer of {lattice} in {rational_group} is not "
        f"computed: {_ABSENCE}"
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
