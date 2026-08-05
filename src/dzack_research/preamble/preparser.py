r"""The research preamble's Sage preparser: a compiler over tree-sitter-sage.

The grammar (github.com/dzackgarza/tree-sitter-sage, a dialect fork of
tree-sitter-python) owns recognition of the Sage language delta; this
module owns only lowering to ordinary Python, which CPython then compiles
as the semantic authority.

Lowering is a recursive re-emission of the parse tree: nodes without a
rule are spliced — verbatim source with lowered children — so untouched
text (comments, spacing, f-string internals) survives exactly.  Nodes
with a rule rebuild their text from lowered fields:

- ``sage_generator_assignment``   ``R.<x,y> = QQ[]`` → constructor call
  with ``names=`` plus ``_first_ngens`` unpacking
- ``sage_symbolic_function_assignment``   ``f(x) = x^2`` → ``var`` +
  ``symbolic_expression(...).function(...)``
- ``sage_generator_access``   ``R.0`` → ``R.gen(0)``
- ``sage_ellipsis_span`` / ``sage_ellipsis`` inside brackets →
  ``ellipsis_range`` / ``ellipsis_iter`` calls
- ``sage_raw_literal``   ``5r``/``2.5R``/``10jr`` → raw Python literals
- ``sage_implicit_product``   ``2x`` → ``2*x``
- ``^``/``^^`` (and augmented forms) → ``**``/``^``
- numeric literals → ``Integer``/``RealNumber``/``ComplexNumber``, except
  inside ``case`` patterns, where literal equality already matches Sage
  numbers
- brace notation: ``{1, 2}`` → ``Set([...])``; the research set-builder
  forms are canonical Python expression shapes (CPython precedence makes
  ``{f(x) | x in D and P}`` parse as
  ``and(comparison(f(x)|x, in, D), P)``) and lower to ``ImageSet`` /
  ``ConditionSet`` / ``Set``; dictionaries stay dictionaries

``time``, prompt stripping, and ``load``/``attach`` are frontend text
protocols, not SagePython grammar, and are handled textually around the
core compiler.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, replace
from typing import Callable

import tree_sitter_sage
from tree_sitter import Language, Node, Parser

from sage.repl import interpreter as sage_interpreter
from sage.repl import preparse as sage_preparse
from sage.repl.load import load_wrap

_native_preparse = sage_preparse.preparse
_native_preparse_file = sage_preparse.preparse_file

_LANGUAGE = Language(tree_sitter_sage.language())
_PARSER = Parser(_LANGUAGE)

_HUGE_INTEGER_DIGITS = 4300
_RAW_SUFFIX = re.compile(r"[rRlLjJ]+$")


@dataclass(frozen=True)
class _Context:
    source: bytes
    wrap_numbers: bool = True
    in_case_pattern: bool = False

    def text(self, node: Node) -> str:
        return self.source[node.start_byte : node.end_byte].decode("utf-8")


def _lower(node: Node, context: _Context) -> str:
    if node.type == "case_pattern" and not context.in_case_pattern:
        context = replace(context, in_case_pattern=True)
    rule = _LOWERINGS.get(node.type)
    if rule is not None:
        return rule(node, context)
    return _splice(node, context)


def _splice(node: Node, context: _Context) -> str:
    pieces = []
    cursor = node.start_byte
    for child in node.children:
        pieces.append(context.source[cursor : child.start_byte].decode("utf-8"))
        pieces.append(_lower(child, context))
        cursor = child.end_byte
    pieces.append(context.source[cursor : node.end_byte].decode("utf-8"))
    return "".join(pieces)


def _gap(left: Node, right: Node, context: _Context) -> str:
    return context.source[left.end_byte : right.start_byte].decode("utf-8")


# ---------------------------------------------------------------------------
# Numeric literals
# ---------------------------------------------------------------------------

def _integer_stem(text: str) -> str:
    stripped = text.lstrip("0")
    return stripped if stripped else "0"


def _lower_integer(node: Node, context: _Context) -> str:
    text = context.text(node)
    if not context.wrap_numbers or context.in_case_pattern:
        return text
    if text[-1] in "jJ":
        return f"ComplexNumber(0, '{text[:-1]}')"
    if text[:2].lower() in {"0x", "0o", "0b"}:
        return f"Integer({text})"
    stem = _integer_stem(text)
    if len(stem) <= _HUGE_INTEGER_DIGITS:
        return f"Integer({stem})"
    return f"Integer('{stem}')"


def _lower_float(node: Node, context: _Context) -> str:
    text = context.text(node)
    if not context.wrap_numbers or context.in_case_pattern:
        return text
    if text[-1] in "jJ":
        return f"ComplexNumber(0, '{text[:-1]}')"
    return f"RealNumber('{text}')"


def _lower_raw_literal(node: Node, context: _Context) -> str:
    text = context.text(node)
    suffix = _RAW_SUFFIX.search(text)
    assert suffix is not None, f"raw literal without suffix: {text!r}"
    base = text[: suffix.start()]
    if "j" in suffix.group().lower():
        return base + "J"
    return base


# ---------------------------------------------------------------------------
# Operators
# ---------------------------------------------------------------------------

_CARET_OPERATORS = {"^": "**", "^^": "^", "^=": "**=", "^^=": "^="}


def _lower_operator_node(node: Node, context: _Context) -> str:
    operator = node.child_by_field_name("operator")
    if operator is None or operator.text is None:
        return _splice(node, context)
    replacement = _CARET_OPERATORS.get(operator.text.decode())
    if replacement is None:
        return _splice(node, context)
    pieces = []
    cursor = node.start_byte
    for child in node.children:
        pieces.append(context.source[cursor : child.start_byte].decode("utf-8"))
        if child.id == operator.id:
            pieces.append(replacement)
        else:
            pieces.append(_lower(child, context))
        cursor = child.end_byte
    pieces.append(context.source[cursor : node.end_byte].decode("utf-8"))
    return "".join(pieces)


def _lower_implicit_product(node: Node, context: _Context) -> str:
    left = node.child_by_field_name("left")
    right = node.child_by_field_name("right")
    assert left is not None and right is not None
    return (
        _lower(left, context)
        + "*"
        + _gap(left, right, context)
        + _lower(right, context)
    )


# ---------------------------------------------------------------------------
# Generators and symbolic functions
# ---------------------------------------------------------------------------

def _lower_generator_assignment(node: Node, context: _Context) -> str:
    name = node.child_by_field_name("name")
    right = node.child_by_field_name("right")
    assert name is not None and right is not None
    generators = [
        context.text(child)
        for child in node.children_by_field_name("generator")
    ]
    others = [
        context.text(child)
        for child in node.children_by_field_name("other_target")
    ]
    constructor = _lower_constructor(right, generators, context)
    obj = context.text(name)
    targets = "".join(f", {other}" for other in others)
    gens = ", ".join(generators)
    return (
        f"{obj}{targets} = {constructor}; "
        f"({gens},) = {obj}._first_ngens({len(generators)})"
    )


def _lower_constructor(right: Node, generators: list[str], context: _Context) -> str:
    names = "('" + "', '".join(generators) + "',)"
    if right.type == "sage_empty_subscript":
        value = right.child_by_field_name("value")
        assert value is not None
        quoted = "'" + ", ".join(generators) + "'"
        return f"{_lower(value, context)}[{quoted}]"
    if right.type == "call":
        arguments = right.child_by_field_name("arguments")
        assert arguments is not None
        lowered = _lower(right, context)
        has_arguments = any(
            child.is_named for child in arguments.children
        )
        comma = ", " if has_arguments else ""
        assert lowered.endswith(")")
        return f"{lowered[:-1]}{comma}names={names})"
    if right.type == "subscript":
        # `S.<q> = QQ[[]]`: fill an empty innermost bracket with the names.
        subscript = right.child_by_field_name("subscript")
        if subscript is not None and subscript.type == "list" and not any(
            child.is_named for child in subscript.children
        ):
            value = right.child_by_field_name("value")
            assert value is not None
            quoted = "'" + ", ".join(generators) + "'"
            return f"{_lower(value, context)}[[{quoted}]]"
    return _lower(right, context)


def _lower_symbolic_function(node: Node, context: _Context) -> str:
    name = node.child_by_field_name("name")
    body = node.child_by_field_name("body")
    assert name is not None and body is not None
    parameters = ",".join(
        context.text(child)
        for child in node.children_by_field_name("parameter")
    )
    return (
        f'__tmp__=var("{parameters}"); '
        f"{context.text(name)} = "
        f"symbolic_expression({_lower(body, context)}).function({parameters})"
    )


def _lower_generator_access(node: Node, context: _Context) -> str:
    target = node.child_by_field_name("object")
    index = node.child_by_field_name("index")
    assert target is not None and index is not None
    digits = context.text(index)[1:]
    return f"{_lower(target, context)}.gen({int(digits)})"


# ---------------------------------------------------------------------------
# Ellipsis ranges
# ---------------------------------------------------------------------------

def _ellipsis_arguments(elements: list[Node], context: _Context) -> str:
    pieces = []
    for element in elements:
        if element.type == "sage_ellipsis_span":
            start = element.child_by_field_name("start")
            end = element.child_by_field_name("end")
            assert start is not None and end is not None
            pieces.append(
                f"{_lower(start, context)},Ellipsis,{_lower(end, context)}"
            )
        elif element.type == "sage_ellipsis":
            pieces.append("Ellipsis")
        else:
            pieces.append(_lower(element, context))
    return ",".join(pieces)


def _has_ellipsis(elements: list[Node]) -> bool:
    return any(
        element.type in {"sage_ellipsis_span", "sage_ellipsis"}
        for element in elements
    )


def _named_elements(node: Node) -> list[Node]:
    return [child for child in node.children if child.is_named]


def _lower_list(node: Node, context: _Context) -> str:
    elements = _named_elements(node)
    if _has_ellipsis(elements):
        return f"(ellipsis_range({_ellipsis_arguments(elements, context)}))"
    return _splice(node, context)


def _lower_parenthesized(node: Node, context: _Context) -> str:
    elements = _named_elements(node)
    if _has_ellipsis(elements):
        return f"(ellipsis_iter({_ellipsis_arguments(elements, context)}))"
    return _splice(node, context)


def _lower_tuple(node: Node, context: _Context) -> str:
    elements = _named_elements(node)
    if _has_ellipsis(elements):
        return f"(ellipsis_iter({_ellipsis_arguments(elements, context)}))"
    return _splice(node, context)


# ---------------------------------------------------------------------------
# Brace notation: sets and the research set-builder forms
# ---------------------------------------------------------------------------

def _and_chain(node: Node) -> list[Node]:
    """Flatten a left-associated ``and`` chain into its operands."""
    if node.type == "boolean_operator":
        operator = node.child_by_field_name("operator")
        if operator is not None and operator.text == b"and":
            left = node.child_by_field_name("left")
            right = node.child_by_field_name("right")
            assert left is not None and right is not None
            return _and_chain(left) + [right]
    return [node]


def _comparison_chain(node: Node) -> tuple[list[Node], list[str]] | None:
    """Operands and operator spellings of a comparison chain."""
    if node.type != "comparison_operator":
        return None
    operands = [child for child in node.children if child.is_named]
    operators = [
        operator.text.decode()
        for operator in node.children_by_field_name("operators")
        if operator.text is not None
    ]
    if len(operands) != len(operators) + 1:
        return None
    return operands, operators


def _top_bitwise_or(node: Node) -> tuple[Node, Node] | None:
    if node.type == "binary_operator":
        operator = node.child_by_field_name("operator")
        if operator is not None and operator.text == b"|":
            left = node.child_by_field_name("left")
            right = node.child_by_field_name("right")
            assert left is not None and right is not None
            return left, right
    return None


def _lower_builder(element: Node, context: _Context) -> str | None:
    """Lower a one-element brace body if it is a set-builder form."""
    chain = _and_chain(element)
    head, conditions = chain[0], chain[1:]
    comparison = _comparison_chain(head)
    if comparison is None:
        return None
    operands, operators = comparison

    condition_text = " and ".join(
        _lower(condition, context) for condition in conditions
    )

    # Form A — `{image | x in domain [and P...]}`:
    # comparison(bitor(image, x), in, domain) [wrapped in `and` chain].
    if len(operands) == 2 and operators == ["in"]:
        split = _top_bitwise_or(operands[0])
        if split is not None and split[1].type == "identifier":
            image, variable = split
            domain = _lower(operands[1], context)
            variable_text = variable.text.decode() if variable.text else ""
            image_text = _lower(image, context)
            if condition_text:
                domain = f"ConditionSet({domain}, lambda {variable_text}: {condition_text})"
            if context.text(image).strip() == variable_text:
                return domain if condition_text else f"Set({domain})"
            return f"ImageSet(lambda {variable_text}: {image_text}, {domain})"

    # Form B — `{x in domain | P [and Q...]}`: the bar lands inside the
    # second operand, and a predicate containing comparisons continues
    # the chain: comparison(x, in, bitor(domain, P), op, rest...).
    if operands[0].type == "identifier" and operators[0] == "in":
        split = _top_bitwise_or(operands[1])
        if split is not None:
            domain, predicate_head = split
            variable_text = (
                operands[0].text.decode() if operands[0].text else ""
            )
            predicate = _lower(predicate_head, context)
            for operator, operand in zip(operators[1:], operands[2:]):
                predicate += f" {operator} {_lower(operand, context)}"
            if condition_text:
                predicate = f"{predicate} and {condition_text}"
            return (
                f"ConditionSet({_lower(domain, context)}, "
                f"lambda {variable_text}: {predicate})"
            )
    return None


def _lower_set(node: Node, context: _Context) -> str:
    elements = _named_elements(node)
    if len(elements) == 1:
        builder = _lower_builder(elements[0], context)
        if builder is not None:
            return builder
    if _has_ellipsis(elements):
        return f"Set((ellipsis_range({_ellipsis_arguments(elements, context)})))"
    inner = ", ".join(_lower(element, context) for element in elements)
    return f"Set([{inner}])"


def _lower_set_comprehension(node: Node, context: _Context) -> str:
    inner = _splice(node, context)
    assert inner.startswith("{") and inner.endswith("}")
    return f"Set([{inner[1:-1]}])"


# ---------------------------------------------------------------------------
# The lowering table and the preparser
# ---------------------------------------------------------------------------

_LOWERINGS: dict[str, Callable[[Node, _Context], str]] = {
    "integer": _lower_integer,
    "float": _lower_float,
    "sage_raw_literal": _lower_raw_literal,
    "binary_operator": _lower_operator_node,
    "augmented_assignment": _lower_operator_node,
    "sage_implicit_product": _lower_implicit_product,
    "sage_generator_assignment": _lower_generator_assignment,
    "sage_symbolic_function_assignment": _lower_symbolic_function,
    "sage_generator_access": _lower_generator_access,
    "list": _lower_list,
    "parenthesized_expression": _lower_parenthesized,
    "tuple": _lower_tuple,
    "set": _lower_set,
    "set_comprehension": _lower_set_comprehension,
}

_TIME_STATEMENT = re.compile(r"^(\s*)time +(\S[^\n]*)$", re.MULTILINE)
_LOAD_ATTACH = re.compile(r"^(\s*)(load|attach) ([^(].*)$", re.MULTILINE)


def _strip_prompts(line: str) -> str:
    for prompt in ("sage:", ">>>"):
        if line.startswith(prompt):
            return line[len(prompt) :].lstrip()
    return line


def _wrap_time_statements(source: str) -> str:
    return _TIME_STATEMENT.sub(
        lambda match: (
            f"{match.group(1)}__time__ = cputime(); __wall__ = walltime(); "
            f"{match.group(2)}; "
            'print("Time: CPU {:.2f} s, Wall: {:.2f} s"'
            ".format(cputime(__time__), walltime(__wall__)))"
        ),
        source,
    )


def preparse(
    line: str,
    reset: bool = True,
    do_time: bool = False,
    ignore_prompts: bool = False,
    numeric_literals: bool = True,
) -> str:
    r"""Transform one cell of Sage source into ordinary Python source.

    The signature matches ``sage.repl.preparse.preparse``; ``reset`` is
    accepted for compatibility but unused — every call transforms a
    whole, lexically complete cell.
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
    if do_time:
        line = _wrap_time_statements(line)

    source = line.encode("utf-8")
    tree = _PARSER.parse(source)
    context = _Context(source=source, wrap_numbers=numeric_literals)
    return _lower(tree.root_node, context)


def preparse_file(
    contents: str,
    globals: dict | None = None,
    numeric_literals: bool = True,
) -> str:
    r"""Preparse the contents of a ``.sage`` file.

    The signature matches ``sage.repl.preparse.preparse_file``.  Bare
    ``load``/``attach`` directives are wrapped exactly as Sage wraps
    them; the ``time`` keyword is active.  Sage's ``_sage_const_``
    hoisting was a loop optimization, not parsing — inline wrapping is
    semantically identical — so ``globals`` and ``numeric_literals`` are
    accepted but unused.
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
