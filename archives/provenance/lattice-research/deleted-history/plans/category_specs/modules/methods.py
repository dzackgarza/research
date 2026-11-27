r"""Base ParentMethods and ElementMethods for ``Modules(R)``."""

from __future__ import annotations

from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING

from sage.categories.tensor import tensor
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method

if TYPE_CHECKING:
    from sage.categories.homset import Homset
    from sage.categories.morphism import Morphism
    from sage.rings.ideal import Ideal_generic
    from sage.rings.infinity import InfinityElement
    from sage.rings.integer import Integer
    from sage.structure.element import Element
    from sage.structure.parent import Parent

    Cardinality = Integer | InfinityElement
    DualRModule = Parent
    Ideal = Ideal_generic
    QuotientModule = Parent
    Ring = Parent
    RingElement = Element
    RingEndomorphism = Morphism
    RModule = Parent
    RModuleAutSet = Homset
    RModuleElement = Element
    ModuleStructure = Callable[[RingElement, RModuleElement], RModuleElement] | Callable[[RingElement], RingEndomorphism]
    RModuleEndSet = Homset
    RModuleForm = Morphism
    RModuleHomset = Homset
    RModuleMorphism = Morphism
    SubModule = Parent


class _RModObjects:
    r"""ParentMethods for ``Modules(R)``.

    ``linear_combination(...)`` is intentionally not provided here: when
    elements are implemented properly the parent does not need it.
    """

    def is_over_integral_domain(self) -> bool:
        return False

    def is_over_dedekind_domain(self) -> bool:
        return False

    def is_over_pid(self) -> bool:
        return False

    def is_over_commutative_ring(self) -> bool:
        return False

    def is_over_field(self) -> bool:
        return False

    def is_over_local_ring(self) -> bool:
        return False

    def is_over_complete_ring(self) -> bool:
        return False

    def is_free(self) -> bool:
        return False

    def is_torsion(self) -> bool:
        return False

    def is_torsionfree(self) -> bool:
        return False

    def is_projective(self) -> bool:
        return False

    def is_finite(self) -> bool:
        return False

    def has_ordered_generating_set(self) -> bool:
        return False

    def is_finitely_generated(self) -> bool:
        return False

    def is_finitely_presented(self) -> bool:
        return False

    def is_ideal(self) -> bool:
        return False

    @cached_method
    def tensor_square(self):
        return self.tensor_power(2)

    def tensor_power(self, n: int):
        match n:
            case 0:
                return self.base_ring()
            case _ if n >= 1:
                return tensor(n * [self])
            case _ if n <= -1:
                return tensor((-n) * [self.dual()])
            case _:
                raise ValueError(f"Unsupported tensor power: {n}")

    def tensor_module(self, p: int, q: int):
        assert p >= 0 and q >= 0, "T_R(M) is NN^2-graded."
        return tensor([self.tensor_power(p), self.dual().tensor_power(q)])

    @abstract_method
    def annihilator(self) -> Ideal: ...

    def __truediv__(self, N: SubModule) -> QuotientModule:
        return self.quotient(N)

    @abstract_method
    def torsion_submodule(self) -> SubModule:
        r"""M_tors := <{m in M | r*m = 0 for some r in R}>
        = <{m in M | Ann_R(m) != 0}>.
        """
        ...

    @abstract_method
    def tensor_algebra(self) -> RModule:
        r"""Return T_R(M) := \bigoplus_n \bigoplus_{p+q=n} T_R(M)[p,q]."""
        ...

    @abstract_method
    def base_change(self, S: Ring) -> RModule:
        r"""Return a representation of M_S := M \otimes_R S in S-Mod."""
        ...

    @abstract_method
    def module_structure(self) -> ModuleStructure:
        r"""The map sigma: R x M -> M such that r.m := sigma(r, m).

        May equivalently be interpreted as a ring morphism
        sigma: R -> End_R(M), where r.m := sigma(r)(m).  Made explicit so
        that M can be twisted by composing with a ring endomorphism.
        """
        ...

    @abstract_method
    def modify_module_structure(self, sigma: ModuleStructure):
        r"""Define a new module structure sigma': R -> End_R(M) so that
        r.m = sigma'(r)(m), replacing the existing sigma.
        """
        ...

    @abstract_method
    def symmetric_algebra(self) -> RModule: ...

    @abstract_method
    def alternating_algebra(self) -> RModule: ...

    @abstract_method
    def dual(self) -> DualRModule: ...

    @abstract_method
    def Hom(self, N: RModule) -> RModuleHomset: ...

    @abstract_method
    def End(self) -> RModuleEndSet: ...

    @abstract_method
    def Aut(self) -> RModuleAutSet: ...

    @abstract_method
    def determinant_module(self) -> RModule:
        r"""Return \Lambda^n_R(M), the top exterior power of M."""
        ...

    @abstract_method
    def __contains__(self, data: RModuleElement | SubModule) -> bool:
        r"""Concrete impls dispatch on RModuleElement vs SubModule."""
        ...

    @abstract_method
    def cardinality(self) -> Cardinality: ...

    @abstract_method
    def is_isomorphic_to(self, other: RModule) -> bool: ...

    @abstract_method
    def is_submodule_of(self, other: RModule) -> bool: ...

    @abstract_method
    def direct_sum(self, other: RModule | Sequence[RModule]) -> RModule: ...

    @abstract_method
    def tensor(self, other: RModule | Sequence[RModule]) -> RModule: ...

    def submodule(self, elts: RModuleElement | Sequence[RModuleElement], *args, **kwds) -> SubModule:
        return self.span(elts)

    @abstract_method
    def intersection(self, other: SubModule) -> SubModule: ...

    @abstract_method
    def span(self, elts: RModuleElement | Sequence[RModuleElement]) -> SubModule: ...

    def __add__(self, other: RModule) -> RModule:
        return self.direct_sum(other)

    @abstract_method
    def __mul__(self, other: RingElement | RModule) -> RModule:
        r"""``r * M`` = submodule spanned by ``{r*m | m in M}``;
        ``N * M`` = the tensor product ``M \otimes_R N``.
        """
        ...

    # Do not define: submodule(), _mul_, _rmul_, _lmul_

    @abstract_method
    def natural_pairing(self) -> RModuleForm:
        r"""The (1,1) form b: M \otimes_R M^* -> R defined by b(v, w^*) := w^*(v)."""
        ...


class _RModElements:
    def span(self) -> SubModule:
        return self.parent().span([self])

    def inclusion(self) -> RModuleMorphism:
        Rm = self.span()
        f = Rm.inclusion()
        assert f in Rm.Hom(self.parent())
        return f

    def annihilator(self) -> Ideal:
        return self.span().annihilator()

    @abstract_method
    def cyclic_submodule(self) -> SubModule: ...

    def is_primitive(self) -> bool:
        return self.span().inclusion().is_primitive()

    @abstract_method
    def __add__(self, m: RModuleElement) -> RModuleElement: ...

    @abstract_method
    def __mul__(self, r: RingElement) -> RModuleElement: ...

    def __neg__(self) -> RModuleElement:
        R = self.base_ring()
        return R(-1) * self

    @abstract_method
    def _lmul_(self, r: RingElement) -> RModuleElement: ...

    @abstract_method
    def _rmul_(self, r: RingElement) -> RModuleElement: ...

    # TODO: define R*m := m.span() when R == m.base_ring(), or base-change.
