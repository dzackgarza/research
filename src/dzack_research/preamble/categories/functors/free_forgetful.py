r"""The free-module/underlying-set adjunction ``F_R ⊣ U``."""

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.functors.core import Adjunction, Functor
from dzack_research.preamble.categories.modules.framed.framed_free_modules import FreeModuleOn
from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.rings.ring_foundation import _owned_ring
from dzack_research.preamble.categories.sets.set_categories import Sets


class FreeModuleFunctor(Functor):
    r"""``F_R : Set -> Mod_R``."""

    def __init__(self, base_ring) -> None:
        self._base_ring = _owned_ring(base_ring)
        super().__init__(Sets(), Modules(self._base_ring))

    def base_ring(self):
        return self._base_ring

    def _apply_object(self, set_object):
        return FreeModuleOn(self.base_ring(), set_object)

    def _apply_morphism(self, set_morphism):
        source = self(set_morphism.domain())
        target = self(set_morphism.codomain())
        return source.module_category().Mor(source, target)(
            lambda label: target.module_generator(set_morphism(label))
        )

    def _repr_(self):
        return f"Free {self.base_ring()}-module functor"


class UnderlyingSetFunctor(Functor):
    r"""``U : Mod_R -> Set``; a module is already a set object."""

    def __init__(self, base_ring) -> None:
        self._base_ring = _owned_ring(base_ring)
        super().__init__(Modules(self._base_ring), Sets())

    def _apply_object(self, module):
        return module

    def _apply_morphism(self, module_morphism):
        return Sets().Mor(
            module_morphism.domain(), module_morphism.codomain()
        )(module_morphism)

    def _repr_(self):
        return f"Underlying-set functor on {self._base_ring}-modules"


class FreeForgetfulAdjunction(Adjunction):
    r"""``F_R ⊣ U`` between sets and ``R``-modules."""

    def __init__(self, base_ring) -> None:
        self._base_ring = _owned_ring(base_ring)
        super().__init__(
            FreeModuleFunctor(self._base_ring),
            UnderlyingSetFunctor(self._base_ring),
        )

    def unit(self, set_object):
        free = self.left_adjoint()(set_object)
        return Sets().Mor(set_object, free)(
            lambda element: free.module_generator(element)
        )

    def hom_set_isomorphism_forward(self, morphism, source=None):
        r"""Transpose ``f:F_R(S)->M`` using ``F_R(S)``'s selected framing.

        The generic provenance store correctly reports ambiguity when several
        source objects have been recorded with one image.  A free module is
        stronger data: its constructor retains the actual generating set ``S``.
        That selected framing therefore determines the adjunction source even
        when unrelated provenance records happen to share the same free-module
        parent.
        """
        if source is None:
            source = morphism.domain().module_generating_set()
        return super().hom_set_isomorphism_forward(morphism, source=source)

    def counit(self, module):
        free = self.left_adjoint()(self.right_adjoint()(module))
        return free.module_category().Mor(free, module)(lambda element: element)


    def _repr_(self):
        return f"Free/underlying-set adjunction over {self._base_ring}"


@cached_function
def free_module_functor(base_ring) -> FreeModuleFunctor:
    return FreeModuleFunctor(base_ring)


@cached_function
def underlying_set_functor(base_ring) -> UnderlyingSetFunctor:
    return UnderlyingSetFunctor(base_ring)


@cached_function
def free_forgetful_adjunction(base_ring) -> FreeForgetfulAdjunction:
    return FreeForgetfulAdjunction(base_ring)
