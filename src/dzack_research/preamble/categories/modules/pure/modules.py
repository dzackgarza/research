"""Owned categories of modules and vector spaces."""

from sage.categories.additive_groups import AdditiveGroups as SageAdditiveGroups
from sage.categories.modules import Modules as SageModules
from sage.categories.vector_spaces import VectorSpaces as SageVectorSpaces
from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.group.magmas import AdditiveGroups
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    EndCategoryConstruction,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.rings import (
    OwnedCategoryOverBaseRing,
    engine_ring,
    owned_ring_view,
)


class ModuleHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
            ModuleHomset,
        )

        return ModuleHomset


class ModuleEndCategoryConstruction(EndCategoryConstruction):
    r"""The ring-valued endomorphism family ``M |-> End_R(M)``."""

    def Of(self, obj, codomain=None):
        if codomain is not None and codomain is not obj:
            raise ValueError("an endomorphism category has equal endpoints")
        if obj not in self.base_category():
            raise TypeError("the endomorphism object must lie in the module category")
        key = id(obj), id(obj)
        cached = self._objects.get(key)
        if cached is not None and cached.domain_object() is obj:
            return cached

        endomorphisms = self.base_category().Hom(obj, obj)
        endomorphisms.attach_end_family(self)
        from dzack_research.preamble.categories.rings import OwnedRings
        from dzack_research.preamble.refine import refine

        refine(endomorphisms, OwnedRings())
        self._objects[key] = endomorphisms
        return endomorphisms

    def __contains__(self, candidate) -> bool:
        return (
            hasattr(candidate, "end_family")
            and candidate.end_family() is self
        )


class Modules(OwnedCategoryOverBaseRing):
    r"""Modules over a ring, on the owned additive and scalar spines."""

    @classmethod
    def _repr_object_names(cls):
        return "modules"

    def super_categories(self):
        return [
            SageModules(engine_ring(self.base_ring())),
            AdditiveGroups(),
            SageAdditiveGroups().AdditiveCommutative(),
        ]

    def homset(self, domain, codomain):
        r"""Return the unique Hom-set ``Hom_R(domain,codomain)``."""
        if domain not in self or codomain not in self:
            raise TypeError("an R-module Hom requires two R-modules")
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
            module_homset,
        )

        return module_homset(domain, codomain)

    _HomCategory = ModuleHomCategoryConstruction
    _EndCategory = ModuleEndCategoryConstruction

    class ParentMethods:
        def base_ring(self):
            selected = self.__dict__.get("_preamble_base_ring")
            if selected is not None:
                return selected
            return owned_ring_view(self.base())

        def is_module(self) -> bool:
            return True

        def _engine_scalar_multiple(self, scalar, element):
            r"""Backend realization of the selected scalar action.

            Public scalar multiplication is defined through
            ``rho_M : R -> End_R(M)`` below.  This method is the coordinate /
            engine crossing used to construct the endomorphism ``rho_M(r)``.
            """
            if element not in self:
                raise TypeError(f"{element} is not an element of {self}")
            engine = engine_ring(self.base_ring())
            engine_scalar = engine(scalar)

            # Category refinement makes ``base_ring()`` return the owned
            # facade, while the concrete Sage module still stores its native
            # coefficient engine.  Reconstruct through that concrete engine
            # instead of asking Sage's coercion model to discover an
            # engine-ring -> facade-ring action.
            from sage.combinat.free_module import CombinatorialFreeModule
            from sage.modules.fg_pid.fgp_module import FGP_Module_class
            from sage.modules.free_module import FreeModule_generic

            if isinstance(self, CombinatorialFreeModule):
                return self._from_dict(
                    {
                        label: engine_scalar * coefficient
                        for label, coefficient in element.monomial_coefficients().items()
                    },
                    coerce=False,
                )
            if isinstance(self, FreeModule_generic):
                return self(tuple(engine_scalar * coefficient for coefficient in element))
            if isinstance(self, FGP_Module_class):
                return self(engine_scalar * element.lift())
            return engine_scalar * element

        @cached_method
        def _ring_morphism_defining_module_action(self):
            r"""Return ``rho_M : R -> End_R(M)``, the module structure itself."""
            from sage.categories.homset import Hom
            from sage.categories.morphism import SetMorphism
            from sage.categories.rings import Rings as SageRings

            ring = self.base_ring()
            endomorphisms = Modules(ring).End(self)
            return SetMorphism(
                Hom(ring, endomorphisms, SageRings()),
                lambda scalar: endomorphisms.elementwise(
                    lambda element: self._engine_scalar_multiple(scalar, element)
                ),
            )

        def scalar_action(self):
            return self._ring_morphism_defining_module_action()

        def scalar_multiple(self, scalar, element):
            r"""Return ``r*m = rho_M(r)(m)``."""
            return self.scalar_action()(self.base_ring()(scalar))(element)

        def restrict_scalars(self, ring_map):
            r"""Read this module over the domain of ``ring_map``."""
            from dzack_research.preamble.categories.modules.restricted_scalars import (
                restrict_scalars,
            )

            return restrict_scalars(self, ring_map)

        def twist_scalar_action(self, ring_endomorphism):
            r"""Twist this module's scalar action along a base-ring endomorphism."""
            from dzack_research.preamble.categories.modules.restricted_scalars import (
                twist_scalar_action,
            )

            return twist_scalar_action(self, ring_endomorphism)

        def internal_hom(self, target):
            r"""Return the enriched Hom object ``Hom_R(self,target)``.

            In ``R``-modules the categorical Hom-set itself carries the
            pointwise ``R``-module structure.  ``InternalHom`` may additionally
            install a finite presentation on that same Hom parent when the
            backend can compute one; it never constructs a second carrier.
            """
            from dzack_research.preamble.categories.modules.internal_hom import (
                InternalHom,
            )

            return InternalHom(self, target)

        def _Hom_(self, codomain, category=None):
            if category is not None and not category.is_subcategory(
                SageModules(engine_ring(self.base_ring()))
            ):
                raise TypeError("this is not a module homset category")
            from dzack_research.preamble.categories.modules.framed.framed_modules import (
                FramedModules,
            )

            if (
                self not in FramedModules(self.base_ring())
                or codomain not in FramedModules(codomain.base_ring())
            ):
                raise TypeError(
                    "the owned parent-level module Hom constructor requires framed source and target; use Modules(R).Hom(source,target) for the category Hom object"
                )
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                module_homset,
            )

            return module_homset(self, codomain)


class VectorSpaces(OwnedCategoryOverBaseRing):
    r"""Vector spaces over a field."""

    @classmethod
    def _repr_object_names(cls):
        return "vector spaces"

    def super_categories(self):
        return [
            SageVectorSpaces(engine_ring(self.base_ring())),
            Modules(self.base_ring()),
        ]
