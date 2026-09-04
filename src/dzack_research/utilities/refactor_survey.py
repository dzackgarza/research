r"""Survey a named operation before changing what it returns.

`CONTRIBUTING.md` requires two checks before a return type or a name is
touched, and both are mechanical:

- `LEX-11` -- count the definitions of a name and compare their codomains.
  Definitions that answer in different places are different operations, and a
  change applied across the name would corrupt the odd one out.  Reported here
  as a divergence warning over the arity of each definition's returned tuple
  displays.

- `DEF-07` -- an operation's codomain is the union over its implementations,
  not the case in front of you.  The per-definition return expressions are
  printed so the union is visible.

The call-site census is the plan for the change itself.  A return that becomes
an element of a product (`CON-15`) leaves unpacking sites working, turns
indexing into a projection, and requires every comparison against a display to
be restated -- so the counts per shape are the size of the work.

    python3 -m dzack_research.utilities.refactor_survey signature_pair
    python3 -m dzack_research.utilities.refactor_survey --json tensor_valence tensor_shape

Static analysis only: nothing is imported, so it runs against a tree that does
not currently load.
"""

from __future__ import annotations

import argparse
import ast
import json
import pathlib
import sys
from collections import Counter
from dataclasses import dataclass, field, asdict

DEFAULT_ROOTS = ("src", "tests")


@dataclass
class Definition:
    path: str
    line: int
    owner: str
    returns: list[str] = field(default_factory=list)
    tuple_arities: list[int] = field(default_factory=list)


@dataclass
class CallSite:
    path: str
    line: int
    shape: str
    source: str


def _owner_chain(stack: list[str]) -> str:
    return " > ".join(stack) if stack else "<module>"


def _classify(parent: ast.AST | None) -> str:
    match parent:
        case ast.Compare():
            return "compared"
        case ast.Subscript():
            return "indexed"
        case ast.Assign(targets=[ast.Tuple() | ast.List(), *_]):
            return "unpacked"
        case ast.Assign():
            return "bound"
        case ast.Return():
            return "returned"
        case ast.Call():
            return "argument"
        case ast.For():
            return "iterated"
        case None:
            return "other"
        case _:
            return "other"


def _visit(tree: ast.Module, source: str, path: str, names: set[str],
           definitions: dict[str, list[Definition]], calls: dict[str, list[CallSite]]) -> None:
    parents: dict[ast.AST, ast.AST] = {}
    for node in ast.walk(tree):
        for child in ast.iter_child_nodes(node):
            parents[child] = node

    def walk(node: ast.AST, stack: list[str]) -> None:
        for child in ast.iter_child_nodes(node):
            match child:
                case ast.ClassDef(name=name):
                    walk(child, stack + [name])
                case ast.FunctionDef(name=name) | ast.AsyncFunctionDef(name=name) if name in names:
                    record = Definition(path, child.lineno, _owner_chain(stack))
                    for inner in ast.walk(child):
                        if isinstance(inner, ast.Return) and inner.value is not None:
                            record.returns.append(ast.unparse(inner.value))
                            if isinstance(inner.value, ast.Tuple):
                                record.tuple_arities.append(len(inner.value.elts))
                    definitions[name].append(record)
                    walk(child, stack + [name + "()"])
                case ast.FunctionDef(name=name) | ast.AsyncFunctionDef(name=name):
                    walk(child, stack + [name + "()"])
                case _:
                    walk(child, stack)

    walk(tree, [])

    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr in names:
            line = source.splitlines()[node.lineno - 1].strip()
            calls[node.func.attr].append(
                CallSite(path, node.lineno, _classify(parents.get(node)), line[:100])
            )


def survey(names: list[str], roots: list[str]) -> dict:
    definitions: dict[str, list[Definition]] = {n: [] for n in names}
    calls: dict[str, list[CallSite]] = {n: [] for n in names}
    wanted = set(names)
    for root in roots:
        for path in sorted(pathlib.Path(root).rglob("*.py")):
            text = path.read_text()
            if not any(n in text for n in wanted):
                continue
            try:
                tree = ast.parse(text)
            except SyntaxError:
                continue
            _visit(tree, text, str(path), wanted, definitions, calls)
    return {
        name: {
            "definitions": [asdict(d) for d in definitions[name]],
            "call_sites": [asdict(c) for c in calls[name]],
            "shapes": dict(Counter(c.shape for c in calls[name]).most_common()),
            "codomain_divergence": sorted({a for d in definitions[name] for a in d.tuple_arities}),
        }
        for name in names
    }


def _report(result: dict) -> int:
    divergent = 0
    for name, data in result.items():
        defs, sites = data["definitions"], data["call_sites"]
        print(f"\n{name}: {len(defs)} definitions, {len(sites)} call sites")
        arities = data["codomain_divergence"]
        if len(arities) > 1:
            divergent += 1
            print(f"  LEX-11: returned tuple arities differ across definitions: {arities}")
            print("          a definition answering in a different place is a different")
            print("          operation and needs its own name; do not change them together.")
        for d in defs:
            shown = d["returns"][0] if d["returns"] else "(no return)"
            extra = f" (+{len(d['returns']) - 1} more)" if len(d["returns"]) > 1 else ""
            print(f"    {d['path']}:{d['line']}  {d['owner']}")
            print(f"        returns {shown}{extra}")
        if sites:
            print("  call sites by shape (DEF-07/CON-15: this is the plan):")
            for shape, count in data["shapes"].items():
                note = {
                    "unpacked": "keeps working if the return unpacks",
                    "indexed": "becomes a projection",
                    "compared": "restate as owned equality",
                }.get(shape, "inspect")
                print(f"    {count:5d}  {shape:10s} {note}")
    return 1 if divergent else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("names", nargs="+", help="operation names to survey")
    parser.add_argument("--root", action="append", dest="roots", default=None,
                        help=f"tree to scan; repeatable (default: {' '.join(DEFAULT_ROOTS)})")
    parser.add_argument("--json", action="store_true", help="emit the survey as JSON")
    args = parser.parse_args(argv)
    result = survey(args.names, args.roots or list(DEFAULT_ROOTS))
    if args.json:
        print(json.dumps(result, indent=2))
        return 0
    return _report(result)


if __name__ == "__main__":
    sys.exit(main())
