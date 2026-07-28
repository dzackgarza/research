"""Pytest fixtures for certificate scaffold tests in this subtree."""

from __future__ import annotations

import pytest

from .projective_framework_loader import load_projective_framework


@pytest.fixture(scope="session", autouse=True)
def projective_framework() -> None:
    """Load framework extensions once for all tests in this directory."""

    load_projective_framework(run_regressions=False)
