# Origin: gitclones/integral_lattice/cat/src/partial_implementation_bases/structures.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

# """
# Structure base classes for categorical objects.

# These provide default/trivial implementations for the structure ABCs in structures.py.
# """

# from __future__ import annotations

# from dataclasses import dataclass
# from typing import Sequence, final, override

# from src._types import CategoryABCs

# # === Terminal/Initial/Zero ===


# class _TerminalCategory_Base(CategoryABCs.Terminal):  
#     """Base mixin for objects with terminal structure."""

#     ...


# class _InitialCategory_Base(CategoryABCs.Initial):  
#     """Base mixin for objects with initial structure."""

#     ...


# class _ZeroCategory_Base(CategoryABCs.Zero):  
#     """Base mixin for objects with zero structure (both terminal and initial)."""

#     ...


# # === Slice/Coslice ===


# @dataclass
# class _Slice_Base(CategoryABCs.Slice):  
#     """Base for slice structures."""

#     _structure_morphism: CategoryABCs.OneMorphism

#     @override
#     @final
#     def structure_morphism(self) -> CategoryABCs.OneMorphism:
#         """π: X → c."""
#         return self._structure_morphism

#     @override
#     @final
#     def base_object(self) -> CategoryABCs.Object:
#         """c."""
#         return self.structure_morphism().target()


# @dataclass
# class Coslice_Base(CategoryABCs.Coslice):
#     """Base for coslice structures."""

#     _structure_morphism: CategoryABCs.OneMorphism

#     @override
#     @final
#     def structure_morphism(self) -> CategoryABCs.OneMorphism:
#         """ι: c → X."""
#         return self._structure_morphism

#     @override
#     @final
#     def apex_object(self) -> CategoryABCs.Object:
#         """c."""
#         return self._structure_morphism.source()


# # === Spans/Cospans ===


# @dataclass
# class _Span_Base(CategoryABCs.Span):  
#     """Base for span objects."""

#     _left_morphism: CategoryABCs.OneMorphism
#     _right_morphism: CategoryABCs.OneMorphism

#     @override
#     @final
#     def left_morphism(self) -> CategoryABCs.OneMorphism:
#         """f: Z → X."""
#         return self._left_morphism

#     @override
#     @final
#     def right_morphism(self) -> CategoryABCs.OneMorphism:
#         """g: Z → Y."""
#         return self._right_morphism

#     @override
#     @final
#     def apex(self) -> CategoryABCs.Object:
#         """Z."""
#         return self._left_morphism.source()


# @dataclass
# class _Cospan_Base(CategoryABCs.Cospan):  
#     """Base for cospan objects."""

#     _left_morphism: CategoryABCs.OneMorphism
#     _right_morphism: CategoryABCs.OneMorphism

#     @override
#     @final
#     def left_morphism(self) -> CategoryABCs.OneMorphism:
#         """f: X → Z."""
#         return self._left_morphism

#     @override
#     @final
#     def right_morphism(self) -> CategoryABCs.OneMorphism:
#         """g: Y → Z."""
#         return self._right_morphism

#     @override
#     @final
#     def nadir(self) -> CategoryABCs.Object:
#         """Z."""
#         return self._left_morphism.target()


# # === Pullback/Pushout ===


# @dataclass
# class _PullbackCategory_Base(CategoryABCs.Pullback):  
#     """Base for pullback structures."""

#     _cospan: CategoryABCs.Cospan

#     @override
#     @final
#     def cospan(self) -> CategoryABCs.Cospan:
#         """The cospan X_1 → Z ← X_2."""
#         return self._cospan

#     @override
#     @final
#     def projection_morphism(self, i: int) -> CategoryABCs.OneMorphism:
#         match i:
#             case 1:
#                 return self._cospan.left_morphism()
#             case 2:
#                 return self._cospan.right_morphism()
#             case _:
#                 raise IndexError("PullbackCategory.projection_morphism: index must be 1 or 2")


# @dataclass
# class _PushoutCategory_Base(CategoryABCs.Pushout):  
#     """Base for pushout structures."""

#     _span: CategoryABCs.Span

#     @override
#     @final
#     def span(self) -> CategoryABCs.Span:
#         """The span X_1 ← Z → X_2."""
#         return self._span

#     @override
#     @final
#     def inclusion_morphism(self, i: int) -> CategoryABCs.OneMorphism:
#         match i:
#             case 1:
#                 return self._span.left_morphism()
#             case 2:
#                 return self._span.right_morphism()
#             case _:
#                 raise IndexError("PushoutCategory.inclusion_morphism: index must be 1 or 2")


# # === Product/Coproduct ===


# @dataclass
# class _ProductCategory_Base(CategoryABCs.Product):  
#     """Base for product structures."""

#     _factors: Sequence[CategoryABCs.Object]

#     @override
#     @final
#     def product_factors(self) -> Sequence[CategoryABCs.Object]:
#         """The factor objects [X_1, X_2, ...]."""
#         return self._factors


# @dataclass
# class _CoproductCategory_Base(CategoryABCs.Coproduct):  
#     """Base for coproduct structures."""

#     _factors: Sequence[CategoryABCs.OneMorphism]

#     @override
#     @final
#     def coproduct_factors(self) -> tuple[CategoryABCs.OneMorphism, ...]:
#         """The factor objects [X_1, X_2, ...]."""
#         return tuple(self._factors)


# # === Tensor/DirectSum ===


# @dataclass
# class _TensorProductCategory_Base(CategoryABCs.TensorProduct):  
#     """Base for tensor product structures."""

#     _factors: Sequence[CategoryABCs.OneMorphism]

#     @override
#     @final
#     def tensor_factors(self) -> tuple[CategoryABCs.OneMorphism, ...]:
#         """The factor objects [X_1, X_2, ...]."""
#         return tuple(self._factors)


# @dataclass
# class _DirectSumCategory_Base(CategoryABCs.DirectSum):  
#     """Base for direct sum structures."""

#     _factors: Sequence[CategoryABCs.OneMorphism]

#     @override
#     @final
#     def factors(self) -> tuple[CategoryABCs.OneMorphism, ...]:
#         """The factor objects [X_1, X_2, ...]."""
#         return tuple(self._factors)
