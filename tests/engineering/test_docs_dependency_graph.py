"""The book's dependency graph, built by scripts/docs_dependency_graph.py on a small book.

The script is run as the post-render step runs it, through `uv run --script`, on a
two-chapter fixture project; the assertions read the node-link JSON and the findings
it writes.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[2] / "scripts" / "docs_dependency_graph.py"

CONFIG = """\
book:
  chapters:
    - one.md
    - part: two.md
      chapters: [three.md]
custom-numbered-blocks:
  classes:
    theorem: {}
    lemma: {}
    definition: {}
"""

LUA = 'local ref_prefixes = { thm = true, lem = true, def = true }\n'

ONE = """\
::: {.definition #def:a title="A"}
An $a$.
:::

::: {.lemma #lem:b}
Every $a$ (@def:a) is a $b$.
:::

::: {.proof}
By [@def:a] and [-@thm:c].
:::

::: {.proof}
Orphan.
:::
"""

TWO = "# Part\n"

THREE = """\
::: {.theorem #thm:c}
By @lem:b, and @thm:missing. Also @sec-elsewhere.
:::

::: {.lemma}
Uses @def:a.
:::
"""


def run(tmp_path: Path) -> tuple[dict, list[dict], int]:
    lua = tmp_path / "_extensions" / "local" / "amsthm-refs"
    lua.mkdir(parents=True)
    (lua / "amsthm-refs.lua").write_text(LUA)
    (tmp_path / "_quarto.yml").write_text(CONFIG)
    for name, text in {"one.md": ONE, "two.md": TWO, "three.md": THREE}.items():
        (tmp_path / name).write_text(text)
    out = tmp_path / "out"
    done = subprocess.run(
        ["uv", "run", "--script", str(SCRIPT), "--project", str(tmp_path), "--out", str(out),
         "--check"],
        capture_output=True, text=True, timeout=300, check=False)
    graph = json.loads((out / "dependency-graph.json").read_text())
    findings = json.loads((out / "dependency-findings.json").read_text())
    return graph, findings, done.returncode


def test_edges_come_from_statement_and_proof_references(tmp_path):
    graph, findings, code = run(tmp_path)
    edges = {(e["source"], e["target"]): e for e in graph["edges"]}
    assert edges[("lem:b", "def:a")]["statement"] and edges[("lem:b", "def:a")]["proof"]
    assert edges[("lem:b", "thm:c")] == {"source": "lem:b", "target": "thm:c",
                                         "statement": False, "proof": True}
    assert ("thm:c", "lem:b") in edges
    nodes = {n["id"]: n for n in graph["nodes"]}
    assert nodes["lem:b"]["proved"] and not nodes["thm:c"]["proved"]
    assert [nodes[i]["position"] for i in ("def:a", "lem:b", "thm:c")] == [0, 1, 2]
    # The unnamed lemma is a node whose reference is still an edge.
    assert ("three.md#3", "def:a") in edges
    assert code == 1


def test_findings_name_each_defect(tmp_path):
    _, findings, _ = run(tmp_path)
    messages = sorted(f["message"] for f in findings)
    assert messages == sorted([
        "#lem:b uses #thm:c, which comes later (in three.md)",
        "#thm:c cites @thm:missing, which no block defines",
        "a lemma block has no id, so nothing can cite it",
        "a proof follows no numbered block",
        next(m for m in messages if m.startswith("cycle: ")),
    ])
    cycle = next(m for m in messages if m.startswith("cycle: "))
    assert set(cycle.removeprefix("cycle: ").split(" -> ")) == {"#lem:b", "#thm:c"}
