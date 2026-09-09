r"""Public module-package exports for the restored function modules."""

from sage.all import RR

from dzack_research.preamble.categories.modules import (
    FunctionModule,
    FunctionModules,
    smooth_functions,
    square_integrable_functions,
)
from dzack_research.preamble.categories.modules.pure import (
    FunctionModule as PureFunctionModule,
)


def test_function_module_archive_exports_use_one_owner() -> None:
    smooth = smooth_functions(RR)
    l2 = square_integrable_functions(RR)

    assert PureFunctionModule is FunctionModule
    assert smooth in FunctionModules(RR)
    assert l2 in FunctionModules(RR)
    assert FunctionModule(RR, "C^infty", "RR") is smooth
    assert FunctionModule(RR, "L^2", "RR") is l2
