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
before any of them runs a line.  Each test module calls ``install_preamble``
itself -- that is what puts the preamble's names in *their* globals -- and it
finds the work already done.
"""

from __future__ import annotations

# Sage's namespace comes in first, and the star import is the spelling that
# brings all of it: with only the preamble imported here, ``GF(5)^3`` and
# ``Zmod(6)^3`` arrive in a later test module carrying none of the owned
# free-module methods.  Whatever the intake path over a finite ring reads, it
# reads it from a session that has already imported ``sage.all``.
from sage.all import *  # noqa: F403

from dzack_research.preamble.install import install_preamble

install_preamble(globals())