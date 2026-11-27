r"""Category obligation examples for the named lattice axiom chain."""

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from category_specs.cat import Cat
from category_specs.lattices import Lattices
from category_specs.modules import Modules
from category_specs.utils import assert_category_statements
from sage.all import ZZ


C = Cat()
MZZ = Modules(ZZ, dispatch=False)
LATTICE_AMBIENT = MZZ.Free().FiniteRank().WithForms().Bilinear().Symmetric().Nondegenerate().Integral()
LZZ = Lattices(ZZ)

CATEGORY_STATEMENTS = (
    ("Lattices(ZZ) is an object of Cat()", lambda _: LZZ in C),
    ("Lattices(ZZ) is registered as a Cat subobject", lambda _: LZZ in C.Subobjects()),
    ("Lattices(ZZ) records the explicit lattice chain as ambient category", lambda _: LZZ.ambient_category() is LATTICE_AMBIENT),
    ("Lattices(ZZ) exposes is_lattice as its defining predicate", lambda _: LZZ.defining_predicates() == ("is_lattice",)),
    ("Lattices(ZZ).Subobjects() is an object of Cat()", lambda _: LZZ.Subobjects() in C),
    ("Lattices(ZZ).Even() exposes is_even as its defining predicate", lambda _: LZZ.Even().defining_predicates() == ("is_even",)),
)

assert_category_statements(CATEGORY_STATEMENTS)
