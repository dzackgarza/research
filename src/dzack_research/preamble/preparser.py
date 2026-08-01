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


def _tokens(source: str) -> list[tuple[int, str]]:
    return [
        (token.type, token.string)
        for token in tokenize.generate_tokens(io.StringIO(source).readline)
        if token.type not in {tokenize.ENCODING, tokenize.ENDMARKER}
    ]


def _untokenize(tokens: list[tuple[int, str]]) -> str:
    return tokenize.untokenize(tokens)


def _binder(
    tokens: list[tuple[int, str]],
) -> tuple[str, str, str | None] | None:
    r"""Parse ``x in X`` or ``x in X and P(x)`` at top level."""
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
            elif nested_depth == 0 and inner_string == "**":
                has_top_level_unpack = True
            elif nested_depth == 0 and inner_string == "|":
                top_level_bars.append(position)

        if top_level_bars:
            if len(top_level_bars) != 1:
                raise SyntaxError("set-builder notation has exactly one top-level bar")
            bar = top_level_bars[0]
            left = _rewrite(original_inner[:bar])
            right = _rewrite(original_inner[bar + 1 :])

            # ``{x in X | P(x)}`` — a predicate-defined subset.
            left_binder = _binder(left)
            if left_binder is not None:
                variable, domain, left_condition = left_binder
                assert left_condition is None, (
                    "the predicate belongs to the right of the set-builder bar"
                )
                condition = _untokenize(_implicit_products(right)).strip()
                if not condition:
                    raise SyntaxError("a set-builder predicate cannot be empty")
                rewritten.extend(_condition_builder(variable, domain, condition))
            else:
                # ``{f(x) | x in X}`` and ``{f(x) | x in X and P(x)}``.
                right_binder = _binder(right)
                if right_binder is None:
                    raise SyntaxError(
                        "set-builder syntax must use x in X as its domain"
                    )
                variable, domain, condition = right_binder
                image = _untokenize(_implicit_products(left)).strip()
                if condition is None:
                    restricted_domain = domain
                else:
                    restricted_domain = f"ConditionSet({domain}, lambda {variable}: {condition})"
                if image == variable:
                    if condition is None:
                        rewritten.extend(
                            _condition_builder(variable, domain, "True")
                        )
                    else:
                        rewritten.extend(_tokens(restricted_domain))
                else:
                    rewritten.extend(
                        _tokens(
                            f"ImageSet(lambda {variable}: {image}, "
                            f"{restricted_domain})"
                        )
                    )
        elif not inner or has_top_level_colon or has_top_level_unpack:
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
    return _rewrite_set_literals(_native_preparse(source, *args, **kwargs))


def install_preparser() -> None:
    r"""Install the research preparser into Sage's two preprocessing surfaces."""
    sage_preparse.implicit_multiplication(True)
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
