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
    remark: {}
"""

LUA = 'local ref_prefixes = { thm = true, lem = true, def = true }\n'

ONE = """\
::: {.definition #def:a title="A"}
An $a$ is a **round apple**; an **apple** is a fruit; $b$ are **round apples**.
:::

::: {.lemma #lem:b}
Every $a$ (@def:a) is a $b$, so round apples are $b$.
:::

::: {.proof}
By [@def:a] and [-@thm:c], by [@Smith20, Theorem 2 and Lem. 4.1] and [@Smith20, Thm. 2].
:::

::: {.proof}
Orphan.
:::
"""

TWO = "# Part\n"

THREE = """\
::: {.theorem #thm:c}
By @lem:b, and @thm:missing, every round apple is $c$. Also @sec-elsewhere; compare @rmk:d.
:::

::: {.lemma}
Uses @def:a.
:::

::: {.remark #rmk:d}
A pointer back to @thm:c, about a round apple [@Jones19, Thm. 1].
:::

::: {.lemma #lem:e}
A round apple is an apple [@Brown18].
:::

::: {.lemma #lem:g}
Every $c$ is $d$.
:::

::: {.proof}
By [@Green21], [@Green21, Ch. 3] and [@stacks-02LS].
:::

::: {.lemma #lem:f}
A [round apple]{.other-sense} of a tree is a crown.
A round $x$ apple is a crown.
:::

::: {.remark #rmk:open}
Its closing fence is on the text line.:::
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
    assert edges[("lem:b", "thm:c")] == {"source": "lem:b", "target": "thm:c", "forward": True,
                                         "relation": "uses",
                                         "statement": False, "proof": True}
    assert ("thm:c", "lem:b") in edges
    # A remark and a theorem that cite each other are commentary, not a cycle.
    assert edges[("thm:c", "rmk:d")]["relation"] == edges[("rmk:d", "thm:c")]["relation"] == "mentions"
    nodes = {n["id"]: n for n in graph["nodes"]}
    assert nodes["lem:b"]["proved"] and not nodes["thm:c"]["proved"]
    assert [nodes[i]["position"] for i in ("def:a", "lem:b", "thm:c")] == [0, 1, 2]
    # The unnamed lemma is a node whose reference is still an edge.
    assert ("three.md#3", "def:a") in edges
    assert code == 1



def test_findings_name_each_defect(tmp_path):
    _, findings, _ = run(tmp_path)
    by_kind = {f["kind"]: f for f in findings}
    assert sorted(f["kind"] for f in findings) == [
        "cycle", "dangling", "missing-id", "orphan-proof", "parse-warning", "uncited-term",
        "unlocated-citation", "unlocated-citation"]
    # lem:e uses the defined phrase and cites nothing. lem:b cites def:a, thm:c reaches it
    # through lem:b, and rmk:d is commentary; the one-word term "apple" is not checked.
    assert by_kind["uncited-term"] == {"kind": "uncited-term", "chapter": "three.md",
                                       "blocks": ["lem:e", "def:a"], "detail": "round apple"}
    assert by_kind["dangling"] == {"kind": "dangling", "chapter": "three.md",
                                   "blocks": ["thm:c", "thm:missing"], "detail": ""}
    assert by_kind["missing-id"]["blocks"] == ["three.md#3"]
    assert by_kind["orphan-proof"]["chapter"] == "one.md"
    # A closing fence on a text line leaves the div open; pandoc warns and the checker reports it.
    assert by_kind["parse-warning"]["chapter"] == "three.md"
    assert "unclosed" in by_kind["parse-warning"]["detail"]
    # lem:f marks its use as another sense, so it is not listed.
    assert [f for f in findings if f["blocks"][:1] == ["lem:f"]] == []
    # The lem:b <-> thm:c circle of uses is reported; the thm:c <-> rmk:d mentions are not.
    assert sorted(by_kind["cycle"]["blocks"]) == ["lem:b", "thm:c"]

def test_cited_results_are_nodes(tmp_path):
    graph, findings, _ = run(tmp_path)
    nodes = {n["id"]: n for n in graph["nodes"]}
    edges = {(e["source"], e["target"]): e for e in graph["edges"]}
    # A citation that names a result is an edge to that result, one node per result.
    # "Theorem 2" and "Thm. 2" are one result; "Theorem 2 and Lem. 4.1" are two.
    assert nodes["Smith20 Thm. 2"]["kind"] == "reference"
    assert nodes["Smith20 Thm. 2"]["work"] == "Smith20"
    assert edges[("lem:b", "Smith20 Thm. 2")]["relation"] == "uses"
    assert edges[("lem:b", "Smith20 Lem. 4.1")]["proof"]
    assert edges[("rmk:d", "Jones19 Thm. 1")]["relation"] == "mentions"
    # A key that names one result, as a Stacks Project tag does, is that result.
    assert edges[("lem:g", "stacks-02LS")]["relation"] == "uses"
    # A whole work, or a chapter of one, is not a result: no node and no edge.
    works = {n["work"] for n in graph["nodes"] if n["kind"] == "reference"}
    assert "Brown18" not in works and "Green21" not in works
    assert not any(t.startswith(("Green21", "Brown18")) for _, t in edges)
    # In a proof such a citation is a premise that cannot be checked, so it is a finding;
    # in a statement it is attribution, and is not.
    unlocated = sorted((f["blocks"], f["detail"]) for f in findings
                       if f["kind"] == "unlocated-citation")
    assert unlocated == [(["lem:g"], "@Green21"), (["lem:g"], "@Green21, Ch. 3")]
