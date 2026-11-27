r"""Category obligation examples for the category-of-categories subtree."""

import logging
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import category_specs as category_specs_root
from category_specs.algebras import Algebras
from category_specs.cat import Category, Cat
from category_specs.cat.autsets import _CatAutofunctorMethods
from category_specs.cat.endsets import CatEndCategory, _CatEndofunctorMethods
from category_specs.cat.homsets import CatHomCategory, _CatConstructionFunctorMethods, _CatFunctorMethods
from category_specs.cat.subcategories.constructions.objects_over import SliceCategories
from category_specs.cat.subcategories.constructions.objects_under import CosliceCategories
from category_specs.cat.subcategories.constructions.subobjects import Subcategories
from category_specs.forms import FormedModules
from category_specs.homsets import HomCategory
from category_specs.lattices import Lattices
from category_specs.modules import Modules
from category_specs.posets import Posets
from category_specs.rings import Rings
from category_specs.sets import Sets
from category_specs.topological_spaces import TopologicalSpaces
from category_specs.utils import (
    assert_category_statements,
    category_diagnostic_logger,
    category_diagnostics_enabled,
    clear_category_diagnostic_history,
    disable_category_diagnostics,
    emit_category_diagnostic,
    enable_category_diagnostics,
)
from sage.all import ZZ
from sage.categories.functor import IdentityFunctor


C = Cat()
registered_set_category = Sets()
registered_ring_category = Rings()
registered_poset_category = Posets()
cat_constructors = C.Constructors()
empty_category = cat_constructors.EmptyCategory()
joined_category = Category.join([registered_ring_category, registered_poset_category])


class _ListHandler(logging.Handler):
    def __init__(self, records):
        super().__init__()
        self._records = records

    def emit(self, record):
        self._records.append(record.getMessage())


class _EndofunctorWitness(_CatEndofunctorMethods):
    def __init__(self, domain, codomain):
        self._domain = domain
        self._codomain = codomain

    def domain(self):
        return self._domain

    def codomain(self):
        return self._codomain


class _AutofunctorWitness(_CatAutofunctorMethods):
    pass


def predicate_witness():
    return type(
        "_PredicateWitness",
        (),
        {
            "has_form": lambda self: True,
            "is_bilinear": lambda self: True,
        },
    )()


def category_diagnostics_are_disabled_by_default_and_keyed_once():
    records = []
    logger = category_diagnostic_logger()
    handler = _ListHandler(records)
    logger.addHandler(handler)
    try:
        disable_category_diagnostics()
        clear_category_diagnostic_history()
        emit_category_diagnostic("suppressed", key="cat-obligation")
        assert not records
        assert not category_diagnostics_enabled()

        enable_category_diagnostics()
        emit_category_diagnostic("shown once", key="cat-obligation")
        emit_category_diagnostic("shown twice", key="cat-obligation")
        assert records == ["shown once"]
        assert category_diagnostics_enabled()
    finally:
        disable_category_diagnostics()
        clear_category_diagnostic_history()
        logger.removeHandler(handler)
    return True


def abstract_method_has_name(method, name):
    return method.__name__ == name


CATEGORY_STATEMENTS = (
    ("Cat() is singleton-valued", lambda _: Cat() is C),
    ("Cat() is not an object of itself", lambda _: C not in C),
    (
        "category diagnostics are disabled by default and emit once per key",
        lambda _: category_diagnostics_are_disabled_by_default_and_keyed_once(),
    ),
    ("category_specs root exports Cat module", lambda _: category_specs_root.cat.Cat() is C),
    ("category_specs root exports Sets module", lambda _: category_specs_root.sets.Sets() is registered_set_category),
    ("category_specs root exports Rings module", lambda _: category_specs_root.rings.Rings() is registered_ring_category),
    ("category_specs root exports Posets module", lambda _: category_specs_root.posets.Posets() is registered_poset_category),
    ("category_specs root exports Algebras module", lambda _: category_specs_root.algebras.Algebras(ZZ) in C),
    ("category_specs root exports Forms module", lambda _: category_specs_root.forms.FormedModules(ZZ) is FormedModules(ZZ)),
    ("category_specs root exports Homsets module", lambda _: category_specs_root.homsets.HomCategory is HomCategory),
    ("category_specs root exports Lattices module", lambda _: category_specs_root.lattices.Lattices is Lattices),
    ("category_specs root exports Modules module", lambda _: category_specs_root.modules.Modules(ZZ) is Modules(ZZ)),
    (
        "category_specs root exports TopologicalSpaces module",
        lambda _: category_specs_root.topological_spaces.TopologicalSpaces() is TopologicalSpaces(),
    ),
    ("Sets() reconstructs as its singleton category object", lambda _: Sets() is Sets().__class__()),
    ("Sets().Finite() reconstructs as its axiom category object", lambda _: Sets().Finite() is Sets().Finite().__class__(Sets())),
    ("Modules(ZZ) reconstructs with base ring ZZ", lambda _: Modules(ZZ) is Modules(ZZ).__class__(ZZ)),
    ("Cat().HomCategory() is a category", lambda _: Cat().HomCategory() in C),
    ("EmptyCategory() is an object of Cat()", lambda _: empty_category in C),
    ("Sets() is not an object of EmptyCategory()", lambda _: Sets() not in empty_category),
    ("ZZ is not an object of EmptyCategory()", lambda _: ZZ not in empty_category),
    ("EmptyCategory() is below Sets()", lambda _: empty_category.is_subcategory(Sets())),
    ("EmptyCategory() is below Rings()", lambda _: empty_category.is_subcategory(Rings())),
    ("Sets() is not below EmptyCategory()", lambda _: not Sets().is_subcategory(empty_category)),
    ("Cat().meet([]) is EmptyCategory()", lambda _: C.meet([]) is empty_category),
    (
        "Cat constructor collection invokes EmptyCategory constructor",
        lambda _: cat_constructors.cat_EmptyCategory() is empty_category,
    ),
    (
        "Cat constructor collection invokes set partition constructor",
        lambda _: sorted(map(sorted, cat_constructors.sets_SetPartition([[1, 2], [3]])))
        == [[1, 2], [3]],
    ),
    ("Cat().join([Rings(), Posets()]) is a category", lambda _: C.join([Rings(), Posets()]) in C),
    ("Cat().join([Rings(), Posets()]) is a join category", lambda _: C.join([Rings(), Posets()]) in C.JoinCategories()),
    ("Sets() is not a join category", lambda _: Sets() not in C.JoinCategories()),
    ("Sets().is_join_category() is false", lambda _: not Sets().is_join_category()),
    ("Cat().meet([Rings(), Posets()]) is a category", lambda _: C.meet([Rings(), Posets()]) in C),
    ("Cat().meet([Rings(), Posets()]) is below Rings()", lambda _: C.meet([Rings(), Posets()]).is_subcategory(Rings())),
    ("Cat().meet([Rings(), Posets()]) is below Posets()", lambda _: C.meet([Rings(), Posets()]).is_subcategory(Posets())),
    ("IdentityFunctor(Sets()) is not an object of Cat()", lambda _: IdentityFunctor(Sets()) not in C),
    ("Sage join category is recognized as a Cat join category", lambda _: joined_category in C.JoinCategories()),
    ("joined category HomCategory() is a category", lambda _: joined_category.HomCategory() in C),
    ("Cat().HomCategory().Of(Sets(), Rings()) has domain Sets()", lambda _: C.HomCategory().Of(Sets(), Rings()).domain() is Sets()),
    ("Cat().HomCategory().Of(Sets(), Rings()) has codomain Rings()", lambda _: C.HomCategory().Of(Sets(), Rings()).codomain() is Rings()),
    ("Cat().EndCategory().Of(Sets()) has domain Sets()", lambda _: C.EndCategory().Of(Sets()).domain() is Sets()),
    ("Cat().EndCategory().Of(Sets()) has codomain Sets()", lambda _: C.EndCategory().Of(Sets()).codomain() is Sets()),
    ("Cat().AutCategory().Of(Sets()) has domain Sets()", lambda _: C.AutCategory().Of(Sets()).domain() is Sets()),
    ("Cat().AutCategory().Of(Sets()) has codomain Sets()", lambda _: C.AutCategory().Of(Sets()).codomain() is Sets()),
    ("Sets() is an object of Cat()", lambda _: Sets() in C),
    ("Sets().Finite() is an object of Cat()", lambda _: Sets().Finite() in C),
    ("ZZ is not an object of Cat()", lambda _: ZZ not in C),
    ("Rings() is an object of Cat()", lambda _: Rings() in C),
    ("Modules(ZZ) is an object of Cat()", lambda _: Modules(ZZ) in C),
    ("Algebras(ZZ) is an object of Cat()", lambda _: Algebras(ZZ) in C),
    ("TopologicalSpaces() is an object of Cat()", lambda _: TopologicalSpaces() in C),
    ("Sets().Subobjects() is a category", lambda _: Sets().Subobjects() in C),
    ("Sets().Quotients() is a category", lambda _: Sets().Quotients() in C),
    ("Sets().Subquotients() is a category", lambda _: Sets().Subquotients() in C),
    ("Sets().ObjectsOver(Sets()) is a category", lambda _: Sets().ObjectsOver(Sets()) in C),
    ("Sets().ObjectsUnder(Sets()) is a category", lambda _: Sets().ObjectsUnder(Sets()) in C),
    ("Sets().CartesianProducts() is a category", lambda _: Sets().CartesianProducts() in C),
    ("Sets().HomCategory() is a category", lambda _: Sets().HomCategory() in C),
    ("Sets().EndCategory() is a category", lambda _: Sets().EndCategory() in C),
    ("Sets().AutCategory() is a category", lambda _: Sets().AutCategory() in C),
    ("Sets().Hom(Sets()) has domain Sets()", lambda _: Sets().Hom(Sets()).domain() is Sets()),
    ("Sets().Hom(Sets()) has codomain Sets()", lambda _: Sets().Hom(Sets()).codomain() is Sets()),
    ("Rings().Subobjects() is a category", lambda _: Rings().Subobjects() in C),
    ("Rings().Quotients() is a category", lambda _: Rings().Quotients() in C),
    ("Rings().Subquotients() is a category", lambda _: Rings().Subquotients() in C),
    ("Rings().ObjectsOver(Sets()) is a category", lambda _: Rings().ObjectsOver(Sets()) in C),
    ("Rings().ObjectsUnder(Sets()) is a category", lambda _: Rings().ObjectsUnder(Sets()) in C),
    ("Rings().CartesianProducts() is a category", lambda _: Rings().CartesianProducts() in C),
    ("Rings().HomCategory() is a category", lambda _: Rings().HomCategory() in C),
    ("Rings().EndCategory() is a category", lambda _: Rings().EndCategory() in C),
    ("Rings().AutCategory() is a category", lambda _: Rings().AutCategory() in C),
    ("Rings().Hom(Rings()) has domain Rings()", lambda _: Rings().Hom(Rings()).domain() is Rings()),
    ("Rings().Hom(Rings()) has codomain Rings()", lambda _: Rings().Hom(Rings()).codomain() is Rings()),
    ("Modules(ZZ).Subobjects() is a category", lambda _: Modules(ZZ).Subobjects() in C),
    ("Modules(ZZ).Quotients() is a category", lambda _: Modules(ZZ).Quotients() in C),
    ("Modules(ZZ).Subquotients() is a category", lambda _: Modules(ZZ).Subquotients() in C),
    ("Modules(ZZ).ObjectsOver(Sets()) is a category", lambda _: Modules(ZZ).ObjectsOver(Sets()) in C),
    ("Modules(ZZ).ObjectsUnder(Sets()) is a category", lambda _: Modules(ZZ).ObjectsUnder(Sets()) in C),
    ("Modules(ZZ).CartesianProducts() is a category", lambda _: Modules(ZZ).CartesianProducts() in C),
    ("Modules(ZZ).HomCategory() is a category", lambda _: Modules(ZZ).HomCategory() in C),
    ("Modules(ZZ).EndCategory() is a category", lambda _: Modules(ZZ).EndCategory() in C),
    ("Modules(ZZ).AutCategory() is a category", lambda _: Modules(ZZ).AutCategory() in C),
    ("Modules(ZZ).Hom(Modules(ZZ)) has domain Modules(ZZ)", lambda _: Modules(ZZ).Hom(Modules(ZZ)).domain() is Modules(ZZ)),
    ("Modules(ZZ).Hom(Modules(ZZ)) has codomain Modules(ZZ)", lambda _: Modules(ZZ).Hom(Modules(ZZ)).codomain() is Modules(ZZ)),
    ("Algebras(ZZ).Subobjects() is a category", lambda _: Algebras(ZZ).Subobjects() in C),
    ("Algebras(ZZ).Quotients() is a category", lambda _: Algebras(ZZ).Quotients() in C),
    ("Algebras(ZZ).Subquotients() is a category", lambda _: Algebras(ZZ).Subquotients() in C),
    ("Algebras(ZZ).ObjectsOver(Sets()) is a category", lambda _: Algebras(ZZ).ObjectsOver(Sets()) in C),
    ("Algebras(ZZ).ObjectsUnder(Sets()) is a category", lambda _: Algebras(ZZ).ObjectsUnder(Sets()) in C),
    ("Algebras(ZZ).CartesianProducts() is a category", lambda _: Algebras(ZZ).CartesianProducts() in C),
    ("Algebras(ZZ).HomCategory() is a category", lambda _: Algebras(ZZ).HomCategory() in C),
    ("Algebras(ZZ).EndCategory() is a category", lambda _: Algebras(ZZ).EndCategory() in C),
    ("Algebras(ZZ).AutCategory() is a category", lambda _: Algebras(ZZ).AutCategory() in C),
    ("Algebras(ZZ).Hom(Algebras(ZZ)) has domain Algebras(ZZ)", lambda _: Algebras(ZZ).Hom(Algebras(ZZ)).domain() is Algebras(ZZ)),
    ("Algebras(ZZ).Hom(Algebras(ZZ)) has codomain Algebras(ZZ)", lambda _: Algebras(ZZ).Hom(Algebras(ZZ)).codomain() is Algebras(ZZ)),
    ("TopologicalSpaces().Subobjects() is a category", lambda _: TopologicalSpaces().Subobjects() in C),
    ("TopologicalSpaces().Quotients() is a category", lambda _: TopologicalSpaces().Quotients() in C),
    ("TopologicalSpaces().Subquotients() is a category", lambda _: TopologicalSpaces().Subquotients() in C),
    ("TopologicalSpaces().ObjectsOver(Sets()) is a category", lambda _: TopologicalSpaces().ObjectsOver(Sets()) in C),
    ("TopologicalSpaces().ObjectsUnder(Sets()) is a category", lambda _: TopologicalSpaces().ObjectsUnder(Sets()) in C),
    ("TopologicalSpaces().CartesianProducts() is a category", lambda _: TopologicalSpaces().CartesianProducts() in C),
    ("TopologicalSpaces().HomCategory() is a category", lambda _: TopologicalSpaces().HomCategory() in C),
    ("TopologicalSpaces().EndCategory() is a category", lambda _: TopologicalSpaces().EndCategory() in C),
    ("TopologicalSpaces().AutCategory() is a category", lambda _: TopologicalSpaces().AutCategory() in C),
    (
        "TopologicalSpaces().Hom(TopologicalSpaces()) has domain TopologicalSpaces()",
        lambda _: TopologicalSpaces().Hom(TopologicalSpaces()).domain() is TopologicalSpaces(),
    ),
    (
        "TopologicalSpaces().Hom(TopologicalSpaces()) has codomain TopologicalSpaces()",
        lambda _: TopologicalSpaces().Hom(TopologicalSpaces()).codomain() is TopologicalSpaces(),
    ),
    ("Modules(ZZ).OverPID() is an object of Cat()", lambda _: Modules(ZZ).OverPID() in C),
    ("Modules(ZZ).OverPID() refines Modules(ZZ)", lambda _: Modules(ZZ).OverPID().is_subcategory(Modules(ZZ))),
    ("Modules(ZZ).OverPID().Subobjects() is a category", lambda _: Modules(ZZ).OverPID().Subobjects() in C),
    ("Cat().Subobjects() is a category", lambda _: C.Subobjects() in C),
    ("Sets() is not registered as a Cat subobject", lambda _: Sets() not in C.Subobjects()),
    ("Modules(ZZ).WithForms() is registered as a Cat subobject", lambda _: Modules(ZZ).WithForms() in C.Subobjects()),
    (
        "Modules(ZZ).WithForms() records Modules(ZZ) as ambient category",
        lambda _: Modules(ZZ).WithForms().ambient_category() is Modules(ZZ),
    ),
    (
        "Modules(ZZ).WithForms() exposes has_form as its defining predicate",
        lambda _: Modules(ZZ).WithForms().defining_predicates() == ("has_form",),
    ),
    (
        "Modules(ZZ).WithForms().Bilinear() is registered as a Cat subobject",
        lambda _: Modules(ZZ).WithForms().Bilinear() in C.Subobjects(),
    ),
    (
        "Modules(ZZ).WithForms().Bilinear() exposes is_bilinear as its defining predicate",
        lambda _: Modules(ZZ).WithForms().Bilinear().defining_predicates() == ("is_bilinear",),
    ),
    ("Cat().Quotients() is a category", lambda _: C.Quotients() in C),
    ("Cat().Subquotients() is a category", lambda _: C.Subquotients() in C),
    ("Cat().ObjectsOver(Sets()) is a category", lambda _: C.ObjectsOver(Sets()) in C),
    ("Cat().ObjectsUnder(Sets()) is a category", lambda _: C.ObjectsUnder(Sets()) in C),
    ("Cat().CartesianProducts() is a category", lambda _: C.CartesianProducts() in C),
    ("Cat().HomCategory() is a category", lambda _: C.HomCategory() in C),
    ("Cat().EndCategory() is a category", lambda _: C.EndCategory() in C),
    ("Cat().AutCategory() is a category", lambda _: C.AutCategory() in C),
    ("Cat().Slice(Sets()) is ObjectsOver(Sets())", lambda _: C.Slice(Sets()) is C.ObjectsOver(Sets())),
    ("Cat().Coslice(Sets()) is ObjectsUnder(Sets())", lambda _: C.Coslice(Sets()) is C.ObjectsUnder(Sets())),
    (
        "Cat slice and coslice categories own structure-category surfaces",
        lambda _: abstract_method_has_name(SliceCategories.ParentMethods.structure_category, "structure_category")
        and abstract_method_has_name(CosliceCategories.ParentMethods.structure_category, "structure_category"),
    ),
    ("Cat().Endsets() is EndCategory()", lambda _: C.Endsets() is C.EndCategory()),
    ("Cat().Subobjects() refines the Subcategories construction", lambda _: issubclass(C.Subobjects().__class__, Subcategories)),
    (
        "Cat hom category exposes construction-functor method surface",
        lambda _: CatHomCategory.ConstructionFunctorMethods.__name__ == "_CatConstructionFunctorMethods",
    ),
    (
        "Cat functor surface owns Sage functor coercion and evaluation methods",
        lambda _: abstract_method_has_name(_CatFunctorMethods._coerce_into_domain, "_coerce_into_domain")
        and abstract_method_has_name(_CatFunctorMethods._apply_functor, "_apply_functor")
        and abstract_method_has_name(_CatFunctorMethods._apply_functor_to_morphism, "_apply_functor_to_morphism"),
    ),
    (
        "Cat construction-functor surface owns Sage construction combinators",
        lambda _: _CatConstructionFunctorMethods.coercion_reversed is False
        and abstract_method_has_name(_CatConstructionFunctorMethods.pushout, "pushout")
        and abstract_method_has_name(_CatConstructionFunctorMethods.merge, "merge")
        and abstract_method_has_name(_CatConstructionFunctorMethods.commutes, "commutes")
        and abstract_method_has_name(_CatConstructionFunctorMethods.expand, "expand")
        and abstract_method_has_name(_CatConstructionFunctorMethods.common_base, "common_base"),
    ),
    (
        "Cat end category exposes the Autset axiom hook",
        lambda _: CatEndCategory.Autset(C.EndCategory()).base_category() is C.EndCategory(),
    ),
    (
        "Cat endofunctor predicate detects matching domain and codomain",
        lambda _: _EndofunctorWitness(Sets(), Sets()).is_endofunctor()
        and not _EndofunctorWitness(Sets(), Rings()).is_endofunctor(),
    ),
    ("Cat autofunctor predicate is true by construction", lambda _: _AutofunctorWitness().is_autofunctor()),
    (
        "Modules(ZZ).WithForms() defining predicate accepts has-form witnesses",
        lambda _: Modules(ZZ).WithForms().defining_predicate(predicate_witness()),
    ),
    (
        "Modules(ZZ).WithForms().Bilinear() defining predicate accepts bilinear witnesses",
        lambda _: Modules(ZZ).WithForms().Bilinear().defining_predicate(predicate_witness()),
    ),
)

assert_category_statements(CATEGORY_STATEMENTS)
