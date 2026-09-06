r"""Integral stabilizers of a commensurability class under a rational group.

Let ``V`` be a finite-dimensional vector space over ``QQ`` and let ``G`` be a
finitely generated subgroup of ``GL(V)``.  Two lattices ``L`` and ``M`` in
``V`` are commensurable when ``d M <= L <= M`` for some positive integer
``d``.  The integral stabilizer is

``G_L = G ∩ GL(L) = {g in G : g(L) = L}``,

which is the definition, and it is what :func:`integral_stabilizer` returns: a
predicate subgroup cut out by that condition, with nothing enumerated and no
engine called.

The other three operations go through the finite quotient ``F_M = M / dM``.
Every element of ``G`` that preserves ``M`` acts on ``F_M``, so there is a
morphism ``rho : G -> Aut(F_M)`` with finite image, and ``L`` becomes the
subgroup ``S_L = L / dM`` of ``F_M``.  Then

``G_L = rho^{-1}(Stab_{rho(G)}(S_L))``,

the orbit of ``S_L`` under the finite group ``rho(G)`` indexes the right
cosets ``G_L \\ G``, a transporter between two commensurable lattices is a
preimage of an element carrying one subgroup to the other, and a double coset
space ``V \\ G / G_L`` is computed in that finite image.  One finite quotient
therefore carries those three answers, which would otherwise be a search in an
infinite group.

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

Restriction acts on morphisms by the identity: ``Res(g)`` is ``g``, since
restriction changes which ring acts and never the underlying map, so an
element of ``Res(V)`` moves under ``g`` by reading it in ``V``, applying
``g``, and reading the result back.  Membership in a lattice is decided by
``ModuleMorphism.lift``, which reads the ``ZZ``-span of the finitely many
generator images in the ``QQ``-framing that ``V`` carries; ``Res(V)`` has no
framing of its own, being divisible and so not finitely generated over ``ZZ``,
and none is needed.

What each row needs now.  ``integral_stabilizer`` needs nothing further: it is
definitional, decided on the finite module generators of ``L`` as described at
its own site.  The transporter, the right cosets and the double cosets each
wait on two pieces that are not built: the finite quotient ``F_M = M / dM``
with the morphism ``rho`` and its image, and the integralization algorithm
itself, which ``polyhedral_common`` carries as ``01_RatIntAutomorphy`` and
``sage-indefinite-port`` will supply through the capability layer.

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
    "restriction functor, holds L and M as two subobjects, d M <= L <= M is a "
    "comparison between them, and Res(g) is g.  Membership in a lattice is "
    "decided, so integral_stabilizer is stated.  This row is not: it needs the "
    "finite quotient F_M = M/dM with the morphism rho : G -> Aut(F_M) and its "
    "finite image, and then the integralization algorithm, which "
    "polyhedral_common carries as 01_RatIntAutomorphy and sage-indefinite-port "
    "will supply through the capability layer.  For a stabilizer inside one "
    "lattice use the predicate subgroups of O(L); for the orbit splitting of a "
    "finite-index subgroup of O(L) use the finite character quotient of "
    "orthogonal_quotients"
)


def integral_stabilizer(rational_group, lattice_inclusion):
    r"""Return ``{g in G : g(L) = L}`` for ``L -> Res(V)`` and a rational group ``G``.

    ``g(L) <= L`` is decided on the module generators of ``L``, because ``g``
    is additive and ``L`` is their ``R``-span, and each membership is the lift
    along ``lattice_inclusion``.  That containment alone is not ``g(L) = L``:
    on the hyperbolic plane over ``QQ`` the isometry ``diag(2, 1/2)`` carries
    the line ``ZZ e_0`` onto ``2 ZZ e_0``, properly inside itself.  Asking the
    same of ``g^{-1}`` gives ``L = g(g^{-1}(L)) <= g(L)``, so the two
    containments together are the equality, and both are decided by the same
    lift.  Nothing is enumerated, so the subgroup is constructed for an
    infinite ``G`` as well.
    """
    from dzack_research.preamble.categories.group.predicate_subgroups import (
        predicate_subgroup,
    )
    from dzack_research.preamble.categories.modules.pure.modules import (
        RestrictedScalarsModules,
    )

    lattice = lattice_inclusion.domain()
    space = lattice_inclusion.codomain()
    ring = lattice.base_ring()
    assert space in RestrictedScalarsModules(ring), (
        f"a lattice in a rational space is a monomorphism into a restriction of "
        f"scalars, and {space} is not one"
    )
    assert space.extension_ring() is ring.fraction_field(), (
        f"the rational space is {ring} read along its fraction field, and "
        f"{space} restricts {space.extension_ring()}"
    )

    # ``Res(g)`` is ``g``: restriction never changes the underlying map, so an
    # element of ``Res(V)`` moves by applying ``g`` in ``V`` and reading the
    # image back.  The generators are held in ``V`` for that reason.
    rational_generators = tuple(
        lattice_inclusion(generator).underlying_element()
        for generator in lattice.module_generators()
    )

    def preserves_the_lattice(automorphism):
        inverse = automorphism.inverse()
        return all(
            lattice_inclusion.is_in_image(space.wrap(automorphism(vector)))
            and lattice_inclusion.is_in_image(space.wrap(inverse(vector)))
            for vector in rational_generators
        )

    return predicate_subgroup(
        rational_group,
        preserves_the_lattice,
        f"g(L)=L for L={lattice}",
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
