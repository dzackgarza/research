import sys
from pathlib import Path

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.cat import Cat
from category_specs.forms import FormedModules
from category_specs.forms.chain import (
    FiniteRankFreeBilinearModulesCategory,
    FiniteRankFreeFormedModulesCategory,
    IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory,
    NondegenerateSymmetricFiniteRankFreeBilinearModulesCategory,
    SymmetricFiniteRankFreeBilinearModulesCategory,
)
from category_specs.forms.subcategories.alternating import AlternatingBilinearModulesCategory
from category_specs.forms.subcategories.bilinear import BilinearModulesCategory as FormsBilinearModulesCategory
from category_specs.forms.subcategories.free_bilinear import FreeBilinearModulesCategory
from category_specs.forms.subcategories.quadratic import QuadraticModulesCategory as FormsQuadraticModulesCategory
from category_specs.forms.subcategories.rational import RationalBilinearModulesCategory
from category_specs.forms.subcategories.symmetric import (
    SymmetricBilinearModulesCategory as FormsSymmetricBilinearModulesCategory,
)
from category_specs.forms.subcategories.torsion_quadratic_modules import (
    TorsionQuadraticModulesCategory as FormsTorsionQuadraticModulesCategory,
)
from category_specs.forms.subcategories.with_forms import FormedModulesCategory as FormsWithFormsCategory
from category_specs.lattices.subcategories.symmetric import (
    SymmetricBilinearModulesCategory as LatticeSymmetricBilinearModulesCategory,
)
from category_specs.modules import Modules
from category_specs.modules.subcategories.bilinear import BilinearModulesCategory as ModuleBilinearModulesCategory
from category_specs.modules.subcategories.quadratic import QuadraticModulesCategory as ModuleQuadraticModulesCategory
from category_specs.modules.subcategories.torsion_quadratic_modules import (
    TorsionQuadraticModulesCategory as ModuleTorsionQuadraticModulesCategory,
)
from category_specs.modules.subcategories.with_forms import FormedModulesCategory as ModuleWithFormsCategory
from category_specs.utils import assert_smoke_statements


MZZ = Modules(ZZ, dispatch=False)
FZZ = FormedModules(ZZ)
LATTICE_AMBIENT = MZZ.Free().FiniteRank().WithForms().Bilinear().Symmetric().Nondegenerate().Integral()


class _AutCategoryWitness:
    def Of(self, parent):
        return ("orthogonal-group", parent)


class _CategoryWitness:
    def AutCategory(self):
        return _AutCategoryWitness()


class _FormedWitness(FiniteRankFreeFormedModulesCategory.ParentMethods):
    def category(self):
        return _CategoryWitness()


class _FormWitness:
    def b(self, v, w):
        return (v, w)


class _BilinearWitness(FiniteRankFreeBilinearModulesCategory.ParentMethods):
    def form(self):
        return _FormWitness()


class _SymmetricWitness(SymmetricFiniteRankFreeBilinearModulesCategory.ParentMethods):
    pass


class _IntegralWitness(IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory.ParentMethods):
    pass


def abstract_method_has_name(method, name):
    return method.__name__ == name


def formed_chain_concrete_methods_route():
    formed = _FormedWitness()
    orthogonal_group = formed.orthogonal_group()
    return (
        formed.has_form()
        and orthogonal_group == ("orthogonal-group", formed)
        and _BilinearWitness().is_bilinear()
        and _BilinearWitness().b("v", "w") == ("v", "w")
        and _SymmetricWitness().is_symmetric()
        and _IntegralWitness().is_integral()
        and _IntegralWitness().is_rational()
    )

SMOKE_STATEMENTS = (
    ("FormedModules(ZZ) is an object of Cat()", lambda _: FZZ in Cat()),
    ("FormedModules(ZZ) is Modules(ZZ).WithForms()", lambda _: FZZ == MZZ.WithForms()),
    ("module WithForms shim resolves to forms owner", lambda _: ModuleWithFormsCategory is FormsWithFormsCategory),
    (
        "module Bilinear shim resolves to forms owner",
        lambda _: ModuleBilinearModulesCategory is FormsBilinearModulesCategory,
    ),
    (
        "module Quadratic shim resolves to forms owner",
        lambda _: ModuleQuadraticModulesCategory is FormsQuadraticModulesCategory,
    ),
    (
        "module TorsionQuadraticModules shim resolves to forms owner",
        lambda _: ModuleTorsionQuadraticModulesCategory is FormsTorsionQuadraticModulesCategory,
    ),
    (
        "torsion quadratic modules inherit Smith invariants from finite-presentation over PID",
        lambda _: MZZ.TorsionQuadraticModules().is_subcategory(MZZ.FinitelyPresented().OverPID()),
    ),
    (
        "lattice symmetric compatibility path resolves to forms owner",
        lambda _: LatticeSymmetricBilinearModulesCategory is FormsSymmetricBilinearModulesCategory,
    ),
    ("FormedModules(ZZ).Bilinear() is below FormedModules(ZZ)", lambda _: FZZ.Bilinear().is_subcategory(FZZ)),
    ("FormedModules(ZZ).Quadratic() is below FormedModules(ZZ)", lambda _: FZZ.Quadratic().is_subcategory(FZZ)),
    (
        "finite-rank lattice ambient chain remains formed-module based",
        lambda _: LATTICE_AMBIENT.is_subcategory(MZZ.Free().FiniteRank().WithForms()),
    ),
    (
        "formed-module chain concrete predicates and forwarding methods route correctly",
        lambda _: formed_chain_concrete_methods_route(),
    ),
    (
        "formed-module chain owns bilinear and quadratic abstract predicates",
        lambda _: abstract_method_has_name(FiniteRankFreeFormedModulesCategory.ParentMethods.is_bilinear, "is_bilinear")
        and abstract_method_has_name(FiniteRankFreeFormedModulesCategory.ParentMethods.is_quadratic, "is_quadratic")
        and abstract_method_has_name(FiniteRankFreeFormedModulesCategory.ParentMethods.form, "form"),
    ),
    (
        "FormedModules(ZZ) routes Hom, End, and Aut through public category objects",
        lambda _: FZZ.HomCategory() in Cat()
        and FZZ.HomCategory().is_subcategory(MZZ.HomCategory())
        and FZZ.EndCategory() in Cat()
        and FZZ.AutCategory() in Cat(),
    ),
    (
        "bilinear formed-module chain owns symmetry and integrality predicates",
        lambda _: abstract_method_has_name(FiniteRankFreeBilinearModulesCategory.ParentMethods.is_symmetric, "is_symmetric")
        and abstract_method_has_name(FiniteRankFreeBilinearModulesCategory.ParentMethods.is_alternating, "is_alternating")
        and abstract_method_has_name(FiniteRankFreeBilinearModulesCategory.ParentMethods.is_integral, "is_integral")
        and abstract_method_has_name(FiniteRankFreeBilinearModulesCategory.ParentMethods.is_rational, "is_rational"),
    ),
    (
        "symmetric formed-module chain owns definiteness and orthogonal-submodule surfaces",
        lambda _: abstract_method_has_name(SymmetricFiniteRankFreeBilinearModulesCategory.ParentMethods.is_definite, "is_definite")
        and abstract_method_has_name(SymmetricFiniteRankFreeBilinearModulesCategory.ParentMethods.is_positive_definite, "is_positive_definite")
        and abstract_method_has_name(SymmetricFiniteRankFreeBilinearModulesCategory.ParentMethods.is_negative_definite, "is_negative_definite")
        and abstract_method_has_name(SymmetricFiniteRankFreeBilinearModulesCategory.ParentMethods.orthogonal_submodule_to, "orthogonal_submodule_to"),
    ),
    (
        "nondegenerate and integral chain owns anisotropy and dual-lattice surfaces",
        lambda _: abstract_method_has_name(NondegenerateSymmetricFiniteRankFreeBilinearModulesCategory.ElementMethods.is_anisotropic, "is_anisotropic")
        and abstract_method_has_name(IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory.ParentMethods.dual_lattice, "dual_lattice"),
    ),
    (
        "forms subcategory surfaces own isotropy, product, rescaling, and divisibility methods",
        lambda _: abstract_method_has_name(AlternatingBilinearModulesCategory.ParentMethods.is_isotropic, "is_isotropic")
        and abstract_method_has_name(FormsBilinearModulesCategory.ElementMethods.inner_product, "inner_product")
        and abstract_method_has_name(FreeBilinearModulesCategory.ParentMethods.tensor_product, "tensor_product")
        and abstract_method_has_name(FreeBilinearModulesCategory.ElementMethods.self_product, "self_product")
        and abstract_method_has_name(RationalBilinearModulesCategory.ParentMethods.integral_rescaling, "integral_rescaling")
        and abstract_method_has_name(FormsSymmetricBilinearModulesCategory.ElementMethods.divisibility, "divisibility"),
    ),
)

assert_smoke_statements(SMOKE_STATEMENTS)
