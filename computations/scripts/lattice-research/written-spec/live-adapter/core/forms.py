"""Bilinear and quadratic form helper objects.

Thin wrappers that coerce raw evaluations into the FormCodomain value space.
BilinearForm evaluates on pairs; QuadraticForm evaluates on single vectors
and provides polar_form().
"""

from __future__ import annotations

from typing import Any


class BilinearForm:
    """Bilinear form on a module, valued in a FormCodomain."""

    def __init__(self, module: object, codomain: Any) -> None:
        self._module = module
        self._codomain = codomain

    def codomain(self) -> Any:
        return self._codomain

    def evaluate(self, u: object, v: object) -> Any:
        """Evaluate the form on two module elements, coercing into codomain."""
        raise NotImplementedError("subclass must implement evaluate")


class QuadraticForm:
    """Quadratic form on a module, valued in a FormCodomain."""

    def __init__(self, module: object, codomain: Any) -> None:
        self._module = module
        self._codomain = codomain

    def codomain(self) -> Any:
        return self._codomain

    def evaluate(self, v: object) -> Any:
        """Evaluate the quadratic form on a module element."""
        raise NotImplementedError("subclass must implement evaluate")

    def polar_form(self) -> BilinearForm:
        """Return the associated bilinear form (q(x+y)-q(x)-q(y))/2."""
        raise NotImplementedError("subclass must implement polar_form")
