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


def query(tmp_path: Path, *args: str) -> str:
    lua = tmp_path / "_extensions" / "local" / "amsthm-refs"
    lua.mkdir(parents=True, exist_ok=True)
    (lua / "amsthm-refs.lua").write_text(LUA)
    (tmp_path / "_quarto.yml").write_text(CONFIG)
    (tmp_path / "one.md").write_text(ONE)
    (tmp_path / "two.md").write_text(TWO)
    done = subprocess.run(
        ["uv", "run", "--quiet", "--script", str(SCRIPT), "--project", str(tmp_path), *args],
        capture_output=True, text=True, timeout=600, check=True, cwd=tmp_path)
    return done.stdout


def test_list_gives_each_block_its_line(tmp_path):
    rows = {r["id"]: r for r in json.loads(query(tmp_path, "list", "--json"))}
    # A title holding braces, as $D_{16}$, does not hide the block's id.
    assert rows["def:a"]["location"] == "one.md:3"
    assert rows["def:a"]["defines"] == "apple; round fruit"
    assert rows["thm:c"]["location"] == "two.md:3"
    assert rows["lem:b"]["proved"] and not rows["thm:c"]["proved"]


def test_list_filters_unproved_theorem_like_blocks(tmp_path):
    assert query(tmp_path, "list", "--unproved", "--ids").split() == ["thm:c"]


def test_show_prints_statement_and_proof(tmp_path):
    out = query(tmp_path, "show", "lem:b")
    # The proof's code fence holds a colon line that closes nothing.
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
    # The remark only mentions thm:c, so it is a user only when mentions are followed.
    assert "rmk:d" not in query(tmp_path, "deps", "thm:c", "--reverse")
    assert "rmk:d" in query(tmp_path, "deps", "thm:c", "--reverse", "--all")


def test_path_is_a_chain_of_uses(tmp_path):
    rows = json.loads(query(tmp_path, "path", "thm:c", "def:a", "--json"))
    assert [r["id"] for r in rows] == ["thm:c", "lem:b", "def:a"]
