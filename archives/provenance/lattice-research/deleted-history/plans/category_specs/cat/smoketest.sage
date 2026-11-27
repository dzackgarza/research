r"""Mathematical smoke surface for the category-of-categories subtree."""

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from category_specs.algebras import Algebras
from category_specs.cat import Category, Cat
from category_specs.modules import Modules
from category_specs.posets import Posets
from category_specs.rings import Rings
from category_specs.sets import Sets
from category_specs.topological_spaces import TopologicalSpaces
from category_specs.utils import assert_smoke_statements
from sage.all import ZZ
from sage.categories.functor import IdentityFunctor


C = Cat()
registered_set_category = Sets()
registered_ring_category = Rings()
registered_poset_category = Posets()
cat_constructors = C.Constructors()
empty_category = cat_constructors.EmptyCategory()
joined_category = Category.join([registered_ring_category, registered_poset_category])

SMOKE_STATEMENTS = (
    ("Cat() is singleton-valued", lambda _: Cat() is C),
    ("Cat() is not an object of itself", lambda _: C not in C),
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
)

assert_smoke_statements(SMOKE_STATEMENTS)
