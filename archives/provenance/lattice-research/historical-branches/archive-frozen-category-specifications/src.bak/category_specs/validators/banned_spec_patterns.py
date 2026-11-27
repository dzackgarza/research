#!/usr/bin/env python3
"""Report category-spec patterns that hide mathematical mistakes."""

from __future__ import annotations

import ast
import re
import subprocess
import sys
from collections import Counter
from collections.abc import Callable, Iterable
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Rule:
    name: str
    pattern: re.Pattern[str]
    message: str
    action: str
    hard_fail: bool = False


@dataclass(frozen=True)
class Finding:
    path: str
    line_number: int
    rule: Rule
    line: str
    staged: bool

    @property
    def location(self) -> str:
        return f"{self.path}:{self.line_number}"


RULES = (
    Rule(
        name="typing-cast-call",
        pattern=re.compile(r"\bcast\s*\("),
        message=("category_specs spec code must not use typing.cast; fix the owner/type surface instead"),
        action=("Replace with a real annotation, protocol, public semantic type, or category/plugin model change; do not silence the checker."),
    ),
    Rule(
        name="typing-cast-import",
        pattern=re.compile(r"\bimport\b.*\bcast\b"),
        message="category_specs spec code must not import typing.cast",
        action=("Remove the import after replacing all casts in the file with source-grounded types or framework fixes."),
    ),
    Rule(
        name="with-axiom-helper-on-self",
        pattern=re.compile(r"\bwith_axiom\s*\(\s*self\s*,\s*['\"]"),
        message=("axiom SubcategoryMethods must use Sage's self._with_axiom(...) binding idiom"),
        action=('Use self._with_axiom("A") and verify the corresponding class is bound on the base named by _base_category_class_and_axiom.'),
    ),
    Rule(
        name="cached-method-import",
        pattern=re.compile(r"from\s+sage\.misc\.cachefunc\s+import\s+cached_method"),
        message=("category_specs spec code must not import cached_method without a source-grounded Sage runtime need"),
        action=(
            "Remove cached_method plumbing from mathematical spec selectors unless "
            "the file records a Sage category identity/cache obligation; plain "
            "selectors should state the category operation directly."
        ),
    ),
    Rule(
        name="cached-method-adapter",
        pattern=re.compile(r"\bdef\s+_\w*cached_method\b|_\w*cached_method\s*=\s*cast\s*\("),
        message=("local cached_method adapters are engineering wrappers, not mathematical spec content"),
        action=(
            "Delete local cached_method adapters; if caching is required by Sage "
            "runtime semantics, centralize and document that interop boundary "
            "instead of scattering wrapper aliases through spec files."
        ),
    ),
    Rule(
        name="cached-method-decorator",
        pattern=re.compile(r"^\s*@\w*cached_method\b"),
        message=("cached_method decorators in category specs are suspect runtime plumbing and must be justified"),
        action=(
            "Remove the decorator unless the selector's cached category identity is "
            "a documented Sage interop requirement; do not add cached_method to "
            "quiet typing or imitate prior agent output."
        ),
    ),
    Rule(
        name="attribute-rebinding-call",
        pattern=re.compile(r"\b(?:setattr|delattr)\s*\(|__setattr__\s*\("),
        message=("category_specs spec code must not mutate attributes to install, replace, or temporarily inject category behavior"),
        action=(
            "Replace attribute rebinding with explicit category-owned surfaces. "
            "Constructor routes belong on Cat().Constructors(); method/provider "
            "relations belong in the category graph or a source-grounded interop "
            "boundary, not in ambient mutation."
        ),
        hard_fail=True,
    ),
    Rule(
        name="ambient-attribute-assignment",
        pattern=re.compile(r"^\s*(?!self\.)(?:\w+_module|sage_all|category|cls)\.[A-Za-z_]\w*\s*="),
        message=("category_specs spec code must not publish mathematical behavior by direct assignment to module, category, or class attributes"),
        action=(
            "Expose the constructor or method on the owning category class. "
            "Direct ambient assignment is a monkeypatch-shaped substitute for "
            "category graph or constructor-surface ownership."
        ),
        hard_fail=True,
    ),
    Rule(
        name="dynamic-namespace-mutation",
        pattern=re.compile(r"\b(?:globals|locals)\s*\(\s*\)\s*\[|\bvars\s*\([^)]*\)\s*\["),
        message=("category_specs spec code must not mutate dynamic namespaces to publish or redirect mathematical surfaces"),
        action=(
            "Declare the public surface on the mathematical owner directly. "
            "If a dynamic namespace bridge is truly unavoidable, move it out "
            "of spec code into an explicit interop boundary with source-grounded "
            "justification before relaxing this QC rule."
        ),
        hard_fail=True,
    ),
    Rule(
        name="multi-category-refinement",
        pattern=re.compile(r"a^"),
        message=("category_specs spec code must refine to the smallest correct category, not manually list several categories"),
        action=(
            "Replace refine_category(X, [A, B, ...]) with refinement to the "
            "single mathematically minimal category. The category hierarchy owns "
            "supercategory closure; manually stacking categories violates the "
            "purpose of having a category hierarchy."
        ),
        hard_fail=True,
    ),
    Rule(
        name="constructor-cast-call",
        pattern=re.compile(r"a^"),
        message=("category constructor collectors must not use typing.cast to assert category membership or constructor result type"),
        action=(
            "Return the Sage-constructed object through refine_category to the "
            "single source-grounded target category. If the type checker cannot "
            "see the result, fix the constructor surface or static model instead "
            "of casting inside the constructor collector."
        ),
        hard_fail=True,
    ),
)

SPEC_PATH_PREFIX = "category_specs/"
EXCLUDED_PREFIXES = ("category_specs/validators/",)
ATTRIBUTE_REBINDING_INTEROP_BOUNDARIES = frozenset(
    {
        "category_specs/cat/base_category_types.py",
    }
)
AXIOM_HELPER_PATTERN = re.compile(r"\bwith_axiom\s*\(\s*self\s*,\s*['\"](?P<axiom>[^'\"]+)['\"]")
MULTI_CATEGORY_REFINEMENT_RULE = next(rule for rule in RULES if rule.name == "multi-category-refinement")
CONSTRUCTOR_CAST_RULE = next(rule for rule in RULES if rule.name == "constructor-cast-call")


def tracked_spec_python_paths() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", SPEC_PATH_PREFIX],
        check=True,
        text=True,
        capture_output=True,
    )
    return [path for path in result.stdout.splitlines() if path.endswith(".py") and not path.startswith(EXCLUDED_PREFIXES) and Path(path).is_file()]


def rule_applies(path: str, rule: Rule) -> bool:
    if rule.name == "attribute-rebinding-call" and path in ATTRIBUTE_REBINDING_INTEROP_BOUNDARIES:
        return False
    return True


def staged_spec_python_paths() -> set[str]:
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
        check=True,
        text=True,
        capture_output=True,
    )
    return {path for path in result.stdout.splitlines() if path.startswith(SPEC_PATH_PREFIX) and path.endswith(".py") and not path.startswith(EXCLUDED_PREFIXES)}


def location_list(findings: Iterable[Finding]) -> str:
    return ", ".join(str(finding.line_number) for finding in findings)


def axiom_names(findings: Iterable[Finding]) -> str:
    names: list[str] = []
    for finding in findings:
        match = AXIOM_HELPER_PATTERN.search(finding.line)
        if match:
            names.append(match.group("axiom"))
    return ", ".join(dict.fromkeys(names))


def findings_by_path(findings: Iterable[Finding]) -> dict[str, list[Finding]]:
    grouped: dict[str, list[Finding]] = {}
    for finding in findings:
        if finding.path not in grouped:
            grouped[finding.path] = []
        grouped[finding.path].append(finding)
    return grouped


def _format_typing_cast_call(findings: list[Finding]) -> str:
    any_casts = [f for f in findings if "cast(Any" in f.line]
    lines = [f"  - eliminate cast calls at lines {location_list(findings)}"]
    if any_casts:
        lines.append(f"  - highest-risk Any casts at lines {location_list(any_casts)}; these require a real owner/type surface, not a narrower local assertion")
    return "\n".join(lines)


def _format_with_axiom(findings: list[Finding]) -> str:
    names = axiom_names(findings)
    suffix = f" for axioms {names}" if names else ""
    return "\n".join(
        [
            f"  - replace with_axiom(self, ...) selectors at lines {location_list(findings)} with self._with_axiom(...){suffix}",
            "  - verify each named axiom is a descriptor on the exact _base_category_class_and_axiom base class identity",
        ]
    )


_RULE_FORMATTERS: dict[str, Callable[[list[Finding]], str]] = {
    "typing-cast-import": lambda fs: f"  - remove typing.cast imports at lines {location_list(fs)} after replacing casts in this file",
    "typing-cast-call": _format_typing_cast_call,
    "with-axiom-helper-on-self": _format_with_axiom,
    "cached-method-import": lambda fs: (
        f"  - remove cached_method imports at lines {location_list(fs)} unless this file records a concrete Sage runtime identity/cache obligation"
    ),
    "cached-method-adapter": lambda fs: f"  - delete local cached_method adapters at lines {location_list(fs)}; wrapper aliases are engineering leakage in spec code",
    "cached-method-decorator": lambda fs: (
        f"  - review cached_method decorators at lines {location_list(fs)}; keep only if a source-grounded Sage category identity/cache requirement is visible"
    ),
    "attribute-rebinding-call": lambda fs: (
        f"  - remove attribute rebinding calls at lines {location_list(fs)}; "
        "category specs must expose constructors and methods through their "
        "mathematical owners, not through ambient mutation"
    ),
    "ambient-attribute-assignment": lambda fs: (
        f"  - remove ambient attribute assignments at lines {location_list(fs)}; publish the constructor or method on the owning category surface instead"
    ),
    "dynamic-namespace-mutation": lambda fs: (
        f"  - remove dynamic namespace mutation at lines {location_list(fs)}; publish the surface on the owning category or move a proven interop bridge out of spec code"
    ),
    "multi-category-refinement": lambda fs: (
        f"  - replace multi-category refinements at lines {location_list(fs)} "
        "with the single smallest mathematically correct category; inherited "
        "categories belong to the category graph"
    ),
    "constructor-cast-call": lambda fs: (
        f"  - remove constructor-local casts at lines {location_list(fs)}; "
        "constructor results must be admitted by refine_category into the "
        "source-grounded target category, not asserted by typing.cast"
    ),
}


def print_repair_frontier(title: str, findings: list[Finding]) -> None:
    print(title)
    if not findings:
        print("- none")
        return

    grouped = findings_by_path(findings)
    for path, file_findings in sorted(grouped.items(), key=lambda item: (-len(item[1]), item[0])):
        by_rule: dict[str, list[Finding]] = {rule.name: [] for rule in RULES}
        for finding in file_findings:
            by_rule[finding.rule.name].append(finding)

        print(f"- {path}: {len(file_findings)} findings")

        for rule in RULES:
            rule_findings = by_rule[rule.name]
            if rule_findings:
                print(_RULE_FORMATTERS[rule.name](rule_findings))


def ast_multi_category_refinement_findings(path: str, text: str, staged: bool) -> list[Finding]:
    try:
        tree = ast.parse(text, filename=path)
    except SyntaxError:
        return []

    lines = text.splitlines()
    findings: list[Finding] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        function = node.func
        if isinstance(function, ast.Name):
            function_name = function.id
        elif isinstance(function, ast.Attribute):
            function_name = function.attr
        else:
            continue
        if function_name != "refine_category" or len(node.args) < 2:
            continue
        categories = node.args[1]
        if not isinstance(categories, ast.List | ast.Tuple):
            continue
        if len(categories.elts) <= 1:
            continue
        line_number = node.lineno
        line = lines[line_number - 1] if 0 < line_number <= len(lines) else ""
        findings.append(
            Finding(
                path=path,
                line_number=line_number,
                rule=MULTI_CATEGORY_REFINEMENT_RULE,
                line=line,
                staged=staged,
            )
        )
    return findings


def ast_constructor_cast_findings(path: str, text: str, staged: bool) -> list[Finding]:
    try:
        tree = ast.parse(text, filename=path)
    except SyntaxError:
        return []

    lines = text.splitlines()
    findings: list[Finding] = []

    class ConstructorCastVisitor(ast.NodeVisitor):
        def __init__(self) -> None:
            self.class_stack: list[str] = []

        def visit_ClassDef(self, node: ast.ClassDef) -> None:
            self.class_stack.append(node.name)
            self.generic_visit(node)
            self.class_stack.pop()

        def visit_Call(self, node: ast.Call) -> None:
            if any(class_name in {"Constructors", "_Constructors"} for class_name in self.class_stack):
                function = node.func
                if isinstance(function, ast.Name):
                    function_name = function.id
                elif isinstance(function, ast.Attribute):
                    function_name = function.attr
                else:
                    function_name = ""
                if function_name == "cast":
                    line_number = node.lineno
                    line = lines[line_number - 1] if 0 < line_number <= len(lines) else ""
                    findings.append(
                        Finding(
                            path=path,
                            line_number=line_number,
                            rule=CONSTRUCTOR_CAST_RULE,
                            line=line,
                            staged=staged,
                        )
                    )
            self.generic_visit(node)

    ConstructorCastVisitor().visit(tree)
    return findings


def print_exact_findings(title: str, findings: list[Finding]) -> None:
    print(title)
    if not findings:
        print("- none")
        return

    for finding in findings:
        staged_marker = " [staged]" if finding.staged else ""
        print(f"- {finding.location}{staged_marker}: {finding.rule.name}: {finding.rule.message}")
        print(f"  Code: {finding.line.strip()}")


def main() -> int:
    fail_on_staged = "--fail-on-staged" in sys.argv[1:]
    staged_paths = staged_spec_python_paths()
    findings: list[Finding] = []
    for path in tracked_spec_python_paths():
        text = Path(path).read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            for rule in RULES:
                if not rule_applies(path, rule):
                    continue
                if rule.pattern.search(line):
                    findings.append(
                        Finding(
                            path=path,
                            line_number=line_number,
                            rule=rule,
                            line=line,
                            staged=path in staged_paths,
                        )
                    )
        findings.extend(ast_multi_category_refinement_findings(path, text, path in staged_paths))
        findings.extend(ast_constructor_cast_findings(path, text, path in staged_paths))

    if findings:
        staged_findings = [finding for finding in findings if finding.staged]
        hard_fail_findings = [finding for finding in findings if finding.rule.hard_fail]
        by_rule = Counter(finding.rule.name for finding in findings)
        staged_by_rule = Counter(finding.rule.name for finding in staged_findings)
        hard_fail_by_rule = Counter(finding.rule.name for finding in hard_fail_findings)
        by_file = Counter(finding.path for finding in findings)
        print("WARNING: category_specs spec code contains banned patterns.")
        print()
        print("Summary:")
        print(f"- scanned files: {len(tracked_spec_python_paths())}")
        print(f"- affected files: {len(by_file)}")
        print(f"- total findings: {len(findings)}")
        print(f"- hard-fail findings: {len(hard_fail_findings)}")
        print(f"- staged affected files: {len({f.path for f in staged_findings})}")
        print(f"- staged findings: {len(staged_findings)}")
        print(f"- mode: {'fail on staged findings' if fail_on_staged else 'warning only'}")
        print()
        print_repair_frontier("Hard-fail repair frontier:", hard_fail_findings)
        print()
        print_repair_frontier("Immediate staged repair frontier:", staged_findings)
        print()
        print("Findings by rule:")
        for rule in RULES:
            total = by_rule[rule.name]
            staged = staged_by_rule[rule.name]
            if total:
                hard = hard_fail_by_rule[rule.name]
                hard_marker = f", {hard} hard-fail" if hard else ""
                print(f"- {rule.name}: {total} total, {staged} staged{hard_marker}")
                print(f"  Action: {rule.action}")
        print()
        print("Repo-wide inherited debt by file:")
        for path, count in by_file.most_common():
            staged_marker = " staged" if path in staged_paths else ""
            print(f"- {path}: {count}{staged_marker}")
        print()
        inherited_findings = [finding for finding in findings if not finding.staged]
        print_repair_frontier("Repo-wide inherited repair frontier:", inherited_findings)
        print()
        print_exact_findings("Exact staged findings:", staged_findings)
        print()
        print_exact_findings("Exact inherited findings:", inherited_findings)

        if hard_fail_findings:
            print()
            print(
                "QC rejected: category_specs contains hard-fail patterns that "
                "can hide constructor ownership, provider routing, category "
                "graph defects, or constructor result/category obligations."
            )
            return 1

        if fail_on_staged and staged_findings:
            print()
            print(f"Commit rejected: staged category_specs files still contain {len(staged_findings)} banned pattern findings.")
            return 1
        print()
        print(f"Warning-only result: {len(findings)} repo-wide findings remain. Use --fail-on-staged to reject commits touching the {len(staged_findings)} staged findings.")
        return 0

    print("No banned category_specs spec patterns found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
