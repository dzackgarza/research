"""Adapters from constructor-discovery surfaces to spec-core provenance data."""

from __future__ import annotations

from inspect import Signature, signature
from typing import Any, cast

from sage.categories.category import Category as SageCategory

from .constructors import ConstructorRegistry, ConstructorSpec


def constructor_registry_for_category(
    category: object,
    *,
    owner_category: str | None = None,
    id_prefix: str | None = None,
) -> ConstructorRegistry:
    """Return constructor provenance records for one category constructor surface."""
    from category_specs.cat import base_category_types as cat_base

    sage_category = cast(SageCategory, category)
    provider = cat_base._explicit_constructors_provider(sage_category)  # noqa: SLF001
    if provider is None:
        constructors = getattr(category, "Constructors", None)
        if not callable(constructors):
            return ConstructorRegistry()
        provider = type(constructors())

    prefix = id_prefix or cat_base._cat_constructor_prefix(sage_category)  # noqa: SLF001
    owner = owner_category or _category_owner_label(category)
    constructor_names = cat_base._cat_constructor_method_names(  # noqa: SLF001
        prefix, provider
    )
    return ConstructorRegistry(
        constructors=tuple(
            _constructor_spec(
                constructor_id=f"{prefix}.{constructor_name}",
                owner_category=owner,
                method_name=constructor_name,
                provider=provider,
                constructor_name=constructor_name,
                sage_entry_point=(
                    f"{provider.__module__}.{provider.__qualname__}.{constructor_name}"
                ),
                target_category=_constructor_target_category(
                    provider, constructor_name, owner
                ),
                target_refinement_route=_constructor_target_refinement_route(
                    provider, constructor_name, owner
                ),
            )
            for constructor_name in constructor_names
        )
    )


def cat_constructor_registry() -> ConstructorRegistry:
    """Return provenance records for constructors surfaced through ``Cat``."""
    from category_specs.cat import base_category_types as cat_base

    specs: list[ConstructorSpec] = []
    for prefix, category in sorted(cat_base._CAT_CONSTRUCTOR_OWNERS.items()):  # noqa: SLF001
        provider = cat_base._explicit_constructors_provider(category)  # noqa: SLF001
        if provider is None:
            continue

        owner = _category_owner_label(category)
        for constructor_name in cat_base._cat_constructor_method_names(  # noqa: SLF001
            prefix, provider
        ):
            method_name = f"{prefix}_{constructor_name}"
            target_category = _constructor_target_category(
                provider, constructor_name, owner
            )
            specs.append(
                _constructor_spec(
                    constructor_id=f"cat.{prefix}.{constructor_name}",
                    owner_category=owner,
                    method_name=method_name,
                    provider=provider,
                    constructor_name=constructor_name,
                    sage_entry_point=f"Cat.Constructors.{method_name}",
                    target_category=target_category,
                    target_refinement_route=(
                        "Cat().Constructors()",
                        f"{owner}.Constructors()",
                        target_category,
                    ),
                    description=(
                        f"Forward to {owner}.Constructors().{constructor_name}."
                    ),
                )
            )
    return ConstructorRegistry(constructors=tuple(specs))


def _constructor_spec(
    *,
    constructor_id: str,
    owner_category: str,
    method_name: str,
    provider: type,
    constructor_name: str,
    sage_entry_point: str,
    target_category: str,
    target_refinement_route: tuple[str, ...],
    description: str = "",
) -> ConstructorSpec:
    return ConstructorSpec(
        id=constructor_id,
        owner_category=owner_category,
        method_name=method_name,
        sage_entry_point=sage_entry_point,
        sage_source=f"{provider.__module__}.{provider.__qualname__}.{constructor_name}",
        target_category=target_category,
        target_refinement_route=target_refinement_route,
        description=description,
    )


def _constructor_return_label(provider: type, constructor_name: str) -> str:
    method = getattr(provider, constructor_name)
    annotation = signature(method).return_annotation
    if annotation is Signature.empty:
        return ""
    if isinstance(annotation, str):
        return annotation.strip("'\"")
    name = getattr(annotation, "__name__", "")
    if name:
        return str(name)
    return str(annotation)


def _constructor_target_category(
    provider: type, constructor_name: str, owner: str
) -> str:
    target_categories = getattr(provider, "_constructor_target_categories", {})
    target_category = target_categories.get(constructor_name)
    if target_category is not None:
        return str(target_category)

    return_label = _constructor_return_label(provider, constructor_name)
    if return_label:
        return return_label
    return owner


def _constructor_target_refinement_route(
    provider: type, constructor_name: str, owner: str
) -> tuple[str, ...]:
    target_routes = getattr(provider, "_constructor_target_refinement_routes", {})
    target_route = target_routes.get(constructor_name)
    if target_route is not None:
        return tuple(str(route) for route in target_route)

    target_category = _constructor_target_category(provider, constructor_name, owner)
    if target_category == owner:
        return (owner,)
    return (owner, target_category)


def _category_owner_label(category: object) -> str:
    from category_specs.cat import base_category_types as cat_base

    sage_category = cast(SageCategory, category)
    category_class = cat_base._static_category_class(sage_category)  # noqa: SLF001
    base_ring = _base_ring_or_none(category)
    if base_ring is None:
        return f"{category_class.__name__}()"
    return f"{category_class.__name__}({base_ring})"


def _base_ring_or_none(category: object) -> Any | None:
    base_getter = getattr(category, "base_ring", None)
    if not callable(base_getter):
        return None
    return base_getter()
