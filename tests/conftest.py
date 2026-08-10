r"""Install the preamble once, before any test module builds a Sage object.

Refinement is process-wide and applies to what is built after it.  Sage's
parents are cached by ``UniqueRepresentation``, so a lattice a test module
builds while importing -- ``IntegralLattice("A2")`` in a module-level table --
is the object every later module gets, refined or not.  Collect two such
modules in one process and the first one's timing decides whether the second
sees the preamble's methods at all: the suite failed here with ``'...' object
has no attribute 'Aut'`` on a file that passes when collected alone.

Loading here removes the race rather than ordering around it.  A conftest is
imported before the test modules beside it, so the refinements are in place
before any of them runs a line.  The modules keep their own ``load`` -- that
is what puts the preamble's names in *their* globals -- and it finds the work
already done.
"""

from __future__ import annotations

from pathlib import Path

import dzack_research

# The preamble is preparsed source: its lowered form spells literals as
# ``Integer(2)`` and ranges as ``ellipsis_range``.  A ``.py`` conftest gets no
# preparser prelude, so ``load`` would run that code against a namespace with
# none of those names.  This is the prelude, and it is why the star import is
# the right spelling here and nowhere else in the suite.
from sage.all import *  # noqa: F403
from sage.repl.load import load as _load

_PREAMBLE = Path(dzack_research.__file__).resolve().parent / "preamble"


def load(filename: str | Path, namespace: dict | None = None) -> None:
    r"""Run a ``.sage`` file the way a session does, into this namespace.

    ``install.sage`` loads its fifty-five files by writing ``load("...")``,
    one argument, because that is what a session provides.  The importable
    ``load`` takes the namespace explicitly, so this supplies it -- and puts
    itself in the namespace it supplies, which is what makes the nested loads
    inside the preamble resolve to this same spelling.
    """
    _load(str(filename), globals() if namespace is None else namespace)


load(_PREAMBLE / "install.sage")
