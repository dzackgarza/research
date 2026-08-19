# Origin: gitclones/integral_lattice/cat/src/partial_implementation_bases/hom/functors.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

# """
# Functor base classes.

# Provides base implementations for Functor_ABC, Endofunctor_ABC, Autofunctor_ABC,
# NaturalTransformation_ABC, etc.
# """

# from __future__ import annotations

# from dataclasses import dataclass
# from typing import final, override

# from src._types import CategoryABCs, CategoryBases


# @dataclass
# class _Functor_Base(CategoryABCs.Functor):  
#     """Base implementation for functors F: C → D."""

#     @override
#     @final
#     def is_contravariant(self) -> bool:
#         """self.domain.is_op_category()."""
#         return self.source().is_op_category()

#     @override
#     @final
#     def is_covariant(self) -> bool:
#         """not self.is_contravariant()."""
#         return not self.is_contravariant()


# @dataclass
# class _Endofunctor_Base(CategoryABCs.EndoFunctor, CategoryBases.Functor):  
#     """Base implementation for endofunctors F: C → C."""

#     pass


# @dataclass
# class Autofunctor_Base(CategoryABCs.AutoFunctor, _Endofunctor_Base):
#     """Base implementation for autofunctors (invertible F: C → C)."""

#     pass


# @dataclass
# class NaturalTransformation_Base(CategoryABCs.NaturalTransformation):
#     """Base implementation for natural transformations α: F ⇒ G."""

#     pass


# @dataclass
# class EndoNaturalTransformation_Base(
#     CategoryABCs.EndoNaturalTransformation, NaturalTransformation_Base
# ):
#     """Base implementation for endo-natural transformations α: F ⇒ F."""

#     pass


# @dataclass
# class AutoNaturalTransformation_Base(
#     CategoryABCs.AutoNaturalTransformation, EndoNaturalTransformation_Base
# ):
#     """Base implementation for auto-natural transformations (invertible α: F ⇒ F)."""

#     pass
