"""Constructor provenance data models for spec-core.

The models in this module intentionally stay close to a minimal canonical record:
- who owns a constructor (`owner_category`)
- how users call it (`method_name`)
- where the implementation comes from (`sage_entry_point` / `sage_source`)
- where results are intended to land (`target_category` / route)
- optional provenance links to providers / witnesses / obligations

These records are designed to be consumed by later adapters in ``cat`` and
category-specific constructor collectors.
"""

from __future__ import annotations

from functools import cached_property
from typing import Self

from pydantic import BaseModel, ConfigDict, Field, model_validator


class ConstructorSpec(BaseModel):
    """Typed constructor metadata for a single named constructor."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    id: str = Field(min_length=1)
    owner_category: str = Field(
        min_length=1,
        description="Math owner category that advertises this constructor.",
    )
    method_name: str = Field(min_length=1)
    sage_entry_point: str = Field(
        min_length=1,
        description="Sage constructor name/route that does the concrete construction.",
    )
    sage_source: str = Field(
        min_length=1,
        description="Primary source reference for the constructor implementation.",
    )
    target_category: str = Field(
        min_length=1,
        description="Target category after constructor completion/refinement.",
    )
    target_refinement_route: tuple[str, ...] = ()
    obligation_ids: tuple[str, ...] = ()
    provider_ids: tuple[str, ...] = ()
    witness_ids: tuple[str, ...] = ()
    description: str = ""


class ConstructorRegistry(BaseModel):
    """Registry of constructor provenance entries with typed lookup/filtering."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    constructors: tuple[ConstructorSpec, ...] = ()

    @model_validator(mode="after")
    def _reject_duplicate_ids(self) -> Self:
        _ = self.constructor_ids  # force validation through mapping construction
        return self

    @cached_property
    def constructor_ids(self) -> tuple[str, ...]:
        return tuple(self._constructors_by_id.keys())

    @cached_property
    def _constructors_by_id(self) -> dict[str, ConstructorSpec]:
        indexed: dict[str, ConstructorSpec] = {}
        for constructor in self.constructors:
            if constructor.id in indexed:
                raise ValueError(f"duplicate constructor id: {constructor.id}")
            indexed[constructor.id] = constructor
        return indexed

    @cached_property
    def _constructors_by_owner(self) -> dict[str, tuple[ConstructorSpec, ...]]:
        grouped: dict[str, list[ConstructorSpec]] = {}
        for constructor in self.constructors:
            grouped.setdefault(constructor.owner_category, []).append(constructor)
        return {owner: tuple(items) for owner, items in grouped.items()}

    @cached_property
    def _constructors_by_obligation(self) -> dict[str, tuple[ConstructorSpec, ...]]:
        grouped: dict[str, list[ConstructorSpec]] = {}
        for constructor in self.constructors:
            for obligation_id in constructor.obligation_ids:
                grouped.setdefault(obligation_id, []).append(constructor)
        return {
            obligation_id: tuple(items)
            for obligation_id, items in grouped.items()
        }

    def has_constructor(self, constructor_id: str) -> bool:
        return constructor_id in self._constructors_by_id

    def constructor(self, constructor_id: str) -> ConstructorSpec:
        constructor = self._constructors_by_id.get(constructor_id)
        if constructor is None:
            raise KeyError(f"unknown constructor id: {constructor_id}")
        return constructor

    def by_owner(self, owner_category: str) -> tuple[ConstructorSpec, ...]:
        return self._constructors_by_owner.get(owner_category, ())

    def owners(self) -> tuple[str, ...]:
        owners = tuple(self._constructors_by_owner.keys())
        return tuple(sorted(owners))

    def with_obligation(self, obligation_id: str) -> tuple[ConstructorSpec, ...]:
        return self._constructors_by_obligation.get(obligation_id, ())

    def by_route_target(self, target_category: str) -> tuple[ConstructorSpec, ...]:
        return tuple(
            constructor
            for constructor in self.constructors
            if constructor.target_category == target_category
        )


ConstructorRegistry.model_rebuild()
