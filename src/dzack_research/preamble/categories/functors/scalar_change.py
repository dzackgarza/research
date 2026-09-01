r"""Scalar extension and restriction along a specified ring morphism."""

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.functors.core import Adjunction, Functor
from dzack_research.preamble.categories.modules import (
    FramedModules,
    Modules,
    RestrictedScalarsModuleView,
    module_homset,
    restrict_scalars,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
)
from dzack_research.preamble.categories.rings import engine_ring, owned_ring_view


class ScalarExtensionFunctor(Functor):
    r"""``S tensor_R - : Mod_R -> Mod_S`` along ``f:R -> S``.

    The mathematical functor is defined on every module.  The live computation
    presently materializes the represented framed/free/presented cases for
    which the module layer has an exact constructor.
    """

    def __init__(self, ring_map) -> None:
        self._ring_map = ring_map
        self._source_ring = owned_ring_view(ring_map.domain())
        self._target_ring = owned_ring_view(ring_map.codomain())
        super().__init__(Modules(self._source_ring), Modules(self._target_ring))

    def ring_map(self):
        return self._ring_map

    def _apply_object(self, module):
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
            FreshFreeModuleOn,
        )

        if isinstance(module, RestrictedScalarsModuleView):
            if (
                engine_ring(module.ring_map().domain()) is engine_ring(self._source_ring)
                and engine_ring(module.ring_map().codomain()) is engine_ring(self._target_ring)
                and module in FramedModules(self._source_ring)
            ):
                image = FreshFreeModuleOn(
                    self._target_ring, module.module_generating_set()
                )
                image._preamble_scalar_extension_source_module = module
                return image
        try:
            base_change = module.base_change
        except AttributeError as error:
            raise NotImplementedError(
                f"scalar extension of the represented module {module} is not materialized yet"
            ) from error
        image = base_change(self.ring_map())
        image._preamble_scalar_extension_source_module = module
        return image

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())

        def image(label):
            original = morphism.domain().module_generator(label)
            coefficients = module_coefficients(morphism(original), morphism.codomain())
            return target.linear_combination(
                {
                    target_label: self._target_ring(
                        self.ring_map()(coefficient)
                    )
                    for target_label, coefficient in coefficients.items()
                }
            )

        return module_homset(source, target)(image)

    def _repr_(self):
        return f"Scalar extension along {self.ring_map()}"


class RestrictionOfScalarsFunctor(Functor):
    r"""``Res_f : Mod_S -> Mod_R`` along ``f:R -> S``."""

    def __init__(self, ring_map) -> None:
        self._ring_map = ring_map
        self._source_ring = owned_ring_view(ring_map.domain())
        self._target_ring = owned_ring_view(ring_map.codomain())
        super().__init__(Modules(self._target_ring), Modules(self._source_ring))

    def ring_map(self):
        return self._ring_map

    def _apply_object(self, module):
        return restrict_scalars(module, self.ring_map())

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        if source not in FramedModules(self._source_ring):
            raise NotImplementedError(
                "the current owned module Hom surface needs a represented framing "
                "to materialize the restricted morphism"
            )

        def image(label):
            source_element = source.module_generator(label).underlying_element()
            return target(morphism(source_element))

        return module_homset(source, target)(image)

    def _repr_(self):
        return f"Restriction of scalars along {self.ring_map()}"


class BaseChangeAdjunction(Adjunction):
    r"""``S tensor_R - ⊣ Res_f``."""

    def __init__(self, ring_map) -> None:
        self._ring_map = ring_map
        super().__init__(
            ScalarExtensionFunctor(ring_map),
            RestrictionOfScalarsFunctor(ring_map),
        )

    def unit(self, module):
        extended = self.left_adjoint()(module)
        restricted = self.right_adjoint()(extended)
        if restricted not in FramedModules(module.base_ring()):
            raise NotImplementedError(
                "the current module Hom surface cannot yet materialize the unit into an unframed restriction"
            )
        return module_homset(module, restricted)(
            lambda label: restricted(extended.module_generator(label))
        )

    def counit(self, module):
        restricted = self.right_adjoint()(module)
        extended = self.left_adjoint()(restricted)
        return module_homset(extended, module)(
            lambda label: restricted.module_generator(label).underlying_element()
        )

    def hom_set_isomorphism_forward(self, extended_morphism):
        source_module = extended_morphism.domain()
        original = getattr(
            source_module,
            "_preamble_scalar_extension_source_module",
            None,
        )
        if original is None:
            raise ValueError(
                "the extended source was not produced by this scalar-extension functor"
            )
        target_restricted = self.right_adjoint()(extended_morphism.codomain())
        return module_homset(original, target_restricted)(
            lambda label: target_restricted(
                extended_morphism(source_module.module_generator(label))
            )
        )

    def hom_set_isomorphism_inverse(self, restricted_morphism, codomain=None):
        if not isinstance(restricted_morphism.codomain(), RestrictedScalarsModuleView):
            raise TypeError("the inverse transpose must land in a restriction of scalars")
        target = restricted_morphism.codomain().module_over_extension()
        if codomain is not None and codomain is not target:
            raise ValueError("the stated codomain is not the module being restricted")
        source = self.left_adjoint()(restricted_morphism.domain())
        return module_homset(source, target)(
            lambda label: restricted_morphism(
                restricted_morphism.domain().module_generator(label)
            ).underlying_element()
        )

    def _repr_(self):
        return f"Scalar-extension/restriction adjunction along {self._ring_map}"


@cached_function
def base_change_adjunction(ring_map) -> BaseChangeAdjunction:
    return BaseChangeAdjunction(ring_map)
