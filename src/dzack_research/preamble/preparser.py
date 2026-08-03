r"""The research preamble's complete extension of Sage's preparser.

The module composes Sage's native preparser with the research notation and owns
installation into both Sage preprocessing entrypoints. Brace literals without a
top-level ``:`` are sets, dictionaries remain dictionaries, and mathematical
set builders become ``ImageSet`` or ``ConditionSet`` expressions.

The transformation is token-based: strings and comments are never inspected as
source text. Sage syntax is lowered first, so this layer never reconstructs
Sage's generator-declaration grammar.
"""

from __future__ import annotations

import io
import tokenize
from typing import Any

from sage.repl import interpreter as sage_interpreter
from sage.repl import preparse as sage_preparse

_native_preparse = sage_preparse.preparse
_layout_token_types = {
    tokenize.INDENT,
    tokenize.DEDENT,
    tokenize.NEWLINE,
    tokenize.NL,
}


def _previous_nonlayout_token(
    tokens: list[tuple[int, str]], position: int
) -> tuple[int, str] | None:
    pointer = position - 1
    while pointer >= 0 and tokens[pointer][0] in _layout_token_types:
        pointer -= 1
    return None if pointer < 0 else tokens[pointer]


def _tokens(source: str) -> list[tuple[int, str]]:
    return [
        (token.type, token.string)
        for token in tokenize.generate_tokens(io.StringIO(source).readline)
        if token.type not in {tokenize.ENCODING, tokenize.ENDMARKER}
    ]


def _untokenize(tokens: list[tuple[int, str]]) -> str:
    return tokenize.untokenize(tokens)


def _repair_match_case_pattern_integers(tokens: list[tuple[int, str]]) -> list[tuple[int, str]]:
    """Restore ``case Integer/N`` pattern constants to plain integer tokens.

    Sage's preparse rewrites integer literals in match patterns as
    ``Integer(<n>)`` (and ``-Integer(<n>)``), which is invalid pattern syntax.
    """
    repaired = []
    index = 0
    while index < len(tokens):
        token_type, token_string = tokens[index]
        if token_type != tokenize.NAME or token_string != "case":
            repaired.append((token_type, token_string))
            index += 1
            continue

        repaired.append((token_type, token_string))
        index += 1
        while index < len(tokens) and tokens[index][0] in _layout_token_types:
            repaired.append(tokens[index])
            index += 1

        pattern_start = index
        if index < len(tokens) and tokens[index] == (tokenize.OP, "*"):
            index += 1
            while index < len(tokens) and tokens[index][0] in _layout_token_types:
                index += 1
            pattern_start = index
        sign = 1
        if index < len(tokens) and tokens[index] == (tokenize.OP, "-"):
            sign = -1
            index += 1
            while index < len(tokens) and tokens[index][0] in _layout_token_types:
                index += 1
            if index >= len(tokens):
                break

        if index < len(tokens) and tokens[index][0] == tokenize.NAME:
            if tokens[index][1].startswith("_sage_const_"):
                suffix = tokens[index][1][12:]
                if suffix.isdigit():
                    repaired.append((tokenize.NUMBER, str(int(suffix) * sign)))
                    index += 1
                    continue

            if (
                tokens[index] == (tokenize.NAME, "Integer")
                and index + 3 < len(tokens)
                and tokens[index + 1] == (tokenize.OP, "(")
            ):
                index += 2
                while index < len(tokens) and tokens[index][0] in _layout_token_types:
                    index += 1
                if (
                    index < len(tokens)
                    and tokens[index][0] == tokenize.NUMBER
                    and tokens[index][1].isdigit()
                    and index + 1 < len(tokens)
                    and tokens[index + 1] == (tokenize.OP, ")")
                ):
                    value = int(tokens[index][1]) * sign
                    repaired.append((tokenize.NUMBER, str(value)))
                    index += 2
                    continue

        # Not a recognized constant pattern: keep tokens verbatim.
        repaired.extend(tokens[pattern_start:index])
    return repaired


def _repair_match_subject_multiplication(tokens: list[tuple[int, str]]) -> list[tuple[int, str]]:
    """Drop implicit-multiplication stars in ``match`` subject positions.

    ``match *foo(...)`` is produced by Sage's implicit-multiplication preparse
    but is invalid Python.
    """
    repaired: list[tuple[int, str]] = []
    index = 0
    while index < len(tokens):
        token_type, token_string = tokens[index]
        repaired.append((token_type, token_string))
        index += 1
        if token_type != tokenize.NAME or token_string != "match":
            continue

        while index < len(tokens) and tokens[index][0] in _layout_token_types:
            repaired.append(tokens[index])
            index += 1

        if index < len(tokens) and tokens[index] == (tokenize.OP, "*"):
            index += 1
            while index < len(tokens) and tokens[index][0] in _layout_token_types:
                index += 1
        continue
    return repaired


def _binder(
    tokens: list[tuple[int, str]],
) -> tuple[str, str, str | None] | None:
    r"""Parse ``x in X`` or ``x in X and P(x)`` at top level."""
    tokens = [
        token
        for token in tokens
        if token[0] not in _layout_token_types
    ]
    if len(tokens) < 3 or tokens[0][0] != tokenize.NAME or tokens[1][1] != "in":
        return None
    depth = 0
    separator = None
    for position, (_, token) in enumerate(tokens[2:], start=2):
        if token in {"(", "[", "{"}:
            depth += 1
        elif token in {")", "]", "}"}:
            depth -= 1
        elif depth == 0 and token == "and":
            separator = position
            break
    match separator:
        case None:
            domain_tokens = tokens[2:]
            condition_tokens = []
        case int():
            domain_tokens = tokens[2:separator]
            condition_tokens = tokens[separator + 1 :]
    domain = _untokenize(_implicit_products(domain_tokens)).strip()
    assert domain, "a set-builder domain cannot be empty"
    condition = _untokenize(_implicit_products(condition_tokens)).strip()
    if separator is not None and not condition:
        raise SyntaxError("a set-builder predicate cannot be empty")
    return tokens[0][1], domain, condition or None


def _condition_builder(
    variable: str, domain: str, condition: str
) -> list[tuple[int, str]]:
    return _tokens(f"ConditionSet({domain}, lambda {variable}: {condition})")


def _implicit_products(tokens: list[tuple[int, str]]) -> list[tuple[int, str]]:
    """Insert the multiplication Sage's preparser cannot insert in lambdas."""
    result: list[tuple[int, str]] = []
    for token in tokens:
        if (
            result
            and result[-1][0] == tokenize.NUMBER
            and token[0] == tokenize.NAME
        ):
            result.append((tokenize.OP, "*"))
        result.append(token)
    return result


def _rewrite(tokens: list[tuple[int, str]]) -> list[tuple[int, str]]:
    rewritten: list[tuple[int, str]] = []
    index = 0
    while index < len(tokens):
        token_type, token_string = tokens[index]
        if token_type == tokenize.FSTRING_START:
            fstring_depth = 1
            rewritten.append((token_type, token_string))
            index += 1
            while index < len(tokens) and fstring_depth:
                fstring_token = tokens[index]
                if fstring_token[0] == tokenize.FSTRING_START:
                    fstring_depth += 1
                if fstring_token[0] == tokenize.FSTRING_END:
                    fstring_depth -= 1
                rewritten.append(fstring_token)
                index += 1
            continue
        if token_string != "{":
            rewritten.append((token_type, token_string))
            index += 1
            continue

        depth = 1
        close = index + 1
        while close < len(tokens) and depth:
            if tokens[close][1] == "{":
                depth += 1
            elif tokens[close][1] == "}":
                depth -= 1
            close += 1
        if depth:
            rewritten.append((token_type, token_string))
            index += 1
            continue

        original_inner = tokens[index + 1 : close - 1]
        inner = _rewrite(original_inner)
        nested_depth = 0
        has_top_level_colon = False
        has_top_level_unpack = False
        top_level_bars = []
        for position, (inner_type, inner_string) in enumerate(original_inner):
            if inner_string in {"(", "[", "{"}:
                nested_depth += 1
            elif inner_string in {
                ")",
                "]",
                "}",
            }:
                nested_depth -= 1
            elif nested_depth == 0 and inner_string == ":":
                has_top_level_colon = True
            elif (
                nested_depth == 0
                and (
                    inner_string == "**"
                    or (
                        inner_string == "*"
                        and position + 1 < len(original_inner)
                        and original_inner[position + 1][1] == "*"
                    )
                )
                and (
                    position == 0
                    or (
                        (previous := _previous_nonlayout_token(original_inner, position))
                        and previous[1] == ","
                    )
                )
            ):
                has_top_level_unpack = True
            elif nested_depth == 0 and inner_string == "|":
                top_level_bars.append(position)

        if has_top_level_colon or has_top_level_unpack:
            rewritten.extend([(tokenize.OP, "{"), *inner, (tokenize.OP, "}")])
        elif len(top_level_bars) == 1:
            bar = top_level_bars[0]
            left = _rewrite(original_inner[:bar])
            right = _rewrite(original_inner[bar + 1 :])

            left_binder = _binder(left)
            right_binder = _binder(right)
            match left_binder, right_binder:
                # ``{x in X | P(x)}`` — a predicate-defined subset.
                case (tuple() as left_binding), _:
                    variable, domain, left_condition = left_binding
                    assert left_condition is None, (
                        "the predicate belongs to the right of the set-builder bar"
                    )
                    cond_text = _untokenize(_implicit_products(right)).strip()
                    if not cond_text:
                        raise SyntaxError("a set-builder predicate cannot be empty")
                    rewritten.extend(
                        _condition_builder(variable, domain, cond_text)
                    )
                # ``{f(x) | x in X}`` and
                # ``{f(x) | x in X and P(x)}``.
                case None, (tuple() as right_binding):
                    v_name, d_name, c_expr = right_binding
                    image = _untokenize(_implicit_products(left)).strip()
                    if c_expr is None:
                        restricted_domain = d_name
                    else:
                        restricted_domain = (
                            f"ConditionSet({d_name}, "
                            f"lambda {v_name}: {c_expr})"
                        )
                    if image == v_name:
                        if c_expr is None:
                            rewritten.extend(_tokens(f"Set({d_name})"))
                        else:
                            rewritten.extend(_tokens(restricted_domain))
                    else:
                        rewritten.extend(
                            _tokens(
                                f"ImageSet(Lambda({v_name}, {image}), {restricted_domain})"
                            )
                        )
                # A non-builder bar is an ordinary expression.
                case None, None:
                    rewritten.extend(
                        _tokens("Set([" + _untokenize(inner) + "])")
                    )
        elif not inner:
            rewritten.extend([(tokenize.OP, "{"), *inner, (tokenize.OP, "}")])
        else:
            replacement = _tokens("Set([" + _untokenize(inner) + "])")
            rewritten.extend(replacement)
        index = close
    return rewritten


def _rewrite_set_literals(source: str) -> str:
    r"""Rewrite mathematical brace-set literals in one source fragment."""
    return _untokenize(_rewrite(_tokens(source)))


def preparse(source: str, *args: Any, **kwargs: Any) -> str:
    r"""Apply Sage's preparser and then the research notation."""
    sage_preparse.implicit_multiplication(True)
    native = _native_preparse(source, *args, **kwargs)
    repaired = _repair_match_case_pattern_integers(_tokens(native))
    repaired = _repair_match_subject_multiplication(repaired)
    return _rewrite_set_literals(_untokenize(repaired))


def install_preparser() -> None:
    r"""Install the research preparser into Sage's two preprocessing surfaces."""
    match sage_preparse.preparse, sage_interpreter.preparse:
        case module_preparse, interpreter_preparse if (
            module_preparse is preparse and interpreter_preparse is preparse
        ):
            return
        case module_preparse, interpreter_preparse if (
            module_preparse is _native_preparse
            and interpreter_preparse is _native_preparse
        ):
            sage_preparse.preparse = preparse
            sage_interpreter.preparse = preparse
        case unexpected:
            raise RuntimeError(
                "Sage's preparser entrypoints are not in an installable state: "
                f"{unexpected!r}"
            )
