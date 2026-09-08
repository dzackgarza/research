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
its own site.  :class:`FiniteCommensurabilityQuotient` now owns the structural
finite quotient ``F_M=M/dM``, its quotient map, the action ``rho`` for a
represented reference lattice through its actual stabilizer ``G_M``, and every
intermediate subgroup ``S_L=L/dM``.  The transporter, right cosets and double cosets still need the
finite image together with the integralization/lifting algorithm that turns a
finite-quotient representative into an actual element of the specified
rational group.  For ``G=O(V)`` and full-rank integral lattices, the existing
OSCAR integral-isometry witness now supplies a transporter and is conjugated
through the actual lattice embeddings into a live element of ``O(V)``.  A
proper prescribed rational subgroup still requires the separate lifting
theorem.  ``polyhedral_common`` carries that arithmetic as
``01_RatIntAutomorphy`` and ``sage-indefinite-port`` is the planned native
provider.

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

from sage.misc.cachefunc import cached_method
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.functors.group_actions import GroupActionFunctor
from dzack_research.preamble.categories.lattice_engines import integral_isometry_witness
from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_homset,
)
from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

_ABSENCE = (
    "the structural objects exist: Res(V) holds L and M as two subobjects, "
    "d M <= L <= M is verified by factorization, and a reference M has the "
    "represented finite quotient F_M=M/dM with its G_M-action functor and "
    "intermediate subgroup S_L.  This row is not complete: it still needs the "
    "finite action image together with the integralization algorithm that lifts "
    "the required quotient representative to an actual element of a prescribed "
    "proper G.  The full O(V), full-rank case uses the OSCAR integral-isometry "
    "witness directly.  The remaining general lifting operation is the one "
    "polyhedral_common carries as 01_RatIntAutomorphy and sage-indefinite-port "
    "will supply through the capability layer.  For a stabilizer inside one "
    "lattice use the predicate subgroups of O(L); for the orbit splitting of a "
    "finite-index subgroup of O(L) use the finite character quotient of "
    "orthogonal_quotients"
)


class FiniteCommensurabilityQuotient(SageObject):
    r"""The finite module ``F_M=M/dM`` controlling a commensurability class.

    The selected reference lattice is a monomorphism ``M -> Res(V)``.  Its
    actual stabilizer ``G_M={g in G:g(M)=M}`` acts on ``M`` and hence on
    ``M/dM``; no hypothesis that all of ``G`` preserves ``M`` is smuggled into
    the construction.  The action is retained as an actual functor
    ``B G_M -> ZZ-Mod``; no finite image is guessed or enumerated here.

    For an intermediate lattice ``dM <= L <= M``, :meth:`intermediate_image`
    returns the actual subobject ``S_L=L/dM <= F_M``.  This supplies the finite
    quotient and action needed by the external integralization theorem while
    keeping the later lift back into ``G`` as a separate obligation.
    """

    def __init__(self, rational_group, reference_inclusion, modulus) -> None:
        self._rational_group = rational_group
        self._reference_inclusion = reference_inclusion
        lattice = reference_inclusion.domain()
        ring = lattice.base_ring()
        self._modulus = ring(modulus)
        if self._modulus <= ring.zero():
            raise ValueError("a commensurability modulus is positive")

    def rational_group(self):
        return self._rational_group

    @cached_method
    def reference_stabilizer(self):
        r"""Return ``G_M={g in G:g(M)=M}``, the group acting on ``M/dM``."""
        return integral_stabilizer(
            self.rational_group(),
            self.reference_inclusion(),
        )

    def reference_inclusion(self):
        return self._reference_inclusion

    def reference_lattice(self):
        return self.reference_inclusion().domain()

    def ambient_restricted_space(self):
        return self.reference_inclusion().codomain()

    def modulus(self):
        return self._modulus

    @cached_method
    def scaling_morphism(self):
        r"""Return multiplication by ``d`` on ``M``."""
        lattice = self.reference_lattice()
        modulus = self.modulus()
        return module_homset(lattice, lattice)(
            {
                label: lattice.scalar_multiple(
                    modulus,
                    lattice.module_generator(label),
                )
                for label in lattice.module_generating_set()
            }
        )

    @cached_method
    def quotient_module(self):
        r"""Return ``F_M=M/dM`` as the actual cokernel of multiplication by ``d``."""
        return self.scaling_morphism().cokernel()

    @cached_method
    def quotient_projection(self):
        r"""Return the quotient morphism ``M -> M/dM``."""
        return self.scaling_morphism().cokernel_projection()

    def restricted_automorphism(self, automorphism):
        r"""Restrict one ``g in G`` to the stable reference lattice ``M``."""
        if automorphism not in self.reference_stabilizer():
            raise ValueError("the selected automorphism does not stabilize the reference lattice")
        lattice = self.reference_lattice()
        inclusion = self.reference_inclusion()
        space = self.ambient_restricted_space()

        def image(label):
            embedded = inclusion(lattice.module_generator(label)).underlying_element()
            moved = space.wrap(automorphism(embedded))
            return inclusion.lift(moved)

        return lattice.Aut()({label: image(label) for label in lattice.module_generating_set()})

    def quotient_automorphism(self, automorphism):
        r"""Return the induced automorphism of ``F_M``."""
        quotient = self.quotient_module()
        projection = self.quotient_projection()
        restricted = self.restricted_automorphism(automorphism)
        lattice = self.reference_lattice()
        return quotient.Aut()(
            {
                label: projection(restricted(lattice.module_generator(label)))
                for label in lattice.module_generating_set()
            }
        )

    @cached_method
    def action_functor(self):
        r"""Return the genuine action functor ``B G_M -> ZZ-Mod`` on ``F_M``."""
        quotient = self.quotient_module()
        return GroupActionFunctor(
            self.reference_stabilizer(),
            Modules(self.reference_lattice().base_ring()),
            quotient,
            self.quotient_automorphism,
        )

    def intermediate_image(self, lattice_inclusion):
        r"""Return ``S_L=L/dM`` inside ``F_M`` for ``dM <= L <= M``.

        Both containments are verified through the actual inclusions in
        ``Res(V)``.  The returned object is the image of the composite
        ``L -> M -> M/dM`` and therefore retains its inclusion in ``F_M``.
        """
        if lattice_inclusion.codomain() is not self.ambient_restricted_space():
            raise ValueError("an intermediate lattice lies in the same restricted rational space")
        into_reference = lattice_inclusion.factor_through(self.reference_inclusion())
        scaled_reference = self.reference_inclusion() * self.scaling_morphism()
        scaled_reference.factor_through(lattice_inclusion)
        return (self.quotient_projection() * into_reference).image()


def finite_commensurability_quotient(rational_group, reference_inclusion, modulus):
    r"""Return ``M/dM`` with the action of the actual reference stabilizer ``G_M``."""
    return FiniteCommensurabilityQuotient(
        rational_group,
        reference_inclusion,
        modulus,
    )


def _full_orthogonal_integral_transporter(
    rational_group,
    source_inclusion,
    target_inclusion,
):
    r"""Transport two full-rank integral lattices inside one rational quadratic space.

    This is the supported case ``G=O(V)``.  OSCAR supplies an integral isometry
    between the two pullback Gram lattices.  Rationalizing that map and
    conjugating through the two actual embeddings gives an automorphism of
    ``V``; the owned orthogonal-group constructor verifies form preservation.
    """
    if source_inclusion.codomain() is not target_inclusion.codomain():
        raise ValueError("an integral transporter compares lattices in one rational space")
    space = source_inclusion.codomain()
    source = source_inclusion.domain()
    target = target_inclusion.domain()
    ring = source.base_ring()
    if target.base_ring() is not ring or ring is not _own_ring(SageZZ):
        raise NotImplementedError(
            "the OSCAR integral-isometry transporter currently uses full-rank ZZ-lattices"
        )
    from dzack_research.preamble.categories.modules.pure.modules import (
        RestrictedScalarsModules,
    )

    if space not in RestrictedScalarsModules(ring):
        raise TypeError("the two lattices must lie in a restriction of a rational quadratic space")
    ambient = space.module_over_extension()
    if rational_group is not ambient.Aut():
        raise NotImplementedError(
            "the maintained OSCAR witness solves the full orthogonal-group transporter; "
            "transport inside a prescribed proper rational subgroup still needs integralization"
        )
    if int(source.module_rank()) != int(ambient.module_rank()) or int(target.module_rank()) != int(
        ambient.module_rank()
    ):
        raise NotImplementedError(
            "the maintained OSCAR specialization currently transports full-rank lattices"
        )

    def embedded_basis(inclusion):
        domain = inclusion.domain()
        return tuple(
            inclusion(domain.module_generator(label)).underlying_element()
            for label in domain.module_generating_set()
        )

    source_basis = embedded_basis(source_inclusion)
    target_basis = embedded_basis(target_inclusion)

    def pullback_lattice(basis):
        rows = tuple(
            tuple(ring(ambient.b(left, right)) for right in basis)
            for left in basis
        )
        return Lattices(ring)(rows)

    source_lattice = pullback_lattice(source_basis)
    target_lattice = pullback_lattice(target_basis)
    witness_rows = integral_isometry_witness(
        source_lattice.gram_tensor(),
        target_lattice.gram_tensor(),
    )
    if witness_rows is None:
        return None

    extension_ring = ambient.base_ring()
    scalar_map = ring.Mor(extension_ring)(lambda element: extension_ring(element))
    source_rational = source.base_change(scalar_map)
    target_rational = target.base_change(scalar_map)
    source_labels = tuple(source_rational.module_generating_set())
    target_labels = tuple(target_rational.module_generating_set())
    if len(witness_rows) != len(source_labels):
        raise ArithmeticError("the OSCAR transporter witness has the wrong source rank")

    source_span = module_homset(source_rational, ambient)(
        {
            label: source_basis[position]
            for position, label in enumerate(source_labels)
        }
    )
    target_span = module_homset(target_rational, ambient)(
        {
            label: target_basis[position]
            for position, label in enumerate(target_labels)
        }
    )
    witness = module_homset(source_rational, target_rational)(
        {
            source_label: target_rational.linear_combination(
                {
                    target_labels[target_position]: extension_ring(coefficient)
                    for target_position, coefficient in enumerate(witness_rows[source_position])
                    if coefficient
                }
            )
            for source_position, source_label in enumerate(source_labels)
        }
    )
    ambient_map = target_span * witness * source_span.inverse()
    candidate = ambient.Aut()(
        {
            label: ambient_map(ambient.module_generator(label))
            for label in ambient.module_generating_set()
        }
    )

    inverse = ~candidate
    for vector in source_basis:
        if not target_inclusion.is_in_image(space.wrap(candidate(vector))):
            raise ArithmeticError("the OSCAR transporter does not carry the source lattice into the target")
    for vector in target_basis:
        if not source_inclusion.is_in_image(space.wrap(inverse(vector))):
            raise ArithmeticError("the OSCAR transporter does not carry the target lattice back to the source")
    return candidate


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
    if source_inclusion.codomain() is target_inclusion.codomain():
        space = source_inclusion.codomain()
        try:
            ambient = space.module_over_extension()
        except AttributeError:
            ambient = None
        if ambient is not None and rational_group is ambient.Aut():
            return _full_orthogonal_integral_transporter(
                rational_group,
                source_inclusion,
                target_inclusion,
            )
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
    "FiniteCommensurabilityQuotient",
    "finite_commensurability_quotient",
    "integral_double_cosets",
    "integral_right_cosets",
    "integral_stabilizer",
    "integral_transporter",
]
