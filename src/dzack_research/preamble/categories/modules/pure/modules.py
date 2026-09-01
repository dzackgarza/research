"""Owned categories of modules and vector spaces."""

import operator

from sage.categories.action import Action
from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.group.magmas import CommutativeAdditiveGroups
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.modules.internal_hom import (
    LinearEndCategoryConstruction,
)
from dzack_research.preamble.categories.rings import (
    OwnedCategoryOverBaseRing,
    engine_element,
    engine_ring,
    owned_ring_view,
)


class _ModuleScalarAction(Action):
    r"""The selected scalar action of the base ring on one module parent."""

    def __init__(self, scalar_parent, module, is_left) -> None:
        self._module = module
        Action.__init__(self, scalar_parent, module, is_left, operator.mul)

    def _act_(self, scalar, element):
        return self._module.scalar_multiple(scalar, element)


def register_module_scalar_action(module) -> None:
    r"""Register ordinary ``r*m``/``m*r`` syntax for an owned module parent."""
    scalar_parent = engine_ring(module.base_ring())
    module.register_action(_ModuleScalarAction(scalar_parent, module, True))
    module.register_action(_ModuleScalarAction(scalar_parent, module, False))


class ModuleHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
            ModuleHomset,
        )

        return ModuleHomset


class ModuleEndCategoryConstruction(LinearEndCategoryConstruction):
    r"""The ring-valued endomorphism family ``M |-> End_R(M)``."""


class Modules(OwnedCategoryOverBaseRing):
    r"""Modules over a ring, on the owned additive and scalar spines."""

    @classmethod
    def _repr_object_names(cls):
        return "modules"

    def super_categories(self):
        return [CommutativeAdditiveGroups()]

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
            engine_scalar = engine_element(self.base_ring(), scalar)

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
                        label: engine_scalar
                        * engine_element(self.base_ring(), coefficient)
                        for label, coefficient in element.monomial_coefficients().items()
                    },
                    coerce=False,
                )
            if isinstance(self, FreeModule_generic):
                return self(
                    tuple(
                        engine_scalar * engine_element(self.base_ring(), coefficient)
                        for coefficient in element
                    )
                )
            if isinstance(self, FGP_Module_class):
                return self(engine_scalar * element.lift())
            lift = getattr(element, "lift", None)
            cover = getattr(self, "V", None)
            if lift is not None and cover is not None:
                lifted = lift()
                selected_cover = cover()
                if getattr(lifted, "parent", lambda: None)() is selected_cover:
                    return self(
                        selected_cover(
                            tuple(
                                engine_scalar
                                * engine_element(self.base_ring(), coefficient)
                                for coefficient in lifted
                            )
                        )
                    )
            return engine_scalar * element

        @cached_method
        def _ring_morphism_defining_module_action(self):
            r"""Return ``rho_M : R -> End_R(M)``, the module structure itself."""
            selected = self.__dict__.get("_preamble_scalar_action_morphism")
            if selected is not None:
                return selected
            ring = self.base_ring()
            endomorphisms = Modules(ring).End(self)
            from dzack_research.preamble.categories.rings import ring_morphism

            return ring_morphism(
                ring,
                endomorphisms,
                lambda scalar: endomorphisms.elementwise(
                    lambda element: self._engine_scalar_multiple(scalar, element),
                    verify_linearity=False,
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

        def localize(self, *datum):
            r"""Return ``S^{-1}M`` by scalar extension to ``S^{-1}R``.

            ``datum`` may be a represented localization ring, a represented
            submonoid ``S <= (R,*)``, or the finite generators used by the
            ring-localization convenience API.
            """
            from dzack_research.preamble.categories.rings import LocalizationRings
            from dzack_research.preamble.categories.functors.module_localization import (
                module_localization_functor,
            )

            ring = self.base_ring()
            if len(datum) == 1 and datum[0] in LocalizationRings():
                localization_ring = datum[0]
                if localization_ring.localization_source() is not ring:
                    raise ValueError("the localization ring has the wrong source ring")
            else:
                localization_ring = ring.localization(*datum)
            return module_localization_functor(localization_ring)(self)

        localization = localize

        def localize_at_prime(self, prime):
            r"""Return the localized module ``M_p`` at a represented prime."""
            ring = self.base_ring()
            if getattr(prime, "parent", lambda: None)() is ring.spectrum():
                point = prime
            else:
                point = ring.spectrum()(prime)
            localization_ring = point.local_ring()
            localized = self.localize(localization_ring)
            localized._preamble_localization_prime_point = point
            return localized

        localization_at_prime = localize_at_prime

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
            if category is not None and not category.is_subcategory(Modules(self.base_ring())):
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
        return [Modules(self.base_ring())]
