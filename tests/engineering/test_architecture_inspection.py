"""Exercise the opt-in inspection CLIs without importing the mathematical session."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from dzack_research.utilities.placement import CategoryRecord
from dzack_research.utilities.source_inventory import source_fingerprint


ROOT = Path(__file__).resolve().parents[2]


class ArchitectureInspection(unittest.TestCase):
    def test_source_routes_keep_receiver_and_lexical_owner(self) -> None:
        with tempfile.TemporaryDirectory(dir=ROOT / ".tmp") as directory:
            source = Path(directory) / "subgroups.py"
            source.write_text(
                'class Subgroups:\n'
                '    def subgroup(self, generators):\n'
                '        """Return the subgroup with its inclusion."""\n'
                '        def lift(x):\n'
                '            return x\n'
                '        return self.subsets()(generators)\n'
                '    def inclusion(self):\n'
                '        return self.ambient._inclusion(self)\n'
                'def generated(group, generators):\n'
                '    return group.subgroup(generators)\n'
            )
            result = self.run_tool("refactor_survey", "--root", directory, "--json", "subgroup", "inclusion")
            data = json.loads(result.stdout)
            definitions = {d["owner"]: d for d in data["definitions"]}
            self.assertEqual(definitions["Subgroups.subgroup"]["returns"], ["self.subsets()(generators)"])
            calls = data["call_sites"]
            self.assertTrue(any(c["owner"] == "generated" and c["expression"] == "group.subgroup(generators)" for c in calls))
            access = definitions["Subgroups.inclusion"]["private_accesses"]
            self.assertEqual(access[0]["receiver"], "self.ambient")
            self.assertEqual(access[0]["name"], "_inclusion")
            self.assertEqual(data["files"], [str(source)])

    def test_source_parse_failure_is_visible(self) -> None:
        with tempfile.TemporaryDirectory(dir=ROOT / ".tmp") as directory:
            source = Path(directory) / "broken.py"
            source.write_text("class Broken(\n")
            result = self.run_tool("refactor_survey", "--root", directory, "subgroup", check=False)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("broken.py", result.stderr)

    def test_declared_categories_are_inspectable_without_sage(self) -> None:
        with tempfile.TemporaryDirectory(dir=ROOT / ".tmp") as directory:
            source = Path(directory) / "categories.py"
            source.write_text(
                'class Sets(OwnedCategory):\n'
                '    def super_categories(self):\n'
                '        return []\n'
                'class Subsets(OwnedCategory):\n'
                '    def super_categories(self):\n'
                '        return [Sets()]\n'
                'class Subgroups(OwnedCategory):\n'
                '    def super_categories(self):\n'
                '        return [Subsets()]\n'
            )
            result = self.run_tool("category_graph", directory, "--format", "json")
            rows = {r["name"]: r for r in json.loads(result.stdout)}
            self.assertEqual(rows["Subgroups"]["heads"], ["Subsets"])
            self.assertEqual(rows["Subsets"]["heads"], ["Sets"])
            interval = self.run_tool("category_graph", directory, "--format", "slice", "--between", "Subgroups", "Sets")
            self.assertEqual(json.loads(interval.stdout)["vertices"], ["Sets", "Subgroups", "Subsets"])
            down = self.run_tool("category_graph", directory, "--format", "slice", "--select", "Subsets", "--direction", "down")
            self.assertEqual(json.loads(down.stdout)["vertices"], ["Subgroups", "Subsets"])

    def test_snapshot_slices_and_changes_preserve_method_owners(self) -> None:
        with tempfile.TemporaryDirectory(dir=ROOT / ".tmp") as directory:
            root = Path(directory)
            (root / "source.py").write_text("x = 1\n")
            categories = {
                "Sets": self.category_record("Sets", [], [], []),
                "Groups": self.category_record("Groups", ["Sets"], ["Sets"], ["inclusion"]),
                "FiniteGroups": self.category_record("FiniteGroups", ["Groups"], ["Groups", "Sets"], ["inclusion"]),
                "Modules": self.category_record("Modules", ["Sets"], ["Sets"], ["inclusion"]),
            }
            graph = root / "graph.json"
            graph.write_text(json.dumps({"categories": categories, "source": {"fingerprint": source_fingerprint(root)}}))
            result = self.run_tool("placement", "--graph", str(graph), "--source-root", directory, "--format", "json", "--direction", "down", "Groups")
            self.assertEqual(set(json.loads(result.stdout)["categories"]), {"Groups", "FiniteGroups"})
            self.assertEqual(json.loads(result.stdout)["freshness"], "matches source")
            worksheet = self.run_tool("placement", "--graph", str(graph), "--source-root", directory, "--method", "inclusion", "Groups")
            self.assertIn("`Groups`, `Modules` -- minimal common upper bounds: `Sets`", worksheet.stdout)
            categories["Unprobed"] = self.category_record("Unprobed", [], [], ["inclusion"])
            categories["Unprobed"]["probed_as"] = ""
            graph.write_text(json.dumps({"categories": categories}))
            unprobed = self.run_tool("placement", "--graph", str(graph), "Unprobed")
            self.assertIn("No live instance was observed", unprobed.stdout)
            self.assertNotIn("on `Groups`, `Unprobed`", unprobed.stdout)
            graph.write_text(json.dumps({"categories": categories, "source": {"fingerprint": source_fingerprint(root)}}))
            previous = root / "previous.json"
            previous.write_bytes(graph.read_bytes())
            categories["FiniteGroups"]["operations"]["objects"] = []
            graph.write_text(json.dumps({"categories": categories}))
            delta = self.run_tool("placement", "--graph", str(graph), "--compare", str(previous))
            self.assertIn(["FiniteGroups", "objects", "inclusion", "()"], json.loads(delta.stdout)["removed"])
            graph.write_bytes(previous.read_bytes())
            (root / "source.py").write_text("x = 2\n")
            stale = self.run_tool("placement", "--graph", str(graph), "--source-root", directory, "--format", "json", "Groups")
            self.assertEqual(json.loads(stale.stdout)["freshness"], "stale: source differs from snapshot")

    @staticmethod
    def category_record(name: str, supers: list[str], ancestry: list[str], methods: list[str]) -> CategoryRecord:
        return {
            "display": name, "source": "specimen.py:1", "summary": name, "owned": True,
            "probed_as": name,
            "supers": supers, "ancestry": ancestry,
            "operations": {"objects": [{"name": method, "signature": "()", "summary": "inclusion map", "mark": ""} for method in methods], "elements": [], "morphisms": []},
            "arrow_mor_class": "", "arrow_type": "", "arrow_type_source": "", "arrow_unthreaded": [],
        }

    @staticmethod
    def run_tool(module: str, *arguments: str, check: bool = True) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "-m", f"dzack_research.utilities.{module}", *arguments],
            cwd=ROOT,
            env=os.environ | {"PYTHONPATH": str(ROOT / "src")},
            check=check,
            capture_output=True,
            text=True,
        )


if __name__ == "__main__":
    unittest.main()
