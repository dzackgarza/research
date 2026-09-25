r"""Native realizations of modules whose additive group is an owned ring.

The native ring is already a complete additive group before its R-module
structure is constructed. This representation supplies the scalar action to
Modules(R), not a category label in place of that action. Over itself its
chosen frame is F_R({0})->R, e_0 |-> 1; the inverse coordinate is r |-> r e_0.
Their composites are identities by the two unit laws, so this is a free
rank-one module, including over the zero ring. No change of scalar object
or second authoritative ring is involved.
"""

from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.group.magmas import AdditiveGroups
from dzack_research.preamble.categories.modules.pure.modules import (
    Modules,
    _fix_selected_module_resolution,
)
from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules
from dzack_research.preamble.refine import refine
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    _FramedTensorBilinearEvaluationMorphism,
)
from dzack_research.preamble.categories.modules.tensor_quotients import (
    _TensorQuotientClassifierMorphism,
)


class _NativeRingProductClassifierMorphism(_TensorQuotientClassifierMorphism):
    r"""The tensor classifier of the product already supplied by a native ring.

    ``_RingModulePresentation`` receives one ring's primitive product together
    with the scalar action induced by the same ring datum.  Distributivity and
    compatibility with those scalars are therefore construction data, not
    properties inferred from sample equalities in the codomain.  In the
    unframed case the tensor quotient still supplies the universal evaluator;
    this named construction supplies the missing bilinearity derivation.
    """

    def _elementwise_linearity_derivation(self):
        return True


class _NativeFramedRingProductClassifierMorphism(
    _FramedTensorBilinearEvaluationMorphism
):
    r"""The direct framed classifier of a native ring product.

    The primitive product is already bilinear for the scalar action retained
    by the same native ring datum.  Keep its direct two-variable evaluation
    while using the selected tensor framing to represent the induced linear
    map.
    """

    def __init__(self, parent, product) -> None:
        super().__init__(parent, product)
        self._linearity_decision = True


class _NativeModuleFrame:
    r"""A native realization of an actual framed module, with inverse coordinates.

    The model is already constructed, with its free framing source and any
    relations.  Images of its generators and inverse coordinates identify
    it with the native realization.  Normalization is the model's, so a
    word quotient is not mistaken for the free module on its monomials.

    ``injective`` states whether the map from the source is also injective.
    When it is not, the source only spans, and the inverse coordinates of an
    element are those of one chosen preimage.
    """

    def __init__(self, source, images, coordinates, *, injective=True):
        assert source.has_selected_module_resolution(), (
            f"{source} cannot index a generating family: it must be a module with a chosen "
            f"generating family over {source.base_ring()}, but it is in {source.category()}"
        )
        self._source = source
        self._images = images
        self._coordinates = coordinates
        self._injective = injective

    def source(self):
        return self._source

    def image(self, label):
        return self._images(label)

    def coefficients(self, element):
        source = self.source()
        return source.framing_coefficients(source.linear_combination(self._coordinates(element)))

    def is_basis(self):
        r"""Whether the source is free and its map onto the module is also injective."""
        return self._injective and self._source in FramedFreeModules(self._source.base_ring())


class _NativeModuleBasis(_NativeModuleFrame):
    r"""The free case of the native frame, on an actual chosen basis."""

    def __init__(self, source, images, coordinates):
        assert source in FramedFreeModules(source.base_ring()), (
            f"{source} cannot index a basis: it must be a free module with a chosen basis "
            f"over {source.base_ring()}, but it is in {source.category()}"
        )
        super().__init__(source, images, coordinates)


class _RingModulePresentation:
    r"""The native additive-group realization and its specified scalar action.

    Private constructor datum accepted only at Modules._call_. Suppliers are
    the ring computation adapters: the product, unit and scalar action must
    be the primitive operations of that ring, before its algebra classifier
    is formed. The ring-product classifier is derived from these operations,
    never supplied by a different constructor or inferred by sampling.

    The module and algebra owners may inspect this datum to retain the native
    realization of that exact product. A different multiplication on this
    same module takes the ordinary stronger-object construction instead.
    """

    def __init__(self, group, scalar_ring, product, unit, scalar_action, *, basis=None):
        self._group = group
        self._ring = scalar_ring
        self._product = product
        self._unit = unit
        self._scalar_action = scalar_action
        self._basis = basis

    def module(self):
        return self._group

    def base_ring(self):
        return self._ring

    def unit(self):
        return self._unit

    def scalar_multiple(self, scalar, element):
        return self.module()(self._scalar_action(self.base_ring()(scalar), self.module()(element)))

    def is_regular(self):
        return self.module() is self.base_ring()

    def construct(self, category):
        module = self.module()
        assert category.base_ring() is self.base_ring(), (
            f"{module} cannot be made an object of {category}: its scalar action is by "
            f"{self.base_ring()}, not by {category.base_ring()}"
        )
        assert module in AdditiveGroups().AdditiveCommutative(), (
            f"{module} cannot be made an {self.base_ring()}-module: a module's addition must be commutative, "
            f"but {module} is only known to be in {module.category()}"
        )
        assert module.base_ring() is self.base_ring(), (
            f"{module} cannot be made an {self.base_ring()}-module: it is already a module over "
            f"{module.base_ring()}"
        )
        assert Modules.ParentMethods._native_module_presentation(module) is None, (
            f"{module} already has a scalar action by {self.base_ring()}; it cannot be given a second one"
        )
        Modules.ParentMethods._retain_native_module_presentation(module, self)
        match module in category:
            case True:
                pass
            case False:
                refine(module, category)
        if self.is_regular():
            assert self._basis is None, (
                f"{module} is the regular module over itself; its basis is {{1}}, and no other basis may be given"
            )
            free = self.base_ring().free_module(1)
            label = next(iter(free.module_generating_set()))
            self._basis = _NativeModuleBasis(free, lambda _: self.unit(), lambda value: {label: module(value)})
        if self._basis is not None:
            source = self._basis.source()
            assert source.base_ring() is self.base_ring(), (
                f"the basis of {module} is indexed by {source}, a module over {source.base_ring()}, "
                f"but {module} is a module over {self.base_ring()}"
            )
            labels = source.module_generating_set()
            _fix_selected_module_resolution(
                module,
                self.base_ring(),
                labels,
                self._basis.image,
                source.framing_source(),
            )
            match self._basis.is_basis():
                case True:
                    placement = FramedFreeModules(self.base_ring())
                    if labels.cardinality().is_finite():
                        placement = placement.FinitelyGenerated()
                    match module in placement:
                        case True:
                            pass
                        case False:
                            refine(module, placement)
        return module

    def module_basis(self):
        return self._basis

    def coefficients(self, element):
        assert self._basis is not None, (
            f"cannot take coordinates of {element} in {self.module()}: no basis of {self.module()} "
            f"over {self.base_ring()} was chosen"
        )
        return self._basis.coefficients(self.module()(element))

    @cached_method
    def multiplication(self):
        module = self.module()
        tensor = Modules(self.base_ring()).tensor_product((module, module))
        match module.has_selected_module_resolution():
            case True:
                return _NativeFramedRingProductClassifierMorphism(
                    tensor.module_category().Mor(tensor, module),
                    self._product,
                )
            case False:
                return _NativeRingProductClassifierMorphism(
                    tensor.module_category().Mor(tensor, module),
                    self._product,
                )
