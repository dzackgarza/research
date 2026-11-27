#!/usr/bin/env python3
"""One-shot migration of in-repo memories into the iwe2 vault.

Reads the committed classification ledger for clean single-file DURABLE rows and
applies hardcoded merge groups, global promotions, and special cases. Runs `iwe2 add`
sequentially (the vault commits per call, so it is not concurrency-safe). Stdlib only.

Usage:
    python3 reports/migrate_memories.py --dry-run   # print planned adds
    python3 reports/migrate_memories.py             # execute
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO = Path("/home/dzack/research")
MEM = REPO / ".agents" / "memories"
SERENA = REPO / ".serena" / "memories"
LEDGER = REPO / "reports" / "2026-06-16-memory-migration-ledger.md"

# --- Skip rules for ledger parsing -------------------------------------------------
# Rows whose path contains any of these are handled explicitly below, never parsed.
PARSE_SKIP_SUBSTRINGS = ("...", "(", "dutsik", "hermes/")

# Merge groups: pointer stem -> source paths (relative to .agents/memories/). The whole
# group becomes ONE memory; member paths are excluded from single-row parsing.
MERGE_GROUPS: dict[str, list[str]] = {
    "category-framework-design": [
        "skills/category-framework-design.md",
        "skills/category-framework-design/autset-categories-path.md",
        "skills/category-framework-design/autset-integration-plan.md",
        "skills/category-framework-design/axioms-with-generators-finitely-presented.md",
        "skills/category-framework-design/category-creation-notes.md",
        "skills/category-framework-design/category-refinement-phases.md",
        "skills/category-framework-design/homsets-structural-core.md",
    ],
    "category-spec-subtrees": [
        "skills/category-spec-subtrees.md",
        "skills/category-spec-subtrees/subtrees.md",
    ],
    "category-spec-workflow": [
        "skills/category-spec-workflow.md",
        "skills/category-spec-workflow/workflow.md",
    ],
    "lattice-redesign": [
        "skills/lattice-redesign.md",
        "skills/lattice-redesign/category-abc-spec.md",
        "skills/lattice-redesign/lattice-interface-style-guide.md",
        "skills/lattice-redesign/lattice-redesign-corrections-spec.md",
    ],
    "research-co-mathematician-workflow": [
        "skills/research-co-mathematician-workflow.md",
        "skills/research-co-mathematician-workflow/architecture.md",
    ],
    "research-math-boundary": [
        "skills/research-math-boundary.md",
        "skills/research-math-boundary/math-boundary.md",
    ],
    "research-project-workflow": [
        "skills/research-project-workflow.md",
        "skills/research-project-workflow/project-workflow.md",
    ],
    "research-proof-auditing": [
        "skills/research-proof-auditing.md",
        "skills/research-proof-auditing/proof-auditing.md",
    ],
    "research-repo-structure": [
        "skills/research-repo-structure.md",
        "skills/research-repo-structure/repo-structure.md",
    ],
    "research-scheduling": [
        "skills/research-scheduling.md",
        "skills/research-scheduling/cadence.md",
    ],
    "sage-category-source-maps": [
        "skills/sage-category-source-maps.md",
        "skills/sage-category-source-maps/ring-integration.md",
        "skills/sage-category-source-maps/set-spec.md",
    ],
}

# Title + type for each merge group (type taken from the pointer row in the ledger).
MERGE_META: dict[str, tuple[str, str]] = {
    "category-framework-design": ("Category Framework Design", "advice"),
    "category-spec-subtrees": ("Category Spec Subtrees", "advice"),
    "category-spec-workflow": ("Category Spec Workflow", "advice"),
    "lattice-redesign": ("Lattice Redesign", "advice"),
    "research-co-mathematician-workflow": ("Research Co Mathematician Workflow", "advice"),
    "research-math-boundary": ("Research Math Boundary", "advice"),
    "research-project-workflow": ("Research Project Workflow", "advice"),
    "research-proof-auditing": ("Research Proof Auditing", "advice"),
    "research-repo-structure": ("Research Repo Structure", "advice"),
    "research-scheduling": ("Research Scheduling", "advice"),
    "sage-category-source-maps": ("Sage Category Source Maps", "reference"),
}

# Stems promoted to global scope (applies to single rows and merge groups by stem).
GLOBAL_STEMS: set[str] = {
    # Group A general research discipline
    "analysis-must-be-grounded",
    "corrections-update-the-model-not-the-artifact",
    "diagnostics-are-navigation",
    "hard-problem-artifact-drift",
    "mathematical-source-report-memories",
    "memory-management-discipline",
    "paperwork-is-a-routing-layer-not-progress",
    "periodic-research-relevance-check",
    "repo-understanding-is-agent-work",
    "research-standardness-and-argument-standards",
    # Group B general research workflows
    "creating-fixtures",
    "opencode-one-shot-workers",
    "research-code-style",
    "research-co-mathematician-workflow",
    "research-planning-cleanup",
    "research-project-workflow",
    "research-proof-auditing",
    "research-scheduling",
    "research-source-acquisition",
}

# Full-path global overrides (for body-only files whose bare stem differs from the
# conceptual name, e.g. skills/research-code-style/code-style.md).
GLOBAL_PATHS: set[str] = {
    "skills/research-code-style/code-style.md",
}

# JUNK stems / paths to exclude from migration entirely (distill-then-trash handled
# separately; nothing durable left to migrate for these).
JUNK_PATHS: set[str] = {
    "current-goal-handoff.md",
    "index.md",
    "provider-satisfaction-goal-contract.md",
    "provider-satisfaction-goal-state.md",
    "provider-satisfaction-phase-source-reconstruction.md",
    "provider-satisfaction-phase-source-repair.md",
    "provider-satisfaction-phase-verification-review.md",
    "skills/request-triager.md",
}


def strip_frontmatter(text: str) -> str:
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "".join(lines[i + 1 :]).lstrip("\n")
    return text  # unterminated frontmatter: leave as-is


def read_body(rel: str, base: Path = MEM) -> str:
    path = base / rel
    assert path.is_file(), f"missing source file: {path}"
    return strip_frontmatter(path.read_text(encoding="utf-8")).rstrip() + "\n"


def stem_of(rel: str) -> str:
    return Path(rel).stem


# --- Build the migration plan ------------------------------------------------------
def parse_ledger_rows() -> list[dict]:
    rows: list[dict] = []
    in_table = False
    for line in LEDGER.read_text(encoding="utf-8").splitlines():
        if line.startswith("|") and "---" in line and set(line) <= set("|-: "):
            in_table = True
            continue
        if not line.startswith("|"):
            in_table = False
            continue
        if not in_table:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5:
            continue
        path, title, mtype, scope, disp = cells[0], cells[1], cells[2], cells[3], cells[4]
        if path in ("path", "serena_path"):  # header
            continue
        # Group D has a different column layout (col 1 = relationship); its UNIQUE rows
        # are migrated explicitly below, so never parse them here.
        if title in ("UNIQUE", "DUPLICATE", "DUPLICATE+UNIQUE", "relationship"):
            continue
        if disp != "DURABLE":
            continue
        if mtype not in ("decision", "trap", "advice", "context", "reference"):
            continue  # skips Group D layout (different columns) and malformed rows
        if any(s in path for s in PARSE_SKIP_SUBSTRINGS):
            continue
        rows.append({"path": path, "title": title, "type": mtype, "scope": scope})
    return rows


def build_plan() -> list[dict]:
    merge_members = {p for paths in MERGE_GROUPS.values() for p in paths}
    plan: list[dict] = []

    # 1. Single-file DURABLE rows from the ledger (Groups A, B, C).
    for row in parse_ledger_rows():
        if row["path"] in JUNK_PATHS or row["path"] in merge_members:
            continue
        is_global = stem_of(row["path"]) in GLOBAL_STEMS or row["path"] in GLOBAL_PATHS
        scope = "global" if is_global else "project"
        plan.append({
            "title": row["title"], "type": row["type"], "scope": scope,
            "sources": [("MEM", row["path"])],
        })

    # 2. Merge groups -> one memory each.
    for stem, members in MERGE_GROUPS.items():
        title, mtype = MERGE_META[stem]
        scope = "global" if stem in GLOBAL_STEMS else "project"
        plan.append({
            "title": title, "type": mtype, "scope": scope,
            "sources": [("MEM", m) for m in members],
        })

    # 3. Explicit special cases.
    # hermes -> global
    plan.append({"title": "Hermes Vault Operations", "type": "reference", "scope": "global",
                 "sources": [("MEM", "hermes/MEMORY.md")]})
    plan.append({"title": "Hermes User Preferences", "type": "advice", "scope": "global",
                 "sources": [("MEM", "hermes/USER.md")]})
    # dutsik: keep repo-specific synthesis, consolidate the rest into one reference.
    plan.append({"title": "Polyhedral Common Indefinite Methods", "type": "reference",
                 "scope": "project", "sources": [(
                     "MEM",
                     "theory/external/dutsik_polyhedral/polyhedral_common/notes/indefinite_methods.md",
                 )]})
    plan.append({"title": "Polyhedral Common Reference", "type": "reference",
                 "scope": "project", "sources": [("FILE", "reports/_staging/polyhedral-common-reference.md")]})
    # 4. Six UNIQUE .serena memories.
    serena_unique = [
        ("Category Spec Predicate Policy", "advice", "category-spec-predicate-policy.md"),
        ("Completion Checklist", "advice", "completion_checklist.md"),
        ("Project Overview", "context", "project_overview.md"),
        ("Style And Workflow", "advice", "style_and_workflow.md"),
        ("Suggested Commands", "reference", "suggested_commands.md"),
        ("Category Spec Smoke Triage", "advice", "skills/category-spec-smoke-triage.md"),
    ]
    for title, mtype, rel in serena_unique:
        plan.append({"title": title, "type": mtype, "scope": "project",
                     "sources": [("SERENA", rel)]})
    return plan


def assemble_body(sources: list[tuple[str, str]]) -> str:
    parts = []
    for kind, rel in sources:
        if kind == "MEM":
            parts.append(read_body(rel, MEM))
        elif kind == "SERENA":
            parts.append(read_body(rel, SERENA))
        elif kind == "FILE":
            p = REPO / rel
            assert p.is_file(), f"missing staged file: {p}"
            parts.append(p.read_text(encoding="utf-8").rstrip() + "\n")
        else:
            raise AssertionError(f"unknown source kind: {kind}")
    return "\n\n".join(parts)


def main() -> int:
    dry = "--dry-run" in sys.argv
    plan = build_plan()
    print(f"planned memories: {len(plan)} (dry-run={dry})\n")
    for i, m in enumerate(plan, 1):
        body = assemble_body(m["sources"]) if not dry else None
        if dry:
            try:
                body_preview = assemble_body(m["sources"])
                nlines = body_preview.count("\n")
            except AssertionError as e:
                nlines = f"!! {e}"
            print(f"{i:3} [{m['scope']:7}/{m['type']:9}] {m['title']!r} "
                  f"<- {len(m['sources'])} src, {nlines} lines")
            continue
        cmd = ["iwe2", "add", "--scope", m["scope"], "--type", m["type"],
               "--title", m["title"], "--content", body]
        res = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True)
        if res.returncode != 0:
            print(f"FAILED on {m['title']!r}:\n{res.stderr}", file=sys.stderr)
            return 1
        print(f"{i:3} added [{m['scope']}/{m['type']}] {m['title']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
