"""Structural queries of scripts/docs_query.py, run as `just book` runs them, on a small book.

The fixture is a two-chapter Quarto project. Each test runs one subcommand through
`uv run --script` and reads its output.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[2] / "scripts" / "docs_query.py"

CONFIG = """\
book:
  chapters: [one.md, two.md]
custom-numbered-blocks:
  classes:
    theorem: {}
    lemma: {}
    definition: {}
    remark: {}
"""

LUA = 'local ref_prefixes = { thm = true, lem = true, def = true }\n'

ONE = """\
# Apples {#sec-apples}

::: {.definition #def:a title="The form $D_{16}$" defines="apple; round fruit"}
An **apple** is a **round fruit**.
:::

## Lemmas

::: {.lemma #lem:b}
Every apple (@def:a) is round [@Smith20, Thm. 2].
:::

::: {.proof}
```
::: not a fence inside code
```
By @def:a.
:::
"""

TWO = """\
# Trees

::: {.theorem #thm:c}
By @lem:b, trees bear apples.
:::

::: {.remark #rmk:d}
Compare @thm:c and [@Smith20, §1].
:::
"""


def query(tmp_path: Path, *args: str, one: str = ONE, two: str = TWO) -> str:
    lua = tmp_path / "_extensions" / "local" / "amsthm-refs"
    lua.mkdir(parents=True, exist_ok=True)
    (lua / "amsthm-refs.lua").write_text(LUA)
    (tmp_path / "_quarto.yml").write_text(CONFIG)
    (tmp_path / "one.md").write_text(one)
    (tmp_path / "two.md").write_text(two)
    done = subprocess.run(
        ["uv", "run", "--quiet", "--script", str(SCRIPT), "--project", str(tmp_path), *args],
        capture_output=True, text=True, timeout=600, check=True, cwd=tmp_path)
    return done.stdout


def test_list_gives_each_block_its_line(tmp_path):
    rows = {r["id"]: r for r in json.loads(query(tmp_path, "list", "--json"))}
    assert rows["def:a"]["location"] == "one.md:3"
    assert rows["def:a"]["defines"] == "apple; round fruit"
    assert rows["thm:c"]["location"] == "two.md:3"
    assert rows["lem:b"]["proved"] and not rows["thm:c"]["proved"]


def test_list_filters_unproved_theorem_like_blocks(tmp_path):
    assert query(tmp_path, "list", "--unproved", "--ids").split() == ["thm:c"]


def test_show_prints_statement_and_proof(tmp_path):
    out = query(tmp_path, "show", "lem:b")
    assert out.startswith("== one.md:9\n::: {.lemma #lem:b}")
    assert out.rstrip().endswith("By @def:a.\n:::")


def test_tree_nests_blocks_under_headings(tmp_path):
    lines = query(tmp_path, "tree", "--blocks", "one").splitlines()
    assert lines == [
        "one.md",
        "  # Apples  {#sec-apples}",
        '    definition def:a  "The form $D_{16}$"',
        "    ## Lemmas",
        "      lemma lem:b",
    ]


def test_where_names_the_enclosing_block_and_part(tmp_path):
    rows = json.loads(query(tmp_path, "where", "def:a", "--json"))
    assert [(r["location"], r["block"], r["part"]) for r in rows] == [
        ("one.md:10", "lem:b", "statement"), ("one.md:17", "lem:b", "proof")]
    rows = json.loads(query(tmp_path, "where", "Smith20", "--json"))
    assert [(r["block"], r["locator"]) for r in rows] == [("lem:b", "Thm. 2"), ("rmk:d", "§1")]


def test_deps_follows_uses_transitively(tmp_path):
    assert query(tmp_path, "deps", "thm:c").splitlines() == [
        "theorem thm:c",
        "  lemma lem:b",
        '    definition def:a  "The form $D_{16}$"',
        "    reference Smith20 Thm. 2",
    ]
    assert "rmk:d" not in query(tmp_path, "deps", "thm:c", "--reverse")
    assert "rmk:d" in query(tmp_path, "deps", "thm:c", "--reverse", "--all")


def test_path_is_a_chain_of_uses(tmp_path):
    rows = json.loads(query(tmp_path, "path", "thm:c", "def:a", "--json"))
    assert [r["id"] for r in rows] == ["thm:c", "lem:b", "def:a"]


def test_catalogue_orders_worker_prerequisites(tmp_path):
    definitions = """
::: {.definition #def:round}
A round apple is an apple (@def:a) of round shape.
:::
"""
    first = TWO.replace("By @lem:b, trees bear apples.", "Trees bear round apples (@def:round).")
    first = first.replace("::: {.remark", "::: {.proof}\nApply @lem:b.\n:::\n\n::: {.remark")

    def catalogue(*args):
        return json.loads(query(tmp_path, "catalogue", "--json", *args, one=first + definitions, two=ONE))

    rows = catalogue()
    ids = [row["id"] for row in rows]
    assert ids.index("def:a") < ids.index("def:round") < ids.index("thm:c")
    assert ids.index("lem:b") < ids.index("thm:c")
    packet = {row["id"]: row for row in catalogue("thm:c")}
    assert set(packet) == {"thm:c", "def:round", "lem:b", "def:a", "Smith20 Thm. 2"}
    assert packet["thm:c"]["uses"] == {"statement": ["def:round"], "proof": ["lem:b"]}
    assert packet["thm:c"]["proof"] == "Apply @lem:b."


def test_catalogue_separates_cycles_from_independent_work(tmp_path):
    chapter = ONE.replace("An **apple**", "Given @lem:b, an **apple**")
    chapter += "\n::: {.definition #def:tree defines=\"tree\"}\nA tree.\n:::\n"
    rows = {r["id"]: r for r in json.loads(query(tmp_path, "catalogue", "--json", one=chapter))}
    cycle = rows["def:a"]["cycle"]
    assert cycle and rows["lem:b"]["cycle"] == cycle
    assert rows["thm:c"]["blocked_by_cycles"] == [cycle]
    assert rows["thm:c"]["cycle"] is None
    assert rows["def:tree"]["layer"] == 0 and rows["def:tree"]["blocked_by_cycles"] == []
    assert rows["rmk:d"]["layer"] is None


def test_proof_needs_its_own_explicit_prerequisite(tmp_path):
    chapter = """
::: {.theorem #thm:c}
Fix a round fruit (@def:a).
:::

::: {.proof}
Every round fruit has the stated property by @lem:b.
:::
"""
    rows = json.loads(query(tmp_path, "catalogue", "thm:c", "--json", two=chapter))
    target = next(row for row in rows if row["id"] == "thm:c")
    assert "def:a" not in target["uses"]["proof"]
    assert any(task["part"] == "proof" and task["term"] == "round fruit"
               for task in target.get("book_tasks", []))
    repaired = chapter.replace("Every round fruit has", "Every round fruit (@def:a) has")
    rows = json.loads(query(tmp_path, "catalogue", "thm:c", "--json", two=repaired))
    target = next(row for row in rows if row["id"] == "thm:c")
    assert "def:a" in target["uses"]["proof"]
    assert not target["book_tasks"]


def test_book_edits_locate_separate_definitions_and_narrative_uses(tmp_path):
    definitions = ONE.replace('apple; round fruit', 'apple; orchard').replace(
        'An **apple** is a **round fruit**.', 'An **apple** is a fruit.\n\nAn **orchard** is a grove.')
    chapter = TWO + '\nAn orchard needs water.\n\nThis orchard (@def:a) has water.\n'
    tasks = json.loads(query(tmp_path, "catalogue", "--book-tasks", "--json", one=definitions, two=chapter))
    assert any(task["block"] == "def:a" and task.get("introductions") == ["apple", "orchard"]
               for task in tasks)
    narrative = [task for task in tasks if task["part"] == "prose"]
    assert [(t["location"], t["passage"], t["candidates"]) for t in narrative] == [
        ("two.md", "An orchard needs water.", ["def:a"])]
