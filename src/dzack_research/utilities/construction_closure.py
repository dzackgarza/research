r"""Symbolic closure of the preamble's declared mathematical constructions.

This is a SOURCE audit, not an execution of Sage or a claim that arbitrary
Python is decidable.  Its unit of enumeration is a *construction scheme*,
not one object per choice of scalar or other infinite parameter.

Run from the repository root::

    PYTHONPATH=src python -m dzack_research.utilities.construction_closure \
        --output .tmp/construction-closure

Outputs are JSON (stable machine-readable facts, including unresolved work),
DOT (typed category/construction hypergraph) and a self-contained searchable
HTML inspector.  No Sage session and no method evaluation are needed.
"""

from __future__ import annotations

import argparse
import ast
import html
import json
from collections import defaultdict, deque
from dataclasses import asdict, dataclass
from pathlib import Path

from dzack_research.utilities.category_graph import (
    _all_edges,
    _container_methods,
    read_tree,
)

# Only category method containers create operations on objects of that
# category.  Class methods are included separately because C(data) itself
# can create a mathematical object.
CONTAINERS = ("ParentMethods", "ElementMethods", "MorphismMethods")
PRIMITIVE = (ast.Constant, ast.List, ast.Tuple, ast.Dict, ast.Set, ast.JoinedStr)
MAX_EXPRESSION_LENGTH = 220


@dataclass(frozen=True)
class Rule:
    id: str
    owner: str
    receiver: str
    method: str
    inputs: tuple[str, ...]
    output: str | None
    expression: str
    conditions: tuple[str, ...]
    location: str
    confidence: str
    status: str


def _source(node: ast.AST) -> str:
    text = ast.unparse(node)
    return text[:MAX_EXPRESSION_LENGTH] + ("..." if len(text) > MAX_EXPRESSION_LENGTH else "")


def _returns(method: ast.FunctionDef | ast.AsyncFunctionDef) -> list[ast.Return]:
    """Returns of the current method, excluding nested function definitions."""
    found: list[ast.Return] = []
    stack = list(method.body)
    while stack:
        node = stack.pop()
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda, ast.ClassDef)):
            continue
        if isinstance(node, ast.Return):
            found.append(node)
        else:
            stack.extend(ast.iter_child_nodes(node))
    return sorted(found, key=lambda node: node.lineno)


def _methods(node: ast.ClassDef, container: str) -> dict[str, ast.FunctionDef]:
    if container == "Category":
        return {
            method.name: method for method in node.body
            if isinstance(method, ast.FunctionDef) and not method.name.startswith("_")
        }
    return _container_methods(node, container)


def _conditions(method: ast.FunctionDef, statement: ast.AST) -> tuple[str, ...]:
    """Conservative syntactic conditions guarding the exact return statement.

    This is source provenance, NOT a claim that the guards are sufficient.
    """
    results: list[str] = []
    def visit(stmts: list[ast.stmt], context: tuple[str, ...]) -> bool:
        for node in stmts:
            if node is statement:
                results.extend(context)
                return True
            if isinstance(node, ast.If):
                if visit(node.body, (*context, _source(node.test))):
                    return True
                if visit(node.orelse, (*context, f"not ({_source(node.test)})")):
                    return True
            elif isinstance(node, (ast.For, ast.While, ast.With, ast.Try, ast.Match)):
                for field, value in ast.iter_fields(node):
                    if isinstance(value, list) and value and all(isinstance(s, ast.stmt) for s in value):
                        if visit(value, (*context, f"inside {type(node).__name__} at {node.lineno}")):
                            return True
                    if field == "cases":
                        for case in value:
                            if visit(case.body, (*context, f"match { _source(case.pattern) }")):
                                return True
        return False
    visit(method.body, ())
    return tuple(results)


def _definitions(method: ast.FunctionDef) -> dict[str, ast.expr]:
    """Use the final local assignment as a clue, never as a proof of dominance."""
    found: dict[str, ast.expr] = {}
    for node in ast.walk(method):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    found[target.id] = node.value
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name) and node.value:
            found[node.target.id] = node.value
    return found


def _category_target(expr: ast.expr, names: set[str]) -> str | None:
    """Find an explicit category application, retaining its symbolic parameters."""
    if isinstance(expr, ast.Call):
        call = expr
        if isinstance(call.func, ast.Call):
            return _category_target(call.func, names)
        if isinstance(call.func, ast.Attribute):
            if call.func.attr == "object":
                return _category_target(call.func.value, names)
            if call.func.attr in {"from_data", "from_module", "from_indexed", "from_predicate", "from_rows"}:
                return _category_target(call.func.value, names)
        head = call.func
        while isinstance(head, ast.Attribute):
            head = head.value
        if isinstance(head, ast.Name) and head.id in names:
            return _source(call)
    return None


def _target(
    expression: ast.expr,
    names: set[str],
    bindings: dict[str, ast.expr],
    local_methods: set[str],
    depth: int = 0,
) -> tuple[str | None, str]:
    """Infer only explicit construction destinations; preserve uncertainty."""
    if depth > 7:
        return None, "depth-limited"
    if isinstance(expression, ast.Name):
        if expression.id == "self":
            return "$receiver", "same-object"
        bound = bindings.get(expression.id)
        return _target(bound, names, bindings, local_methods, depth + 1) if bound is not None else (None, "unresolved-local")
    if isinstance(expression, PRIMITIVE):
        return None, "non-object-or-container"
    if isinstance(expression, ast.Call):
        target = _category_target(expression, names)
        if target is not None:
            return target, "explicit-category"
        fun = expression.func
        if isinstance(fun, ast.Name) and fun.id == "_object_of":
            category = expression.args[0] if expression.args else None
            return (_source(category), "explicit-constructor") if category is not None else (None, "unresolved-constructor")
        if isinstance(fun, ast.Attribute) and fun.attr == "_with_structure":
            return "$receiver plus structure " + _source(expression), "structure-extension"
        if isinstance(fun, ast.Attribute) and isinstance(fun.value, ast.Name) and fun.value.id == "self":
            if fun.attr in local_methods:
                return f"$method:{fun.attr}", "recursive-dispatch"
            # Other methods are inherited or dynamically dispatched; keep a
            # symbolic method-expression rather than guessing a category.
            return f"$dispatch:{fun.attr}", "unresolved-dispatch"
    return None, "unresolved-expression"


def _arguments(method: ast.FunctionDef, container: str) -> tuple[str, ...]:
    """Inputs are symbolic parameter variables, not arbitrary example values."""
    params = [*method.args.posonlyargs, *method.args.args, *method.args.kwonlyargs]
    if params and params[0].arg in {"self", "cls"}:
        params = params[1:]
    results = []
    for param in params:
        anno = _source(param.annotation) if param.annotation is not None else "?"
        results.append(f"{param.arg}:{anno}")
    if method.args.vararg:
        results.append(f"*{method.args.vararg.arg}:variadic")
    if method.args.kwarg:
        results.append(f"**{method.args.kwarg.arg}:keywords")
    return tuple(results)


def inventory(root: Path) -> dict:
    """Read every declared category and all source-level operation returns."""
    declarations = read_tree(root)
    names = {d.name for d in declarations}
    # Preserve parameters and axioms as distinct category schemes; never
    # identify two objects just because their categories share a class.
    declarations_by_location = defaultdict(list)
    for d in declarations:
        declarations_by_location[Path(d.path)].append(d)
    rules: list[Rule] = []
    exceptions: list[dict] = []
    for path, group in sorted(declarations_by_location.items()):
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except (OSError, SyntaxError) as err:
            exceptions.append({"path": str(path), "error": repr(err)})
            continue
        classes = {c.lineno: c for c in ast.walk(tree) if isinstance(c, ast.ClassDef)}
        for declaration in group:
            node = classes.get(declaration.line)
            if node is None:
                exceptions.append({"path": str(path), "error": f"missing class at {declaration.line}"})
                continue
            for container in ("Category", *CONTAINERS):
                methods = _methods(node, container)
                for method_name, method in sorted(methods.items()):
                    bindings = _definitions(method)
                    ret = _returns(method)
                    if not ret:
                        # Nonreturning methods are still included so that
                        # coverage counts them, but they produce no object.
                        rules.append(Rule(
                            f"{declaration.vertex}:{container}.{method_name}@{method.lineno}",
                            declaration.vertex, container, method_name,
                            _arguments(method, container), None, "<no return>",
                            (), f"{path}:{method.lineno}", "none", "no-return",
                        ))
                    for index, statement in enumerate(ret):
                        if statement.value is None:
                            target, evidence = None, "none"
                            expr = "None"
                        else:
                            target, evidence = _target(
                                statement.value, names, bindings, set(methods)
                            )
                            expr = _source(statement.value)
                        conditions = _conditions(method, statement)
                        status = "resolved" if target and not target.startswith("$dispatch:") else (
                            "unresolved" if evidence.startswith("unresolved") or evidence == "depth-limited"
                            else "non-object" if evidence in {"non-object-or-container", "none"} else "symbolic"
                        )
                        rules.append(Rule(
                            f"{declaration.vertex}:{container}.{method_name}@{statement.lineno}:{index}",
                            declaration.vertex, container, method_name,
                            _arguments(method, container), target, expr,
                            conditions, f"{path}:{statement.lineno}", evidence, status,
                        ))

    category_edges = sorted(_all_edges(declarations))
    vertices = sorted(
        set(d.vertex for d in declarations)
        | {v for edge in category_edges for v in edge}
    )
    return {
        "schema": "preamble-construction-closure/v1",
        "basis": "source-only; categorical placement is a claim in the source, not an automatic mathematical proof",
        "categories": [
            {
                "vertex": d.vertex,
                "source": f"{d.path}:{d.line}",
                "bases": list(d.bases),
                "summary": d.summary,
                "axiom_of": d.axiom_of,
                "nested_in": d.nested_in,
            }
            for d in declarations
        ],
        "vertices": vertices,
        "category_edges": [{"from": a, "to": b, "kind": "subcategory-of"} for a, b in category_edges],
        "rules": [asdict(rule) for rule in rules],
        "extraction_errors": exceptions,
    }


def closure(data: dict) -> dict:
    """Compute the least fixed point of candidate *type schemes*.

    Category declarations are available as symbolic seeds, not witnesses of
    inhabited categories. No operation requiring unbound arguments is marked
    as a verified construction: its reachable result is CONDITIONAL. A newly
    derived expression such as ``Modules(R)`` activates every method of
    ``Modules`` and its supercategories, even though it is not literally a
    vertex in the source category graph. This is what makes the closure
    compositional rather than a one-step method-return inventory.

    The finite abstraction is by declared category families and result
    expressions. We do not generate the infinite set of nested object
    *values*, nor claim that a Python condition is decidable statically.
    """
    import re

    vertices = set(data["vertices"])
    ancestor_edges = defaultdict(set)
    for edge in data["category_edges"]:
        ancestor_edges[edge["from"]].add(edge["to"])

    def ancestors(vertex: str) -> set[str]:
        seen = {vertex}
        pending = list(ancestor_edges[vertex])
        while pending:
            item = pending.pop()
            if item not in seen:
                seen.add(item)
                pending.extend(ancestor_edges[item])
        return seen

    def declared_family(expression: str) -> str | None:
        match = re.match(r"^([A-Za-z_]\\w*)", expression)
        return match.group(1) if match else None

    by_owner = defaultdict(list)
    for rule in data["rules"]:
        if rule["output"] is not None:
            by_owner[rule["owner"]].append(rule)

    # A scheme carries symbolic arguments; a source declaration is NOT a
    # constructibility witness. "Candidate" means that some input instance
    # could realize the rule. Conditions remain explicit on each derivation.
    reasons: dict[str, list[dict]] = {
        vertex: [{"kind": "declared-type", "verified-inhabited": False}]
        for vertex in vertices
    }
    work = deque(sorted(vertices))
    family_vertices = defaultdict(set)
    for vertex in vertices:
        family_vertices[declared_family(vertex)].add(vertex)
    unfolded: set[str] = set()

    while work:
        scheme = work.popleft()
        if scheme in unfolded:
            continue
        unfolded.add(scheme)
        family = declared_family(scheme)
        if family not in family_vertices:
            # The output names an unresolved category family. Its absence
            # must be visible, not treated as a proved construction.
            continue
        applicable = {
            owner
            for canonical in family_vertices[family]
            for owner in ancestors(canonical)
        }
        for owner in sorted(applicable):
            for rule in by_owner[owner]:
                target = rule["output"]
                if target == "$receiver":
                    target = scheme
                if not target or target.startswith(("$dispatch:", "$method:")):
                    continue
                required = bool(rule["inputs"]) or bool(rule["conditions"])
                witness = {
                    "kind": "candidate-construction",
                    "operation": rule["id"],
                    "from": scheme,
                    "conditional": required,
                    "inputs": list(rule["inputs"]),
                    "conditions": list(rule["conditions"]),
                }
                if target not in reasons:
                    reasons[target] = [witness]
                    work.append(target)
                elif witness not in reasons[target]:
                    reasons[target].append(witness)

    data["reachable_schemes"] = sorted(reasons)
    data["derivations"] = reasons
    data["unmatched_result_families"] = sorted(
        x for x in reasons
        if (family := declared_family(x)) not in family_vertices
        and x not in vertices
    )
    data["summary"] = {
        "category_vertices": len(vertices),
        "category_edges": len(data["category_edges"]),
        "operations_and_return_branches": len(data["rules"]),
        "resolved_return_branches": sum(r["status"] == "resolved" for r in data["rules"]),
        "unresolved_return_branches": sum(r["status"] == "unresolved" for r in data["rules"]),
        "symbolic_return_branches": sum(r["status"] == "symbolic" for r in data["rules"]),
        "candidate_symbolic_schemes": len(reasons),
        "unmatched_result_families": len(data["unmatched_result_families"]),
    }
    return data


def dot(data: dict) -> str:
    def q(text: str) -> str:
        return json.dumps(text)
    lines = ["digraph Constructions {", "  rankdir=LR;", '  node [fontsize=10];']
    for category in data["vertices"]:
        lines.append(f"  {q('C:'+category)} [label={q(category)},shape=ellipse];")
    for edge in data["category_edges"]:
        lines.append(f"  {q('C:'+edge['from'])} -> {q('C:'+edge['to'])} [color=gray];")
    for i, rule in enumerate(data["rules"]):
        if not rule["output"]:
            continue
        op = "O:" + str(i)
        dest = "C:" + rule["output"]
        lines.append(f"  {q(op)} [label={q(rule['method'])},shape=box];")
        lines.append(f"  {q(dest)} [label={q(rule['output'])}];")
        lines.append(f"  {q('C:'+rule['owner'])} -> {q(op)} [style=dashed];")
        lines.append(f"  {q(op)} -> {q(dest)} [label={q(rule['status'])}];")
    lines.append("}")
    return "\n".join(lines) + "\n"


def inspector(data: dict) -> str:
    """Self-contained browser: searchable category/rule and unresolved views."""
    escaped = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    return '''<!doctype html><html lang="en"><meta charset="utf-8">
<title>Preamble construction closure</title><meta name="viewport" content="width=device-width,initial-scale=1">
<style>body{font:14px system-ui,sans-serif;margin:0;color:#202c36;background:#f5f7fa}
header{background:#14273b;color:white;padding:20px 28px}
main{display:grid;grid-template-columns:minmax(280px,1fr) minmax(380px,2fr);gap:16px;padding:16px}
section{background:white;border:1px solid #d8e0e8;border-radius:8px;padding:16px;min-width:0}
input,select{padding:10px;border:1px solid #afb9c5;border-radius:6px;width:100%;box-sizing:border-box;margin:6px 0}
button{cursor:pointer;padding:8px;border:0;background:transparent;color:#1b527d;text-align:left;width:100%;border-bottom:1px solid #edf0f3}
button:hover,button.selected{background:#ecf2f8}
#items{height:65vh;overflow:auto}#detail{white-space:pre-wrap;overflow-wrap:anywhere;line-height:1.65}
small{color:#64798d}code{background:#eff2f5;padding:2px 4px}h1{margin:0 0 8px}h2{font-size:16px}
@media(max-width:800px){main{grid-template-columns:1fr}#items{height:36vh}}
</style><header><h1>Preamble construction closure</h1><div id="metrics"></div></header>
<main><section><label for="filter">Find category, method, type or source</label>
<input id="filter" placeholder="Search the mathematical universe">
<select id="mode"><option value="categories">Categories</option><option value="rules">Operation and return rules</option>
<option value="unresolved">Unresolved destinations</option><option value="reachable">Reachable symbolic schemes</option></select>
<p id="count"></p><div id="items"></div></section>
<section><h2>Selected construction</h2><div id="detail">Select a category or rule.</div></section></main>
<script type="application/json" id="model">''' + escaped + '''</script>
<script>
const db=JSON.parse(document.getElementById("model").textContent);
const $=id=>document.getElementById(id);
$("metrics").textContent=Object.entries(db.summary).map(([k,v])=>k.replaceAll("_"," ")+": "+v).join(" · ");
function rows(){const mode=$("mode").value;
if(mode==="categories")return db.categories.map(x=>({label:x.vertex,record:x}));
if(mode==="reachable")return db.reachable_schemes.map(x=>({label:x,record:{scheme:x,witnesses:db.derivations[x]}}));
return db.rules.filter(x=>mode!=="unresolved"||x.status==="unresolved")
 .map(x=>({label:x.owner+" · "+x.receiver+"."+x.method+" → "+(x.output||"?"),record:x}));}
function draw(){const needle=$("filter").value.toLowerCase();const matches=rows().filter(x=>JSON.stringify(x).toLowerCase().includes(needle));
$("items").replaceChildren();$("count").textContent=matches.length+" entries";
for(const entry of matches.slice(0,5000)){const button=document.createElement("button");
button.textContent=entry.label;button.onclick=()=>{$("detail").textContent=JSON.stringify(entry.record,null,2);
document.querySelectorAll(".selected").forEach(x=>x.classList.remove("selected"));button.classList.add("selected");};
$("items").append(button);}}
$("filter").oninput=draw;$("mode").onchange=draw;draw();
</script></html>'''


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1] / "preamble")
    parser.add_argument("--output", type=Path, default=Path(".tmp/construction-closure"))
    args = parser.parse_args(argv)
    args.output.mkdir(parents=True, exist_ok=True)
    data = closure(inventory(args.root))
    (args.output / "universe.json").write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")
    (args.output / "universe.dot").write_text(dot(data), encoding="utf-8")
    (args.output / "index.html").write_text(inspector(data), encoding="utf-8")
    print(json.dumps(data["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
