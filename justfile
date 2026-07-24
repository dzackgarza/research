# research — SageMath research automation.
#
# QC delegates to ~/ai-review-ci/justfiles/sage.just. Project-specific recipes
# below are non-QC entry points or narrow repo orchestration.

# ai-review-ci contract variables consumed by doctor and workflow installers.
ai_review_ci_schema_version := "1"
ai_review_ci_profile := "sage"
ai_review_ci_ref := "main"
ai_review_ci_release_channel := "main"
ai_review_ci_workflow_template_version := "1"
ai_review_ci_local_delegation := "global-justfile"
ai_review_ci_default_branch := "main"

# List available recipes
default:
    @just --list

# Prepare generated local artifacts needed by the interactive category viewer.
setup:
    @just -f computations/experiments/sage_category_tree_stubs/justfile setup

# Build the installable Sage research distribution
build: _lock
    uv build

# Refresh the docs bibliography from the shared ~/.pandoc bib (never frozen in-repo; CI fetches it from the pandoc-config repo)
docs-bib:
    cp ~/.pandoc/bib/references.bib docs/references.bib

# Gate: render the docs book and fail on undefined citations, unresolved cross-refs, or broken anchor links
docs-check: docs-bib
    python3 scripts/docs_check.py

# Add an nLab citation to docs/refs-web.bib by scraping its canonical /cite page
cite-nlab page:
    python3 scripts/cite_add.py nlab "{{page}}"

# Verify a Stacks Project tag resolves (cite as [@stacks-TAG]; links via the global The25 entry)
cite-stacks tag:
    python3 scripts/cite_add.py stacks "{{tag}}"

# Regenerate docs/refs-web.bib from canonical sources (re-scrapes every nLab entry; hand-edits are lost)
refs-web-refresh:
    python3 scripts/refs_web_refresh.py

# Regenerate the interactive category graph from its DOT manifest (docs/lean/category-graph.dot)
graph:
    python3 scripts/build_graph.py

# Serve the docs site locally with live reload
docs-preview: docs-bib
    quarto preview docs --no-browser --port 7654

[private]
_lock:
    uv lock

_lean-axiom-audit:
    @just -f computations/experiments/lean_category_dsl_spike/justfile _lean-axiom-audit

# Run commit-tier SageMath QC through the central implementation
test-commit:
    @just -f ~/ai-review-ci/justfiles/sage.just -d . test-commit

# Run push-tier SageMath QC through the central implementation
test-push:
    @just -f ~/ai-review-ci/justfiles/sage.just -d . test-push
    @just -f ~/ai-review-ci/justfiles/lean.just -d . lean-axiom-audit

# Run CI acceptance QC through the central implementation
test-ci:
    @just -f ~/ai-review-ci/justfiles/sage.just -d . test-ci
    @just -f ~/ai-review-ci/justfiles/lean.just -d . lean-axiom-audit

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
