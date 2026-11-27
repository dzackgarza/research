import sys
from pathlib import Path

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.cat import Cat
from category_specs.forms import FormedModules
from category_specs.forms.subcategories.bilinear import _BilinearModules as FormsBilinearModules
from category_specs.forms.subcategories.quadratic import _QuadraticModules as FormsQuadraticModules
from category_specs.forms.subcategories.symmetric import _SymmetricBilinearModules as FormsSymmetricBilinearModules
from category_specs.forms.subcategories.torsion_quadratic_modules import (
    _TorsionQuadraticModules as FormsTorsionQuadraticModules,
)
from category_specs.forms.subcategories.with_forms import _WithForms as FormsWithForms
from category_specs.lattices.subcategories.symmetric import _SymmetricBilinearModules as LatticeSymmetricBilinearModules
from category_specs.modules import Modules
from category_specs.modules.subcategories.bilinear import _BilinearModules as ModuleBilinearModules
from category_specs.modules.subcategories.quadratic import _QuadraticModules as ModuleQuadraticModules
from category_specs.modules.subcategories.torsion_quadratic_modules import (
    _TorsionQuadraticModules as ModuleTorsionQuadraticModules,
)
from category_specs.modules.subcategories.with_forms import _WithForms as ModuleWithForms
from category_specs.utils import assert_smoke_statements


MZZ = Modules(ZZ, dispatch=False)
FZZ = FormedModules(ZZ)
LATTICE_AMBIENT = MZZ.Free().FiniteRank().WithForms().Bilinear().Symmetric().Nondegenerate().Integral()

SMOKE_STATEMENTS = (
    ("FormedModules(ZZ) is an object of Cat()", lambda _: FZZ in Cat()),
    ("FormedModules(ZZ) is Modules(ZZ).WithForms()", lambda _: FZZ == MZZ.WithForms()),
    ("module WithForms shim resolves to forms owner", lambda _: ModuleWithForms is FormsWithForms),
    ("module Bilinear shim resolves to forms owner", lambda _: ModuleBilinearModules is FormsBilinearModules),
    ("module Quadratic shim resolves to forms owner", lambda _: ModuleQuadraticModules is FormsQuadraticModules),
    (
        "module TorsionQuadraticModules shim resolves to forms owner",
        lambda _: ModuleTorsionQuadraticModules is FormsTorsionQuadraticModules,
    ),
    (
        "lattice symmetric compatibility path resolves to forms owner",
        lambda _: LatticeSymmetricBilinearModules is FormsSymmetricBilinearModules,
    ),
    ("FormedModules(ZZ).Bilinear() is below FormedModules(ZZ)", lambda _: FZZ.Bilinear().is_subcategory(FZZ)),
    ("FormedModules(ZZ).Quadratic() is below FormedModules(ZZ)", lambda _: FZZ.Quadratic().is_subcategory(FZZ)),
    (
        "finite-rank lattice ambient chain remains formed-module based",
        lambda _: LATTICE_AMBIENT.is_subcategory(MZZ.Free().FiniteRank().WithForms()),
    ),
)

assert_smoke_statements(SMOKE_STATEMENTS)
