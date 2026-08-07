r"""Sage-session surfaces over the SagePython compiler.

``sagepython`` owns recognition and lowering (sage-free); this module
owns what only exists inside a Sage session: the ``preparse``
entrypoint contract, ``.sage``-file handling, and installation into
Sage's preprocessing hooks.  ``time``, prompt stripping, and
``load``/``attach`` are frontend text protocols handled here, around
the core compiler.
"""

from __future__ import annotations

import builtins
import re

from sage.categories.rings import Rings
from sage.repl import interpreter as sage_interpreter
from sage.repl import preparse as sage_preparse
from sage.repl.load import load_wrap
from sage.rings.integer import Integer
from sage.structure.parent import Parent

from sagepython import (  # noqa: F401  (re-exports)
    Context,
    LoweredSource,
    Node,
    Segment,
    SourceMap,
    lower,
    lower_node,
)
from sagepython.research import EXTENSION as _RESEARCH_NOTATION

_native_preparse = sage_preparse.preparse
_native_preparse_file = sage_preparse.preparse_file


_TIME_STATEMENT = re.compile(r"^(\s*)time +(\S[^\n]*)$", re.MULTILINE)
_LOAD_ATTACH = re.compile(r"^(\s*)(load|attach) ([^(].*)$", re.MULTILINE)


# ---------------------------------------------------------------------------
# ``R^n``: the caret is research notation, ``**`` is Python's operator
# ---------------------------------------------------------------------------

_ring_power = None


def register_ring_power(constructor) -> None:
    r"""Name the free module ``R^n`` builds for a ring ``R``.

    The preamble calls this once its own free module exists.  Until then
    -- and for every ring Sage builds inside its own algorithms, which
    write ``R**n`` in ordinary Python -- ``R^n`` is Sage's native power.
    """
    global _ring_power
    _ring_power = constructor


def research_pow(base, exponent):
    r"""Evaluate ``base ^ exponent`` as written in research source.

    Only a ring parent raised to a cardinality is the preamble's noun;
    everything else -- ring elements, group elements, symbolic
    expressions, non-ring parents -- is Python's ``**`` unchanged.
    """
    if (
        _ring_power is not None
        and isinstance(exponent, (int, Integer))
        and exponent >= 0
        and isinstance(base, Parent)
        and base in Rings()
    ):
        return _ring_power(base, exponent)
    return base**exponent


def _lower_caret(node: Node, context: Context) -> str | None:
    r"""Lower ``a ^ b`` to the research power and ``a ^^ b`` to Python's xor."""
    operator = node.child_by_field_name("operator")
    left = node.child_by_field_name("left")
    right = node.child_by_field_name("right")
    if operator is None or left is None or right is None:
        return None
    match operator.text:
        case b"^":
            return (
                f"research_pow({lower_node(left, context)}, "
                f"{lower_node(right, context)})"
            )
        case b"^^":
            return f"({lower_node(left, context)}) ^ ({lower_node(right, context)})"
        case _:
            return None


_CARET_NOTATION = {"binary_operator": _lower_caret}


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

    return lower(
        line,
        numbers="wrapped" if numeric_literals else "raw",
        extensions=(_RESEARCH_NOTATION, _CARET_NOTATION),
    ).python


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
    # Lowered source names this at every caret, including inside the
    # preamble's own scripts, so it is a builtin rather than a global of
    # any one namespace.
    builtins.research_pow = research_pow
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
