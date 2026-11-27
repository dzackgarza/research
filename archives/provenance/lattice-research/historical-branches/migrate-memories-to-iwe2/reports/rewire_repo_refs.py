#!/usr/bin/env python3
"""Phase 4 (bulk): rewrite `.agents/memories/<path>` and `mem:<oldkey>` references in
repo docs to their new iwe2 vault keys, so they survive the Phase 5 trash. Dropped
targets (the trashed handoff) are redirected explicitly. Residual unmapped references
are reported loudly, never silently left.

Targets: repo *.md files that reference the old system, EXCLUDING the soon-trashed
memory stores, the migration reports, and session-junk files.

Usage:
    python3 reports/rewire_repo_refs.py --dry-run
    python3 reports/rewire_repo_refs.py
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from migrate_memories import REPO, build_plan  # noqa: E402

# Explicit redirects for dropped/junk targets still referenced by forward-facing docs.
DROPPED_REDIRECTS = {
    ".agents/memories/current-goal-handoff.md": ".agents/current-goal-phase.md",
    ".agents/memories/current-goal-handoff": ".agents/current-goal-phase.md",
    "mem:current-goal-handoff": ".agents/current-goal-phase.md",
    # Directory / index references whose targets are now scattered vault memories.
    ".agents/memories/theory/external/dutsik_polyhedral/polyhedral_common/":
        "the Polyhedral Common Reference memory in the iwe2 vault",
    ".agents/memories/theory/backends/": "the iwe2 vault (theory backend memories; iwe2 search)",
    ".agents/memories/theory/foundations/": "the iwe2 vault (theory foundation memories; iwe2 search)",
    ".agents/memories/theory/": "the iwe2 vault (theory memories; iwe2 search)",
    ".agents/memories/index.md": "iwe2 inspect tree --scope project",
}

EXCLUDE_PREFIXES = ("/home/dzack/research/.agents/memories/",
                    "/home/dzack/research/.serena/memories/",
                    "/home/dzack/research/reports/")
EXCLUDE_NAMES = {"realset_update_session.md", "session-ses_1914.md", "QC.md", "QC_REPORT.md"}


def live_title_to_key() -> dict[str, str]:
    res = subprocess.run(
        ["iwe2", "inspect", "paths", "--scope", "both", "--kind", "notes", "--format", "json"],
        cwd=REPO, capture_output=True, text=True, check=True,
    )
    return {n["title"]: n["key"] for n in json.loads(res.stdout)["paths"]}


def build_map() -> dict[str, str]:
    title_to_key = live_title_to_key()
    m: dict[str, str] = {}
    for entry in build_plan():
        newkey = title_to_key[entry["title"]]
        for kind, rel in entry["sources"]:
            if kind != "MEM":
                continue
            stem_path = rel[:-3] if rel.endswith(".md") else rel
            m[f".agents/memories/{rel}"] = newkey
            m[f".agents/memories/{stem_path}"] = newkey
            m[f"mem:{stem_path}"] = f"mem:{newkey}"
    m.update(DROPPED_REDIRECTS)
    return m


def target_files() -> list[Path]:
    res = subprocess.run(
        ["grep", "-rlE", r"iwe retrieve|iwe find|iwe tree|iwe stats|iwe search|\.agents/memories|mem:|current-goal-handoff",
         "--include=*.md", "."], cwd=REPO, capture_output=True, text=True)
    files = []
    for line in res.stdout.splitlines():
        p = (REPO / line[2:]).resolve()
        if any(str(p).startswith(pre) for pre in EXCLUDE_PREFIXES):
            continue
        if p.name in EXCLUDE_NAMES:
            continue
        if p.name == "AGENTS.md" and p.parent == REPO:
            continue  # root AGENTS.md hand-edited separately
        files.append(p)
    return files


def main() -> int:
    dry = "--dry-run" in sys.argv
    m = build_map()
    keys_by_len = sorted(m, key=len, reverse=True)  # longest first, avoid prefix clobber
    residual_re = re.compile(r"\.agents/memories/[A-Za-z0-9/_.-]+|mem:[A-Za-z0-9/_.-]+")
    changed = 0
    residuals: dict[str, int] = {}
    for path in target_files():
        text = path.read_text(encoding="utf-8")
        new = text
        for k in keys_by_len:
            if k in new:
                new = new.replace(k, m[k])
        # report anything still pointing at the old system
        for hit in residual_re.findall(new):
            if hit.startswith("mem:projects/") or hit.startswith("mem:global/"):
                continue  # already a valid new key
            residuals[hit] = residuals.get(hit, 0) + 1
        if new != text:
            changed += 1
            if not dry:
                path.write_text(new, encoding="utf-8")
            print(f"{'would rewrite' if dry else 'rewrote'}: {path.relative_to(REPO)}")
    print(f"\nfiles changed: {changed} (dry-run={dry})")
    if residuals:
        print("\nRESIDUAL unmapped old-system refs (review):")
        for k, n in sorted(residuals.items(), key=lambda kv: -kv[1]):
            print(f"  {n:3}x  {k}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
