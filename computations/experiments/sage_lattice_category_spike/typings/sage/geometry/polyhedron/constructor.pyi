# Repo-scoped stubs; see lexicon/README.md. Polyhedron here is honestly the
# CONSTRUCTOR (a factory function); the class of its values is
# sage.geometry.polyhedron.base.Polyhedron_base (lexicon noun:
# geometry.Polyhedron). Annotating returns with this function is a defect
# (INVENTORY.md II.4).
from typing import Any

from sage.geometry.polyhedron.base import Polyhedron_base

def Polyhedron(*args: Any, **kwds: Any) -> Polyhedron_base: ...
