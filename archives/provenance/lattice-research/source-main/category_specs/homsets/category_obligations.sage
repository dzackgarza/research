r"""Examples verifying Hom/End/Aut category hierarchy obligations."""

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from category_specs.cat import Cat
from category_specs.homsets import AutCategory, EndCategory, HomCategory
from category_specs.homsets.autsets import UniversalAutObjectMethods
from category_specs.homsets.endsets import UniversalEndObjectMethods
from category_specs.homsets.homsets import UniversalHomElementMethods, UniversalHomObjectMethods
from category_specs.modules import Modules
from category_specs.posets import Posets
from category_specs.rings import Rings
from category_specs.sets import Sets
from category_specs.topological_spaces import TopologicalSpaces
from category_specs.utils import assert_category_statements
from sage.all import ZZ
from sage.categories.groups import Groups


C = Cat()
S = Sets()
R = Rings()
P = Posets()


class _HomObjectWitness(UniversalHomObjectMethods):
    def __init__(self, domain, codomain):
        self._domain = domain
        self._codomain = codomain

    def domain(self):
        return self._domain

    def codomain(self):
        return self._codomain

    def natural_map(self):
        return self

    def reversed(self):
        return _HomObjectWitness(self.codomain(), self.domain())

    def __call__(self, data):
        return data


class _EndObjectWitness(UniversalEndObjectMethods):
    def identity(self):
        return self


def aut_object_from_end_category():
    return S.AutCategory().from_end_category(S.EndCategory().Of(ZZ))


BASIC_CATEGORY_EXAMPLES = (
    ("HomCategory() is a category", lambda _: HomCategory() in C),
    ("EndCategory() is a category", lambda _: EndCategory() in C),
    ("AutCategory() is a category", lambda _: AutCategory() in C),
    ("Cat().HomCategory() is a category", lambda _: C.HomCategory() in C),
    ("Cat().EndCategory() is a category", lambda _: C.EndCategory() in C),
    ("Cat().AutCategory() is a category", lambda _: C.AutCategory() in C),
    ("Cat().EndCategory() is Cat().HomCategory().EndCategory()", lambda _: C.EndCategory() is C.HomCategory().EndCategory()),
    ("Cat().AutCategory() is Cat().EndCategory().AutCategory()", lambda _: C.AutCategory() is C.EndCategory().AutCategory()),
    ("AutCategory() is a group category", lambda _: AutCategory().is_subcategory(Groups())),
    ("Sets().HomCategory() is a category", lambda _: S.HomCategory() in C),
    ("Sets().EndCategory() is a category", lambda _: S.EndCategory() in C),
    ("Sets().AutCategory() is a category", lambda _: S.AutCategory() in C),
    ("Rings().HomCategory() is a category", lambda _: R.HomCategory() in C),
    ("Rings().EndCategory() is a category", lambda _: R.EndCategory() in C),
    ("Rings().AutCategory() is a category", lambda _: R.AutCategory() in C),
    ("Posets().HomCategory() is a category", lambda _: P.HomCategory() in C),
    ("Posets().EndCategory() is a category", lambda _: P.EndCategory() in C),
    ("Posets().AutCategory() is a category", lambda _: P.AutCategory() in C),
    ("TopologicalSpaces().HomCategory() is a category", lambda _: TopologicalSpaces().HomCategory() in C),
    ("TopologicalSpaces().EndCategory() is a category", lambda _: TopologicalSpaces().EndCategory() in C),
    ("TopologicalSpaces().AutCategory() is a category", lambda _: TopologicalSpaces().AutCategory() in C),
    ("Modules(ZZ).HomCategory() is a category", lambda _: Modules(ZZ).HomCategory() in C),
    ("Modules(ZZ).EndCategory() is a category", lambda _: Modules(ZZ).EndCategory() in C),
    ("Modules(ZZ).AutCategory() is a category", lambda _: Modules(ZZ).AutCategory() in C),
)

REFINEMENT_EXAMPLES = (
    ("Sets().EndCategory() refines its hom end category", lambda _: S.EndCategory().is_subcategory(S.HomCategory().EndCategory())),
    (
        "Sets().AutCategory() refines its end aut category",
        lambda _: S.AutCategory().is_subcategory(S.EndCategory().AutCategory()),
    ),
    ("Sets().AutCategory() refines Sage group objects", lambda _: S.AutCategory().is_subcategory(Groups())),
    ("Rings().HomCategory() refines set hom categories", lambda _: R.HomCategory().is_subcategory(S.HomCategory())),
    ("Rings().EndCategory() refines set end categories", lambda _: R.EndCategory().is_subcategory(S.EndCategory())),
    ("Rings().AutCategory() refines set aut categories", lambda _: R.AutCategory().is_subcategory(S.AutCategory())),
    ("Posets().HomCategory() refines set hom categories", lambda _: P.HomCategory().is_subcategory(S.HomCategory())),
    ("Posets().EndCategory() refines set end categories", lambda _: P.EndCategory().is_subcategory(S.EndCategory())),
    ("Posets().AutCategory() refines set aut categories", lambda _: P.AutCategory().is_subcategory(S.AutCategory())),
    (
        "TopologicalSpaces().HomCategory() refines set hom categories",
        lambda _: TopologicalSpaces().HomCategory().is_subcategory(S.HomCategory()),
    ),
    (
        "TopologicalSpaces().EndCategory() refines set end categories",
        lambda _: TopologicalSpaces().EndCategory().is_subcategory(S.EndCategory()),
    ),
    (
        "TopologicalSpaces().AutCategory() refines set aut categories",
        lambda _: TopologicalSpaces().AutCategory().is_subcategory(S.AutCategory()),
    ),
    ("Modules(ZZ).HomCategory() refines set hom categories", lambda _: Modules(ZZ).HomCategory().is_subcategory(S.HomCategory())),
    ("Modules(ZZ).EndCategory() refines set end categories", lambda _: Modules(ZZ).EndCategory().is_subcategory(S.EndCategory())),
    ("Modules(ZZ).AutCategory() refines set aut categories", lambda _: Modules(ZZ).AutCategory().is_subcategory(S.AutCategory())),
)

CATEGORY_OBJECT_EXAMPLES = (
    ("generic Hom object detects equal-domain endomorphism sets", lambda _: _HomObjectWitness(S, S).is_endomorphism_set()),
    ("generic Hom object rejects unequal-domain endomorphism sets", lambda _: not _HomObjectWitness(S, R).is_endomorphism_set()),
    (
        "generic Hom element owns extensional equality predicate",
        lambda _: UniversalHomElementMethods.equals_as_function.__name__ == "equals_as_function"
        and UniversalHomElementMethods.is_equal_function.__name__ == "is_equal_function",
    ),
    (
        "generic Hom object owns reversed parent and coercion-map navigation",
        lambda _: UniversalHomObjectMethods.reversed.__name__ == "reversed"
        and UniversalHomObjectMethods.natural_map.__name__ == "natural_map",
    ),
    ("generic End object reports an endomorphism set", lambda _: _EndObjectWitness().is_endomorphism_set()),
    ("generic End object owns identity alias one", lambda _: UniversalEndObjectMethods.one.__name__ == "one"),
    (
        "Sets().AutCategory().from_end_category returns an Aut object",
        lambda _: aut_object_from_end_category() in S.AutCategory(),
    ),
    (
        "generic Aut object records its defining end category",
        lambda _: aut_object_from_end_category().end_category() is S.EndCategory().Of(ZZ),
    ),
    (
        "generic Aut object owns centralizer subgroup construction",
        lambda _: UniversalAutObjectMethods.centralizer.__name__ == "centralizer",
    ),
)

CATEGORY_STATEMENTS = (
    BASIC_CATEGORY_EXAMPLES
    + REFINEMENT_EXAMPLES
    + CATEGORY_OBJECT_EXAMPLES
)

assert_category_statements(CATEGORY_STATEMENTS)
