r"""Function spaces \(C^k(X,Y)\), Lebesgue spaces \(L^p\), and sequence spaces \(\ell^p\)."""

from dzack_research.preamble.categories.functions.lebesgue_graded import (
    GradedLebesgueModule,
    GradedTensorProductModules,
    GradedTensorSquare,
    LebesgueGradedModules,
    LebesgueConvolution,
    LebesgueConvolutionModule,
    graded_lebesgue_algebra,
    lebesgue_convolution_algebra,
)
from dzack_research.preamble.categories.functions.real_functions import (
    Lp,
    C,
    ell,
)

__all__ = [
    "C",
    "GradedLebesgueModule",
    "GradedTensorProductModules",
    "GradedTensorSquare",
    "LebesgueGradedModules",
    "LebesgueConvolution",
    "LebesgueConvolutionModule",
    "Lp",
    "ell",
    "graded_lebesgue_algebra",
    "lebesgue_convolution_algebra",
]
