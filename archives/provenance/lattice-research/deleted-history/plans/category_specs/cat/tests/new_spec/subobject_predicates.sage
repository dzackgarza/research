r"""Spec smoke for predicate-defined subcategories as Cat-subobjects."""

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from category_specs.cat import Cat
from category_specs.lattices import Lattices
from category_specs.modules import Modules
from category_specs.utils import assert_smoke_statements
from sage.all import ZZ


C = Cat()
M = Modules(ZZ, dispatch=False)
LATTICE_AMBIENT = M.Free().FiniteRank().WithForms().Bilinear().Symmetric().Nondegenerate().Integral()
L = Lattices(ZZ)

SMOKE_STATEMENTS = (
    ("Modules(ZZ) is not registered as a Cat subobject", lambda _: M not in C.Subobjects()),
    ("Modules(ZZ).WithForms() is registered as a Cat subobject", lambda _: M.WithForms() in C.Subobjects()),
    ("Modules(ZZ).WithForms() records Modules(ZZ) as ambient category", lambda _: M.WithForms().ambient_category() is M),
    ("Modules(ZZ).WithForms() is defined by has_form", lambda _: M.WithForms().defining_predicates() == ("has_form",)),
    (
        "Modules(ZZ).WithForms().Bilinear() is registered as a Cat subobject",
        lambda _: M.WithForms().Bilinear() in C.Subobjects(),
    ),
    (
        "Modules(ZZ).WithForms().Bilinear() is defined by is_bilinear",
        lambda _: M.WithForms().Bilinear().defining_predicates() == ("is_bilinear",),
    ),
    ("Lattices(ZZ) is registered as a Cat subobject", lambda _: L in C.Subobjects()),
    ("Lattices(ZZ) records the explicit lattice chain as ambient category", lambda _: L.ambient_category() is LATTICE_AMBIENT),
    ("Lattices(ZZ) is defined by is_lattice", lambda _: L.defining_predicates() == ("is_lattice",)),
)

assert_smoke_statements(SMOKE_STATEMENTS)
