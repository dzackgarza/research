r"""Localization of modules as scalar extension along a ring localization."""

from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.functors.scalar_change import (
    _ScalarExtensionFunctor,
)
from dzack_research.preamble.categories.modules.localizations import (
    LocalizedModules,
    _localized_module,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    FramedModules,
    ModuleSubobjects,
)


class ModuleLocalizationFunctor(_ScalarExtensionFunctor):
    r"""The functor ``S^{-1}R tensor_R - : Mod_R -> Mod_{S^{-1}R}``."""

    def __init__(self, localization_ring) -> None:
        from dzack_research.preamble.categories.rings.ring_foundation import LocalizationRings

        assert localization_ring in LocalizationRings(), (
            "module localization is induced by a ring localization"
        )
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
        source_ring = self.localization_ring().localization_source()
        subobject_data = {}
        if (
            module in ModuleSubobjects(source_ring)
            and module in FramedModules(source_ring)
        ):
            source_inclusion = module.inclusion()
            localized_ambient = self(source_inclusion.codomain())
            def inclusion(localized_subobject):
                hom = localized_subobject.Mono(localized_ambient)
                return hom.element_class(
                    hom,
                    lambda element: localized_ambient.fraction(
                        source_inclusion(element.numerator()), element.denominator(),
                    ),
                    elementwise=True,
                    verify_linearity=False,
                    scalar_extension_of=source_inclusion,
                    scalar_extension_functor=self,
                )

            subobject_data = {"subobject_inclusion_factory": inclusion}
        return _localized_module(
            module,
            self.localization_ring(),
            self,
            **subobject_data,
        )

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        if source in ModuleSubobjects(source.base_ring()):
            if morphism is morphism.domain().inclusion():
                inclusion = source.inclusion()
                assert inclusion.codomain() is target
                assert inclusion.scalar_extension_of() is morphism
                return inclusion

        match source:
            case _ if source in LocalizedModules(source.base_ring()):
                match target:
                    case _ if target in LocalizedModules(target.base_ring()):
                        def action(fraction):
                            return target.fraction(
                                morphism(fraction.numerator()), fraction.denominator(),
                            )
                    case _:
                        target_unit = self.unit(morphism.codomain(), localized=target)

                        def action(fraction):
                            numerator = target_unit(morphism(fraction.numerator())).underlying_element()
                            denominator = self.localization_ring().localization_map()(fraction.denominator())
                            return target.scalar_multiple(denominator.inverse_of_unit(), numerator)
                elementwise = True
            case _ if target in LocalizedModules(target.base_ring()):
                assert source in FramedModules(source.base_ring()), (
                    "the mixed localization image uses its selected source framing"
                )

                def action(label):
                    return target.fraction(morphism(morphism.domain().module_generator(label)))

                elementwise = False
            case _:
                return super()._apply_morphism(morphism)

        # Flatness preserves a selected monomorphism.  Read its mathematical
        # Hom placement, not its concrete morphism implementation.
        source_hom = morphism.parent().homset_category()
        monomorphisms = morphism.domain().module_category().Mono()
        match source_hom.is_subcategory(monomorphisms):
            case True:
                hom = source.Mono(target)
            case False:
                hom = source.module_category().Mor(source, target)
        return hom.element_class(
            hom,
            action,
            elementwise=elementwise,
            verify_linearity=False,
            scalar_extension_of=morphism,
            scalar_extension_functor=self,
        )

    def unit(self, module, *, localized=None):
        r"""Return ``M -> Res_R(S^{-1}M)``, the localization unit."""

        image = self(module) if localized is None else localized
        restricted = image.restrict_scalars(self.ring_map())
        if image in LocalizedModules(image.base_ring()):
            return module.module_category().Mor(module, restricted).elementwise(
                lambda element: restricted.wrap(image.fraction(element)),
                verify_linearity=False,
            )
        return module.module_category().Mor(module, restricted)(
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

        self._forward = self._localized_source_cokernel.module_category().Mor(
            self._localized_source_cokernel,
            self._target_cokernel,
        )(
            {
                label: target_projection(localized_codomain.module_generator(label))
                for label in codomain_labels
            }
        )
        self._inverse = self._target_cokernel.module_category().Mor(
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
        self._localized_source_kernel = functor(self._source_kernel)
        self._target_kernel = self._localized_morphism.kernel()
        if self._target_kernel is not self._localized_source_kernel:
            raise ArithmeticError(
                "the image of the localized kernel inclusion is not the selected kernel of the localized morphism"
            )
        identity = self._localized_source_kernel.module_category().Mor(
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


__all__ = [
    "LocalizationCokernelComparison",
    "LocalizationKernelComparison",
]
