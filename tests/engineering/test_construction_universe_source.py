r"""Source-only constructions audit contracts (execution deferred under DEV-58).

These miniature source trees have no Sage imports at runtime. The auditor
parses their AST instead of importing or executing their classes.
"""

from __future__ import annotations

from dzack_research.utilities.construction_universe import build_manifest, render_html


def _fixture(tmp_path):
    root = tmp_path / "src" / "dzack_research" / "preamble"
    root.mkdir(parents=True)
    (root / "example.py").write_text(
        '''
class Sets(OwnedCategory):
    def super_categories(self):
        return []

class Modules(OwnedCategory):
    def super_categories(self):
        return [Sets()]

class Lattices(OwnedCategory):
    def super_categories(self):
        return [Modules()]

    def an_object(self):
        return Lattices()(0)

    class ParentMethods:
        def extend(self, other, choose):
            if choose:
                return Modules()(other)
            else:
                return Sets()(other)

        def unknown_result(self, x):
            return unregistered_constructor(x)

        def no_result(self):
            pass

class MapsMor(OwnedCategory):
    def super_categories(self):
        return [Sets()]
    ElementMethods = SelectedArrow

class SelectedArrow:
    def domain(self):
        return self._source

    def apply(self, argument):
        return self._value(argument)

class NamedLattices:
    @lazy_class_attribute
    def U(cls):
        return Lattices()(0)

    @lazy_class_attribute
    def H(cls):
        return cls.U
''',
        encoding="utf-8",
    )
    (root / "all.py").write_text(
        "from dzack_research.preamble.example import Lattices, NamedLattices\n",
        encoding="utf-8",
    )
    return root


def test_guards_and_required_arguments_are_distinct_hyperedge_ports(tmp_path):
    report = build_manifest(_fixture(tmp_path))
    rule = next(r for r in report["rules"]
                if r["owner"] == "Lattices" and r["name"] == "extend")
    assert {r["type"] for r in rule["results"]} == {
        "object:Modules", "object:Sets",
    }
    assert any(r["guards"] == ["choose"] for r in rule["results"])
    assert any(r["guards"] == ["not (choose)"] for r in rule["results"])
    inputs = [e for e in report["edges"]
              if e["relation"] == "argument-input"
              and e["target"] == "operation:" + rule["id"]]
    assert {e["label"] for e in inputs} == {"other", "choose"}


def test_inclusions_reach_upwards_and_unknown_returns_stay_unknown(tmp_path):
    report = build_manifest(_fixture(tmp_path))
    edges = {tuple(x) for x in report["inclusions"]}
    assert ("Lattices", "Modules") in edges
    rules = [r for r in report["rules"] if r["owner"] == "Lattices"]
    unknown = next(r for r in rules if r["name"] == "unknown_result")
    assert unknown["result_status"] == "unresolved"
    assert any("unregistered_constructor" in x["expression"]
               for x in unknown["results"])
    assert "object:Lattices" in {x["type"] for x in report["closure"]["types"]}
    assert "object:Modules" in {x["type"] for x in report["closure"]["types"]}
    assert "object:Sets" in {x["type"] for x in report["closure"]["types"]}
    assert ("Modules", "Lattices") not in edges


def test_mor_implementations_and_catalogue_delegation(tmp_path):
    report = build_manifest(_fixture(tmp_path))
    mor = [r["name"] for r in report["rules"]
           if r["owner"] == "MapsMor" and r["slot"] == "morphism"]
    assert {"domain", "apply"} <= set(mor)
    aliases = [r for r in report["rules"]
               if r["slot"] == "catalogue" and r["owner"] == "NamedLattices"]
    assert {r["name"] for r in aliases} == {"U", "H"}
    assert all(any(x["type"] == "object:Lattices" for x in r["results"])
               for r in aliases)


def test_uninterpreted_return_is_not_a_missing_method_or_hidden_success(tmp_path):
    report = build_manifest(_fixture(tmp_path))
    empty = next(r for r in report["rules"]
                 if r["owner"] == "Lattices" and r["name"] == "no_result")
    assert empty["result_status"] == "classified"
    assert empty["results"][0]["kind"] == "none"
    html = render_html(report)
    assert "construction-universe/1" in html
    assert 'type="application/json"' in html
    assert "<!--CONSTRUCTION_UNIVERSE_DATA-->" not in html
    assert report["source_sha256"] == build_manifest(
        tmp_path / "src" / "dzack_research" / "preamble"
    )["source_sha256"]
