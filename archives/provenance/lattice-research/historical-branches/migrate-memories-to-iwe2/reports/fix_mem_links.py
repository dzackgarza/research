#!/usr/bin/env python3
"""Rewrite old `mem:<oldkey>` cross-references in migrated vault memories to new iwe2
keys. Builds oldkey->newkey from the migration plan + live vault titles. Reports any
dangling reference (points at a dropped/junk memory) instead of silently leaving it.

Usage:
    python3 reports/fix_mem_links.py --dry-run
    python3 reports/fix_mem_links.py
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from migrate_memories import REPO, build_plan  # noqa: E402

VAULT = Path("/home/dzack/.agent-memory-vault")
MEM_LINK = re.compile(r"mem:([A-Za-z0-9/_.-]+)")


def live_title_to_key() -> dict[str, str]:
    res = subprocess.run(
        ["iwe2", "inspect", "paths", "--scope", "both", "--kind", "notes", "--format", "json"],
        cwd=REPO, capture_output=True, text=True, check=True,
    )
    return {n["title"]: n["key"] for n in json.loads(res.stdout)["paths"]}


def build_oldkey_map() -> dict[str, str]:
    title_to_key = live_title_to_key()
    mapping: dict[str, str] = {}
    for entry in build_plan():
        newkey = title_to_key.get(entry["title"])
        assert newkey, f"no live key for migrated title {entry['title']!r}"
        for kind, rel in entry["sources"]:
            if kind == "MEM":
                mapping[rel[:-3] if rel.endswith(".md") else rel] = newkey
    return mapping


def main() -> int:
    dry = "--dry-run" in sys.argv
    mapping = build_oldkey_map()
    note_files = [p for p in VAULT.rglob("*.md") if p.name != "index.md"]
    dangling: dict[str, int] = {}
    changed = 0
    for path in note_files:
        text = path.read_text(encoding="utf-8")
        refs = MEM_LINK.findall(text)
        if not refs:
            continue
        new_text = text
        for old in sorted(set(refs), key=len, reverse=True):  # longest first
            if old in mapping:
                new_text = new_text.replace(f"mem:{old}", f"mem:{mapping[old]}")
            else:
                dangling[old] = dangling.get(old, 0) + text.count(f"mem:{old}")
        if new_text != text:
            changed += 1
            if not dry:
                path.write_text(new_text, encoding="utf-8")
    print(f"files with mem: refs rewritten: {changed} (dry-run={dry})")
    if dangling:
        print("\nDANGLING refs (target dropped/never-migrated):")
        for k, n in sorted(dangling.items(), key=lambda kv: -kv[1]):
            print(f"  {n:3}x  mem:{k}")
    if not dry and changed:
        subprocess.run(["git", "-C", str(VAULT), "add", "-A"], check=True)
        subprocess.run(
            ["git", "-C", str(VAULT), "commit", "-q", "-m",
             "fix: rewrite mem: cross-refs to new iwe2 keys"], check=True,
        )
        print("vault committed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
