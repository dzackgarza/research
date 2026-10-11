r"""Integral stabilizers of a commensurability class under a rational group.

Let ``V`` be a finite-dimensional vector space over ``QQ`` and let ``G`` be a
finitely generated subgroup of ``GL(V)``.  Two lattices ``L`` and ``M`` in
``V`` are commensurable when ``d M <= L <= M`` for some positive integer
``d``.  The integral stabilizer is

``G_L = G ∩ GL(L) = {g in G : g(L) = L}``,

which is the definition.  For a generated group with a bounded integral model,
:meth:`IntegralStructureAction.stabilizer` returns the effective preimage of
the stabilizer in the finite residue action; without that finite construction,
the owned-group fallback remains the exact predicate subgroup cut out by the
same condition.

The effective stabilizer and the other three operations go through the finite quotient ``F_M = M / dM``.
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
:class:`FiniteCommensurabilityQuotient`.  A proper finitely generated rational
group is handled here from its supplied generators.  For an infinite group the
caller additionally retains a justified finite stable containing module with
``with_stable_containing_bound``; this hypothesis is not inferred from mere
commensurability.  The common orbit-span construction gives the least stable
module ``M``.  The exponent of ``M/L`` gives ``d`` with ``dM <= L``, and the
finite residue action on ``M/dM`` computes stabilizer generators,
transporters, right cosets and double cosets with live source-group witnesses.
For ``G=O(V)`` and full-rank integral lattices, the direct transporter remains
an isometry of the two pullback lattices.

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
from dzack_research.preamble.categories.group.g_objects import GObjects
from dzack_research.preamble.categories.group.g_sets import FiniteGSets
from dzack_research.preamble.categories.group.groups import (
    OwnedGroups,
    _integer_engine_point,
    _owned_point,
)
from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.modules.pure.modules import (
    Modules,
    RestrictedScalarsModules,
)
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set

class RightCosetDecomposition(SageObject):
    r"""A finite decomposition ``G/G_L`` retaining the subgroup on the right."""

    def __init__(self, ambient_group, right_subgroup, representatives) -> None:
        self._ambient_group = ambient_group
        self._right_subgroup = right_subgroup
        self._representatives = tuple(representatives)

    def ambient_group(self):
        return self._ambient_group

    def right_subgroup(self):
        return self._right_subgroup

    def representatives(self):
        return self._representatives

    def cardinality(self):
        return len(self._representatives)

    def __iter__(self):
        return iter(self.representatives())


class DoubleCosetDecomposition(SageObject):
    r"""A finite decomposition ``H \\ G / G_L`` retaining all three sides."""

    def __init__(self, left_subgroup, ambient_group, right_subgroup, representatives) -> None:
        self._left_subgroup = left_subgroup
        self._ambient_group = ambient_group
        self._right_subgroup = right_subgroup
        self._representatives = tuple(representatives)

    def left_subgroup(self):
        return self._left_subgroup

    def ambient_group(self):
        return self._ambient_group

    def right_subgroup(self):
        return self._right_subgroup

    def representatives(self):
        return self._representatives

    def cardinality(self):
        return len(self._representatives)

    def __iter__(self):
        return iter(self.representatives())


class _FiniteIntegralRepresentation(SageObject):
    r"""Finite orbit of ``L/dM`` with its source-group permutation action."""

    def __init__(self, action) -> None:
        self._action = action
        quotient = action.finite_module()
        self._quotient_points = tuple(quotient)
        selected = action.selected_submodule()
        selected_key = self._submodule_key(selected)
        self._submodules = {selected_key: selected}
        self._witnesses = {selected_key: action.rational_group().one()}
        self._orbit_keys = [selected_key]
        group = action.rational_group()
        generators = action._group_generators()
        steps = generators + tuple(~generator for generator in generators)
        frontier = [selected_key]
        while frontier:
            source_key = frontier.pop()
            source = self._submodules[source_key]
            source_witness = self._witnesses[source_key]
            for step in steps:
                candidate = self._move_submodule(step, source)
                candidate_key = self._submodule_key(candidate)
                if candidate_key in self._submodules:
                    continue
                self._submodules[candidate_key] = candidate
                self._witnesses[candidate_key] = step * source_witness
                self._orbit_keys.append(candidate_key)
                frontier.append(candidate_key)
        self._position_by_key = {key: position for position, key in enumerate(self._orbit_keys)}
        self._point_set = finite_ordered_set(tuple(range(len(self._orbit_keys))))
        self._g_set = FiniteGSets(group)(self._point_set, self._act_on_position)

    def action(self):
        return self._action

    def g_set(self):
        return self._g_set

    def permutation_representation(self):
        return self.g_set().permutation_representation()

    def finite_image(self):
        return self.permutation_representation().image()

    def _submodule_key(self, submodule):
        inclusion = submodule.inclusion()
        return tuple(position for position, point in enumerate(self._quotient_points) if inclusion.is_in_image(point))

    def _move_submodule(self, group_element, submodule):
        quotient = self.action().finite_module()
        automorphism = self.action().quotient_automorphism(group_element)
        inclusion = submodule.inclusion()
        images = tuple(
            automorphism(inclusion(submodule.module_generator(label)))
            for label in submodule.module_generating_set()
        )
        return quotient.subobject_on(images)

    def _act_on_position(self, group_element, position):
        source = self._submodules[self._orbit_keys[int(position)]]
        key = self._submodule_key(self._move_submodule(group_element, source))
        return self._point_set(self._position_by_key[key])

    def orbit_submodules(self):
        return tuple(self._submodules[key] for key in self._orbit_keys)

    def orbit_witnesses(self):
        return tuple(self._witnesses[key] for key in self._orbit_keys)

    def transporter_to(self, submodule):
        return self._witnesses.get(self._submodule_key(submodule))

    @cached_method
    def finite_stabilizer(self):
        image = self.finite_image()
        permutations = self.permutation_representation().codomain()
        selected = self.g_set().point_set()(0)
        return image.subgroup(tuple(
            element
            for element in image
            if _owned_point(permutations(element)(_integer_engine_point(selected))) == selected
        ))

    @cached_method
    def lattice_stabilizer(self):
        group = self.action().rational_group()
        preimage = self.permutation_representation().preimage_subgroup(self.finite_stabilizer())
        generators = preimage.schreier_generators(generators=self.action()._group_generators())
        return group.subgroup(generators)

    @cached_method
    def image_lifts(self):
        return self.action().rational_group().finite_image_lifts(
            self.permutation_representation(), generators=self.action()._group_generators()
        )

    def right_cosets(self):
        return RightCosetDecomposition(
            self.action().rational_group(), self.lattice_stabilizer(), self.orbit_witnesses()
        )

    def double_cosets(self, left_subgroup):
        group = self.action().rational_group()
        if left_subgroup is group:
            left_image = self.finite_image()
        else:
            if left_subgroup.supergroup() is not group:
                raise ValueError(f"the left subgroup {left_subgroup} lies in {left_subgroup.supergroup()}, not in {group}")
            left_image = left_subgroup.image_under(
                self.permutation_representation(), ambient_generators=self.action()._group_generators()
            )
        right_image = self.finite_stabilizer()
        representatives = []
        covered = []
        lifts = self.image_lifts()
        for element in self.finite_image():
            if any(element == known for known in covered):
                continue
            double = tuple(left * element * right for left in left_image for right in right_image)
            for candidate in double:
                if not any(candidate == known for known in covered):
                    covered.append(candidate)
            representatives.append(
                next(witness for image, witness in lifts.items() if image == element)
            )
        return DoubleCosetDecomposition(left_subgroup, group, self.lattice_stabilizer(), tuple(representatives))


class IntegralStructureAction(SageObject):
    r"""The action of a rational isometry group on one selected integral lattice.

    The defining datum is the pair ``(G, i: L -> Res(V))``.  Stabilizers,
    transporters, and the associated coset decompositions are operations of
    that action; the finite quotient ``L/dL`` is a further construction from
    the same selected lattice.
    """

    def __init__(self, rational_group, lattice_inclusion) -> None:
        if rational_group not in OwnedGroups():
            raise TypeError(
                f"an integral-structure action needs an owned rational group with supplied generators, but got {rational_group}"
            )
        self._rational_group = rational_group
        self._lattice_inclusion = lattice_inclusion
        self._stable_containing_bound = None

    def rational_group(self):
        return self._rational_group

    def lattice_inclusion(self):
        return self._lattice_inclusion

    def with_stable_containing_bound(self, containing_inclusion):
        r"""Return this action with a justified finite stable module containing ``L`` retained."""
        result = IntegralStructureAction(self.rational_group(), self.lattice_inclusion())
        result._stable_containing_bound = containing_inclusion
        result._validate_stable_containing_bound()
        return result

    def stable_containing_bound(self):
        return self._stable_containing_bound

    def _group_generators(self):
        group = self.rational_group()
        if group.has_selected_group_resolution() and group.has_selected_finite_group_generating_set():
            return tuple(group.group_generators())
        if group.is_finite() is True:
            return tuple(group)
        raise ValueError(
            f"the rational group {group} needs a finite selected generating family for integral-structure computation"
        )

    @cached_method
    def _ambient_group_inclusion(self):
        group = self.rational_group()
        inclusion = OwnedGroups().Mor(group, group).identity()
        current = group
        while current.supergroup() is not current:
            step = current.inclusion()
            inclusion = OwnedGroups().Mor(group, step.codomain())(step) * inclusion
            current = current.supergroup()
        ambient = self.lattice_inclusion().codomain().module_over_extension()
        if current is not ambient.Aut():
            raise ValueError(
                f"the rational group {group} must be a represented subgroup of Aut({ambient}), but its ambient group is {current}"
            )
        return inclusion

    @cached_method
    def ambient_action_functor(self):
        lattice = self.lattice_inclusion().domain()
        ring = lattice.base_ring()
        space = self.lattice_inclusion().codomain()
        if space not in RestrictedScalarsModules(ring):
            raise TypeError(
                f"the lattice inclusion must land in a restriction-of-scalars module, but it lands in {space}"
            )
        ambient = space.module_over_extension()
        restrict = Modules(ambient.base_ring()).restriction_of_scalars(ring.fraction_field_map())
        group_inclusion = self._ambient_group_inclusion()
        return GroupActionFunctor(
            self.rational_group(),
            Modules(ring),
            space,
            lambda element: restrict(
                ambient.module_category().Mor(ambient, ambient)(group_inclusion(element))
            ),
        )

    def _validate_stable_containing_bound(self):
        containing = self.stable_containing_bound()
        if containing is None:
            return
        selected = self.lattice_inclusion()
        if containing.codomain() is not selected.codomain():
            raise ValueError("the stable containing bound and selected lattice must lie in one rational space")
        if containing.domain().module_generating_set().cardinality().is_finite() is not True:
            raise ValueError("the stable containing bound must be finitely generated")
        selected.factor_through(containing)
        action = self.ambient_action_functor()
        generators = self._group_generators()
        classifying = self.rational_group().classifying_category()
        point = classifying.an_object()
        arrows = classifying.Mor(point, point)
        for element in generators + tuple(~generator for generator in generators):
            arrow = action(arrows(element))
            for generator in containing.domain().module_generators():
                if not containing.is_in_image(arrow(containing(generator))):
                    raise ValueError(
                        f"the supplied containing module {containing.domain()} is not stable under {element}"
                    )

    @cached_method
    def invariant_module_construction(self):
        group = self.rational_group()
        containing = self.stable_containing_bound()
        if group.is_finite() is not True and containing is None:
            raise ValueError(
                f"integralizing the infinite rational group {group} requires a justified finite stable "
                "containing module; supply it with with_stable_containing_bound(...)"
            )
        return GObjects(group, Modules(self.lattice_inclusion().domain().base_ring())).orbit_generated_submodule(
            self.ambient_action_functor(), self.lattice_inclusion(), containing=containing
        )

    def invariant_module(self):
        r"""Return the least represented stable module ``M`` containing the selected lattice."""
        return self.invariant_module_construction().inclusion()

    invariant_overlattice = invariant_module

    @cached_method
    def quotient_exponent(self):
        invariant = self.invariant_module()
        selected_into_invariant = self.lattice_inclusion().factor_through(invariant)
        quotient = selected_into_invariant.cokernel()
        exponent = quotient.exponent()
        if exponent == quotient.base_ring().zero():
            raise ValueError(
                f"the selected lattice {self.lattice_inclusion().domain()} has infinite index in the stable module {invariant.domain()}"
            )
        return abs(exponent)

    @cached_method
    def finite_quotient_action(self):
        return FiniteCommensurabilityQuotient(
            self.rational_group(), self.invariant_module(), self.quotient_exponent()
        )

    def finite_module(self):
        return self.finite_quotient_action().quotient_module()

    def finite_projection(self):
        return self.finite_quotient_action().quotient_projection()

    def quotient_automorphism(self, automorphism):
        return self.finite_quotient_action().quotient_automorphism(automorphism)

    def intermediate_image(self, lattice_inclusion):
        return self.finite_quotient_action().intermediate_image(lattice_inclusion)

    @cached_method
    def selected_submodule(self):
        return self.intermediate_image(self.lattice_inclusion())

    @cached_method
    def residue_action_functor(self):
        quotient = self.finite_module()
        return GroupActionFunctor(
            self.rational_group(), Modules(quotient.base_ring()), quotient, self.quotient_automorphism
        )

    @cached_method
    def finite_representation(self):
        return _FiniteIntegralRepresentation(self)

    def stabilizer(self):
        r"""Return ``{g in G : g(L)=L}`` for the selected lattice ``L``."""
        rational_group = self.rational_group()
        lattice_inclusion = self.lattice_inclusion()
        if (
            rational_group.has_selected_group_resolution()
            and rational_group.has_selected_finite_group_generating_set()
            and (rational_group.is_finite() is True or self.stable_containing_bound() is not None)
        ):
            return self.finite_representation().lattice_stabilizer()

        lattice = lattice_inclusion.domain()
        space = lattice_inclusion.codomain()
        ring = lattice.base_ring()
        assert space in RestrictedScalarsModules(ring), (
            f"{lattice} is not given as a lattice in a rational space: its inclusion "
            f"must land in a {ring}-module obtained by restriction of scalars, but it "
            f"lands in {space}, which is in {space.category()}"
        )
        assert space.extension_ring() is ring.fraction_field(), (
            f"{lattice} is not a lattice in a rational space: {space} must be a "
            f"module over the fraction field of {ring} with scalars restricted to "
            f"{ring}, but it is a module over {space.extension_ring()}"
        )

        rational_generators = tuple(lattice_inclusion(generator).underlying_element() for generator in lattice.module_generators())

        def preserves_the_lattice(automorphism):
            inverse = automorphism.inverse()
            return all(
                lattice_inclusion.is_in_image(space.wrap(automorphism(vector))) and lattice_inclusion.is_in_image(space.wrap(inverse(vector))) for vector in rational_generators
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
            case _ if target_inclusion.codomain() is space and space in RestrictedScalarsModules(space.base_ring()) and rational_group is space.module_over_extension().Aut():
                return _full_orthogonal_integral_transporter(
                    rational_group,
                    source_inclusion,
                    target_inclusion,
                )
            case _:
                pass
        if not (
            rational_group.has_selected_group_resolution()
            and rational_group.has_selected_finite_group_generating_set()
        ):
            raise ValueError(
                f"a transporter in {rational_group} needs a finite selected generating family"
            )
        try:
            target_submodule = self.intermediate_image(target_inclusion)
        except (ValueError, TypeError):
            return None
        witness = self.finite_representation().transporter_to(target_submodule)
        if witness is None:
            return None
        if not self._carries_lattice(witness, source_inclusion, target_inclusion):
            raise ArithmeticError(
                "a finite residue-action witness does not carry the actual source lattice to the target"
            )
        return witness

    def _carries_lattice(self, automorphism, source_inclusion, target_inclusion):
        if source_inclusion.codomain() is not target_inclusion.codomain():
            return False
        space = source_inclusion.codomain()
        inverse = ~automorphism
        return all(
            target_inclusion.is_in_image(
                space.wrap(automorphism(source_inclusion(generator).underlying_element()))
            )
            for generator in source_inclusion.domain().module_generators()
        ) and all(
            source_inclusion.is_in_image(
                space.wrap(inverse(target_inclusion(generator).underlying_element()))
            )
            for generator in target_inclusion.domain().module_generators()
        )

    def right_cosets(self):
        r"""Return ``G/G_L`` with the selected lattice stabilizer on the right."""
        return self.finite_representation().right_cosets()

    def double_cosets(self, subgroup):
        r"""Return ``subgroup \\ G / G_L`` with all three sides retained."""
        rational_group = self.rational_group()
        if subgroup is not rational_group and subgroup.supergroup() is not rational_group:
            raise ValueError(
                f"cannot form the double cosets {subgroup} \\ G / G_L for G = "
                f"{rational_group}: {subgroup} must be a subgroup of G, but it is a "
                f"subgroup of {subgroup.supergroup()}"
            )
        return self.finite_representation().double_cosets(subgroup)

    lattice_stabilizer = stabilizer

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
            raise ValueError(f"cannot form the quotient M/dM of {lattice} with d = {self._modulus}: the modulus d must be positive")

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
        lattice = self.reference_lattice()
        inclusion = self.reference_inclusion()
        space = self.ambient_restricted_space()

        def image(label):
            embedded = inclusion(lattice.module_generator(label)).underlying_element()
            moved = space.wrap(automorphism(embedded))
            return inclusion.lift(moved)

        forward = lattice.Aut()({label: image(label) for label in lattice.module_generating_set()})
        inverse = ~automorphism
        if not all(
            inclusion.is_in_image(
                space.wrap(inverse(inclusion(generator).underlying_element()))
            )
            for generator in lattice.module_generators()
        ):
            raise ValueError(
                f"cannot restrict {automorphism} to {lattice}: its inverse does not preserve the reference lattice"
            )
        return forward

    def quotient_automorphism(self, automorphism):
        r"""Return the induced automorphism of ``F_M``."""
        quotient = self.quotient_module()
        projection = self.quotient_projection()
        restricted = self.restricted_automorphism(automorphism)
        lattice = self.reference_lattice()
        return quotient.Aut()({label: projection(restricted(lattice.module_generator(label))) for label in lattice.module_generating_set()})

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
            raise ValueError(
                f"{lattice_inclusion.domain()} cannot lie between dM and M for M = "
                f"{self.reference_lattice()}: it lies in {lattice_inclusion.codomain()}, not "
                f"in the rational space {self.ambient_restricted_space()} containing M"
            )
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

    This is the supported case ``G=O(V)``.  The isometry homset of the two
    pullback Gram lattices supplies an integral isometry between them.  Rationalizing that map and
    conjugating through the two actual embeddings gives an automorphism of
    ``V``; the owned orthogonal-group constructor verifies form preservation.
    """
    if source_inclusion.codomain() is not target_inclusion.codomain():
        raise ValueError(
            f"no element of {rational_group} can carry {source_inclusion.domain()} to "
            f"{target_inclusion.domain()}: they lie in different rational spaces, "
            f"{source_inclusion.codomain()} and {target_inclusion.codomain()}"
        )
    space = source_inclusion.codomain()
    source = source_inclusion.domain()
    target = target_inclusion.domain()
    ring = source.base_ring()
    assert target.base_ring() is ring and ring is _own_ring(SageZZ), (
        f"cannot search for an isometry carrying {source} to {target}: the search works only for lattices over ZZ, and these are over {ring} and {target.base_ring()}"
    )
    if space not in RestrictedScalarsModules(ring):
        raise TypeError(
            f"cannot compare {source} and {target} as lattices in a rational quadratic "
            f"space: they must lie in a {ring}-module obtained by restriction of scalars, "
            f"but {space} is in {space.category()}"
        )
    ambient = space.module_over_extension()
    assert rational_group is ambient.Aut(), (
        f"cannot search {rational_group} for an element carrying {source} to {target}: "
        f"this search finds isometries in the full orthogonal group "
        f"O(V) of {ambient} only, and a proper subgroup needs the integral structure "
        f"of that subgroup"
    )
    assert int(source.module_rank()) == int(ambient.module_rank()) and int(target.module_rank()) == int(ambient.module_rank()), (
        f"cannot search for an isometry of {ambient} carrying {source} to {target}: "
        f"the search needs lattices of full rank {ambient.module_rank()}, but they "
        f"have ranks {source.module_rank()} and {target.module_rank()}"
    )

    def embedded_basis(inclusion):
        domain = inclusion.domain()
        return tuple(inclusion(domain.module_generator(label)).underlying_element() for label in domain.module_generating_set())

    source_basis = embedded_basis(source_inclusion)
    target_basis = embedded_basis(target_inclusion)

    def pullback_lattice(basis):
        rows = tuple(tuple(ring(ambient.b(left, right)) for right in basis) for left in basis)
        return Lattices(ring)(rows)

    source_lattice = pullback_lattice(source_basis)
    target_lattice = pullback_lattice(target_basis)
    isometries = source_lattice.Isom(target_lattice)
    if isometries.is_empty():
        return None
    lattice_witness = isometries.an_element()

    extension_ring = ambient.base_ring()
    scalar_map = ring.Mor(extension_ring)(lambda element: extension_ring(element))
    source_rational = source.base_change(scalar_map)
    target_rational = target.base_change(scalar_map)
    source_labels = tuple(source_rational.module_generating_set())
    source_lattice_generators = tuple(source_lattice.module_generators())

    def _coordinates(element):
        vector = element.to_vector()
        return tuple(vector(label) for label in target_lattice.module_generating_set())

    target_labels = tuple(target_rational.module_generating_set())
    source_span = source_rational.module_category().Mor(source_rational, ambient)({label: source_basis[position] for position, label in enumerate(source_labels)})
    target_span = target_rational.module_category().Mor(target_rational, ambient)({label: target_basis[position] for position, label in enumerate(target_labels)})
    witness = source_rational.module_category().Mor(source_rational, target_rational)(
        {
            source_label: target_rational.linear_combination(
                {
                    target_labels[target_position]: extension_ring(coefficient)
                    for target_position, coefficient in enumerate(_coordinates(lattice_witness(source_lattice_generators[source_position])))
                    if coefficient
                }
            )
            for source_position, source_label in enumerate(source_labels)
        }
    )
    ambient_map = target_span * witness * source_span.inverse()
    candidate = ambient.Aut()({label: ambient_map(ambient.module_generator(label)) for label in ambient.module_generating_set()})

    inverse = ~candidate
    for vector in source_basis:
        if not target_inclusion.is_in_image(space.wrap(candidate(vector))):
            raise ArithmeticError(f"the isometry {candidate} of {ambient} does not carry {source} into {target}: it sends {vector} outside {target}")
    for vector in target_basis:
        if not source_inclusion.is_in_image(space.wrap(inverse(vector))):
            raise ArithmeticError(f"the isometry {candidate} of {ambient} does not carry {source} onto {target}: its inverse sends {vector} outside {source}")
    return candidate


__all__ = [
    "DoubleCosetDecomposition",
    "FiniteCommensurabilityQuotient",
    "IntegralStructureAction",
    "RightCosetDecomposition",
]
