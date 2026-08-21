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

# Build the installable Sage research distribution
build: _lock
    uv build

# Refresh the docs bibliography from the shared ~/.pandoc bib (never frozen in-repo; CI fetches it from the pandoc-config repo)
docs-bib:
    cp ~/.pandoc/bib/references.bib docs/references.bib

# Gate: render the docs book and fail on undefined citations, unresolved cross-refs, or broken anchor links
docs-check: docs-bib
    python3 scripts/docs_check.py

# Fast check of one docs file: surfaces tikz-compile and pandoc/markdown syntax errors in seconds (no full-book link gate). e.g. `just docs-lint framework/Mathematical-Framework.md`
docs-lint FILE: docs-bib
    cd docs && uvx --from quarto-cli quarto render "{{FILE}}" --to html

# Rename a docs cross-reference/anchor slug everywhere, then prove every reference still resolves. Rewrites {#slug} anchors, @slug crossrefs, and ](…#slug) link fragments in one hyphen-boundary-safe pass (a longer slug is never partially hit) and runs the docs gate. e.g. `just docs-rename-ref def-old-name def-new-name`
docs-rename-ref OLD NEW:
    #!/usr/bin/env bash
    set -euo pipefail
    old="{{OLD}}"
    new="{{NEW}}"
    export old new
    mapfile -t files < <(find docs -name '*.md' -not -path '*/_extensions/*')
    if rg -q --pcre2 "\\{#\\Q${new}\\E(?=[ }])" "${files[@]}"; then
        echo "docs-rename-ref: refusing — {#${new}} is already a defined anchor; choose a free name" >&2
        exit 1
    fi
    n=$({ rg -c --pcre2 "(?<![-\\w])\\Q${old}\\E(?![-\\w])" "${files[@]}" || true; } | awk -F: '{s+=$2} END{print s+0}')
    if [ "${n}" -eq 0 ]; then
        echo "docs-rename-ref: no occurrences of '${old}' found" >&2
        exit 1
    fi
    echo "docs-rename-ref: rewriting ${n} occurrence(s) of '${old}' → '${new}'"
    perl -i -pe 's/(?<![-\w])\Q$ENV{old}\E(?![-\w])/$ENV{new}/g' "${files[@]}"
    if just docs-check; then
        echo "docs-rename-ref: done — every reference resolves"
    else
        echo "docs-rename-ref: docs gate FAILED after rename; inspect the report, or 'git checkout -- docs' to revert" >&2
        exit 1
    fi

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

# Serve the docs site locally with live reload (quarto provisioned via uvx)
docs-preview: docs-bib
    # ponytail: two previews on the same dir cross-trigger each other's watchers
    # (each renders output back into docs/) → endless ~10s reload loop. Kill any
    # stale instance first so this always replaces rather than duplicates.
    -pkill -f 'quarto preview docs --no-browser --port 7654'
    @sleep 1
    uvx --from quarto-cli quarto preview docs --no-browser --port 7654

# Link sage-init.sage as Sage's startup file (${DOT_SAGE:-~/.sage}/init.sage), giving every Sage process — terminal REPL and every Jupyter kernel — implicit LaTeX rendering of cell results. Idempotent, and refuses to replace anything it did not create.
sage-init-install:
    #!/usr/bin/env bash
    set -euo pipefail
    source="{{justfile_directory()}}/src/dzack_research/preamble/init.sage"
    target="${DOT_SAGE:-$HOME/.sage}/init.sage"
    [ -f "${source}" ] || { echo "sage-init-install: missing ${source}" >&2; exit 1; }
    mkdir -p "$(dirname "${target}")"
    if [ -L "${target}" ]; then
        current="$(readlink -f "${target}")"
        if [ "${current}" = "$(readlink -f "${source}")" ]; then
            echo "sage-init-install: already installed (${target})"
            exit 0
        fi
        echo "sage-init-install: refusing — ${target} is a symlink to ${current}, not to ${source}" >&2
        echo "sage-init-install: remove it yourself if that link is stale" >&2
        exit 1
    fi
    if [ -e "${target}" ]; then
        echo "sage-init-install: refusing — ${target} already exists and is not a symlink" >&2
        echo "sage-init-install: it is not ours to replace; move it aside, then rerun" >&2
        exit 1
    fi
    ln -s "${source}" "${target}"
    echo "sage-init-install: linked ${target} -> ${source}"
    echo "sage-init-install: restart running kernels to pick it up"

# Prove the installed startup file actually typesets in a real Sage kernel
sage-init-check:
    #!/usr/bin/env bash
    set -euo pipefail
    # Through ``sage -c``, which is the only way this Sage runs code: the CLI
    # has no ``--python``.  The probe is written out first because ``-c`` reads
    # trailing words as more code.
    probe="$(mktemp --suffix=.py)"
    trap 'gio trash "${probe}" 2>/dev/null || true' EXIT
    cat > "${probe}" <<'PY'
    from jupyter_client.manager import start_new_kernel

    km, kc = start_new_kernel(kernel_name="sagemath")
    try:
        results = {}
        # A matrix, not ``QQ['t']``: in a preamble session ``PolynomialRing``
        # is the owned free-algebra constructor, so that expression no longer
        # names a Sage object at all.  The rule under test is that an object
        # able to typeset does, and a matrix is the specimen a session still
        # gets from the engine.
        for label, code in [("typeset", "matrix(ZZ, [[1, 2], [3, 4]])"), ("plain", "'a plain string'")]:
            got = {}
            kc.execute_interactive(
                code, timeout=180,
                output_hook=lambda m: got.update(m["content"]["data"])
                if m["msg_type"] in ("execute_result", "display_data") else None)
            results[label] = got
        assert results["typeset"].get("text/latex"), "Sage object did not render as LaTeX"
        assert not results["plain"].get("text/latex"), "plain string was typeset; it should not be"
        print("sage-init-check: ok — Sage objects typeset, plain text left alone")
    finally:
        kc.stop_channels()
        km.shutdown_kernel()
    PY
    "$(just --evaluate sage_bin 2>/dev/null || echo "${SAGE_BIN:-sage}")" \
        -c "exec(open('${probe}').read())"

# Rebuild the Sage development environment, then install the current preparser and research package
sage-rebuild:
    #!/usr/bin/env bash
    set -euo pipefail
    research_root="{{justfile_directory()}}"
    sage_root="${SAGE_DEV_ROOT:-/home/dzack/gitclones/sage-dev-allopts}"
    sage_python_version="${SAGE_PYTHON_VERSION:-3.14}"
    [ -f "${sage_root}/uv.lock" ] || { echo "sage-rebuild: missing ${sage_root}/uv.lock" >&2; exit 1; }
    cd "${sage_root}"
    uv sync --python "${sage_python_version}" --frozen --inexact --no-install-project
    uv sync --python "${sage_python_version}" --frozen --inexact --no-build-isolation --reinstall-package sagemath
    sage_python="${sage_root}/.venv/bin/python"
    uv pip install --python "${sage_python}" --reinstall-package tree-sitter-sage \
        "tree-sitter-sage @ git+https://github.com/dzackgarza/tree-sitter-sage@main"
    uv pip install --python "${sage_python}" --no-deps --editable "${research_root}"

[private]
_lock:
    uv lock

# Run commit-tier SageMath QC through the central implementation
test-commit:
    @just -f ~/ai-review-ci/justfiles/sage.just -d . test-commit

# Run push-tier SageMath QC through the central implementation
test-push:
    @just -f ~/ai-review-ci/justfiles/sage.just -d . test-push

# Run CI acceptance QC through the central implementation
test-ci:
    @just -f ~/ai-review-ci/justfiles/sage.just -d . test-ci

# Review calibration (submodule) — delegate to review-calibration/justfile.
# Requires the submodule: git submodule update --init review-calibration
review-calibration-packet:
    just -f review-calibration/justfile review-packet

# Score a review calibration artifact
review-calibration-score artifact:
    just -f review-calibration/justfile score "{{artifact}}"

# Trigger general review on review-calibration
review-calibration-general:
    gh workflow run "General Review" --repo dzackgarza/research-review-calibration

# Trigger slop review on review-calibration
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
    surface is the preamble under `src/dzack_research/preamble/` (the
    earlier lattice spikes were absorbed into it and deleted). Reviews
    here are advisory: they feed a triage ledger and never block work. An
    empty report is always preferable to a stretched finding.

    Prioritize, in order:

    1. **Mathematical correctness.** Claims in code, tests, and notebooks
       must be consistent with the cited mathematical literature; expected
       values come from cited sources or an independent oracle,
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

    mkdir -p "$staging/policies" "$staging/references"
    cp STYLE.md "$staging/policies/STYLE.md"
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
