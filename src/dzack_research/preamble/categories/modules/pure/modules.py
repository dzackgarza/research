"""Owned categories of modules and vector spaces."""

import itertools
import operator
from dataclasses import dataclass

from sage.categories.action import Action
from sage.categories.category import Category
from sage.categories.category_with_axiom import all_axioms
from sage.categories.commutative_additive_groups import CommutativeAdditiveGroups
from sage.categories.groups import Groups as SageGroups
from sage.matrix.constructor import matrix as engine_matrix
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.misc_c import prod
from sage.misc.unknown import Unknown
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.element import ModuleElement
from sage.structure.element import parent as element_parent
from sage.structure.parent import Parent
from sage.structure.richcmp import richcmp
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    EndCategoryConstruction,
    HomCategoryConstruction,
    IsoCategoryConstruction,
    MonoCategoryConstruction,
    _category_homset,
)
from dzack_research.preamble.categories.abstract_categories.products import (
    SelectedColimitConstruction,
    SelectedLimitConstruction,
    _discrete_diagram,
    _factor_family,
    _finite_factor_family,
    _parallel_pair_diagram,
)
from dzack_research.preamble.categories.algebras.associative_algebra_morphisms import (
    AssociativeAlgebraHomCategoryConstruction,
)
from dzack_research.preamble.categories.group.magmas import AdditiveGroups
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleAutomorphismGroup,
    ModuleEmbeddingHomset,
    ModuleHomset,
    ModuleMorphism,
    SubFramingMorphism,
    TensorProductModuleHomset,
    _framing_morphism,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    IntegralDomains,
    LocalizationRings,
    LocalRings,
    OwnedCategoryOverBaseRing,
    OwnedFields,
    OwnedOrders,
    OwnedRings,
    PrincipalIdealDomains,
    _engine_element,
    _engine_ring,
    _own_ring,
    _owned_ring,
)
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.modules.module_morphisms.morphism_matrices import (
    _row_normal_form,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    FiniteOrderedSets,
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    IndexedFamily,
    finite_indexed_family,
    indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import (
    NN,
    Sets,
)
from dzack_research.preamble.owned_category_bases import CategoryWithAxiom
from dzack_research.preamble.refine import refine

for _module_axiom in ("FinitelyGenerated", "Free", "Projective", "Torsion"):
    if _module_axiom not in all_axioms:
        all_axioms.add(_module_axiom)


class _ModuleScalarAction(Action):
    r"""The selected scalar action of the base ring on one module parent."""

    def __init__(self, scalar_parent, module, is_left) -> None:
        self._module = module
        Action.__init__(self, scalar_parent, module, is_left, operator.mul)

    def _act_(self, scalar, element):
        return self._module.scalar_multiple(scalar, element)


def _register_module_scalar_action(module) -> None:
    r"""Register ordinary ``r*m``/``m*r`` syntax for an owned module parent."""
    scalar_parent = module.base_ring()
    module.register_action(_ModuleScalarAction(scalar_parent, module, True))
    if scalar_parent in OwnedRings().Commutative():
        module.register_action(_ModuleScalarAction(scalar_parent, module, False))


class ModuleHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):

        return ModuleHomset

    def fixed_category_class_for(self, domain, codomain):
        return domain._module_homset_class()


class ModuleMonoCategoryConstruction(MonoCategoryConstruction):
    r"""The declared monomorphisms of modules over one scalar ring."""

    def fixed_category_class(self):
        return ModuleEmbeddingHomset


class LinearEndCategoryConstruction(EndCategoryConstruction):
    r"""Endomorphism rings for categories enriched in modules."""

    def Of(self, obj, codomain=None):
        if codomain is not None and codomain is not obj:
            raise ValueError("an endomorphism category has equal endpoints")
        if obj not in self.base_category():
            raise TypeError("the endomorphism object must lie in the base category")
        endomorphisms = super().Of(obj)
        endomorphisms.attach_end_family(self)
        if endomorphisms not in OwnedRings():
            raise TypeError("a module endomorphism Hom must be constructed as an owned ring")
        return endomorphisms

    def __contains__(self, candidate) -> bool:
        return hasattr(candidate, "end_family") and candidate.end_family() is self


class ModuleEndCategoryConstruction(LinearEndCategoryConstruction):
    r"""The ring-valued endomorphism family ``M |-> End_R(M)``."""


class ModuleIsoCategoryConstruction(IsoCategoryConstruction):
    r"""Module isomorphisms, with ``Aut_R(M)`` represented by its unit group."""

    def Of(self, domain, codomain=None):
        if codomain is None:
            codomain = domain
        if domain is not codomain:
            return super().Of(domain, codomain)
        if domain not in self.base_category():
            raise TypeError("a module automorphism requires a module in the base category")
        cached = self._cached_between(domain, domain)
        if cached is not None:
            return cached
        result = ModuleAutomorphismGroup(self, domain)
        return self._remember_between(domain, domain, result)


def _is_group_algebra(ring) -> bool:
    r"""Decide whether ``ring`` is an owned group algebra ``R[G]``.

    Read off the ring's own category: constructing ``GroupAlgebras(R)`` to
    ask would need ``Modules(R)``, which may be the category being built.
    """
    from dzack_research.preamble.categories.algebras.group_algebras import GroupAlgebras

    if ring not in OwnedRings():
        return False
    # Sage realizes each category instance in a dynamic subclass, so the
    # placement is recognized by its category class, not by identity.
    return any(isinstance(placement, GroupAlgebras) for placement in ring.category().all_super_categories(proper=False))


class Modules(OwnedCategoryOverBaseRing):
    r"""Modules over a ring, on the owned additive and scalar spines."""

    @staticmethod
    def __classcall__(cls, base_ring, *args, **kwargs):
        r"""``Modules(R[G])`` is the category of modules over a group algebra.

        The owned placement of a group module is the ring it is a module
        over, so the group algebra selects the category class that knows its
        group; every other ring reaches the generic construction.
        """
        if cls is Modules and _is_group_algebra(base_ring):
            from dzack_research.preamble.categories.modules.group_modules.group_modules import (
                ModulesOverGroupAlgebra,
            )

            return ModulesOverGroupAlgebra(base_ring)
        return OwnedCategoryOverBaseRing.__classcall__(cls, base_ring, *args, **kwargs)

    def _augmentation(self, group):
        r"""The augmentation ``epsilon: R[G] -> R``, ``g |-> 1``."""
        return self.base_ring()[group].augmentation()

    def trivial_action(self, group):
        r"""``Triv_G : Modules(R) -> Modules(R[G])``, restriction along the augmentation."""
        return self.restriction_of_scalars(self._augmentation(group))

    def trivial_invariants_adjunction(self, group):
        r"""``Triv_G -| (-)^G``, restriction/coextension along the augmentation."""
        return self.restriction_coextension_adjunction(self._augmentation(group))

    def _call_(self, datum, scalar_action=None):
        r"""Construct the left module defined by ``rho : R -> End_Ab(X)``.

        ``Modules(R)(rho)`` obtains ``X`` from the target Hom endpoints.
        ``Modules(R)(X, rho)`` states those same endpoints explicitly.
        """
        from dzack_research.preamble.categories.modules.general_modules import GeneralModules
        from dzack_research.preamble.owned_category import _object_of

        from dzack_research.preamble.categories.modules.native_modules import _RingModulePresentation

        if isinstance(datum, _RingModulePresentation):
            assert scalar_action is None, "the native presentation already supplies the action"
            return datum.construct(self)
        if scalar_action is None:
            scalar_action = datum
            module = scalar_action.codomain().domain()
        else:
            module = datum
        assert scalar_action.parent().homset_category().is_subcategory(OwnedRings()), (
            "a left module requires a unital ring morphism"
        )
        assert _owned_ring(scalar_action.domain()) is self.base_ring(), f"the scalar action must be a ring morphism out of {self.base_ring()}"
        assert scalar_action.codomain() is AdditiveGroups().AdditiveCommutative().End(module), (
            f"the scalar action must land in the additive endomorphism ring of {module}"
        )
        return _object_of(
            GeneralModules(self.base_ring()),
            base_ring=self.base_ring(),
            rho=scalar_action,
        )

    @cached_method
    def underlying_additive_group_functor(self):
        r"""Return the forgetful functor ``Mod_R -> Ab`` on objects and maps."""
        from dzack_research.preamble.categories.functors.module_additive_groups import (
            UnderlyingAdditiveGroupFunctor,
        )

        return UnderlyingAdditiveGroupFunctor(self)

    # Scalar change along a ring morphism ``f: R -> S``: the adjoint triple
    # ``S tensor_R - -| Res_f -| Hom_R(S, -)``, each functor spelled on its
    # domain category and each adjunction on its left adjoint's domain.

    def scalar_extension(self, ring_map):
        r"""``S tensor_R - : Modules(R) -> Modules(S)`` along ``ring_map: R -> S``."""
        from dzack_research.preamble.categories.functors.scalar_change import (
            _ScalarExtensionFunctor,
        )

        assert _owned_ring(ring_map.domain()) is self.base_ring()
        return _ScalarExtensionFunctor(ring_map)

    def restriction_of_scalars(self, ring_map):
        r"""``Res_f : Modules(S) -> Modules(R)`` along ``ring_map: R -> S``.

        Along the augmentation ``R[G] -> R`` this is the trivial action.
        """
        from dzack_research.preamble.categories.functors.group_actions import (
            _TrivialActionFunctor,
        )
        from dzack_research.preamble.categories.functors.scalar_change import (
            _RestrictionOfScalarsFunctor,
        )

        assert _owned_ring(ring_map.codomain()) is self.base_ring()
        match ring_map:
            case _ if ring_map.is_group_algebra_augmentation():
                return _TrivialActionFunctor(ring_map)
            case _:
                return _RestrictionOfScalarsFunctor(ring_map)

    def coextension_of_scalars(self, ring_map):
        r"""``Hom_R(S, -) : Modules(R) -> Modules(S)`` along ``ring_map: R -> S``."""
        from dzack_research.preamble.categories.functors.scalar_change import (
            _CoextensionOfScalarsFunctor,
        )

        assert _owned_ring(ring_map.domain()) is self.base_ring()
        return _CoextensionOfScalarsFunctor(ring_map)

    def base_change_adjunction(self, ring_map):
        r"""``S tensor_R - -| Res_f`` along ``ring_map: R -> S``."""
        from dzack_research.preamble.categories.functors.scalar_change import (
            _base_change_adjunction,
        )

        assert _owned_ring(ring_map.domain()) is self.base_ring()
        return _base_change_adjunction(ring_map)

    def restriction_coextension_adjunction(self, ring_map):
        r"""``Res_f -| Hom_R(S, -)`` along ``ring_map: R -> S``.

        Along the augmentation ``R[G] -> R`` this is ``Triv_G -| (-)^G``.
        """
        from dzack_research.preamble.categories.functors.group_actions import (
            _TrivialInvariantsAdjunction,
        )
        from dzack_research.preamble.categories.functors.scalar_change import (
            _restriction_coextension_adjunction,
        )

        assert _owned_ring(ring_map.codomain()) is self.base_ring()
        match ring_map:
            case _ if ring_map.is_group_algebra_augmentation():
                return _TrivialInvariantsAdjunction(ring_map)
            case _:
                return _restriction_coextension_adjunction(ring_map)

    class SubcategoryMethods:
        r"""Constructions this category owns, reachable from any subcategory."""

        # Properties of the objects, each an axiom on this category.

        def FinitelyGenerated(self):
            r"""Return this category with the axiom that its objects are finitely generated."""
            return self._with_axiom("FinitelyGenerated")

        def FinitelyPresented(self):
            r"""Return this category with the axiom that its objects are finitely presented."""
            return self._with_axiom("FinitelyPresented")

        def Free(self):
            r"""Return this category with the axiom that its objects are free."""
            return self._with_axiom("Free")

        def Projective(self):
            r"""Return this category with the axiom that its objects are projective."""
            return self._with_axiom("Projective")

        def Torsion(self):
            r"""Return this category with the axiom that its objects are torsion."""
            return self._with_axiom("Torsion")

        # Functors out of ``Mod_R``, each spelled as a method of this, their
        # domain category, and named by the construction it performs.

        def underlying_set(self):
            r"""``U : Mod_R -> Set``, the underlying-set functor.

            The right adjoint of the free-module functor spelled on ``Set``.
            On an object it is the identity: a module already is a set object,
            and forgetting the scalar action removes structure, not elements.
            """
            from dzack_research.preamble.categories.functors.free_forgetful import (
                _underlying_set_functor,
            )

            return _underlying_set_functor(self.base_ring())

        def dualization(self):
            r"""``(-)^* = Hom_R(-, R)``, the contravariant ``R``-linear dualization.

            Which duality this is, is named by the category it is a method of:
            it is the ``R``-linear one, into the free module of rank one.  The
            represented functor has the finitely generated free modules for
            domain and codomain, where the dual basis frames ``M^*``.
            """
            from dzack_research.preamble.categories.functors.linear_constructions import (
                _dualization_functor,
            )

            return _dualization_functor(self.base_ring())

        def symmetric_algebra(self):
            r"""``Sym_R : Mod_R -> CAlg_R``, the symmetric-algebra functor.

            Left adjoint of the underlying-module functor on commutative
            ``R``-algebras; the adjunction is ``symmetric_algebra_adjunction``.
            """
            from dzack_research.preamble.categories.functors.free_algebras import (
                _symmetric_algebra_functor,
            )

            return _symmetric_algebra_functor(self.base_ring())

        def tensor_algebra(self):
            r"""``T_R : Mod_R -> Alg_R``, the tensor-algebra functor.

            Left adjoint of the underlying-module functor on associative unital
            ``R``-algebras; the adjunction is ``tensor_algebra_adjunction``.
            """
            from dzack_research.preamble.categories.functors.free_algebras import (
                _tensor_algebra_functor,
            )

            return _tensor_algebra_functor(self.base_ring())

        def exterior_algebra(self):
            r"""``Lambda_R : Mod_R -> AltAlg_R``, the exterior-algebra functor.

            The alternating quotient of the tensor algebra, graded by the
            exterior powers ``Lambda^n M``.
            """
            from dzack_research.preamble.categories.functors.free_algebras import (
                _alternating_algebra_functor,
            )

            return _alternating_algebra_functor(self.base_ring())

        def divided_power_algebra(self):
            r"""``Gamma_R : Mod_R -> DPAlg_R``, the divided-power algebra functor."""
            from dzack_research.preamble.categories.functors.free_algebras import (
                _divided_power_algebra_functor,
            )

            return _divided_power_algebra_functor(self.base_ring())

        # An adjunction is a method of its left adjoint's domain category.
        # ``Sym_R`` and ``T_R`` are left adjoints out of ``Mod_R``, so their
        # adjunctions are asked for here.  ``Lambda_R`` has none.

        def symmetric_algebra_adjunction(self):
            r"""``Sym_R -| U``, between ``Mod_R`` and commutative ``R``-algebras."""
            from dzack_research.preamble.categories.functors.free_algebras import (
                _symmetric_algebra_adjunction,
            )

            return _symmetric_algebra_adjunction(self.base_ring())

        def tensor_algebra_adjunction(self):
            r"""``T_R -| U``, between ``Mod_R`` and associative unital ``R``-algebras."""
            from dzack_research.preamble.categories.functors.free_algebras import (
                _tensor_algebra_adjunction,
            )

            return _tensor_algebra_adjunction(self.base_ring())

        def bilinear_free_form_adjunction(self):
            r"""Return the free bilinear-form/underlying-module adjunction on ``Mod_R``."""
            from dzack_research.preamble.categories.functors.free_forms import (
                _bilinear_free_form_adjunction,
            )

            return _bilinear_free_form_adjunction(self.base_ring())

        def quadratic_free_form_adjunction(self):
            r"""Return the free quadratic-form/underlying-module adjunction on ``Mod_R``."""
            from dzack_research.preamble.categories.functors.free_forms import (
                _quadratic_free_form_adjunction,
            )

            return _quadratic_free_form_adjunction(self.base_ring())

        def tensor_product(self, factors):
            r"""Return $\bigotimes_{i \in I} M_i$ for an indexed family of modules.

            The tensor product is taken over the index set: its generating set
            is the product of the factors' generating sets over $I$, so a
            generator is a section of that family rather than a nest of pairs.
            """
            family = _finite_factor_family(factors, name="Tensor factors")
            assert all(factor in self for factor in family), (
                "a module tensor product requires modules over one ring"
            )
            return _module_tensor_product(family)

        def _categorical_tensor_product(self, left, right):
            return self.tensor_product((left, right))

        def biproduct(
            self,
            factors,
            *,
            extra_categories=(),
            extra_construction_data=None,
        ):
            r"""Return $\bigoplus_{i \in I} M_i$ for an indexed family of modules.

            The biproduct is taken over the index set: its generating set is
            the coproduct of the factors' generating sets over $I$, so the
            injection and the projection at $i$ are arrows between $M_i$ and
            the one biproduct, not composites through a nested binary one.
            """
            family = _finite_factor_family(factors, name="Biproduct factors")
            assert all(factor in self for factor in family), (
                "a module biproduct requires modules over one ring"
            )
            if extra_categories or extra_construction_data:
                return _module_biproduct_with_data(
                    family,
                    extra_categories=extra_categories,
                    extra_construction_data=extra_construction_data,
                )
            return _module_biproduct(family)

        def _categorical_biproduct(self, left, right):
            return self.biproduct((left, right))

        def product(self, factors):
            r"""Return $\prod_{i \in I} M_i$, which over a finite index set is the biproduct."""
            return self._categorical_product_construction(factors).object()

        def _categorical_product(self, left, right):
            return self._categorical_product_construction((left, right)).object()

        def coproduct(self, factors):
            r"""Return $\coprod_{i \in I} M_i$, which over a finite index set is the biproduct."""
            return self._categorical_coproduct_construction(factors).object()

        def _categorical_coproduct(self, left, right):
            return self._categorical_coproduct_construction((left, right)).object()

        def _categorical_product_construction(self, factors):
            r"""Return the selected finite product cone on the module biproduct."""
            family = _finite_factor_family(factors, name="Product factors")
            assert all(factor in self for factor in family), (
                "a module product requires modules over one ring"
            )
            product = self.biproduct(family)
            diagram = _discrete_diagram(family, self)
            universal_cone = (diagram).ProductCones().cone(
                product,
                lambda index: product.projection(index.value()),
            )

            def factorizer(cone):
                legs = indexed_family(
                    family.index_set(),
                    lambda label: cone.structure_morphism(diagram.domain()(label)),
                    name="Product cone legs",
                )
                return product.from_product_cone(legs)

            return SelectedLimitConstruction(diagram, universal_cone, factorizer)

        def _categorical_coproduct_construction(self, factors):
            r"""Return the selected finite coproduct cocone on the module biproduct."""
            family = _finite_factor_family(factors, name="Coproduct factors")
            assert all(factor in self for factor in family), (
                "a module coproduct requires modules over one ring"
            )
            coproduct = self.biproduct(family)
            diagram = _discrete_diagram(family, self)
            universal_cocone = (diagram).CoproductCocones().cocone(
                coproduct,
                lambda index: coproduct.injection(index.value()),
            )

            def factorizer(cocone):
                legs = indexed_family(
                    family.index_set(),
                    lambda label: cocone.costructure_morphism(diagram.domain()(label)),
                    name="Coproduct cocone legs",
                )
                return coproduct.from_coproduct_cocone(legs)

            return SelectedColimitConstruction(diagram, universal_cocone, factorizer)

        def _categorical_equalizer(self, left_morphism, right_morphism):
            r"""Realize an equalizer in ``R-Mod`` as ``ker(left-right)``."""
            return self._categorical_equalizer_construction(
                left_morphism, right_morphism
            ).object()

        @cached_method
        def _categorical_equalizer_construction(self, left_morphism, right_morphism):
            r"""Realize the selected equalizer cone through ``ker(left-right)``."""
            if (
                left_morphism.domain() not in self
                or left_morphism.codomain() not in self
                or left_morphism.domain() is not right_morphism.domain()
                or left_morphism.codomain() is not right_morphism.codomain()
            ):
                raise ValueError("module equalizer arrows must be parallel R-linear maps")
            equalizer = (left_morphism - right_morphism).kernel()
            inclusion = equalizer.inclusion()
            ambient_modules = Modules(left_morphism.domain().base_ring())
            diagram = _parallel_pair_diagram(
                left_morphism, right_morphism, ambient_modules
            )
            shape = diagram.domain()
            universal_cone = (diagram).Cones().cone(
                equalizer,
                lambda index: (
                    inclusion
                    if index is shape.source()
                    else left_morphism * inclusion
                ),
            )

            def factorizer(cone):
                source_leg = cone.structure_morphism(shape.source())
                source = cone.apex()
                return source.module_category().Mor(source, equalizer)(
                    lambda label: inclusion.lift(
                        source_leg(source.module_generator(label))
                    )
                )

            return SelectedLimitConstruction(diagram, universal_cone, factorizer)

        def _categorical_coequalizer(self, left_morphism, right_morphism):
            r"""Realize a coequalizer in ``R-Mod`` as ``coker(left-right)``."""
            return self._categorical_coequalizer_construction(
                left_morphism, right_morphism
            ).object()

        @cached_method
        def _categorical_coequalizer_construction(self, left_morphism, right_morphism):
            r"""Realize the selected coequalizer cocone through ``coker(left-right)``."""
            if (
                left_morphism.domain() not in self
                or left_morphism.codomain() not in self
                or left_morphism.domain() is not right_morphism.domain()
                or left_morphism.codomain() is not right_morphism.codomain()
            ):
                raise ValueError("module coequalizer arrows must be parallel R-linear maps")
            difference = left_morphism - right_morphism
            raw_coequalizer = difference.cokernel()
            raw_projection = difference.cokernel_projection()

            # A stricter module category may still contain this particular
            # coequalizer even though cokernels do not stay in that category
            # in general.  Over a PID a torsion-free presented quotient is
            # finite free and supplies the actual trivialization.  Use that
            # isomorphic free representative when it lies in ``self`` so the
            # selected colimit is genuinely an object of its stated target
            # category, rather than a merely isomorphic presented module.
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
                _SelectedFinitePresentationModules,
            )

            ring = left_morphism.domain().base_ring()
            coequalizer = raw_coequalizer
            projection = raw_projection
            coequalizer_transport = None
            match raw_coequalizer:
                case _ if raw_coequalizer in self:
                    pass
                case _ if (
                    raw_coequalizer in _SelectedFinitePresentationModules(ring)
                    and ring in PrincipalIdealDomains()
                    and raw_coequalizer.is_torsion_free()
                ):
                    candidate_transport = raw_coequalizer.finite_free_trivialization()
                    if candidate_transport.codomain() in self:
                        coequalizer_transport = candidate_transport
                        coequalizer = candidate_transport.codomain()
                        projection = candidate_transport.forward() * raw_projection

            ambient_modules = Modules(left_morphism.domain().base_ring())
            diagram = _parallel_pair_diagram(
                left_morphism, right_morphism, ambient_modules
            )
            shape = diagram.domain()
            universal_cocone = (diagram).Cocones().cocone(
                coequalizer,
                lambda index: (
                    projection * left_morphism
                    if index is shape.source()
                    else projection
                ),
            )

            def factorizer(cocone):
                target_leg = cocone.costructure_morphism(shape.target())
                target = cocone.apex()
                ambient = left_morphism.codomain()
                raw_factor = raw_coequalizer.module_category().Mor(raw_coequalizer, target)(
                    lambda label: target_leg(ambient.module_generator(label))
                )
                if coequalizer_transport is None:
                    return raw_factor
                return raw_factor * coequalizer_transport.inverse()

            return SelectedColimitConstruction(diagram, universal_cocone, factorizer)

        def _categorical_equalizer_family(self, morphisms):
            r"""Realize a finite wide equalizer through kernels/intersections."""
            size = morphisms.cardinality()
            assert size.is_finite(), (
                "the represented module wide equalizer is taken over a finite arrow family"
            )
            count = int(size.finite_value())
            if count == 0:
                raise ValueError("a wide equalizer family must be nonempty")
            reference = morphisms[0]
            equalizer = self._categorical_equalizer(reference, reference)
            for position in range(1, count):
                equalizer = equalizer.intersection(self._categorical_equalizer(morphisms[position], reference))
            return equalizer

        def _categorical_coequalizer_family(self, morphisms):
            r"""Realize a finite wide coequalizer through images/sums/cokernels."""
            size = morphisms.cardinality()
            assert size.is_finite(), (
                "the represented module wide coequalizer is taken over a finite arrow family"
            )
            count = int(size.finite_value())
            if count == 0:
                raise ValueError("a wide coequalizer family must be nonempty")
            reference = morphisms[0]
            relations = (reference - reference).image()
            for position in range(1, count):
                relations = relations.sum((morphisms[position] - reference).image())
            return relations.inclusion().cokernel()

        def _categorical_product_morphism(self, left_morphism, right_morphism, source, target):
            return left_morphism.biproduct_map(right_morphism, source=source, target=target)

        _categorical_coproduct_morphism = _categorical_product_morphism

    @classmethod
    def _repr_object_names(cls):
        return "modules"

    def an_object(self):
        r"""The free module of rank one, which is the base ring itself."""
        return self.base_ring().free_module(1)

    def super_categories(self):
        return [AdditiveGroups().AdditiveCommutative()]

    def Mor(self, domain, codomain):
        r"""Return the unique Hom-set ``Hom_R(domain,codomain)``."""
        domain = self._hom_endpoint(domain)
        codomain = self._hom_endpoint(codomain)
        if domain not in self or codomain not in self:
            raise TypeError("an R-module Hom requires two R-modules")
        return self.HomCategory().Of(domain, codomain)

    def _hom_endpoint(self, obj):
        r"""Read an ``R[G]``-module over ``R`` by restriction of scalars along ``R -> R[G]``.

        ``Hom_R(M, N)`` for two ``R[G]``-modules is the Hom of their
        restrictions, so the endpoints of this category's Hom are restricted
        before the Hom parent is built.
        """
        if obj in self:
            return obj
        from dzack_research.preamble.categories.algebras.group_algebras import GroupAlgebras

        scalars = obj.base_ring()
        if scalars in GroupAlgebras(self.base_ring()):
            group_modules = Modules(scalars)
            return group_modules.restriction_of_scalars(group_modules.coefficient_inclusion())(obj)
        return obj

    def _hom_parent_placement(self, domain, codomain, *, full_internal_hom=False):
        r"""Return the category chosen when the canonical module Hom is constructed."""

        from dzack_research.preamble.categories.group.additive_homsets import (
            AdditiveEndomorphismRings,
        )

        ring = self.base_ring()
        if ring not in OwnedRings().Commutative():
            center = ring.ring_center()
            placement = [LinearHomModules(center)]
            if domain is codomain:
                placement.append(AdditiveEndomorphismRings(center))
            return Category.join(tuple(placement))
        placement = [InternalHomModules(ring) if full_internal_hom else LinearHomModules(ring)]
        matrix = _coordinate_framed_free_module(domain, ring) and _coordinate_framed_free_module(codomain, ring)
        if matrix:
            placement.append(MatrixSpaces(ring))
            if domain is codomain:
                from dzack_research.preamble.categories.algebras.algebras import (
                    MatrixAlgebras,
                )

                placement.append(MatrixAlgebras(ring))
        elif domain is codomain:
            placement.append(AdditiveEndomorphismRings(ring))
        if full_internal_hom and not matrix:
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
                _SelectedFinitePresentationModules,
            )

            if _represented_finite_presentation(domain) and _represented_finite_presentation(codomain):
                placement.append(_SelectedFinitePresentationModules(ring))
        if full_internal_hom and domain in TensorProductModules(ring):
            factors = domain.tensor_factors()
            if factors.cardinality().is_finite() and int(factors.cardinality().finite_value()) == 2 and factors[0] is factors[1]:
                from dzack_research.preamble.categories.forms.forms import BilinearFormHoms

                placement.append(BilinearFormHoms(ring))
        return Category.join(tuple(placement))

    _HomCategory = ModuleHomCategoryConstruction
    _MonoCategory = ModuleMonoCategoryConstruction
    _IsoCategory = ModuleIsoCategoryConstruction
    _EndCategory = ModuleEndCategoryConstruction

    class ElementMethods:
        def __rmul__(self, scalar):
            r"""Return ring multiplication or the left module scalar action.

            For an algebra/ring viewed also as a module, two elements with the
            same owned ring parent multiply in that ring.  Only an element of
            the module's scalar ring acts through ``R -> End_R(M)``.
            """
            match scalar:
                case _ if element_parent(scalar) is self.parent() and self.parent() in OwnedRings():
                    return scalar._mul_(self)
                case _:
                    return self.parent().scalar_multiple(scalar, self)

    class ParentMethods:
        # The ring acting on this module: the datum this level introduces.
        _preamble_base_ring = None
        _preamble_native_module_presentation = None

        def _native_module_presentation(self):
            r"""The supplied native additive-group realization, or no such realization.

            Protected Modules constructor contract. Only the module entry
            installs it; its scalar/coordinate operations and the algebra
            constructor consume it. It records the complete defining action,
            never a category claim or a deferred reconstruction.
            """
            return self._preamble_native_module_presentation


        def __init__(self, base_ring, **rest) -> None:
            ring = _owned_ring(base_ring)
            self._preamble_base_ring = ring
            super().__init__(base=ring, **rest)

        def __init_extra__(self) -> None:
            r"""Register the action of this module's ring on its own elements.

            A module is an abelian group together with a ring acting on it, so
            recording the ring is only half of what this level constructs; the
            action is the other half, and ``r*m`` is what it is called at a
            prompt.  Sage calls this hook from ``Parent.__init__`` for every
            parent of this category, whatever route constructed it, so one
            declaration here reaches a module built through the chain and a
            ring the preamble adopts alike, and neither has anything to state
            about its scalars afterwards.
            """
            _register_module_scalar_action(self)

        def Mor(self, codomain, category=None):
            modules = Modules(self.base_ring())
            if category is None:
                return modules.Mor(self, codomain)
            return _category_homset(category, self, codomain)

        def Mono(self, codomain):
            r"""Return the declared injective linear maps into ``codomain``."""
            return Modules(self.base_ring()).Mono(self, codomain)

        def End(self):
            r"""Return ``End_R(M)``, the endomorphism ring of this module."""
            return Modules(self.base_ring()).End(self)

        def Aut(self):
            r"""Return ``Aut_R(M)``, the automorphisms of this module.

            The Hom packet gives every object its automorphisms, so a module
            reaches them the way a group and a lattice already do rather than
            through a class of its own.
            """
            return Modules(self.base_ring()).Aut(self)

        def module_category(self):
            return Modules(self.base_ring())

        def pairings_with(self, right_module, value_module):
            r"""Return bilinear pairings ``self x right_module -> value_module``."""
            from dzack_research.preamble.categories.forms.forms import _pairings

            return _pairings(self, right_module, value_module)

        def bilinear_forms(self, value_module):
            r"""Return bilinear forms ``self x self -> value_module``."""
            from dzack_research.preamble.categories.forms.forms import _bilinear_forms

            return _bilinear_forms(self, value_module)

        def quadratic_forms(self, value_module):
            r"""Return quadratic forms ``self -> value_module`` through ``Gamma^2(self)``."""
            from dzack_research.preamble.categories.forms.forms import _quadratic_forms

            return _quadratic_forms(self, value_module)

        def quadratic_map(self, value_module, function):
            r"""Return the quadratic map classified by ``function``."""
            from dzack_research.preamble.categories.forms.forms import _quadratic_map

            return _quadratic_map(self, value_module, function)

        def quadratic_map_from_morphism(self, morphism):
            r"""Recover the quadratic map classified by a map out of ``Gamma^2(self)``."""
            from dzack_research.preamble.categories.forms.forms import (
                _quadratic_map_from_morphism,
            )

            return _quadratic_map_from_morphism(self, morphism)

        def equip_bilinear_form(self, value_module, datum):
            r"""Return this module construction equipped with the selected bilinear form."""
            from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
                _bilinear_form,
            )

            return _bilinear_form(self, value_module, datum)

        def equip_quadratic_form(self, value_module, datum):
            r"""Return this module construction equipped with the selected quadratic form."""
            from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
                _quadratic_form,
            )

            return _quadratic_form(self, value_module, datum)

        def tensor_algebra(self):
            r"""Return the tensor algebra ``T_R(self)``."""
            return self.module_category().tensor_algebra()(self)

        def mixed_tensor_algebra(self):
            r"""Return ``T(self) tensor T(self^*)`` with finite bidegree support."""
            from dzack_research.preamble.tensors.tensor import MixedTensorAlgebraParent

            return MixedTensorAlgebraParent(self)

        def symmetric_algebra(self):
            r"""Return the symmetric algebra ``Sym_R(self)``."""
            return self.module_category().symmetric_algebra()(self)

        def exterior_algebra(self):
            r"""Return the exterior algebra ``Lambda_R(self)``."""
            return self.module_category().exterior_algebra()(self)

        def divided_power_algebra(self):
            r"""Return the divided-power algebra ``Gamma_R(self)``."""
            return self.module_category().divided_power_algebra()(self)

        def tensor_to_symmetric(self):
            r"""Return the canonical quotient ``T(self) -> Sym(self)``."""
            from dzack_research.preamble.categories.algebras.comparison_maps import (
                _tensor_to_symmetric,
            )

            return _tensor_to_symmetric(self)

        def tensor_to_alternating(self):
            r"""Return the canonical quotient ``T(self) -> Lambda(self)``."""
            from dzack_research.preamble.categories.algebras.comparison_maps import (
                _tensor_to_alternating,
            )

            return _tensor_to_alternating(self)

        def symmetric_to_divided(self):
            r"""Return the canonical comparison ``Sym(self) -> Gamma(self)``."""
            from dzack_research.preamble.categories.algebras.comparison_maps import (
                _symmetric_to_divided,
            )

            return _symmetric_to_divided(self)

        def divided_to_symmetric(self):
            r"""Return ``Gamma(self) -> Sym(self)`` when the factorials are invertible."""
            from dzack_research.preamble.categories.algebras.comparison_maps import (
                _divided_to_symmetric,
            )

            return _divided_to_symmetric(self)

        def connections(self):
            r"""Return the space of algebraic connections on this module."""
            from dzack_research.preamble.categories.modules.connections import (
                _connections,
            )

            return _connections(self)

        def determinant_line(self):
            r"""Return ``det(self) = Lambda^rank(self) self``."""
            from dzack_research.preamble.categories.modules.hodge import (
                _determinant_line,
            )

            return _determinant_line(self)

        def exterior_forms(self, degree):
            r"""Return ``Lambda^degree(self^vee)``."""
            from dzack_research.preamble.categories.modules.hodge import (
                _exterior_forms,
            )

            return _exterior_forms(self, degree)

        def volume_trivialization(self, forward, inverse):
            r"""Return the stated isomorphism ``det(self) ~= R``."""
            from dzack_research.preamble.categories.modules.hodge import (
                _volume_trivialization,
            )

            return _volume_trivialization(self, forward, inverse)

        def framing_volume_trivialization(self, unit=None):
            r"""Trivialize ``det(self)`` using the selected framing."""
            from dzack_research.preamble.categories.modules.hodge import (
                _framing_volume_trivialization,
            )

            return _framing_volume_trivialization(self, unit=unit)

        def poincare_duality(self, volume, degree):
            r"""Return Poincare duality in exterior degree ``degree``."""
            from dzack_research.preamble.categories.modules.hodge import (
                _poincare_duality,
            )

            return _poincare_duality(self, volume, degree)

        def divided_square(self):
            r"""Return ``Gamma^2_R(self)``, the universal target for quadratic maps."""
            from dzack_research.preamble.categories.modules.powers import _divided_square

            return _divided_square(self)

        def tensor_power(self, degree):
            r"""Return ``self^{tensor degree}``."""
            from dzack_research.preamble.categories.modules.powers import _tensor_power

            return _tensor_power(self, degree)

        def symmetric_power(self, degree):
            r"""Return ``Sym^degree(self)``."""
            from dzack_research.preamble.categories.modules.powers import _symmetric_power

            return _symmetric_power(self, degree)

        def exterior_power(self, degree):
            r"""Return ``Lambda^degree(self)``."""
            from dzack_research.preamble.categories.modules.powers import _alternating_power

            return _alternating_power(self, degree)

        def divided_power_module(self, degree):
            r"""Return the divided-power module ``Gamma^degree(self)``."""
            from dzack_research.preamble.categories.modules.powers import _divided_power

            return _divided_power(self, degree)

        def tensor_power_permutation(self, degree, positions):
            r"""Return the endomorphism permuting the factors of ``self^tensor degree``."""
            from dzack_research.preamble.categories.modules.powers import (
                _tensor_power_permutation,
            )

            return _tensor_power_permutation(self, degree, positions)

        def divided_power_product(self, left_degree, left, right_degree, right):
            r"""Multiply homogeneous divided powers of ``self``."""
            from dzack_research.preamble.categories.modules.powers import (
                _divided_power_product,
            )

            return _divided_power_product(
                self, left_degree, left, right_degree, right
            )

        def exterior_power_product(self, left_degree, left, right_degree, right):
            r"""Multiply homogeneous exterior powers of ``self`` by the wedge product."""
            from dzack_research.preamble.categories.modules.powers import (
                _alternating_power_product,
            )

            return _alternating_power_product(
                self, left_degree, left, right_degree, right
            )

        def divided_power_element(self, degree, element):
            r"""Return ``gamma_degree(element)`` in ``Gamma^degree(self)``."""
            from dzack_research.preamble.categories.modules.powers import (
                _divided_power_element,
            )

            return _divided_power_element(self, degree, element)

        def divided_power_invariant_inclusion(self, degree):
            r"""Return ``Gamma^degree(self) -> self^tensor degree`` by orbit sum."""
            from dzack_research.preamble.categories.modules.powers import (
                _divided_power_invariant_inclusion,
            )

            return _divided_power_invariant_inclusion(self, degree)

        def tensor_power_polarization(self, degree):
            r"""Return ``self^tensor degree -> Gamma^degree(self)`` by polarization."""
            from dzack_research.preamble.categories.modules.powers import (
                _tensor_power_polarization,
            )

            return _tensor_power_polarization(self, degree)

        def divided_square_invariant_inclusion(self):
            r"""Return the degree-two divided-power invariant inclusion."""
            return self.divided_power_invariant_inclusion(2)

        def tensor_square_polarization(self):
            r"""Return the degree-two tensor polarization map."""
            return self.tensor_power_polarization(2)

        def _module_homset_class(self):
            r"""Return the canonical fixed homset for maps out of this module type."""

            return ModuleHomset

        def base_ring(self):
            r"""Return the ring acting on this module.

            A module constructed through this level stores its ring; a parent
            refined into ``Modules(R)`` without running this level reads the
            ring it was built over.
            """
            match self._preamble_base_ring:
                case None:
                    return _owned_ring(self.base())
                case ring:
                    return ring

        def is_module(self) -> bool:
            return True

        def is_free(self) -> bool:
            return False

        def is_finitely_generated(self) -> bool:
            return False

        def is_framed_module(self) -> bool:
            return False

        def is_finite(self):
            return Unknown

        def is_flat(self) -> bool:
            r"""Decide flatness in the field and PID regimes.

            Every module over a field is flat.  Over a PID, flatness is
            equivalent to torsion-freeness (Stacks Project, Tag 0AUW), so the
            torsion-freeness decision of the module decides it.
            """

            ring = self.base_ring()
            match ring:
                case _ if ring in OwnedFields():
                    return True
                case _ if ring in PrincipalIdealDomains():
                    return bool(self.is_torsion_free())
                case _:
                    raise AssertionError(
                        f"flatness is decided over a field or a principal ideal domain, and {ring} is neither"
                    )

        @abstract_method
        def base_change(self, ring_map):
            r"""Return ``S tensor_R M`` along ``ring_map : R -> S``.

            Every module has a scalar extension; each representation of modules
            constructs it on its own data.
            """
            ...

        def vector_space(self):
            r"""Return ``M tensor_R Frac(R)`` along the canonical fraction-field map."""
            return self.base_change(self.base_ring().fraction_field_map())

        def _represented_fiber_dimension(self, point):
            _ = point
            return NotImplemented

        def _free_biproduct_over(
            self,
            labels,
            factors,
            *,
            extra_categories=(),
            extra_construction_data=None,
        ):
            _ = (labels, factors, extra_categories, extra_construction_data)
            return NotImplemented

        def _presented_biproduct_over(
            self,
            labels,
            factors,
            *,
            extra_categories=(),
            extra_construction_data=None,
        ):
            _ = (labels, factors, extra_categories, extra_construction_data)
            return NotImplemented

        def _presented_module_from_relation_rows(
            self,
            labels,
            rows,
            *,
            extra_categories=(),
            extra_construction_data=None,
        ):
            _ = (labels, rows, extra_categories, extra_construction_data)
            return NotImplemented

        def _selected_presentation_rows(self):
            return None

        def _selected_module_coefficients(self, element):
            r"""Read the coordinates of ``element`` in the selected framing.

            Protected contract of ``Modules(R)``: the one caller is
            :meth:`framing_coefficients`, and a level whose elements are not
            stored as their own finite support in the framing -- a localized
            module, a quotient, a restriction of scalars -- implements it for
            the representation it constructs.  It takes an element of this
            module and returns the finite-support coefficients, keyed by the
            labels of ``module_generating_set()``.  The default reads an
            element that stores its own finite support.
            """
            return dict(element.monomial_coefficients())

        def framing_coefficients(self, element):
            r"""Return the finite-support coefficients in this module's selected framing.

            The framing is the mathematical owner of this coordinate map. In
            particular, facade elements such as number-field order elements may
            have a different concrete Sage parent without changing which module
            supplies their selected coefficients.
            """
            native = self._native_module_presentation()
            if native is not None and native.basis() is not None:
                return native.coefficients(element)
            match self:
                case _ if self in OwnedOrders():
                    # The selected integral basis of an order: the engine
                    # reads coordinates in that basis, one per framing label.
                    labels = self.module_generating_set()
                    engine = _engine_ring(self)
                    backend_element = _engine_element(self, element)
                    coordinates = (
                        (SageZZ(backend_element),)
                        if engine is SageZZ
                        else tuple(engine.coordinates(backend_element))
                    )
                    base = self.base_ring()
                    base_engine = _engine_ring(base)
                    return {
                        label: base._from_engine_element(base_engine(coefficient))
                        for label, coefficient in zip(labels, coordinates, strict=True)
                        if coefficient != 0
                    }
                case _:
                    return self._selected_module_coefficients(element)

        def _represented_kernel_of_morphism(self, morphism):
            _ = morphism
            return NotImplemented

        def _represented_cokernel_of_morphism(self, morphism):
            _ = morphism
            return NotImplemented

        def _represented_annihilator_ideal(self):
            return NotImplemented

        def _represented_vector_space_dimension(self):
            return NotImplemented

        def _represented_vector_space_basis_generator_labels(self):
            return NotImplemented

        def _owned_scalar_multiple(self, scalar, element):
            r"""Apply the owned scalar action to an owned module element."""
            native = self._native_module_presentation()
            if native is not None:
                return native.scalar_multiple(scalar, element)
            if element not in self:
                raise TypeError(f"{element} is not an element of {self}")
            scalar = self.base_ring()(scalar)
            return element._lmul_(scalar)

        def underlying_additive_group(self):
            r"""Return the additive group on which this module's scalars act."""
            return self

        def _underlying_additive_element(self, element):
            r"""Element map used by scalar evaluation and the forgetful functor.

            Module representations with a distinct underlying additive group
            implement this protected conversion together with
            ``underlying_additive_group``.  An ``R[G]``-module built on the
            data of ``M`` has the underlying additive group of ``M``, and its
            :meth:`_element_of_unformed_module` reads an element there.
            """
            return self(element)

        def unformed_module(self):
            r"""Return the module this module is built on.

            A form or a group action stated on an ``R``-module ``M`` builds a
            module on the data of ``M`` that retains ``M`` (``CON-16``); the
            level stating that structure answers ``M`` here.  A module on
            which no structure was stated is built on its own data.
            """
            return self

        def _element_of_unformed_module(self, element):
            r"""Read an element of this module in :meth:`unformed_module`.

            Protected contract of ``Modules(R)``.  Every level whose
            constructor retains the module its structure was stated on
            implements it together with :meth:`_element_from_unformed_module`;
            its one caller is :meth:`_element_on_the_same_data`.  It takes an
            element of this module and returns the element of
            ``unformed_module()`` on the same data.
            """
            assert self.unformed_module() is self, (
                f"{self} retains {self.unformed_module()} and states no reading of its elements there"
            )
            return element

        def _element_from_unformed_module(self, element):
            r"""Read an element of :meth:`unformed_module` in this module.

            The inverse half of :meth:`_element_of_unformed_module`, with the
            same owner, implementers and caller.
            """
            assert self.unformed_module() is self, (
                f"{self} retains {self.unformed_module()} and states no reading of its elements here"
            )
            return element

        def _module_with_structure(self, categories, construction_data):
            r"""Construct further structure on this exact module's data.

            The module owner, not the stronger algebra/form/action owner,
            selects its realization.  A realization with additional intrinsic
            data (for example a direct sum's pieces) supplies this operation.
            """
            match self:
                case _ if self in ModulesWithChosenFinitePresentation(self.base_ring()):
                    return self._same_presentation_module(
                        self.module_generating_set(), _extra_categories=categories,
                        _extra_construction_data=construction_data,
                    )
                case _ if _is_framed_free_module(self):
                    return self._fresh_free_module_on(
                        self.module_generating_set(), _extra_categories=categories,
                        _extra_construction_data=construction_data,
                    )
                case _:
                    from dzack_research.preamble.categories.modules.general_modules import GeneralModules
                    from dzack_research.preamble.owned_category import _object_of

                    return _object_of(
                        Category.join((GeneralModules(self.base_ring()), *categories)),
                        base_ring=self.base_ring(), rho=self.scalar_action(),
                        verify=False, **construction_data,
                    )

        def _built_on_the_same_data(self, source) -> bool:
            r"""Decide whether ``source`` and this module are built on the data of one module.

            That holds when ``source`` retains this module, this module
            retains ``source``, or both retain the same module.  It is asked
            of the parent of an element, by its membership in ``Modules`` over
            its own ring and by the identity of the retained modules.
            """
            ring = source.base_ring()
            if ring not in OwnedRings() or source not in Modules(ring):
                return False
            retained = source.unformed_module()
            return (
                retained is self
                or self.unformed_module() is source
                or self.unformed_module() is retained
            )

        def _element_on_the_same_data(self, source, element):
            r"""Read an element of ``source`` as the element of this module on the same data.

            The dispatcher of the protected pair
            :meth:`_element_of_unformed_module` and
            :meth:`_element_from_unformed_module`, called from an element
            constructor once :meth:`_built_on_the_same_data` holds.  A module
            built on the data of ``M`` has no identification morphism back to
            ``M`` (``CON-16``), and Sage's registered conversions do not reach
            these parents: their ``__call__`` goes straight to
            ``_element_constructor_`` because the generic conversion map Sage
            would build (``Parent.discover_convert_map_from``,
            ``sage/structure/parent.pyx``) takes its homset in
            ``SetsWithPartialMaps``, which owned parents are not in.  So the
            level that retains the module declares the reading, and the
            receiving constructor asks the element's parent for it.
            """
            if source.unformed_module() is self:
                return source._element_of_unformed_module(element)
            if self.unformed_module() is source:
                return self._element_from_unformed_module(element)
            assert source.unformed_module() is self.unformed_module(), (
                f"{source} and {self} are not built on the data of one module"
            )
            return self._element_from_unformed_module(
                source._element_of_unformed_module(element)
            )

        @cached_method
        def _ring_morphism_defining_module_action(self):
            r"""Return ``rho_M : R -> End_Ab(U(M))``, ``r |-> (m |-> r m)``, from the scalar multiplication.

            A module whose datum is ``rho`` itself states it at its own level.
            """
            ring = self.base_ring()
            endomorphisms = AdditiveGroups().AdditiveCommutative().End(self.underlying_additive_group())

            return ring.Mor(endomorphisms)(
                lambda scalar: endomorphisms.elementwise(
                    lambda element: self._owned_scalar_multiple(scalar, element),
                ),
            )

        def scalar_action(self):
            return self._ring_morphism_defining_module_action()

        def annihilator(self):
            r"""Return ``Ann_R(M)=ker(R -> End_R(M))``.

            The kernel is read from the presentation of this module rather
            than from the morphism, which has no route to it: an ideal of
            ``R`` cut out by a condition on ``End_R(M)`` is not something a
            ring morphism can contract.
            """
            represented = self._represented_annihilator_ideal()
            assert represented is not NotImplemented, (
                f"the annihilator of {self} has no represented computation"
            )
            return represented

        @cached_method
        def generic_fibre_map(self):
            r"""Return the unit ``M -> K tensor_R M`` of scalar extension to ``Frac(R)``."""
            ring = self.base_ring()
            assert ring in IntegralDomains(), (
                f"the generic fibre of a module over {ring} needs an integral-domain base"
            )
            return Modules(ring).base_change_adjunction(ring.fraction_field_map()).unit(self)

        def torsion_submodule(self):
            r"""Return ``Tor(M) = ker(M -> K tensor_R M)`` over an integral domain.

            An element is torsion exactly when some nonzero scalar kills it, and
            over a domain that is exactly when it dies in the generic fibre: the
            unit of scalar extension along ``R -> K`` inverts every nonzero
            scalar and nothing else.  So the torsion submodule is that unit's
            kernel, computed as a kernel rather than read off a decomposition
            that only a principal ideal domain supplies.
            """
            return self.generic_fibre_map().kernel()

        def is_torsion_free(self) -> bool:
            r"""Return whether ``Tor(M)=0``, that is whether ``M -> K tensor_R M`` is injective."""
            return self.generic_fibre_map().is_injective()

        def scalar_multiple(self, scalar, element):
            r"""Return ``r*m = rho_M(r)(m)``."""
            underlying = self._underlying_additive_element(element)
            return self(self.scalar_action()(self.base_ring()(scalar))(underlying))

        def dual_module(self):
            r"""Return the linear dual ``Hom_R(M, R)`` over a commutative ring.

            For left modules over a noncommutative ring, ``Hom_R(M,R)`` is
            naturally a right module and therefore is not an object of this
            left-module category without a separate bimodule/opposite-ring
            construction.  The commutative case is the internal Hom into the
            regular rank-one module and inherits its selected presentation
            whenever the endpoint data represent one.
            """
            ring = self.base_ring()
            if ring not in OwnedRings().Commutative():
                raise TypeError(
                    "the represented left-module dual requires a commutative base ring"
                )
            return self.module_category().Mor(self, ring.regular_module())

        def restrict_scalars(self, ring_map):
            r"""Read this module over the domain of ``ring_map``."""
            return _restricted_scalars_view(self, ring_map)

        def twist_scalar_action(self, ring_endomorphism):
            r"""Twist this module's scalar action along an endomorphism ``R -> R``.

            This is restriction of scalars along an endomorphism of the scalar
            ring; it is unrelated to ``L.twist(a)``, which rescales a lattice
            form while leaving its scalar action unchanged.
            """
            ring = _engine_ring(self.base_ring())
            if (
                _engine_ring(ring_endomorphism.domain()) is not ring
                or _engine_ring(ring_endomorphism.codomain()) is not ring
            ):
                raise ValueError(
                    "a scalar-action twist is specified by an endomorphism of the module's base ring"
                )
            return self.restrict_scalars(ring_endomorphism)

        def localize(self, *datum):
            r"""Return ``S^{-1}M`` by scalar extension to ``S^{-1}R``.

            ``datum`` may be a represented localization ring, a represented
            submonoid ``S <= (R,*)``, or the finite generators used by the
            ring-localization convenience API.
            """
            ring = self.base_ring()
            if len(datum) == 1 and datum[0] in LocalizationRings():
                localization_ring = datum[0]
                if localization_ring.localization_source() is not ring:
                    raise ValueError("the localization ring has the wrong source ring")
            else:
                localization_ring = ring.localization(*datum)
            return localization_ring.localize_module(self)

        localization = localize

        def localize_at_prime(self, prime):
            r"""Return the localized module ``M_p`` at a represented prime."""
            ring = self.base_ring()
            if self is ring:
                return ring.localize_at_prime(prime)
            localization_ring = ring.spectrum()(prime).local_ring()
            return self.localize(localization_ring)

        localization_at_prime = localize_at_prime

    class FinitelyGenerated(CategoryWithAxiom):
        r"""Modules admitting a finite generating set."""

        def an_object(self):
            r"""The free module of rank one."""
            return self.base_ring().free_module(1)

        class ParentMethods:
            def is_finitely_generated(self) -> bool:
                return True

            @cached_method
            def fiber(self, point):
                r"""Return ``M(p)=M tensor_R kappa(p)`` at ``p in Spec(R)``."""
                ring = self.base_ring()
                if point.parent().ring() is not ring:
                    raise ValueError("a module fiber requires a point of Spec(base_ring)")
                localized = self.localize_at_prime(point)
                fiber = localized.base_change(point.local_ring().residue_map())
                residue = point.residue_field()
                assert fiber in VectorSpaces(residue), (
                    "base change to a residue field constructs a vector space"
                )
                return fiber

            def fiber_dimension(self, point):
                r"""Return ``dim_{kappa(p)} M(p)`` when the finite fiber is represented."""
                return self.fiber(point).dimension()

            def rank_at(self, point):
                r"""Return the local fiber rank ``dim_{kappa(p)} M(p)``."""
                return self.fiber_dimension(point)

            def rank_function(self):
                r"""Return ``r_M : Spec(R) -> NN``, ``p |-> dim_{kappa(p)} M(p)``.

                A module that is not locally free has no rank; it has a rank at
                each point, and those values vary.  So the rank of a finitely
                generated module is a function on the spectrum, and this returns
                that function as a morphism of sets: it composes with maps of
                spectra, restricts to a subset, and is the object whose fibres are
                the rank strata, rather than a number a caller recomputes at every
                point.

                This is a different invariant from the generic rank, which is one
                value of it, and from the local free rank of a finite projective
                module, which is this function where it is locally constant.
                """
                return Sets().Mor(self.base_ring().spectrum(), NN)(self.rank_at)

            def local_number_of_generators(self, point):
                r"""Return the minimal number of generators of ``M_p`` by Nakayama."""
                return self.localize_at_prime(point).minimal_number_of_generators()

            def local_minimal_generators(self, point):
                r"""Return a selected minimal generating set of ``M_p`` when represented."""
                return self.localize_at_prime(point).minimal_module_generators()

            def residue_module(self):
                r"""Return ``M/mM = M tensor_R k`` for a represented local base ring."""

                ring = self.base_ring()
                if ring not in LocalRings():
                    raise TypeError("the residue module is defined here for modules over a local ring")
                residue = ring.residue_field()
                module = self.base_change(ring.residue_map())
                if module not in VectorSpaces(residue):
                    raise TypeError("base change to a residue field must construct a vector space")
                return module

            def minimal_number_of_generators(self):
                r"""Return ``dim_k(M/mM)`` for a finite module over a local ring."""

                ring = self.base_ring()
                if ring not in LocalRings():
                    raise TypeError("minimal generator counts via Nakayama require a represented local base ring")
                return self.residue_module().dimension()

            def generic_rank(self):
                r"""Return ``dim_K(M tensor_R K)`` for an integral-domain base ``R``."""

                ring = self.base_ring()
                if ring not in IntegralDomains():
                    raise TypeError("generic rank is defined here over an integral domain")
                return self.fiber_dimension(ring.spectrum().generic_point())

            def is_torsion(self) -> bool:
                r"""Return whether ``K tensor_R M = 0`` over an integral domain.

                The generic fibre is a vector space over ``K``, so it vanishes
                exactly when its dimension does.  A free module of positive rank is
                therefore not torsion, whatever its relations look like.
                """
                return self.generic_rank() == 0

    class FinitelyPresented(CategoryWithAxiom):
        r"""Modules admitting a finite presentation."""

        def an_object(self):
            r"""The free module of rank one, presented by no relations."""
            return self.base_ring().free_module(1)

        def extra_super_categories(self):
            return [Modules(self.base_ring()).FinitelyGenerated()]

        def biproduct_bifunctor(self):
            r"""Return the biproduct bifunctor on finitely presented modules."""
            from dzack_research.preamble.categories.functors.linear_constructions import (
                _biproduct_bifunctor,
            )

            return _biproduct_bifunctor(self.base_ring())

        def cokernel_arrow_functor(self):
            r"""Return the cokernel functor on this module arrow category."""
            from dzack_research.preamble.categories.functors.linear_constructions import (
                _cokernel_arrow_functor,
            )

            return _cokernel_arrow_functor(self.base_ring())

        class ParentMethods:
            def is_finitely_presented(self) -> bool:
                return True

            def tor(self, other, degree=0):
                r"""Return ``Tor_degree(self, other)`` from the selected free resolution."""
                from dzack_research.preamble.categories.modules.derived_functors import _tor

                return _tor(self, other, degree=degree)

            def ext(self, other, degree=0):
                r"""Return ``Ext^degree(self, other)`` from the selected free resolution."""
                from dzack_research.preamble.categories.modules.derived_functors import _ext

                return _ext(self, other, degree=degree)

            def projective_dimension(self):
                r"""Return the projective dimension in the regimes where it is decided exactly.

                A projective module has dimension zero.  Over a principal ideal
                domain every submodule of a free module is free, so every finitely
                presented module has projective dimension at most one; a
                nonprojective one therefore has dimension exactly one.  No finite
                bound is inferred over a more general ring.
                """
                if self.is_projective():
                    return 0
                assert self.base_ring() in PrincipalIdealDomains(), (
                    "projective dimension beyond the projective and PID regimes "
                    "requires a represented finite resolution bound"
                )
                return 1

        class Torsion(CategoryWithAxiom):
            r"""Finitely presented torsion modules over a PID."""

            def an_object(self):
                r"""The discriminant group of U."""
                from dzack_research.preamble.categories.lattices import Lattices

                return Lattices(self.base_ring())("U").discriminant_group()

            def _call_(self, presentation):
                module = presentation.cokernel()
                if module.base_ring() is not self.base_ring():
                    raise ValueError("a torsion presentation belongs to its coefficient ring")
                return _refine_finitely_presented_torsion_module(module)

            class ParentMethods:
                def is_torsion(self) -> bool:
                    return True

                def invariants(self):
                    r"""Return the invariant factors of this finite presented torsion module."""
                    return self.invariant_factors()

                @cached_method
                def elements(self):
                    r"""Return all elements through the private finite Smith workspace."""

                    assert _engine_ring(self.base_ring()) is SageZZ, (
                        "finite torsion enumeration is represented here in the ZZ Smith specialization"
                    )
                    engine = self._smith_engine()
                    assert engine is not None, (
                        "finite torsion enumeration requires the represented Smith workspace"
                    )
                    positions = Sets.Δ[int(engine.cardinality()) - 1]
                    return FiniteOrderedSets().from_indexed(
                        positions,
                        lambda position: self._from_smith_engine_element(
                            engine[int(position)]
                        ),
                        name="Finite torsion elements",
                    )

                def __iter__(self):
                    return iter(self.elements())

            def direct_sum_of_cyclics(self, orders):
                r"""Return ``\bigoplus_i R/(a_i)`` for the selected nonzero scalars.

                Over ``ZZ`` the ``a_i`` are the usual cyclic-group orders.  Over a
                general PID the same diagonal presentation is the invariant-factor
                construction; unit entries contribute zero summands, as they should.
                A zero entry would contribute a free copy of ``R`` and hence would not
                define an object of the torsion category.
                """
                ring = self.base_ring()
                assert ring in PrincipalIdealDomains(), (
                    "direct sums of cyclic torsion modules require a represented PID"
                )
                orders = tuple(ring(order) for order in orders)
                if any(order == ring.zero() for order in orders):
                    raise ValueError("a cyclic torsion summand requires a nonzero relation scalar")
                orders = tuple(order for order in orders if not order.is_unit())
                size = len(orders)

                relations = ring.matrix_space(size, size).from_rows(
                    tuple(
                        tuple(
                            order if row == column else ring.zero()
                            for column in range(size)
                        )
                        for row, order in enumerate(orders)
                    )
                )
                return _torsion_module_presented_by_matrix(relations, base_ring=ring)

            def from_abelian_group(self, group):
                r"""Return a finite abelian group as a torsion ``ZZ``-module presentation.

                The selected group generators remain the module-generator labels.  In
                particular a represented ``C_2 x C_3`` remains a two-generator object;
                it is not silently replaced by an isomorphic one-generator ``C_6``.
                Relations are the complete kernel of the map from the free abelian
                group on those selected generators, found inside the finite box cut out
                by their individual orders and reduced to Hermite row normal form.
                """
                assert _engine_ring(self.base_ring()) is SageZZ, (
                    "finite abelian groups are represented here as ZZ-torsion modules"
                )
                if not group.is_finite():
                    raise ValueError("a torsion-module crossing requires a finite group")
                additive = group.category().is_subcategory(CommutativeAdditiveGroups())
                if not additive:
                    commutative = group.category().is_subcategory(SageGroups().Commutative())
                    if not commutative and not bool(group.is_abelian()):
                        raise ValueError("a ZZ-module crossing requires an abelian group")

                generators = tuple(group.group_generators())
                ring = self.base_ring()
                if not generators:
                    return _torsion_module_presented_by_matrix(
                        engine_matrix(SageZZ, 0, 0),
                        finite_ordered_set(()),
                        base_ring=ring,
                    )
                orders = tuple(int(generator.order()) for generator in generators)
                search_size = prod(orders)
                assert search_size <= 10**6, (
                    "exact relation enumeration uses the selected generator-order box only up to size 10^6; "
                    "larger groups require a represented finite presentation"
                )

                if additive:
                    identity = group.zero()

                    def combine(exponents):
                        return sum(
                            (exponent * generator for exponent, generator in zip(exponents, generators, strict=True)),
                            identity,
                        )
                else:
                    identity = group.one()

                    def combine(exponents):
                        return prod(
                            (generator**exponent for exponent, generator in zip(exponents, generators, strict=True)),
                            identity,
                        )

                relation_rows = [
                    exponents
                    for exponents in itertools.product(*(range(order) for order in orders))
                    if combine(exponents) == identity
                ]
                relation_rows.extend(
                    tuple(order if row == column else 0 for column in range(len(orders)))
                    for row, order in enumerate(orders)
                )
                relations = engine_matrix(SageZZ, relation_rows)
                reduced = _row_normal_form(relations, include_zero_rows=True)
                full_rank_rows = reduced.matrix_from_rows(tuple(range(len(generators))))
                return _torsion_module_presented_by_matrix(
                    full_rank_rows,
                    finite_ordered_set(generators),
                    base_ring=ring,
                )

    class Free(CategoryWithAxiom):
        r"""Modules admitting a basis."""

        def an_object(self):
            r"""The free module of rank one."""
            return self.base_ring().free_module(1)

        def extra_super_categories(self):
            return [Modules(self.base_ring()).Projective()]

        class ParentMethods:
            def is_free(self) -> bool:
                return True

    class Projective(CategoryWithAxiom):
        r"""Direct summands of free modules."""

        _certifying_predicate = "is_projective"

        def an_object(self):
            r"""The free module of rank one, which is projective."""
            return self.base_ring().free_module(1)

        class ParentMethods:
            def is_projective(self) -> bool:
                return True

            def projective_rank(self, point):
                r"""Return the local free rank of a finite projective module at ``point``."""
                if self not in Modules(self.base_ring()).FinitelyGenerated():
                    raise TypeError("projective_rank currently requires a finite projective module")
                return self.fiber_dimension(point)

            def local_free_trivialization(self, point):
                r"""Return the isomorphism ``R_p^r -> M_p`` at a point of the spectrum.

                By Nakayama a family whose images span the fibre ``M(p)`` generates
                ``M_p``, and a projective module is free there, so a family of that
                size generating a free module of that rank is a basis.  The
                residue field already selects such a family among the chosen
                generators, so the trivialization is the map carrying the standard
                basis to it, and it is an isomorphism rather than merely a
                surjection because the ranks agree.
                """


                localized = self.localize_at_prime(point)
                labels = localized.residue_module().basis_generator_labels()
                free = localized.base_ring().free_module(labels)
                return free.module_category().Mor(free, localized)(
                    lambda label: localized.module_generator(label)
                )

    class Torsion(CategoryWithAxiom):
        r"""Modules whose generic fibre vanishes."""

        _certifying_predicate = "is_torsion"

        def an_object(self):
            r"""The discriminant group of U, which is torsion."""
            from dzack_research.preamble.categories.lattices import Lattices

            return Lattices(self.base_ring())("U").discriminant_group()

        class ParentMethods:
            def is_torsion(self) -> bool:
                return True


FinitelyGeneratedModules = Modules.FinitelyGenerated
FinitelyPresentedModules = Modules.FinitelyPresented
FinitelyPresentedTorsionModules = Modules.FinitelyPresented.Torsion
FreeModules = Modules.Free
ProjectiveModules = Modules.Projective
TorsionModules = Modules.Torsion


def FinitelyGeneratedFreeModules(base_ring):
    r"""``FramedFreeModules(R).FinitelyGenerated()``, under the name the session catalogue uses."""
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
        FramedFreeModules,
    )

    return FramedFreeModules(base_ring).FinitelyGenerated()


class LinearHomModules(OwnedCategoryOverBaseRing):
    r"""Represented Hom parents closed under pointwise ``R``-linear operations."""

    def an_object(self):
        r"""The endomorphisms of the free module of rank one."""
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        modules = Modules(self.base_ring())
        free = modules.an_object()
        return modules.Mor(free, free)

    @classmethod
    def _repr_object_names(cls):
        return "linear Hom modules"

    def super_categories(self):
        return [Modules(self.base_ring())]

    class ParentMethods:
        def base_ring(self):
            r"""The ring acting pointwise on ``Hom_R(M, N)``: ``R`` when commutative, else its centre.

            ``(r f)(m) = r f(m)`` is ``R``-linear in ``m`` exactly when ``r``
            commutes with the scalars, so a noncommutative ring acts through
            its centre.
            """
            ring = self.domain().base_ring()
            match ring:
                case _ if ring in OwnedRings().Commutative():
                    return ring
                case _:
                    return ring.ring_center()

        def source_module(self):
            return self.domain()

        def target_module(self):
            return self.codomain()

        def scalar_multiple(self, scalar, morphism):
            if morphism.parent() is not self:
                morphism = self(morphism)
            scalar = self.base_ring()(scalar)
            return self.elementwise(
                lambda element: self.codomain().scalar_multiple(
                    scalar,
                    morphism(element),
                ),
                verify_linearity=False,
            )

        def as_morphism(self, element):
            return self(element)

        def from_morphism(self, morphism):
            return self(morphism)

        def evaluation(self, map_element, source_element):
            return self(map_element)(source_element)


class InternalHomModules(OwnedCategoryOverBaseRing):
    r"""The canonical full enriched Hom modules ``Hom_R(M,N)``."""

    def an_object(self):
        r"""The endomorphisms of the free module of rank one."""
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        modules = Modules(self.base_ring())
        free = modules.an_object()
        return modules.Mor(free, free)

    @classmethod
    def _repr_object_names(cls):
        return "internal Hom modules"

    def super_categories(self):
        return [LinearHomModules(self.base_ring())]

    class ParentMethods:
        def _smith_engine(self):
            r"""Read the native FGP workspace of the endpoint-determined model."""
            return self.internal_hom_model()._smith_engine()

        def _to_smith_engine_element(self, morphism):
            model = self.internal_hom_model()
            return model._to_smith_engine_element(self._internal_model_from_morphism(morphism))

        def _from_smith_engine_element(self, element):
            model = self.internal_hom_model()
            return self._morphism_from_internal_model(model._from_smith_engine_element(element))

        def internal_hom_model(self):
            r"""The presented module ``ker(N^{gens(M)} -> N^{rels(M)})`` modelling ``Hom_R(M, N)``.

            A map out of ``M = coker(F_1 -> F_0)`` is an assignment of an
            element of ``N`` to each generator of ``M`` killing every relation,
            so ``Hom_R(M, N)`` is the kernel of the evaluation of relations on
            generator assignments; its endpoints determine it.
            """
            from dzack_research.preamble.categories.modules.internal_hom import (
                _internal_hom_model_data,
            )

            model, _inclusion, _relations, _presentation = _internal_hom_model_data(self)
            return model

        def inclusion_into_generator_maps(self):
            r"""The inclusion of the presented model of ``Hom(M, N)`` into ``N^{gens(M)}``."""
            from dzack_research.preamble.categories.modules.internal_hom import (
                _internal_hom_model_data,
            )

            _model, inclusion, _relations, _presentation = _internal_hom_model_data(self)
            return inclusion

        def _morphism_from_internal_model(self, model_element):
            r"""Read an element of :meth:`internal_hom_model` as the linear map it assigns."""
            assignment_space = self.inclusion_into_generator_maps().codomain()
            assignment = self.inclusion_into_generator_maps()(model_element)
            coefficients = assignment_space.framing_coefficients(assignment)
            assignment_labels = assignment_space.module_generating_set()
            return self(
                {
                    source_label: self.codomain().linear_combination(
                        {
                            target_label: coefficients[pair]
                            for target_label in self.codomain().module_generating_set()
                            if (pair := assignment_labels(lambda index: source_label if int(index) == 0 else target_label)) in coefficients
                        }
                    )
                    for source_label in self.domain().module_generating_set()
                }
            )

        def _internal_model_from_morphism(self, morphism):
            r"""Read a linear map as the element of :meth:`internal_hom_model` assigning its generator images."""
            model = self.internal_hom_model()
            power = self.inclusion_into_generator_maps().codomain()
            power_labels = power.module_generating_set()
            coefficients = {}
            for source_label in self.domain().module_generating_set():
                image = morphism(self.domain().module_generator(source_label))
                for target_label, coefficient in self.codomain().framing_coefficients(image).items():
                    coefficients[power_labels(lambda index: source_label if int(index) == 0 else target_label)] = coefficient
            assignment = power.linear_combination(coefficients)
            inclusion = self.inclusion_into_generator_maps()
            if inclusion.has_selected_lift():
                return inclusion.lift(assignment)
            return model(assignment)

        def _selected_module_coefficients(self, morphism):
            r"""Coordinates of a linear map in the framing of the presented model."""
            model = self.internal_hom_model()
            return model.framing_coefficients(self._internal_model_from_morphism(self(morphism)))


class ModuleSubobjectConstruction:
    r"""The selected data defining one module subobject and its inclusion."""

    def __init__(
        self,
        *,
        ambient=None,
        generator_images=None,
        lift=None,
        inclusion_factory=None,
        verify_linearity=True,
    ) -> None:
        if inclusion_factory is None and (ambient is None or generator_images is None):
            raise ValueError("a module subobject requires constructor-owned inclusion data")
        self._ambient = ambient
        self._generator_images = generator_images
        self._lift = lift
        self._inclusion_factory = inclusion_factory
        self._verify_linearity = bool(verify_linearity)

    def ambient_module(self):
        return self._ambient

    def generator_images(self):
        return self._generator_images

    def selected_lift(self):
        return self._lift

    def inclusion_factory(self):
        return self._inclusion_factory

    def verify_linearity(self) -> bool:
        return self._verify_linearity

    def inclusion(self, subobject):
        factory = self.inclusion_factory()
        if factory is not None:
            return factory(subobject)
        lift = self.selected_lift()
        return subobject.Mono(self.ambient_module())(
            self.generator_images(),
            verify_linearity=self.verify_linearity(),
            lift=(None if lift is None else lambda element: lift(subobject, element)),
        )


class ModuleSubobjects(OwnedCategoryOverBaseRing):
    r"""Modules carrying a chosen monomorphism into another module."""

    def an_object(self):
        r"""The ideal (2), a submodule of the base ring."""
        return self.base_ring().ideal(2)

    @classmethod
    def _repr_object_names(cls):
        return "module subobjects"

    def super_categories(self):
        return [Modules(self.base_ring())]

    class ParentMethods:
        def __init__(
            self,
            subobject_ambient=None,
            subobject_generator_images=None,
            subobject_lift=None,
            subobject_inclusion_factory=None,
            subobject_verify_linearity=True,
            **rest,
        ) -> None:
            self._module_subobject_construction = ModuleSubobjectConstruction(
                ambient=subobject_ambient,
                generator_images=subobject_generator_images,
                lift=subobject_lift,
                inclusion_factory=subobject_inclusion_factory,
                verify_linearity=subobject_verify_linearity,
            )
            super().__init__(**rest)

        def module_subobject_construction(self):
            r"""Return the selected construction defining this module subobject."""
            return self._module_subobject_construction

        @cached_method
        def inclusion(self):
            r"""Return the chosen monomorphism represented by constructor data."""
            return self.module_subobject_construction().inclusion(self)

        def ambient_module(self):
            r"""Return the ambient module, i.e. the codomain of the inclusion."""
            return self.inclusion().codomain()

        def embedded_module_generators(self):
            r"""Return the indexed family of selected generator images."""
            labels = self.module_generating_set()
            return finite_indexed_family(
                labels,
                lambda label: self.inclusion()(self.module_generator(label)),
                name=f"Embedded framing of {self}",
            )

        def is_primitive(self) -> bool:
            return self.inclusion().is_primitive()

        is_saturated = is_primitive

        def index(self):
            return self.inclusion().index()

        def orthogonal_complement(self):
            r"""Return the orthogonal complement by deferring to the inclusion."""
            return self.inclusion().orthogonal_complement()

        def sum(self, other):
            r"""Return the join of two subobjects of the same codomain."""
            if self.inclusion().codomain() is not other.inclusion().codomain():
                raise ValueError("a subobject sum requires one common codomain")
            codomain = self.inclusion().codomain()
            summands = Sets().coproduct(
                indexed_family(
                    Sets.Δ[1],
                    lambda index: (
                        self.module_generating_set()
                        if int(index) == 0
                        else other.module_generating_set()
                    ),
                )
            )
            generators = finite_indexed_family(
                summands,
                lambda tagged: (
                    self.inclusion()(self.module_generator(tagged.summand_element()))
                    if int(tagged.summand_index()) == 0
                    else other.inclusion()(other.module_generator(tagged.summand_element()))
                ),
                name="Subobject-sum generators",
            )
            return codomain.subobject_on(generators)

        def intersection(self, other):
            r"""Return the meet as the image of the kernel of ``(i,-j)``."""
            if self.inclusion().codomain() is not other.inclusion().codomain():
                raise ValueError("a subobject intersection requires one common codomain")

            direct_sum = Modules(self.base_ring()).biproduct((self, other))
            difference = direct_sum.from_summands(self.inclusion(), -other.inclusion())
            kernel = difference.kernel()
            into_left = direct_sum.left_projection() * kernel.inclusion()
            into_codomain = self.inclusion() * into_left
            return into_codomain.image()

        def saturation(self):
            r"""Return the primitive closure by deferring to the inclusion."""
            return self.inclusion().saturation()


class VectorSpaces(OwnedCategoryOverBaseRing):
    r"""Vector spaces over a field."""

    def an_object(self):
        r"""The free module of rank one over the base field."""
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        return Modules(self.base_ring()).an_object()

    def additional_condition(self):
        r"""None: over a field, a vector space is exactly a module.

        The condition is on the parameter, not on the object.  Every module
        over a field is a vector space over it, so nothing has to be placed
        here to be here.
        """
        return None

    @classmethod
    def _repr_object_names(cls):
        return "vector spaces"

    def super_categories(self):
        return [Modules(self.base_ring())]

    class ParentMethods:
        def dimension(self):
            r"""Return the dimension from this vector space's represented backend."""
            represented = self._represented_vector_space_dimension()
            if represented is NotImplemented:
                raise NotImplementedError(f"the dimension of {self} has no represented vector-space backend")
            return represented

        def basis_generator_labels(self):
            r"""Return selected framing labels whose classes form a basis."""
            represented = self._represented_vector_space_basis_generator_labels()
            if represented is NotImplemented:
                raise NotImplementedError(f"{self} has no represented basis subfamily of its selected generators")
            return represented


class ModulesWithChosenFinitePresentation(OwnedCategoryOverBaseRing):
    r"""Finitely presented modules carrying one selected finite presentation."""

    def an_object(self):
        r"""The hyperbolic plane U, presented by its Gram matrix."""
        from dzack_research.preamble.categories.lattices import Lattices

        return Lattices(self.base_ring())("U")

    @classmethod
    def _repr_object_names(cls):
        return "modules with a chosen finite presentation"

    def _call_(self, morphism, category=None, **construction_data):
        r"""Construct ``coker(rho)`` for ``rho: A -> B`` into a module with a chosen finite presentation.

        A presentation ``F_1 -> F_0`` is the case ``B = F_0`` free.  The
        chosen presentation of the cokernel is the presentation of ``B`` with
        the images of the module generators of ``A`` added as relations, and
        the cokernel retains ``rho`` as the morphism it is the cokernel of.
        ``category`` joins a structured category to the cokernel; the levels
        of that category read their data from ``construction_data``.
        """
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
            _presented_module_from_morphism,
        )

        ring = self.base_ring()
        assert morphism.domain() in FramedModules(ring), (
            "the finite cokernel presentation uses a selected source framing"
        )
        assert morphism.domain().module_generating_set().cardinality().is_finite(), (
            "adjoining the image of a framing gives finitely many relations only for a finite framing"
        )
        assert morphism.codomain() in ModulesWithChosenFinitePresentation(ring), (
            f"a cokernel with a chosen finite presentation is taken of a morphism into "
            f"a module over {ring} with a chosen finite presentation"
        )
        return _presented_module_from_morphism(
            morphism,
            _cokernel_morphism=morphism,
            _extra_categories=() if category is None else (category,),
            _extra_construction_data=construction_data or None,
        )

    def super_categories(self):
        return [
            Modules(self.base_ring()).FinitelyPresented(),
            FramedModules(self.base_ring()),
        ]

    @cached_method
    def presentation_category(self):
        r"""Return the category of selected presentation arrows in ``R-Mod``.

        A chosen presentation is additional structure on a module, and its
        morphisms are commuting squares between the selected free-module
        arrows.  The common arrow-category owner already supplies exactly
        those objects and morphisms, so this category exposes that owner
        rather than inventing a second presentation-morphism implementation.
        """
        return Modules(self.base_ring()).ArrowCategory()

    class ParentMethods:
        @cached_method
        def tensor_hom_adjunction(self):
            r"""Return ``- tensor self ⊣ Hom_R(self,-)`` on chosen finite presentations."""
            from dzack_research.preamble.categories.functors.tensor_hom import (
                _TensorHomAdjunction,
            )

            return _TensorHomAdjunction(self)

        @cached_method
        def presentation_object(self):
            r"""Return this module's selected presentation as an arrow object."""
            category = ModulesWithChosenFinitePresentation(
                self.base_ring()
            ).presentation_category()
            return category(self.presentation())

        def adic_completion(self, ideal, *, precision=20):
            r"""Return ``M tensor_R R_hat`` along the represented ``I``-adic completion."""
            ring = self.base_ring()
            if ideal.ring() is not ring:
                raise ValueError("module completion requires an ideal of the module base ring")
            completion = ring.adic_completion(ideal, precision=precision)
            return self.base_change_to_completion(completion)

        def base_change_to_completion(self, completion):
            r"""Return ``M tensor_R R_hat`` for one already selected completion."""
            ring = self.base_ring()
            if completion.completion_source() is not ring:
                raise ValueError("the completion has the wrong source ring for this module")
            adjunction = Modules(ring).base_change_adjunction(completion.completion_map())
            return adjunction.left_adjoint()(self)

        # The completion M_hat is an ordinary scalar-extension image and holds
        # no record of M; the maps that need both are stated on M, whose
        # base-change functor answers M_hat by object identity.

        def completion_unit(self, completion):
            r"""Return the canonical ``R``-linear map ``M -> Res_R(M_hat)`` for one selected completion."""
            ring = self.base_ring()
            if completion.completion_source() is not ring:
                raise ValueError("the completion has the wrong source ring for this module")
            return Modules(ring).base_change_adjunction(completion.completion_map()).unit(self)

        @cached_method
        def adic_module_truncation(self, completion, exponent):
            r"""Return ``M tensor_R R/I^exponent`` from the same selected presentation."""
            quotient = completion.adic_truncation(exponent)
            return self.base_change(quotient.quotient_map())

        @cached_method
        def adic_module_projection(self, completion, exponent):
            r"""Return ``M_hat -> Res(M/I^exponent M)`` over ``R_hat``."""
            completed = self.base_change_to_completion(completion)
            target = self.adic_module_truncation(completion, exponent)
            ring_map = completion.adic_projection(exponent)
            restricted = target.restrict_scalars(ring_map)
            labels = completed.module_generating_set()
            target_labels = target.module_generating_set()
            if labels.cardinality() != target_labels.cardinality():
                raise ArithmeticError("adic base change changed the selected module framing cardinality")
            return completed.module_category().Mor(completed, restricted)(
                {
                    label: restricted(
                        target.module_generator(
                            target_labels[int(labels.ranking_map()(label))]
                        )
                    )
                    for label in labels
                }
            )

        @cached_method
        def adic_module_transition_map(self, completion, higher_exponent, lower_exponent):
            r"""Return ``M/I^higher M -> Res(M/I^lower M)`` for one selected completion."""
            higher_exponent = int(higher_exponent)
            lower_exponent = int(lower_exponent)
            higher = self.adic_module_truncation(completion, higher_exponent)
            lower = self.adic_module_truncation(completion, lower_exponent)
            ring_map = completion.adic_transition_map(
                higher_exponent,
                lower_exponent,
            )
            restricted = lower.restrict_scalars(ring_map)
            higher_labels = higher.module_generating_set()
            lower_labels = lower.module_generating_set()
            if higher_labels.cardinality() != lower_labels.cardinality():
                raise ArithmeticError("adic transition changed the selected module framing cardinality")
            return higher.module_category().Mor(higher, restricted)(
                {
                    label: restricted(
                        lower.module_generator(
                            lower_labels[int(higher_labels.ranking_map()(label))]
                        )
                    )
                    for label in higher_labels
                }
            )


@dataclass(frozen=True)
class FreeResolution:
    r"""The exact resolution ``0 -> F_n -> ... -> F_0 -> M -> 0`` by free modules.

    The datum is an indexed family of free modules over the degrees carrying a
    term, together with the family of differentials over the degrees that carry
    one, which are the nonzero ones.  A module over a principal ideal domain
    resolves in one step, while ``k = R/(x,y)`` over ``R = k[x,y]`` needs the
    Koszul complex and two, so the degrees are what varies and the top degree is
    read off them.  Outside those degrees everything is the zero module and the
    zero map, which is what makes the resolution finite.
    """

    _module: Parent
    _degrees: Parent
    _terms: IndexedFamily
    _differentials: IndexedFamily
    _augmentation: ModuleMorphism
    _zero_term: Parent

    def module(self):
        return self._module

    def degrees(self):
        r"""Return the degrees carrying a term, an owned ordered set."""
        return self._degrees

    def term(self, degree):
        if int(degree) < 0:
            raise ValueError("a homological degree is nonnegative")
        if degree in self._degrees:
            return self._terms.value(degree)
        return self._zero_term

    def differential(self, degree):

        if int(degree) <= 0:
            raise ValueError("resolution differentials are indexed in positive degree")
        if degree in self._differentials.index_set():
            return self._differentials.value(degree)
        source = self.term(degree)
        target = self.term(int(degree) - 1)
        return source.module_category().Mor(source, target).zero()

    def augmentation(self):
        return self._augmentation

    def length(self):
        r"""Return the largest degree carrying a nonzero term."""
        return int(max(self._degrees))

    def is_exact(self):
        r"""Decide exactness of ``0 -> F_n -> ... -> F_0 -> M -> 0``.

        Exactness is checked where it is stated: the augmentation is onto, the
        last differential is injective, and at every intermediate spot the
        image of the incoming map equals the kernel of the outgoing one, each
        equality decided as a pair of subobject containments.
        """

        if not self.augmentation().is_surjective():
            return False
        length = self.length()
        if length == 0:
            return self.augmentation().is_injective()
        if not self.differential(length).is_injective():
            return False

        def agree(image, kernel, term):
            subobjects = Modules(term.base_ring()).Subobjects(term)
            return subobjects.leq(image, kernel) and subobjects.leq(kernel, image)

        if not agree(
            self.differential(1).image(),
            self.augmentation().kernel(),
            self.term(0),
        ):
            return False
        return all(
            agree(
                self.differential(int(degree) + 1).image(),
                self.differential(degree).kernel(),
                self.term(degree),
            )
            for degree in self._differentials.index_set()
            if int(degree) != length
        )

    def lift_morphism(self, morphism, target_resolution=None):
        r"""Lift ``morphism : M -> N`` to a chain map of selected free resolutions.

        The lift is constructed degree by degree by projectivity of the free
        terms.  In degree zero, lift ``f epsilon_F`` through the target
        augmentation.  In degree ``i>0``, exactness puts the already-defined
        composite ``f_{i-1} d_i`` in the image of the target differential, so
        lift each selected free generator through that differential.  No
        coordinate chain-map formula is introduced here; the common module
        image/preimage operations supply the lifts.
        """
        if morphism.domain() is not self.module():
            raise ValueError("a resolution morphism must start at the resolved source module")
        if target_resolution is None:
            target_resolution = morphism.codomain().free_resolution(self.length() + 1)
        if target_resolution.module() is not morphism.codomain():
            raise ValueError("the target resolution resolves the wrong module")

        components = {}
        source_zero = self.term(0)
        target_augmentation = target_resolution.augmentation()
        components[0] = source_zero.module_category().Mor(source_zero, target_resolution.term(0))(
            {
                label: target_augmentation.preimage(
                    morphism(self.augmentation()(source_zero.module_generator(label)))
                )
                for label in source_zero.module_generating_set()
            }
        )

        for degree in range(1, self.length() + 1):
            source_term = self.term(degree)
            target_differential = target_resolution.differential(degree)
            previous = components[degree - 1]
            source_differential = self.differential(degree)
            components[degree] = source_term.module_category().Mor(source_term, target_resolution.term(degree))(
                {
                    label: target_differential.preimage(
                        previous(source_differential(source_term.module_generator(label)))
                    )
                    for label in source_term.module_generating_set()
                }
            )
        return FreeResolutionMorphism(self, target_resolution, morphism, components)


@dataclass(frozen=True)
class FreeResolutionMorphism:
    r"""A chain map between free resolutions lying over one module morphism."""

    _domain: FreeResolution
    _codomain: FreeResolution
    _module_morphism: ModuleMorphism
    _components: dict

    def __post_init__(self):
        degree_zero = self.component(0)
        source_zero = self.domain().term(0)
        for label in source_zero.module_generating_set():
            generator = source_zero.module_generator(label)
            if self.codomain().augmentation()(degree_zero(generator)) != self.module_morphism()(
                self.domain().augmentation()(generator)
            ):
                raise ValueError("the lifted degree-zero map does not commute with augmentation")
        for degree in range(1, self.domain().length() + 1):
            component = self.component(degree)
            previous = self.component(degree - 1)
            source_differential = self.domain().differential(degree)
            target_differential = self.codomain().differential(degree)
            for label in component.domain().module_generating_set():
                generator = component.domain().module_generator(label)
                if target_differential(component(generator)) != previous(
                    source_differential(generator)
                ):
                    raise ValueError(f"the lifted resolution square fails in degree {degree}")

    def domain(self):
        return self._domain

    def codomain(self):
        return self._codomain

    def module_morphism(self):
        return self._module_morphism

    def component(self, degree):
        degree = int(degree)
        selected = self._components.get(degree)
        if selected is not None:
            return selected
        source = self.domain().term(degree)
        target = self.codomain().term(degree)
        return source.module_category().Mor(source, target).zero()

    def chain_homotopy_to(self, other):
        r"""Return a chain homotopy from this lift to ``other``.

        Two chain maps between free resolutions lifting the same module map are
        homotopic.  The homotopy is constructed degree by degree using exactness
        of the target resolution, exactly as :meth:`FreeResolution.lift_morphism`
        constructs a lift by projectivity of the free source terms.
        """
        if other.domain() is not self.domain() or other.codomain() is not self.codomain():
            raise ValueError("chain homotopy compares maps between the same resolutions")
        if other.module_morphism() is not self.module_morphism():
            raise ValueError("chain homotopy here compares lifts of one selected module morphism")
        source = self.domain()
        target = self.codomain()
        components = {}
        for degree in range(source.length() + 1):
            source_term = source.term(degree)
            target_next = target.term(degree + 1)
            target_differential = target.differential(degree + 1)

            def residual(generator, degree=degree):
                value = self.component(degree)(generator) - other.component(degree)(generator)
                if degree > 0:
                    previous_homotopy = components[degree - 1]
                    value -= previous_homotopy(source.differential(degree)(generator))
                return value

            components[degree] = source_term.module_category().Mor(source_term, target_next)(
                {
                    label: target_differential.preimage(
                        residual(source_term.module_generator(label))
                    )
                    for label in source_term.module_generating_set()
                }
            )
        return FreeResolutionHomotopy(self, other, components)


@dataclass(frozen=True)
class FreeResolutionHomotopy:
    r"""A selected homotopy ``h`` with ``f-g = d h + h d``."""

    _source: FreeResolutionMorphism
    _target: FreeResolutionMorphism
    _components: dict

    def __post_init__(self):
        source_resolution = self._source.domain()
        target_resolution = self._source.codomain()
        for degree in range(source_resolution.length() + 1):
            source_term = source_resolution.term(degree)
            for label in source_term.module_generating_set():
                generator = source_term.module_generator(label)
                right = target_resolution.differential(degree + 1)(
                    self.component(degree)(generator)
                )
                if degree > 0:
                    right += self.component(degree - 1)(
                        source_resolution.differential(degree)(generator)
                    )
                left = self._source.component(degree)(generator) - self._target.component(degree)(generator)
                if left != right:
                    raise ValueError(f"the selected maps are not homotopic in degree {degree}")

    def source(self):
        return self._source

    def target(self):
        return self._target

    def component(self, degree):
        degree = int(degree)
        selected = self._components.get(degree)
        if selected is not None:
            return selected
        chain_map = self.source()
        source = chain_map.domain().term(degree)
        target = chain_map.codomain().term(degree + 1)
        return source.module_category().Mor(source, target).zero()


class FramedModules(OwnedCategoryOverBaseRing):
    r"""Modules carrying a selected epimorphism from a free module."""

    @classmethod
    def _repr_object_names(cls):
        return "framed modules"

    def an_object(self):
        r"""The free module of rank one, framed by its one generator."""
        return self.base_ring().free_module(1)

    def super_categories(self):
        return [Modules(self.base_ring())]

    @cached_method
    def framing_category(self):
        r"""Return the category whose objects are selected module framings.

        A framing is the epimorphism ``F_R(S) -> M`` itself.  A morphism of
        framed modules is therefore a commuting square between two such arrows;
        the left edge is an arbitrary ``R``-linear map between the selected free
        sources, not necessarily one induced by a function of label sets.
        """
        return Modules(self.base_ring()).ArrowCategory()

    class ParentMethods:
        # The selected framing epimorphism ``F_R(S) -> M``, this level's datum.
        _selected_framing_source = None
        _selected_framing_images = None

        def __init__(
            self,
            module_generating_set=None,
            module_generator_function=None,
            framing_source=None,
            **rest,
        ) -> None:
            r"""Construct the framed module on its selected framing.

            The datum is the epimorphism ``F_R(S) -> M`` from the free module
            on ``module_generating_set``, sending the generator at ``s`` to
            ``module_generator_function(s)``.  The source free module and the
            epimorphism are retained here; accessors below project from that
            one arrow and never reconstruct an isomorphic source from labels.
            """
            super().__init__(**rest)
            if module_generating_set is not None:
                self._install_framing(
                    module_generating_set,
                    module_generator_function,
                    framing_source,
                )

        def _install_framing(
            self,
            module_generating_set,
            module_generator_function,
            framing_source=None,
        ) -> None:
            r"""Establish the framing epimorphism of this module.

            Protected contract of ``FramedModules(R)``.  Its callers are this
            level's constructor and a construction whose framing is computed
            from the datum it introduces -- the localization of a framed
            module carries the source framing to fractions, a restriction of
            scalars frames by products of framings -- when that construction
            is placed beside ``FramedModules(R)`` in a join rather than below
            it, so that this level's constructor may run before the datum the
            framing is computed from exists.  It is called once, before the
            constructed object is returned, with the framing labels, the
            images of the free generators, and optionally the free module on
            those labels; it stores the framing epimorphism.
            """
            assert self._selected_framing_source is None, f"{self} already has a framing"
            source = framing_source
            if source is None:
                source = self.base_ring().free_module(module_generating_set)
            assert source.module_generating_set() == module_generating_set, (
                "the selected framing source does not have the requested generator set"
            )
            self._selected_framing_source = source
            self._selected_framing_images = module_generator_function

        def module_generating_set(self):
            return self.framing_source().module_generating_set()

        def module_generator(self, label):
            source = self.framing_source()
            if label not in source.module_generating_set():
                raise ValueError(f"{label!r} is not a module-generator label")
            return self.framing_morphism()(source.module_generator(label))

        def number_of_module_generators(self):
            return self.module_generating_set().cardinality()

        @cached_method
        def module_generators(self):
            r"""Return the selected framing as the indexed family ``s ↦ m_s``."""

            return indexed_family(
                self.module_generating_set(),
                self.module_generator,
                name="Module generators",
            )

        def module_generator_morphism(self):
            return self.framing_morphism().module_generator_morphism()

        def framing_source(self):
            r"""Return the actual free module selected as the source of this framing."""
            source = self._selected_framing_source
            assert source is not None, f"{self} was constructed without its framing source"
            return source

        def sub_framing_morphism(self, codomain):
            r"""Return the inclusion induced by this framing inside ``codomain``'s framing."""
            if codomain not in FramedModules(self.base_ring()):
                raise TypeError("a sub-framing inclusion requires another framed module over the same ring")
            return SubFramingMorphism(
                self.Mono(codomain),
                codomain.module_generator,
                verify_linearity=False,
            )

        @cached_method
        def framing_morphism(self):
            r"""Realize the selected epimorphism on its already constructed source.

            The source and generator map are fixed at construction. Only the
            host morphism wrapper is lazy: eagerly constructing its enriched
            Mor would ask for that Mor module's framing, and repeat without
            end. No underlying module or framing choice is reconstructed here.
            """
            return _framing_morphism(self.framing_source(), self, self._selected_framing_images)

        @cached_method
        def framing_object(self):
            r"""Return this selected framing as an object of ``Arr(R-Mod)``."""
            category = FramedModules(self.base_ring()).framing_category()
            return category(self.framing_morphism())

        def linear_combination(self, coefficients):
            r"""Return ``sum_s c_s m_s`` for finitely supported coefficients ``s |-> c_s``.

            The coefficients are a finitely supported function on the framing
            labels, given as a mapping from labels to scalars.
            """
            return sum(
                (
                    self.scalar_multiple(
                        coefficient,
                        self.module_generator(label),
                    )
                    for label, coefficient in coefficients.items()
                ),
                self.zero(),
            )

        def inject_variables(self, scope=None, verbose=True):
            assert scope is not None, "module generators are injected into a stated scope"
            assert self.module_generating_set().cardinality().is_finite(), (
                "injecting module generators as variables requires a finite framing"
            )
            names = tuple(self.variable_names())
            generators = tuple(self.module_generators())
            if len(names) != len(generators):
                raise ValueError("the variable names do not describe the module framing")
            if verbose:
                print(f"Defining {', '.join(names)}")
            scope.update(zip(names, generators, strict=True))

        def is_framed_module(self) -> bool:
            return True


class RestrictedScalarsModules(OwnedCategoryOverBaseRing):
    r"""Modules ``Res_f(M)``: an ``S``-module ``M`` read over ``R`` along ``f: R -> S``.

    The datum is the pair ``(M, f)``.  The underlying additive group is that
    of ``M`` and ``r`` acts as ``f(r)``.  When ``S`` is finite free over ``R``
    on ``(s_i)`` and ``M`` is finitely framed over ``S`` on ``(m_j)``, the
    products ``s_i m_j`` frame ``Res_f(M)``, and a chosen finite presentation
    of ``M`` induces one of ``Res_f(M)``.
    """

    def an_object(self):
        r"""``Res_{id}(R^2)``: a free module along the identity of ``R``."""

        from dzack_research.preamble.categories.sets.set_categories import finite_ordinal_set

        ring = self.base_ring()
        return ring.free_module(finite_ordinal_set(2)).restrict_scalars(
            ring.Mor(ring)(lambda element: element)
        )

    @classmethod
    def _repr_object_names(cls):
        return "restricted-scalars modules"

    def super_categories(self):
        return [Modules(self.base_ring())]

    def _call_(self, module, ring_map):
        r"""Construct ``Res_f(M)`` for an ``S``-module ``M`` along ``f: R -> S``."""
        assert _owned_ring(ring_map.domain()) is self.base_ring(), (
            f"restriction of scalars to {self.base_ring()} is along a ring morphism out of it"
        )
        return _restricted_scalars_view(module, ring_map)

    class ElementMethods(ModuleElement):
        r"""An element of ``Res_f(M)``, which is an element of ``M`` read over ``R``."""

        def __init__(self, parent, underlying_element) -> None:
            ModuleElement.__init__(self, parent)
            self._underlying_element = underlying_element

        def underlying_element(self):
            r"""Return this element read in ``M``."""
            return self._underlying_element

        def _add_(self, other):
            return self.parent().element_class(
                self.parent(),
                self._underlying_element + other._underlying_element,
            )

        def _neg_(self):
            return self.parent().element_class(self.parent(), -self._underlying_element)

        def _lmul_(self, scalar):
            return self.parent().scalar_multiple(scalar, self)

        def _richcmp_(self, other, op):
            return richcmp(
                self._underlying_element,
                other._underlying_element,
                op,
            )

        def _repr_(self):
            return repr(self._underlying_element)

    class ParentMethods:
        _derived_construction_parameters = frozenset({"base_ring"})

        def __init__(self, module_over_extension, ring_map, **rest) -> None:
            self._module_over_extension = module_over_extension
            self._ring_map = ring_map
            ring = _owned_ring(ring_map.domain())
            super().__init__(base_ring=ring, **rest)
            match self:
                case _ if self in FramedModules(ring):
                    # The products ``s_i m_j`` frame ``Res_f(M)``; a chosen
                    # presentation of it is written on the free module over
                    # those products, which is then the framing source.
                    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
                        _SelectedFinitePresentationModules,
                    )

                    match self:
                        case _ if self in _SelectedFinitePresentationModules(ring):
                            source = self.presentation().codomain()
                        case _:
                            source = ring._fresh_free_module_on(
                                _restricted_scalar_framing_labels(module_over_extension)
                            )
                    self._install_framing(
                        source.module_generating_set(),
                        self._restricted_scalar_generator,
                        source,
                    )

        def ring_map(self):
            r"""Return the selected scalar map ``R -> S``."""
            return self._ring_map

        def module_over_extension(self):
            r"""Return the original ``S``-module before restriction of scalars."""
            return self._module_over_extension

        def extension_ring(self):
            return _owned_ring(self.module_over_extension().base_ring())

        def underlying_additive_group(self):
            r"""Return the unchanged additive group of the extension-ring module."""
            return self.module_over_extension().underlying_additive_group()

        def _underlying_additive_element(self, element):
            element = self(element)
            extension = self.module_over_extension()
            return extension._underlying_additive_element(element.underlying_element())

        @cached_method
        def _ring_morphism_defining_module_action(self):
            r"""Return ``rho_M compose f`` for restriction along ``f : R -> S``."""
            return self.module_over_extension().scalar_action() * self.ring_map()

        def scalar_multiple(self, scalar, element):
            element = self(element)
            underlying = self._underlying_additive_element(element)
            return self.wrap(
                self.scalar_action()(self.base_ring()(scalar))(underlying)
            )

        def _element_constructor_(self, value):
            if isinstance(value, self.element_class) and value.parent() is self:
                return value
            if isinstance(value, RestrictedScalarsModules.ElementMethods):
                value = value.underlying_element()
            return self.wrap(self.module_over_extension()(value))

        def wrap(self, underlying_element):
            r"""Read an element of ``M`` as the same element of ``Res_f(M)``."""
            return self.element_class(self, self.module_over_extension()(underlying_element))

        def _coerce_map_from_(self, source):
            # Restriction of scalars is a change of structure, not a coercion of
            # mathematical objects.  ``wrap`` reads an element of ``M`` here
            # explicitly when the same additive-group element is meant.
            if source is self.module_over_extension():
                return None
            return super()._coerce_map_from_(source)

        def __contains__(self, value) -> bool:
            if isinstance(value, self.element_class) and value.parent() is self:
                return True
            return value in self.module_over_extension()

        def _restricted_scalar_generator(self, label):
            r"""Return ``s_i m_j`` for the framing label ``(i, j)``."""
            labels = self.module_generating_set()
            assert label in labels, f"{label!r} is not a restricted-scalar module-generator label"
            label = labels(label)
            extension_module = self.module_over_extension()
            scalar = self.extension_ring().module_generator(label.component(0))
            module_generator = extension_module.module_generator(label.component(1))
            return self.element_class(
                self,
                extension_module.scalar_multiple(scalar, module_generator),
            )

        def _selected_module_coefficients(self, element):
            r"""``m = sum_j t_j m_j`` and ``t_j = sum_i c_ij s_i`` give ``m = sum_ij c_ij s_i m_j``."""
            element = self(element)
            extension_coefficients = self.module_over_extension().framing_coefficients(
                element.underlying_element()
            )
            framing = self.module_generating_set()
            return {
                framing((scalar_label, module_label)): self.base_ring()(coefficient)
                for module_label, scalar in extension_coefficients.items()
                for scalar_label, coefficient in self.extension_ring().framing_coefficients(scalar).items()
            }

        def zero(self):
            return self.element_class(self, self.module_over_extension().zero())

        def an_element(self):
            return self.element_class(self, self.module_over_extension().an_element())

        def _repr_(self):
            return f"{self.module_over_extension()} restricted to {self.base_ring()} along {self.ring_map()}"


def _restricted_scalar_framing_labels(module):
    r"""Return the framing labels ``I x J`` of ``Res_f(M)`` for ``S`` framed on ``I``, ``M`` on ``J``."""
    extension_ring = _owned_ring(module.base_ring())
    scalar_labels = extension_ring.module_generating_set()
    module_labels = module.module_generating_set()
    return Sets().product(
        indexed_family(
            Sets.Δ[1],
            lambda index: scalar_labels if int(index) == 0 else module_labels,
        )
    )


def _restricted_scalar_presentation(module, ring_map, labels):
    r"""Return the finite presentation of ``Res_f(M)`` induced by one of ``M``.

    Suppose ``S`` is finite free over ``R`` on ``(s_i)`` and ``M`` is
    presented over ``S`` on ``(m_j)`` with relation rows ``(a_j)``.  The
    restricted module is generated over ``R`` by ``s_i m_j``.  For every
    selected relation and every ``s_i`` we expand ``s_i a_j`` in the
    selected ``R``-basis of ``S``.  These are exactly the restriction of
    the original ``S``-relation submodule to ``R``.
    """
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
        _presentation_from_relation_rows,
    )

    ring = _owned_ring(ring_map.domain())
    extension_ring = _owned_ring(module.base_ring())
    scalar_labels = extension_ring.module_generating_set()
    module_labels = module.module_generating_set()
    width = int(labels.cardinality())
    relation_rows = []
    source_rows = module._selected_presentation_rows()
    assert source_rows is not None, f"{module} has a chosen finite presentation and states its relations"
    for relation in source_rows:
        for scalar_label in scalar_labels:
            scalar_generator = extension_ring.module_generator(scalar_label)
            row = [ring.zero()] * width
            for module_label, coefficient in zip(module_labels, relation, strict=True):
                if not coefficient:
                    continue
                product = extension_ring(scalar_generator * extension_ring(coefficient))
                for output_scalar_label, output_coefficient in extension_ring.framing_coefficients(product).items():
                    column = labels.ranking_map()(labels(lambda index: output_scalar_label if int(index) == 0 else module_label))
                    row[column] += ring(output_coefficient)
            if any(row):
                relation_rows.append(tuple(row))
    relations = ring.matrix_space(len(relation_rows), width).from_rows(tuple(relation_rows))
    presentation = _presentation_from_relation_rows(
        ring,
        labels,
        Sets.Δ[len(relation_rows) - 1],
        relations,
    )
    return relations, presentation


def _restricted_scalars_view(
    module,
    ring_map,
    *,
    _subobject_ambient=None,
    _subobject_generator_images=None,
    _subobject_lift=None,
    _subobject_inclusion_factory=None,
    _subobject_verify_linearity=True,
):
    r"""Return ``Res_f(M)`` along ``f: R -> S``, placed by what ``M`` and ``S`` already are.

    ``Res_f(M)`` is framed, finitely generated and finitely presented over
    ``R`` when ``S`` is finite free over ``R`` and ``M`` is so over ``S``; a
    selected inclusion places it among the subobjects.
    """
    assert _engine_ring(ring_map.codomain()) is _engine_ring(module.base_ring()), (
        f"restriction of scalars for {module} requires a map into {module.base_ring()}, "
        f"got codomain {ring_map.codomain()}"
    )
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
        _SelectedFinitePresentationModules,
    )

    base_ring = _owned_ring(ring_map.domain())
    extension_ring = _owned_ring(module.base_ring())
    placement = [RestrictedScalarsModules(base_ring)]
    data = {"module_over_extension": module, "ring_map": ring_map}

    framed_over_finite_free_scalars = (
        module in FramedModules(extension_ring)
        and module in Modules(extension_ring).FinitelyGenerated()
        and extension_ring in FinitelyGeneratedFreeModules(base_ring)
    )
    match module:
        case _ if framed_over_finite_free_scalars and module in ModulesWithChosenFinitePresentation(extension_ring):
            relations, presentation = _restricted_scalar_presentation(
                module,
                ring_map,
                _restricted_scalar_framing_labels(module),
            )
            placement.append(_SelectedFinitePresentationModules(base_ring))
            data.update(relation_matrix=relations, presentation=presentation)
        case _ if framed_over_finite_free_scalars:
            placement.extend((FramedModules(base_ring), Modules(base_ring).FinitelyGenerated()))

    if _subobject_inclusion_factory is not None or (
        _subobject_ambient is not None and _subobject_generator_images is not None
    ):
        placement.append(ModuleSubobjects(base_ring))
        data.update(
            subobject_ambient=_subobject_ambient,
            subobject_generator_images=_subobject_generator_images,
            subobject_lift=_subobject_lift,
            subobject_inclusion_factory=_subobject_inclusion_factory,
            subobject_verify_linearity=_subobject_verify_linearity,
        )

    from dzack_research.preamble.owned_category import _object_of

    return _object_of(Category.join(tuple(placement)), **data)


def _tensor_label_set(factors):
    r"""Return $\prod_{i \in I} S_i$, the generating set of $\bigotimes_i M_i$.

    A generator of the tensor product is one generator chosen in each factor,
    which is a section of the family of generating sets over the index set.
    """
    return Sets().product(
        indexed_family(
            factors.index_set(),
            lambda index: factors.value(index).module_generating_set(),
        )
    )


def _tensor_pair(label_set, left_label, right_label):
    return label_set(lambda index: left_label if int(index) == 0 else right_label)


class BilinearMap(SageObject):
    r"""A bilinear map specified on the selected product framing."""

    def __init__(self, left, right, codomain, generator_images) -> None:
        if left.base_ring() != right.base_ring() or left.base_ring() != codomain.base_ring():
            raise ValueError("a bilinear map requires one common base ring")
        self._left = left
        self._right = right
        self._codomain = codomain
        self._generator_indices = _tensor_label_set(
            _factor_family((left, right), name="Tensor factors")
        )

        if isinstance(generator_images, dict):
            size = self._generator_indices.cardinality()
            if not size.is_finite():
                raise TypeError("an infinite bilinear generator assignment is specified by a callable")

            def raw_image(pair):
                ingress_key = (pair.component(0), pair.component(1))
                if ingress_key not in generator_images:
                    raise ValueError(f"bilinear generator assignment omits {ingress_key!r}")
                return generator_images[ingress_key]

            # Validate the finite syntactic assignment once, without retaining
            # a sequence-valued mathematical representation.
            for pair in self._generator_indices:
                raw_image(pair)
        elif callable(generator_images):

            def raw_image(pair):
                return generator_images(pair.component(0), pair.component(1))
        else:
            raise TypeError("a bilinear map is specified by a callable or finite assignment")

        self._generator_images = indexed_family(
            self._generator_indices,
            lambda pair: self.codomain()(raw_image(pair)),
            name="Generator images",
        )
        self._check_relations()

    def left_factor(self):
        return self._left

    def right_factor(self):
        return self._right

    def codomain(self):
        return self._codomain

    def generator_index_set(self):
        return self._generator_indices

    def generator_image(self, left_label, right_label):
        pair = _tensor_pair(
            self.generator_index_set(),
            left_label,
            right_label,
        )
        return self._generator_images[pair]

    def _check_relations(self) -> None:
        zero = self.codomain().zero()
        left = self.left_factor()
        right = self.right_factor()
        left_labels = left.module_generating_set()
        right_labels = right.module_generating_set()

        left_relations = left._selected_presentation_rows()
        if left_relations is not None:
            for row in left_relations:
                for right_label in right_labels:
                    value = sum(
                        (coefficient * self.generator_image(left_label, right_label) for left_label, coefficient in zip(left_labels, row, strict=True) if coefficient),
                        zero,
                    )
                    if value != zero:
                        raise ValueError("the bilinear map does not kill a left-factor relation")

        right_relations = right._selected_presentation_rows()
        if right_relations is not None:
            for row in right_relations:
                for left_label in left_labels:
                    value = sum(
                        (coefficient * self.generator_image(left_label, right_label) for right_label, coefficient in zip(right_labels, row, strict=True) if coefficient),
                        zero,
                    )
                    if value != zero:
                        raise ValueError("the bilinear map does not kill a right-factor relation")

    def __call__(self, left_element, right_element):

        left_coefficients = self.left_factor().framing_coefficients(left_element)
        right_coefficients = self.right_factor().framing_coefficients(right_element)
        return sum(
            (
                left_coefficient * right_coefficient * self.generator_image(left_label, right_label)
                for left_label, left_coefficient in left_coefficients.items()
                for right_label, right_coefficient in right_coefficients.items()
            ),
            self.codomain().zero(),
        )

    def _repr_(self) -> str:
        return f"Bilinear map {self.left_factor()} x {self.right_factor()} -> {self.codomain()}"



class TensorProductModules(OwnedCategoryOverBaseRing):
    r"""Modules carrying a selected tensor-product universal object."""

    def an_object(self):
        r"""The tensor square of the free module of rank one."""
        free = Modules(self.base_ring()).an_object()
        return Modules(self.base_ring()).tensor_product((free, free))

    @classmethod
    def _repr_object_names(cls):
        return "chosen tensor-product modules"

    def super_categories(self):
        return [Modules(self.base_ring())]

    class ParentMethods:
        def __init__(self, tensor_factors, **rest) -> None:
            self._preamble_tensor_factors = tensor_factors
            super().__init__(**rest)

        def _module_homset_class(self):

            return TensorProductModuleHomset

        def tensor_factors(self):
            r"""Return the family of factors, indexed by the product's own index set."""

            return _finite_factor_family(self._preamble_tensor_factors, name="Tensor factors")

        def tensor_factor(self, index):
            return self.tensor_factors()[index]

        def _two_factors(self):
            r"""The two factors, where the universal map of this product is bilinear.

            A tensor product over an index set of any size is constructed
            here, but its universal multilinear map is represented only for
            two factors, because ``BilinearMap`` is the only multilinear map
            the preamble owns.
            """
            factors = self.tensor_factors()
            assert factors.cardinality() == cardinal(2), (
                "the universal map of a tensor product is represented here only "
                "for two factors, where it is a bilinear map"
            )
            return self.tensor_factor(0), self.tensor_factor(1)

        def pure_tensor(self, left_element, right_element):
            r"""Return the universal pure tensor of two elements."""
            left, right = self._two_factors()

            left_coefficients = left.framing_coefficients(left_element)
            right_coefficients = right.framing_coefficients(right_element)
            labels = self.module_generating_set()
            return self.linear_combination(
                {
                    _tensor_pair(labels, left_label, right_label): left_coefficient * right_coefficient
                    for left_label, left_coefficient in left_coefficients.items()
                    for right_label, right_coefficient in right_coefficients.items()
                    if left_coefficient * right_coefficient
                }
            )

        def universal_bilinear_map(self):
            left, right = self._two_factors()
            labels = self.module_generating_set()
            return BilinearMap(
                left,
                right,
                self,
                lambda left_label, right_label: self.module_generator(_tensor_pair(labels, left_label, right_label)),
            )

        def from_bilinear_map(self, codomain, bilinear):
            r"""The unique linear map induced by an R-bilinear evaluation."""
            left, right = self._two_factors()
            return self.from_bilinear(BilinearMap(
                left, right, codomain,
                lambda i, j: bilinear(left.module_generator(i), right.module_generator(j)),
            ))

        def from_bilinear(self, bilinear):
            left, right = self._two_factors()
            if bilinear.left_factor() is not left or bilinear.right_factor() is not right:
                raise ValueError("the bilinear map has different tensor factors")

            return self.module_category().Mor(self, bilinear.codomain())(
                lambda pair: bilinear.generator_image(
                    pair.component(0),
                    pair.component(1),
                )
            )


def _represented_finite_presentation(module) -> bool:
    r"""Return whether ``module`` carries selected finite presentation data."""
    return module in ModulesWithChosenFinitePresentation(module.base_ring())


def _represented_framed_free(module) -> bool:
    r"""Return whether ``module`` carries the framed free construction.

    Membership, not ``is_framed_module() and is_free()``.  Those two are true of
    every module that happens to be framed and free -- the zero presented
    module is one, and it is the discriminant module of a unimodular lattice
    -- while the backend they were standing in for is the one a module gets
    by being *constructed* free.
    """
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
        FramedFreeModules,
    )

    return module in FramedFreeModules(module.base_ring())


@cached_function(key=lambda factors: (factors.index_set(), tuple(map(id, factors))))
def _module_tensor_product(factors):
    r"""Return $\bigotimes_{i \in I} M_i$ over the family's own index set."""
    return _module_tensor_product_with_data(factors)


def _module_tensor_product_with_data(
    factors,
    *,
    extra_categories=(),
    extra_construction_data=None,
):
    r"""Construct a represented tensor product with additional owned structure."""
    values = tuple(factors)
    assert values, "a tensor product is taken over a nonempty family of factors"
    ring = _owned_ring(values[0].base_ring())
    assert all(_owned_ring(factor.base_ring()) == ring for factor in values), (
        "a tensor product requires one common base ring"
    )

    represented_free = all(_represented_framed_free(factor) for factor in values)
    represented_presented = all(
        _represented_finite_presentation(factor) for factor in values
    )
    if not represented_free and not represented_presented:
        from dzack_research.preamble.categories.modules.tensor_quotients import _tensor_quotient

        return _tensor_quotient(
            factors, extra_categories=extra_categories,
            extra_construction_data=extra_construction_data,
        )

    tensor_labels = _tensor_label_set(factors)

    if represented_free:
        construction_data = {"tensor_factors": factors}
        if extra_construction_data is not None:
            construction_data.update(extra_construction_data)
        return ring._fresh_free_module_on(
            tensor_labels,
            _extra_categories=(TensorProductModules(ring), *tuple(extra_categories)),
            _extra_construction_data=construction_data,
        )

    label_sets = tuple(factor.module_generating_set() for factor in values)
    if not all(labels.cardinality().is_finite() for labels in label_sets):
        raise TypeError("the selected presentation backend requires finite framings")

    width = int(tensor_labels.cardinality().finite_value())
    ranking = factors.index_set().ranking_map()
    rows = []

    # A relation of one factor, tensored with a generator chosen in each of
    # the others, is a relation of the product; over a family of presented
    # modules those exhaust the relations of the tensor product.
    for position, factor_labels in enumerate(label_sets):
        elsewhere_sets = tuple(
            labels for other, labels in enumerate(label_sets) if other != position
        )
        for relation in values[position]._selected_presentation_rows() or ():
            for elsewhere in itertools.product(*elsewhere_sets):
                row = [ring.zero()] * width
                for label_position, coefficient in enumerate(relation):
                    if coefficient:
                        section = (
                            elsewhere[:position]
                            + (factor_labels[label_position],)
                            + elsewhere[position:]
                        )
                        label = tensor_labels(
                            lambda place, section=section: section[int(ranking(place))]
                        )
                        row[tensor_labels.ranking_map()(label)] = coefficient
                rows.append(row)

    result = NotImplemented
    construction_data = {"tensor_factors": factors}
    if extra_construction_data is not None:
        construction_data.update(extra_construction_data)
    for presentation_owner in values:
        result = presentation_owner._presented_module_from_relation_rows(
            tensor_labels,
            rows,
            extra_categories=(TensorProductModules(ring), *tuple(extra_categories)),
            extra_construction_data=construction_data,
        )
        if result is not NotImplemented:
            break
    if result is NotImplemented:
        raise NotImplementedError("the selected tensor-product presentation has no represented quotient constructor")
    return result


def _biproduct_label_set(factors):
    r"""Return $\coprod_{i \in I} S_i$, the generating set of $\bigoplus_i M_i$.

    A generator of the biproduct is a generator of exactly one factor,
    remembering which; that is a point of the coproduct of the family of
    generating sets over the index set.
    """
    return Sets().coproduct(
        indexed_family(
            factors.index_set(),
            lambda index: factors.value(index).module_generating_set(),
        )
    )


def _biproduct_label(label_set, index, label):
    return label_set(index, label)


class BiproductModules(OwnedCategoryOverBaseRing):
    def an_object(self):
        r"""The biproduct of the free module of rank one with itself."""
        free = Modules(self.base_ring()).an_object()
        return Modules(self.base_ring()).biproduct((free, free))

    @classmethod
    def _repr_object_names(cls):
        return "chosen module biproducts"

    def super_categories(self):
        from dzack_research.preamble.categories.abstract_categories.direct_sum_objects import (
            DirectSumObjects,
        )

        return [DirectSumObjects(Modules(self.base_ring()))]

    class ParentMethods:
        _derived_construction_parameters = frozenset({"summands"})

        def __init__(self, biproduct_factors, **rest) -> None:
            self._preamble_biproduct_factors = biproduct_factors
            super().__init__(summands=biproduct_factors, **rest)

        def biproduct_factors(self):
            return self._preamble_biproduct_factors

        def biproduct_factor(self, index):
            return self.biproduct_factors()[index]

        def injection(self, index):
            r"""Return \(\iota_i : M_i \to \bigoplus_{j \in I} M_j\).

            A biproduct is a coproduct, so it has one injection per index, and
            each is an arrow out of that factor itself.
            """
            summand = self.biproduct_factor(index)
            labels = self.module_generating_set()
            return summand.module_category().Mor(summand, self)(
                lambda label: self.module_generator(_biproduct_label(labels, index, label))
            )

        def projection(self, index):
            r"""Return \(\pi_i : \bigoplus_{j \in I} M_j \to M_i\)."""
            summand = self.biproduct_factor(index)
            place = self.module_generating_set().index_set()(index)

            def image(label):
                if label.summand_index() == place:
                    return summand.module_generator(label.summand_element())
                return summand.zero()

            return self.module_category().Mor(self, summand)(image)

        def left_inclusion(self):
            r"""Return \(\iota_0\), the injection at the first index."""
            return self.injection(0)

        def right_inclusion(self):
            r"""Return \(\iota_1\), the injection at the second index."""
            return self.injection(1)

        left_injection = left_inclusion
        right_injection = right_inclusion

        def left_projection(self):
            r"""Return \(\pi_0\), the projection at the first index."""
            return self.projection(0)

        def right_projection(self):
            r"""Return \(\pi_1\), the projection at the second index."""
            return self.projection(1)

        def from_coproduct_cocone(self, legs):
            r"""The unique map \(\bigoplus_i M_i \to X\) with the stated legs.

            A cocone under the biproduct is the family of legs
            \(f_i : M_i \to X\), indexed the way the factors are, so that is
            the datum this takes.  A generator of the biproduct lies in one
            factor and remembers which, so its image is the value of that
            index's leg.
            """
            factors = self.biproduct_factors()
            legs = _finite_factor_family(legs, name="Coproduct cocone legs")
            assert legs.index_set() == factors.index_set(), (
                "a cocone under a biproduct has one leg per factor"
            )
            target = legs[factors.index_set().ranking_map().inverse()(0)].codomain()
            assert all(leg.codomain() is target for leg in legs), (
                "a cocone has one apex"
            )
            assert all(
                legs.value(index).domain() is factors.value(index)
                for index in factors.index_set()
            ), "each leg of the cocone starts at its own factor"

            return self.module_category().Mor(self, target)(
                lambda label: legs.value(label.summand_index())(
                    factors.value(label.summand_index()).module_generator(
                        label.summand_element()
                    )
                )
            )

        def from_product_cone(self, legs):
            r"""The unique map \(X \to \prod_i M_i\) with the stated legs.

            A cone over the biproduct is the family of legs
            \(f_i : X \to M_i\), indexed the way the factors are.  The image
            of a generator of the apex is the sum over the index set of the
            coordinates of its images, each placed at its own index.
            """
            factors = self.biproduct_factors()
            legs = _finite_factor_family(legs, name="Product cone legs")
            assert legs.index_set() == factors.index_set(), (
                "a cone over a biproduct has one leg per factor"
            )
            source = legs[factors.index_set().ranking_map().inverse()(0)].domain()
            assert all(leg.domain() is source for leg in legs), "a cone has one apex"
            assert all(
                legs.value(index).codomain() is factors.value(index)
                for index in factors.index_set()
            ), "each leg of the cone lands in its own factor"

            labels = self.module_generating_set()

            def image(source_label):
                generator = source.module_generator(source_label)
                coefficients = {}
                for index in factors.index_set():
                    for target_label, coefficient in factors.value(index).framing_coefficients(legs.value(index)(generator)).items():
                        coefficients[_biproduct_label(labels, index, target_label)] = coefficient
                return self.linear_combination(coefficients)

            return source.module_category().Mor(source, self)(image)

        def from_summands(self, left_map, right_map):
            r"""Return the unique map ``self -> X`` extending both summand maps."""
            return self.from_coproduct_cocone((left_map, right_map))

        def to_product(self, left_map, right_map):
            r"""Return the unique map ``X -> self`` with the specified projections."""
            return self.from_product_cone((left_map, right_map))


@cached_function(key=lambda factors: (factors.index_set(), tuple(factors)))
def _module_biproduct(factors):
    r"""Return $\bigoplus_{i \in I} M_i$ over the family's own index set."""
    return _module_biproduct_with_data(factors)


def _module_biproduct_with_data(
    factors,
    *,
    extra_categories=(),
    extra_construction_data=None,
):
    r"""Construct a represented biproduct with additional owned structure."""
    values = tuple(factors)
    assert values, "a biproduct is taken over a nonempty family of factors"
    ring = _owned_ring(values[0].base_ring())
    assert all(_owned_ring(factor.base_ring()) == ring for factor in values), (
        "a biproduct requires one common base ring"
    )

    labels = _biproduct_label_set(factors)
    result = values[0]._free_biproduct_over(
        labels,
        factors,
        extra_categories=extra_categories,
        extra_construction_data=extra_construction_data,
    )
    if result is NotImplemented:
        for factor in values:
            result = factor._presented_biproduct_over(
                labels,
                factors,
                extra_categories=extra_categories,
                extra_construction_data=extra_construction_data,
            )
            if result is not NotImplemented:
                break
    if result is NotImplemented:
        raise NotImplementedError("the represented module factors provide no biproduct realization")
    return result


def _biproduct_morphism(left_morphism, right_morphism, source=None, target=None):
    if source is None:
        source = Modules(left_morphism.domain().base_ring()).biproduct(
            (left_morphism.domain(), right_morphism.domain())
        )
    if target is None:
        target = Modules(left_morphism.codomain().base_ring()).biproduct(
            (left_morphism.codomain(), right_morphism.codomain())
        )

    if source.biproduct_factor(0) is not left_morphism.domain() or source.biproduct_factor(1) is not right_morphism.domain():
        raise ValueError("the source biproduct has different factors")
    if target.biproduct_factor(0) is not left_morphism.codomain() or target.biproduct_factor(1) is not right_morphism.codomain():
        raise ValueError("the target biproduct has different factors")

    return source.module_category().Mor(source, target)(
        lambda label: (
            target.left_inclusion()(left_morphism(left_morphism.domain().module_generator(label.summand_element())))
            if int(label.summand_index()) == 0
            else target.right_inclusion()(right_morphism(right_morphism.domain().module_generator(label.summand_element())))
        )
    )


class MatrixSpaces(OwnedCategoryOverBaseRing):
    r"""Hom objects between finitely generated framed free ``R``-modules."""

    def an_object(self):
        r"""The one-by-one matrices over the base ring."""
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        modules = Modules(self.base_ring())
        free = modules.an_object()
        return modules.Mor(free, free)

    @classmethod
    def _repr_object_names(cls):
        return "matrix Hom objects"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
            FramedFreeModules,
        )

        return [
            InternalHomModules(self.base_ring()),
            FramedFreeModules(self.base_ring()).FinitelyGenerated(),
        ]

    class ParentMethods:
        def row_index_set(self):
            return self.codomain().module_generating_set()

        def column_index_set(self):
            return self.domain().module_generating_set()

        def nrows(self):
            return int(self.row_index_set().cardinality())

        def ncols(self):
            return int(self.column_index_set().cardinality())

        def matrix_shape(self):
            return self.nrows(), self.ncols()

        def matrix_unit(self, row_label, column_label):
            label = self.module_generating_set()((row_label, column_label))
            return self.module_generator(label)

        def _selected_module_coefficients(self, morphism):
            r"""The entries of a linear map, keyed by the matrix units ``(t, s)``."""
            return _matrix_coefficients(self, morphism)

        def from_rows(self, rows):
            r"""Construct the matrix morphism with the stated row entries."""
            rows = tuple(tuple(row) for row in rows)
            if len(rows) != self.nrows() or any(len(row) != self.ncols() for row in rows):
                raise ValueError(f"matrix rows have shape incompatible with {self.matrix_shape()}")
            ring = self.base_ring()
            row_labels = tuple(self.row_index_set())
            column_labels = tuple(self.column_index_set())
            images = {}
            for column_position, column_label in enumerate(column_labels):
                images[column_label] = self.codomain().linear_combination(
                    {
                        row_label: ring(rows[row_position][column_position])
                        for row_position, row_label in enumerate(row_labels)
                        if ring(rows[row_position][column_position]) != ring.zero()
                    }
                )
            return self(images)

        def from_tensor(self, coordinate_tensor):
            r"""Read a compatible type-``(1,1)`` tensor as this linear map.

            This is an explicit interpretation, not a second matrix object:
            the returned object is an element of this Hom object.
            """
            if coordinate_tensor.tensor_valence() != (NN**2)((1, 1)):
                raise TypeError("a matrix morphism is represented here by a type-(1,1) tensor")
            if coordinate_tensor.base_ring() is not self.base_ring():
                raise TypeError("the tensor and matrix Hom must have one base ring")
            # A type-(1,1) tensor represents a morphism here when its
            # contravariant index has the codomain's rank and its covariant
            # index the domain's rank.
            shape = coordinate_tensor.tensor_shape()
            if shape[0] != self.nrows() or shape[1] != self.ncols():
                raise ValueError(f"tensor shape {shape} does not match matrix shape {self.matrix_shape()}")
            return self.from_rows(tuple(tuple(coordinate_tensor[row, column] for column in range(self.ncols())) for row in range(self.nrows())))

        def from_flat_entries(self, entries):
            entries = tuple(entries)
            expected = self.nrows() * self.ncols()
            if len(entries) != expected:
                raise ValueError(f"matrix shape {self.matrix_shape()} requires {expected} entries")
            return self.from_rows(tuple(entries[row * self.ncols() : (row + 1) * self.ncols()] for row in range(self.nrows())))

    class ElementMethods:
        def nrows(self):
            return self.parent().nrows()

        def ncols(self):
            return self.parent().ncols()

        def matrix_shape(self):
            return self.parent().matrix_shape()

        def change_ring(self, ring):
            r"""Return the same finite coordinate matrix over ``ring``."""
            target = ring.matrix_space(self.parent().nrows(), self.parent().ncols())
            return target.from_rows(
                (
                    ring(self.matrix_entry(row_label, column_label))
                    for column_label in self.parent().column_index_set()
                )
                for row_label in self.parent().row_index_set()
            )

        @cached_method
        def _matrix_column_coefficients(self, column_label):
            column_label = _matrix_index(self.parent().column_index_set(), column_label)
            generator_image = self._generator_image
            image = generator_image(column_label) if generator_image is not None else self(self.domain().module_generator(column_label))
            return self.codomain().framing_coefficients(image)

        def matrix_entry(self, row_label, column_label):
            row_label = _matrix_index(self.parent().row_index_set(), row_label)
            column_label = _matrix_index(self.parent().column_index_set(), column_label)
            return self._matrix_column_coefficients(column_label).get(
                row_label,
                self.parent().base_ring().zero(),
            )

        def __getitem__(self, index):
            r"""The entry at ``(row, column)``."""
            row, column = index
            return self.matrix_entry(row, column)

        def row(self, row_label):
            row_label = _matrix_index(self.parent().row_index_set(), row_label)
            dual = self.domain().dual_module()
            return dual.linear_combination(
                {column_label: self.matrix_entry(row_label, column_label) for column_label in self.parent().column_index_set() if self.matrix_entry(row_label, column_label)}
            )

        def column(self, column_label):
            column_label = _matrix_index(self.parent().column_index_set(), column_label)
            return self(self.domain().module_generator(column_label))

        def rows(self):
            return tuple(self.row(label) for label in self.parent().row_index_set())

        def columns(self):
            return tuple(self.column(label) for label in self.parent().column_index_set())

        def determinant(self):
            if self.parent().nrows() != self.parent().ncols():
                raise ValueError("a determinant requires a square matrix")
            backend = _engine_matrix(self)
            return self.parent().base_ring()._from_engine_element(backend.det())

        det = determinant

        def multiplicative_order(self):
            r"""Return the exact multiplicative order of this square matrix when finite."""
            if self.parent().nrows() != self.parent().ncols():
                raise ValueError("multiplicative order requires a square matrix")
            order = _engine_matrix(self).multiplicative_order()
            from sage.rings.infinity import Infinity
            from sage.rings.integer_ring import ZZ as SageZZ

            if order == Infinity:
                return Infinity
            return _own_ring(SageZZ)._from_engine_element(SageZZ(order))

        def matrix_rank(self):
            from sage.rings.integer_ring import ZZ as SageZZ

            integers = _own_ring(SageZZ)
            return integers._from_engine_element(SageZZ(_engine_matrix(self).rank()))

        def solve_right(self, target):
            r"""Return ``x`` in the domain with ``self(x)=target``."""
            from sage.modules.free_module_element import vector as sage_vector

            target = target if target.parent() is self.codomain() else self.codomain()(target)
            ring = self.parent().base_ring()
            coefficients = self.codomain().framing_coefficients(target)
            rhs = sage_vector(
                _engine_ring(ring),
                [_engine_element(ring, coefficients.get(label, ring.zero())) for label in self.parent().row_index_set()],
            )
            solution = _engine_matrix(self).solve_right(rhs)
            return self.domain().linear_combination(
                {label: ring._from_engine_element(solution[position]) for position, label in enumerate(self.parent().column_index_set()) if solution[position]}
            )

        def _kernel_spanning_family(self):
            r"""Return a private owned finite family spanning ``ker(self)``."""

            ring = self.parent().base_ring()
            if ring in LocalizationRings():
                source_ring = ring.localization_source()
                row_labels = self.parent().row_index_set()
                column_labels = self.parent().column_index_set()
                entries = tuple(
                    tuple(self.matrix_entry(row_label, column_label) for column_label in column_labels)
                    for row_label in row_labels
                )
                fractions = tuple(
                    tuple(ring.localization_fraction_data(entry) for entry in row)
                    for row in entries
                )
                denominators = tuple(
                    denominator
                    for row in fractions
                    for _numerator, denominator in row
                )

                cleared_rows = []
                for row in fractions:
                    cleared_row = []
                    for numerator, denominator in row:
                        multiplier = source_ring.one()
                        skipped = False
                        for candidate in denominators:
                            if not skipped and candidate == denominator:
                                skipped = True
                                continue
                            multiplier *= candidate
                        cleared_row.append(numerator * multiplier)
                    cleared_rows.append(tuple(cleared_row))

                source_domain = source_ring._fresh_free_module_on(column_labels)
                source_codomain = source_ring._fresh_free_module_on(row_labels)
                source_map = source_domain.module_category().Mor(source_domain, source_codomain).from_rows(
                    tuple(cleared_rows)
                )
                source_kernel = source_map.kernel()
                kernel_labels = source_kernel.module_generating_set()
                inclusion = source_kernel.inclusion()
                localized_domain = self.domain()
                localization_map = ring.localization_map()

                return finite_indexed_family(
                    kernel_labels,
                    lambda label: localized_domain.linear_combination(
                        {
                            column_label: localization_map(coefficient)
                            for column_label, coefficient in source_domain.framing_coefficients(inclusion(source_kernel.module_generator(label))).items()
                            if coefficient
                        }
                    ),
                    name=f"Localized kernel spanning family of {self}",
                )

            basis = _engine_matrix(self).right_kernel().basis_matrix()
            labels = self.parent().column_index_set()
            positions = Sets.Δ[int(basis.nrows()) - 1]
            return finite_indexed_family(
                positions,
                lambda position: self.domain().linear_combination(
                    {label: ring._from_engine_element(basis[int(position), column]) for column, label in enumerate(labels) if basis[int(position), column]}
                ),
                name=f"Kernel spanning family of {self}",
            )

        def list(self):
            ring = self.parent().base_ring()
            rows = tuple(self.parent().row_index_set())
            columns = tuple(self.parent().column_index_set())
            column_coefficients = {column_label: self._matrix_column_coefficients(column_label) for column_label in columns}
            return [column_coefficients[column_label].get(row_label, ring.zero()) for row_label in rows for column_label in columns]

        def transpose(self):

            source = self.codomain()
            codomain = self.domain()
            target = source.module_category().Mor(source, codomain)
            _refine_matrix_hom(target)
            return target.from_rows(
                tuple(tuple(self.matrix_entry(row_label, column_label) for row_label in self.parent().row_index_set()) for column_label in self.parent().column_index_set())
            )

        T = transpose

        def inverse(self):
            r"""Return the inverse matrix morphism with reversed endpoints."""
            if self.parent().nrows() != self.parent().ncols():
                raise ValueError("a matrix inverse requires a square matrix")

            backend = _engine_matrix(self).inverse()
            ring = self.parent().base_ring()
            source = self.codomain()
            codomain = self.domain()
            target = _refine_matrix_hom(source.module_category().Mor(source, codomain))
            return target.from_rows((ring._from_engine_element(backend[row, column]) for column in range(target.ncols())) for row in range(target.nrows()))

        __invert__ = inverse

        def __matmul__(self, other):

            result = ModuleMorphism.__mul__(self, other)
            if result is NotImplemented:
                raise ValueError("matrix shapes are not composable")
            return result

        def smith_form(self):
            r"""Return ``(D,U,V)`` from invariant-factor presentation normalization."""

            ring = self.parent().base_ring()
            if ring not in PrincipalIdealDomains():
                raise NotImplementedError(f"Smith normal form is guaranteed here only over a PID, not {ring}")
            presented = self.codomain()._represented_cokernel_of_morphism(self)
            if presented is NotImplemented:
                raise NotImplementedError("Smith normalization requires a represented presentation quotient")
            normalization = presented.invariant_factor_presentation()
            diagonal = normalization.codomain().arrow()
            # For a square in Arr(Mod_R), right * original = diagonal * left.
            # Thus D = right * A * left^{-1} in matrix notation.
            left_change = normalization.forward().right()
            right_change = normalization.inverse().left()
            return diagonal, left_change, right_change

        def smith_normal_form(self):
            return self.smith_form()[0]

        def invariant_factors(self):
            diagonal = self.smith_normal_form()
            zero = self.parent().base_ring().zero()
            return tuple(diagonal[index, index] for index in range(min(diagonal.parent().nrows(), diagonal.parent().ncols())) if diagonal[index, index] != zero)


class MatrixEndomorphismSpaces(OwnedCategoryOverBaseRing):
    r"""The matrix realization of ``End_R(F)`` for a finite framed free module ``F``."""

    def an_object(self):
        r"""The endomorphisms of the free module of rank one."""
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        modules = Modules(self.base_ring())
        free = modules.an_object()
        return modules.Mor(free, free)

    @classmethod
    def _repr_object_names(cls):
        return "matrix endomorphism objects"

    def super_categories(self):
        from dzack_research.preamble.categories.algebras.algebras import (
            Algebras,
        )

        # ``MatrixSpaces`` states only the linear half; the ring structure of
        # End_R(F) under composition arrives with the associative unital
        # algebras.
        return [
            MatrixSpaces(self.base_ring()),
            Algebras(self.base_ring()).Associative().Unital(),
        ]

    # The two above state two different morphisms, so this names which of
    # them End_R(F) means: the one that preserves everything it is.
    _HomCategory = AssociativeAlgebraHomCategoryConstruction

    class ParentMethods:
        def is_commutative(self):
            r"""Return whether \(\operatorname{End}_R(F)\cong M_n(R)\) commutes.

            The base is not assumed commutative here, so the answer depends on
            both the ring and the rank, and each rank is its own statement.

            Rank zero gives the zero ring, which commutes whatever \(R\) is.
            Rank one gives \(R\) acting on itself, whose endomorphisms are the
            right multiplications, so it commutes exactly when \(R\) does; a
            ring that does not decide its own commutativity leaves this
            undecided too, and says so through the answer it gives.  From rank
            two the matrix units satisfy \(e_{11}e_{12}=e_{12}\) and
            \(e_{12}e_{11}=0\), so commuting forces \(e_{12}=0\) and hence
            \(1=0\): the ring commutes exactly when \(R\) is the zero ring.
            """
            ring = self.base_ring()
            match self.nrows():
                case 0:
                    return True
                case 1:
                    return ring.is_commutative()
                case _:
                    return ring.one() == ring.zero()

        def identity_matrix(self):
            return self.identity()

        def diagonal(self, entries):
            values = tuple(entries)
            labels = tuple(self.column_index_set())
            if len(values) != len(labels):
                raise ValueError("a diagonal needs one scalar per framing element")
            ring = self.base_ring()
            return self(
                {
                    label: self.codomain().scalar_multiple(
                        ring(values[position]),
                        self.codomain().module_generator(label),
                    )
                    for position, label in enumerate(labels)
                }
            )

    class ElementMethods:
        def is_unit(self) -> bool:
            r"""Return whether this endomorphism is invertible in \(\operatorname{End}_R(M)\).

            A unit of a ring is an element with a two-sided inverse in it, and
            an endomorphism has one in \(\operatorname{End}_R(M)\) exactly when
            it is an isomorphism of \(M\): a bijective linear map has a
            set-theoretic inverse, that inverse is linear, and the two compose
            to the identity on either side.  So this is decided as injectivity
            together with surjectivity, which are the kernel and the cokernel
            of the morphism, and not from a determinant -- that is a criterion
            for the special case of a finite free module, carrying hypotheses
            the definition of a unit does not.

            Reading the units of \(\operatorname{End}_R(M)\) is what gives
            \(\operatorname{Aut}_R(M)\) its group structure, through the unit
            group functor on the owned ring category.
            """
            return self.is_injective() and self.is_surjective()

        def trace(self):
            ring = self.parent().base_ring()
            return sum(
                (self.matrix_entry(label, label) for label in self.parent().row_index_set()),
                ring.zero(),
            )


def _matrix_index(index_set, key):
    r"""Read a row or column key as a label of ``index_set``, or as the position of a label."""
    return index_set(key) if key in index_set else index_set[operator.index(key)]


def _engine_matrix(morphism):
    r"""Privately materialize one matrix-Hom element in Sage."""
    from sage.matrix.constructor import matrix as sage_matrix

    parent = _refine_matrix_hom(morphism.parent())
    if parent not in MatrixSpaces(parent.base_ring()):
        raise TypeError("backend matrix materialization requires a matrix Hom element")
    ring = parent.base_ring()
    return sage_matrix(
        _engine_ring(ring),
        parent.nrows(),
        parent.ncols(),
        [_engine_element(ring, entry) for entry in morphism.list()],
    )


def _matrix_unit(homset, label):
    label = homset.module_generating_set()(label)
    row_label = label[0]
    column_label = label[1]
    column_labels = homset.column_index_set()
    return homset(
        {source_label: (homset.codomain().module_generator(row_label) if source_label == column_label else homset.codomain().zero()) for source_label in column_labels}
    )


def _matrix_coefficients(homset, morphism):

    morphism = homset(morphism)
    labels = homset.module_generating_set()
    coefficients = {}
    for column_label in homset.column_index_set():
        for row_label, coefficient in morphism._matrix_column_coefficients(column_label).items():
            coefficients[labels((row_label, column_label))] = coefficient
    return coefficients


def _refine_matrix_hom(homset):
    r"""Return the already-constructed matrix Hom for finite free endpoints."""
    ring = homset.base_ring()
    domain = homset.domain()
    codomain = homset.codomain()
    if not (_coordinate_framed_free_module(domain, ring) and _coordinate_framed_free_module(codomain, ring)):
        return homset
    assert homset in MatrixSpaces(ring), "a Hom between coordinate framed free modules is constructed as a matrix Hom"
    return homset


def _coordinate_framed_free_module(module, ring) -> bool:
    r"""Whether the selected framing is a finite basis, independently of its engine.

    Freeness of the underlying module does not say that an arbitrary chosen
    generating family is a basis.  ``FramedFreeModules`` supplies that stronger
    datum; finite cardinality supplies the finite matrix calculation.
    """
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
        FramedFreeModules,
    )

    return (
        module in FramedFreeModules(ring)
        and module.module_generating_set().cardinality().is_finite()
    )


def _torsion_module_presented_by_matrix(
    relations, module_generating_set=None, *, base_ring=None
):
    r"""Return the torsion module presented by relation rows ``relations``."""

    ring = _own_ring(SageZZ) if base_ring is None else base_ring
    match relations:
        case _ if element_parent(relations) in MatrixSpaces(ring):
            width = relations.parent().ncols()
            relation_count = relations.parent().nrows()
        case _:
            rows = tuple(tuple(row) for row in relations)
            relation_count = len(rows)
            width = 0 if not rows else len(rows[0])
            relations = ring.matrix_space(relation_count, width).from_rows(rows)
    labels = (
        finite_ordered_set(range(width))
        if module_generating_set is None
        else finite_ordered_set(module_generating_set)
    )
    if labels.cardinality() != width:
        raise ValueError(
            "the module-generating set and relation matrix have different widths"
        )
    target = ring.free_module(labels)
    source = ring.free_module(relation_count)

    def relation_entry(row_position, column_position):
        row_label = relations.parent().row_index_set()[row_position]
        column_label = relations.parent().column_index_set()[column_position]
        return relations.matrix_entry(row_label, column_label)

    def relation_image(row_position):
        return target.linear_combination(
            {
                label: relation_entry(row_position, column_position)
                for column_position, label in enumerate(labels)
                if relation_entry(row_position, column_position)
            }
        )

    images = {
        source_label: relation_image(row_position)
        for row_position, source_label in enumerate(source.module_generating_set())
    }
    return Modules(ring).FinitelyPresented().Torsion()(
        source.module_category().Mor(source, target)(images)
    )


def _refine_finitely_presented_torsion_module(module):
    r"""Attach the torsion intersection after verifying the represented property."""

    ring = module.base_ring()
    if module not in Modules(ring).FinitelyPresented():
        raise TypeError("torsion refinement requires a finitely presented module")
    if not module.is_torsion():
        raise ValueError(
            "the supplied finite presentation does not present a torsion module"
        )
    return refine(module, Modules(ring).FinitelyPresented().Torsion())
