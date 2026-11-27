import sys
from pathlib import Path

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.cat import Cat
from category_specs.topological_spaces import TopologicalSpaces
from category_specs.utils import assert_smoke_statements


T = TopologicalSpaces()

SMOKE_STATEMENTS = (
    ("TopologicalSpaces() is an object of Cat()", lambda _: T in Cat()),
    ("TopologicalSpaces().Connected() is an object of Cat()", lambda _: T.Connected() in Cat()),
    ("TopologicalSpaces().Connected() is a subcategory of TopologicalSpaces()", lambda _: T.Connected().is_subcategory(T)),
    ("TopologicalSpaces().Compact() is an object of Cat()", lambda _: T.Compact() in Cat()),
    ("TopologicalSpaces().Compact() is a subcategory of TopologicalSpaces()", lambda _: T.Compact().is_subcategory(T)),
    ("TopologicalSpaces().Metric() is an object of Cat()", lambda _: T.Metric() in Cat()),
    ("TopologicalSpaces().Metric() is a subcategory of TopologicalSpaces()", lambda _: T.Metric().is_subcategory(T)),
    ("TopologicalSpaces().Metric().Complete() is an object of Cat()", lambda _: T.Metric().Complete() in Cat()),
    (
        "TopologicalSpaces().Metric().Complete() is a subcategory of TopologicalSpaces().Metric()",
        lambda _: T.Metric().Complete().is_subcategory(T.Metric()),
    ),
    ("TopologicalSpaces().Subobjects() is an object of Cat()", lambda _: T.Subobjects() in Cat()),
    ("TopologicalSpaces().Quotients() is an object of Cat()", lambda _: T.Quotients() in Cat()),
    ("TopologicalSpaces().Subquotients() is an object of Cat()", lambda _: T.Subquotients() in Cat()),
)

assert_smoke_statements(SMOKE_STATEMENTS)
