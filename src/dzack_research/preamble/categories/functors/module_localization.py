r"""Localization of modules as scalar extension along a ring localization."""

from sage.misc.cachefunc import cached_function
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.functors.scalar_change import (
    ScalarExtensionFunctor,
)
from dzack_research.preamble.categories.modules.localizations import (
    GeneralLocalizedModuleParent,
    LocalizedModules,
)
from dzack_research.preamble.refine import refine
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleEmbedding,
    module_embedding,
    module_homset,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    FramedModules,
    restrict_scalars,
)
from dzack_research.preamble.categories.rings.ring_foundation import _engine_ring


class ModuleLocalizationFunctor(ScalarExtensionFunctor):
    r"""The functor ``S^{-1}R tensor_R - : Mod_R -> Mod_{S^{-1}R}``."""

    def __init__(self, localization_ring) -> None:
        if not hasattr(localization_ring, "localization_source") or not hasattr(
            localization_ring, "localization_map"
        ):
            raise TypeError("module localization requires a represented ring localization")
        self._localization_ring = localization_ring
        super().__init__(localization_ring.localization_map())

    def localization_ring(self):
        return self._localization_ring

    def localization_submonoid(self):
        return self.localization_ring().localization_submonoid()

    def is_exact(self) -> bool:
        r"""Localization of modules is exact."""
        return True

    def _apply_object(self, module):
        from sage.categories.rings import Rings as SageRings

        represented_by_sage_ring = _engine_ring(self.localization_ring()) in SageRings()
        if represented_by_sage_ring:
            try:
                localized = super()._apply_object(module)
            except NotImplementedError:
                localized = GeneralLocalizedModuleParent(
                    module,
                    self.localization_ring(),
                    self,
                )
        else:
            localized = GeneralLocalizedModuleParent(
                module,
                self.localization_ring(),
                self,
            )
        localized._preamble_localization_ring = self.localization_ring()
        localized._preamble_localization_submonoid = self.localization_submonoid()
        localized._preamble_localization_functor = self
        return refine(localized, LocalizedModules(self.localization_ring()))

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())

        if isinstance(source, GeneralLocalizedModuleParent):
            if isinstance(target, GeneralLocalizedModuleParent):
                def on_fraction(fraction):
                    return target.fraction(
                        morphism(fraction.numerator()),
                        fraction.denominator(),
                        _trusted_denominator=True,
                    )
            else:
                target_unit = self.unit(morphism.codomain(), localized=target)

                def on_fraction(fraction):
                    represented = target_unit(morphism(fraction.numerator()))
                    target_element = represented.underlying_element()
                    denominator = self.localization_ring().localization_map()(
                        fraction.denominator()
                    )
                    return target.scalar_multiple(denominator.inverse_of_unit(), target_element)

            image = module_homset(source, target).elementwise(
                on_fraction,
                verify_linearity=False,
            )
        elif isinstance(target, GeneralLocalizedModuleParent):

            if source not in FramedModules(source.base_ring()):
                raise NotImplementedError(
                    "this mixed scalar-extension morphism has neither a fraction source nor a represented source framing"
                )
            image = module_homset(source, target)(
                {
                    label: target.fraction(
                        morphism(
                            morphism.domain().module_generator(label)
                        )
                    )
                    for label in source.module_generating_set()
                }
            )
        else:
            image = super()._apply_morphism(morphism)

        if not isinstance(morphism, ModuleEmbedding):
            image._preamble_localization_functor = self
            return image


        if source in FramedModules(source.base_ring()):
            embedded = module_embedding(
                source,
                target,
                {
                    label: image(source.module_generator(label))
                    for label in source.module_generating_set()
                },
            )
            embedded._preamble_localization_functor = self
            return embedded
        embedded = ModuleEmbedding(
            module_homset(source, target),
            lambda element: image(element),
            elementwise=True,
            verify_linearity=False,
        )
        embedded._preamble_localization_functor = self
        return embedded

    def unit(self, module, *, localized=None):
        r"""Return ``M -> Res_R(S^{-1}M)``, the localization unit."""

        image = self(module) if localized is None else localized
        restricted = restrict_scalars(image, self.ring_map())
        if isinstance(image, GeneralLocalizedModuleParent):
            return module_homset(module, restricted).elementwise(
                lambda element: restricted.wrap(image.fraction(element)),
                verify_linearity=False,
            )
        return module_homset(module, restricted)(
            lambda label: restricted.wrap(image.module_generator(label))
        )

    def cokernel_comparison(self, morphism):
        r"""Return ``S^{-1}coker(f) ~= coker(S^{-1}f)`` in represented regimes."""
        return LocalizationCokernelComparison(self, morphism)

    def kernel_comparison(self, morphism):
        r"""Return ``S^{-1}ker(f) ~= ker(S^{-1}f)``."""
        return LocalizationKernelComparison(self, morphism)

    def _repr_(self):
        return f"Module localization along {self.localization_ring().localization_map()}"


class LocalizationCokernelComparison(SageObject):
    r"""The canonical right-exactness comparison for module localization."""

    def __init__(self, functor, morphism) -> None:

        self._functor = functor
        self._morphism = morphism
        self._localized_morphism = functor(morphism)
        self._source_cokernel = morphism.cokernel()
        self._localized_source_cokernel = functor(self._source_cokernel)
        self._target_cokernel = self._localized_morphism.cokernel()

        localized_codomain = self._localized_morphism.codomain()
        if (
            self._localized_source_cokernel
            not in FramedModules(functor.localization_ring())
            or self._target_cokernel not in FramedModules(functor.localization_ring())
            or localized_codomain not in FramedModules(functor.localization_ring())
        ):
            raise NotImplementedError(
                "the represented cokernel comparison currently requires selected finite framings"
            )

        source_projection = self._source_cokernel.cokernel_projection()
        localized_source_projection = functor(source_projection)
        target_projection = self._target_cokernel.cokernel_projection()

        left_labels = tuple(self._localized_source_cokernel.module_generating_set())
        right_labels = tuple(self._target_cokernel.module_generating_set())
        codomain_labels = tuple(localized_codomain.module_generating_set())
        if left_labels != codomain_labels or right_labels != codomain_labels:
            raise ArithmeticError(
                "localized cokernel framings no longer match the selected codomain framing"
            )

        self._forward = module_homset(
            self._localized_source_cokernel,
            self._target_cokernel,
        )(
            {
                label: target_projection(localized_codomain.module_generator(label))
                for label in codomain_labels
            }
        )
        self._inverse = module_homset(
            self._target_cokernel,
            self._localized_source_cokernel,
        )(
            {
                label: localized_source_projection(
                    localized_codomain.module_generator(label)
                )
                for label in codomain_labels
            }
        )

    def functor(self):
        return self._functor

    def morphism(self):
        return self._morphism

    def localized_morphism(self):
        return self._localized_morphism

    def localized_cokernel(self):
        return self._localized_source_cokernel

    def cokernel_of_localized_morphism(self):
        return self._target_cokernel

    def forward(self):
        return self._forward

    isomorphism = forward

    def inverse(self):
        return self._inverse

    def _repr_(self):
        return (
            f"{self.localized_cokernel()} ~= "
            f"{self.cokernel_of_localized_morphism()}"
        )


class LocalizationKernelComparison(SageObject):
    r"""The canonical left-exactness comparison for module localization."""

    def __init__(self, functor, morphism) -> None:

        self._functor = functor
        self._morphism = morphism
        self._localized_morphism = functor(morphism)
        self._source_kernel = morphism.kernel()
        self._localized_source_kernel = functor(self._source_kernel.inclusion()).image()
        self._target_kernel = self._localized_morphism.kernel()
        if self._target_kernel is not self._localized_source_kernel:
            raise ArithmeticError(
                "the image of the localized kernel inclusion is not the selected kernel of the localized morphism"
            )
        identity = module_homset(
            self._localized_source_kernel,
            self._target_kernel,
        ).identity()
        self._forward = identity
        self._inverse = identity

    def functor(self):
        return self._functor

    def morphism(self):
        return self._morphism

    def localized_morphism(self):
        return self._localized_morphism

    def localized_kernel(self):
        return self._localized_source_kernel

    def kernel_of_localized_morphism(self):
        return self._target_kernel

    def forward(self):
        return self._forward

    isomorphism = forward

    def inverse(self):
        return self._inverse

    def _repr_(self):
        return (
            f"{self.localized_kernel()} ~= "
            f"{self.kernel_of_localized_morphism()}"
        )


@cached_function
def module_localization_functor(localization_ring):
    return ModuleLocalizationFunctor(localization_ring)


__all__ = [
    "LocalizationCokernelComparison",
    "LocalizationKernelComparison",
    "LocalizedModules",
    "ModuleLocalizationFunctor",
    "module_localization_functor",
]
