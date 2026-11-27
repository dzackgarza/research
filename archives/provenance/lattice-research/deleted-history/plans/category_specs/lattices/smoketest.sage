r"""Mathematical smoke surface for the lattice category subtree."""

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from category_specs.cat import Cat
from category_specs.lattices import Lattices
from category_specs.lattices.subcategories.over_integers import _LatticesOverIntegers as LatticesOverIntegers
from category_specs.modules import Modules
from category_specs.utils import assert_smoke_statements
from sage.all import IntegralLattice, ZZ


C = Cat()
MZZ = Modules(ZZ, dispatch=False)
LATTICE_AMBIENT = MZZ.Free().FiniteRank().WithForms().Bilinear().Symmetric().Nondegenerate().Integral()
LZZ = Lattices(ZZ)


def a2_short_vectors_below_three():
    return IntegralLattice("A2").short_vectors(3)


def a2_short_vectors_below_three_up_to_sign():
    return LatticesOverIntegers.ParentMethods.short_vectors_up_to_sign(IntegralLattice("A2"), 3)


SMOKE_STATEMENTS = (
    ("Lattices(ZZ) is an object of Cat()", lambda _: LZZ in C),
    ("Lattices(ZZ) is registered as a Cat subobject", lambda _: LZZ in C.Subobjects()),
    ("Lattices(ZZ) records the explicit lattice chain as ambient category", lambda _: LZZ.ambient_category() is LATTICE_AMBIENT),
    ("Lattices(ZZ) exposes is_lattice as its defining predicate", lambda _: LZZ.defining_predicates() == ("is_lattice",)),
    ("Lattices(ZZ).HomCategory() is an object of Cat()", lambda _: LZZ.HomCategory() in C),
    ("Lattices(ZZ).EndCategory() is an object of Cat()", lambda _: LZZ.EndCategory() in C),
    ("Lattices(ZZ).AutCategory() is an object of Cat()", lambda _: LZZ.AutCategory() in C),
    ("Lattices(ZZ).Subobjects() is an object of Cat()", lambda _: LZZ.Subobjects() in C),
    ("Lattices(ZZ).DualObjects() is an object of Cat()", lambda _: LZZ.DualObjects() in C),
    ("Lattices(ZZ).DualLattices() aliases DualObjects()", lambda _: LZZ.DualLattices() is LZZ.DualObjects()),
    ("Lattices(ZZ).Even() exposes is_even as its defining predicate", lambda _: LZZ.Even().defining_predicates() == ("is_even",)),
    (
        "IntegralLattice('A2').short_vectors(3) has six roots of norm 2",
        lambda _: len(a2_short_vectors_below_three()[2]) == 6,
    ),
    ("Lattices(ZZ).OverIntegers().ParentMethods.short_vectors is admitted", lambda _: LatticesOverIntegers.ParentMethods.short_vectors),
    (
        "IntegralLattice('A2').short_vectors_up_to_sign(3) has three roots modulo sign",
        lambda _: len(a2_short_vectors_below_three_up_to_sign()[2]) == 3,
    ),
)

assert_smoke_statements(SMOKE_STATEMENTS)
