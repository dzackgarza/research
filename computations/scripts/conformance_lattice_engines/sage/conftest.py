from __future__ import annotations

import inspect
import os
from pathlib import Path
from types import ModuleType

from conftest import (  # noqa: F401 — re-exported for test imports
    assert_equal,
    covered_methods_from_module,
)


# Sage writes caches under HOME/.sage; keep this writable in sandboxed runs.
_sage_home = Path("/tmp/sage-home")
_sage_home.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("HOME", str(_sage_home))


# Global blacklist of methods considered infrastructure/noise for coverage.
GLOBAL_IRRELEVANT_METHODS = {
    "category",
    "parent",
    "rename",
    "reset_name",
    "is_parent_of",
    "an_element",
    "random_element",
    "some_elements",
    "dump",
    "dumps",
    "save",
    "load",
    "plot",
    "show",
    "latex",
    "_latex_",
    "str",
    "repr",
    "hash",
}


def relevant_runtime_methods(
    sample_object,
    module_prefixes: tuple[str, ...],
    extra_irrelevant: set[str] | None = None,
) -> set[str]:
    irrelevant = set(GLOBAL_IRRELEVANT_METHODS)
    if extra_irrelevant:
        irrelevant.update(extra_irrelevant)

    methods: set[str] = set()
    for name, attr in inspect.getmembers(sample_object):
        if name.startswith("_") or name in irrelevant:
            continue
        if not callable(attr):
            continue
        mod = inspect.getmodule(attr)
        mod_name = "" if mod is None else mod.__name__
        if module_prefixes and not any(mod_name.startswith(p) for p in module_prefixes):
            continue
        methods.add(name)
    return methods


def assert_runtime_methods_covered(
    *,
    test_module: ModuleType,
    sample_object,
    module_prefixes: tuple[str, ...],
    extra_irrelevant: set[str] | None = None,
) -> None:
    covered = covered_methods_from_module(test_module)
    relevant = relevant_runtime_methods(
        sample_object,
        module_prefixes=module_prefixes,
        extra_irrelevant=extra_irrelevant,
    )
    missing = sorted(relevant - covered)
    if missing:
        msg = [
            "Coverage failure: uncovered relevant runtime methods found.",
            f"Relevant methods count: {len(relevant)}",
            f"Covered methods count: {len(covered)}",
            f"Uncovered methods count: {len(missing)}",
            "Uncovered methods:",
            *[f"- {name}" for name in missing],
        ]
        raise AssertionError("\n".join(msg))
