"""Inspection facade for ``SpecReport`` data."""

from __future__ import annotations

from typing import Self

from .reports import (
    ComputedValue,
    ConstructionWitness,
    SpecCheckResult,
    SpecObligation,
    SpecProvider,
    SpecReport,
)


class Spec:
    """A typed, small source-of-truth view over a ``SpecReport``.

    The facade deliberately delegates classification and lookup to the immutable
    ``SpecReport`` kernel and only exposes convenience query methods.
    """

    __slots__ = ("_report",)

    _report: SpecReport

    def __init__(self, report: SpecReport) -> None:
        self._report = report

    @classmethod
    def of(cls, report: SpecReport) -> Self:
        """Create a façade view for the given report."""
        return cls(report)

    @property
    def subject(self) -> str:
        return self._report.subject

    @property
    def declared_category(self) -> str:
        return self._report.declared_category

    @property
    def obligations(self) -> tuple[SpecObligation, ...]:
        """Return all inherited obligations tracked by the report."""
        return self._report.inherited_obligations

    @property
    def missing_obligations(self) -> tuple[SpecCheckResult, ...]:
        """Return the missing obligation checks."""
        return self._report.missing_obligations

    @property
    def providers(self) -> tuple[SpecProvider, ...]:
        """Return providers that satisfy obligations."""
        return tuple(
            result.provider
            for result in self._report.satisfied_by_provider
            if result.provider is not None
        )

    @property
    def construction_witnesses(self) -> tuple[ConstructionWitness, ...]:
        """Return construction witnesses that satisfy obligations."""
        return tuple(
            result.witness
            for result in self._report.satisfied_by_witness
            if result.witness is not None
        )

    @property
    def witnesses(self) -> tuple[ConstructionWitness, ...]:
        """Backward-compatible alias for construction witnesses."""
        return self.construction_witnesses

    @property
    def computed_values(self) -> tuple[ComputedValue, ...]:
        """Return computed report values."""
        return self._report.computed_values

    @property
    def is_complete(self) -> bool:
        """Report-level completion status."""
        return self._report.is_complete()

    def obligation(self, obligation_id: str) -> SpecObligation:
        """Return the obligation metadata for ``obligation_id``."""
        return self._report.obligation_result_by_id(obligation_id).obligation

    def obligation_result(self, obligation_id: str) -> SpecCheckResult:
        """Return the full check result for ``obligation_id``."""
        return self._report.obligation_result_by_id(obligation_id)

    def value(self, name: str) -> ComputedValue:
        """Return the computed value named ``name``."""
        return self._report.computed_value(name)
