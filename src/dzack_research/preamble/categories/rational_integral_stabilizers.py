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

The vocabulary for all of this is subobjects of one module, and restriction of
scalars supplies that module.  ``Res`` is the restriction functor along
``ZZ -> QQ``, a method of its domain category,

``Res = Modules(QQ).restriction_of_scalars(ZZ.Mor(QQ)(lambda n: QQ(n)))``,

and ``Res(V)`` is the same additive group read over ``ZZ``.  Nothing is
tensored and no lattice is base changed.  A lattice in ``V`` is then a
monomorphism into that one module,

``module_embedding(L, Res(V), images)``,

with ``ZZ`` on both sides, so the base-ring rule is satisfied rather than
violated.  ``L`` and ``M`` are two subobjects of one object, ``d M <= L <= M``
is a comparison between subobjects of that object, and ``F_M`` is an ordinary
quotient of ``ZZ``-modules.  This is what the four operations below take: the
monomorphism presenting a lattice in ``V``, not a bare lattice, and no
commensurability type is invented.

What refuses is one operation, and its name is ``ModuleMorphism.lift`` in
``modules/module_morphisms/module_morphisms.py``.  It solves coordinates
against the framings of both endpoints and raises without them, and
``is_in_image`` is built on it.  ``Res(V)`` has no finite free framing over
``ZZ``: a rational vector space is divisible, so it is not finitely generated
over ``ZZ`` at all.  Every *decision* about these subobjects therefore refuses
there -- whether ``d M`` lies in ``L``, whether ``L`` lies in ``M``, and
whether ``g`` carries ``L`` onto itself.  The construction stands; the
membership test on top of it does not.  What would supply it is a lift that
decides membership in the ``ZZ``-span of finitely many elements of an unframed
module, which is the rational linear solve followed by an integrality test,
and it belongs beside the coordinate lift it generalizes.

The arrow is not missing either.  Mathematically ``Res(g)`` is ``g``:
restriction changes which ring acts, never the underlying map, so the
functor's action on morphisms is the identity and there is nothing to
construct.  This preamble's functor does not say it that way -- it
materializes a morphism by naming images of a framing, so on the unframed
``Res(V)`` it refuses an arrow that exists, and that repair belongs to the
scalar-change functor, where the obstacle is.  Either way it is not the
binding constraint: ``g`` applies to an element of ``Res(V)`` without it, and
what is missing is the decision, not the map.

Then the algorithm.  ``polyhedral_common`` carries it as
``01_RatIntAutomorphy``, the rational matrix group integralization, and
``sage-indefinite-port`` is the port that will supply it through the
capability layer.  Note which rows need it: with the lift above,
``integral_stabilizer`` is definitional, a predicate subgroup cut out by
``g(L) = L`` on the finite generators of ``L``, with no engine called at all.
The transporter, the right cosets and the double cosets are the three that
need the finite quotient computed.

One further gap bounds the argument these operations take.  The preamble names
no general linear group of a module: ``module_homset(V, V)`` is the
endomorphism set, and the group of its units is not an owned object.  A
rational group here is therefore a subgroup of ``V.Aut()`` for a rational
lattice (``rational_lattices.py``), which is the arithmetic case this program
uses, and not the full ``GL(V)`` the rows are stated over.

What *is* owned, so a caller does not come here for it:

- the stabilizer of a subobject inside one lattice, as a predicate subgroup of
  ``O(L)``: ``I.parabolic_subgroup()`` for a primitive isotropic subobject,
  and ``predicate_subgroup`` for any other stabilizing condition;
- the splitting of a full-``O(L)`` orbit into the orbits of a finite-index
  subgroup, through the finite character quotient of
  ``orthogonal_quotients``, which is the same finite-quotient argument for
  the discriminant, determinant and spinor characters rather than for a
  commensurability class.
"""

_ABSENCE = (
    "the objects exist: Res(V), the rational space read over ZZ through the "
    "restriction functor, holds L and M as two subobjects, and d M <= L <= M "
    "is a comparison between them.  The arrow exists too: Res(g) is g, since "
    "restriction changes which ring acts and never the underlying map, so "
    "there is nothing to construct and functoriality is free; this preamble's "
    "scalar-change functor writes its morphism action through framings and so "
    "refuses an arrow that exists, which is an implementation limitation to "
    "repair in functors/scalar_change.py.  What refuses the mathematics is "
    "ModuleMorphism.lift in "
    "modules/module_morphisms/module_morphisms.py, which solves coordinates "
    "against the framings of both endpoints; Res(V) has no finite free "
    "framing over ZZ because a rational vector space is divisible, so "
    "is_in_image and with it every containment and every g(L) = L decision "
    "refuses there.  A lift deciding membership in the ZZ-span of finitely "
    "many elements of an unframed module -- the rational solve plus an "
    "integrality test -- is what these rows wait on, and after it the "
    "computation on top is polyhedral_common's 01_RatIntAutomorphy through "
    "sage-indefinite-port and the capability layer.  For a stabilizer inside "
    "one lattice use the predicate subgroups of O(L); for the orbit splitting "
    "of a finite-index subgroup of O(L) use the finite character quotient of "
    "orthogonal_quotients"
)


def integral_stabilizer(rational_group, lattice_inclusion):
    r"""Return ``G ∩ GL(L)`` for a lattice ``L -> Res(V)`` and a rational group."""
    assert False, (
        f"the integral stabilizer of {lattice_inclusion} in {rational_group} "
        f"is not stated: {_ABSENCE}"
    )


def integral_transporter(rational_group, source_inclusion, target_inclusion):
    r"""Return one ``g`` in ``G`` with ``g(L_1) = L_2``, or the empty transporter."""
    assert False, (
        f"an integral transporter in {rational_group} from {source_inclusion} "
        f"to {target_inclusion} is not computed: {_ABSENCE}"
    )


def integral_right_cosets(rational_group, lattice_inclusion):
    r"""Return a transversal of the right cosets of ``G_L`` in ``G``."""
    assert False, (
        f"the right cosets of the {rational_group}-stabilizer of "
        f"{lattice_inclusion} are not computed: {_ABSENCE}"
    )


def integral_double_cosets(subgroup, rational_group, lattice_inclusion):
    r"""Return a transversal of ``V \\ G / G_L`` on the finite quotient of ``M``."""
    assert False, (
        f"the double cosets of {subgroup} in {rational_group} and the integral "
        f"stabilizer of {lattice_inclusion} are not computed: {_ABSENCE}"
    )


__all__ = [
    "integral_double_cosets",
    "integral_right_cosets",
    "integral_stabilizer",
    "integral_transporter",
]
