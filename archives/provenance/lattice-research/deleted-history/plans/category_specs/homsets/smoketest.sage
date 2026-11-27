r"""Mathematical smoke surface for the generic hom category subtree."""

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from category_specs.cat import Cat
from category_specs.homsets import AutCategory, EndCategory, HomCategory
from category_specs.modules import Modules
from category_specs.posets import Posets
from category_specs.rings import Rings
from category_specs.sets import Sets
from category_specs.topological_spaces import TopologicalSpaces
from category_specs.utils import assert_smoke_statements
from sage.all import ZZ


C = Cat()

SMOKE_STATEMENTS = (
    ("HomCategory() is a category", lambda _: HomCategory() in C),
    ("EndCategory() is a category", lambda _: EndCategory() in C),
    ("AutCategory() is a category", lambda _: AutCategory() in C),
    ("Cat().HomCategory() is a category", lambda _: C.HomCategory() in C),
    ("Cat().EndCategory() is a category", lambda _: C.EndCategory() in C),
    ("Cat().AutCategory() is a category", lambda _: C.AutCategory() in C),
    ("Cat().EndCategory() is Cat().HomCategory().EndCategory()", lambda _: C.EndCategory() is C.HomCategory().EndCategory()),
    ("Cat().AutCategory() is Cat().EndCategory().AutCategory()", lambda _: C.AutCategory() is C.EndCategory().AutCategory()),
    ("Sets().HomCategory() is a category", lambda _: Sets().HomCategory() in C),
    ("Sets().EndCategory() is a category", lambda _: Sets().EndCategory() in C),
    ("Sets().AutCategory() is a category", lambda _: Sets().AutCategory() in C),
    ("Sets().EndCategory() refines its hom end category", lambda _: Sets().EndCategory().is_subcategory(Sets().HomCategory().EndCategory())),
    (
        "Sets().AutCategory() refines its end aut category",
        lambda _: Sets().AutCategory().is_subcategory(Sets().EndCategory().AutCategory()),
    ),
    ("Rings().HomCategory() is a category", lambda _: Rings().HomCategory() in C),
    ("Rings().EndCategory() is a category", lambda _: Rings().EndCategory() in C),
    ("Rings().AutCategory() is a category", lambda _: Rings().AutCategory() in C),
    ("Rings().HomCategory() refines set hom categories", lambda _: Rings().HomCategory().is_subcategory(Sets().HomCategory())),
    ("Rings().EndCategory() refines set end categories", lambda _: Rings().EndCategory().is_subcategory(Sets().EndCategory())),
    ("Rings().AutCategory() refines set aut categories", lambda _: Rings().AutCategory().is_subcategory(Sets().AutCategory())),
    ("Posets().HomCategory() is a category", lambda _: Posets().HomCategory() in C),
    ("Posets().EndCategory() is a category", lambda _: Posets().EndCategory() in C),
    ("Posets().AutCategory() is a category", lambda _: Posets().AutCategory() in C),
    ("Posets().HomCategory() refines set hom categories", lambda _: Posets().HomCategory().is_subcategory(Sets().HomCategory())),
    ("Posets().EndCategory() refines set end categories", lambda _: Posets().EndCategory().is_subcategory(Sets().EndCategory())),
    ("Posets().AutCategory() refines set aut categories", lambda _: Posets().AutCategory().is_subcategory(Sets().AutCategory())),
    ("TopologicalSpaces().HomCategory() is a category", lambda _: TopologicalSpaces().HomCategory() in C),
    ("TopologicalSpaces().EndCategory() is a category", lambda _: TopologicalSpaces().EndCategory() in C),
    ("TopologicalSpaces().AutCategory() is a category", lambda _: TopologicalSpaces().AutCategory() in C),
    (
        "TopologicalSpaces().HomCategory() refines set hom categories",
        lambda _: TopologicalSpaces().HomCategory().is_subcategory(Sets().HomCategory()),
    ),
    (
        "TopologicalSpaces().EndCategory() refines set end categories",
        lambda _: TopologicalSpaces().EndCategory().is_subcategory(Sets().EndCategory()),
    ),
    (
        "TopologicalSpaces().AutCategory() refines set aut categories",
        lambda _: TopologicalSpaces().AutCategory().is_subcategory(Sets().AutCategory()),
    ),
    ("Modules(ZZ).HomCategory() is a category", lambda _: Modules(ZZ).HomCategory() in C),
    ("Modules(ZZ).EndCategory() is a category", lambda _: Modules(ZZ).EndCategory() in C),
    ("Modules(ZZ).AutCategory() is a category", lambda _: Modules(ZZ).AutCategory() in C),
    ("Modules(ZZ).HomCategory() refines set hom categories", lambda _: Modules(ZZ).HomCategory().is_subcategory(Sets().HomCategory())),
    ("Modules(ZZ).EndCategory() refines set end categories", lambda _: Modules(ZZ).EndCategory().is_subcategory(Sets().EndCategory())),
    ("Modules(ZZ).AutCategory() refines set aut categories", lambda _: Modules(ZZ).AutCategory().is_subcategory(Sets().AutCategory())),
)

assert_smoke_statements(SMOKE_STATEMENTS)
