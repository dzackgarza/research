import sys
from pathlib import Path

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.cat import Cat
from category_specs.topological_spaces import (
    MetricSpaceAutCategory,
    MetricSpaceHomCategory,
    MetricSpacesCategory,
    TopologicalSpaceAutCategory,
    TopologicalSpaceHomCategory,
    TopologicalSpaces,
)
from category_specs.topological_spaces.subcategories.compact import _CompactTopologicalSpaces
from category_specs.topological_spaces.subcategories.complete import _CompleteMetricSpaces
from category_specs.topological_spaces.subcategories.connected import _ConnectedTopologicalSpaces
from category_specs.topological_spaces.subcategories.constructions.objects_over import _ObjectsOver
from category_specs.topological_spaces.subcategories.constructions.objects_under import _ObjectsUnder
from category_specs.utils import assert_category_statements


T = TopologicalSpaces()
M = T.Metric()
C = Cat()


class _TopologicalWitness(TopologicalSpaces.ParentMethods):
    pass


class _MetricWitness(MetricSpacesCategory.ParentMethods):
    pass


def abstract_method_has_name(method, name):
    return method.__name__ == name

CATEGORY_STATEMENTS = (
    ("TopologicalSpaces() is an object of Cat()", lambda _: T in C),
    (
        "TopologicalSpaces() records topological axiom ownership over Sets()",
        lambda _: TopologicalSpaces._base_category_class_and_axiom[1] == "Topological",
    ),
    ("TopologicalSpaces() object method surface reports topological objects", lambda _: _TopologicalWitness().is_topological()),
    ("TopologicalSpaces() has no direct Sage supercategory splice", lambda _: T._sage_super_categories() == ()),
    ("TopologicalSpaces().Connected() is an object of Cat()", lambda _: T.Connected() in C),
    ("TopologicalSpaces().Connected() is a subcategory of TopologicalSpaces()", lambda _: T.Connected().is_subcategory(T)),
    (
        "TopologicalSpaces().Connected() records the connected axiom owner",
        lambda _: _ConnectedTopologicalSpaces._base_category_class_and_axiom == (TopologicalSpaces, "Connected"),
    ),
    (
        "TopologicalSpaces().Connected() object method surface reports connected objects",
        lambda _: _ConnectedTopologicalSpaces.ParentMethods().is_connected(),
    ),
    ("TopologicalSpaces().Compact() is an object of Cat()", lambda _: T.Compact() in C),
    ("TopologicalSpaces().Compact() is a subcategory of TopologicalSpaces()", lambda _: T.Compact().is_subcategory(T)),
    (
        "TopologicalSpaces().Compact() records the compact axiom owner",
        lambda _: _CompactTopologicalSpaces._base_category_class_and_axiom == (TopologicalSpaces, "Compact"),
    ),
    (
        "TopologicalSpaces().Compact() object method surface reports compact objects",
        lambda _: _CompactTopologicalSpaces.ParentMethods().is_compact(),
    ),
    ("TopologicalSpaces().Metric() is an object of Cat()", lambda _: M in C),
    ("TopologicalSpaces().Metric() is a subcategory of TopologicalSpaces()", lambda _: M.is_subcategory(T)),
    (
        "TopologicalSpaces().Metric() records the metric axiom owner",
        lambda _: MetricSpacesCategory._base_category_class_and_axiom == (TopologicalSpaces, "Metric"),
    ),
    ("TopologicalSpaces().Metric() object method surface reports metric objects", lambda _: _MetricWitness().is_metric()),
    ("TopologicalSpaces().Metric().Complete() is an object of Cat()", lambda _: M.Complete() in C),
    (
        "TopologicalSpaces().Metric().Complete() is a subcategory of TopologicalSpaces().Metric()",
        lambda _: M.Complete().is_subcategory(M),
    ),
    (
        "TopologicalSpaces().Metric().Complete() records the complete metric axiom owner",
        lambda _: _CompleteMetricSpaces._base_category_class_and_axiom == (MetricSpacesCategory, "Complete"),
    ),
    (
        "TopologicalSpaces().HomCategory() owns continuous-map element predicates",
        lambda _: abstract_method_has_name(TopologicalSpaceHomCategory.ElementMethods.is_continuous, "is_continuous"),
    ),
    (
        "TopologicalSpaces().AutCategory() owns homeomorphism element predicates",
        lambda _: TopologicalSpaceAutCategory.ElementMethods().is_homeomorphism(),
    ),
    (
        "TopologicalSpaces().Metric().HomCategory() owns short-map predicates",
        lambda _: MetricSpaceHomCategory.ElementMethods().is_short(),
    ),
    (
        "TopologicalSpaces().Metric().AutCategory() owns isometry element predicates",
        lambda _: MetricSpaceAutCategory.ElementMethods().is_isometry(),
    ),
    ("TopologicalSpaces().Subobjects() is an object of Cat()", lambda _: T.Subobjects() in C),
    ("TopologicalSpaces().Quotients() is an object of Cat()", lambda _: T.Quotients() in C),
    ("TopologicalSpaces().Subquotients() is an object of Cat()", lambda _: T.Subquotients() in C),
    (
        "TopologicalSpaces().ObjectsOver() owns structure-space surfaces",
        lambda _: abstract_method_has_name(_ObjectsOver.ParentMethods.structure_space, "structure_space"),
    ),
    (
        "TopologicalSpaces().ObjectsUnder() owns structure-space surfaces",
        lambda _: abstract_method_has_name(_ObjectsUnder.ParentMethods.structure_space, "structure_space"),
    ),
)

assert_category_statements(CATEGORY_STATEMENTS)
