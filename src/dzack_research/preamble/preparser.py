r"""The research preamble's Sage preparser, rebuilt on CPython's tokenizer.

The preamble owns the complete source-to-Python transformation: Sage's
regex preparser is no longer consulted.  CPython's ``tokenize`` module is
the grammar authority — every Sage construct (``2x``, ``R.<x>``, ``[1..5]``,
``1.sqrt()``, ``f(x) = x^2``, ``^``) is token-level valid Python, so Sage's
syntax delta lives entirely at the parse level, where a token-stream pass
can lower it.  Strings, comments, f-strings (including nesting and format
specifiers), indentation, and continuation lines are therefore handled by
CPython itself, never by this module.

Architecture: an ordered pipeline of lowering passes.  Each pass reads the
freshly tokenized cell and returns :class:`Edit` objects — replacements of
source spans — which are applied right-to-left; the cell is re-lexed
between passes.  Untouched source (spacing, comments, f-string text) is
preserved verbatim.

Pipeline order:

1. ``time`` statements (``do_time`` mode only)
2. brace set literals and set builders (the preamble's notation)
3. generator declarations  (``R.<x,y> = QQ[]``)
4. calculus assignments    (``f(x) = x^2``)
5. ellipsis ranges         (``[1..n]``, ``(a..b)``; runs to fixpoint)
6. generator indexing      (``R.0``)
7. caret operators         (``^`` power, ``^^`` xor, augmented forms)
8. implicit multiplication (``2x``, ``(x+1)y``, ``a b``)
9. numeric literals        (``Integer``/``RealNumber``/``ComplexNumber``
   wrapping and ``2r``/``5jr`` raw suffixes)

``case`` pattern positions are excluded from implicit multiplication and
numeric wrapping: literal patterns match Sage numbers by equality, so
``case 1 | 2:`` stays valid Python.
"""

from __future__ import annotations

import bisect
import io
import keyword
import re
import tokenize
from dataclasses import dataclass
from typing import Callable

from sage.repl import interpreter as sage_interpreter
from sage.repl import preparse as sage_preparse
from sage.repl.load import load_wrap

_native_preparse = sage_preparse.preparse
_native_preparse_file = sage_preparse.preparse_file

TokenInfo = tokenize.TokenInfo
Pos = tuple[int, int]

_LAYOUT = {
    tokenize.COMMENT,
    tokenize.NL,
    tokenize.NEWLINE,
    tokenize.INDENT,
    tokenize.DEDENT,
    tokenize.ENCODING,
    tokenize.ENDMARKER,
}
_LITERAL_TOKENS = {
    tokenize.STRING,
    tokenize.FSTRING_START,
    tokenize.FSTRING_MIDDLE,
    tokenize.FSTRING_END,
    tokenize.COMMENT,
}
_OPENERS = frozenset("([{")
_CLOSERS = frozenset(")]}")
_RAW_SUFFIXES = frozenset({"R", "L", "RL", "LR", "RJ", "JR"})
_NO_MULTIPLY_NAMES = frozenset({"print", "exec"})
_SOFT_KEYWORD_HEADS = frozenset({"match", "case", "time", "type"})
_NUMERIC_NAME_PREFIX = "_sage_const_"
_HUGE_INTEGER_DIGITS = 4300


@dataclass(frozen=True)
class Edit:
    """Replace ``source[start:end]`` (tokenize row/column spans) with ``text``."""

    start: Pos
    end: Pos
    text: str


class _Cell:
    """One lexed cell: source, tokens, and position arithmetic."""

    def __init__(self, source: str) -> None:
        self.source = source
        self.tokens = _lex(source)
        self.offsets = [0]
        for line in source.split("\n"):
            self.offsets.append(self.offsets[-1] + len(line) + 1)
        self.significant = [
            index
            for index, token in enumerate(self.tokens)
            if token.type not in _LAYOUT
        ]

    def index(self, position: Pos) -> int:
        row, column = position
        return self.offsets[row - 1] + column

    def position(self, index: int) -> Pos:
        row = bisect.bisect_right(self.offsets, index)
        return row, index - self.offsets[row - 1]

    def text(self, start: Pos, end: Pos) -> str:
        return self.source[self.index(start) : self.index(end)]

    def statements(self) -> list[list[int]]:
        """Significant-token index lists split at depth-0 boundaries.

        Boundaries are logical newlines, depth-0 semicolons, and depth-0
        comments — the same statement model Sage's preparser used.
        """
        result: list[list[int]] = []
        current: list[int] = []
        depth = 0
        for index, token in enumerate(self.tokens):
            if token.type == tokenize.OP and token.string in _OPENERS:
                depth += 1
            elif token.type == tokenize.OP and token.string in _CLOSERS:
                depth -= 1
            if (
                token.type == tokenize.NEWLINE
                or (token.type == tokenize.COMMENT and depth == 0)
                or (token.type == tokenize.OP and token.string == ";" and depth == 0)
            ):
                if current:
                    result.append(current)
                    current = []
            elif token.type not in _LAYOUT:
                current.append(index)
        if current:
            result.append(current)
        return result


def _lex(source: str) -> list[TokenInfo]:
    # Boundary translation: tokenize's failure protocol is TokenError; the
    # preparser's contract is SyntaxError.
    try:
        return list(tokenize.generate_tokens(io.StringIO(source).readline))
    except tokenize.TokenError as error:
        raise SyntaxError(f"invalid Sage input: {error}") from None


def _apply(cell: _Cell, edits: list[Edit]) -> str:
    ordered = sorted(edits, key=lambda edit: cell.index(edit.start), reverse=True)
    for later, earlier in zip(ordered, ordered[1:]):
        assert cell.index(earlier.end) <= cell.index(later.start), (
            "overlapping preparser edits"
        )
    source = cell.source
    for edit in ordered:
        source = source[: cell.index(edit.start)] + edit.text + source[cell.index(edit.end) :]
    return source


def _case_pattern_indices(cell: _Cell) -> set[int]:
    """Token indices inside ``case`` patterns (subject to no literal wrapping)."""
    banned: set[int] = set()
    for statement in cell.statements():
        head = cell.tokens[statement[0]]
        if head.type != tokenize.NAME or head.string != "case":
            continue
        depth = 0
        pattern: list[int] = []
        is_case_statement = False
        for index in statement[1:]:
            token = cell.tokens[index]
            if token.type == tokenize.OP and token.string in _OPENERS:
                depth += 1
            elif token.type == tokenize.OP and token.string in _CLOSERS:
                depth -= 1
            if depth == 0 and token.type == tokenize.OP and token.string in {"=", ":="}:
                break
            if depth == 0 and token.type == tokenize.OP and token.string == ":":
                is_case_statement = True
                break
            if depth == 0 and token.type == tokenize.NAME and token.string == "if":
                is_case_statement = True  # the guard is ordinary code
                break
            pattern.append(index)
        if is_case_statement:
            banned.update(pattern)
    return banned


# ---------------------------------------------------------------------------
# Pass: time statements (preparse_file mode)
# ---------------------------------------------------------------------------

def _time_statements(cell: _Cell) -> list[Edit]:
    edits = []
    for statement in cell.statements():
        head = cell.tokens[statement[0]]
        if head.type != tokenize.NAME or head.string != "time" or len(statement) < 2:
            continue
        rest_first = cell.tokens[statement[1]]
        if rest_first.start[0] != head.start[0]:
            continue
        last = cell.tokens[statement[-1]]
        rest = cell.text(rest_first.start, last.end)
        edits.append(
            Edit(
                head.start,
                last.end,
                "__time__ = cputime(); __wall__ = walltime(); "
                f"{rest}; "
                'print("Time: CPU {:.2f} s, Wall: {:.2f} s"'
                ".format(cputime(__time__), walltime(__wall__)))",
            )
        )
    return edits


# ---------------------------------------------------------------------------
# Pass: brace set literals and set builders
# ---------------------------------------------------------------------------

def _set_literals(cell: _Cell) -> list[Edit]:
    edits = []
    for open_index, close_index in _outermost_brace_spans(cell):
        replacement = _brace_text(cell, open_index, close_index)
        if replacement is not None:
            edits.append(
                Edit(
                    cell.tokens[open_index].start,
                    cell.tokens[close_index].end,
                    replacement,
                )
            )
    return edits


def _outermost_brace_spans(cell: _Cell) -> list[tuple[int, int]]:
    """Outermost ``{...}`` token spans, ignoring f-string interiors."""
    spans = []
    fstring_depth = 0
    brace_depth = 0
    open_index = -1
    for index, token in enumerate(cell.tokens):
        if token.type == tokenize.FSTRING_START:
            fstring_depth += 1
        elif token.type == tokenize.FSTRING_END:
            fstring_depth -= 1
        if fstring_depth or token.type != tokenize.OP:
            continue
        if token.string == "{":
            if brace_depth == 0:
                open_index = index
            brace_depth += 1
        elif token.string == "}" and brace_depth:
            brace_depth -= 1
            if brace_depth == 0:
                spans.append((open_index, index))
    return spans


def _matching_brace(cell: _Cell, open_index: int, limit: int) -> int:
    depth = 0
    for index in range(open_index, limit):
        token = cell.tokens[index]
        if token.type != tokenize.OP:
            continue
        if token.string == "{":
            depth += 1
        elif token.string == "}":
            depth -= 1
            if depth == 0:
                return index
    raise AssertionError("unbalanced braces inside a matched span")


def _region_text(cell: _Cell, indices: list[int]) -> str:
    """Source text of a token range with nested brace literals rewritten."""
    if not indices:
        return ""
    pieces = []
    cursor = cell.tokens[indices[0]].start
    fstring_depth = 0
    position = 0
    while position < len(indices):
        index = indices[position]
        token = cell.tokens[index]
        if token.type == tokenize.FSTRING_START:
            fstring_depth += 1
        elif token.type == tokenize.FSTRING_END:
            fstring_depth -= 1
        if (
            fstring_depth == 0
            and token.type == tokenize.OP
            and token.string == "{"
        ):
            close_index = _matching_brace(cell, index, indices[-1] + 1)
            replacement = _brace_text(cell, index, close_index)
            if replacement is not None:
                pieces.append(cell.text(cursor, token.start))
                pieces.append(replacement)
                cursor = cell.tokens[close_index].end
            while position < len(indices) and indices[position] <= close_index:
                position += 1
            continue
        position += 1
    pieces.append(cell.text(cursor, cell.tokens[indices[-1]].end))
    return "".join(pieces)


def _binder(cell: _Cell, indices: list[int]) -> tuple[str, str, str | None] | None:
    r"""Parse ``x in X`` or ``x in X and P(x)`` at the top level of a region."""
    significant = [
        index for index in indices if cell.tokens[index].type not in _LAYOUT
    ]
    if len(significant) < 3:
        return None
    first, second = cell.tokens[significant[0]], cell.tokens[significant[1]]
    if first.type != tokenize.NAME or second.string != "in":
        return None
    depth = 0
    separator = None
    for position, index in enumerate(significant[2:], start=2):
        token = cell.tokens[index]
        if token.string in _OPENERS:
            depth += 1
        elif token.string in _CLOSERS:
            depth -= 1
        elif depth == 0 and token.type == tokenize.NAME and token.string == "and":
            separator = position
            break
    if separator is None:
        domain_indices = significant[2:]
        condition_indices: list[int] = []
    else:
        domain_indices = significant[2:separator]
        condition_indices = significant[separator + 1 :]
    domain = _region_text(cell, domain_indices).strip()
    assert domain, "a set-builder domain cannot be empty"
    condition = _region_text(cell, condition_indices).strip()
    if separator is not None and not condition:
        raise SyntaxError("a set-builder predicate cannot be empty")
    return first.string, domain, condition or None


def _brace_text(cell: _Cell, open_index: int, close_index: int) -> str | None:
    """Replacement text for one brace literal, or ``None`` to leave it alone."""
    inner = [
        index
        for index in range(open_index + 1, close_index)
        if cell.tokens[index].type not in _LAYOUT
    ]
    if not inner:
        return None

    depth = 0
    fstring_depth = 0
    has_colon = False
    has_unpack = False
    bars = []
    for position, index in enumerate(inner):
        token = cell.tokens[index]
        if token.type == tokenize.FSTRING_START:
            fstring_depth += 1
        elif token.type == tokenize.FSTRING_END:
            fstring_depth -= 1
        if fstring_depth or token.type != tokenize.OP:
            continue
        if token.string in _OPENERS:
            depth += 1
        elif token.string in _CLOSERS:
            depth -= 1
        elif depth == 0 and token.string == ":":
            has_colon = True
        elif (
            depth == 0
            and token.string == "**"
            and (position == 0 or cell.tokens[inner[position - 1]].string == ",")
        ):
            has_unpack = True
        elif depth == 0 and token.string == "|":
            bars.append(position)

    if has_colon or has_unpack:
        return "{" + _region_text(cell, inner) + "}"

    if len(bars) == 1:
        left = inner[: bars[0]]
        right = inner[bars[0] + 1 :]
        left_binder = _binder(cell, left)
        right_binder = _binder(cell, right)
        if left_binder is not None:
            # ``{x in X | P(x)}`` — a predicate-defined subset.
            variable, domain, condition = left_binder
            assert condition is None, (
                "the predicate belongs to the right of the set-builder bar"
            )
            predicate = _region_text(cell, right).strip()
            if not predicate:
                raise SyntaxError("a set-builder predicate cannot be empty")
            return f"ConditionSet({domain}, lambda {variable}: {predicate})"
        if right_binder is not None:
            # ``{f(x) | x in X}`` and ``{f(x) | x in X and P(x)}``.
            variable, domain, condition = right_binder
            image = _region_text(cell, left).strip()
            if condition is None:
                restricted = domain
            else:
                restricted = f"ConditionSet({domain}, lambda {variable}: {condition})"
            if image == variable:
                return f"Set({domain})" if condition is None else restricted
            return f"ImageSet(lambda {variable}: {image}, {restricted})"
        # A non-builder bar is an ordinary expression.
        return "Set([" + _region_text(cell, inner) + "])"

    return "Set([" + _region_text(cell, inner) + "])"


# ---------------------------------------------------------------------------
# Pass: generator declarations
# ---------------------------------------------------------------------------

def _generator_declarations(cell: _Cell) -> list[Edit]:
    edits = []
    for statement in cell.statements():
        edit = _generator_statement(cell, statement)
        if edit is not None:
            edits.append(edit)
    return edits


def _generator_statement(cell: _Cell, statement: list[int]) -> Edit | None:
    tokens = cell.tokens
    if len(statement) < 6:
        return None
    head, dot, less = (tokens[index] for index in statement[:3])
    if not (
        head.type == tokenize.NAME
        and not keyword.iskeyword(head.string)
        and dot.type == tokenize.OP
        and dot.string == "."
        and less.type == tokenize.OP
        and less.string == "<"
        and head.end == dot.start
        and dot.end == less.start
    ):
        return None

    # Generator names up to '>'.  A spaceless declaration fuses the closing
    # angle with the assignment into one '>=' token.
    gens = []
    cursor = 3
    expect_name = True
    fused_assignment = False
    while cursor < len(statement):
        token = tokens[statement[cursor]]
        if expect_name and token.type == tokenize.NAME:
            gens.append(token.string)
            expect_name = False
        elif not expect_name and token.string == ",":
            expect_name = True
        elif not expect_name and token.string == ">":
            break
        elif not expect_name and token.string == ">=":
            fused_assignment = True
            break
        else:
            return None
        cursor += 1
    if not gens or cursor >= len(statement):
        return None
    closer = tokens[statement[cursor]]
    cursor += 1

    # Optional extra assignment targets: ``F.<b>, f, g = ...``.
    targets_end = closer.end
    if not fused_assignment:
        while cursor < len(statement) and tokens[statement[cursor]].string != "=":
            token = tokens[statement[cursor]]
            if not (token.type == tokenize.NAME or token.string == ","):
                return None
            targets_end = token.end
            cursor += 1
        if cursor >= len(statement) or tokens[statement[cursor]].string != "=":
            return None
        cursor += 1
    targets = "" if fused_assignment else cell.text(closer.end, targets_end)
    rhs = statement[cursor:]
    if not rhs:
        return None

    constructor = _constructor_with_names(cell, rhs, gens)
    last = tokens[rhs[-1]]
    gens_tuple = ", ".join(gens)
    replacement = (
        f"{head.string}{targets} = {constructor}; "
        f"({gens_tuple},) = {head.string}._first_ngens({len(gens)})"
    )
    return Edit(head.start, last.end, replacement)


def _constructor_with_names(cell: _Cell, rhs: list[int], gens: list[str]) -> str:
    tokens = cell.tokens
    first, last = tokens[rhs[0]], tokens[rhs[-1]]
    names = "('" + "', '".join(gens) + "',)"

    if last.string == ")":
        opener = _matching_opener(cell, rhs, "(", ")")
        if opener is None:
            return cell.text(first.start, last.end)
        has_arguments = any(
            tokens[index].type not in _LAYOUT
            for index in rhs
            if tokens[opener].end <= tokens[index].start
            and tokens[index].end <= last.start
        )
        comma = ", " if has_arguments else ""
        return cell.text(first.start, last.start) + f"{comma}names={names})"

    if last.string == "]":
        bracket_openers = [
            index for index in rhs
            if tokens[index].type == tokenize.OP and tokens[index].string == "["
        ]
        if not bracket_openers:
            return cell.text(first.start, last.end)
        opener = bracket_openers[-1]
        closer = _matching_closer(cell, rhs, opener, "[", "]")
        empty = not any(
            tokens[index].type not in _LAYOUT
            for index in rhs
            if tokens[opener].end <= tokens[index].start
            and tokens[index].end <= tokens[closer].start
        )
        if empty:
            quoted = "'" + ", ".join(gens) + "'"
            return (
                cell.text(first.start, tokens[opener].end)
                + quoted
                + cell.text(tokens[closer].start, last.end)
            )
        return cell.text(first.start, last.end)

    return cell.text(first.start, last.end)


def _matching_opener(
    cell: _Cell, indices: list[int], opening: str, closing: str
) -> int | None:
    """Index of the opener matching the final ``closing`` token of ``indices``."""
    depth = 0
    for index in reversed(indices):
        token = cell.tokens[index]
        if token.type != tokenize.OP:
            continue
        if token.string == closing:
            depth += 1
        elif token.string == opening:
            depth -= 1
            if depth == 0:
                return index
    return None


def _matching_closer(
    cell: _Cell, indices: list[int], opener: int, opening: str, closing: str
) -> int:
    depth = 0
    for index in indices:
        if index < opener:
            continue
        token = cell.tokens[index]
        if token.string == opening:
            depth += 1
        elif token.string == closing:
            depth -= 1
            if depth == 0:
                return index
    raise AssertionError("unbalanced constructor brackets")


# ---------------------------------------------------------------------------
# Pass: calculus assignments
# ---------------------------------------------------------------------------

def _calculus_assignments(cell: _Cell) -> list[Edit]:
    edits = []
    for statement in cell.statements():
        edit = _calculus_statement(cell, statement)
        if edit is not None:
            edits.append(edit)
    return edits


def _calculus_statement(cell: _Cell, statement: list[int]) -> Edit | None:
    tokens = cell.tokens
    if len(statement) < 5:
        return None
    head = tokens[statement[0]]
    if (
        head.type != tokenize.NAME
        or keyword.iskeyword(head.string)
        or head.string in _SOFT_KEYWORD_HEADS
        or tokens[statement[1]].string != "("
    ):
        return None

    parameters = []
    cursor = 2
    expect_name = True
    while cursor < len(statement):
        token = tokens[statement[cursor]]
        if expect_name and token.type == tokenize.NAME:
            parameters.append(token.string)
            expect_name = False
        elif not expect_name and token.string == ",":
            expect_name = True
        elif not expect_name and token.string == ")":
            break
        else:
            return None
        cursor += 1
    if not parameters or cursor >= len(statement):
        return None
    cursor += 1
    if cursor >= len(statement) or tokens[statement[cursor]].string != "=":
        return None
    expression = statement[cursor + 1 :]
    if not expression:
        return None

    variables = ",".join(parameters)
    body = cell.text(tokens[expression[0]].start, tokens[expression[-1]].end)
    replacement = (
        f'__tmp__=var("{variables}"); '
        f"{head.string} = symbolic_expression({body}).function({variables})"
    )
    return Edit(head.start, tokens[expression[-1]].end, replacement)


# ---------------------------------------------------------------------------
# Pass: ellipsis ranges
# ---------------------------------------------------------------------------

def _masked_source(cell: _Cell) -> str:
    """Source with string/f-string/comment payload characters blanked."""
    masked = list(cell.source)
    for token in cell.tokens:
        if token.type not in _LITERAL_TOKENS:
            continue
        for index in range(cell.index(token.start), cell.index(token.end)):
            if masked[index] != "\n":
                masked[index] = " "
    return "".join(masked)


def _containing_block(code: str, index: int) -> tuple[int, int] | None:
    """Bounds of the innermost ``()``/``[]`` block containing ``index``."""
    openings, closings = "([", ")]"
    levels = [0, 0]
    start = index
    kind = 0
    while start >= 0:
        if code[start] in openings:
            kind = openings.index(code[start])
            levels[kind] -= 1
            if levels[kind] == -1:
                break
        elif code[start] in closings and start < index:
            levels[closings.index(code[start])] += 1
        start -= 1
    if start == -1 or levels.count(0) != 1:
        return None
    end = index
    while end < len(code):
        if code[end] in closings:
            found = closings.index(code[end])
            levels[found] += 1
            if found == kind and levels[found] == 0:
                break
        elif code[end] in openings and end > index:
            levels[openings.index(code[end])] -= 1
        end += 1
    if levels != [0, 0]:
        return None
    return start, end + 1


def _is_range_dots(masked: str, index: int) -> bool:
    """A ``..`` at ``index`` that is not part of a ``...`` Ellipsis."""
    if masked[index : index + 2] != "..":
        return False
    before = index > 0 and masked[index - 1] == "."
    after = masked[index + 2 : index + 3] == "."
    return not before and not after


def _ellipsis_ranges(cell: _Cell) -> list[Edit]:
    masked = _masked_source(cell)
    index = masked.find("..")
    while index != -1 and not _is_range_dots(masked, index):
        index = masked.find("..", index + 1)
    if index <= 0:
        return []

    block = _containing_block(masked, index)
    if block is None:
        return []
    start, end = block
    # Narrow to the innermost block whose ellipses must be lowered first.
    probe = masked.find("..", index + 2, end)
    while probe != -1:
        if _is_range_dots(masked, probe):
            inner = _containing_block(masked, probe)
            if inner is None:
                return []
            start, end = inner
        probe = masked.find("..", probe + 2, end)

    arguments = _ellipsis_arguments(cell.source, masked, start + 1, end - 1)
    kind = "range" if masked[start] == "[" else "iter"
    return [
        Edit(
            cell.position(start),
            cell.position(end),
            f"(ellipsis_{kind}({arguments}))",
        )
    ]


def _ellipsis_arguments(source: str, masked: str, start: int, end: int) -> str:
    pieces: list[str] = []
    index = start
    while index < end:
        if masked[index] == "." and masked[index + 1 : index + 2] == ".":
            run = 3 if masked[index + 2 : index + 3] == "." else 2
            # Absorb an adjacent separating comma on either side.
            while pieces and pieces[-1] and pieces[-1][-1].isspace():
                pieces[-1] = pieces[-1][:-1]
            if pieces and pieces[-1] and pieces[-1][-1] == ",":
                pieces[-1] = pieces[-1][:-1]
            index += run
            while index < end and masked[index].isspace():
                index += 1
            if index < end and masked[index] == ",":
                index += 1
            pieces.append(",Ellipsis,")
            continue
        pieces.append(source[index])
        index += 1
    return "".join(pieces)


# ---------------------------------------------------------------------------
# Pass: generator indexing (R.0)
# ---------------------------------------------------------------------------

def _generator_indexing(cell: _Cell) -> list[Edit]:
    edits = []
    tokens = cell.tokens
    for left_index, right_index in zip(cell.significant, cell.significant[1:]):
        left, right = tokens[left_index], tokens[right_index]
        if (
            right.type == tokenize.NUMBER
            and right.string.startswith(".")
            and right.string[1:].isdigit()
            and left.end == right.start
            and (
                left.type == tokenize.NAME
                or (left.type == tokenize.OP and left.string in {")", "]"})
            )
        ):
            edits.append(Edit(right.start, right.end, f".gen({int(right.string[1:])})"))
    return edits


# ---------------------------------------------------------------------------
# Pass: caret operators
# ---------------------------------------------------------------------------

def _caret_operators(cell: _Cell) -> list[Edit]:
    edits = []
    tokens = cell.tokens
    significant = cell.significant
    xor_pairs = {("^", "^"): "^", ("^", "^="): "^=", ("**", "**"): "^"}
    position = 0
    while position < len(significant):
        token = tokens[significant[position]]
        if position + 1 < len(significant):
            following = tokens[significant[position + 1]]
            if token.end == following.start:
                replacement = xor_pairs.get((token.string, following.string))
                if replacement is not None:
                    edits.append(Edit(token.start, following.end, replacement))
                    position += 2
                    continue
        if token.string == "^":
            edits.append(Edit(token.start, token.end, "**"))
        elif token.string == "^=":
            edits.append(Edit(token.start, token.end, "**="))
        position += 1
    return edits


# ---------------------------------------------------------------------------
# Pass: implicit multiplication (level 5 semantics, always on)
# ---------------------------------------------------------------------------

def _is_raw_suffix_pair(left: TokenInfo, right: TokenInfo) -> bool:
    return (
        left.type == tokenize.NUMBER
        and right.type == tokenize.NAME
        and left.end == right.start
        and right.string.upper() in _RAW_SUFFIXES
    )


def _implicit_multiplication(cell: _Cell) -> list[Edit]:
    edits = []
    tokens = cell.tokens
    banned = _case_pattern_indices(cell)
    statement_heads = {statement[0] for statement in cell.statements()}
    for left_index, right_index in zip(cell.significant, cell.significant[1:]):
        left, right = tokens[left_index], tokens[right_index]
        if left.end[0] != right.start[0]:
            continue  # multiplication never crosses a line
        if left_index in banned or right_index in banned:
            continue
        if (
            right.type != tokenize.NAME
            or keyword.iskeyword(right.string)
            or right.string in _NO_MULTIPLY_NAMES
        ):
            continue
        if left.type == tokenize.NUMBER:
            if _is_raw_suffix_pair(left, right):
                continue
            if left.string.endswith("."):
                continue  # ``87.factor()``: a method call, not a product
        elif left.type == tokenize.OP:
            if left.string != ")":
                continue
        elif left.type == tokenize.NAME:
            if keyword.iskeyword(left.string) or left.string in _NO_MULTIPLY_NAMES:
                continue
            if left_index in statement_heads and left.string in _SOFT_KEYWORD_HEADS:
                continue
            if not (
                left.end < right.start
                or left.string.startswith(_NUMERIC_NAME_PREFIX)
            ):
                continue
        else:
            continue
        edits.append(Edit(left.end, left.end, "*"))
    return edits


# ---------------------------------------------------------------------------
# Pass: numeric literals
# ---------------------------------------------------------------------------

def _integer_stem(text: str) -> str:
    """Decimal integer text with Sage's leading-zero tolerance applied."""
    stripped = text.lstrip("0")
    return stripped if stripped else "0"


def _numeric_wrapping(cell: _Cell, wrap: bool) -> list[Edit]:
    edits = []
    tokens = cell.tokens
    banned = _case_pattern_indices(cell)
    significant = cell.significant
    for position, index in enumerate(significant):
        token = tokens[index]
        if token.type != tokenize.NUMBER:
            continue
        following = (
            tokens[significant[position + 1]]
            if position + 1 < len(significant)
            else None
        )

        if following is not None and _is_raw_suffix_pair(token, following):
            text = token.string
            if "J" in following.string.upper():
                base = text[:-1] if text[-1] in "jJ" else text
                replacement = base + "J"
            elif text[-1] in "jJ":
                replacement = text[:-1] + "J"
            else:
                replacement = text
            edits.append(Edit(token.start, following.end, replacement))
            continue

        if not wrap or index in banned:
            continue

        text = token.string
        if text[-1] in "jJ":
            edits.append(
                Edit(token.start, token.end, f"ComplexNumber(0, '{text[:-1]}')")
            )
        elif text[:2].lower() in {"0x", "0o", "0b"}:
            edits.append(Edit(token.start, token.end, f"Integer({text})"))
        elif (
            text.endswith(".")
            and following is not None
            and following.type == tokenize.NAME
            and token.end == following.start
        ):
            # ``5.sqrt()``: the dot is a method call, not a decimal point.
            edits.append(
                Edit(token.start, token.end, f"Integer({_integer_stem(text[:-1])}).")
            )
        elif "." in text or "e" in text or "E" in text:
            edits.append(Edit(token.start, token.end, f"RealNumber('{text}')"))
        else:
            stem = _integer_stem(text)
            if len(stem) <= _HUGE_INTEGER_DIGITS:
                edits.append(Edit(token.start, token.end, f"Integer({stem})"))
            else:
                edits.append(Edit(token.start, token.end, f"Integer('{stem}')"))
    return edits


# ---------------------------------------------------------------------------
# The preparser
# ---------------------------------------------------------------------------

def _strip_prompts(line: str) -> str:
    for prompt in ("sage:", ">>>"):
        if line.startswith(prompt):
            return line[len(prompt) :].lstrip()
    return line


def preparse(
    line: str,
    reset: bool = True,
    do_time: bool = False,
    ignore_prompts: bool = False,
    numeric_literals: bool = True,
) -> str:
    r"""Transform one cell of Sage source into ordinary Python source.

    The signature matches ``sage.repl.preparse.preparse``; ``reset`` is
    accepted for compatibility but unused — every call transforms a whole,
    lexically complete cell.
    """
    del reset
    if line.lstrip().startswith("..."):
        cut = line.find("...") + 3
        return line[:cut] + preparse(
            line[cut:],
            do_time=do_time,
            ignore_prompts=ignore_prompts,
            numeric_literals=numeric_literals,
        )
    if ignore_prompts:
        line = _strip_prompts(line)

    passes: list[tuple[Callable[[_Cell], list[Edit]], bool]] = []
    if do_time:
        passes.append((_time_statements, False))
    passes += [
        (_set_literals, False),
        (_generator_declarations, False),
        (_calculus_assignments, False),
        (_ellipsis_ranges, True),
        (_generator_indexing, False),
        (_caret_operators, False),
        (_implicit_multiplication, False),
        (lambda cell: _numeric_wrapping(cell, wrap=numeric_literals), False),
    ]

    source = line
    for lowering, to_fixpoint in passes:
        while True:
            cell = _Cell(source)
            edits = lowering(cell)
            if not edits:
                break
            source = _apply(cell, edits)
            if not to_fixpoint:
                break
    return source


_LOAD_ATTACH = re.compile(r"^(\s*)(load|attach) ([^(].*)$", re.MULTILINE)


def preparse_file(
    contents: str,
    globals: dict | None = None,
    numeric_literals: bool = True,
) -> str:
    r"""Preparse the contents of a ``.sage`` file.

    The signature matches ``sage.repl.preparse.preparse_file``.  Bare
    ``load``/``attach`` directives are wrapped exactly as Sage wraps them;
    the ``time`` keyword is active.  Sage's ``_sage_const_`` hoisting was a
    loop optimization, not parsing — inline wrapping is semantically
    identical (and, unlike hoisting, keeps ``match`` patterns valid) — so
    ``globals`` and ``numeric_literals`` are accepted but unused.
    """
    del globals, numeric_literals
    assert isinstance(contents, str), "preparse_file expects a string"
    lines: list[str] = []
    start = 0
    for directive in _LOAD_ATTACH.finditer(contents):
        lines += preparse(contents[start : directive.start()], do_time=True).splitlines()
        lines.append(
            directive.group(1)
            + load_wrap(directive.group(3), directive.group(2) == "attach")
        )
        start = directive.end()
    lines += preparse(contents[start:], do_time=True).splitlines()
    return "\n".join(lines)


def install_preparser() -> None:
    r"""Install the research preparser into Sage's preprocessing surfaces."""
    if (
        sage_preparse.preparse is preparse
        and sage_interpreter.preparse is preparse
        and sage_preparse.preparse_file is preparse_file
    ):
        return
    if not (
        sage_preparse.preparse is _native_preparse
        and sage_interpreter.preparse is _native_preparse
        and sage_preparse.preparse_file is _native_preparse_file
    ):
        raise RuntimeError(
            "Sage's preparser entrypoints are not in an installable state"
        )
    sage_preparse.preparse = preparse
    sage_interpreter.preparse = preparse
    sage_preparse.preparse_file = preparse_file
