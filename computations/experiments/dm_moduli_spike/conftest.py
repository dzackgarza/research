r"""Importing the package at collection time makes a broken public re-export
fail loudly during collection instead of surfacing mid-test."""

from __future__ import annotations

from typing import Protocol

import dm_moduli_spike  # noqa: F401


class _PytestConfig(Protocol):
    def addinivalue_line(self, name: str, line: str) -> None: ...


def pytest_configure(config: _PytestConfig) -> None:
    config.addinivalue_line(
        "markers",
        "ci: full stratification or large poset oracle (test-ci only, excluded from just test)",
    )
