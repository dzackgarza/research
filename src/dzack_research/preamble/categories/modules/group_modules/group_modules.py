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

from dzack_research.preamble.categories.abstract_categories.constructions import (
    CoequalizerOfFamily,
    EqualizerOfFamily,
)
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.algebras.group_algebras import (
    GroupAlgebra,
    GroupAlgebras,
)
from dzack_research.preamble.categories.functors.scalar_change import (
    ScalarExtensionFunctor,
)
from dzack_research.preamble.categories.group.class_functions import (
    finite_group_class_function,
)
from dzack_research.preamble.categories.group.g_objects import GObjectHomset, GObjects
from dzack_research.preamble.categories.group.groups import (
    OwnedGroups,
    _engine_group,
    _owned_group,
)
from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
    FinitelyPresentedModule,
)
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    FreshFreeModuleOn,
)
from dzack_research.preamble.categories.modules.group_modules.isotypic import (
    _split_irreducible_characters,
    isotypic_component,
    isotypic_decomposition,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
    _initialize_module_hom_parent,
    _ModuleHomsetCommonMethods,
    module_homset,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    FinitelyGeneratedFreeModules,
    FinitelyPresentedModules,
    LinearEndCategoryConstruction,
    Modules,
    ModulesWithChosenFinitePresentation,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _engine_element,
    _engine_ring,
    _own_ring,
    _owned_ring,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    finite_indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import (
    CoproductOfFamily,
    Sets,
)


class GroupModuleHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return GroupModuleHomset


class ModulesOverGroupAlgebra(OwnedCategoryOverBaseRing):
    r"""``Modules(R[G])``: the modules over a group algebra.

    ``Modules(S)`` constructs this category whenever ``S`` is a group
    algebra, so the spelling is ``Modules(R[G])``.  Its objects are the
    ``R``-modules with a chosen left ``G``-action, its morphisms the
    ``R``-linear equivariant maps.
    """

    def group_algebra(self):
        return self.base_ring()

    def coefficient_ring(self):
        r"""``R``, the scalars of the group algebra ``R[G]``."""
        return self.base_ring().base_ring()

    def acting_group(self):
        return self.base_ring().group()

    def _repr_object_names(self):
        return f"modules over {self.base_ring()}"

    def super_categories(self):
        ring = self.coefficient_ring()
        return [
            GObjects(self.acting_group(), Modules(ring)),
            Modules(ring),
        ]

    _HomCategory = GroupModuleHomCategoryConstruction
    _EndCategory = LinearEndCategoryConstruction

    def an_object(self):
        r"""The trivial action on the free module of rank one."""
        ring = self.coefficient_ring()
        return Modules(ring).trivial_action(self.acting_group())(Modules(ring).an_object())

    def _call_(self, module, action):
        r"""Equip an ``R``-module with a left ``G``-action, ``action(g, m)``."""
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
        assert inclusion.codomain() is _owned_group(supergroup), (
            f"{subgroup} was not constructed as a subgroup of {supergroup}"
        )
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
        return self.restriction_of_scalars(
            Modules(GroupAlgebra(self.coefficient_ring(), subgroup))._group_algebra_inclusion(
                self.acting_group()
            )
        )

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
        return self.restriction_coextension_adjunction(
            Modules(GroupAlgebra(self.coefficient_ring(), subgroup))._group_algebra_inclusion(
                self.acting_group()
            )
        )

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
            self._preamble_action_is_trivial = bool(action_is_trivial)

            def generator_images(group_element):
                forget_action = self.forget_action_morphism()
                equip_action = self.equip_action_morphism()
                return {
                    label: equip_action(
                        _apply_action(
                            source_action,
                            group_element,
                            forget_action(self.module_generator(label)),
                        )
                    )
                    for label in self.module_generating_set()
                }

            super().__init__(
                acting_group=acting_group,
                action=generator_images,
                underlying_category=Modules(unacted_module.base_ring()),
                **rest,
            )

        def group(self):
            return self._preamble_acting_group

        def acting_group(self):
            # ``GroupLattices`` enters through refinement and supplies
            # ``group()`` itself, so the acting group is read through it.
            return self.group()

        def group_algebra(self):
            r"""``R[G]``, the ring this is a module over."""
            return GroupAlgebra(self.base_ring(), self.group())

        def is_trivial_action(self) -> bool:
            return self._preamble_action_is_trivial

        def unacted_module(self):
            r"""Return the module from which this chosen action was equipped."""
            return self._preamble_unacted_module

        @cached_method
        def forget_action_morphism(self):
            unacted = self.unacted_module()
            return module_homset(self, unacted)(
                {
                    label: unacted.module_generator(label)
                    for label in self.module_generating_set()
                }
            )

        @cached_method
        def equip_action_morphism(self):
            unacted = self.unacted_module()
            return module_homset(unacted, self)(
                {
                    label: self.module_generator(label)
                    for label in self.module_generating_set()
                }
            )

        def Mor(self, codomain, category=None):
            r"""``Mor_{R[G]}(M, N)``, the equivariant maps; ``Modules(R)`` names the linear ones."""
            if category is None or category.is_subcategory(Modules(self.group_algebra())):
                return group_module_homset(self, codomain)
            return super().Mor(codomain, category)

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
                raise NotImplementedError(
                    "the represented action equalizer/coequalizer requires a chosen finite group generating set"
                )
            generators = group.group_generators()
            indices = CoproductOfFamily(
                Sets.Δ[1],
                lambda side: Sets.Δ[0] if int(side) == 0 else generators,
            )
            identity = module_homset(self, self).identity()
            return finite_indexed_family(
                indices,
                lambda tagged: (
                    identity
                    if int(tagged.summand_index()) == 0
                    else self.action_of(tagged.summand_element())
                ),
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

            endomorphisms = InternalHom(self, self)

            def conjugation(group_element, endomorphism):
                return (
                    self.action_of(group_element)
                    * endomorphism
                    * self.action_of(group_element.inverse())
                )

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

            return finite_ordered_set(
                tuple(
                    character
                    for character in _split_irreducible_characters(self)
                    if isotypic_component(self, character).rank() != 0
                )
            )

        def isotypic_component(self, character):
            r"""Return the integral/base-ring isotypic component as a subobject."""

            return isotypic_component(self, character)

        def isotypic_decomposition(self):
            r"""Return the sum of isotypic components together with its inclusion in ``M``."""

            return isotypic_decomposition(self)

        def character(self):
            r"""Return the ordinary trace character in characteristic zero."""
            group = self.group()
            if group.is_finite() is not True:
                raise NotImplementedError("ordinary character tables here require a finite group")
            if self not in FinitelyGeneratedFreeModules(self.base_ring()):
                raise NotImplementedError(
                    "the ordinary character is implemented here for a finite free group module; a finite presentation alone does not supply the finite-dimensional linear representation used by this construction"
                )
            if self.base_ring().characteristic() != 0:
                raise TypeError(
                    "ordinary characters are not obtained by treating modular traces as characteristic-zero class functions; use the native Brauer-character machinery when appropriate"
                )
            representatives = group.conjugacy_classes_representatives()
            traces = tuple(
                self.action_of(group_element).trace()
                for group_element in representatives
            )

            return finite_group_class_function(
                group,
                self.base_ring(),
                traces,
                representatives=representatives,
            )

        def brauer_character(self):
            r"""Return the Brauer character of a finite-dimensional modular representation."""
            group = self.group()
            if group.is_finite() is not True:
                raise NotImplementedError("Brauer characters here require a finite group")
            if self not in FinitelyGeneratedFreeModules(self.base_ring()):
                raise NotImplementedError(
                    "the Brauer character is defined here for a finite free group module"
                )
            if self.base_ring().characteristic() == 0:
                raise TypeError("Brauer characters are the positive-characteristic representation invariant")
            if not self.base_ring().is_field():
                raise TypeError(
                    "Brauer characters require a finite-dimensional representation over a field of positive characteristic"
                )

            from sage.combinat.free_module import CombinatorialFreeModule

            indices = tuple(range(int(self.rank())))
            computation_module = CombinatorialFreeModule(
                _engine_ring(self.base_ring()),
                indices,
            )
            basis = computation_module.basis()

            def on_basis(group_element, index):
                action_matrix = self.action_of(group_element).matrix()
                return computation_module.sum(
                    _engine_element(
                        self.base_ring(),
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
            values = tuple(
                value_ring._from_engine_element(engine_value_ring(value))
                for value in backend_values
            )
            characteristic = int(self.base_ring().characteristic())
            representatives = tuple(
                representative
                for representative in group.conjugacy_classes_representatives()
                if int(representative.order()) % characteristic
            )
            if len(representatives) != len(values):
                raise ArithmeticError(
                    "the private Brauer-character engine returned the wrong number of p-regular class values"
                )
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
                underlying_action = (
                    self.forget_action_morphism()
                    * self.action_of(group_element)
                    * self.equip_action_morphism()
                )
                return scalar_extension(underlying_action)(vector)

            return _equip_action(changed_module, self.group(), changed_action)


def _apply_action(action, group_element, vector):
    if isinstance(action, Map):
        return action(group_element)(vector)
    return action(group_element, vector)


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
        super().__init__(
            parent,
            images,
            elementwise=elementwise,
            verify_linearity=verify_linearity,
        )
        if verify_equivariance and parent.is_equivariant(self) is not True:
            raise ValueError("the stated module map is not G-equivariant")

    def __mul__(self, other):
        if not isinstance(other, GroupModuleMorphism):
            return super().__mul__(other)
        if other.codomain() is not self.domain():
            return NotImplemented
        return group_module_homset(
            other.domain(), self.codomain()
        )._from_equivariant_images(
            lambda element: self(other(element)),
            elementwise=True,
            verify_linearity=False,
        )


class GroupModuleHomset(_ModuleHomsetCommonMethods, GObjectHomset):
    Element = GroupModuleMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        assert domain.group() == codomain.group(), (
            "R[G]-module morphisms require the same acting group"
        )
        _initialize_module_hom_parent(self, hom_family, domain, codomain)


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
    ring = domain.base_ring()
    group = domain.group()
    if codomain.base_ring() is not ring or codomain.group() != group:
        raise ValueError("R[G]-module morphisms require one coefficient ring and acting group")
    return Modules(GroupAlgebra(ring, group)).Mor(domain, codomain)


def _equip_action(module, group_or_action, action=None, *, _action_is_trivial=False):
    r"""Equip a finitely presented ``R``-module with a left ``G``-action.

    The result is an object of ``Modules(R[G])``, and of ``Modules(ZZ[G])``
    by restriction along ``ZZ[G] -> R[G]``.  ``action`` is either a morphism
    ``rho`` with domain the acting group, or the binary ``action(g, m)``.
    The selected module labels are transported unchanged.
    """

    base_ring = module.base_ring()
    if module not in FinitelyPresentedModules(base_ring):
        raise NotImplementedError(
            "equipping an action requires a represented finite presentation"
        )
    if action is None:
        action = group_or_action
        if not isinstance(action, Map):
            raise TypeError(
                "with two arguments, an action morphism whose domain is the acting group is expected"
            )
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
        raise NotImplementedError(
            "equipping an action currently materializes a finite framing"
        )

    is_free = module in FinitelyGeneratedFreeModules(base_ring)
    if not is_free and module not in ModulesWithChosenFinitePresentation(base_ring):
        raise TypeError(
            "a nonfree group module requires a chosen finite presentation"
        )

    from dzack_research.preamble.catalogue import ZZ as integers

    categories = [Modules(GroupAlgebra(base_ring, group))]
    if base_ring is not integers:
        categories.append(Modules(GroupAlgebra(integers, group)))
    construction_data = {
        "acting_group": group,
        "unacted_module": module,
        "source_action": action,
        "action_is_trivial": _action_is_trivial,
    }
    if is_free:
        return FreshFreeModuleOn(
            base_ring,
            labels,
            _extra_categories=tuple(categories),
            _extra_construction_data=construction_data,
        )
    return FinitelyPresentedModule(
        module.presentation(),
        _extra_categories=tuple(categories),
        _extra_construction_data=construction_data,
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
