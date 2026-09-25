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
from sage.misc.unknown import Unknown
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.richcmp import op_EQ, op_NE

from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    MorCategoryConstruction,
)
from dzack_research.preamble.categories.algebras.group_algebras import (
    GroupAlgebras,
)
from dzack_research.preamble.categories.functors.core import (
    Adjunction,
    Functor,
    NaturalTransformation,
)
from dzack_research.preamble.categories.functors.scalar_change import (
    _ScalarExtensionFunctor,
)
from dzack_research.preamble.categories.group.g_objects import GObjects
from dzack_research.preamble.categories.group.groups import (
    OwnedGroups,
    _element_from_engine,
    _engine_group,
    _owned_group,
)
from dzack_research.preamble.categories.group.magmas import AdditiveGroups
from dzack_research.preamble.categories.modules.general_modules import GeneralModules
from dzack_research.preamble.categories.modules.group_modules.isotypic import (
    _split_irreducible_characters,
    _isotypic_component,
    _isotypic_decomposition,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
    _ModuleMorCommonMethods,
    _combined_linearity_decision,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    FinitelyGeneratedFreeModules,
    FinitelyPresentedModules,
    LinearEndCategoryConstruction,
    LinearMorModules,
    Modules,
    ModulesWithChosenFinitePresentation,
)
from dzack_research.preamble.categories.rings.ring_foundation import _owned_engine_element
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedRings,
    _engine_element,
    _engine_ring,
    _own_ring,
    _owned_ring,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    finite_indexed_family,
    indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.owned_category import _object_of


class GroupModuleMorCategoryConstruction(MorCategoryConstruction):
    def fixed_category_class(self):
        return GroupModuleMor


class ModulesOverGroupAlgebra(Modules):
    r"""``Modules(R[G])``: the modules over a group algebra.

    ``Modules(S)`` constructs this category whenever ``S`` is a group
    algebra, so the spelling is ``Modules(R[G])``.  A represented object is an
    actual module with scalar ring ``R[G]``, built on the data of the
    ``R``-module ``M`` the action was stated on: ``Modules(R[G])(M, rho)``
    retains ``M`` as its datum and answers ``unformed_module()`` with it, and
    elements pass between the two by coercion, ``N(m)`` and ``M(n)``.
    Equivariant morphisms are the ``R``-linear maps between the retained
    modules commuting with ``G``.
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
        r"""What every module category declares; ``G``-objects over ``R`` are reached by :meth:`restriction_along_group_inclusion`."""
        return [AdditiveGroups().AdditiveCommutative()]

    _MorCategory = GroupModuleMorCategoryConstruction
    _EndCategory = LinearEndCategoryConstruction

    def an_object(self):
        r"""The trivial action on the free module of rank one."""
        ring = self.coefficient_ring()
        return Modules(ring).trivial_action(self.acting_group())(Modules(ring).an_object())

    @cached_method
    def coefficient_inclusion(self):
        r"""The ring morphism ``R -> R[G]``, ``r |-> r 1``, along which scalars restrict to ``R``."""
        algebra = self.group_algebra()
        return OwnedRings().Mor(self.coefficient_ring(), algebra)(
            lambda scalar: algebra.scalar_multiple(scalar, algebra.one())
        )

    # The equivalence ``Modules(R[G]) ~ GObjects(G, Modules(R))``: restricting
    # the ring action along ``G -> R[G]`` gives the action, and extending an
    # action ``R``-linearly gives back the ``R[G]``-module.

    @cached_method
    def restriction_along_group_inclusion(self):
        r"""``Modules(R[G]) -> GObjects(G, Modules(R))``, the action ``G -> Aut_R(M)`` of an ``R[G]``-module."""
        return _RestrictionAlongGroupInclusionFunctor(self.group_algebra())

    @cached_method
    def linearization(self):
        r"""``GObjects(G, Modules(R)) -> Modules(R[G])``, the ``R``-linear extension of a ``G``-action."""
        return _LinearizationFunctor(self.group_algebra())

    @cached_method
    def linearization_equivalence(self):
        r"""Linearization left adjoint to restriction along ``G -> R[G]``, with invertible unit and counit."""
        return _LinearizationEquivalence(self.group_algebra())

    def _call_(self, module, action):
        r"""Construct the actual ``R[G]``-module defined by the supplied action."""
        if isinstance(action, Functor):
            if action.domain() != self.acting_group().classifying_category():
                raise ValueError(
                    f"{action} cannot define an action of {self.acting_group()} on {module}: its domain is "
                    f"{action.domain()}, not the one-object category of {self.acting_group()}"
                )
            return _equip_action(module, action)
        if isinstance(action, Map) and action.domain() is self.group_algebra():
            return _equip_action(module, action)
        return _equip_action(module, self.acting_group(), action)

    def is_semisimple(self) -> bool:
        r"""Maschke's theorem, asked of the group algebra."""
        return self.base_ring().is_semisimple()

    def splitting_field(self):
        r"""Return a represented cyclotomic field splitting the finite acting group.

        Brauer's theorem gives ``QQ(zeta_|G|)`` as a splitting field.  For
        groups of order at most two the coefficient fraction field already
        contains all character values, so it is retained literally.
        """
        from dzack_research.preamble.categories.rings.number_fields import (
            CyclotomicField,
        )

        group = self.acting_group()
        assert group.is_finite() is True, (
            f"cannot give a splitting field for {group}: this is computed only for finite groups, "
            f"and {group} is not known to be finite"
        )
        fraction_field = self.coefficient_ring().fraction_field()
        order = int(group.order())
        if order <= 2:
            return fraction_field
        cyclotomic = CyclotomicField(order)
        assert fraction_field.exact_embeddings(cyclotomic).cardinality() != 0, (
            f"cannot give a splitting field for {group} over {self.coefficient_ring()}: the fraction field "
            f"{fraction_field} does not embed into the cyclotomic field {cyclotomic} of order {order}"
        )
        return cyclotomic

    def is_split(self) -> bool:
        r"""Return whether the coefficient fraction field already contains the selected splitting field."""
        fraction_field = self.coefficient_ring().fraction_field()
        return bool(fraction_field.has_coerce_map_from(self.splitting_field()))

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

    def coefficient_base_change_adjunction(self, ring_map):
        r"""Return coefficient scalar change ``R[G]-Mod <-> S[G]-Mod`` along ``R -> S``."""
        if _owned_ring(ring_map.domain()) is not self.coefficient_ring():
            raise ValueError(
                f"cannot change coefficients of {self} along {ring_map}: its domain is "
                f"{ring_map.domain()}, but the coefficient ring is {self.coefficient_ring()}"
            )
        from dzack_research.preamble.categories.functors.group_scalar_change import (
            _group_module_base_change_adjunction,
        )

        return _group_module_base_change_adjunction(ring_map, self.acting_group())

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
            _CoinvariantsFunctor,
        )
        from dzack_research.preamble.categories.functors.group_induction import (
            _InductionFunctor,
        )

        assert _owned_ring(ring_map.domain()) is self.base_ring()
        match ring_map:
            case _ if ring_map.is_group_algebra_subgroup_inclusion():
                return _InductionFunctor(ring_map)
            case _ if ring_map.is_group_algebra_augmentation():
                return _CoinvariantsFunctor(ring_map)
            case _:
                return _ScalarExtensionFunctor(ring_map)

    def restriction_of_scalars(self, ring_map):
        r"""``Res_f : Modules(R[G]) -> Modules(A)`` along ``ring_map: A -> R[G]``."""
        from dzack_research.preamble.categories.functors.group_induction import (
            _RestrictionOfActingGroupFunctor,
        )
        from dzack_research.preamble.categories.functors.scalar_change import (
            _RestrictionOfScalarsFunctor,
        )

        assert _owned_ring(ring_map.codomain()) is self.base_ring()
        match ring_map:
            case _ if ring_map.is_group_algebra_subgroup_inclusion():
                return _RestrictionOfActingGroupFunctor(ring_map)
            case _:
                return _RestrictionOfScalarsFunctor(ring_map)

    def coextension_of_scalars(self, ring_map):
        r"""``Hom_{R[G]}(S, -) : Modules(R[G]) -> Modules(S)`` along ``ring_map: R[G] -> S``."""
        from dzack_research.preamble.categories.functors.group_actions import (
            _InvariantsFunctor,
        )
        from dzack_research.preamble.categories.functors.group_induction import (
            _CoinductionFunctor,
        )
        from dzack_research.preamble.categories.functors.scalar_change import (
            _CoextensionOfScalarsFunctor,
        )

        assert _owned_ring(ring_map.domain()) is self.base_ring()
        match ring_map:
            case _ if ring_map.is_group_algebra_subgroup_inclusion():
                return _CoinductionFunctor(ring_map)
            case _ if ring_map.is_group_algebra_augmentation():
                return _InvariantsFunctor(ring_map)
            case _:
                return _CoextensionOfScalarsFunctor(ring_map)

    def base_change_adjunction(self, ring_map):
        r"""``S tensor_{R[G]} - -| Res_f`` along ``ring_map: R[G] -> S``."""
        from dzack_research.preamble.categories.functors.group_actions import (
            _CoinvariantsTrivialAdjunction,
        )
        from dzack_research.preamble.categories.functors.group_induction import (
            _InductionRestrictionAdjunction,
        )
        from dzack_research.preamble.categories.functors.scalar_change import (
            _base_change_adjunction,
        )

        assert _owned_ring(ring_map.domain()) is self.base_ring()
        match ring_map:
            case _ if ring_map.is_group_algebra_subgroup_inclusion():
                return _InductionRestrictionAdjunction(ring_map)
            case _ if ring_map.is_group_algebra_augmentation():
                return _CoinvariantsTrivialAdjunction(ring_map)
            case _:
                return _base_change_adjunction(ring_map)

    def restriction_coextension_adjunction(self, ring_map):
        r"""``Res_f -| Hom_A(R[G], -)`` along ``ring_map: A -> R[G]``."""
        from dzack_research.preamble.categories.functors.group_induction import (
            _RestrictionCoinductionAdjunction,
        )
        from dzack_research.preamble.categories.functors.scalar_change import (
            _restriction_coextension_adjunction,
        )

        assert _owned_ring(ring_map.codomain()) is self.base_ring()
        match ring_map:
            case _ if ring_map.is_group_algebra_subgroup_inclusion():
                return _RestrictionCoinductionAdjunction(ring_map)
            case _:
                return _restriction_coextension_adjunction(ring_map)

    def restriction(self, subgroup):
        r"""``Res_H^G : Modules(R[G]) -> Modules(R[H])``, restriction along ``R[H] -> R[G]``."""
        return self.restriction_of_scalars(Modules(self.coefficient_ring()[subgroup])._group_algebra_inclusion(self.acting_group()))

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
        return self.restriction_coextension_adjunction(Modules(self.coefficient_ring()[subgroup])._group_algebra_inclusion(self.acting_group()))

    class ParentMethods:
        def __init__(
            self,
            unformed_module,
            source_action_functor,
            **rest,
        ) -> None:
            self._preamble_unformed_module = unformed_module
            self._preamble_source_action_functor = source_action_functor
            super().__init__(**rest)

        def _group_module_placement(self):
            r"""The ``Modules(R[G])`` this object is placed in; its parameter names the group."""
            for placement in self.category().all_super_categories(proper=False):
                # Sage realizes each category instance in a dynamic subclass,
                # so the placement is recognized by its category class.
                if isinstance(placement, ModulesOverGroupAlgebra):
                    return placement
            raise AssertionError(
                f"{self} is not a module over a group algebra R[G]; it is only known to be in {self.category()}"
            )

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
            coefficient_module = self.unformed_module()
            endomorphisms = Modules(self.coefficient_ring()).Mor(
                coefficient_module,
                coefficient_module,
            )
            functor = self.action_functor()
            classifying = functor.domain()
            point = classifying.an_object()
            arrows = classifying.Mor(point, point)
            return Sets().Mor(self.group(), endomorphisms)(
                lambda group_element: endomorphisms(functor(arrows(group_element)))
            )

        @cached_method
        def action_functor(self):
            from dzack_research.preamble.categories.functors.group_actions import (
                GroupActionFunctor,
            )

            match self._is_the_regular_module():
                case False:
                    return self._preamble_source_action_functor
                case True:
                    coefficient_module = self.unformed_module()
                    endomorphisms = Modules(self.coefficient_ring()).Mor(
                        coefficient_module,
                        coefficient_module,
                    )
                    labels = coefficient_module.module_generating_set()
                    return GroupActionFunctor(
                        self.group(),
                        Modules(self.coefficient_ring()),
                        coefficient_module,
                        lambda group_element: endomorphisms(
                            {
                                label: coefficient_module.module_generator(group_element * label)
                                for label in labels
                            }
                        ),
                    )

        @cached_method
        def action_of(self, group_element):
            r"""The coefficient-linear automorphism induced by ``group_element``."""
            if group_element not in self.group():
                raise ValueError(f"{group_element} is not an element of {self.group()}")
            return self.action()(group_element)

        def act(self, group_element, element):
            r"""Act on an ``R[G]``-module element through the module the action was stated on."""
            module = self.unformed_module()
            return self(self.action_of(group_element)(module(element)))

        def is_invariant(self, element):
            r"""Decide ``g . element = element`` for every ``g``, on the chosen group generators."""
            group = self.group()
            if not group.has_selected_group_resolution():
                return Unknown
            return all(self.act(generator, element) == element for generator in group.group_generators())

        def restrict_action(self, group_morphism):
            r"""This module acted on by ``H`` through ``phi: H -> G``: restriction of scalars along ``R[H] -> R[G]``."""
            algebra_morphism = OwnedGroups().group_algebra(self.coefficient_ring())(group_morphism)
            return self.module_category().restriction_of_scalars(algebra_morphism)(self)

        @cached_method
        def is_trivial_action(self) -> bool:
            r"""Decide whether every represented group element acts as the identity.

            Triviality is a property of the action, decided from it: for a
            finitely generated group acting on a finitely generated module it
            is enough to check the selected group generators on the selected
            module generators.
            """
            if self._is_the_regular_module():
                return bool(self.group().cardinality() == 1)

            group = self.group()
            assert group.has_selected_group_resolution(), (
                f"cannot decide whether {group} acts trivially on {self}: this needs a chosen finite generating "
                f"set of {group}, but {group} is only known to be in {group.category()}"
            )
            module = self.unformed_module()
            labels = module.module_generating_set()
            assert labels.cardinality().is_finite() is True, (
                f"cannot decide whether {group} acts trivially on {self}: this needs a finite generating set of "
                f"the module {module}, but its chosen generating set {labels} is not known to be finite"
            )
            for group_generator in group.group_generators():
                action = self.action_of(group_generator)
                for label in labels:
                    generator = module.module_generator(label)
                    equal = action(generator) == generator
                    if equal is False:
                        return False
                    assert equal is True, (
                        f"cannot decide whether {group} acts trivially on {self}: whether the generator "
                        f"{group_generator} fixes the module generator {generator} is undecided"
                    )
            return True

        def unformed_module(self):
            r"""Return the ``R``-module the action was stated on: the datum this module is built on."""
            if self._is_the_regular_module():
                return self
            return self._preamble_unformed_module

        def _element_of_unformed_module(self, element):
            r"""The element of the module the action was stated on, on the same data.

            The ``R[G]``-module is built on the underlying additive group of
            that module, so an element reads there as its underlying additive
            element.
            """
            return self.unformed_module()(self._underlying_additive_element(element))

        def _element_from_unformed_module(self, element):
            r"""The element of this ``R[G]``-module on the data of an element of the module the action was stated on."""
            return self(element)

        def Mor(self, codomain, category=None):
            r"""``Mor_{R[G]}(M,N)``, the equivariant maps.

            The underlying coefficient-linear Mor is
            ``Hom_R(M.unformed_module(), N.unformed_module())`` and is
            exposed by the resulting Mor object's :meth:`underlying_mor`.
            """
            if category is None or category.is_subcategory(Modules(self.group_algebra())):
                return Modules(self.group_algebra()).Mor(self, codomain)
            return super().Mor(codomain, category)

        def End(self):
            r"""``End_{R[G]}(M)``, the equivariant endomorphism object.

            The underlying ``R``-linear endomorphisms are
            ``Modules(R).End(M.unformed_module())``.  A group module's
            default Mor is already equivariant, so its default End uses the
            same owner.
            """
            return Modules(self.group_algebra()).End(self)

        def Aut(self):
            r"""``Aut_{R[G]}(M)``, the equivariant module automorphisms.

            Use ``Modules(R).Aut(M.unformed_module())`` explicitly when the
            action is to be forgotten and all underlying ``R``-linear
            automorphisms are wanted.
            """
            return Modules(self.group_algebra()).Aut(self)

        def _Hom_(self, codomain, category=None):
            if codomain not in Modules(self.group_algebra()):
                raise TypeError(
                    f"no {self.group_algebra()}-module morphisms {self} -> {codomain}: the codomain is not a "
                    f"module over {self.group_algebra()}; it is in {codomain.category()}"
                )
            return Modules(self.group_algebra()).Mor(self, codomain)

        def _finite_action_endomorphism_family(self):
            r"""Return ``{id_M} union {rho(s) : s in S}`` for a chosen finite ``S``.

            Choosing a finite group generating set is a represented backend for
            the wide equalizer/coequalizer of the full action; callers retain
            the universal-construction spelling.
            """
            group = self.group()
            assert group.has_selected_group_resolution(), (
                f"cannot form the invariants or coinvariants of {self}: this needs a chosen finite generating "
                f"set of {group}, but {group} is only known to be in {group.category()}"
            )
            generators = group.group_generators()
            indices = Sets().coproduct(
                indexed_family(
                    Sets.Δ[1],
                    lambda side: Sets.Δ[0] if int(side) == 0 else generators,
                )
            )
            coefficient_module = self.unformed_module()
            identity = coefficient_module.module_category().Mor(coefficient_module, coefficient_module).identity()
            return finite_indexed_family(
                indices,
                lambda tagged: identity if int(tagged.summand_index()) == 0 else self.action_of(tagged.summand_element()),
                name=f"Identity and chosen action generators on {self}",
            )

        def module_invariants(self):
            r"""``M^G = Hom_{R[G]}(R, M)``, the wide equalizer of the action and the identity."""
            if self.is_trivial_action():
                return self.unformed_module()
            coefficient_module = self.unformed_module()
            return Modules(coefficient_module.base_ring()).equalizer_of_family(
                self._finite_action_endomorphism_family()
            )

        def module_coinvariants(self):
            r"""``M_G = R tensor_{R[G]} M``, the wide coequalizer of the action and the identity."""
            if self.is_trivial_action():
                return self.unformed_module()
            coefficient_module = self.unformed_module()
            return Modules(coefficient_module.base_ring()).coequalizer_of_family(
                self._finite_action_endomorphism_family()
            )

        @cached_method
        def equivariant_endomorphism_module(self):
            r"""``End_{R[G]}(M) = Hom_R(M, M)^G``: the invariants of conjugation.

            ``G`` acts on ``Hom_R(M, M)`` by ``g . f = rho(g) f rho(g)^{-1}``,
            and the equivariant endomorphisms are its fixed points.
            """
            coefficient_module = self.unformed_module()
            endomorphisms = coefficient_module.module_category().Mor(
                coefficient_module,
                coefficient_module,
            )

            def conjugation(group_element, endomorphism):
                return self.action_of(group_element) * endomorphism * self.action_of(group_element.inverse())

            return Modules(endomorphisms.base_ring()[self.group()])(
                endomorphisms,
                conjugation,
            ).module_invariants()

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

            return finite_ordered_set(tuple(character for character in _split_irreducible_characters(self) if self.isotypic_component(character).module_rank() != 0))

        def isotypic_component(self, character):
            r"""Return the integral/base-ring isotypic component as a subobject."""

            return _isotypic_component(self, character)

        def isotypic_decomposition(self):
            r"""Return the sum of isotypic components together with its inclusion in ``M``."""

            return _isotypic_decomposition(self)

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
            coefficient_module = self.unformed_module()
            assert inclusion.codomain() is coefficient_module, (
                f"{inclusion} is not a subobject inclusion into {coefficient_module}"
            )

            def restricted_action(group_element, vector):
                return inclusion.lift(self.action_of(group_element)(inclusion(vector)))

            acted = Modules(submodule.base_ring()[self.group()])(submodule, restricted_action)
            def lift_from_ambient(element):
                preimage = inclusion._preimage_or_none(coefficient_module(element))
                return None if preimage is None else acted(preimage)

            return _RestrictedActionInclusionMorphism(
                acted.Mor(self),
                lambda label: self(inclusion(submodule.module_generator(label))),
                lift=lift_from_ambient,
            )

        def restrict_endomorphism_to(self, endomorphism, inclusion):
            r"""Restrict an equivariant endomorphism of ``M`` to a stable subobject.

            ``inclusion`` is the ordinary represented subobject inclusion
            ``S -> M``.  The action is first restricted to ``S`` through
            :meth:`restrict_action_to`; the endomorphism is then forced through
            ``Mor_{R[G]}(M,M)``, which is exactly the condition that it commute
            with the action.  Stability of ``S`` under the endomorphism is not
            assumed: the exact lift through the inclusion decides it.
            """
            if inclusion.codomain() is not self.unformed_module():
                raise ValueError(
                    f"cannot restrict {endomorphism} to the domain of {inclusion}: that map is not a "
                    f"submodule inclusion into {self.unformed_module()}, since its codomain is {inclusion.codomain()}"
                )
            equivariant = self.Mor(self)(endomorphism)
            acted_inclusion = self.restrict_action_to(inclusion)
            return equivariant.restrict_to(acted_inclusion)

        def restrict_automorphism_to(self, automorphism, inclusion):
            r"""Restrict an equivariant automorphism to a stable subobject.

            The result is an actual element of ``Aut_{R[G]}(S)``.  Both the
            forward and inverse ambient maps are checked in the equivariant Mor
            before restriction, and the same acted subobject is used for both
            directions; hence the returned pair is the restricted isomorphism,
            not merely an invertible-looking ``R``-linear map.
            """
            if automorphism.domain() is not self or automorphism.codomain() is not self:
                raise ValueError(
                    f"{automorphism} is not an automorphism of {self}: it is a map "
                    f"{automorphism.domain()} -> {automorphism.codomain()}"
                )
            if inclusion.codomain() is not self.unformed_module():
                raise ValueError(
                    f"cannot restrict {automorphism} to the domain of {inclusion}: that map is not a "
                    f"submodule inclusion into {self.unformed_module()}, since its codomain is {inclusion.codomain()}"
                )

            from dzack_research.preamble.categories.abstract_categories.mor_categories import (
                CategoricalIsomorphism,
            )

            acted_inclusion = self.restrict_action_to(inclusion)
            forward = self.Mor(self)(automorphism.forward()).restrict_to(
                acted_inclusion
            )
            inverse = self.Mor(self)(automorphism.inverse()).restrict_to(
                acted_inclusion
            )
            piece = acted_inclusion.domain()
            return Modules(self.group_algebra()).Aut(piece)(
                CategoricalIsomorphism(
                    forward.parent(),
                    forward,
                    inverse,
                )
            )

        def character(self):
            r"""Return the ordinary trace character in characteristic zero."""
            group = self.group()
            coefficient_module = self.unformed_module()
            coefficient_ring = self.coefficient_ring()
            assert group.is_finite() is True, (
                f"cannot compute the character of {self}: this needs a finite group, and {group} is not known to be finite"
            )
            assert coefficient_module in FinitelyGeneratedFreeModules(coefficient_ring), (
                f"cannot compute the character of {self}: the trace needs a free {coefficient_ring}-module of "
                f"finite rank, but {coefficient_module} is only known to be in {coefficient_module.category()}"
            )
            if coefficient_ring.characteristic() != 0:
                raise TypeError(
                    f"cannot compute the ordinary character of {self}: {coefficient_ring} has characteristic "
                    f"{coefficient_ring.characteristic()}, not 0; a modular representation has a Brauer "
                    f"character instead (brauer_character())"
                )
            representatives = group.conjugacy_classes_representatives()
            traces = tuple(self.action_of(group_element).trace() for group_element in representatives)

            return group.class_function(
                coefficient_ring,
                traces,
                representatives=representatives,
            )

        def brauer_character(self):
            r"""Return the Brauer character of a finite-dimensional modular representation."""
            group = self.group()
            coefficient_module = self.unformed_module()
            coefficient_ring = self.coefficient_ring()
            assert group.is_finite() is True, (
                f"cannot compute the Brauer character of {self}: this needs a finite group, and {group} is not known to be finite"
            )
            assert coefficient_module in FinitelyGeneratedFreeModules(coefficient_ring), (
                f"cannot compute the Brauer character of {self}: this needs a free {coefficient_ring}-module of "
                f"finite rank, but {coefficient_module} is only known to be in {coefficient_module.category()}"
            )
            if coefficient_ring.characteristic() == 0:
                raise TypeError(
                    f"cannot compute the Brauer character of {self}: {coefficient_ring} has characteristic 0, "
                    f"and Brauer characters are defined in positive characteristic; use character()"
                )
            if not coefficient_ring.is_field():
                raise TypeError(
                    f"cannot compute the Brauer character of {self}: the coefficient ring {coefficient_ring} is not a field"
                )

            from sage.combinat.free_module import CombinatorialFreeModule

            indices = tuple(range(int(coefficient_module.module_rank())))
            computation_module = CombinatorialFreeModule(
                _engine_ring(coefficient_ring),
                indices,
            )
            basis = computation_module.basis()

            def on_basis(group_element, index):
                action_matrix = self.action_of(group_element)
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
                return on_basis(_element_from_engine(group, engine_group_element), index)

            backend_character = engine_group.representation(
                computation_module,
                engine_on_basis,
                side="left",
            ).brauer_character()
            backend_values = tuple(backend_character)
            if not backend_values:
                raise ArithmeticError(
                    f"the Brauer character of {self} came back with no values, but {group} has at least the "
                    f"identity as a p-regular class"
                )
            value_ring = _own_ring(backend_values[0].parent())
            engine_value_ring = _engine_ring(value_ring)
            values = tuple(_owned_engine_element(value_ring, engine_value_ring(value)) for value in backend_values)
            characteristic = int(coefficient_ring.characteristic())
            representatives = tuple(representative for representative in group.conjugacy_classes_representatives() if int(representative.order()) % characteristic)
            if len(representatives) != len(values):
                raise ArithmeticError(
                    f"the Brauer character of {self} has {len(values)} values, but {group} has "
                    f"{len(representatives)} {characteristic}-regular conjugacy classes"
                )
            return group.class_function(
                value_ring,
                values,
                representatives=representatives,
            )

        def base_change(self, ring_map):
            r"""Transport this group module through the category-owned coefficient extension."""
            extension = self.module_category().coefficient_base_change_adjunction(
                ring_map
            ).left_adjoint()
            return extension(self)


def _apply_action(action, group_element, vector):
    if isinstance(action, Map):
        return action(group_element)(vector)
    return action(group_element, vector)


class _CoefficientViewModuleMorphism(ModuleMorphism):
    r"""An acted-module map read on the retained coefficient modules."""

    def __init__(self, parent, source_morphism, acted_source, acted_target) -> None:
        self._source_morphism = source_morphism
        self._acted_source = acted_source
        self._acted_target = acted_target
        target = parent.codomain()
        super().__init__(
            parent,
            lambda element: target(source_morphism(acted_source(element))),
            elementwise=True,
        )

    def _elementwise_linearity_derivation(self):
        return self._source_morphism.linearity_decision()


class _RestrictedEquivariantCoefficientMorphism(ModuleMorphism):
    r"""The coefficient map induced by restricting an equivariant endomorphism to a stable subobject."""

    def __init__(self, parent, ambient_map, inclusion) -> None:
        self._ambient_map = ambient_map
        self._inclusion = inclusion
        target = parent.codomain()
        super().__init__(
            parent,
            lambda element: target(
                inclusion.lift(ambient_map(inclusion(element)))
            ),
            elementwise=True,
        )

    def _elementwise_linearity_derivation(self):
        return _combined_linearity_decision(
            (
                self._ambient_map.underlying_module_morphism(),
                self._inclusion.underlying_module_morphism(),
            )
        )


def _coefficient_morphism_from_images(
    parent,
    images,
    *,
    elementwise=False,
):
    r"""Read equivariant-map data as a map of the retained coefficient modules."""
    source = parent.domain().unformed_module()
    target = parent.codomain().unformed_module()
    mor = source.module_category().Mor(source, target)

    if isinstance(images, GroupModuleMorphism):
        underlying = images.underlying_module_morphism()
        if underlying.domain() is source and underlying.codomain() is target:
            return mor(underlying)

    if isinstance(images, ModuleMorphism):
        if images.domain() is source and images.codomain() is target:
            return mor(images)
        if images.domain() is parent.domain() and images.codomain() is parent.codomain():
            return _CoefficientViewModuleMorphism(
                mor,
                images,
                parent.domain(),
                parent.codomain(),
            )

    if isinstance(images, Map):
        if images.domain() is source and images.codomain() is target:
            return mor.elementwise(lambda element: target(images(element)))
        if images.domain() is parent.domain() and images.codomain() is parent.codomain():
            return mor.elementwise(
                lambda element: target(images(parent.domain()(element)))
            )
        raise ValueError(
            f"{images} cannot give a map {parent.domain()} -> {parent.codomain()}: it is a map "
            f"{images.domain()} -> {images.codomain()}"
        )

    # An image stated in the acted codomain or in its retained module reads
    # in the retained module by coercion.
    if elementwise:
        if not callable(images):
            raise TypeError(
                f"{images} cannot define a map {parent.domain()} -> {parent.codomain()} elementwise: it is not a function"
            )
        return mor.elementwise(
            lambda element: target(images(parent.domain()(element))),
        )

    if isinstance(images, dict):
        return mor({label: target(value) for label, value in images.items()})
    if isinstance(images, (tuple, list)):
        return mor(tuple(target(value) for value in images))
    if callable(images):
        return mor(lambda label: target(images(label)))
    return mor(images)


class GroupModuleMorphism(ModuleMorphism):
    r"""An ``R``-linear map commuting with the chosen ``G``-actions."""

    def __init__(
        self,
        parent,
        images,
        *,
        elementwise=False,
        lift=None,
    ) -> None:
        underlying = _coefficient_morphism_from_images(
            parent,
            images,
            elementwise=elementwise,
        )
        if underlying.linearity_decision() is not True:
            raise ValueError(
                f"{underlying} is not known to be {underlying.domain().base_ring()}-linear, so it is not a "
                f"morphism {parent.domain()} -> {parent.codomain()}"
            )
        self._preamble_underlying_module_morphism = underlying
        super().__init__(
            parent,
            lambda element: parent.codomain()(
                underlying(parent.domain().unformed_module()(element))
            ),
            elementwise=True,
            lift=lift,
        )
        match self._equivariance_derivation():
            case True:
                pass
            case False:
                raise ValueError(
                    f"{underlying} is not {parent.domain().group()}-equivariant, so it is not a morphism "
                    f"{parent.domain()} -> {parent.codomain()}"
                )
            case _:
                match parent.is_equivariant(self):
                    case True:
                        pass
                    case _:
                        raise ValueError(
                            f"{underlying} is not known to be {parent.domain().group()}-equivariant, so it is "
                            f"not a morphism {parent.domain()} -> {parent.codomain()}"
                        )

    def _equivariance_derivation(self):
        r"""Return a construction-derived equivariance decision, or ``None``."""
        return None

    def _elementwise_linearity_derivation(self):
        return self._preamble_underlying_module_morphism.linearity_decision()

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

    def __mul__(self, other):
        if not isinstance(other, GroupModuleMorphism):
            return super().__mul__(other)
        if other.codomain() is not self.domain():
            return NotImplemented
        underlying = self.underlying_module_morphism() * other.underlying_module_morphism()
        return other.domain().Mor(self.codomain())._from_equivariant_images(
            underlying,
        )

    def natural_transformation(self):
        r"""Return this equivariant map as the corresponding transformation ``BG => C``."""
        source = self.domain().action_functor()
        target = self.codomain().action_functor()
        component = self.underlying_module_morphism()
        return NaturalTransformation(
            source, target, lambda _obj: component
        ).morphism()

    def restrict_to(self, inclusion):
        r"""Restrict this equivariant endomorphism along an equivariant inclusion.

        If ``i:S -> M`` is equivariant and ``f:M -> M`` preserves ``i(S)``, the
        restriction is the unique ``f_S`` satisfying ``i f_S = f i``.  The
        inclusion's represented lift constructs that unique map.
        """
        ambient = self.domain()
        if self.codomain() is not ambient:
            raise ValueError(
                f"cannot restrict {self} to a submodule: it is a map {ambient} -> {self.codomain()}, "
                f"not an endomorphism"
            )
        if inclusion.codomain() is not ambient:
            raise ValueError(
                f"cannot restrict {self} along {inclusion}: that map lands in {inclusion.codomain()}, not in {ambient}"
            )
        piece = inclusion.domain()
        if piece not in Modules(ambient.group_algebra()):
            raise TypeError(
                f"cannot restrict {self} to {piece}: the submodule is not a module over "
                f"{ambient.group_algebra()}; it is in {piece.category()}"
            )

        underlying = _RestrictedEquivariantCoefficientMorphism(
            piece.unformed_module().module_category().Mor(
                piece.unformed_module(),
                piece.unformed_module(),
            ),
            self,
            inclusion,
        )
        return piece.Mor(piece)._from_equivariant_images(
            underlying,
        )

    def inverse(self):
        r"""The inverse of an equivariant isomorphism, still equivariant."""
        ordinary_inverse = self.underlying_module_morphism().inverse()
        return self.codomain().Mor(self.domain())._from_equivariant_images(
            ordinary_inverse,
        )

    def as_automorphism(self):
        r"""Return this invertible equivariant endomorphism in ``Aut_{R[G]}(M)``."""
        from dzack_research.preamble.categories.abstract_categories.mor_categories import (
            CategoricalIsomorphism,
        )

        module = self.domain()
        if self.codomain() is not module:
            raise ValueError(
                f"{self} is not an automorphism: it is a map {module} -> {self.codomain()}"
            )
        inverse = self.inverse()
        return Modules(module.group_algebra()).Aut(module)(
            CategoricalIsomorphism(
                self.parent(),
                self,
                inverse,
            )
        )


class _ConstructedEquivariantGroupModuleMorphism(GroupModuleMorphism):
    r"""An equivariant map whose construction already proves the action square."""

    def _equivariance_derivation(self):
        return True


class _RestrictedActionInclusionMorphism(_ConstructedEquivariantGroupModuleMorphism):
    r"""The equivariant inclusion induced from an admitted stable module subobject."""

    def _selected_lift_derivation(self):
        return True


class GroupModuleMor(_ModuleMorCommonMethods, CategoricalMor):
    Element = GroupModuleMorphism

    def __init__(self, mor_family, domain, codomain) -> None:
        assert domain.group() == codomain.group(), (
            f"no equivariant morphisms {domain} -> {codomain}: the domain is acted on by {domain.group()} "
            f"but the codomain by {codomain.group()}"
        )
        coefficient_ring = domain.coefficient_ring()
        if codomain.coefficient_ring() is not coefficient_ring:
            raise ValueError(
                f"no equivariant morphisms {domain} -> {codomain}: the domain has coefficients in "
                f"{coefficient_ring} but the codomain in {codomain.coefficient_ring()}"
            )
        scalar_ring = (
            coefficient_ring
            if coefficient_ring in OwnedRings().Commutative()
            else _own_ring(SageZZ)
        )
        self._preamble_base_ring = scalar_ring
        self._preamble_algebra_base_ring = scalar_ring
        CategoricalMor.__init__(
            self,
            mor_family,
            domain,
            codomain,
            category=LinearMorModules(scalar_ring),
        )

    def underlying_mor(self):
        r"""``Hom_R(Res M, Res N)``, containing the equivariant maps."""
        source = self.domain().unformed_module()
        target = self.codomain().unformed_module()
        return source.module_category().Mor(source, target)

    def is_equivariant(self, arrow):
        group = self.domain().group()
        if not group.has_selected_group_resolution():
            return Unknown
        underlying = _coefficient_morphism_from_images(
            self,
            arrow,
            elementwise=False,
        )
        return all(
            underlying * self.domain().action_of(generator)
            == self.codomain().action_of(generator) * underlying
            for generator in group.group_generators()
        )

    def _element_constructor_(self, images, *, lift=None):
        if isinstance(images, GroupModuleMorphism) and images.parent() is self and lift is None:
            return images
        return self.element_class(self, images, lift=lift)

    def _from_equivariant_images(
        self,
        images,
        *,
        elementwise=False,
    ):
        r"""Construct a map whose equivariance follows from its construction.

        This protected path is for functorial images, identities, and
        compositions.  Arbitrary user-supplied maps still use the ordinary
        constructor and are checked on the selected group/module generators.
        """
        return _ConstructedEquivariantGroupModuleMorphism(
            self,
            images,
            elementwise=elementwise,
        )

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError(
                f"{self} has no identity: its domain {self.domain()} and codomain {self.codomain()} differ"
            )
        underlying = self.underlying_mor().identity()
        return self._from_equivariant_images(underlying)

    def _repr_(self):
        return f"Mor_{self.domain().group()}({self.domain()}, {self.codomain()})"



class _CoefficientModuleEngine:
    r"""The coefficient presentation of a linearized action.

    Private realization selected only by the group-module entry.  A lattice
    carrying an action already has its free-module realization and must not
    inherit conversions through a second coefficient-module presentation.
    The group-module category owns the action; this engine reads coordinates
    from the exact coefficient module on which that action was stated.
    """

    def _selected_module_coefficients(self, element):
        if self._is_the_regular_module():
            return super()._selected_module_coefficients(element)
        module = self.unformed_module()
        group_algebra = self.group_algebra()
        return {
            label: group_algebra(coefficient)
            for label, coefficient in module.framing_coefficients(module(element)).items()
        }

    def _selected_presentation_rows(self):
        if self._is_the_regular_module():
            return super()._selected_presentation_rows()
        return self.unformed_module()._selected_presentation_rows()

    def coefficient_module_rank(self):
        return self.unformed_module().module_rank()

    def module_rank(self):
        r"""Return the rank of the retained coefficient-module presentation.

        This is the representation rank over ``R``.  It is not a claim
        that the module is free of this rank over ``R[G]``.
        """
        return self.coefficient_module_rank()

    def invariant_factors(self):
        r"""Invariant factors of the retained coefficient module."""
        return self.unformed_module().invariant_factors()


def _equip_action(module, group_or_action, action=None):
    r"""Linearize a left ``G``-action to an actual ``R[G]``-module.

    The ``R[G]``-module is built on the data of ``M`` by the generic module
    action ``R[G] -> End_Ab(U_R(M))``; ``M`` is retained as the datum and
    answered by ``unformed_module()``, with its selected presentation.
    ``action`` may be an actual ``BG -> Modules(R)`` functor, a ring morphism
    out of ``R[G]``, or the binary action ``action(g,m)``.
    """

    base_ring = module.base_ring()
    assert module in FinitelyPresentedModules(base_ring), (
        f"cannot equip {module} with a group action: this needs a finitely presented {base_ring}-module, "
        f"but {module} is only known to be in {module.category()}"
    )
    ring_action = None
    supplied_action_functor = None
    source_action = action
    match action:
        case None:
            source_action = group_or_action
            match source_action:
                case Functor():
                    classifying = source_action.domain()
                    match source_action.codomain() == Modules(base_ring):
                        case True:
                            pass
                        case False:
                            raise ValueError(
                                f"{source_action} cannot define an action on {module}: its codomain is "
                                f"{source_action.codomain()}, not {Modules(base_ring)}"
                            )
                    group = _owned_group(classifying.group())
                    match source_action(classifying.an_object()) is module:
                        case True:
                            pass
                        case False:
                            raise ValueError(
                                f"{source_action} does not define an action on {module}: it sends the one "
                                f"object to {source_action(classifying.an_object())}"
                            )
                    supplied_action_functor = source_action
                case Map():
                    match source_action.domain():
                        case group_algebra if group_algebra in GroupAlgebras(base_ring):
                            group = group_algebra.group()
                            ring_action = source_action

                            def action_from_ring(group_element, vector):
                                return ring_action(group_algebra.module_generator(group_element))(vector)

                            source_action = action_from_ring

                        case acting_group:
                            group = _owned_group(acting_group)
                case _:
                    raise TypeError(
                        f"{source_action} cannot define a group action on {module}: expected a functor from "
                        f"the one-object category of a group, or a morphism out of a group or group algebra"
                    )
        case _:
            group = _owned_group(group_or_action)

    labels = module.module_generating_set()
    assert labels.cardinality().is_finite(), (
        f"cannot equip {module} with a group action: this needs a finite generating set of the module, "
        f"but its chosen generating set {labels} is not known to be finite"
    )

    is_free = module in FinitelyGeneratedFreeModules(base_ring)
    if not is_free and module not in ModulesWithChosenFinitePresentation(base_ring):
        raise TypeError(
            f"cannot equip {module} with a group action: it is not known to be free, so it needs a chosen "
            f"finite presentation by generators and relations, and it has none; it is in {module.category()}"
        )

    group_algebra = base_ring[group]
    coefficient_modules = Modules(base_ring)
    coefficient_endomorphisms = coefficient_modules.Mor(module, module)
    classifying = group.classifying_category()
    point = classifying.an_object()
    classifying_arrows = classifying.Mor(point, point)

    def admitted_action_morphism(group_element):
        match supplied_action_functor:
            case None:
                return coefficient_endomorphisms(
                    {
                        label: module(
                            _apply_action(
                                source_action,
                                group_element,
                                module.module_generator(label),
                            )
                        )
                        for label in labels
                    }
                )
            case functor:
                return coefficient_endomorphisms(
                    functor(classifying_arrows(group_element))
                )

    match group.has_selected_group_resolution():
        case True:
            identity = coefficient_endomorphisms.identity()
            match admitted_action_morphism(group.one()) == identity:
                case True:
                    pass
                case _:
                    raise ValueError(
                        f"the proposed action of {group} on {module} is not an action: the identity of {group} "
                        f"does not act as the identity map"
                    )
            for group_generator in group.group_generators():
                forward = admitted_action_morphism(group_generator)
                inverse = admitted_action_morphism(~group_generator)
                match (inverse * forward == identity, forward * inverse == identity):
                    case (True, True):
                        pass
                    case _:
                        raise ValueError(
                            f"the proposed action of {group} on {module} is not an action: the generator "
                            f"{group_generator} does not act by an automorphism, since its action and that of "
                            f"its inverse do not compose to the identity"
                        )
        case _:
            pass

    from dzack_research.preamble.categories.functors.group_actions import GroupActionFunctor
    from dzack_research.preamble.categories.group.g_objects import _verify_relators

    represented_action = Sets().Mor(group, coefficient_endomorphisms)(
        admitted_action_morphism
    )
    _verify_relators(represented_action, group, coefficient_endomorphisms)
    match supplied_action_functor:
        case None:
            source_action_functor = GroupActionFunctor(
                group,
                coefficient_modules,
                module,
                admitted_action_morphism,
            )
        case functor:
            source_action_functor = functor

    def selected_action_morphism(group_element):
        return coefficient_endomorphisms(
            source_action_functor(classifying_arrows(group_element))
        )

    additive_group = module.underlying_additive_group()
    additive_endomorphisms = AdditiveGroups().AdditiveCommutative().End(additive_group)

    def module_element(additive_element):
        return module(additive_element)

    def additive_element(module_element_value):
        return module._underlying_additive_element(module(module_element_value))

    def linearized_scalar(scalar):
        coefficients = group_algebra.framing_coefficients(group_algebra(scalar))

        def apply(additive_vector):
            vector = module_element(additive_vector)
            result = module.zero()
            for group_element, coefficient in coefficients.items():
                result += module.scalar_multiple(
                    coefficient,
                    selected_action_morphism(group_element)(vector),
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
        else group_algebra.Mor(additive_endomorphisms)(
            linearized_scalar,
        )
    )
    framing_source = group_algebra.free_module(labels)
    return _object_of(
        GeneralModules(group_algebra),
        _engine=(Modules(group_algebra), _CoefficientModuleEngine, None),
        base_ring=group_algebra,
        rho=scalar_action,
        module_generating_set=labels,
        module_generator_function=module.module_generator,
        framing_source=framing_source,
        unformed_module=module,
        source_action_functor=source_action_functor,
    )


class _RestrictionAlongGroupInclusionFunctor(Functor):
    r"""``Modules(R[G]) -> GObjects(G, Modules(R))``: the action ``G -> Aut_R(M)`` of an ``R[G]``-module."""

    _faithful = True

    def __init__(self, group_algebra) -> None:
        modules = Modules(group_algebra)
        self._group = modules.acting_group()
        self._coefficient_modules = Modules(modules.coefficient_ring())
        super().__init__(modules, GObjects(self._group, self._coefficient_modules))

    def _apply_object(self, module):
        return self.codomain()(module.action_functor())

    def _apply_morphism(self, morphism):
        source = self.object_image(morphism.domain())
        target = self.object_image(morphism.codomain())
        return self.codomain().Mor(source, target)(morphism.natural_transformation())

    def _repr_(self):
        return f"Restriction of {self.domain()} along {self._group} -> {self.domain().base_ring()}"


class _LinearizationFunctor(Functor):
    r"""``GObjects(G, Modules(R)) -> Modules(R[G])``: the ``R``-linear extension of a ``G``-action."""

    _faithful = True

    def __init__(self, group_algebra) -> None:
        modules = Modules(group_algebra)
        self._group = modules.acting_group()
        self._coefficient_modules = Modules(modules.coefficient_ring())
        super().__init__(GObjects(self._group, self._coefficient_modules), modules)

    def _apply_object(self, acted):
        from dzack_research.preamble.categories.functors.group_actions import (
            _action_functor_of,
        )

        action = _action_functor_of(acted, self._group, self._coefficient_modules)
        return self.codomain()(action(action.domain().an_object()), action)

    def _apply_morphism(self, arrow):
        from dzack_research.preamble.categories.functors.group_actions import (
            _underlying_equivariant_arrow,
        )

        source = self.object_image(arrow.domain())
        target = self.object_image(arrow.codomain())
        component = _underlying_equivariant_arrow(arrow, self._group, self._coefficient_modules)
        return self.codomain().Mor(source, target)._from_equivariant_images(
            component,
        )

    def _repr_(self):
        return f"Linearization of {self._group}-actions over {self._coefficient_modules.base_ring()}"


class _LinearizationEquivalence(Adjunction):
    r"""``GObjects(G, Modules(R)) ~ Modules(R[G])``, linearization left adjoint to restriction along ``G -> R[G]``.

    Unit and counit are the identity of the underlying ``R``-module read
    between the two constructions, so both are isomorphisms.
    """

    def __init__(self, group_algebra) -> None:
        super().__init__(
            _LinearizationFunctor(group_algebra),
            _RestrictionAlongGroupInclusionFunctor(group_algebra),
        )

    def _unit_component(self, acted):
        linearized = self.left_adjoint()(acted)
        underlying = linearized.unformed_module()
        identity = underlying.module_category().Mor(underlying, underlying).identity()
        return self.left_adjoint().domain().Mor(acted, self.right_adjoint()(linearized))(
            lambda _obj: identity
        )

    def _counit_component(self, module):
        relinearized = self.left_adjoint()(self.right_adjoint()(module))
        underlying = module.unformed_module()
        identity = underlying.module_category().Mor(underlying, underlying).identity()
        return self.right_adjoint().domain().Mor(relinearized, module)._from_equivariant_images(
            identity,
        )

    def _repr_(self):
        return f"Linearization equivalence {self.left_adjoint().domain()} <-> {self.left_adjoint().codomain()}"


__all__ = [
    "GroupModuleMor",
    "GroupModuleMorphism",
    "ModulesOverGroupAlgebra",
]
