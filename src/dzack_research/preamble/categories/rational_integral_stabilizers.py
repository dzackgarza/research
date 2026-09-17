r"""Integral stabilizers of a commensurability class under a rational group.

Let ``V`` be a finite-dimensional vector space over ``QQ`` and let ``G`` be a
finitely generated subgroup of ``GL(V)``.  Two lattices ``L`` and ``M`` in
``V`` are commensurable when ``d M <= L <= M`` for some positive integer
``d``.  The integral stabilizer is

``G_L = G ∩ GL(L) = {g in G : g(L) = L}``,

which is the definition, and it is what :meth:`IntegralStructureAction.stabilizer` returns: a
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

``L.Mono(Res(V))(images)``,

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

The structural finite quotient remains available locally through
:class:`FiniteCommensurabilityQuotient`.  For a proper finitely generated
rational isometry group, ``sage-indefinite-port`` now supplies the T2
``IntegralStructureAction``: it constructs the invariant over-lattice, the
exponent and finite submodule action, lifts the lattice stabilizer and
transporters back to live rational isometries, and returns ``G/G_L`` and
``V \ G / G_L`` with their sides retained.  This file reaches that operation
through the lazy lattice-engine capability boundary; it does not import the
port directly.  For ``G=O(V)`` and full-rank integral lattices, the existing
OSCAR integral-isometry witness remains the direct transporter specialization.
Predicate-only rational subgroups with no represented generating family still
do not satisfy the T2 input contract and are refused rather than approximated.

One further gap bounds the argument these operations take.  The preamble names
no general linear group of a module: ``V.module_category().Mor(V, V)`` is the
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
from dzack_research.preamble.categories.group.groups import OwnedGroups
from dzack_research.preamble.categories.lattice_engines import _integral_isometry_witness
from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.modules.pure.modules import (
    Modules,
    RestrictedScalarsModules,
)
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.engine_capabilities import engine_capabilities

_ABSENCE = (
    "the structural finite quotient exists, but a prescribed proper rational "
    "group must either be the T2 RationalMatrixGroup supplied by "
    "sage-indefinite-port or have another exact integralization provider.  "
    "Predicate-only subgroups with no represented generating family cannot be "
    "recovered by bounding denominators or filtering ambient generators"
)


def _ported_rational_group(rational_group):
    r"""Return the rational group supplied by the T2 provider, or ``None`` for an owned group."""
    match rational_group:
        case _ if rational_group in OwnedGroups():
            return None
        case _:
            return rational_group


def _ported_integral_structure(rational_group, lattice_inclusion):
    r"""Reach T2 through the registered lazy provider without importing it here."""
    selected = _ported_rational_group(rational_group)
    assert selected is not None, (
        f"integral-structure transport/coset computation requires the registered T2 rational-group provider: {_ABSENCE}"
    )
    return engine_capabilities.compute(
        "lattice.rational_integral_structure",
        selected,
        lattice_inclusion,
    )



class IntegralStructureAction(SageObject):
    r"""The action of a rational isometry group on one selected integral lattice.

    The defining datum is the pair ``(G, i: L -> Res(V))``.  Stabilizers,
    transporters, and the associated coset decompositions are operations of
    that action; the finite quotient ``L/dL`` is a further construction from
    the same selected lattice.
    """

    def __init__(self, rational_group, lattice_inclusion) -> None:
        self._rational_group = rational_group
        self._lattice_inclusion = lattice_inclusion

    def rational_group(self):
        return self._rational_group

    def lattice_inclusion(self):
        return self._lattice_inclusion

    def stabilizer(self):
        r"""Return ``{g in G : g(L)=L}`` for the selected lattice ``L``."""
        rational_group = self.rational_group()
        lattice_inclusion = self.lattice_inclusion()
        match _ported_rational_group(rational_group):
            case None:
                pass
            case _:
                return _ported_integral_structure(
                    rational_group,
                    lattice_inclusion,
                ).lattice_stabilizer()

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

        return rational_group.predicate_subgroup(
            preserves_the_lattice,
            f"g(L)=L for L={lattice}",
        )

    def transporter(self, target_inclusion):
        r"""Return one ``g in G`` with ``g(L_1)=L_2``, or ``None``."""
        rational_group = self.rational_group()
        source_inclusion = self.lattice_inclusion()
        space = source_inclusion.codomain()
        match space:
            case _ if (
                target_inclusion.codomain() is space
                and space in RestrictedScalarsModules(space.base_ring())
                and rational_group is space.module_over_extension().Aut()
            ):
                return _full_orthogonal_integral_transporter(
                    rational_group,
                    source_inclusion,
                    target_inclusion,
                )
            case _:
                pass
        return _ported_integral_structure(
            rational_group,
            source_inclusion,
        ).transporter(source_inclusion, target_inclusion)

    def right_cosets(self):
        r"""Return ``G/G_L`` with the selected lattice stabilizer on the right."""
        return _ported_integral_structure(
            self.rational_group(),
            self.lattice_inclusion(),
        ).right_cosets()

    def double_cosets(self, subgroup):
        r"""Return ``subgroup \\ G / G_L`` with all three sides retained."""
        rational_group = self.rational_group()
        action = _ported_integral_structure(
            rational_group,
            self.lattice_inclusion(),
        )
        if subgroup.supergroup() is not rational_group:
            raise ValueError(
                "the left subgroup must have the selected rational group as supergroup"
            )
        return action.double_cosets(subgroup)

    def finite_quotient(self, modulus):
        r"""Return the finite commensurability quotient ``L/modulus*L``."""
        return FiniteCommensurabilityQuotient(
            self.rational_group(),
            self.lattice_inclusion(),
            modulus,
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
        return IntegralStructureAction(
            self.rational_group(),
            self.reference_inclusion(),
        ).stabilizer()

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
        return lattice.module_category().Mor(lattice, lattice)(
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
    assert target.base_ring() is ring and ring is _own_ring(SageZZ), (
        "the maintained OSCAR integral-isometry transporter is represented for ZZ-lattices"
    )
    if space not in RestrictedScalarsModules(ring):
        raise TypeError("the two lattices must lie in a restriction of a rational quadratic space")
    ambient = space.module_over_extension()
    assert rational_group is ambient.Aut(), (
        "the maintained OSCAR witness represents the full orthogonal-group transporter; "
        "a prescribed proper rational subgroup requires the registered integral-structure provider"
    )
    assert int(source.module_rank()) == int(ambient.module_rank()) and int(
        target.module_rank()
    ) == int(ambient.module_rank()), (
        "the maintained OSCAR specialization represents full-rank lattice transport"
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
    witness_rows = _integral_isometry_witness(
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

    source_span = source_rational.module_category().Mor(source_rational, ambient)(
        {
            label: source_basis[position]
            for position, label in enumerate(source_labels)
        }
    )
    target_span = target_rational.module_category().Mor(target_rational, ambient)(
        {
            label: target_basis[position]
            for position, label in enumerate(target_labels)
        }
    )
    witness = source_rational.module_category().Mor(source_rational, target_rational)(
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


__all__ = [
    "FiniteCommensurabilityQuotient",
    "IntegralStructureAction",
]
