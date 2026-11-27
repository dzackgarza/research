"""Typed category hierarchy for inherited obligation closure."""

from __future__ import annotations

from functools import cached_property
from typing import Self

from pydantic import BaseModel, ConfigDict, Field, model_validator


class CategorySpec(BaseModel):
    """Typed declaration for a single category node."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    direct_obligation_ids: tuple[str, ...] = ()
    super_category_ids: tuple[str, ...] = ()
    provider_ids: tuple[str, ...] = ()
    witness_ids: tuple[str, ...] = ()

    @model_validator(mode="after")
    def _reject_duplicates(self) -> Self:
        if len(self.direct_obligation_ids) != len(set(self.direct_obligation_ids)):
            raise ValueError(
                "category direct obligations must not contain duplicates"
            )
        if len(self.super_category_ids) != len(set(self.super_category_ids)):
            raise ValueError("category super ids must not contain duplicates")
        if len(self.provider_ids) != len(set(self.provider_ids)):
            raise ValueError("category provider ids must not contain duplicates")
        if len(self.witness_ids) != len(set(self.witness_ids)):
            raise ValueError("category witness ids must not contain duplicates")
        return self


class CategorySpecRegistry(BaseModel):
    """Typed registry that resolves inherited obligations by category hierarchy."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    categories: tuple[CategorySpec, ...] = ()
    obligation_ids: tuple[str, ...] = ()

    @model_validator(mode="after")
    def _validate(self) -> Self:
        self._assert_unique_category_ids()
        self._validate_known_obligation_ids()
        self._validate_known_super_ids()
        self._validate_no_cycles()
        return self

    @cached_property
    def categories_by_id(self) -> dict[str, CategorySpec]:
        categories: dict[str, CategorySpec] = {}
        for category in self.categories:
            if category.id in categories:
                raise ValueError(f"duplicate category id: {category.id}")
            categories[category.id] = category
        return categories

    @cached_property
    def obligation_ids_by_id(self) -> frozenset[str]:
        return frozenset(self.obligation_ids)

    @cached_property
    def obligation_closure_by_id(self) -> dict[str, tuple[str, ...]]:
        closure_by_id: dict[str, tuple[str, ...]] = {}

        def _compute(category_id: str, path: tuple[str, ...]) -> tuple[str, ...]:
            if category_id in closure_by_id:
                return closure_by_id[category_id]
            if category_id in path:
                cycle = " -> ".join(path + (category_id,))
                raise ValueError(f"category hierarchy cycle detected: {cycle}")

            category = self.categories_by_id[category_id]
            next_path = path + (category_id,)
            obligations: list[str] = []
            seen: set[str] = set()

            for super_category_id in category.super_category_ids:
                for obligation_id in _compute(super_category_id, next_path):
                    if obligation_id not in seen:
                        obligations.append(obligation_id)
                        seen.add(obligation_id)

            for obligation_id in category.direct_obligation_ids:
                if obligation_id not in seen:
                    obligations.append(obligation_id)
                    seen.add(obligation_id)

            closure_by_id[category_id] = tuple(obligations)
            return closure_by_id[category_id]

        for category_id in self.categories_by_id:
            _compute(category_id, ())
        return closure_by_id

    @property
    def category_ids(self) -> tuple[str, ...]:
        return tuple(self.categories_by_id.keys())

    def category(self, category_id: str) -> CategorySpec:
        category = self.categories_by_id.get(category_id)
        if category is None:
            raise KeyError(f"unknown category id: {category_id}")
        return category

    def inherited_obligation_ids(self, category_id: str) -> tuple[str, ...]:
        obligations = self.obligation_closure_by_id.get(category_id)
        if obligations is None:
            raise KeyError(f"unknown category id: {category_id}")
        return obligations

    def obligation(self, obligation_id: str) -> str:
        if obligation_id not in self.obligation_ids_by_id:
            raise KeyError(f"unknown obligation id: {obligation_id}")
        return obligation_id

    def _assert_unique_category_ids(self) -> None:
        seen: dict[str, int] = {}
        for category in self.categories:
            seen[category.id] = seen.get(category.id, 0) + 1
            if seen[category.id] > 1:
                raise ValueError(f"duplicate category id: {category.id}")

    def _validate_known_obligation_ids(self) -> None:
        known_obligation_ids = self.obligation_ids_by_id
        for category in self.categories:
            for obligation_id in category.direct_obligation_ids:
                if obligation_id not in known_obligation_ids:
                    raise ValueError(
                        f"unknown obligation id {obligation_id} "
                        f"in category {category.id}"
                    )
        if len(self.obligation_ids) != len(known_obligation_ids):
            raise ValueError("obligation ids must not contain duplicates")

    def _validate_known_super_ids(self) -> None:
        for category in self.categories:
            for super_category_id in category.super_category_ids:
                if super_category_id not in self.categories_by_id:
                    raise ValueError(
                        f"unknown super category id {super_category_id} "
                        f"in category {category.id}"
                    )

    def _validate_no_cycles(self) -> None:
        categories_by_id = self.categories_by_id
        visiting: set[str] = set()
        completed: set[str] = set()

        def _visit(category_id: str, path: tuple[str, ...]) -> None:
            if category_id in completed:
                return
            if category_id in visiting:
                cycle = list(path)
                raise ValueError(
                    "category hierarchy cycle detected: "
                    + " -> ".join(cycle + [category_id])
                )

            visiting.add(category_id)
            next_path = path + (category_id,)
            for super_category_id in categories_by_id[category_id].super_category_ids:
                _visit(super_category_id, next_path)
            visiting.remove(category_id)
            completed.add(category_id)

        for category_id in categories_by_id:
            _visit(category_id, ())


CategorySpecRegistry.model_rebuild()
