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

    def __init__(self, group, scalar_ring, product, unit, scalar_action):
        self._group = group
        self._ring = scalar_ring
        self._product = product
        self._unit = unit
        self._scalar_action = scalar_action

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
            free = self.base_ring().free_module(1)
            labels = free.module_generating_set()
            # The selected map and its coefficient inverse precede the free
            # placement. No property label supplies this frame afterwards.
            refine(module, FramedModules(self.base_ring()))
            FramedModules.ParentMethods._install_framing(module, labels, lambda _: self.unit(), free)
            refine(module, FramedFreeModules(self.base_ring()).FinitelyGenerated())
        return module

    def regular_coefficients(self, element):
        assert self.is_regular(), "these coordinates are the regular rank-one frame"
        module = self.module()
        coefficient = module(element)
        if (coefficient == module.zero()) is True:
            return {}
        return {next(iter(module.module_generating_set())): coefficient}

    @cached_method
    def multiplication(self):
        module = self.module()
        tensor = Modules(self.base_ring()).tensor_product((module, module))
        return tensor.from_bilinear_map(module, self._product)
