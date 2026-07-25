r"""Interactive-session ergonomics: the non-mathematical half of the old init.sage.

Nothing here has a mathematical home, which is exactly why it can live in a
module of its own without violating naming doctrine. It owns one question --
what a fresh interactive namespace contains -- and answers nothing about
lattices.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable
from typing import Any


def lmap[T, U](f: Callable[[T], U], ls: Iterable[T]) -> list[U]:
    """``list(map(f, ls))``. Carried over from the old init.sage verbatim."""
    return list(map(f, ls))


def lzip(*iterables: Iterable[Any]) -> list[tuple[Any, ...]]:
    """``list(zip(*iterables))``. Carried over from the old init.sage verbatim."""
    return list(zip(*iterables))


def to_var_names(s: str) -> list[str]:
    """Split a comma-separated generator-name string into stripped names.

    The old init.sage used this to feed generator lists; kept because notebooks
    still write basis names as one string.
    """
    return [x.replace(" ", "").strip() for x in s.split(",")]


def enable_implicit_multiplication() -> None:
    """Turn on Sage's implicit multiplication preparsing (``2x`` for ``2*x``).

    Separate from :func:`install` because it changes how *source* is read, which
    is a bigger commitment than adding names to a namespace: it can turn a typo
    into a valid expression. Off unless asked for.
    """
    from sage.repl.preparse import implicit_multiplication

    implicit_multiplication(True)


def load_gap_package_manager() -> None:
    """Load GAP's ``PackageManager``, as old init.sage line 19 did at startup.

    Separate and opt-in: it reaches into a GAP subprocess, which is a slow and
    failure-prone thing to do unconditionally when starting a kernel.
    """
    from sage.libs.gap.libgap import libgap

    libgap.LoadPackage("PackageManager")


def enable_red_traceback_highlight() -> None:
    """Highlight the current frame in tracebacks on red, as the old init.sage did."""
    import IPython.core.ultratb

    IPython.core.ultratb.VerboseTB._tb_highlight = "bg:ansired"
