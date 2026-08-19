from __future__ import annotations

from types import ModuleType

import sage.all  # noqa: F401
from sage.all import libgap

from conftest import covered_methods_from_module


def gap_bound_methods(method_names: set[str]) -> set[str]:
    bound: set[str] = set()
    for name in method_names:
        if bool(libgap.eval(f'IsBoundGlobal("{name}")')):
            bound.add(name)
    return bound


def assert_gap_methods_covered(
    *,
    test_module: ModuleType,
    method_names: set[str],
) -> None:
    covered = covered_methods_from_module(test_module)
    relevant = gap_bound_methods(method_names)
    missing = sorted(relevant - covered)
    if missing:
        msg = [
            "Coverage failure: uncovered relevant GAP methods found.",
            f"Relevant GAP methods count: {len(relevant)}",
            f"Covered GAP methods count: {len(covered)}",
            f"Uncovered GAP methods count: {len(missing)}",
            "Uncovered GAP methods:",
            *[f"- {name}" for name in missing],
        ]
        raise AssertionError("\n".join(msg))
