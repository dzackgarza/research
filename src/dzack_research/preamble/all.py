r"""The preamble's ``sage.all``: importing it is what makes a scope a session.

``from dzack_research.preamble.all import *`` binds the owned rings, the
catalogue and its specimens, and every constructor the preamble's modules
export -- the same names, from the same two calls, that ``init.sage`` binds
into a notebook.  A session's :math:`\ZZ` is then the owned ring, so
``ZZ^3`` is the free module the preamble builds and ``ZZ['x']`` the free
algebra; the engine's ring is still what Sage's algorithms hold, reached
through ``engine_ring`` at the boundary.

Named for the module it is the analogue of.  ``sage.all`` is the one import
that turns a plain Python scope into a Sage session, and this is the one
import that turns a Sage session into a preamble session; a session reaches
for it by that shape without being told the name.

**The rebinding hazard, and why ``load`` is exported here.**
``install_session_rings`` binds the session's ring names last, and its
docstring says it must be called again after every further ``load()``,
because a loaded script that imports Sage's namespace rebinds ``ZZ`` and
``QQ`` to the engine behind the session's back.  Left as an instruction that
is a trap: a caller who forgets it gets Sage's ring under the session's name,
silently, which is the failure the owned rings exist to remove.  So the
instruction is not left to the caller -- the ``load`` bound by this module is
the one that discharges it.

A hand-typed ``from sage.all import *`` in a later cell rebinds the same
names and no module can hook that.  The remedy is the one ``sage.all``
itself offers for the same situation: import this module again.  Doing so
rebinds every name from this module's own namespace and costs nothing.
"""

import sys as _sys

from sage.repl.load import load as _engine_load

from dzack_research.preamble.categories.modules.framed.formed.lattices import Lattices
from dzack_research.preamble.categories.rings.rings import install_session_rings
from dzack_research.preamble.install import install_preamble


def load(filename: str, globals: dict | None = None, attach: bool = False) -> None:
    r"""Run ``filename`` in this session, and keep the session's rings owned.

    Sage's own ``load`` takes the scope to run in as an argument; a session
    types ``load("script.sage")`` and means its own, so the scope defaults to
    the caller's.  ``install_session_rings`` then runs on that same scope,
    which is the whole reason this name is bound here rather than Sage's.
    """
    scope = _sys._getframe(1).f_globals if globals is None else globals
    _engine_load(filename, scope, attach)
    install_session_rings(scope)


# The two calls ``init.sage`` makes, in its order and for its reasons: the
# categories and every exported name first, then the catalogue -- which binds
# the named specimens and, last, the session's ring names.  Reading them off
# this module is what makes ``from ... import *`` deliver them.
install_preamble(globals())
Lattices.install(globals())
