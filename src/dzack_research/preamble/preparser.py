r"""Sage-session surfaces over the SagePython compiler.

``sagepython`` owns recognition and lowering (sage-free); this module
owns what only exists inside a Sage session: the ``preparse``
entrypoint contract, ``.sage``-file handling, and installation into
Sage's preprocessing hooks.  ``time``, prompt stripping, and
``load``/``attach`` are frontend text protocols handled here, around
the core compiler.
"""

from __future__ import annotations

import re

from sage.repl import interpreter as sage_interpreter
from sage.repl import preparse as sage_preparse
from sage.repl.load import load_wrap

from dzack_research.preamble.sagepython import (  # noqa: F401  (re-exports)
    LoweredSource,
    Segment,
    SourceMap,
    lower,
)

_native_preparse = sage_preparse.preparse
_native_preparse_file = sage_preparse.preparse_file


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

    return lower(line, wrap_numbers=numeric_literals).python


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
