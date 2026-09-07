r"""Modules over a group algebra: ``Modules(R[G])``.

An ``R[G]``-module is a module over the ring ``R[G]``.  Restricting the
ring action along the group inclusion ``G -> R[G]`` gives a left action of
``G`` by ``R``-linear automorphisms, and conversely an ``R``-module with a
left ``G``-action is an ``R[G]``-module by linear extension; this is the
equivalence ``GObjects(G, Modules(R)) ~ Modules(R[G])``.  Since ``ZZ`` is
initial, every ``R[G]``-module is a ``ZZ[G]``-module by restriction along
``ZZ[G] -> R[G]``, and the functors stated over ``ZZ`` apply to it.

Invariants and coinvariants are scalar change along the augmentation
``R[G] -> R``: ``M^G = Hom_{R[G]}(R, M)`` is the coextension and
``M_G = R tensor_{R[G]} M`` the extension, computed as the wide equalizer
and coequalizer of the action on a finite group generating set.
"""

from sage.categories.map import Map
from sage.misc.cachefunc import cached_method
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.richcmp import op_EQ, op_NE

from dzack_research.preamble.categories.abstract_categories.constructions import (
    CoequalizerOfFamily,
    EqualizerOfFamily,
)
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.algebras.group_algebras import (
    GroupAlgebra,
    GroupAlgebras,
)
from dzack_research.preamble.categories.functors.scalar_change import (
    ScalarExtensionFunctor,
)
from dzack_research.preamble.categories.functors.core import Functor, NaturalTransformation
from dzack_research.preamble.categories.group.class_functions import (
    finite_group_class_function,
)
from dzack_research.preamble.categories.group.g_objects import GObjectHomset, GObjects
from dzack_research.preamble.categories.group.magmas import AdditiveGroups
from dzack_research.preamble.categories.group.groups import (
    OwnedGroups,
    _engine_group,
    _owned_group,
)
from dzack_research.preamble.categories.modules.general_modules import GeneralModules
from dzack_research.preamble.categories.modules.group_modules.isotypic import (
    _split_irreducible_characters,
    isotypic_component,
    isotypic_decomposition,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
    _ModuleHomsetCommonMethods,
    module_coefficients,
    module_homset,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    FinitelyGeneratedFreeModules,
    FinitelyPresentedModules,
    LinearEndCategoryConstruction,
    LinearHomModules,
    Modules,
    ModulesWithChosenFinitePresentation,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedRings,
    _engine_element,
    _engine_ring,
    _own_ring,
    _owned_ring,
    ring_morphism,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    finite_indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import (
    CoproductOfFamily,
    Sets,
)
from dzack_research.preamble.owned_category import object_of


class GroupModuleHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return GroupModuleHomset


class ModulesOverGroupAlgebra(Modules):
    r"""``Modules(R[G])``: the modules over a group algebra.

    ``Modules(S)`` constructs this category whenever ``S`` is a group
    algebra, so the spelling is ``Modules(R[G])``.  A represented object is an
    actual module with scalar ring ``R[G]``.  It retains the exact ``R``-module
    whose action was linearized as its coefficient restriction; equivariant
    morphisms are the ``R``-linear maps between those restrictions commuting
    with ``G``.
    """

    def __init__(self, group_algebra) -> None:
        # Read once, at construction: the group algebra itself is an object
        # of this category, the regular module, and asking it for its group
        # after it is placed here would come back to this category.
        self._acting_group = group_algebra.group()
        self._coefficient_ring = group_algebra.base_ring()
        super().__init__(group_algebra)

    def group_algebra(self):
        return self.base_ring()

    def coefficient_ring(self):
        r"""``R``, the scalars of the group algebra ``R[G]``."""
        return self._coefficient_ring

    def acting_group(self):
        return self._acting_group

    def _repr_object_names(self):
        return f"modules over {self.base_ring()}"

    def super_categories(self):
        # Scalar restriction to R and evaluation of the associated BG-functor
        # are genuine functors, not literal category inclusions.  The group
        # module keeps both structures as defining data instead of obtaining
        # them from a false supercategory edge.
        return [GObjects(self.acting_group(), Modules(self.coefficient_ring()))]

    _HomCategory = GroupModuleHomCategoryConstruction
    _EndCategory = LinearEndCategoryConstruction

    def an_object(self):
        r"""The trivial action on the free module of rank one."""
        ring = self.coefficient_ring()
        return Modules(ring).trivial_action(self.acting_group())(Modules(ring).an_object())

    def _call_(self, module, action):
        r"""Construct the actual ``R[G]``-module defined by the supplied action."""
        if isinstance(action, Functor):
            if action.domain() != self.acting_group().classifying_category():
                raise ValueError("the action functor has the wrong acting group")
            return _equip_action(module, action)
        if isinstance(action, Map) and action.domain() is self.group_algebra():
            return _equip_action(module, action)
        return _equip_action(module, self.acting_group(), action)

    def is_semisimple(self) -> bool:
        r"""Maschke's theorem, asked of the group algebra."""
        return self.base_ring().is_semisimple()

    # The three scalar-change functors along the augmentation R[G] -> R.

    def _augmentation(self):
        return Modules(self.coefficient_ring())._augmentation(self.acting_group())

    def invariants(self):
        r"""``(-)^G = Hom_{R[G]}(R, -) : Modules(R[G]) -> Modules(R)``, coextension along the augmentation."""
        return self.coextension_of_scalars(self._augmentation())

    def coinvariants(self):
        r"""``(-)_G = R tensor_{R[G]} - : Modules(R[G]) -> Modules(R)``, scalar extension along the augmentation."""
        return self.scalar_extension(self._augmentation())

    def coinvariants_trivial_adjunction(self):
        r"""``(-)_G -| Triv_G``, base change along the augmentation."""
        return self.base_change_adjunction(self._augmentation())

    # Scalar change along a ring morphism out of, or into, R[G].  Along
    # R[H] -> R[G] for a subgroup H <= G the functors are induction,
    # restriction and coinduction, realized on a transversal of G/H; along
    # any other ring morphism they are the general scalar-change functors.

    def _group_algebra_inclusion(self, supergroup):
        r"""``R[H] -> R[G]`` for the acting group ``H`` inside ``supergroup``."""
        subgroup = self.acting_group()
        inclusion = subgroup.inclusion()
        assert inclusion.codomain() is _owned_group(supergroup), f"{subgroup} was not constructed as a subgroup of {supergroup}"
        return OwnedGroups().group_algebra(self.coefficient_ring())(inclusion)

    def scalar_extension(self, ring_map):
        r"""``S tensor_{R[G]} - : Modules(R[G]) -> Modules(S)`` along ``ring_map: R[G] -> S``."""
        from dzack_research.preamble.categories.functors.group_actions import (
            CoinvariantsFunctor,
            is_augmentation_of_group_algebra,
        )
        from dzack_research.preamble.categories.functors.group_induction import (
            InductionFunctor,
            is_group_algebra_map_of_subgroup_inclusion,
        )

        assert _owned_ring(ring_map.domain()) is self.base_ring()
        match ring_map:
            case _ if is_group_algebra_map_of_subgroup_inclusion(ring_map):
                return InductionFunctor(ring_map)
            case _ if is_augmentation_of_group_algebra(ring_map):
                return CoinvariantsFunctor(ring_map)
            case _:
                return ScalarExtensionFunctor(ring_map)

    def restriction_of_scalars(self, ring_map):
        r"""``Res_f : Modules(R[G]) -> Modules(A)`` along ``ring_map: A -> R[G]``."""
        from dzack_research.preamble.categories.functors.group_induction import (
            RestrictionOfActingGroupFunctor,
            is_group_algebra_map_of_subgroup_inclusion,
        )
        from dzack_research.preamble.categories.functors.scalar_change import (
            RestrictionOfScalarsFunctor,
        )

        assert _owned_ring(ring_map.codomain()) is self.base_ring()
        match ring_map:
            case _ if is_group_algebra_map_of_subgroup_inclusion(ring_map):
                return RestrictionOfActingGroupFunctor(ring_map)
            case _:
                return RestrictionOfScalarsFunctor(ring_map)

    def coextension_of_scalars(self, ring_map):
        r"""``Hom_{R[G]}(S, -) : Modules(R[G]) -> Modules(S)`` along ``ring_map: R[G] -> S``."""
        from dzack_research.preamble.categories.functors.group_actions import (
            InvariantsFunctor,
            is_augmentation_of_group_algebra,
        )
        from dzack_research.preamble.categories.functors.group_induction import (
            CoinductionFunctor,
            is_group_algebra_map_of_subgroup_inclusion,
        )
        from dzack_research.preamble.categories.functors.scalar_change import (
            CoextensionOfScalarsFunctor,
        )

        assert _owned_ring(ring_map.domain()) is self.base_ring()
        match ring_map:
            case _ if is_group_algebra_map_of_subgroup_inclusion(ring_map):
                return CoinductionFunctor(ring_map)
            case _ if is_augmentation_of_group_algebra(ring_map):
                return InvariantsFunctor(ring_map)
            case _:
                return CoextensionOfScalarsFunctor(ring_map)

    def base_change_adjunction(self, ring_map):
        r"""``S tensor_{R[G]} - -| Res_f`` along ``ring_map: R[G] -> S``."""
        from dzack_research.preamble.categories.functors.group_actions import (
            CoinvariantsTrivialAdjunction,
            is_augmentation_of_group_algebra,
        )
        from dzack_research.preamble.categories.functors.group_induction import (
            InductionRestrictionAdjunction,
            is_group_algebra_map_of_subgroup_inclusion,
        )
        from dzack_research.preamble.categories.functors.scalar_change import (
            base_change_adjunction,
        )

        assert _owned_ring(ring_map.domain()) is self.base_ring()
        match ring_map:
            case _ if is_group_algebra_map_of_subgroup_inclusion(ring_map):
                return InductionRestrictionAdjunction(ring_map)
            case _ if is_augmentation_of_group_algebra(ring_map):
                return CoinvariantsTrivialAdjunction(ring_map)
            case _:
                return base_change_adjunction(ring_map)

    def restriction_coextension_adjunction(self, ring_map):
        r"""``Res_f -| Hom_A(R[G], -)`` along ``ring_map: A -> R[G]``."""
        from dzack_research.preamble.categories.functors.group_induction import (
            RestrictionCoinductionAdjunction,
            is_group_algebra_map_of_subgroup_inclusion,
        )
        from dzack_research.preamble.categories.functors.scalar_change import (
            restriction_coextension_adjunction,
        )

        assert _owned_ring(ring_map.codomain()) is self.base_ring()
        match ring_map:
            case _ if is_group_algebra_map_of_subgroup_inclusion(ring_map):
                return RestrictionCoinductionAdjunction(ring_map)
            case _:
                return restriction_coextension_adjunction(ring_map)

    def restriction(self, subgroup):
        r"""``Res_H^G : Modules(R[G]) -> Modules(R[H])``, restriction along ``R[H] -> R[G]``."""
        return self.restriction_of_scalars(Modules(GroupAlgebra(self.coefficient_ring(), subgroup))._group_algebra_inclusion(self.acting_group()))

    def induction(self, supergroup):
        r"""``Ind_H^G : Modules(R[H]) -> Modules(R[G])``, scalar extension along ``R[H] -> R[G]``."""
        return self.scalar_extension(self._group_algebra_inclusion(supergroup))

    def coinduction(self, supergroup):
        r"""``Coind_H^G : Modules(R[H]) -> Modules(R[G])``, coextension along ``R[H] -> R[G]``."""
        return self.coextension_of_scalars(self._group_algebra_inclusion(supergroup))

    def induction_restriction_adjunction(self, supergroup):
        r"""``Ind_H^G -| Res_H^G``."""
        return self.base_change_adjunction(self._group_algebra_inclusion(supergroup))

    def restriction_coinduction_adjunction(self, subgroup):
        r"""``Res_H^G -| Coind_H^G``."""
        return self.restriction_coextension_adjunction(Modules(GroupAlgebra(self.coefficient_ring(), subgroup))._group_algebra_inclusion(self.acting_group()))

    class ParentMethods:
        def __init__(
            self,
            acting_group,
            unacted_module,
            source_action,
            action_is_trivial=False,
            **rest,
        ) -> None:
            self._preamble_unacted_module = unacted_module
            self._preamble_source_group_action = source_action
            self._preamble_action_is_trivial = bool(action_is_trivial)

            coefficient_endomorphisms = Modules(unacted_module.base_ring()).Mor(
                unacted_module,
                unacted_module,
            )

            def coefficient_action(group_element):
                return coefficient_endomorphisms.elementwise(
                    lambda vector: _apply_action(source_action, group_element, vector),
                    verify_linearity=False,
                )

            super().__init__(
                acting_group=acting_group,
                action=coefficient_action,
                underlying_category=Modules(unacted_module.base_ring()),
                **rest,
            )

        def _group_module_placement(self):
            r"""The ``Modules(R[G])`` this object is placed in; its parameter names the group."""
            for placement in self.category().all_super_categories(proper=False):
                # Sage realizes each category instance in a dynamic subclass,
                # so the placement is recognized by its category class.
                if isinstance(placement, ModulesOverGroupAlgebra):
                    return placement
            raise AssertionError(f"{self} is not placed over a group algebra")

        def group(self):
            return self._group_module_placement().acting_group()

        def acting_group(self):
            # ``GroupLattices`` enters through refinement and supplies
            # ``group()`` itself, so the acting group is read through it.
            return self.group()

        def group_algebra(self):
            r"""``R[G]``, the ring this is a module over."""
            return self._group_module_placement().group_algebra()

        def coefficient_ring(self):
            r"""``R``, the scalar ring after forgetting the ``G``-action."""
            return self._group_module_placement().coefficient_ring()

        def underlying_category(self):
            r"""The coefficient-module category ``Modules(R)``."""
            return Modules(self.coefficient_ring())

        # The group algebra is an object of this category by its own
        # promotion, as the regular module: the action is left multiplication
        # and the module it acts on is itself.  Every other object arrived by
        # linearizing a chosen action on its retained coefficient module.

        def _is_the_regular_module(self) -> bool:
            return self is self.group_algebra()

        @cached_method
        def action(self):
            coefficient_module = self.unacted_module()
            endomorphisms = Modules(self.coefficient_ring()).Mor(
                coefficient_module,
                coefficient_module,
            )
            if self._is_the_regular_module():
                labels = coefficient_module.module_generating_set()
                return Sets().Mor(self.group(), endomorphisms)(
                    lambda group_element: endomorphisms(
                        {
                            label: coefficient_module.module_generator(group_element * label)
                            for label in labels
                        }
                    )
                )
            source_action = self._preamble_source_group_action
            return Sets().Mor(self.group(), endomorphisms)(
                lambda group_element: endomorphisms.elementwise(
                    lambda vector: _apply_action(source_action, group_element, vector),
                    verify_linearity=False,
                )
            )

        @cached_method
        def action_functor(self):
            from dzack_research.preamble.categories.functors.group_actions import (
                GroupActionFunctor,
            )

            action = self.action()
            return GroupActionFunctor(
                self.group(),
                Modules(self.coefficient_ring()),
                self.unacted_module(),
                lambda group_element: action(group_element),
            )

        @cached_method
        def action_of(self, group_element):
            r"""The coefficient-linear automorphism induced by ``group_element``."""
            if group_element not in self.group():
                raise ValueError(f"{group_element} is not an element of {self.group()}")
            return self.action()(group_element)

        def act(self, group_element, element):
            r"""Act on an ``R[G]``-module element through its coefficient restriction."""
            if self._is_the_regular_module():
                return self.action_of(group_element)(element)
            coefficient = self.forget_action_morphism()(element)
            return self.equip_action_morphism()(self.action_of(group_element)(coefficient))

        def is_trivial_action(self) -> bool:
            if self._is_the_regular_module():
                return bool(self.group().cardinality() == 1)
            return self._preamble_action_is_trivial

        def scalar_multiple(self, scalar, element):
            r"""Apply the actual ``R[G]`` scalar action."""
            if self._is_the_regular_module():
                return super().scalar_multiple(scalar, element)
            return super().scalar_multiple(scalar, element)

        def unacted_module(self):
            r"""Return the exact coefficient restriction on which ``G`` acts."""
            if self._is_the_regular_module():
                return self
            return self._preamble_unacted_module

        scalar_restriction = unacted_module

        @cached_method
        def forget_action_morphism(self):
            unacted = self.unacted_module()
            if unacted is self:
                return module_homset(self, self).identity()
            return Sets().Mor(self, unacted)(
                lambda element: unacted(self(element).underlying_element())
            )

        @cached_method
        def equip_action_morphism(self):
            unacted = self.unacted_module()
            if unacted is self:
                return module_homset(self, self).identity()
            return Sets().Mor(unacted, self)(
                lambda element: self(unacted._underlying_additive_element(unacted(element)))
            )

        # The selected R-framing belongs to the scalar restriction.  These
        # accessors intentionally expose that retained presentation without
        # asserting that it is an R[G]-basis.

        def module_generating_set(self):
            if self._is_the_regular_module():
                return super().module_generating_set()
            return self.unacted_module().module_generating_set()

        def module_generator(self, label):
            if self._is_the_regular_module():
                return super().module_generator(label)
            return self.equip_action_morphism()(self.unacted_module().module_generator(label))

        @cached_method
        def module_generators(self):
            return finite_indexed_family(
                self.module_generating_set(),
                self.module_generator,
                name=f"Coefficient-module generators of {self}",
            )

        def linear_combination(self, coefficients, factor_on_left=True):
            if self._is_the_regular_module():
                return super().linear_combination(
                    coefficients,
                    factor_on_left=factor_on_left,
                )
            return self.equip_action_morphism()(
                self.unacted_module().linear_combination(
                    coefficients,
                    factor_on_left=factor_on_left,
                )
            )

        def _selected_module_coefficients(self, element):
            if self._is_the_regular_module():
                return super()._selected_module_coefficients(element)
            return module_coefficients(
                self.forget_action_morphism()(element),
                self.unacted_module(),
            )

        def _selected_presentation_rows(self):
            if self._is_the_regular_module():
                return super()._selected_presentation_rows()
            return self.unacted_module()._selected_presentation_rows()

        def coefficient_module_rank(self):
            return self.unacted_module().module_rank()

        def module_rank(self):
            r"""Return the rank of the retained coefficient-module presentation.

            This is the representation rank over ``R``.  It is not a claim
            that the module is free of this rank over ``R[G]``.
            """
            return self.coefficient_module_rank()

        def invariant_factors(self):
            r"""Invariant factors of the retained coefficient module."""
            return self.unacted_module().invariant_factors()

        def Mor(self, codomain, category=None):
            r"""``Mor_{R[G]}(M,N)``, the equivariant maps.

            The underlying coefficient-linear Hom is
            ``Hom_R(M.scalar_restriction(), N.scalar_restriction())`` and is
            exposed by the resulting Hom object's :meth:`underlying_homset`.
            """
            if category is None or category.is_subcategory(Modules(self.group_algebra())):
                return group_module_homset(self, codomain)
            return super().Mor(codomain, category)

        def End(self):
            r"""``End_{R[G]}(M)``, the equivariant endomorphism object.

            The underlying ``R``-linear endomorphisms are
            ``Modules(R).End(M.scalar_restriction())``.  A group module's
            default Hom is already equivariant, so its default End uses the
            same owner.
            """
            return Modules(self.group_algebra()).End(self)

        def Aut(self):
            r"""``Aut_{R[G]}(M)``, the equivariant module automorphisms.

            Use ``Modules(R).Aut(M.scalar_restriction())`` explicitly when the
            action is to be forgotten and all underlying ``R``-linear
            automorphisms are wanted.
            """
            return Modules(self.group_algebra()).Aut(self)

        def _Hom_(self, codomain, category=None):
            if codomain not in Modules(self.group_algebra()):
                raise TypeError("an R[G]-module morphism requires the same acting group")
            return group_module_homset(self, codomain)

        def _finite_action_endomorphism_family(self):
            r"""Return ``{id_M} union {rho(s) : s in S}`` for a chosen finite ``S``.

            Choosing a finite group generating set is a represented backend for
            the wide equalizer/coequalizer of the full action; callers retain
            the universal-construction spelling.
            """
            group = self.group()
            if group.is_finitely_generated() is not True:
                raise NotImplementedError("the represented action equalizer/coequalizer requires a chosen finite group generating set")
            generators = group.group_generators()
            indices = CoproductOfFamily(
                Sets.Δ[1],
                lambda side: Sets.Δ[0] if int(side) == 0 else generators,
            )
            coefficient_module = self.unacted_module()
            identity = module_homset(coefficient_module, coefficient_module).identity()
            return finite_indexed_family(
                indices,
                lambda tagged: identity if int(tagged.summand_index()) == 0 else self.action_of(tagged.summand_element()),
                name=f"Identity and chosen action generators on {self}",
            )

        def module_invariants(self):
            r"""``M^G = Hom_{R[G]}(R, M)``, the wide equalizer of the action and the identity."""
            if self.is_trivial_action():
                return self.unacted_module()
            return EqualizerOfFamily(self._finite_action_endomorphism_family())

        def module_coinvariants(self):
            r"""``M_G = R tensor_{R[G]} M``, the wide coequalizer of the action and the identity."""
            if self.is_trivial_action():
                return self.unacted_module()
            return CoequalizerOfFamily(self._finite_action_endomorphism_family())

        @cached_method
        def equivariant_endomorphism_module(self):
            r"""``End_{R[G]}(M) = Hom_R(M, M)^G``: the invariants of conjugation.

            ``G`` acts on ``Hom_R(M, M)`` by ``g . f = rho(g) f rho(g)^{-1}``,
            and the equivariant endomorphisms are its fixed points.
            """
            from dzack_research.preamble.categories.modules.internal_hom import InternalHom

            coefficient_module = self.unacted_module()
            endomorphisms = InternalHom(coefficient_module, coefficient_module)

            def conjugation(group_element, endomorphism):
                return self.action_of(group_element) * endomorphism * self.action_of(group_element.inverse())

            return _equip_action(endomorphisms, self.group(), conjugation).module_invariants()

        def isotypic_characters(self):
            r"""The characters of the isotypic components present in this module.

            Over the coefficient ring the index is the set of irreducible
            characters, or their rational Galois orbits over ``ZZ`` and
            ``QQ``; a character is present when its isotypic component is
            nonzero.
            """
            from dzack_research.preamble.categories.sets.finite_ordered_sets import (
                finite_ordered_set,
            )

            return finite_ordered_set(tuple(character for character in _split_irreducible_characters(self) if isotypic_component(self, character).module_rank() != 0))

        def isotypic_component(self, character):
            r"""Return the integral/base-ring isotypic component as a subobject."""

            return isotypic_component(self, character)

        def isotypic_decomposition(self):
            r"""Return the sum of isotypic components together with its inclusion in ``M``."""

            return isotypic_decomposition(self)

        def restrict_action_to(self, inclusion):
            r"""Return the subobject ``S`` of ``M`` in ``Modules(R[G])``, as its inclusion.

            A submodule whose image is stable under the action carries exactly
            one action making the inclusion equivariant, namely
            ``s . x = i^{-1}(rho(s) i(x))``, so the ``G``-module structure is
            not a choice.  A subobject of ``M`` in ``Modules(R[G])`` is the
            pair of that module and its inclusion, and that pair is what this
            returns: the equivariant monomorphism ``S -> M``.

            The invariants and each isotypic component are stable, the latter
            because the central idempotent cutting it out commutes with the
            action, so this is how the action of ``G`` and of any equivariant
            automorphism reaches those pieces.  Stability is not assumed: the
            lift back along ``inclusion`` fails on a generator whose image
            leaves the submodule.
            """
            submodule = inclusion.domain()
            coefficient_module = self.unacted_module()
            assert inclusion.codomain() is coefficient_module, (
                f"{inclusion} is not a subobject inclusion into {coefficient_module}"
            )

            def restricted_action(group_element, vector):
                return inclusion.lift(self.action_of(group_element)(inclusion(vector)))

            acted = _equip_action(submodule, self.group(), restricted_action)
            equivariant_inclusion = group_module_homset(acted, self)(
                lambda label: self.equip_action_morphism()(
                    inclusion(submodule.module_generator(label))
                )
            )
            # The original subobject inclusion owns the exact lift.  Preserve
            # that lift on the equivariant reading so every later restriction
            # uses the same represented subobject rather than solving a second
            # coordinate problem.
            equivariant_inclusion._preamble_lift = (
                lambda element: acted.equip_action_morphism()(
                    inclusion.lift(self.forget_action_morphism()(element))
                )
            )
            return equivariant_inclusion

        def restrict_endomorphism_to(self, endomorphism, inclusion):
            r"""Restrict an equivariant endomorphism of ``M`` to a stable subobject.

            ``inclusion`` is the ordinary represented subobject inclusion
            ``S -> M``.  The action is first restricted to ``S`` through
            :meth:`restrict_action_to`; the endomorphism is then forced through
            ``Mor_{R[G]}(M,M)``, which is exactly the condition that it commute
            with the action.  Stability of ``S`` under the endomorphism is not
            assumed: the exact lift through the inclusion decides it.
            """
            if inclusion.codomain() is not self.unacted_module():
                raise ValueError("the stable subobject inclusion must land in the coefficient restriction")
            equivariant = group_module_homset(self, self)(endomorphism)
            acted_inclusion = self.restrict_action_to(inclusion)
            return equivariant.restrict_to(acted_inclusion)

        def restrict_automorphism_to(self, automorphism, inclusion):
            r"""Restrict an equivariant automorphism to a stable subobject.

            The result is an actual element of ``Aut_{R[G]}(S)``.  Both the
            forward and inverse ambient maps are checked in the equivariant Hom
            before restriction, and the same acted subobject is used for both
            directions; hence the returned pair is the restricted isomorphism,
            not merely an invertible-looking ``R``-linear map.
            """
            if automorphism.domain() is not self or automorphism.codomain() is not self:
                raise ValueError("the automorphism must be an endomorphism of this group module")
            if inclusion.codomain() is not self.unacted_module():
                raise ValueError("the stable subobject inclusion must land in the coefficient restriction")

            from dzack_research.preamble.categories.abstract_categories.hom_categories import (
                CategoricalIsomorphism,
            )

            acted_inclusion = self.restrict_action_to(inclusion)
            forward = group_module_homset(self, self)(automorphism.forward()).restrict_to(
                acted_inclusion
            )
            inverse = group_module_homset(self, self)(automorphism.inverse()).restrict_to(
                acted_inclusion
            )
            piece = acted_inclusion.domain()
            return Modules(self.group_algebra()).Aut(piece)(
                CategoricalIsomorphism(
                    forward.parent(),
                    forward,
                    inverse,
                    verify=False,
                )
            )

        def character(self):
            r"""Return the ordinary trace character in characteristic zero."""
            group = self.group()
            coefficient_module = self.unacted_module()
            coefficient_ring = self.coefficient_ring()
            if group.is_finite() is not True:
                raise NotImplementedError("ordinary character tables here require a finite group")
            if coefficient_module not in FinitelyGeneratedFreeModules(coefficient_ring):
                raise NotImplementedError(
                    "the ordinary character is implemented here for a finite free group module; "
                    "a finite presentation alone does not supply the finite-dimensional linear "
                    "representation used by this construction"
                )
            if coefficient_ring.characteristic() != 0:
                raise TypeError(
                    "ordinary characters are not obtained by treating modular traces as "
                    "characteristic-zero class functions; use the native Brauer-character "
                    "machinery when appropriate"
                )
            representatives = group.conjugacy_classes_representatives()
            traces = tuple(self.action_of(group_element).trace() for group_element in representatives)

            return finite_group_class_function(
                group,
                coefficient_ring,
                traces,
                representatives=representatives,
            )

        def brauer_character(self):
            r"""Return the Brauer character of a finite-dimensional modular representation."""
            group = self.group()
            coefficient_module = self.unacted_module()
            coefficient_ring = self.coefficient_ring()
            if group.is_finite() is not True:
                raise NotImplementedError("Brauer characters here require a finite group")
            if coefficient_module not in FinitelyGeneratedFreeModules(coefficient_ring):
                raise NotImplementedError("the Brauer character is defined here for a finite free group module")
            if coefficient_ring.characteristic() == 0:
                raise TypeError("Brauer characters are the positive-characteristic representation invariant")
            if not coefficient_ring.is_field():
                raise TypeError("Brauer characters require a finite-dimensional representation over a field of positive characteristic")

            from sage.combinat.free_module import CombinatorialFreeModule

            indices = tuple(range(int(coefficient_module.module_rank())))
            computation_module = CombinatorialFreeModule(
                _engine_ring(coefficient_ring),
                indices,
            )
            basis = computation_module.basis()

            def on_basis(group_element, index):
                action_matrix = self.action_of(group_element).matrix()
                return computation_module.sum(
                    _engine_element(
                        coefficient_ring,
                        action_matrix[image_index, index],
                    )
                    * basis[image_index]
                    for image_index in indices
                )

            # Sage maintains the Teichmuller-lift computation on a private
            # finite-basis representation.  Only the resulting exact values
            # cross back into the owned class-function object.

            engine_group = _engine_group(group)

            def engine_on_basis(engine_group_element, index):
                return on_basis(group._from_engine(engine_group_element), index)

            backend_character = engine_group.representation(
                computation_module,
                engine_on_basis,
                side="left",
            ).brauer_character()
            backend_values = tuple(backend_character)
            if not backend_values:
                raise ArithmeticError("a finite group has at least the identity p-regular class")
            value_ring = _own_ring(backend_values[0].parent())
            engine_value_ring = _engine_ring(value_ring)
            values = tuple(value_ring._from_engine_element(engine_value_ring(value)) for value in backend_values)
            characteristic = int(coefficient_ring.characteristic())
            representatives = tuple(representative for representative in group.conjugacy_classes_representatives() if int(representative.order()) % characteristic)
            if len(representatives) != len(values):
                raise ArithmeticError("the private Brauer-character engine returned the wrong number of p-regular class values")
            return finite_group_class_function(
                group,
                value_ring,
                values,
                representatives=representatives,
            )

        def base_change(self, ring_map):
            r"""Transport this group module along ``R -> S`` functorially."""

            unacted = self.unacted_module()
            scalar_extension = ScalarExtensionFunctor(ring_map)
            changed_module = scalar_extension(unacted)
            if self.is_trivial_action():
                return _trivial_action(changed_module, self.group())

            def changed_action(group_element, vector):
                return scalar_extension(self.action_of(group_element))(vector)

            return _equip_action(changed_module, self.group(), changed_action)


def _apply_action(action, group_element, vector):
    if isinstance(action, Map):
        return action(group_element)(vector)
    return action(group_element, vector)


def _coefficient_morphism_from_images(
    parent,
    images,
    *,
    elementwise=False,
    verify_linearity=True,
):
    r"""Read equivariant-map data as a map of the retained coefficient modules."""
    source = parent.domain().unacted_module()
    target = parent.codomain().unacted_module()
    homset = module_homset(source, target)

    if isinstance(images, GroupModuleMorphism):
        underlying = images.underlying_module_morphism()
        if underlying.domain() is source and underlying.codomain() is target:
            return homset(underlying)

    if isinstance(images, ModuleMorphism):
        if images.domain() is source and images.codomain() is target:
            return homset(images)
        if images.domain() is parent.domain() and images.codomain() is parent.codomain():
            return homset.elementwise(
                lambda element: parent.codomain().forget_action_morphism()(
                    images(parent.domain().equip_action_morphism()(element))
                ),
                verify_linearity=False,
            )

    def coefficient_value(value):
        try:
            acted = parent.codomain()(value)
        except (TypeError, ValueError):
            return target(value)
        return parent.codomain().forget_action_morphism()(acted)

    if elementwise:
        if not callable(images):
            raise TypeError("an elementwise equivariant map must be callable")
        return homset.elementwise(
            lambda element: coefficient_value(
                images(parent.domain().equip_action_morphism()(element))
            ),
            verify_linearity=verify_linearity,
        )

    if isinstance(images, dict):
        return homset({label: coefficient_value(value) for label, value in images.items()})
    if isinstance(images, (tuple, list)):
        return homset(tuple(coefficient_value(value) for value in images))
    if callable(images):
        return homset(lambda label: coefficient_value(images(label)))
    return homset(images)


class GroupModuleMorphism(ModuleMorphism):
    r"""An ``R``-linear map commuting with the chosen ``G``-actions."""

    def __init__(
        self,
        parent,
        images,
        *,
        elementwise=False,
        verify_linearity=True,
        verify_equivariance=True,
    ) -> None:
        underlying = _coefficient_morphism_from_images(
            parent,
            images,
            elementwise=elementwise,
            verify_linearity=verify_linearity,
        )
        self._preamble_underlying_module_morphism = underlying
        super().__init__(
            parent,
            lambda element: parent.codomain().equip_action_morphism()(
                underlying(parent.domain().forget_action_morphism()(element))
            ),
            elementwise=True,
            verify_linearity=False,
        )
        if verify_equivariance and parent.is_equivariant(self) is not True:
            raise ValueError("the stated module map is not G-equivariant")

    def underlying_module_morphism(self):
        r"""The same map in ``Hom_R(Res M, Res N)``."""
        return self._preamble_underlying_module_morphism

    underlying_arrow = underlying_module_morphism

    def _richcmp_(self, other, op):
        if op not in (op_EQ, op_NE):
            return NotImplemented
        if not isinstance(other, GroupModuleMorphism):
            return op == op_NE
        if other.parent() is not self.parent():
            return op == op_NE
        equal = self.underlying_module_morphism() == other.underlying_module_morphism()
        return equal if op == op_EQ else not equal

    def matrix(self):
        r"""The matrix of the underlying coefficient-linear map."""
        return self.underlying_module_morphism().matrix()

    def __mul__(self, other):
        if not isinstance(other, GroupModuleMorphism):
            return super().__mul__(other)
        if other.codomain() is not self.domain():
            return NotImplemented
        return group_module_homset(other.domain(), self.codomain())._from_equivariant_images(
            lambda element: self(other(element)),
            elementwise=True,
            verify_linearity=False,
        )

    def natural_transformation(self):
        r"""Return this equivariant map as the corresponding transformation ``BG => C``."""
        source = self.domain().action_functor()
        target = self.codomain().action_functor()
        component = self.underlying_module_morphism()
        return NaturalTransformation(source, target, lambda _obj: component)

    def restrict_to(self, inclusion):
        r"""Restrict this equivariant endomorphism along an equivariant inclusion.

        If ``i:S -> M`` is equivariant and ``f:M -> M`` preserves ``i(S)``, the
        restriction is the unique ``f_S`` satisfying ``i f_S = f i``.  The
        inclusion's represented lift constructs that unique map.
        """
        ambient = self.domain()
        if self.codomain() is not ambient:
            raise ValueError("restriction to a stable subobject is defined here for an endomorphism")
        if inclusion.codomain() is not ambient:
            raise ValueError("the equivariant inclusion must land in the endomorphism domain")
        piece = inclusion.domain()
        if piece not in Modules(ambient.group_algebra()):
            raise TypeError("the restricted subobject must carry the same group-module structure")

        return group_module_homset(piece, piece)._from_equivariant_images(
            lambda element: inclusion.lift(self(inclusion(element))),
            elementwise=True,
            verify_linearity=False,
        )

    def inverse(self):
        r"""The inverse of an equivariant isomorphism, still equivariant."""
        ordinary_inverse = self.underlying_module_morphism().inverse()
        return group_module_homset(self.codomain(), self.domain())._from_equivariant_images(
            ordinary_inverse,
            verify_linearity=False,
        )

    def as_automorphism(self):
        r"""Return this invertible equivariant endomorphism in ``Aut_{R[G]}(M)``."""
        from dzack_research.preamble.categories.abstract_categories.hom_categories import (
            CategoricalIsomorphism,
        )

        module = self.domain()
        if self.codomain() is not module:
            raise ValueError("an automorphism is an endomorphism")
        inverse = self.inverse()
        return Modules(module.group_algebra()).Aut(module)(
            CategoricalIsomorphism(
                self.parent(),
                self,
                inverse,
                verify=False,
            )
        )


class GroupModuleHomset(_ModuleHomsetCommonMethods, GObjectHomset):
    Element = GroupModuleMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        assert domain.group() == codomain.group(), "R[G]-module morphisms require the same acting group"
        coefficient_ring = domain.coefficient_ring()
        if codomain.coefficient_ring() is not coefficient_ring:
            raise ValueError("equivariant maps require one coefficient ring")
        scalar_ring = (
            coefficient_ring
            if coefficient_ring in OwnedRings().Commutative()
            else _own_ring(SageZZ)
        )
        self._preamble_base_ring = scalar_ring
        self._preamble_algebra_base_ring = scalar_ring
        CategoricalHomset.__init__(
            self,
            hom_family,
            domain,
            codomain,
            category=LinearHomModules(scalar_ring),
        )

    def underlying_homset(self):
        r"""``Hom_R(Res M, Res N)``, containing the equivariant maps."""
        return module_homset(
            self.domain().unacted_module(),
            self.codomain().unacted_module(),
        )

    def is_equivariant(self, arrow):
        group = self.domain().group()
        if group.is_finitely_generated() is not True:
            from sage.misc.unknown import Unknown

            return Unknown
        underlying = _coefficient_morphism_from_images(
            self,
            arrow,
            elementwise=False,
            verify_linearity=False,
        )
        return all(
            underlying * self.domain().action_of(generator)
            == self.codomain().action_of(generator) * underlying
            for generator in group.group_generators()
        )

    def _element_constructor_(self, images):
        if isinstance(images, GroupModuleMorphism) and images.parent() is self:
            return images
        return self.element_class(self, images)

    def _from_equivariant_images(
        self,
        images,
        *,
        elementwise=False,
        verify_linearity=True,
    ):
        r"""Construct a map whose equivariance follows from its construction.

        This protected path is for functorial images, identities, and
        compositions.  Arbitrary user-supplied maps still use the ordinary
        constructor and are checked on the selected group/module generators.
        """
        return self.element_class(
            self,
            images,
            elementwise=elementwise,
            verify_linearity=verify_linearity,
            verify_equivariance=False,
        )

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to an endomorphism Hom-set")
        return self._from_equivariant_images(
            lambda element: element,
            elementwise=True,
            verify_linearity=False,
        )

    def _repr_(self):
        return f"Mor_{self.domain().group()}({self.domain()}, {self.codomain()})"


def group_module_homset(domain, codomain) -> GroupModuleHomset:
    group_algebra = domain.group_algebra()
    group = domain.group()
    if codomain.group_algebra() is not group_algebra or codomain.group() != group:
        raise ValueError("R[G]-module morphisms require one group algebra and acting group")
    return Modules(group_algebra).Mor(domain, codomain)


def _equip_action(module, group_or_action, action=None, *, _action_is_trivial=False):
    r"""Linearize a left ``G``-action to an actual ``R[G]``-module.

    The carrier is constructed by the generic module action
    ``R[G] -> End_Ab(U_R(M))``.  The original ``R``-module ``M`` is retained
    literally as the scalar restriction, including its selected presentation.
    ``action`` may be an actual ``BG -> Modules(R)`` functor, a ring morphism
    out of ``R[G]``, or the binary action ``action(g,m)``.
    """

    base_ring = module.base_ring()
    if module not in FinitelyPresentedModules(base_ring):
        raise NotImplementedError("equipping an action requires a represented finite presentation")
    ring_action = None
    if action is None:
        action = group_or_action
        if isinstance(action, Functor):
            classifying = action.domain()
            if action.codomain() != Modules(base_ring):
                raise ValueError("a module action functor must land in Modules(R)")
            group = _owned_group(classifying.group())
            if action(classifying.an_object()) is not module:
                raise ValueError("the action functor must select the module being equipped")
            arrows = classifying.Mor(classifying.an_object(), classifying.an_object())
            functor_action = action

            def action(group_element, vector):
                return functor_action(arrows(group_element))(vector)

        elif not isinstance(action, Map):
            raise TypeError("with two arguments, an action functor or morphism with the acting group as domain is expected")
        else:
            match action.domain():
                case group_algebra if group_algebra in GroupAlgebras(base_ring):
                    # ``rho: R[G] -> End_R(M)`` restricted along ``G -> R[G]``.
                    group = group_algebra.group()
                    ring_action = action

                    def action(group_element, vector):
                        return ring_action(group_algebra.module_generator(group_element))(vector)
                case acting_group:
                    group = _owned_group(acting_group)
    else:
        group = _owned_group(group_or_action)

    labels = module.module_generating_set()
    if not labels.cardinality().is_finite():
        raise NotImplementedError("equipping an action currently materializes a finite framing")

    is_free = module in FinitelyGeneratedFreeModules(base_ring)
    if not is_free and module not in ModulesWithChosenFinitePresentation(base_ring):
        raise TypeError("a nonfree group module requires a chosen finite presentation")

    group_algebra = GroupAlgebra(base_ring, group)
    additive_group = module.underlying_additive_group()
    additive_endomorphisms = AdditiveGroups().AdditiveCommutative().End(additive_group)

    def module_element(additive_element):
        return module(additive_element)

    def additive_element(module_element_value):
        return module._underlying_additive_element(module(module_element_value))

    def linearized_scalar(scalar):
        coefficients = module_coefficients(group_algebra(scalar), group_algebra)

        def apply(additive_vector):
            vector = module_element(additive_vector)
            result = module.zero()
            for group_element, coefficient in coefficients.items():
                result += module.scalar_multiple(
                    coefficient,
                    _apply_action(action, group_element, vector),
                )
            return additive_element(result)

        return additive_endomorphisms.elementwise(apply)

    scalar_action = (
        ring_action
        if (
            ring_action is not None
            and ring_action.domain() is group_algebra
            and ring_action.codomain() is additive_endomorphisms
        )
        else ring_morphism(
            group_algebra,
            additive_endomorphisms,
            linearized_scalar,
        )
    )
    return object_of(
        GeneralModules(group_algebra),
        base_ring=group_algebra,
        rho=scalar_action,
        acting_group=group,
        unacted_module=module,
        source_action=action,
        action_is_trivial=_action_is_trivial,
    )


def _trivial_action(module, group):
    r"""Equip ``module`` with the trivial action of ``group``."""
    return _equip_action(
        module,
        group,
        lambda _group_element, vector: vector,
        _action_is_trivial=True,
    )


__all__ = [
    "GroupModuleHomset",
    "GroupModuleMorphism",
    "ModulesOverGroupAlgebra",
    "group_module_homset",
]
