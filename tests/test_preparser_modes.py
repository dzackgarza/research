r"""Contract tests for the preparser's keyword modes and error surface.

These pin the two real call shapes of the installed preparser:

- ``preparse(cell)`` — whole-cell transform used by ``SagePreparseTransformer``;
- ``preparse(contents, do_time=True, ignore_prompts=False,
  numeric_literals=False)`` — the shape ``sage.repl.preparse.preparse_file``
  uses for ``.sage`` files (``time`` keyword active, no numeric wrapping).

Plain-Python test file: source strings below pass only through the research
``preparse`` under test.
"""

import contextlib
import io

import pytest

from dzack_research.preamble.preparser import preparse

from sage.all import (  # noqa: F401  (names used by the executed source)
    ZZ,
    QQ,
    Set,
    Integer,
    RealNumber,
    cputime,
    walltime,
    ellipsis_range,
)


def _execute(source: str, **preparse_kwargs) -> dict:
    namespace = dict(globals())
    exec(preparse(source, **preparse_kwargs), namespace)
    return namespace


def test_do_time_executes_statement_and_reports_timings() -> None:
    namespace = dict(globals())
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        exec(preparse("time r = 2^5", do_time=True), namespace)

    assert namespace["r"] == 32
    assert "Time: CPU" in buffer.getvalue() and "Wall:" in buffer.getvalue()


def test_do_time_without_time_keyword_is_plain_execution() -> None:
    namespace = _execute("r = 2 + 3", do_time=True)

    assert namespace["r"] == 5 and namespace["r"].parent() == ZZ


def test_numeric_literals_disabled_yields_python_ints_but_keeps_caret() -> None:
    namespace = _execute("r = 2^3 + 1", numeric_literals=False)

    assert namespace["r"] == 9 and type(namespace["r"]) is int


def test_ignore_prompts_strips_sage_prompt() -> None:
    namespace = _execute("sage: r = 2 + 2", ignore_prompts=True)

    assert namespace["r"] == 4 and namespace["r"].parent() == ZZ


def test_ignore_prompts_strips_doctest_prompt() -> None:
    namespace = _execute(">>> r = 3 + 2", ignore_prompts=True)

    assert namespace["r"] == 5


def test_doctest_continuation_prefix_is_preserved_and_rest_preparsed() -> None:
    out = preparse("...     x = 2^3")

    assert out.startswith("...")
    remainder = out[3:].lstrip()
    compile(remainder, "<continuation>", "exec")
    namespace = dict(globals())
    exec(remainder, namespace)
    assert namespace["x"] == 8


def test_empty_and_comment_only_cells_pass_through() -> None:
    for cell in ("", "# just a comment", "\n\n"):
        compile(preparse(cell), "<cell>", "exec")


def test_sequential_cells_are_independent() -> None:
    first = _execute("s = 'first'; r = 2^2")
    second = _execute("t = 'second'; r = 3^2")

    assert first["r"] == 4 and first["s"] == "first"
    assert second["r"] == 9 and second["t"] == "second"


def test_augmented_call_assignment_is_not_calculus_and_stays_invalid() -> None:
    out = preparse("f(x) -= 5")

    assert "symbolic_expression" not in out
    with pytest.raises(SyntaxError):
        compile(out, "<cell>", "exec")


def test_incomplete_generator_declaration_stays_invalid() -> None:
    with pytest.raises(SyntaxError):
        compile(preparse("R.<x> = "), "<cell>", "exec")


@pytest.mark.xfail(
    reason="composed sage preparser crashes with TokenError; rewrite red proof #308",
    strict=True,
)
def test_backslash_operator_surfaces_as_syntax_error() -> None:
    with pytest.raises(SyntaxError):
        compile(preparse("A \\ B"), "<cell>", "exec")


@pytest.mark.xfail(
    reason="composed sage preparser crashes with TokenError; rewrite red proof #308",
    strict=True,
)
def test_unbalanced_bracket_surfaces_as_syntax_error() -> None:
    with pytest.raises(SyntaxError):
        compile(preparse("r = [1.."), "<cell>", "exec")
