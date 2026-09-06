"""Owned categories of modules and vector spaces."""

import operator
from dataclasses import dataclass

from sage.categories.action import Action
from sage.categories.category import Category
from sage.categories.morphism import SetMorphism
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.unknown import Unknown
from sage.structure.element import ModuleElement
from sage.structure.parent import Parent
from sage.structure.richcmp import richcmp
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.constructions import (
    Biproduct,
    Subobjects,
)
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    EndCategoryConstruction,
    HomCategoryConstruction,
    _category_homset,
)
from dzack_research.preamble.categories.abstract_categories.products import _finite_factor_family
from dzack_research.preamble.categories.group.magmas import AdditiveGroups
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleHomset,
    ModuleMorphism,
    TensorProductModuleHomset,
    framing_morphism,
    module_coefficients,
    module_embedding,
    module_homset,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    IntegralDomains,
    LocalizationRings,
    LocalRings,
    OwnedCategoryOverBaseRing,
    OwnedRings,
    PrincipalIdealDomains,
    _engine_element,
    _engine_ring,
    _own_ring,
    _owned_ring,
    _proper_restriction_base_ring,
    ring_morphism,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.indexed_families import (
    IndexedFamily,
    finite_indexed_family,
    indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import (
    NN,
    CartesianProductOfFamily,
    CoproductOfFamily,
    Sets,
)
from dzack_research.preamble.refine import realize_owned_category


class _ModuleScalarAction(Action):
    r"""The selected scalar action of the base ring on one module parent."""

    def __init__(self, scalar_parent, module, is_left) -> None:
        self._module = module
        Action.__init__(self, scalar_parent, module, is_left, operator.mul)

    def _act_(self, scalar, element):
        return self._module.scalar_multiple(scalar, element)


def register_module_scalar_action(module) -> None:
    r"""Register ordinary ``r*m``/``m*r`` syntax for an owned module parent."""
    scalar_parent = module.base_ring()
    module.register_action(_ModuleScalarAction(scalar_parent, module, True))
    module.register_action(_ModuleScalarAction(scalar_parent, module, False))


class ModuleHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):

        return ModuleHomset

    def fixed_category_class_for(self, domain, codomain):
        return domain._module_homset_class()


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
        from dzack_research.preamble.categories.algebras.group_algebras import GroupAlgebra

        return GroupAlgebra(self.base_ring(), group).augmentation()

    def trivial_action(self, group):
        r"""``Triv_G : Modules(R) -> Modules(R[G])``, restriction along the augmentation."""
        return self.restriction_of_scalars(self._augmentation(group))

    def trivial_invariants_adjunction(self, group):
        r"""``Triv_G -| (-)^G``, restriction/coextension along the augmentation."""
        return self.restriction_coextension_adjunction(self._augmentation(group))

    def _call_(self, module, scalar_action):
        r"""The ``R``-module on the additive group of ``module`` with the action ``rho: R -> End(M)``.

        An ``R``-module is an abelian group with a ring morphism ``R -> End(M)``;
        the abelian group here is that of ``module``, an object of any module
        category, and ``scalar_action`` is that morphism.
        """
        from dzack_research.preamble.categories.modules.general_modules import GeneralModule

        assert _owned_ring(scalar_action.domain()) is self.base_ring(), f"the scalar action must be a ring morphism out of {self.base_ring()}"
        assert scalar_action.codomain().domain() is module, f"the scalar action must land in the endomorphisms of {module}"
        return GeneralModule(
            self.base_ring(),
            module,
            addition=lambda left, right: left + right,
            zero=module.zero(),
            negation=lambda element: -element,
            rho=scalar_action,
        )

    # Scalar change along a ring morphism ``f: R -> S``: the adjoint triple
    # ``S tensor_R - -| Res_f -| Hom_R(S, -)``, each functor spelled on its
    # domain category and each adjunction on its left adjoint's domain.

    def scalar_extension(self, ring_map):
        r"""``S tensor_R - : Modules(R) -> Modules(S)`` along ``ring_map: R -> S``."""
        from dzack_research.preamble.categories.functors.scalar_change import (
            ScalarExtensionFunctor,
        )

        assert _owned_ring(ring_map.domain()) is self.base_ring()
        return ScalarExtensionFunctor(ring_map)

    def restriction_of_scalars(self, ring_map):
        r"""``Res_f : Modules(S) -> Modules(R)`` along ``ring_map: R -> S``.

        Along the augmentation ``R[G] -> R`` this is the trivial action.
        """
        from dzack_research.preamble.categories.functors.group_actions import (
            TrivialActionFunctor,
            is_augmentation_of_group_algebra,
        )
        from dzack_research.preamble.categories.functors.scalar_change import (
            RestrictionOfScalarsFunctor,
        )

        assert _owned_ring(ring_map.codomain()) is self.base_ring()
        match ring_map:
            case _ if is_augmentation_of_group_algebra(ring_map):
                return TrivialActionFunctor(ring_map)
            case _:
                return RestrictionOfScalarsFunctor(ring_map)

    def coextension_of_scalars(self, ring_map):
        r"""``Hom_R(S, -) : Modules(R) -> Modules(S)`` along ``ring_map: R -> S``."""
        from dzack_research.preamble.categories.functors.scalar_change import (
            CoextensionOfScalarsFunctor,
        )

        assert _owned_ring(ring_map.domain()) is self.base_ring()
        return CoextensionOfScalarsFunctor(ring_map)

    def base_change_adjunction(self, ring_map):
        r"""``S tensor_R - -| Res_f`` along ``ring_map: R -> S``."""
        from dzack_research.preamble.categories.functors.scalar_change import (
            base_change_adjunction,
        )

        assert _owned_ring(ring_map.domain()) is self.base_ring()
        return base_change_adjunction(ring_map)

    def restriction_coextension_adjunction(self, ring_map):
        r"""``Res_f -| Hom_R(S, -)`` along ``ring_map: R -> S``.

        Along the augmentation ``R[G] -> R`` this is ``Triv_G -| (-)^G``.
        """
        from dzack_research.preamble.categories.functors.group_actions import (
            TrivialInvariantsAdjunction,
            is_augmentation_of_group_algebra,
        )
        from dzack_research.preamble.categories.functors.scalar_change import (
            restriction_coextension_adjunction,
        )

        assert _owned_ring(ring_map.codomain()) is self.base_ring()
        match ring_map:
            case _ if is_augmentation_of_group_algebra(ring_map):
                return TrivialInvariantsAdjunction(ring_map)
            case _:
                return restriction_coextension_adjunction(ring_map)

    class SubcategoryMethods:
        r"""Constructions this category owns, reachable from any subcategory."""

        def tensor_product(self, factors):
            r"""Return the tensor product of a finite family of objects of this category."""
            return self._fold_construction(self._categorical_tensor_product, factors, name="Tensor product factors")

        def _categorical_tensor_product(self, left, right):
            if left not in self or right not in self:
                raise TypeError("a module tensor product requires two modules over one ring")
            return _module_tensor_product(left, right)

        def biproduct(self, factors):
            r"""Return the biproduct of a finite family of objects of this category."""
            return self._fold_construction(self._categorical_biproduct, factors, name="Biproduct factors")

        def _categorical_biproduct(self, left, right):
            if left not in self or right not in self:
                raise TypeError("a module biproduct requires two modules over one ring")
            return _module_biproduct(left, right)

        def product(self, factors):
            r"""Return the product of a finite family of objects of this category."""
            return self._fold_construction(self._categorical_product, factors, name="Product factors")

        def _categorical_product(self, left, right):
            return self._categorical_biproduct(left, right)

        def coproduct(self, factors):
            r"""Return the coproduct of a finite family of objects of this category."""
            return self._fold_construction(self._categorical_coproduct, factors, name="Coproduct factors")

        def _categorical_coproduct(self, left, right):
            return self._categorical_biproduct(left, right)

        def equalizer(self, left_arrow, right_arrow):
            r"""Return the equalizer of a parallel pair."""
            return self._categorical_equalizer(left_arrow, right_arrow)

        def coequalizer(self, left_arrow, right_arrow):
            r"""Return the coequalizer of a parallel pair."""
            return self._categorical_coequalizer(left_arrow, right_arrow)

        def _categorical_equalizer(self, left_morphism, right_morphism):
            r"""Realize an equalizer in ``R-Mod`` as ``ker(left-right)``."""
            if (
                left_morphism.domain() not in self
                or left_morphism.codomain() not in self
                or left_morphism.domain() is not right_morphism.domain()
                or left_morphism.codomain() is not right_morphism.codomain()
            ):
                raise ValueError("module equalizer arrows must be parallel R-linear maps")
            return (left_morphism - right_morphism).kernel()

        def _categorical_coequalizer(self, left_morphism, right_morphism):
            r"""Realize a coequalizer in ``R-Mod`` as ``coker(left-right)``."""
            if (
                left_morphism.domain() not in self
                or left_morphism.codomain() not in self
                or left_morphism.domain() is not right_morphism.domain()
                or left_morphism.codomain() is not right_morphism.codomain()
            ):
                raise ValueError("module coequalizer arrows must be parallel R-linear maps")
            return (left_morphism - right_morphism).cokernel()

        def equalizer_of_family(self, arrows):
            r"""Return the wide equalizer of a family of parallel arrows."""
            return self._categorical_equalizer_family(arrows)

        def coequalizer_of_family(self, arrows):
            r"""Return the wide coequalizer of a family of parallel arrows."""
            return self._categorical_coequalizer_family(arrows)

        def _categorical_equalizer_family(self, morphisms):
            r"""Realize a finite wide equalizer through kernels/intersections."""
            size = morphisms.cardinality()
            if not size.is_finite():
                raise NotImplementedError("the represented module wide-equalizer backend requires a finite arrow family")
            count = int(size.finite_value())
            if count == 0:
                raise ValueError("a wide equalizer family must be nonempty")
            reference = morphisms.unrank(0)
            equalizer = self._categorical_equalizer(reference, reference)
            for position in range(1, count):
                equalizer = equalizer.intersection(self._categorical_equalizer(morphisms.unrank(position), reference))
            return equalizer

        def _categorical_coequalizer_family(self, morphisms):
            r"""Realize a finite wide coequalizer through images/sums/cokernels."""
            size = morphisms.cardinality()
            if not size.is_finite():
                raise NotImplementedError("the represented module wide-coequalizer backend requires a finite arrow family")
            count = int(size.finite_value())
            if count == 0:
                raise ValueError("a wide coequalizer family must be nonempty")
            reference = morphisms.unrank(0)
            relations = (reference - reference).image()
            for position in range(1, count):
                relations = relations.sum((morphisms.unrank(position) - reference).image())
            return relations.inclusion().cokernel()

        def _categorical_product_morphism(self, left_morphism, right_morphism, source, target):
            return biproduct_morphism(left_morphism, right_morphism, source=source, target=target)

        _categorical_coproduct_morphism = _categorical_product_morphism

    @classmethod
    def _repr_object_names(cls):
        return "modules"

    def an_object(self):
        r"""The free module of rank one, which is the base ring itself."""
        from dzack_research.preamble.categories.functors.free_forgetful import FreeModuleFunctor
        from dzack_research.preamble.categories.sets.set_categories import finite_ordinal_set

        return FreeModuleFunctor(self.base_ring())(finite_ordinal_set(1))

    def super_categories(self):
        base = _proper_restriction_base_ring(self.base_ring())
        if base is not None:
            return [Modules(base)]
        return [AdditiveGroups().AdditiveCommutative()]

    def Mor(self, domain, codomain):
        r"""Return the unique Hom-set ``Hom_R(domain,codomain)``."""
        if domain not in self or codomain not in self:
            raise TypeError("an R-module Hom requires two R-modules")
        return self.HomCategory().Of(domain, codomain)

    def _hom_parent_placement(self, domain, codomain, *, full_internal_hom=False):
        r"""Return the category chosen when the canonical module Hom is constructed."""
        ring = self.base_ring()
        placement = [InternalHomModules(ring) if full_internal_hom else LinearHomModules(ring)]
        free = FinitelyGeneratedFreeModules(ring)
        matrix = (
            domain in free
            and codomain in free
            and callable(getattr(domain, "_preamble_free_module_constructor", None))
            and callable(getattr(codomain, "_preamble_free_module_constructor", None))
            and callable(getattr(domain, "module_generating_set", None))
            and callable(getattr(codomain, "module_generating_set", None))
        )
        if matrix:
            placement.append(MatrixSpaces(ring))
            if domain is codomain:
                if ring in OwnedRings().Commutative():
                    from dzack_research.preamble.categories.algebras.algebras import (
                        MatrixAlgebras,
                    )

                    placement.append(MatrixAlgebras(ring))
                else:
                    placement.append(MatrixEndomorphismSpaces(ring))
        elif domain is codomain:
            placement.append(OwnedRings())
        if full_internal_hom and not matrix:
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
                _SelectedFinitePresentationModules,
            )

            if _represented_finite_presentation(domain) and _represented_finite_presentation(codomain):
                placement.append(_SelectedFinitePresentationModules(ring))
        if full_internal_hom and domain in TensorProductModules(ring):
            factors = domain.tensor_factors()
            if factors.cardinality().is_finite() and int(factors.cardinality().finite_value()) == 2 and factors.unrank(0) is factors.unrank(1):
                from dzack_research.preamble.categories.forms.forms import BilinearFormHoms

                placement.append(BilinearFormHoms(ring))
        return Category.join(tuple(placement))

    _HomCategory = ModuleHomCategoryConstruction
    _EndCategory = ModuleEndCategoryConstruction

    class ElementMethods:
        def __rmul__(self, scalar):
            r"""Return ring multiplication or the left module scalar action.

            For an algebra/ring viewed also as a module, two elements with the
            same owned ring parent multiply in that ring.  Only an element of
            the module's scalar ring acts through ``R -> End_R(M)``.
            """
            scalar_parent = getattr(scalar, "parent", lambda: None)()
            if scalar_parent is self.parent():
                if self.parent() in OwnedRings():
                    return scalar._mul_(self)
            return self.parent().scalar_multiple(scalar, self)

    class ParentMethods:
        def __init__(self, base_ring, **rest) -> None:
            ring = _owned_ring(base_ring)
            self._preamble_base_ring = ring
            super().__init__(base=ring, **rest)
            register_module_scalar_action(self)

        def Mor(self, codomain, category=None):
            modules = Modules(self.base_ring())
            if category is None:
                return modules.Mor(self, codomain)
            return _category_homset(category, self, codomain)

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

        def _module_homset_class(self):
            r"""Return the canonical fixed homset for maps out of this module type."""

            return ModuleHomset

        def base_ring(self):
            selected = self.__dict__.get("_preamble_base_ring")
            if selected is not None:
                return selected
            return _owned_ring(self.base())

        def is_module(self) -> bool:
            return True

        def is_free(self) -> bool:
            return False

        def is_finitely_generated(self) -> bool:
            return False

        def is_framed(self) -> bool:
            return False

        def is_finite(self):
            return Unknown

        def is_flat(self) -> bool:
            r"""Decide flatness in the represented field/PID regimes.

            Every module over a field is flat.  Over a PID, flatness is
            equivalent to torsion-freeness (Stacks Project, Tag 0AUW), so a
            module type that already represents ``is_torsion_free`` supplies
            an exact flatness decision without a second flatness algorithm.
            """

            ring = self.base_ring()
            if bool(_engine_ring(ring).is_field()):
                return True
            if ring not in PrincipalIdealDomains():
                raise NotImplementedError(
                    "flatness is currently decided from torsion-freeness over a represented PID"
                )
            torsion_free = getattr(self, "is_torsion_free", None)
            if torsion_free is None:
                raise NotImplementedError(
                    "this PID-module has no represented torsion-freeness decision"
                )
            return bool(torsion_free())

        def base_change(self, ring_map):
            _ = ring_map
            raise NotImplementedError(f"base change of {self} has no represented module construction")

        def _represented_fiber_dimension(self, point):
            _ = point
            return NotImplemented

        def _free_biproduct_with(self, other, labels, factors):
            _ = (other, labels, factors)
            return NotImplemented

        def _presented_biproduct_with(self, other, labels, factors):
            _ = (other, labels, factors)
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
            _ = element
            return None

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
            if element not in self:
                raise TypeError(f"{element} is not an element of {self}")
            scalar = self.base_ring()(scalar)
            return element._lmul_(scalar)

        @cached_method
        def _ring_morphism_defining_module_action(self):
            r"""Return ``rho_M : R -> End_R(M)``, the module structure itself."""
            selected = self.__dict__.get("_preamble_scalar_action_morphism")
            if selected is not None:
                return selected
            ring = self.base_ring()
            endomorphisms = Modules(ring).End(self)

            return ring_morphism(
                ring,
                endomorphisms,
                lambda scalar: endomorphisms.elementwise(
                    lambda element: self._owned_scalar_multiple(scalar, element),
                    verify_linearity=False,
                ),
            )

        def scalar_action(self):
            action = self._ring_morphism_defining_module_action()
            action._preamble_kernel_ideal_provider = self
            return action

        def annihilator(self):
            r"""Return ``Ann_R(M)=ker(R -> End_R(M))``."""
            return self.scalar_action().kernel()

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
            return self.scalar_action()(self.base_ring()(scalar))(element)

        def restrict_scalars(self, ring_map):
            r"""Read this module over the domain of ``ring_map``."""
            return restrict_scalars(self, ring_map)

        def twist_scalar_action(self, ring_endomorphism):
            r"""Twist this module's scalar action along a base-ring endomorphism."""
            return twist_scalar_action(self, ring_endomorphism)

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
                from dzack_research.preamble.categories.rings.commutative_algebra import (
                    PrimeLocalization,
                )

                return PrimeLocalization(ring, prime)
            point = ring.spectrum()(prime)
            localization_ring = point.local_ring()
            localized = self.localize(localization_ring)
            localized._preamble_localization_prime_point = point
            return localized

        localization_at_prime = localize_at_prime


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
        def inclusion_into_generator_maps(self):
            r"""The inclusion of the presented model of ``Hom(M, N)`` into ``N^{gens(M)}``."""
            inclusion = self.__dict__.get("_preamble_internal_hom_inclusion")
            if inclusion is not None:
                return inclusion
            _model, inclusion, _relations, _presentation = self._internal_hom_model_data()
            return inclusion


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
            if subobject_ambient is None and subobject_inclusion_factory is None:
                raise ValueError("a module subobject requires constructor-owned inclusion data")
            self._preamble_subobject_ambient = subobject_ambient
            self._preamble_subobject_generator_images = subobject_generator_images
            self._preamble_subobject_lift = subobject_lift
            self._preamble_subobject_inclusion_factory = subobject_inclusion_factory
            self._preamble_subobject_verify_linearity = subobject_verify_linearity
            super().__init__(**rest)

        @cached_method
        def inclusion(self):
            r"""Return the chosen monomorphism represented by constructor data."""
            factory = self.__dict__.get("_preamble_subobject_inclusion_factory")
            if factory is not None:
                inclusion = factory(self)
            else:
                ambient = self.__dict__.get("_preamble_subobject_ambient")
                images = self.__dict__.get("_preamble_subobject_generator_images")
                if ambient is None or images is None:
                    selected = self.__dict__.get("_preamble_inclusion")
                    assert selected is not None, f"{self} is a module subobject without constructor-owned inclusion data"
                    return selected
                inclusion = module_embedding(
                    self,
                    ambient,
                    images,
                    verify_linearity=self.__dict__.get("_preamble_subobject_verify_linearity", True),
                )
            lift = self.__dict__.get("_preamble_subobject_lift")
            if lift is not None:
                inclusion._preamble_lift = lambda element: lift(self, element)
            return inclusion

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
            summands = CoproductOfFamily(
                Sets.Δ[1],
                lambda index: self.module_generating_set() if int(index) == 0 else other.module_generating_set(),
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

            direct_sum = Biproduct(self, other)
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


class FreeModules(OwnedCategoryOverBaseRing):
    r"""Modules admitting a basis."""

    @classmethod
    def _repr_object_names(cls):
        return "free modules"

    def an_object(self):
        r"""The free module of rank one."""
        from dzack_research.preamble.categories.functors.free_forgetful import FreeModuleFunctor
        from dzack_research.preamble.categories.sets.set_categories import finite_ordinal_set

        return FreeModuleFunctor(self.base_ring())(finite_ordinal_set(1))

    def super_categories(self):
        return [
            Modules(self.base_ring()),
            ProjectiveModules(self.base_ring()),
        ]

    class ParentMethods:
        def is_free(self) -> bool:
            return True


class FinitelyGeneratedModules(OwnedCategoryOverBaseRing):
    @classmethod
    def _repr_object_names(cls):
        return "finitely generated modules"

    def an_object(self):
        r"""The free module of rank one."""
        from dzack_research.preamble.categories.functors.free_forgetful import FreeModuleFunctor
        from dzack_research.preamble.categories.sets.set_categories import finite_ordinal_set

        return FreeModuleFunctor(self.base_ring())(finite_ordinal_set(1))

    def super_categories(self):
        return [Modules(self.base_ring())]

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
            if fiber not in VectorSpaces(residue):
                raise TypeError("base change to a residue field must construct a vector space")
            fiber._preamble_fiber_localization = localized
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


class FinitelyPresentedModules(OwnedCategoryOverBaseRing):
    r"""Modules admitting a finite presentation."""

    @classmethod
    def _repr_object_names(cls):
        return "finitely presented modules"

    def an_object(self):
        r"""The free module of rank one, presented by no relations."""
        from dzack_research.preamble.categories.functors.free_forgetful import FreeModuleFunctor
        from dzack_research.preamble.categories.sets.set_categories import finite_ordinal_set

        return FreeModuleFunctor(self.base_ring())(finite_ordinal_set(1))

    def super_categories(self):
        return [FinitelyGeneratedModules(self.base_ring())]

    class ParentMethods:
        def is_finitely_presented(self) -> bool:
            return True


class ModulesWithChosenFinitePresentation(OwnedCategoryOverBaseRing):
    r"""Finitely presented modules carrying one selected finite presentation."""

    def an_object(self):
        r"""The hyperbolic plane U, presented by its Gram matrix."""
        from dzack_research.preamble.categories.lattices import Lattices

        return Lattices(self.base_ring())("U")

    @classmethod
    def _repr_object_names(cls):
        return "modules with a chosen finite presentation"

    def super_categories(self):
        return [
            FinitelyPresentedModules(self.base_ring()),
            FramedModules(self.base_ring()),
        ]


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
        return module_homset(self.term(degree), self.term(int(degree) - 1)).zero()

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
            subobjects = Subobjects(term, Modules(term.base_ring()))
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


def free_resolution(module, steps=None):
    return module.free_resolution(steps)


class FinitelyGeneratedFreeModules(OwnedCategoryOverBaseRing):
    r"""Finite-rank free modules with a chosen ordered basis."""

    @classmethod
    def _repr_object_names(cls):
        return "finitely generated free modules"

    def an_object(self):
        r"""The free module of rank one."""
        from dzack_research.preamble.categories.functors.free_forgetful import FreeModuleFunctor
        from dzack_research.preamble.categories.sets.set_categories import finite_ordinal_set

        return FreeModuleFunctor(self.base_ring())(finite_ordinal_set(1))

    def super_categories(self):
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
            FramedFreeModules,
        )

        return [
            FramedFreeModules(self.base_ring()),
            ModulesWithChosenFinitePresentation(self.base_ring()),
            ProjectiveModules(self.base_ring()),
        ]

    class ParentMethods:
        def _fresh_free_module_on(self, labels, **options):
            constructor = self.__dict__.get("_preamble_free_module_constructor")
            if constructor is None:
                raise NotImplementedError("this finite free module has no selected free-module constructor")
            return constructor(labels, **options)

        def _represented_vector_space_dimension(self):
            return self.rank()

        def _represented_vector_space_basis_generator_labels(self):
            return self.module_generating_set()

        def _selected_presentation_rows(self):
            return ()

        def fitting_ideal(self, index):
            r"""Return ``Fitt_i(R^n)``: zero below the rank, the unit ideal from it on.

            A free module is presented by no relations, so its relation matrix
            has no rows and the ideal of its ``(n - i)``-minors is zero while a
            minor of positive size is asked for and the unit ideal once none
            is.  The general minor computation has no matrix to read here, so
            the same formula is stated directly.
            """
            ring = self.base_ring()
            rank = int(self.number_of_module_generators())
            return ring.ideal(ring.one() if int(index) >= rank else ring.zero())

        def _represented_kernel_of_morphism(self, morphism):
            if morphism.domain() is not self:
                return NotImplemented
            try:
                generators = morphism.matrix()._kernel_spanning_family()
            except NotImplementedError:
                return NotImplemented
            return self.subobject_on(generators)

        def _same_presentation_module(
            self,
            labels,
            *,
            _extra_categories=(),
            _extra_construction_data=None,
        ):
            return self._fresh_free_module_on(
                labels,
                _extra_categories=tuple(_extra_categories),
                _extra_construction_data=_extra_construction_data,
            )

        def free_resolution(self, steps=None):
            r"""A free module is its own resolution, in degree zero alone.

            The number of steps a caller is willing to compute does not enter:
            the identity already resolves a free module, so the same resolution
            answers however far it is asked to go.
            """
            _ = steps
            return self._identity_resolution()

        @cached_method
        def _identity_resolution(self):
            zero = self._fresh_free_module_on(finite_ordered_set(()))
            degrees = Sets.Δ[0]
            return FreeResolution(
                self,
                degrees,
                indexed_family(degrees, lambda degree: self, name="Free resolution terms"),
                indexed_family(
                    Sets.Δ[-1],
                    lambda degree: None,
                    name="Free resolution differentials",
                ),
                module_homset(self, self).identity(),
                zero,
            )

        def dual_module(self):
            return self._fresh_free_module_on(self.module_generating_set())


class ProjectiveModules(OwnedCategoryOverBaseRing):
    _certifying_predicate = "is_projective"

    def an_object(self):
        r"""The free module of rank one, which is projective."""
        from dzack_research.preamble.categories.functors.free_forgetful import FreeModuleFunctor
        from dzack_research.preamble.categories.sets.set_categories import finite_ordinal_set

        return FreeModuleFunctor(self.base_ring())(finite_ordinal_set(1))

    @classmethod
    def _repr_object_names(cls):
        return "projective modules"

    def super_categories(self):
        return [Modules(self.base_ring())]

    class ParentMethods:
        def is_projective(self) -> bool:
            return True

        def projective_rank(self, point):
            r"""Return the local free rank of a finite projective module at ``point``."""
            if self not in FinitelyGeneratedModules(self.base_ring()):
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

            from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
                FreeModuleOn,
            )

            localized = self.localize_at_prime(point)
            labels = localized.residue_module().basis_generator_labels()
            free = FreeModuleOn(localized.base_ring(), labels)
            return module_homset(free, localized)(
                lambda label: localized.module_generator(label)
            )


class FramedModules(OwnedCategoryOverBaseRing):
    r"""Modules carrying a specified generating map from a set."""

    @classmethod
    def _repr_object_names(cls):
        return "framed modules"

    def an_object(self):
        r"""The free module of rank one, framed by its one generator."""
        from dzack_research.preamble.categories.functors.free_forgetful import FreeModuleFunctor
        from dzack_research.preamble.categories.sets.set_categories import finite_ordinal_set

        return FreeModuleFunctor(self.base_ring())(finite_ordinal_set(1))

    def super_categories(self):
        return [Modules(self.base_ring())]

    class ParentMethods:
        def __init__(
            self,
            module_generating_set=None,
            module_generator_function=None,
            **rest,
        ) -> None:
            r"""Store a chosen framing.

            A framing is a choice, so most modules are constructed with one.  A
            module whose framing is *determined* -- the localization of a framed
            module, a module read over a smaller ring -- receives none here and
            says what its framing is by overriding the two accessors below.
            """
            self._preamble_module_generating_set = module_generating_set
            self._preamble_module_generator_function = module_generator_function
            super().__init__(**rest)

        def module_generating_set(self):
            return self._preamble_module_generating_set

        def module_generator(self, label):
            if label not in self.module_generating_set():
                raise ValueError(f"{label!r} is not a module-generator label")
            return self._preamble_module_generator_function(label)

        def number_of_module_generators(self):
            return self.module_generating_set().cardinality()

        @cached_method
        def module_generators(self):

            return indexed_family(
                self.module_generating_set(),
                self.module_generator,
                name="Module-generator family",
            )

        def module_generator_morphism(self):
            return SetMorphism(
                Sets().Mor(self.module_generating_set(), self),
                self.module_generator,
            )

        def framing_morphism(self):
            r"""Return the presentation \(F(S) \twoheadrightarrow M\) of the framing.

            The framing datum is a set \(S\) and a generator function on it;
            the free module on \(S\) is the domain of the epimorphism those two
            determine, and that epimorphism is what "framed" means.
            """
            from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
                FreeModuleOn,
            )
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                framing_morphism,
            )

            source = FreeModuleOn(self.base_ring(), self.module_generating_set())
            return framing_morphism(source, self, self.module_generator)

        def linear_combination(self, coefficients, factor_on_left=True):
            if not isinstance(coefficients, dict):
                return super().linear_combination(
                    coefficients,
                    factor_on_left=factor_on_left,
                )
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
            if not isinstance(scope, dict):
                raise TypeError("scope is required when injecting module generators")
            if not self.module_generating_set().cardinality().is_finite():
                raise NotImplementedError("inject_variables requires a finite module framing")
            names = tuple(self.variable_names())
            generators = tuple(self.module_generators())
            if len(names) != len(generators):
                raise ValueError("the variable names do not describe the module framing")
            if verbose:
                print(f"Defining {', '.join(names)}")
            scope.update(zip(names, generators, strict=True))

        def is_framed(self) -> bool:
            return True


class RestrictedScalarsModules(OwnedCategoryOverBaseRing):
    r"""Modules obtained by reading an ``S``-module over ``R`` along ``R -> S``."""

    def an_object(self):
        r"""``Res_{id}(R^2)``: a free module along the identity of ``R``."""
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import BasedFreeModule
        from dzack_research.preamble.categories.rings.ring_foundation import ring_morphism
        from dzack_research.preamble.categories.sets.set_categories import finite_ordinal_set

        ring = self.base_ring()
        return restrict_scalars(
            BasedFreeModule(ring, finite_ordinal_set(2)),
            ring_morphism(ring, ring, lambda element: element),
        )

    @classmethod
    def _repr_object_names(cls):
        return "restricted-scalars modules"

    def super_categories(self):
        return [Modules(self.base_ring())]

    class ParentMethods:
        def ring_map(self):
            r"""Return the selected scalar map ``R -> S``."""
            return self._preamble_ring_map

        def module_over_extension(self):
            r"""Return the original ``S``-module before restriction of scalars."""
            return self._preamble_extension_module

        def extension_ring(self):
            return _owned_ring(self.module_over_extension().base_ring())

        def scalar_multiple(self, scalar, element):
            if element.parent() is not self:
                element = self(element)
            extension_module = self.module_over_extension()
            return self.element_class(
                self,
                extension_module.scalar_multiple(
                    self.ring_map()(scalar),
                    element.underlying_element(),
                ),
            )


class RestrictedScalarsModuleView(Parent):
    r"""A distinct parent for the same additive group with a restricted scalar action."""

    class Element(ModuleElement):
        def __init__(self, parent, underlying_element) -> None:
            ModuleElement.__init__(self, parent)
            self._underlying_element = underlying_element

        def underlying_element(self):
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

    def __init__(
        self,
        module,
        ring_map,
        *,
        subobject_ambient=None,
        subobject_generator_images=None,
        subobject_lift=None,
        subobject_inclusion_factory=None,
        subobject_verify_linearity=True,
    ) -> None:
        self._preamble_extension_module = module
        self._preamble_ring_map = ring_map
        base_ring = _owned_ring(ring_map.domain())
        extension_ring = _owned_ring(module.base_ring())
        self._preamble_module_generating_set = None

        categories = [RestrictedScalarsModules(base_ring)]

        selected_finite_module_framing = module in FramedModules(extension_ring) and module in FinitelyGeneratedModules(extension_ring)
        if selected_finite_module_framing and extension_ring in FinitelyGeneratedFreeModules(base_ring):
            scalar_labels = extension_ring.module_generating_set()
            module_labels = module.module_generating_set()
            if scalar_labels.cardinality().is_finite() and module_labels.cardinality().is_finite():
                self._preamble_module_generating_set = CartesianProductOfFamily(
                    Sets.Δ[1],
                    lambda index: scalar_labels if int(index) == 0 else module_labels,
                )
                categories.append(FramedModules(base_ring))
                if extension_ring in FinitelyGeneratedModules(base_ring) and module in FinitelyGeneratedModules(extension_ring):
                    categories.append(FinitelyGeneratedModules(base_ring))
                if extension_ring in FinitelyGeneratedFreeModules(base_ring):
                    if module in FinitelyPresentedModules(extension_ring):
                        categories.append(FinitelyPresentedModules(base_ring))
                    if module in FinitelyGeneratedFreeModules(extension_ring):
                        categories.append(FinitelyGeneratedFreeModules(base_ring))

        subobject_data = subobject_inclusion_factory is not None or (subobject_ambient is not None and subobject_generator_images is not None)
        if subobject_data:
            self._preamble_subobject_ambient = subobject_ambient
            self._preamble_subobject_generator_images = subobject_generator_images
            self._preamble_subobject_lift = subobject_lift
            self._preamble_subobject_inclusion_factory = subobject_inclusion_factory
            self._preamble_subobject_verify_linearity = subobject_verify_linearity
            categories.append(ModuleSubobjects(base_ring))

        self._preamble_base_ring = base_ring
        if self._preamble_module_generating_set is not None:
            self._preamble_module_generator_function = lambda label: RestrictedScalarsModuleView.module_generator(self, label)
        Parent.__init__(
            self,
            base=base_ring,
            category=Category.join(tuple(categories)),
        )
        realize_owned_category(self)

    def __call__(self, value):
        r"""Construct through the owned restriction-of-scalars element parser."""
        return self._element_constructor_(value)

    def _element_constructor_(self, value):
        if isinstance(value, self.element_class) and value.parent() is self:
            return value
        if isinstance(value, RestrictedScalarsModuleView.Element):
            value = value.underlying_element()
        return self.wrap(self._preamble_extension_module(value))

    def wrap(self, underlying_element):
        r"""Read an element of the extension module in this restricted module."""
        extension_module = self._preamble_extension_module
        underlying_element = extension_module(underlying_element)
        return self.element_class(self, underlying_element)

    def _coerce_map_from_(self, source):
        # Restriction of scalars is a change of structure, not a coercion of
        # mathematical objects.  Call ``wrap`` explicitly when the same
        # underlying additive-group element is to be read in this parent.
        if source is self._preamble_extension_module:
            return None
        return super()._coerce_map_from_(source)

    def __contains__(self, value) -> bool:
        if isinstance(value, self.element_class) and value.parent() is self:
            return True
        try:
            return value in self._preamble_extension_module
        except TypeError, ValueError:
            return False

    def module_generating_set(self):
        if self._preamble_module_generating_set is None:
            raise NotImplementedError("this scalar restriction has no selected finite framing")
        return self._preamble_module_generating_set

    def module_generator(self, label):
        labels = self.module_generating_set()
        if label not in labels:
            raise ValueError(f"{label!r} is not a restricted-scalar module-generator label")
        label = labels(label)
        scalar_label = label.component(0)
        module_label = label.component(1)
        extension_ring = _owned_ring(self._preamble_extension_module.base_ring())
        scalar = extension_ring.module_generator(scalar_label)
        module_generator = self._preamble_extension_module.module_generator(module_label)
        underlying = self._preamble_extension_module.scalar_multiple(
            scalar,
            module_generator,
        )
        return self.element_class(self, underlying)

    def _selected_module_coefficients(self, element):

        element = self(element)
        extension_module = self.module_over_extension()
        extension_coefficients = module_coefficients(
            element.underlying_element(),
            extension_module,
        )
        coefficients = {}
        framing = self.module_generating_set()
        for module_label, scalar in extension_coefficients.items():
            for scalar_label, coefficient in module_coefficients(
                scalar,
                self.extension_ring(),
            ).items():
                label = framing(lambda index: scalar_label if int(index) == 0 else module_label)
                coefficients[label] = self.base_ring()(coefficient)
        return coefficients

    @cached_method
    def module_generators(self):

        return indexed_family(
            self.module_generating_set(),
            self.module_generator,
            name="Restricted-scalar generator family",
        )

    def framing_morphism(self):

        source = self.extension_ring()._fresh_free_module_on(self.module_generating_set())
        return framing_morphism(source, self, self.module_generator)

    def _selected_presentation_rows(self):
        r"""Return the induced finite-presentation rows over the smaller ring.

        Suppose ``S`` is finite free over ``R`` on ``(s_i)`` and ``M`` is
        presented over ``S`` on ``(m_j)`` with relation rows ``(a_j)``.  The
        restricted module is generated over ``R`` by ``s_i m_j``.  For every
        selected relation and every ``s_i`` we expand ``s_i a_j`` in the
        selected ``R``-basis of ``S``.  These are exactly the restriction of
        the original ``S``-relation submodule to ``R``.
        """
        if self._preamble_module_generating_set is None:
            raise NotImplementedError("this scalar restriction has no selected finite presentation")

        extension_ring = self.extension_ring()
        extension_module = self.module_over_extension()
        scalar_labels = extension_ring.module_generating_set()
        module_labels = extension_module.module_generating_set()
        restricted_labels = self.module_generating_set()
        ring = self.base_ring()
        width = int(restricted_labels.cardinality())
        relation_rows = []
        relation_source = extension_module._selected_presentation_rows()
        if relation_source is None:
            relation_source = ()
        for relation in relation_source:
            for scalar_label in scalar_labels:
                scalar_generator = extension_ring.module_generator(scalar_label)
                row = [ring.zero()] * width
                for module_label, coefficient in zip(module_labels, relation, strict=True):
                    if not coefficient:
                        continue
                    product = extension_ring(scalar_generator * extension_ring(coefficient))
                    for output_scalar_label, output_coefficient in module_coefficients(product, extension_ring).items():
                        column = restricted_labels.rank(restricted_labels(lambda index: output_scalar_label if int(index) == 0 else module_label))
                        row[column] += ring(output_coefficient)
                if any(row):
                    relation_rows.append(row)
        return tuple(tuple(row) for row in relation_rows)

    def zero(self):
        return self.element_class(self, self._preamble_extension_module.zero())

    def an_element(self):
        return self.element_class(self, self._preamble_extension_module.an_element())

    def _repr_(self):
        return f"{self._preamble_extension_module} restricted to {self.base_ring()} along {self._preamble_ring_map}"


def restrict_scalars(
    module,
    ring_map,
    *,
    _subobject_ambient=None,
    _subobject_generator_images=None,
    _subobject_lift=None,
    _subobject_inclusion_factory=None,
    _subobject_verify_linearity=True,
):
    r"""Return ``Res_R^S(module)`` along the specified morphism ``R -> S``."""
    if _engine_ring(ring_map.codomain()) is not _engine_ring(module.base_ring()):
        raise ValueError(f"restriction of scalars for {module} requires a map into {module.base_ring()}, got codomain {ring_map.codomain()}")
    return RestrictedScalarsModuleView(
        module,
        ring_map,
        subobject_ambient=_subobject_ambient,
        subobject_generator_images=_subobject_generator_images,
        subobject_lift=_subobject_lift,
        subobject_inclusion_factory=_subobject_inclusion_factory,
        subobject_verify_linearity=_subobject_verify_linearity,
    )


def twist_scalar_action(module, ring_endomorphism):
    r"""Twist the scalar action of an ``R``-module along ``R -> R``.

    This is restriction of scalars along an endomorphism of the scalar ring;
    it is unrelated to ``L.twist(a)``, which rescales a lattice form while
    leaving its scalar action unchanged.
    """
    ring = _engine_ring(module.base_ring())
    if _engine_ring(ring_endomorphism.domain()) is not ring or _engine_ring(ring_endomorphism.codomain()) is not ring:
        raise ValueError("a scalar-action twist is specified by an endomorphism of the module's base ring")
    return restrict_scalars(module, ring_endomorphism)


def _tensor_label_set(left, right):

    indices = Sets.Δ[1]
    left_labels = left.module_generating_set()
    right_labels = right.module_generating_set()
    return CartesianProductOfFamily(
        indices,
        lambda index: left_labels if int(index) == 0 else right_labels,
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
        self._generator_indices = _tensor_label_set(left, right)

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
            name="Bilinear generator-image family",
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

        left_coefficients = module_coefficients(left_element, self.left_factor())
        right_coefficients = module_coefficients(right_element, self.right_factor())
        return sum(
            (
                left_coefficient * right_coefficient * self.generator_image(left_label, right_label)
                for left_label, left_coefficient in left_coefficients.items()
                for right_label, right_coefficient in right_coefficients.items()
            ),
            self.codomain().zero(),
        )


class TensorProductModules(OwnedCategoryOverBaseRing):
    r"""Modules carrying a selected tensor-product universal object."""

    def an_object(self):
        r"""The tensor square of the free module of rank one."""
        from dzack_research.preamble.categories.abstract_categories.constructions import TensorProduct
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        free = Modules(self.base_ring()).an_object()
        return TensorProduct(free, free)

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

        def pure_tensor(self, left_element, right_element):
            r"""Return the universal pure tensor of two elements."""
            left = self.tensor_factor(0)
            right = self.tensor_factor(1)

            left_coefficients = module_coefficients(left_element, left)
            right_coefficients = module_coefficients(right_element, right)
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
            left = self.tensor_factor(0)
            right = self.tensor_factor(1)
            labels = self.module_generating_set()
            return BilinearMap(
                left,
                right,
                self,
                lambda left_label, right_label: self.module_generator(_tensor_pair(labels, left_label, right_label)),
            )

        def from_bilinear(self, bilinear):
            left = self.tensor_factor(0)
            right = self.tensor_factor(1)
            if bilinear.left_factor() is not left or bilinear.right_factor() is not right:
                raise ValueError("the bilinear map has different tensor factors")

            return module_homset(self, bilinear.codomain())(lambda pair: bilinear.generator_image(pair.component(0), pair.component(1)))


def _represented_finite_presentation(module) -> bool:
    r"""Return whether ``module`` carries selected finite presentation data."""
    return module in ModulesWithChosenFinitePresentation(module.base_ring())


@cached_function(key=lambda left, right: (id(left), id(right)))
def _module_tensor_product(left, right):
    r"""Return the represented categorical tensor product ``left tensor right``."""
    ring = _owned_ring(left.base_ring())
    if _owned_ring(right.base_ring()) != ring:
        raise ValueError("a tensor product requires one common base ring")

    represented_free = bool(left.is_framed()) and bool(left.is_free()) and bool(right.is_framed()) and bool(right.is_free())
    represented_presented = _represented_finite_presentation(left) and _represented_finite_presentation(right)
    if not represented_free and not represented_presented:
        raise NotImplementedError("the tensor product has no selected represented module backend for these factors")

    tensor_labels = _tensor_label_set(left, right)
    tensor_factors = indexed_family(
        Sets.Δ[1],
        lambda index: left if int(index) == 0 else right,
        name="Tensor factors",
    )

    if represented_free:
        return left._fresh_free_module_on(
            tensor_labels,
            _extra_categories=(TensorProductModules(ring),),
            _extra_construction_data={"tensor_factors": tensor_factors},
        )

    left_labels = left.module_generating_set()
    right_labels = right.module_generating_set()
    if not left_labels.cardinality().is_finite() or not right_labels.cardinality().is_finite():
        raise TypeError("the selected presentation backend requires finite framings")

    width = int(tensor_labels.cardinality().finite_value())
    rows = []
    left_relations = left._selected_presentation_rows() or ()
    right_relations = right._selected_presentation_rows() or ()

    for relation in left_relations:
        for right_label in right_labels:
            row = [ring.zero()] * width
            for left_position, coefficient in enumerate(relation):
                if coefficient:
                    left_label = left_labels.unrank(left_position)
                    pair = _tensor_pair(tensor_labels, left_label, right_label)
                    row[tensor_labels.rank(pair)] = coefficient
            rows.append(row)

    for left_label in left_labels:
        for relation in right_relations:
            row = [ring.zero()] * width
            for right_position, coefficient in enumerate(relation):
                if coefficient:
                    right_label = right_labels.unrank(right_position)
                    pair = _tensor_pair(tensor_labels, left_label, right_label)
                    row[tensor_labels.rank(pair)] = coefficient
            rows.append(row)

    result = NotImplemented
    for presentation_owner in (left, right):
        result = presentation_owner._presented_module_from_relation_rows(
            tensor_labels,
            rows,
            extra_categories=(TensorProductModules(ring),),
            extra_construction_data={"tensor_factors": tensor_factors},
        )
        if result is not NotImplemented:
            break
    if result is NotImplemented:
        raise NotImplementedError("the selected tensor-product presentation has no represented quotient constructor")
    return result


def _biproduct_label_set(left, right):

    indices = Sets.Δ[1]
    left_labels = left.module_generating_set()
    right_labels = right.module_generating_set()
    return CoproductOfFamily(
        indices,
        lambda index: left_labels if int(index) == 0 else right_labels,
    )


def _biproduct_label(label_set, side, label):
    return label_set(side, label)


def _biproduct_factor_family(left, right):

    return indexed_family(
        Sets.Δ[1],
        lambda index: left if int(index) == 0 else right,
        name="Biproduct factors",
    )


class BiproductModules(OwnedCategoryOverBaseRing):
    def an_object(self):
        r"""The biproduct of the free module of rank one with itself."""
        from dzack_research.preamble.categories.abstract_categories.constructions import Biproduct
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        free = Modules(self.base_ring()).an_object()
        return Biproduct(free, free)

    @classmethod
    def _repr_object_names(cls):
        return "chosen module biproducts"

    def super_categories(self):
        from dzack_research.preamble.categories.abstract_categories.direct_sum_objects import (
            DirectSumObjects,
        )

        return [Modules(self.base_ring()), DirectSumObjects()]

    class ParentMethods:
        def __init__(self, biproduct_factors, **rest) -> None:
            self._preamble_biproduct_factors = biproduct_factors
            super().__init__(summands=biproduct_factors, **rest)

        def biproduct_factors(self):
            return self._preamble_biproduct_factors

        def biproduct_factor(self, index):
            return self.biproduct_factors()[index]

        def left_inclusion(self):
            left = self.biproduct_factor(0)
            labels = self.module_generating_set()

            return module_homset(left, self)(lambda label: self.module_generator(_biproduct_label(labels, 0, label)))

        def right_inclusion(self):
            right = self.biproduct_factor(1)
            labels = self.module_generating_set()

            return module_homset(right, self)(lambda label: self.module_generator(_biproduct_label(labels, 1, label)))

        def left_injection(self):
            r"""Return \(\iota_0 : M_0 \to M_0 \oplus M_1\)."""
            return self._summand_injection(0)

        def right_injection(self):
            r"""Return \(\iota_1 : M_1 \to M_0 \oplus M_1\)."""
            return self._summand_injection(1)

        def _summand_injection(self, position):
            r"""A biproduct is a coproduct, so it has these beside its projections."""
            summand = self.biproduct_factor(position)
            labels = self.module_generating_set()
            return module_homset(summand, self)({label: self.module_generator(_biproduct_label(labels, position, label)) for label in summand.module_generating_set()})

        def left_projection(self):
            left = self.biproduct_factor(0)

            def image(label):
                if int(label.summand_index()) == 0:
                    return left.module_generator(label.summand_element())
                return left.zero()

            return module_homset(self, left)(image)

        def right_projection(self):
            right = self.biproduct_factor(1)

            def image(label):
                if int(label.summand_index()) == 1:
                    return right.module_generator(label.summand_element())
                return right.zero()

            return module_homset(self, right)(image)

        def from_summands(self, left_map, right_map):
            r"""Return the unique map ``self -> X`` extending both summand maps."""
            if left_map.domain() is not self.biproduct_factor(0):
                raise ValueError("the left map has the wrong source")
            if right_map.domain() is not self.biproduct_factor(1):
                raise ValueError("the right map has the wrong source")
            if left_map.codomain() is not right_map.codomain():
                raise ValueError("the summand maps require one common target")

            return module_homset(self, left_map.codomain())(
                lambda label: (
                    left_map(self.biproduct_factor(0).module_generator(label.summand_element()))
                    if int(label.summand_index()) == 0
                    else right_map(self.biproduct_factor(1).module_generator(label.summand_element()))
                )
            )

        def to_product(self, left_map, right_map):
            r"""Return the unique map ``X -> self`` with the specified projections."""
            if left_map.domain() is not right_map.domain():
                raise ValueError("the product maps require one common source")
            if left_map.codomain() is not self.biproduct_factor(0):
                raise ValueError("the left map has the wrong target")
            if right_map.codomain() is not self.biproduct_factor(1):
                raise ValueError("the right map has the wrong target")

            source = left_map.domain()
            labels = self.module_generating_set()

            def image(source_label):
                coefficients = {}
                for target_label, coefficient in module_coefficients(
                    left_map(source.module_generator(source_label)),
                    self.biproduct_factor(0),
                ).items():
                    coefficients[_biproduct_label(labels, 0, target_label)] = coefficient
                for target_label, coefficient in module_coefficients(
                    right_map(source.module_generator(source_label)),
                    self.biproduct_factor(1),
                ).items():
                    coefficients[_biproduct_label(labels, 1, target_label)] = coefficient
                return self.linear_combination(coefficients)

            return module_homset(source, self)(image)


@cached_function
def _module_biproduct(left, right):
    ring = _owned_ring(left.base_ring())
    if _owned_ring(right.base_ring()) != ring:
        raise ValueError("a biproduct requires one common base ring")

    labels = _biproduct_label_set(left, right)
    factors = _biproduct_factor_family(left, right)
    result = left._free_biproduct_with(right, labels, factors)
    if result is NotImplemented:
        result = left._presented_biproduct_with(right, labels, factors)
    if result is NotImplemented:
        raise NotImplementedError("the represented module factors provide no biproduct realization")
    return result


def biproduct_morphism(left_morphism, right_morphism, source=None, target=None):
    if source is None:
        source = Biproduct(left_morphism.domain(), right_morphism.domain())
    if target is None:
        target = Biproduct(left_morphism.codomain(), right_morphism.codomain())

    if source.biproduct_factor(0) is not left_morphism.domain() or source.biproduct_factor(1) is not right_morphism.domain():
        raise ValueError("the source biproduct has different factors")
    if target.biproduct_factor(0) is not left_morphism.codomain() or target.biproduct_factor(1) is not right_morphism.codomain():
        raise ValueError("the target biproduct has different factors")

    return module_homset(source, target)(
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
        return [
            InternalHomModules(self.base_ring()),
            FinitelyGeneratedFreeModules(self.base_ring()),
        ]

    class ParentMethods:
        def module_generating_set(self):
            return self._preamble_module_generating_set

        def module_generator(self, label):
            labels = self.module_generating_set()
            if label not in labels:
                raise ValueError(f"{label!r} is not a matrix-unit label")
            return self._preamble_module_generator_function(labels(label))

        @cached_method
        def module_generators(self):

            return indexed_family(
                self.module_generating_set(),
                self.module_generator,
                name="Matrix-unit family",
            )

        def number_of_module_generators(self):
            return self.module_generating_set().cardinality()

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

        @cached_method
        def _matrix_column_coefficients(self, column_label):

            columns = self.parent().column_index_set()
            try:
                column_label = columns(column_label)
            except TypeError, ValueError:
                column_label = columns.unrank(int(column_label))
            generator_image = self.__dict__.get("_generator_image")
            image = generator_image(column_label) if generator_image is not None else self(self.domain().module_generator(column_label))
            return module_coefficients(image, self.codomain())

        def matrix_entry(self, row_label, column_label):
            rows = self.parent().row_index_set()
            columns = self.parent().column_index_set()
            try:
                row_label = rows(row_label)
            except TypeError, ValueError:
                row_label = rows.unrank(int(row_label))
            try:
                column_label = columns(column_label)
            except TypeError, ValueError:
                column_label = columns.unrank(int(column_label))
            return self._matrix_column_coefficients(column_label).get(
                row_label,
                self.parent().base_ring().zero(),
            )

        def __getitem__(self, index):
            if not isinstance(index, tuple) or len(index) != 2:
                raise IndexError("a matrix entry is indexed by (row, column)")
            row, column = index
            return self.matrix_entry(row, column)

        def row(self, row_label):
            rows = self.parent().row_index_set()
            try:
                row_label = rows(row_label)
            except TypeError, ValueError:
                row_label = rows.unrank(int(row_label))
            dual = self.domain().dual_module()
            return dual.linear_combination(
                {column_label: self.matrix_entry(row_label, column_label) for column_label in self.parent().column_index_set() if self.matrix_entry(row_label, column_label)}
            )

        def column(self, column_label):
            columns = self.parent().column_index_set()
            try:
                column_label = columns(column_label)
            except TypeError, ValueError:
                column_label = columns.unrank(int(column_label))
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

        def matrix_rank(self):
            from sage.rings.integer_ring import ZZ as SageZZ

            integers = _own_ring(SageZZ)
            return integers._from_engine_element(SageZZ(_engine_matrix(self).rank()))

        def solve_right(self, target):
            r"""Return ``x`` in the domain with ``self(x)=target``."""
            from sage.modules.free_module_element import vector as sage_vector

            target = target if target.parent() is self.codomain() else self.codomain()(target)
            ring = self.parent().base_ring()
            coefficients = module_coefficients(target, self.codomain())
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

            basis = _engine_matrix(self).right_kernel().basis_matrix()
            ring = self.parent().base_ring()
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

            target = module_homset(self.codomain(), self.domain())
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
            target = _refine_matrix_hom(module_homset(self.codomain(), self.domain()))
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
        return [MatrixSpaces(self.base_ring()), OwnedRings()]

    class ParentMethods:
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
        def trace(self):
            ring = self.parent().base_ring()
            return sum(
                (self.matrix_entry(label, label) for label in self.parent().row_index_set()),
                ring.zero(),
            )


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
    free = FinitelyGeneratedFreeModules(ring)
    domain = homset.domain()
    codomain = homset.codomain()
    if domain not in free or codomain not in free:
        return homset
    if (
        not callable(getattr(domain, "_preamble_free_module_constructor", None))
        or not callable(getattr(codomain, "_preamble_free_module_constructor", None))
        or not callable(getattr(domain, "module_generating_set", None))
        or not callable(getattr(codomain, "module_generating_set", None))
    ):
        return homset
    if homset not in MatrixSpaces(ring):
        raise TypeError("a finite-free module Hom must be constructed as a matrix Hom")
    return homset
