# Build the installable Sage research distribution
build: _lock
    uv build

[private]
_lock:
    uv lock

# Run repository and spike quality gates
test:
    #!/usr/bin/env bash
    set -euo pipefail
    just -f ~/ai-review-ci/justfiles/sage.just -d . test
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

test-ci:
    #!/usr/bin/env bash
    set -euo pipefail
    just -f ~/ai-review-ci/justfiles/sage.just -d . test-ci

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

# Assemble the LLM-review context packet (review-packet.tar).
#
# The packet is the extensible context surface for the advisory review
# workflows (.github/workflows/review-*.yml): a PROMPT.md plus whatever
# reference documents the reviews should be sensitive to, organized below.
# Only the tar is tracked — the exploded tree exists solely for the CI
# reviewer, which unpacks it into .review-context/ and inlines PROMPT.md
# and every packet *.md into the reviewer prompt.
#
# Sources may be untracked in this repo (e.g. vault memory files reached
# through the .agents symlink); assembling locally is what makes them
# available to CI. To change review context: edit the declaration below,
# run `just review-packet`, and commit the tar. The archive is
# byte-deterministic, so git sees a change only when content changed.
review-packet:
    #!/usr/bin/env bash
    set -euo pipefail
    staging="$(mktemp -d)"
    trap 'rm -rf "$staging"' EXIT

    # --- Review packet declaration (edit here) -------------------------
    cat > "$staging/PROMPT.md" <<'PROMPT'
    # Review focus: mathematical research repository

    This repository is a mathematical research monorepo. The active code
    surface is the lattice spike under
    `computations/experiments/sage_lattice_category_spike/` (plus its
    feature-spike fork). Reviews here are advisory: they feed a triage
    ledger and never block work. An empty report is always preferable to
    a stretched finding.

    Prioritize, in order:

    1. **Mathematical correctness.** Claims in code, tests, and notebooks
       must be consistent with the synthetic lattice model specification
       (`spec/SYNTHETIC_LATTICE_MODEL.md` in this packet). Expected values
       must come from the Sage reference or the mapped doctest corpus,
       never from memory. Flag any test asserting a mathematically wrong
       value, any invariant checked in the wrong category, and any
       conflation of near-synonym lattice terms (see the vault traps in
       this packet, e.g. saturation / discriminant triple / dual pair).

    2. **Categorical substrate violations (#100, #101).** The deepest
       current slop drivers are architectural, not cosmetic:
       - **#100 — morphism-centric predicates:** subobjects are `(L, f:
         L ↪ M)`; no `from_ambient_basis`, `ambient=`, stored `_ambient`,
         or coordinate/matrix bypasses (`coordinate_vector`, echelon
         comparison, `solve_left`) where kernel/cokernel/morphism definitions
         exist. Flag latent sites in dual→quotient chains and any predicate
         that demands a shared coordinate frame.
       - **#101 — method placement:** witness-consuming predicates
         (`is_primitive`, `is_isometric`, containment) belong on
         Hom/Emb/Subobjects, not on bare `Lattice` parents. Flag public
         presentation constructors (`_from_module`, `_from_ambient_basis`)
         that should be private.

    3. **Terminology drift.** Public API names, docstrings, and findings
       must use categorical/lexicon vocabulary, not invented engineering
       terms. Consult `references/terminology-dictionary.md` and
       `references/slop-pattern-index.md` in this packet. The always-banned
       terms **carrier** and free-standing **ambient** are hard failures.
       A finding written in drift vocabulary is itself slop.

    4. **Ratified-decision violations.** The `vault/` documents in this
       packet are durable decisions, traps, and advice for this repo.
       Treat them as authoritative: code that contradicts a ratified
       decision is a finding; code that follows one is not, even if it
       looks unusual. Do not re-raise what a decision document already
       settles.

    5. **Style-guide conformance.** `policies/STYLE.md` governs code,
       notebooks, and documentation written against the spike (host-
       language idioms, symbolic API boundary, assertion discipline).

    **Ledger hygiene:** strict `pytest.mark.xfail` markers that cite an
    open GitHub issue in `reason=` are *owned gaps*, not new findings.
    Do not re-file them. Notebook traps already in `vault/traps/` are
    valid only if the artifact was never remediated.

    Do not raise generic software-engineering nitpicks that these
    documents do not support; the deterministic QC stack already owns
    lint/type/coverage concerns.
    PROMPT

    mkdir -p "$staging/policies" "$staging/spec" "$staging/references"
    cp STYLE.md "$staging/policies/STYLE.md"
    cp computations/experiments/sage_lattice_category_spike/SYNTHETIC_LATTICE_MODEL.md "$staging/spec/"
    cp .agents/references/terminology-dictionary.md "$staging/references/"
    cp .agents/references/slop-pattern-index.md "$staging/references/"

    # Vault memory (untracked here; reached through the .agents symlink).
    for section in decisions traps advice context; do
        mkdir -p "$staging/vault/$section"
        cp .agents/"$section"/*.md "$staging/vault/$section/"
    done
    # --------------------------------------------------------------------

    tar --sort=name --owner=0 --group=0 --numeric-owner \
        --mtime='UTC 2020-01-01' --format=gnu \
        -cf review-packet.tar -C "$staging" .
    echo "review-packet.tar: $(tar -tf review-packet.tar | grep -c -v '/$') files"
