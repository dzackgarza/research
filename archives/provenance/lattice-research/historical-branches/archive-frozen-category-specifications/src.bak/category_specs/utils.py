import logging
import os
from collections.abc import Callable, Sequence
from functools import wraps
from textwrap import dedent
from typing import Any, Protocol, TypeVar, cast, overload, runtime_checkable

from sage.categories.category import Category
from sage.structure.parent import Parent

CATEGORY_DIAGNOSTIC_LOGGER_NAME = "category_specs.diagnostics"

_FoldParent = TypeVar("_FoldParent", contravariant=True)
_FoldElement = TypeVar("_FoldElement")
_CATEGORY_DIAGNOSTICS_ENABLED = False
_CATEGORY_DIAGNOSTIC_LOGGER = logging.getLogger(CATEGORY_DIAGNOSTIC_LOGGER_NAME)
_EMITTED_CATEGORY_DIAGNOSTICS: set[str] = set()


def category_diagnostics_enabled() -> bool:
    r"""Return whether opt-in category diagnostics are enabled."""
    return _CATEGORY_DIAGNOSTICS_ENABLED


def set_category_diagnostics_enabled(enabled: bool) -> None:
    r"""Set the process-local category diagnostics flag."""
    global _CATEGORY_DIAGNOSTICS_ENABLED
    _CATEGORY_DIAGNOSTICS_ENABLED = enabled


def enable_category_diagnostics() -> None:
    r"""Enable opt-in category diagnostic logging for this process."""
    set_category_diagnostics_enabled(True)


def disable_category_diagnostics() -> None:
    r"""Disable category diagnostic logging for this process."""
    set_category_diagnostics_enabled(False)


def category_diagnostic_logger() -> logging.Logger:
    r"""Return the category diagnostic logger."""
    return _CATEGORY_DIAGNOSTIC_LOGGER


def clear_category_diagnostic_history() -> None:
    r"""Clear the once-per-key category diagnostic history."""
    _EMITTED_CATEGORY_DIAGNOSTICS.clear()


def emit_category_diagnostic(
    message: str,
    *,
    key: str | None = None,
    once: bool = True,
) -> None:
    r"""Emit an opt-in category diagnostic warning.

    Diagnostics are disabled by default and logging-only.  They are for
    mathematically valid but non-obvious conventions, not for recovering from
    invalid hypotheses or implementation gaps.
    """
    if not _CATEGORY_DIAGNOSTICS_ENABLED:
        return
    if once and key is not None:
        if key in _EMITTED_CATEGORY_DIAGNOSTICS:
            return
        _EMITTED_CATEGORY_DIAGNOSTICS.add(key)
    _CATEGORY_DIAGNOSTIC_LOGGER.warning(message)


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


@runtime_checkable
class _CategoryAxiomRefiner(Protocol):
    def _with_axiom(self, axiom: str) -> Category: ...


def with_axiom(category: object, axiom: str) -> Category:
    r"""Return Sage's dynamic axiom refinement for ``category``."""
    if not isinstance(category, _CategoryAxiomRefiner):
        raise TypeError(f"{type(category).__name__} does not expose _with_axiom")
    return category._with_axiom(axiom)


def _fold_nonempty_binary_operation[FoldParent, FoldElement](
    operation: Callable[[FoldParent, FoldElement, FoldElement], FoldElement],
    parent: FoldParent,
    elements: Sequence[FoldElement],
) -> FoldElement:
    assert len(elements) >= 1, "foldable binary operation requires a nonempty sequence"
    result: FoldElement = elements[0]
    for element in elements[1:]:
        result = operation(parent, result, element)
    return result


def foldable_operation[FoldParent, FoldElement](
    operation: Callable[[FoldParent, FoldElement, FoldElement], FoldElement],
) -> _FoldableOperation[FoldParent, FoldElement]:
    r"""Decorate a binary method with the standard nonempty-sequence fold."""

    @wraps(operation)
    def folded_operation(
        parent: FoldParent,
        left_or_elements: FoldElement | Sequence[FoldElement],
        right: FoldElement | _MissingFoldArgument = _MISSING_FOLD_ARGUMENT,
    ) -> FoldElement:
        if right is _MISSING_FOLD_ARGUMENT:
            assert isinstance(left_or_elements, Sequence), "sequence overload requires a finite sequence"
            return _fold_nonempty_binary_operation(
                operation,
                parent,
                cast(Sequence[FoldElement], left_or_elements),
            )
        return operation(
            parent,
            cast(FoldElement, left_or_elements),
            cast(FoldElement, right),
        )

    return cast("_FoldableOperation[FoldParent, FoldElement]", folded_operation)


@overload
def refine_category[_ParentClassT: type[Parent]](
    X: _ParentClassT,
    C: Category | Sequence[Category],
    test: bool = True,
) -> _ParentClassT: ...


@overload
def refine_category[_ParentT: Parent](
    X: _ParentT,
    C: Category | Sequence[Category],
    test: bool = True,
) -> _ParentT: ...


def refine_category[_ParentT: Parent, _ParentClassT: type[Parent]](
    X: _ParentT | _ParentClassT,
    C: Category | Sequence[Category],
    test: bool = True,
) -> _ParentT | _ParentClassT:
    from .cat.base_category_types import refine_parent_category, refine_parent_class

    categories = tuple(C) if isinstance(C, (list, tuple)) else (C,)
    if isinstance(X, type):
        return cast(_ParentClassT, refine_parent_class(X, categories))
    refine_parent_category(X, categories)
    return X


def _format_category_statement_failure(message: str, exc: Exception) -> str:
    return f"{message}: {type(exc).__name__}: {exc}"


def _run_category_statement(
    message: str,
    statement: Callable[[Any], bool],
) -> str | None:
    try:
        assert statement(None), message
    except Exception as exc:
        return _format_category_statement_failure(message, exc)
    return None


def _write_all(fd: int, payload: bytes) -> None:
    view = memoryview(payload)
    while view:
        written = os.write(fd, view)
        view = view[written:]


def _run_category_statement_isolated(
    message: str,
    statement: Callable[[Any], bool],
) -> str | None:
    if not hasattr(os, "fork"):
        return _run_category_statement(message, statement)

    read_fd, write_fd = os.pipe()
    pid = os.fork()
    if pid == 0:
        os.close(read_fd)
        failure = _run_category_statement(message, statement)
        payload = b"" if failure is None else failure.encode("utf-8", "backslashreplace")
        try:
            _write_all(write_fd, payload)
        finally:
            os.close(write_fd)
        os._exit(0 if failure is None else 1)

    os.close(write_fd)
    chunks: list[bytes] = []
    while True:
        chunk = os.read(read_fd, 8192)
        if not chunk:
            break
        chunks.append(chunk)
    os.close(read_fd)
    _, status = os.waitpid(pid, 0)

    failure = b"".join(chunks).decode("utf-8", "replace")
    if os.WIFEXITED(status):
        exit_status = os.WEXITSTATUS(status)
        if exit_status == 0:
            return None
        return failure or f"{message}: category assertion child exited with status {exit_status}"
    if os.WIFSIGNALED(status):
        return f"{message}: category assertion child terminated by signal {os.WTERMSIG(status)}"
    return failure or f"{message}: category assertion child ended with wait status {status}"


def assert_category_statements(
    statements: tuple[tuple[str, Callable[[Any], bool]], ...],
) -> None:
    failures: list[str] = []
    for message, statement in statements:
        # Run every assertion so one failed obligation does not hide other
        # failed obligations for the same category example set.
        failure = _run_category_statement_isolated(message, statement)
        if failure is not None:
            failures.append(failure)

    assert not failures, _format_category_obligation_failure_message(failures)


def _format_category_obligation_failure_message(failures: list[str]) -> str:
    reminder = dedent(
        """
        Failed category assertions are mathematical evidence, not a spec-weakening signal.
    
        A failed category assertion means that the tested object does not currently
        satisfy the declared category obligation, or that the asserted obligation is
        misstated. It is not by itself evidence that the category definition should
        be weakened.
    
        Before editing specs, abstract methods, constructor routing, or category
        assertions in response to this output, load:
        - category-spec-style
        - category-spec-obligation-test-triage
        - category-spec-workflow
    
        Also check repo memory:
        - .agents/memories/category-specs-sage-interop-is-a-design-constraint.md
    
        Do not remove or move a category obligation merely because a tested Sage
        object fails it. Either implement the missing obligation, refine the object
        through a correct constructor, or prove that the obligation belongs to a
        different weakest category.
    
        Before advancing the task, review git diff output and any task-local commits
        for deleted obligations, narrowed category assertions, or Sage-gap-driven
        interface shrinkage.
        """
    ).strip()
    return f"{reminder}\n\nFailed category assertions:\n" + "\n".join(failures)
