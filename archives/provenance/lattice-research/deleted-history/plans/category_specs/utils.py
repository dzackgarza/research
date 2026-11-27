from collections.abc import Callable, Sequence
from functools import wraps
from typing import Any, Protocol, TypeVar, cast, overload

from sage.categories.category import Category
from sage.misc.abstract_method import AbstractMethod
from sage.structure.parent import Parent

PROJECT_MODULE_PREFIX = "category_specs."

_FoldParent = TypeVar("_FoldParent")
_FoldElement = TypeVar("_FoldElement")


class _FoldableOperation(Protocol[_FoldParent, _FoldElement]):
    @overload
    def __call__(
        self,
        parent: _FoldParent,
        x: _FoldElement,
        y: _FoldElement,
    ) -> _FoldElement: ...

    @overload
    def __call__(
        self,
        parent: _FoldParent,
        elements: Sequence[_FoldElement],
    ) -> _FoldElement: ...


class _MissingFoldArgument: ...


_MISSING_FOLD_ARGUMENT = _MissingFoldArgument()


def _fold_nonempty_binary_operation(
    operation: Callable[[_FoldParent, _FoldElement, _FoldElement], _FoldElement],
    parent: _FoldParent,
    elements: Sequence[_FoldElement],
) -> _FoldElement:
    assert len(elements) >= 1, (
        "foldable binary operation requires a nonempty sequence"
    )
    result = elements[0]
    for element in elements[1:]:
        result = operation(parent, result, element)
    return result


def foldable_operation(
    operation: Callable[[_FoldParent, _FoldElement, _FoldElement], _FoldElement],
) -> _FoldableOperation[_FoldParent, _FoldElement]:
    r"""Decorate a binary method with the standard nonempty-sequence fold."""

    @wraps(operation)
    def folded_operation(
        parent: _FoldParent,
        left_or_elements: _FoldElement | Sequence[_FoldElement],
        right: _FoldElement | _MissingFoldArgument = _MISSING_FOLD_ARGUMENT,
    ) -> _FoldElement:
        if right is _MISSING_FOLD_ARGUMENT:
            assert isinstance(left_or_elements, Sequence), (
                "sequence overload requires a finite sequence"
            )
            return _fold_nonempty_binary_operation(
                operation,
                parent,
                left_or_elements,
            )
        return operation(
            parent,
            cast(_FoldElement, left_or_elements),
            cast(_FoldElement, right),
        )

    return cast(_FoldableOperation[_FoldParent, _FoldElement], folded_operation)


def _is_project_method_provider(cls: type) -> bool:
    return getattr(cls, "__module__", "").startswith(PROJECT_MODULE_PREFIX)


def _abstract_method_owner(cls: type, name: str) -> type | None:
    for base in cls.__mro__:
        attr = base.__dict__.get(name)
        if attr is not None and isinstance(attr, AbstractMethod) and _is_project_method_provider(base):
            return base
    return None


def _validate_no_missing_abc_methods(X: Parent) -> None:
    missing = sorted(getattr(type(X), "__abstractmethods__", ()))
    if not missing:
        return

    details = []
    for name in missing:
        owner = _abstract_method_owner(type(X), name)
        if owner is None:
            details.append(name)
        else:
            details.append(f"{name} ({owner.__name__})")

    detail_str = ", ".join(details)
    assert not missing, f"Can't refine category of {type(X).__name__}: unimplemented abstract methods: {detail_str}"


def refine_category(X: Parent, C: Category | Sequence[Category], test: bool = True) -> Parent:
    X._refine_category_(C)
    _validate_no_missing_abc_methods(X)
    if test:
        X._test_not_implemented_methods()
    return X


def assert_smoke_statements(statements: tuple[tuple[str, Callable[[Any], bool]], ...]) -> None:
    failures: list[str] = []
    for message, statement in statements:
        # This is the allowed smoke-harness exception pattern: spec smokes are
        # frontier sensors, so one missing method must not hide the rest of the
        # missing surface.  The failures are still reported and made fatal
        # after every labeled statement has run.
        try:
            assert statement(None), message
        except Exception as exc:
            failures.append(f"{message}: {type(exc).__name__}: {exc}")

    assert not failures, "\n".join(failures)
