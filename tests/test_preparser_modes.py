r"""Contract tests for the preparser's keyword modes and error surface.

These pin the two real call shapes of the installed preparser:

- ``preparse(cell)`` — whole-cell transform used by ``SagePreparseTransformer``;
- ``preparse(contents, do_time=True, ignore_prompts=False,
  numeric_literals=False)`` — the shape ``sage.repl.preparse.preparse_file``
  uses for ``.sage`` files (``time`` keyword active, no numeric wrapping).

Plain-Python test file: source strings below pass only through the research
``preparse`` under test.
"""

import ast
import contextlib
import io
from pathlib import Path

import pytest

import sage.repl.load  # noqa: F401  (the wrapped load directive references it)
from dzack_research.preamble.preparser import lower, preparse, preparse_file

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


def test_preparse_file_keeps_match_case_integer_patterns() -> None:
    source = (
        "def classify(x):\n"
        "    match x:\n"
        "        case 0:\n"
        "            return 0\n"
        "        case -1:\n"
        "            return -1\n"
        "        case 1 | 2:\n"
        "            return 12\n"
        "        case _:\n"
        "            return x\n"
    )
    transformed = preparse_file(source)

    assert "_sage_const_" not in transformed
    namespace = dict(globals())
    exec(transformed, namespace)
    classify = namespace["classify"]
    assert (classify(0), classify(-1), classify(2), classify(7)) == (0, -1, 12, 7)


def test_preparse_file_time_keyword_is_active() -> None:
    namespace = dict(globals())
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        exec(preparse_file("time r = 3^4"), namespace)

    assert namespace["r"] == 81
    assert "Time: CPU" in buffer.getvalue()


def test_preparse_file_wraps_bare_load_directives(tmp_path: Path) -> None:
    loaded = tmp_path / "loaded.sage"
    loaded.write_text("w = 2^10\n")
    contents = f"before = 2^2\nload {loaded}\nafter = before + w\n"

    namespace = dict(globals())
    exec(preparse_file(contents), namespace)

    assert namespace["w"] == 1024
    assert namespace["after"] == 1028


def test_source_map_translates_verbatim_positions_exactly() -> None:
    result = lower("R.<x, y> = QQ[]\nq = 2^5 + zz\n")

    generated_column = result.python.split("\n")[1].find("zz")
    assert result.source_map.original_position(2, generated_column) == (2, 10)


def test_source_map_points_rebuilt_constructs_at_their_origin() -> None:
    result = lower("v = 1\nR.<x, y> = QQ[]\n")

    assert result.python.split("\n")[1].startswith("R = QQ[")
    assert result.source_map.original_position(2, 20) == (2, 0)


def test_source_map_translates_a_real_syntax_error() -> None:
    result = lower("R.<x> = QQ[]\ndef broken(:\n    pass\n")

    with pytest.raises(SyntaxError) as excinfo:
        compile(result.python, "<cell>", "exec")
    line, column = result.source_map.original_position(
        excinfo.value.lineno or 0, excinfo.value.offset or 0
    )
    assert line == 2 and column == 12


def test_source_map_generated_position_round_trips_verbatim_spans() -> None:
    result = lower("R.<x, y> = QQ[]\nq = 2^5 + zz\n")

    line, column = result.source_map.generated_position(2, 10)
    assert result.python.split("\n")[line - 1][column : column + 2] == "zz"
    assert result.source_map.original_position(line, column) == (2, 10)


def test_source_map_generated_position_anchors_rebuilt_constructs() -> None:
    result = lower("v = 1\nR.<x, y> = QQ[]\n")

    assert result.source_map.generated_position(2, 8) == (2, 0)


def test_lint_sensitive_constructs_lower_to_ordinary_python() -> None:
    # The construct list sage-lsp monkey-patches into pycodestyle
    # (E201/E202/E225/E227/E231 suppressions around `R.<...>` and `^^`).
    # Lowering removes the need for any of that: the output is ordinary
    # Python that the stock toolchain parses.
    for source in (
        "R.<x, y> = QQ[]",
        "R.< x , y > = QQ[]",
        "b = 123 ^^ 123",
        "w = 5r + 2.5R + 0xEAr",
    ):
        ast.parse(preparse(source))


def test_backslash_operator_surfaces_as_syntax_error() -> None:
    with pytest.raises(SyntaxError):
        compile(preparse("A \\ B"), "<cell>", "exec")


def test_unbalanced_bracket_surfaces_as_syntax_error() -> None:
    with pytest.raises(SyntaxError):
        compile(preparse("r = [1.."), "<cell>", "exec")
