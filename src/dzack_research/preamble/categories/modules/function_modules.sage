r"""Modules of functions, as a check that nothing here needs coordinates.

$C^\infty(\RR)$ and $L^2(\RR)$ are $\RR$-modules whose elements are functions.
They have no finite generating set, no Gram matrix, and no coordinates, so
they exercise the parts of this preamble that are about being a module rather
than about being a finitely generated one.

Shells, deliberately.  An element is a callable and the module trusts it:
smoothness is not checked, square-integrability is not checked, and the
bilinearity of $\langle f,g\rangle=\int fg$ is not checked.  None of that is
decidable here, and pretending otherwise would be worse than saying so.  What
*is* checked is the module structure -- that $\rho(r)$ scales, that addition
is addition -- and that the form is a morphism out of the tensor square with
values in $\RR$, which is a statement about shape rather than about analysis.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sage_lattice_category_spike.lexicon import Element, Module

from typing import Self

from sage.categories.homset import Hom
from sage.categories.morphism import SetMorphism
from sage.categories.rings import Rings
from sage.structure.element import ModuleElement
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

from dzack_research.preamble.categories.modules.pure.modules import Modules


class FunctionModuleElement(ModuleElement):
    r"""A function, as an element of a module of functions."""

    def __init__(self, parent: "FunctionModule", function) -> None:
        ModuleElement.__init__(self, parent)
        assert callable(function), f"an element of {parent} is a function, got {function!r}"
        self._function = function

    def __call__(self, point):
        r"""Return the value at ``point``; an element of a function module is a function."""
        return self._function(point)

    def _add_(self, other: "FunctionModuleElement") -> "FunctionModuleElement":
        return self.parent()(lambda point: self(point) + other(point))

    def _neg_(self) -> "FunctionModuleElement":
        return self.parent()(lambda point: -self(point))

    def _lmul_(self, scalar) -> "FunctionModuleElement":
        return self.parent()(lambda point: scalar * self(point))

    _rmul_ = _lmul_

    def _repr_(self) -> str:
        return f"function in {self.parent()}"


class FunctionModule(UniqueRepresentation, Parent):
    r"""The $R$-module of functions of a stated kind on a stated domain."""

    Element = FunctionModuleElement

    def __init__(self, base_ring: "Ring", kind: str, domain_name: str) -> None:
        self._kind = kind
        self._domain_name = domain_name
        Parent.__init__(self, base=base_ring, category=Modules(base_ring))

    def base_ring(self) -> "Ring":
        return self.base()

    def _element_constructor_(self, function) -> FunctionModuleElement:
        if isinstance(function, FunctionModuleElement) and function.parent() is self:
            return function
        return self.element_class(self, function)

    def zero(self) -> FunctionModuleElement:
        return self(lambda point: self.base_ring().zero())

    def _ring_morphism_defining_module_action(self: Self) -> "Morphism":
        r"""Return $\rho:R\to\operatorname{End}(M)$, $r\mapsto(f\mapsto rf)$.

        The action a module of functions has for free: scaling a function is
        scaling its values.  No generating set is consulted, which is the
        point -- the obligation is about being a module, and this module has
        no generators to read it off.
        """
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

        endomorphisms = module_homset(self, self)
        return SetMorphism(
            Hom(self.base_ring(), endomorphisms, Rings()),
            lambda scalar: SetMorphism(
                endomorphisms, lambda element: scalar * element
            ),
        )

    def _repr_(self) -> str:
        return f"{self._kind}({self._domain_name}) as a module over {self.base_ring()}"


def smooth_functions(base_ring: "Ring", domain_name: str = "RR") -> FunctionModule:
    r"""Return $C^\infty$ on the named domain, as an $R$-module."""
    return FunctionModule(base_ring, "C^infty", domain_name)


def square_integrable_functions(base_ring: "Ring", domain_name: str = "RR") -> FunctionModule:
    r"""Return $L^2$ on the named domain, as an $R$-module."""
    return FunctionModule(base_ring, "L^2", domain_name)
