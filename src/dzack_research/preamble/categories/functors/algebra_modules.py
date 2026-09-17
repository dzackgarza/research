r"""The forgetful functor \(U\colon R\text{-}\mathbf{Alg}\to R\text{-}\mathbf{Mod}\).

An algebra is a module equipped with a multiplication, so \(U\) is the
identity on objects: it changes which operations an object answers to, never
the object.  An algebra built by ``Algebras(R)(M, m)`` is a module constructed
through ``Modules(R)`` on the data of \(M\), and its module operations are
inherited from that construction.  On a morphism \(U\) is the underlying
linear map.
"""

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.algebras.algebras import Algebras
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    Modules,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    _owned_ring,
)


class UnderlyingAlgebraModuleMorphism(ModuleMorphism):
    r"""An algebra morphism read as its underlying linear map.

    \(U\) changes neither an element nor its image; it changes which
    operations the map answers to.  So this is constructed as an ordinary
    module morphism, on the framing of its domain when there is one and
    elementwise otherwise, and the kernel, cokernel, matrix and composites of
    the module level are then computed from the algebra morphism rather than
    from state a bare ``Morphism`` never established.

    Linearity is not re-established here.  An \(R\)-algebra morphism is
    \(R\)-linear by definition, so the module level is told the theorem rather
    than asked to test it.
    """

    def __init__(self, parent, algebra_morphism) -> None:
        self._algebra_morphism = algebra_morphism
        domain = parent.domain()
        if domain.is_framed_module():
            super().__init__(
                parent,
                lambda label: self._underlying_image(domain.module_generator(label)),
                verify_linearity=False,
            )
            return
        super().__init__(
            parent,
            self._underlying_image,
            elementwise=True,
            verify_linearity=False,
        )

    def _underlying_image(self, element):
        r"""Return the image of one element under the algebra morphism."""
        return self._algebra_morphism(element)

    def algebra_morphism(self):
        return self._algebra_morphism


class _AlgebraUnderlyingModuleFunctor(Functor):
    r"""\(U\colon\mathbf{Alg}_R\to\mathbf{Mod}_R\)."""

    def __init__(self, base_ring, algebra_category=None) -> None:
        self._base_ring = _owned_ring(base_ring)
        domain = (
            Algebras(self._base_ring) if algebra_category is None else algebra_category
        )
        assert domain.is_subcategory(Algebras(self._base_ring)), (
            f"the underlying-module functor starts on a category of {self._base_ring}-algebras"
        )
        super().__init__(domain, Modules(self._base_ring))

    def base_ring(self):
        return self._base_ring

    def _apply_object(self, algebra):
        r"""Return the underlying \(R\)-module of one algebra: the algebra itself."""
        return algebra

    def _apply_morphism(self, morphism):
        r"""Return the algebra morphism read as a module morphism between the same objects."""
        source = self(morphism.domain())
        target = self(morphism.codomain())
        return UnderlyingAlgebraModuleMorphism(
            source.module_category().Mor(source, target),
            morphism,
        )

    def _repr_(self):
        return f"Underlying-module functor on {self.base_ring()}-algebras"


@cached_function
def _algebra_underlying_module_functor(
    base_ring,
    algebra_category=None,
) -> _AlgebraUnderlyingModuleFunctor:
    return _AlgebraUnderlyingModuleFunctor(base_ring, algebra_category)


__all__ = [
    "UnderlyingAlgebraModuleMorphism",
]
