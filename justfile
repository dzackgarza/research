test:
    #!/usr/bin/env bash
    set -euo pipefail
    export PYTHONDONTWRITEBYTECODE=1
    python3 - <<'PY'
    import json
    import os
    import re
    from pathlib import Path

    required_dirs = [
        Path("computations"),
        Path("notes"),
        Path(".agents"),
        Path(".agents/provenance"),
        Path(".agents/references/sage-integral-lattice"),
        Path("projects"),
        Path("references"),
        Path("projects/lattice-research"),
    ]
    for path in required_dirs:
        if not path.exists():
            raise SystemExit(f"missing required path: {path}")
    if Path("notes/research-legacy").exists():
        raise SystemExit("legacy notes bucket still exists; classify notes under notes/papers, notes/topics, or .agents")

    submodule_root = Path("projects/lattice-research")
    def owned_by_umbrella(path):
        return path == submodule_root or submodule_root not in path.parents

    # Use git ls-files so we check only tracked paths, not transient disk
    # state (caches, locks) that .gitignore already excludes.  Walking the
    # filesystem (Path.rglob) fails the next test run on caches the previous
    # run just regenerated.
    import subprocess
    tracked = subprocess.check_output(
        ["git", "ls-files", "-z"], cwd=os.getcwd()
    ).decode().split("\0")
    for entry in tracked:
        if not entry:
            continue
        path = Path(entry)
        if not owned_by_umbrella(path):
            continue
        parts = set(path.parts)
        if ".git" in parts:
            continue
        if path.is_dir() and not any(path.iterdir()):
            raise SystemExit(f"empty placeholder directory should not exist: {path}")
        if path.suffix == ".lock":
            raise SystemExit(f"transient lock file should not be tracked here: {path}")
        # Artifact placement routing (AGENTS.md / CLAUDE.md / .claude ownership)
        # is global QC's concern — owned by ~/ai-review-ci, not reinvented here.

    suspicious_patterns = [
        re.compile(r"gh" + r"o_[A-Za-z0-9_]{20,}"),
        re.compile(r"sk" + r"-[A-Za-z0-9]{20,}"),
        re.compile(r"AI" + r"zaSy[A-Za-z0-9_-]{20,}"),
    ]
    suspicious_literals = [
        " ".join(("PRIVATE", "KEY")),
        " ".join(("BEGIN", "OPENSSH")),
        " ".join(("BEGIN", "RSA")),
    ]
    for path in Path(".").rglob("*"):
        if not owned_by_umbrella(path):
            continue
        if not path.is_file() or ".git" in path.parts:
            continue
        try:
            text = path.read_text(errors="ignore")
        except OSError:
            continue
        env_magic = "%e" + "nv "
        api_key_suffix = "_" + "API" + "_" + "KEY"
        if env_magic in text and api_key_suffix in text:
            raise SystemExit(f"notebook-style API key environment assignment in {path}")
        for pattern in suspicious_patterns:
            if pattern.search(text):
                raise SystemExit(f"credential-looking token matching {pattern.pattern!r} in {path}")
        for needle in suspicious_literals:
            if needle in text:
                raise SystemExit(f"credential-looking marker {needle!r} in {path}")

    for path in Path("computations/notebooks").rglob("*.ipynb"):
        json.loads(path.read_text())

    gitmodules = Path(".gitmodules")
    if "projects/lattice-research" not in gitmodules.read_text():
        raise SystemExit("lattice-research submodule missing from .gitmodules")
    PY
    # Every spike that carries a justfile is on QC rails automatically —
    # adding a spike never requires editing this file (see AGENTS.md).
    shopt -s nullglob
    for spike_justfile in computations/experiments/*/justfile; do
        just -f "$spike_justfile" test
    done

test-ci: test

# Review calibration (submodule) — delegate to review-calibration/justfile.
# Requires the submodule: git submodule update --init review-calibration
review-calibration-packet:
    just -f review-calibration/justfile review-packet

review-calibration-score artifact:
    just -f review-calibration/justfile score "{{artifact}}"

review-calibration-general:
    gh workflow run "General Review" --repo dzackgarza/research-review-calibration

review-calibration-slop:
    gh workflow run "Slop Review" --repo dzackgarza/research-review-calibration
