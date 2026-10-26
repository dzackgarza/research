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
preamble_megadoc_file := "docs/preamble-megadoc.md"

# List available recipes
default:
    @just --list

# Build the installable Sage research distribution
build: _lock
    uv build

# Refresh the docs bibliography and MathJax macro include from the shared ~/.pandoc sources (never frozen in-repo; CI fetches them from the pandoc-config repo). The macros are the generated corpus: the book defines none of its own.
docs-assets:
    cp --remove-destination ~/.pandoc/bib/references.bib writing/.assets/references.bib
    cp --remove-destination ~/.pandoc/templates/css/mathjax-macros.html writing/.assets/mathjax-macros.html
    python3 scripts/docs_figures.py

# Rebuild the book and refresh the local static copy at http://lattice-research.localhost/
docs-deploy: docs-check
    #!/usr/bin/env bash
    set -euo pipefail
    # nginx serves /var/www/static-sites/<app> for <app>.localhost, and the entry for
    # this book is a symlink straight at the render output, so a successful render *is*
    # the deploy: nothing to copy, and no window where the site is half-written. The
    # gate is a dependency, so a book with a broken citation or a dangling reference
    # never reaches the served copy -- the previous render stays up instead.
    site="$(pwd)/writing/.book/_site"
    link=/var/www/static-sites/lattice-research
    [ -f "$site/index.html" ] || { echo "docs-deploy: $site has no index.html" >&2; exit 1; }
    [ "$(readlink -f "$link" 2>/dev/null)" = "$site" ] || ln -sfn "$site" "$link"
    code=$(curl -s -o /dev/null -w '%{http_code}' -H 'Host: lattice-research.localhost' http://127.0.0.1/)
    [ "$code" = 200 ] || { echo "docs-deploy: nginx answered $code for lattice-research.localhost" >&2; exit 1; }
    echo "docs-deploy: http://lattice-research.localhost/ is serving $(find "$site" -name '*.html' | wc -l) pages"

# Gate: render the docs book and fail on undefined citations, unresolved cross-refs, or broken anchor links
docs-check: docs-assets
    python3 scripts/docs_check.py

# Fast check of one docs file: surfaces tikz-compile and pandoc/markdown syntax errors in seconds (no full-book link gate). e.g. `just docs-lint category-theory/framework/Mathematical-Framework.md`
docs-lint FILE: docs-assets
    cd writing/.book && uvx --from quarto-cli quarto render "{{FILE}}" --to html

# Rename a docs cross-reference/anchor slug everywhere, then prove every reference still resolves. Rewrites {#slug} anchors, @slug crossrefs, and ](…#slug) link fragments in one hyphen-boundary-safe pass (a longer slug is never partially hit) and runs the docs gate. e.g. `just docs-rename-ref def-old-name def-new-name`
docs-rename-ref OLD NEW:
    #!/usr/bin/env bash
    set -euo pipefail
    old="{{OLD}}"
    new="{{NEW}}"
    export old new
    # Skip the Quarto project root: every part of the book appears there a
    # second time, as a symlink, and rewriting through both would double-apply.
    mapfile -t files < <(find writing -name '*.md' -not -path 'writing/.book/*')
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
        echo "docs-rename-ref: docs gate FAILED after rename; inspect the report, then revert the rewrite yourself" >&2
        exit 1
    fi

# Add an nLab citation to writing/.assets/refs-web.bib by scraping its canonical /cite page
cite-nlab page:
    python3 scripts/cite_add.py nlab "{{page}}"

# Verify a Stacks Project tag resolves (cite as [@stacks-TAG]; links via the global The25 entry)
cite-stacks tag:
    python3 scripts/cite_add.py stacks "{{tag}}"

# Regenerate writing/.assets/refs-web.bib from canonical sources (re-scrapes every nLab entry; hand-edits are lost)
refs-web-refresh:
    python3 scripts/refs_web_refresh.py

# Regenerate the interactive category graph from its DOT manifest (writing/category-theory/lean/category-graph.dot)
graph:
    python3 scripts/build_graph.py

# Regenerate the Sage category inventory pages from the tracked audit data under writing/data/. Rewrites docs/sage-inventory/inventory/ wholesale; edit the data or the generator, never the pages.
sage-inventory:
    python3 scripts/build_sage_inventory_site.py

# Serve the docs site locally with live reload (quarto provisioned via uvx)
docs-preview: docs-assets
    #!/usr/bin/env bash
    set -euo pipefail
    # ponytail: two previews on the same dir cross-trigger each other's watchers
    # (each renders output back into the project) → endless ~10s reload loop. Kill
    # any stale instance first so this always replaces rather than duplicates.
    # A preview left over from an earlier layout also holds the port, so match
    # any quarto preview rather than only one on the current directory.
    pkill -f 'quarto preview' || true
    for _ in $(seq 25); do
        ss -ltn 'sport = :7654' | grep -q ':7654' || break
        sleep 0.2
    done
    # The project root is writing/.book; it symlinks the prose in from writing/.
    uvx --from quarto-cli quarto preview writing/.book --no-browser --port 7654

# Survey a live session into the preamble reference, its graph JSON, and the interactive graph
preamble-megadoc:
    # The survey imports the preamble, so it runs under Sage's Python, which the
    # global QC resolves.
    PYTHONPATH=src "$(just -f ~/ai-review-ci/justfiles/sage.just -d . _sage-python)" \
        -m dzack_research.utilities.megadoc -o "{{preamble_megadoc_file}}"
    # Leave the reference in the form the commit gate's Markdown formatter
    # writes, so a regenerated file stages unchanged.
    uvx --from 'git+https://github.com/dzackgarza/flowmark.git' flowmark \
        --inplace --nobackup --semantic "{{preamble_megadoc_file}}"

# Slice a saved live category survey by category, direction, interval or method (--help)
[positional-arguments]
placement *categories:
    PYTHONPATH=src python3 -m dzack_research.utilities.placement "$@"

# Every declared category and its declared supercategories, read from source
# without importing it -- so it answers on a tree that does not currently load.
# Inspect declared categories: table, json, slice, audit, shape, cells or topology (--help)
[positional-arguments]
category-graph format="table" *args:
    @case "$1" in audit|shape|cells|topology) inspection_python="$(just -f ~/ai-review-ci/justfiles/sage.just -d . _sage-python)" ;; *) inspection_python=python3 ;; esac; inspection_format="$1"; shift; PYTHONPATH=src "$inspection_python" -m dzack_research.utilities.category_graph --format "$inspection_format" "$@"

# Every category's operations, input category -> output category: traced from source, else read from the returned value's class
category-constructions *args:
    mkdir -p .tmp
    PYTHONPATH=src "$(just -f ~/ai-review-ci/justfiles/sage.just -d . _sage-python)" \
        -m dzack_research.utilities.category_inference -o .tmp/category-inference.json
    just category-graph constructions --inferred .tmp/category-inference.json {{args}}

# Full typed construction grammar: all category/axiom nodes, operation input
# ports, guarded source-level result alternatives, recursive closure, and
# unresolved paths. Pure Python source analysis; no Sage or mathematical tests.
# Open the generated HTML locally; JSON is suitable for machine review.
construction-universe out=".tmp" depth="6":
    mkdir -p "{{out}}"
    PYTHONPATH=src python3 -m dzack_research.utilities.construction_universe \
        --depth "{{depth}}" --json "{{out}}/construction-universe.json" \
        --html "{{out}}/construction-universe.html"
    @echo "Audit browser: {{out}}/construction-universe.html"

# Enumerate candidate type constructions and recursive method-result reachability.
# Pure source analysis: does not execute the preamble or establish mathematical
# correctness. Unresolved outcomes and parameter obligations remain explicit.
[positional-arguments]
category-universe output=".tmp/construction-closure":
    PYTHONPATH=src python3 -m dzack_research.utilities.construction_closure --output "{{output}}"

# The declared category graph as a rendered image, for reading the shape of it
category-graph-svg:
    just category-graph dot > docs/declared-category-graph.dot
    dot -Tsvg docs/declared-category-graph.dot -o docs/declared-category-graph.svg
    @echo "wrote docs/declared-category-graph.svg"

# Intra-package imports that name nothing their module binds, read from source
preamble-imports:
    PYTHONPATH=src python3 -m dzack_research.utilities.import_audit src/dzack_research

# Static architecture/complexity inventory for the live preamble
preamble-complexity:
    PYTHONPATH=src "$(just -f ~/ai-review-ci/justfiles/sage.just -d . _sage-python)" -m dzack_research.utilities.complexity_analysis

# Index Python symbols for navigation; json emits scoped symbols to stdout
[positional-arguments]
tags format="tags" root="src":
    @case "$1" in tags) ctags -R --languages=Python -f tags "$2" ;; json) ctags -R --languages=Python --output-format=json --fields=+n --extras=+q "$2" ;; *) echo 'format must be tags or json' >&2; exit 2 ;; esac

# Link sage-init.sage as Sage's startup file (${DOT_SAGE:-~/.sage}/init.sage), giving every Sage process — terminal REPL and every Jupyter kernel — implicit LaTeX rendering of cell results. Idempotent, and refuses to replace anything it did not create.
sage-init-install: _sage-plain-kernel
    #!/usr/bin/env bash
    set -euo pipefail
    source="{{justfile_directory()}}/sage-init.sage"
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

# _sage-plain-kernel: the "SageMath (no preamble)" Jupyter kernel for the
# notebooks under computations/notebooks/base-sage. It is the sagemath kernel
# with SAGE_STARTUP_FILE pointed at an empty file, so sage-init.sage and the
# preamble are never loaded.
[private]
_sage-plain-kernel:
    #!/usr/bin/env bash
    set -euo pipefail
    kernels="${JUPYTER_DATA_DIR:-$HOME/.local/share/jupyter}/kernels"
    mkdir -p "${kernels}/sagemath-plain"
    jq '.display_name = "SageMath (no preamble)" | .env = {"SAGE_STARTUP_FILE": "/dev/null"}' \
        "${kernels}/sagemath/kernel.json" > "${kernels}/sagemath-plain/kernel.json"
    echo "sage-init-install: kernel sagemath-plain at ${kernels}/sagemath-plain"

# Prove the installed startup file actually typesets in a real Sage kernel
sage-init-check: sage-init-install
    #!/usr/bin/env bash
    set -euo pipefail
    # Through ``sage -c``, which is the only way this Sage runs code: the CLI
    # has no ``--python``.  The probe is written out first because ``-c`` reads
    # trailing words as more code.
    probe="$(mktemp --suffix=.py)"
    trap 'gio trash "${probe}" 2>/dev/null || true' EXIT
    cat > "${probe}" <<'PY'
    import os
    from pathlib import Path

    from jupyter_client.manager import start_new_kernel
    from sage.env import SAGE_STARTUP_FILE

    expected_startup = Path("{{justfile_directory()}}/sage-init.sage").resolve()
    assert Path(SAGE_STARTUP_FILE).resolve() == expected_startup, (
        f"installed Sage startup resolves to {Path(SAGE_STARTUP_FILE).resolve()}, "
        f"expected {expected_startup}"
    )

    km, kc = start_new_kernel(kernel_name="sagemath", env=os.environ.copy())
    try:
        results = {}
        # The rule under test is that an ordinary fresh Sage Jupyter kernel uses
        # the installed startup link, imports preamble.all into its user scope,
        # and installs the implicit typesetter without any test-only env override.
        namespace = {"stdout": ""}

        def capture_namespace(message):
            if message["msg_type"] == "stream":
                namespace["stdout"] += message["content"]["text"]

        kc.execute_interactive(
            "import sys; print('preamble=' + str('dzack_research.preamble.all' in sys.modules)); "
            "print('Cat=' + str('Cat' in globals())); print('Lattices=' + str('Lattices' in globals()))",
            timeout=180,
            output_hook=capture_namespace,
        )
        stdout = namespace["stdout"]
        assert "preamble=True" in stdout, "fresh Sage kernel did not import dzack_research.preamble.all"
        assert "Cat=True" in stdout and "Lattices=True" in stdout, "research preamble names are absent from fresh Sage kernel"
        for label, code in [("typeset", "Lattices(ZZ)('A2')"), ("plain", "'a plain string'")]:
            got = {}
            kc.execute_interactive(
                code, timeout=180,
                output_hook=lambda m: got.update(m["content"]["data"])
                if m["msg_type"] in ("execute_result", "display_data") else None)
            results[label] = got
        assert results["typeset"].get("text/latex"), "Sage object did not render as LaTeX"
        assert not results["plain"].get("text/latex"), "plain string was typeset; it should not be"
        print("sage-init-check: ok — fresh Jupyter kernel imported preamble.all and typesets Sage objects")
    finally:
        kc.stop_channels()
        km.shutdown_kernel()
    PY
    "$(just --evaluate sage_bin 2>/dev/null || echo "${SAGE_BIN:-sage}")" \
        -c "exec(open('${probe}').read())"

# Rebuild the Sage-owned research environment.
sage-rebuild:
    #!/usr/bin/env bash
    set -euo pipefail
    sage_root="${SAGE_DEV_ROOT:-/home/dzack/gitclones/sage-dev-allopts}"
    just --justfile "${sage_root}/justfile" research-environment-sync

[private]
_lock:
    uv lock

# Development commits inspect staged source syntax only.
test-commit:
    @just -f ~/ai-review-ci/justfiles/sage.just -d . test-commit

# No full-tree scan, test suite, or site deployment on the publication path.
test-push:
    @just -f ~/ai-review-ci/justfiles/sage.just -d . test-push

# Run the CI suites.
test-ci:
    @just -f ~/ai-review-ci/justfiles/sage.just -d . test-ci

# The scheduled whole-tree audit.
ambient:
    @just -f ~/ai-review-ci/justfiles/sage.just -d . ambient

# Survey an operation before changing what it returns or renaming it.
# Reports every definition with its owner and return expressions, flags
# divergent codomains (CONTRIBUTING.md LEX-11), and censuses the call sites by
# syntactic shape, which is the plan for the change (DEF-07, CON-15).
#   just refactor-survey signature_pair
#   just refactor-survey tensor_valence tensor_shape
# Inspect definitions, callers, constructors, private accesses or duplicate bodies (--help)
[positional-arguments]
refactor-survey *args:
    PYTHONPATH=src python3 -m dzack_research.utilities.refactor_survey "$@"

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

    This repository is a mathematical research monorepo. The former
    preamble lives under `archives/preamble/` and is not a live surface.
    Reviews here are advisory: they feed a triage ledger and never block
    work. An
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

# Sterk formalization: link authored files into the Prove2Me workspace and check
# that every proved solution rests on Lean's three standard axioms.
sterk-link workspace=(justfile_directory() / "formalization/prove2me_workspace"):
    #!/usr/bin/env bash
    set -euo pipefail
    src="{{justfile_directory()}}/formalization/sterk-enriques"
    for d in Definitions Theorems Solutions; do
        mkdir -p "{{workspace}}/$d"
        shopt -s nullglob
        for f in "$src/$d"/*.lean; do
            ln -sfn "$f" "{{workspace}}/$d/$(basename "$f")"
        done
    done
    echo "linked into {{workspace}}"

sterk-check workspace=(justfile_directory() / "formalization/prove2me_workspace"):
    @formalization/sterk-enriques/verification/check_axioms.sh {{workspace}}

