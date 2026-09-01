r"""Mapping spaces \(C^k(X,Y)\), Lebesgue spaces \(L^p\), and sequence spaces \(\ell^p\)."""

from dzack_research.preamble.categories.functions.real_functions import C, Lp, ell
from dzack_research.preamble.categories.functions.lebesgue_graded import (
    GradedLebesgueModule,
    GradedTensorProductModules,
    GradedTensorSquare,
    LebesgueGradedModules,
    graded_lebesgue_algebra,
    lebesgue_convolution_algebra,
)

__all__ = [
    "C",
    "GradedLebesgueModule",
    "GradedTensorProductModules",
    "GradedTensorSquare",
    "LebesgueGradedModules",
    "Lp",
    "ell",
    "graded_lebesgue_algebra",
    "lebesgue_convolution_algebra",
]
