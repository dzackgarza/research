r"""Localization of modules as scalar extension along a ring localization."""

from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    _isomorphism_from_known_inverse_pair,
)
from dzack_research.preamble.categories.functors.scalar_change import (
    _ScalarExtensionFunctor,
)
from dzack_research.preamble.categories.modules.localizations import (
    LocalizedModules,
    _localized_module,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleEmbedding,
    ModuleMorphism,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    ModuleSubobjects,
)


class _LocalizedModuleMorphism(ModuleMorphism):
    r"""Localization of an admitted module map along one ring localization."""

    def __init__(self, parent, source_morphism, functor, action, *, elementwise) -> None:
        self._source_morphism = source_morphism
        self._localization_functor = functor
        super().__init__(
            parent,
            action,
            elementwise=elementwise,
            scalar_extension_of=source_morphism,
            scalar_extension_functor=functor,
        )
        self._linearity_decision = source_morphism.linearity_decision()

    def _elementwise_linearity_derivation(self):
        return self._source_morphism.linearity_decision()


class _LocalizedModuleEmbedding(ModuleEmbedding):
    r"""Localization of a monomorphism; flatness preserves injectivity."""

    def __init__(self, parent, source_embedding, functor, action, *, elementwise) -> None:
        self._source_embedding = source_embedding
        self._localization_functor = functor
        super().__init__(
            parent,
            action,
            elementwise=elementwise,
            scalar_extension_of=source_embedding,
            scalar_extension_functor=functor,
        )

    def _elementwise_linearity_derivation(self):
        return self._source_embedding.linearity_decision()

    def _injectivity_derivation(self):
        return True


class _LocalizationUnitMorphism(ModuleMorphism):
    r"""The canonical linear map ``M -> Res(S^{-1}M)``."""

    def __init__(self, parent, localized, restricted) -> None:
        super().__init__(
            parent,
            lambda element: restricted.wrap(localized.fraction(element)),
            elementwise=True,
        )

    def _elementwise_linearity_derivation(self):
        return True


class ModuleLocalizationFunctor(_ScalarExtensionFunctor):
    r"""The functor ``S^{-1}R tensor_R - : Mod_R -> Mod_{S^{-1}R}``."""

    def __init__(self, localization_ring) -> None:
        from dzack_research.preamble.categories.rings.ring_foundation import LocalizationRings

        match localization_ring in LocalizationRings():
            case True:
                pass
            case False:
                raise TypeError(
                    f"module localization is the functor induced by a localization S^-1 R, but {localization_ring} "
                    "is not a localization"
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
            and module.has_selected_module_resolution()
        ):
            source_inclusion = module.inclusion()
            localized_ambient = self(source_inclusion.codomain())
            def inclusion(localized_subobject):
                mor = localized_subobject.Mono(localized_ambient)
                return _LocalizedModuleEmbedding(
                    mor,
                    source_inclusion,
                    self,
                    lambda element: localized_ambient.fraction(
                        source_inclusion(element.numerator()), element.denominator(),
                    ),
                    elementwise=True,
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
                match source.has_selected_module_resolution():
                    case True:
                        pass
                    case False:
                        raise TypeError(
                            f"cannot localize the morphism {morphism}: its domain {morphism.domain()} must have a chosen "
                            "generating set"
                        )

                def action(label):
                    return target.fraction(morphism(morphism.domain().module_generator(label)))

                elementwise = False
            case _:
                return super()._apply_morphism(morphism)

        # Flatness preserves a selected monomorphism.  Read its mathematical
        # Mor placement, not its concrete morphism implementation.
        source_mor = morphism.parent().mor_category()
        monomorphisms = morphism.domain().module_category().Mono()
        match source_mor.is_subcategory(monomorphisms):
            case True:
                mor = source.Mono(target)
                return _LocalizedModuleEmbedding(
                    mor,
                    morphism,
                    self,
                    action,
                    elementwise=elementwise,
                )
            case False:
                mor = source.module_category().Mor(source, target)
        return _LocalizedModuleMorphism(
            mor,
            morphism,
            self,
            action,
            elementwise=elementwise,
        )

    def unit(self, module, *, localized=None):
        r"""Return ``M -> Res_R(S^{-1}M)``, the localization unit."""

        image = self(module) if localized is None else localized
        restricted = image.restrict_scalars(self.ring_map())
        if image in LocalizedModules(image.base_ring()):
            return _LocalizationUnitMorphism(
                module.module_category().Mor(module, restricted),
                image,
                restricted,
            )
        return module.module_category().Mor(module, restricted)(
            lambda label: restricted.wrap(image.module_generator(label))
        )

    def cokernel_comparison(self, morphism):
        r"""Return ``S^{-1}coker(f) ~= coker(S^{-1}f)`` in represented regimes."""
        return _localization_cokernel_comparison(self, morphism)

    def kernel_comparison(self, morphism):
        r"""Return ``S^{-1}ker(f) ~= ker(S^{-1}f)``."""
        return _localization_kernel_comparison(self, morphism)

    def _repr_(self):
        return f"Module localization along {self.localization_ring().localization_map()}"


def _localization_cokernel_comparison(functor, morphism):
    r"""The canonical represented isomorphism ``S^-1 coker(f) ~= coker(S^-1 f)``.

    The comparison is an arrow in the core of the module category, not a
    separate record carrying two arrows.  The current explicit construction
    uses the selected finite framings of the two represented cokernels.
    """

    localized_morphism = functor(morphism)
    source_cokernel = morphism.cokernel()
    localized_source_cokernel = functor(source_cokernel)
    target_cokernel = localized_morphism.cokernel()
    localized_codomain = localized_morphism.codomain()
    assert (
        localized_source_cokernel.has_selected_module_resolution()
        and target_cokernel.has_selected_module_resolution()
        and localized_codomain.has_selected_module_resolution()
    ), (
        f"the comparison of S^-1 coker({morphism}) with coker(S^-1 {morphism}) is computed only when "
        f"both cokernels and {localized_codomain} have chosen generating sets"
    )

    source_projection = source_cokernel.cokernel_projection()
    localized_source_projection = functor(source_projection)
    target_projection = target_cokernel.cokernel_projection()
    left_labels = tuple(localized_source_cokernel.module_generating_set())
    right_labels = tuple(target_cokernel.module_generating_set())
    codomain_labels = tuple(localized_codomain.module_generating_set())
    assert left_labels == codomain_labels and right_labels == codomain_labels, (
        f"the comparison of S^-1 coker({morphism}) with coker(S^-1 {morphism}) needs both cokernels "
        f"generated by the images of the generators of {localized_codomain}, but they are generated by "
        f"{left_labels} and {right_labels}, not {codomain_labels}"
    )

    forward = localized_source_cokernel.module_category().Mor(
        localized_source_cokernel,
        target_cokernel,
    )(
        {
            label: target_projection(localized_codomain.module_generator(label))
            for label in codomain_labels
        }
    )
    inverse = target_cokernel.module_category().Mor(
        target_cokernel,
        localized_source_cokernel,
    )(
        {
            label: localized_source_projection(
                localized_codomain.module_generator(label)
            )
            for label in codomain_labels
        }
    )
    return _isomorphism_from_known_inverse_pair(forward, inverse)


def _localization_kernel_comparison(functor, morphism):
    r"""The canonical represented isomorphism ``S^-1 ker(f) ~= ker(S^-1 f)``."""

    localized_morphism = functor(morphism)
    localized_source_kernel = functor(morphism.kernel())
    target_kernel = localized_morphism.kernel()
    assert target_kernel is localized_source_kernel, (
        f"the kernel of S^-1 {morphism} is {target_kernel}, not the localization {localized_source_kernel} "
        f"of ker({morphism})"
    )
    identity = localized_source_kernel.module_category().Mor(
        localized_source_kernel,
        target_kernel,
    ).identity()
    return _isomorphism_from_known_inverse_pair(identity, identity)


__all__ = []
