r"""Sage preparser extension for mathematical set literals.

Brace literals without a top-level ``:`` are set notation in the research
notebooks, so ``{a, b}`` is preparsed as ``Set([a, b])``.  Dictionary literals
remain dictionaries.  Image builders such as ``{f(x) | x in X}`` become Sage's
lazy ``ImageSet``; domain-and-predicate builders become lazy ``ConditionSet``
objects.  The transformation is token-based: strings, comments, and nested
literals are not inspected as source text.
"""

from __future__ import annotations

import io
import tokenize
from types import ModuleType
from typing import Any


def _tokens(source: str) -> list[tuple[int, str]]:
    return [(token.type, token.string) for token in tokenize.generate_tokens(io.StringIO(source).readline) if token.type not in {tokenize.ENCODING, tokenize.ENDMARKER}]


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


def _condition_builder(variable: str, domain: str, condition: str) -> list[tuple[int, str]]:
    return _tokens(f"ConditionSet({domain}, lambda {variable}: {condition})")


def _implicit_products(tokens: list[tuple[int, str]]) -> list[tuple[int, str]]:
    """Insert the multiplication Sage's preparser cannot insert in lambdas."""
    result: list[tuple[int, str]] = []
    for token in tokens:
        if result and result[-1][0] == tokenize.NUMBER and token[0] == tokenize.NAME:
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
                assert left_condition is None, "the predicate belongs to the right of the set-builder bar"
                condition = _untokenize(_implicit_products(right)).strip()
                if not condition:
                    raise SyntaxError("a set-builder predicate cannot be empty")
                rewritten.extend(_condition_builder(variable, domain, condition))
            else:
                # ``{f(x) | x in X}`` and ``{f(x) | x in X and P(x)}``.
                right_binder = _binder(right)
                if right_binder is None:
                    raise SyntaxError("set-builder syntax must use x in X as its domain")
                variable, domain, condition = right_binder
                image = _untokenize(_implicit_products(left)).strip()
                if condition is None:
                    restricted_domain = domain
                else:
                    restricted_domain = f"ConditionSet({domain}, lambda {variable}: {condition})"
                if image == variable:
                    if condition is None:
                        rewritten.extend(_condition_builder(variable, domain, "True"))
                    else:
                        rewritten.extend(_tokens(restricted_domain))
                else:
                    rewritten.extend(_tokens(f"ImageSet(lambda {variable}: {image}, {restricted_domain})"))
        elif not inner or has_top_level_colon or has_top_level_unpack:
            rewritten.extend([(tokenize.OP, "{"), *inner, (tokenize.OP, "}")])
        else:
            replacement = _tokens("Set([" + _untokenize(inner) + "])")
            rewritten.extend(replacement)
        index = close
    return rewritten


def rewrite_set_literals(source: str) -> str:
    r"""Rewrite mathematical brace-set literals in one source fragment."""
    return _untokenize(_rewrite(_tokens(source)))


def install_set_literal_preparser(preparse_module: ModuleType, interpreter_module: ModuleType) -> None:
    r"""Install the wrapper once on Sage's preparser and IPython transformer."""
    if getattr(preparse_module, "_dzack_set_literals_installed", False):
        return
    original = preparse_module.preparse

    def preparse_with_sets(line: str, *args: Any, **kwargs: Any) -> str:
        return rewrite_set_literals(original(line, *args, **kwargs))

    preparse_module.preparse = preparse_with_sets
    interpreter_module.preparse = preparse_with_sets
    preparse_module._dzack_set_literals_installed = True
