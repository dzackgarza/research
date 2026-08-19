# Origin: gitclones/integral_lattice/cat/src/partial_implementation_bases/concrete_categories/cat/functor.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.


# from __future__ import annotations

# from src._types import CategoryABCs, CategoryBases

# class _Functor_Base(CategoryABCs.Functor, CategoryBases.Morphism):
#     ...

# class _EndoFunctor_Base(CategoryABCs.EndoFunctor, _Functor_Base):
#     ...

# class _AutoFunctor_Base(CategoryABCs.AutoFunctor, _EndoFunctor_Base):
#     ...

# class _NaturalTransformation_Base(CategoryABCs.NaturalTransformation, CategoryBases.Morphism):
#     ...

# class _EndoNaturalTransformation_Base(CategoryABCs.EndoNaturalTransformation, _NaturalTransformation_Base):
#     ...

# class _AutoNaturalTransformation_Base(CategoryABCs.AutoNaturalTransformation, _EndoNaturalTransformation_Base):
#     ...

# class CatMorphisms:
#     Functor: _Functor_Base
#     EndoFunctor: _EndoFunctor_Base
#     AutoFunctor: _AutoFunctor_Base
#     NaturalTransformation: _NaturalTransformation_Base
#     EndoNaturalTransformation: _EndoNaturalTransformation_Base
#     AutoNaturalTransformation: _AutoNaturalTransformation_Base