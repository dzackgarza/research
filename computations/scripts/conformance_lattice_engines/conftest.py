from __future__ import annotations

import inspect
from types import ModuleType


def assert_equal(actual, expected, label: str) -> None:
    if actual != expected:
        raise AssertionError(f"{label}: actual={actual}, expected={expected}")


def _method_token_from_docstring(func) -> str | None:
    doc = (inspect.getdoc(func) or getattr(func, "__doc__", None) or "")
    for line in doc.splitlines():
        line = line.strip()
        if line.startswith("method:"):
            return line.split(":", 1)[1].strip()
    return None


def covered_methods_from_module(module: ModuleType) -> set[str]:
    covered: set[str] = set()
    for name, func in inspect.getmembers(module, inspect.isfunction):
        if not name.startswith("test_") or name.endswith("_coverage"):
            continue
        token = _method_token_from_docstring(func)
        if token is None:
            continue
        covered.add(token)
    return covered
