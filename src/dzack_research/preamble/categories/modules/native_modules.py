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
from dzack_research.preamble.categories.modules.pure.modules import Modules, FramedModules
from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules
from dzack_research.preamble.refine import refine


class _NativeModuleFrame:
    r"""A native realization of an actual framed module, with inverse coordinates.

    The model is already constructed, with its free framing source and any
    relations.  Images of its generators and inverse coordinates identify
    it with the native realization.  Normalization is the model's, so a
    word quotient is not mistaken for the free module on its monomials.
    """

    def __init__(self, source, images, coordinates):
        assert source in FramedModules(source.base_ring()), (
            "a native frame is evaluated from an actual framed module"
        )
        self._source = source
        self._images = images
        self._coordinates = coordinates

    def source(self):
        return self._source

    def image(self, label):
        return self._images(label)

    def coefficients(self, element):
        source = self.source()
        return source.framing_coefficients(source.linear_combination(self._coordinates(element)))


class _NativeModuleBasis(_NativeModuleFrame):
    r"""The free case of the native frame, on an actual chosen basis."""

    def __init__(self, source, images, coordinates):
        assert source in FramedFreeModules(source.base_ring()), (
            "a native basis is evaluated from an actual framed free module"
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
        assert category.base_ring() is self.base_ring(), "the native action has the constructor's scalar ring"
        assert module in AdditiveGroups().AdditiveCommutative(), "the action is on the supplied owned additive group"
        assert module.base_ring() is self.base_ring(), "native scalar structure cannot overwrite another chosen base"
        assert Modules.ParentMethods._native_module_presentation(module) is None, "the native module is constructed once"
        module._preamble_native_module_presentation = self
        module._preamble_base_ring = self.base_ring()
        refine(module, category)
        if self.is_regular():
            assert self._basis is None, "the canonical regular frame is supplied by its unit"
            free = self.base_ring().free_module(1)
            label = next(iter(free.module_generating_set()))
            self._basis = _NativeModuleBasis(free, lambda _: self.unit(), lambda value: {label: module(value)})
        if self._basis is not None:
            source = self._basis.source()
            assert source.base_ring() is self.base_ring(), "the basis uses the native action's exact scalars"
            labels = source.module_generating_set()
            refine(module, FramedModules(self.base_ring()))
            FramedModules.ParentMethods._install_framing(
                module, labels, self._basis.image, source.framing_source()
            )
            match source:
                case _ if source in FramedFreeModules(self.base_ring()):
                    placement = FramedFreeModules(self.base_ring())
                    if labels.cardinality().is_finite():
                        placement = placement.FinitelyGenerated()
                    refine(module, placement)
        return module

    def basis(self):
        return self._basis

    def coefficients(self, element):
        assert self._basis is not None, "coordinates require the native construction's chosen basis"
        return self._basis.coefficients(self.module()(element))

    @cached_method
    def multiplication(self):
        module = self.module()
        tensor = Modules(self.base_ring()).tensor_product((module, module))
        return tensor.from_bilinear_map(module, self._product)
