r"""Source-only contract tests for the construction-closure audit.

No Sage objects, preamble import, or mathematical execution are needed.
"""

import ast
import json
import tempfile
import unittest
from pathlib import Path

from dzack_research.utilities.construction_closure import (
    _conditions,
    _target,
    closure,
    dot,
    inspector,
    inventory,
)


class ConstructionClosureTests(unittest.TestCase):
    def test_return_branches_and_guards_are_kept(self):
        root = ast.parse("""
def build(self, n):
    if n:
        return Other(n)
    return self
""").body[0]
        branches = [statement for statement in ast.walk(root)
                    if isinstance(statement, ast.Return)]
        guarded = next(x for x in branches if isinstance(x.value, ast.Call))
        self.assertIn("n", _conditions(root, guarded))
        self.assertEqual(
            _target(guarded.value, {"Other"}, {}, set()),
            ("Other(n)", "explicit-category"),
        )
        unchanged = next(x for x in branches if isinstance(x.value, ast.Name))
        self.assertEqual(
            _target(unchanged.value, set(), {}, set()),
            ("$receiver", "same-object"),
        )

    def test_declared_category_graph_and_compositional_rules(self):
        source = """
class Base(OwnedCategory):
    def super_categories(self):
        return []
    class ParentMethods:
        def create(self, parameter: int):
            return Child()(parameter)
        def unresolved(self):
            return opaque_third_party_call()

class Child(Base):
    def super_categories(self):
        return [Base()]
    class ParentMethods:
        def special(self):
            return Result()(0)
        def via(self):
            return self.special()

class Result(OwnedCategory):
    def super_categories(self):
        return [Base()]
    class ParentMethods:
        def clone(self):
            return self
"""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "fixture.py").write_text(source, encoding="utf-8")
            model = closure(inventory(root))

        self.assertIn("Base", model["vertices"])
        self.assertIn("Child", model["vertices"])
        self.assertIn("Result", model["vertices"])
        self.assertIn(
            {"from": "Child", "to": "Base", "kind": "subcategory-of"},
            model["category_edges"],
        )
        rules = model["rules"]
        build = next(x for x in rules if x["method"] == "create"
                     and x["receiver"] == "ParentMethods")
        self.assertEqual(build["output"], "Child()")
        self.assertEqual(build["inputs"], ("parameter:int",))
        candidate = model["derivations"]["Child()"]
        self.assertTrue(any(x.get("operation") == build["id"]
                            and x["conditional"] for x in candidate))
        # The result family Child has its own method and also inherits the
        # Base operations. A result must be expandable beyond the first hop.
        self.assertTrue(
            any(r.get("from") == "Child()" and "special" in r.get("operation", "")
                for r in model["derivations"]["Result()"])
        )
        self.assertTrue(
            any(r.get("from") == "Child()" and "via" in r.get("operation", "")
                and len(r.get("call_chain", [])) == 2
                for r in model["derivations"]["Result()"])
        )
        unresolved = next(x for x in rules if x["method"] == "unresolved")
        self.assertEqual(unresolved["status"], "unresolved")
        self.assertNotIn("opaque_third_party_call()", model["reachable_schemes"])
        self.assertIn("digraph Constructions", dot(model))
        page = inspector(model)
        self.assertIn("Preamble construction closure", page)
        self.assertIn("application/json", page)
        json.dumps(model)

    def test_category_values_are_not_misplaced_as_category_objects(self):
        expr = ast.parse("Result()", mode="eval").body
        self.assertEqual(_target(expr, {"Result"}, {}, set()),
                         ("Cat(Result())", "category-value"))

    def test_unknown_results_never_become_verified_objects(self):
        model = {
            "vertices": ["A"],
            "category_edges": [],
            "rules": [{
                "id": "A:ParentMethods.new@1",
                "owner": "A",
                "receiver": "ParentMethods",
                "method": "new",
                "inputs": ["argument:?"],
                "output": "Undeclared(argument)",
                "conditions": ["condition(argument)"],
                "status": "resolved",
            }],
            "categories": [],
            "extraction_errors": [],
        }
        result = closure(model)
        witness = result["derivations"]["Undeclared(argument)"][0]
        self.assertTrue(witness["conditional"])
        self.assertIn("Undeclared(argument)", result["unmatched_result_families"])
        self.assertEqual(result["derivations"]["A"][0]["kind"], "declared-type")


if __name__ == "__main__":
    unittest.main()
