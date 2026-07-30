r"""Interactive Sage session defaults and small helpers.

``init.sage`` loads this so notebooks and the IPython REPL get the defaults
without calling anything.

EXAMPLES::

    sage: lmap(lambda x: x^2, [1, 2, 3])
    [1, 4, 9]
    sage: lzip([1, 2], ["a", "b"])
    [(1, 'a'), (2, 'b')]
"""

from collections.abc import Callable, Iterable
from typing import Any

import IPython.core.ultratb
from sage.libs.gap.libgap import libgap
from sage.repl.preparse import implicit_multiplication

__all__ = ["lmap", "lzip", "to_var_names"]

implicit_multiplication(True)
libgap.LoadPackage("PackageManager")
IPython.core.ultratb.VerboseTB._tb_highlight = "bg:ansired"

def lmap[T, U](f: Callable[[T], U], ls: Iterable[T]) -> list[U]:
    """Return ``map(f, ls)`` as a list."""
    return list(map(f, ls))

def lzip(*iterables: Iterable[Any]) -> list[tuple[Any, ...]]:
    """Return ``zip(*iterables)`` as a list."""
    return list(zip(*iterables))

def to_var_names(s: str) -> list[str]:
    """Split a comma-separated list of generator names.

    EXAMPLES::

        sage: from dzack_research.preamble.ergonomics import to_var_names
        sage: to_var_names("e, f, a1")
        ['e', 'f', 'a1']
    """
    return [x.replace(" ", "").strip() for x in s.split(",")]
