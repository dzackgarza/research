r"""Tensor-algebra component category.

``TensorAlgebraComponents(R)`` is the category whose objects are the graded
pieces ``T_R(M)[p,q]`` for finite-rank free ``R``-modules ``M``.  Its elements
are tensors in those component modules.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, final, override

from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method

from ..cat import Category, Category_over_base_ring, DualObjectsCategory
from ..modules import Modules
from ..modules.homsets import RModuleAutCategory, RModuleEndCategory, RModuleHomCategory
from ..utils import refine_category

if TYPE_CHECKING:
    from ..types import (
        FreeModule,
        Integer,
        Matrix,
        Ring,
        RingElement,
        RModule,
        RModuleElement,
        Tensor,
        TensorAlgebraComponent,
    )


class _TensorAlgebraComponentParentMethods:
    r"""Methods on tensor component modules ``T_R(M)[p,q]``."""

    @abstract_method
    def base_module(self) -> RModule:
        r"""Return ``M`` for ``T_R(M)[p,q]``."""
        ...

    @abstract_method
    def tensor_type(self) -> tuple[Integer, Integer]:
        r"""Return the standard tensor type ``(p, q)``."""
        ...

    @final
    def lift_from_product(self, elts: Sequence[RModuleElement]) -> RModuleElement:
        r"""Lift pure-product data into this tensor component."""
        assert False, f"Pure-tensor lifting for tensor algebra components is not specified yet: {elts}"


class _TensorElementMethods:
    r"""Methods on tensors."""

    @abstract_method
    def base_module(self) -> RModule:
        r"""Return the module ``M`` on which this tensor is defined."""
        ...

    @abstract_method
    def tensor_type(self) -> tuple[Integer, Integer]:
        r"""Return the standard tensor type ``(p, q)``."""
        ...

    @final
    def structure_constants(self) -> Sequence[Matrix]:
        r"""Return coordinate structure constants encoded by a product tensor."""
        assert self.tensor_type() == (1, 2), (
            f"Structure constants are only defined for multiplication tensors of type (1, 2): {self.tensor_type()}"
        )
        return self[:]


class _TensorMorphismMethods:
    r"""Morphisms between tensor component modules."""


class _DualObjects(DualObjectsCategory):
    r"""Dual tensor-algebra components.

    For finite-rank free modules, ``T_R(M)[p,q]^*`` is again a tensor-algebra
    component, namely ``T_R(M)[q,p]``.  The hom/form interpretation is extra
    structure, not a separate tensor-component identity.
    """

    @override
    @final
    def extra_super_categories(self) -> list[Category]:
        r"""Return the categories refined by dual tensor components."""
        base = self.base_category()
        R = base.base_ring()
        return [base, Modules(R).HomCategory().Forms().Integral()]

    class ParentMethods:
        @final
        def tensor_type(self) -> tuple[Integer, Integer]:
            r"""Return the tensor type opposite to the original component's type."""
            p, q = self.dual().tensor_type()
            return (q, p)

    class ElementMethods: ...
    class MorphismMethods: ...


class TensorAlgebraComponents(Category_over_base_ring):
    r"""Category of tensor-algebra components over ``R``.

    Canonical chain: ``TensorAlgebraComponents(R)``.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return f"tensor algebra components over {self.base_ring()}"

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return the module categories satisfied by tensor-algebra components."""
        RMod = Modules(self.base_ring())
        return [RMod.TensorProducts(), RMod.Free().FiniteRank()]

    @cached_method
    @final
    def DualObjects(self) -> Category:
        r"""Return dual tensor components, equivalently integral forms."""
        return _DualObjects.category_of(self)

    dual = DualObjects

    class Constructors:
        r"""Construct tensor component modules and tensor elements."""

        @final
        def __init__(self, category: TensorAlgebraComponents) -> None:
            self._category = category

        @final
        def __repr__(self) -> str:
            return f"tensor algebra component constructors over {self.base_ring()}"

        @override
        @final
        def category(self) -> TensorAlgebraComponents:
            r"""Return the tensor-component category that owns these constructors."""
            return self._category

        @final
        def base_ring(self) -> Ring:
            r"""Return the base ring of the owning tensor-component category."""
            return self.category().base_ring()

        @final
        def _check_tensor_type(self, tensor_type: tuple[Integer, Integer]) -> tuple[Integer, Integer]:
            p, q = tensor_type
            assert p >= 0 and q >= 0, f"Tensor type entries must be nonnegative: {tensor_type}"
            return p, q

        @final
        def component_module(
            self,
            base_module: FreeModule,
            tensor_type: tuple[Integer, Integer],
            *,
            sym: tuple[Integer, ...] | Sequence[tuple[Integer, ...]] | None = None,
            antisym: tuple[Integer, ...] | Sequence[tuple[Integer, ...]] | None = None,
        ) -> TensorAlgebraComponent:
            r"""Return ``T_R(M)[p,q]`` for ``tensor_type=(p,q)``."""
            assert base_module.base_ring() is self.base_ring(), (
                f"Tensor base module must be over {self.base_ring()}: {base_module}"
            )
            p, q = self._check_tensor_type(tensor_type)
            T = base_module.tensor_module(p, q, sym=sym, antisym=antisym)
            return refine_category(T, self.category())

        @final
        def tensor(
            self,
            base_module: FreeModule,
            tensor_type: tuple[Integer, Integer],
            *,
            name: str | None = None,
            latex_name: str | None = None,
            sym: tuple[Integer, ...] | Sequence[tuple[Integer, ...]] | None = None,
            antisym: tuple[Integer, ...] | Sequence[tuple[Integer, ...]] | None = None,
        ) -> Tensor:
            r"""Construct a tensor element in ``T_R(M)[p,q]``."""
            self.component_module(base_module, tensor_type, sym=sym, antisym=antisym)
            return base_module.tensor(tensor_type, name=name, latex_name=latex_name, sym=sym, antisym=antisym)

        @final
        def _from_components(
            self,
            base_module: FreeModule,
            tensor_type: tuple[Integer, Integer],
            components: Matrix
            | Sequence[RingElement]
            | Sequence[Sequence[RingElement]]
            | Sequence[Sequence[Sequence[RingElement]]]
            | Sequence[Matrix],
            *,
            name: str | None = None,
            latex_name: str | None = None,
        ) -> Tensor:
            r"""Construct a tensor from component data in the preferred generating set."""
            tensor = self.tensor(base_module, tensor_type, name=name, latex_name=latex_name)
            tensor[:] = components
            return tensor

        @final
        def from_matrix(
            self,
            base_module: FreeModule,
            entries: Matrix,
            *,
            name: str | None = None,
            latex_name: str | None = None,
        ) -> Tensor:
            r"""Construct the scalar-valued ``(0,2)`` tensor encoded by ``entries``."""
            assert entries.base_ring() is self.base_ring(), f"Tensor matrix must be over {self.base_ring()}: {entries}"
            rank = base_module.rank()
            assert entries.nrows() == rank and entries.ncols() == rank, (
                f"Tensor matrix must be {rank} by {rank}: {entries.nrows()} by {entries.ncols()}"
            )
            return self._from_components(base_module, (0, 2), entries, name=name, latex_name=latex_name)

        @final
        def _module_element_coordinates(self, base_module: FreeModule, element: RModuleElement) -> Sequence[RingElement]:
            assert element.parent() is base_module, f"Tensor output element must lie in {base_module}: {element}"
            return element[:]

        @final
        def from_module_element_matrix(
            self,
            base_module: FreeModule,
            entries: Sequence[Sequence[RModuleElement]],
            *,
            name: str | None = None,
            latex_name: str | None = None,
        ) -> Tensor:
            r"""Construct the ``(1,2)`` tensor encoded by module-valued products."""
            rank = base_module.rank()
            output_coordinates = [
                [self._module_element_coordinates(base_module, element) for element in row]
                for row in entries
            ]
            assert len(output_coordinates) == rank, (
                f"Module-element matrix must have {rank} rows: {len(output_coordinates)}"
            )
            assert all(len(row) == rank for row in output_coordinates), (
                f"Module-element matrix rows must all have length {rank}: {output_coordinates}"
            )
            assert all(len(coordinates) == rank for row in output_coordinates for coordinates in row), (
                f"Each product must have {rank} coordinates in {base_module}: {output_coordinates}"
            )
            components = [
                [[output_coordinates[i][j][k] for j in range(rank)] for i in range(rank)]
                for k in range(rank)
            ]
            return self._from_components(base_module, (1, 2), components, name=name, latex_name=latex_name)

        @final
        def from_multidimensional_list(
            self,
            base_module: FreeModule,
            tensor_type: tuple[Integer, Integer],
            entries: Sequence[RingElement] | Sequence[Sequence[RingElement]] | Sequence[Sequence[Sequence[RingElement]]],
            *,
            name: str | None = None,
            latex_name: str | None = None,
        ) -> Tensor:
            r"""Construct a tensor from nested component lists."""
            return self._from_components(base_module, tensor_type, entries, name=name, latex_name=latex_name)

        @final
        def from_matrices(
            self,
            base_module: FreeModule,
            tensor_type: tuple[Integer, Integer],
            matrices: Sequence[Matrix],
            *,
            name: str | None = None,
            latex_name: str | None = None,
        ) -> Tensor:
            r"""Construct a tensor whose components are supplied as matrices."""
            return self._from_components(base_module, tensor_type, matrices, name=name, latex_name=latex_name)

    _Constructors = Constructors

    @cached_method
    @final
    def Constructors(self):
        r"""Return the tensor-component constructor collector."""
        return self.__class__._Constructors(self)

    ParentMethods = _TensorAlgebraComponentParentMethods
    ElementMethods = _TensorElementMethods
    MorphismMethods = _TensorMorphismMethods
    HomCategory = RModuleHomCategory


TensorAlgebraComponentsCategory = TensorAlgebraComponents
TensorAlgebraComponentsObject = TensorAlgebraComponents.ParentMethods
TensorAlgebraComponentsElement = TensorAlgebraComponents.ElementMethods
TensorAlgebraComponentsMorphism = TensorAlgebraComponents.MorphismMethods
TensorAlgebraComponentsHomCategory = RModuleHomCategory
TensorAlgebraComponentsEndCategory = RModuleEndCategory
TensorAlgebraComponentsAutCategory = RModuleAutCategory
TensorAlgebraComponentsHom = RModuleHomCategory.ParentMethods
TensorAlgebraComponentsEnd = RModuleEndCategory.ParentMethods
TensorAlgebraComponentsAut = RModuleAutCategory.ParentMethods
TensorAlgebraComponentsEndomorphism = RModuleEndCategory.ElementMethods
TensorAlgebraComponentsAutomorphism = RModuleAutCategory.ElementMethods
