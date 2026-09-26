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

# Experimental Pyrefly semantic contracts for the Sage mathematical API
semantic-types:
    uv run pyrefly check -c pyrefly-semantic.toml typing_tests/positive.py
    @if uv run pyrefly check -c pyrefly-semantic.toml typing_tests/negative.py >/tmp/research-pyrefly-negative.log 2>&1; then \
        cat /tmp/research-pyrefly-negative.log; \
        echo "negative semantic typing corpus unexpectedly type-checks" >&2; \
        rm -f /tmp/research-pyrefly-negative.log; \
        exit 1; \
    fi
    @cat /tmp/research-pyrefly-negative.log
    @rm -f /tmp/research-pyrefly-negative.log

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

# The CAT-05 placement worksheet: each category's introduced object, element and
# arrow operations against its up-set U_C, with the mechanical findings.  Reads
# docs/preamble-graph.json; run `just preamble-megadoc` first when it is stale.
placement *categories:
    PYTHONPATH=src python3 -m dzack_research.utilities.placement {{categories}}

# Every declared category and its declared supercategories, read from source
# without importing it -- so it answers on a tree that does not currently load.
# FORMAT: table (default), by-supercategory, foreign, audit, shape, cells, dot, json.
category-graph format="table":
    # The graph theory is Sage's, so it runs under Sage's Python as
    # `preamble-megadoc` does.
    PYTHONPATH=src "$(just -f ~/ai-review-ci/justfiles/sage.just -d . _sage-python)" \
        -m dzack_research.utilities.category_graph --format {{format}}

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
    PYTHONPATH=src python3 -m dzack_research.utilities.complexity_analysis src/dzack_research/preamble

# Generate a ctags index for the installable package source
tags:
    ctags -R --languages=Python -f tags src

# Link sage-init.sage as Sage's startup file (${DOT_SAGE:-~/.sage}/init.sage), giving every Sage process — terminal REPL and every Jupyter kernel — implicit LaTeX rendering of cell results. Idempotent, and refuses to replace anything it did not create.
sage-init-install:
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

# Run commit-tier SageMath QC through the central implementation
test-commit:
    @just -f ~/ai-review-ci/justfiles/sage.just -d . test-commit

# Run push-tier SageMath QC through the central implementation
test-push:
    #!/usr/bin/env bash
    set -euo pipefail
    just -f ~/ai-review-ci/justfiles/sage.just -d . test-push
    # A push that changes the book refreshes what lattice-research.localhost serves.
    # The push gate itself is machine-wide and owns none of this; the deploy belongs
    # to the repo that owns the book, which is why it hangs off this recipe.
    if ! git diff --quiet "@{upstream}" -- writing 2>/dev/null; then
        just docs-deploy
    fi

# Run CI acceptance QC through the central implementation
test-ci:
    @just -f ~/ai-review-ci/justfiles/sage.just -d . test-ci

# The suite runs in parallel, one Sage process per worker, and records which
# test ran each line; only lines a passing test ran count as covered.
# Every preamble line and branch no passing test runs, file by file
coverage workers="6":
    #!/usr/bin/env bash
    set -euo pipefail
    qc=~/ai-review-ci/justfiles/sage.just
    # tests/ is the suite for src/; computation scripts elsewhere are not.
    mapfile -t tests < <(just -f "$qc" -d . _sage-test-files; just -f "$qc" -d . _sage-python-test-files)
    mapfile -t tests < <(printf '%s\n' "${tests[@]}" | grep '^tests/')
    out=.tmp/coverage
    mkdir -p "$out"
    for old in "$out"/*.jsonl; do if [ -e "$old" ]; then gio trash "$old"; fi; done
    touch "$out/measured-at"
    # Work stealing rebalances the few long tests across idle workers.
    status=0
    just _coverage-pytest "$out/.coverage" "$out/run.jsonl" -n {{workers}} --dist worksteal "${tests[@]}" || status=$?
    just coverage-report
    echo "pytest exit status: $status"

# Use it while writing tests against a gap the full run reported; it costs
# the named tests, not the suite.
# Add the named tests to the last full run; report the preamble files they reach
[positional-arguments]
coverage-add +tests:
    #!/usr/bin/env bash
    set -euo pipefail
    out=.tmp/coverage
    if [ ! -e "$out/.coverage" ]; then echo "no full run to add to: run just coverage first"; exit 1; fi
    sage_python="$(just -f ~/ai-review-ci/justfiles/sage.just -d . _sage-python)"
    run="$(date +%s%N)"
    status=0
    # Many tests share out across workers; a few run in one process, sparing the worker startups.
    parallel=(); if [ "$#" -gt 50 ]; then parallel=(-n 6 --dist worksteal); fi
    just _coverage-pytest "$out/.coverage.add-$run" "$out/add-$run.jsonl" "${parallel[@]}" "$@" || status=$?
    # Several sessions may add at once; the lock serializes the merge and the report.
    flock "$out/.lock" "$sage_python" -m coverage combine --keep --append \
        --data-file="$out/.coverage" "$out/.coverage.add-$run"
    flock "$out/.lock" "$sage_python" -m dzack_research.utilities.coverage_gaps \
        --touched-by "$out/.coverage.add-$run"
    gio trash "$out/.coverage.add-$run"
    echo "pytest exit status: $status"

# The stored data records which tests ran each preamble file, so after an edit
# only those tests, and the edited test files, run again.
# Remeasure what edits since the last measurement reach, then report
coverage-update:
    #!/usr/bin/env bash
    set -euo pipefail
    out=.tmp/coverage
    if [ ! -e "$out/.coverage" ]; then echo "nothing measured yet: run just coverage first"; exit 1; fi
    sage_python="$(just -f ~/ai-review-ci/justfiles/sage.just -d . _sage-python)"
    mapfile -t tests < <(flock "$out/.lock" "$sage_python" -m dzack_research.utilities.coverage_gaps --select-affected)
    # A purged file whose lines only the import runs is remeasured by collection alone.
    if [ "${#tests[@]}" -eq 0 ]; then
        just coverage-add --collect-only tests/conftest.py > /dev/null
        just coverage-report
        exit 0
    fi
    echo "rerunning ${#tests[@]} tests reached by the edits"
    just coverage-add "${tests[@]}"

# The coverage recorded so far, for the preamble or for the source paths matching globs such as '*/schemes/*'
[positional-arguments]
coverage-report *include:
    #!/usr/bin/env bash
    set -euo pipefail
    select=(); if [ "$#" -gt 0 ]; then select=(--include "$@"); fi
    "$(just -f ~/ai-review-ci/justfiles/sage.just -d . _sage-python)" -m dzack_research.utilities.coverage_gaps "${select[@]}"

# The specification subtrees are red until the preamble meets them, so a
# failing suite still yields its coverage; the caller reports the exit status.
# No per-test timeout: its SIGALRM inside Cython ends the whole run (TRAPS.md),
# and coverage's tracing makes the time gates meaningless.  One-line
# tracebacks keep failure reports from computing owned reprs.
[positional-arguments]
_coverage-pytest data log *args:
    #!/usr/bin/env bash
    set -euo pipefail
    export PYTHONPATH="$HOME/ai-review-ci/tool-artifacts/pytest_plugins${PYTHONPATH:+:$PYTHONPATH}"
    export COVERAGE_FILE="$1"
    log="$2"
    shift 2
    "$(just -f ~/ai-review-ci/justfiles/sage.just -d . _sage-python)" -m pytest -p qc_sage_session \
        -q --no-time-gates --timeout=0 --tb=line --report-log="$log" \
        --cov=src/dzack_research/preamble --cov-branch --cov-context=test --cov-report= \
        "$@"

# Survey an operation before changing what it returns or renaming it.
# Reports every definition with its owner and return expressions, flags
# divergent codomains (CONTRIBUTING.md LEX-11), and censuses the call sites by
# syntactic shape, which is the plan for the change (DEF-07, CON-15).
#   just refactor-survey signature_pair
#   just refactor-survey "tensor_valence tensor_shape"
refactor-survey names:
    PYTHONPATH=src python3 -m dzack_research.utilities.refactor_survey {{names}}

# Check that the proof surface stays inside the mathematical universe.
# Policies: CONTRIBUTING.md DEV-37 (a test stays inside the universe) and
# DEV-38 (assert the object, not a chosen presentation).
#
# tests/engineering/ is the cordon for tests that prove no mathematics.
# ast-grep matches the syntax tree, so `== (0, 2)` is found wherever it is
# written -- across line breaks, and never inside a string or a docstring.
test-universe:
    #!/usr/bin/env bash
    set -uo pipefail
    files=$(git ls-files 'tests/*.py' 'tests/**/*.py' | grep -v '^tests/engineering/')
    if [ -z "$files" ]; then echo "No mathematical tests to check."; exit 0; fi
    total=0
    count() { ast-grep run --lang python --pattern "$1" --json $files 2>/dev/null \
        | python3 -c 'import json,sys; print(len(json.load(sys.stdin)))'; }
    show()  { ast-grep run --lang python --pattern "$1" $files 2>/dev/null | head -"$2"; }
    check() {
        local policy="$1" why="$2"; shift 2
        local n=0 p
        for p in "$@"; do n=$((n + $(count "$p"))); done
        total=$((total + n))
        printf '%-7s %4d  %s\n' "$policy" "$n" "$why"
        [ "$n" -gt 0 ] && for p in "$@"; do show "$p" 4; done
        return 0
    }
    echo "Checking $(echo "$files" | wc -l) mathematical test files."
    echo
    check DEV-37 'extraction constructor: ask the object, not a Python container' \
        'tuple($$$A)' 'list($$$A)' 'set($$$A)' 'frozenset($$$A)' 'sorted($$$A)'
    check DEV-37 'len() where cardinality() is the mathematical operation' \
        'len($$$A)'
    check DEV-37 'compared against a Python tuple or list display' \
        '$X == ($A, $$$B)' '$X == [$$$B]' '$X != ($A, $$$B)' '$X != [$$$B]'
    check DEV-40 'extraction accessor: state the claim about the owned elements' \
        '$X.to_tuple()' '$X.to_list()' '$X.tolist()' '$X.list()'
    echo
    if [ "$total" -gt 0 ]; then
        echo "$total findings.  Extraction is strictly weaker than comparing the"
        echo "objects: it passes whether or not their own equality is implemented."
        exit 1
    fi
    echo "The proof surface stays inside the universe."

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

# Lint the test tree against the session standard (dzack_research.utilities.test_lint).
# With no paths it lints every test outside the protected specification subtrees.
test-lint *paths:
    sage_launcher="${SAGE_BIN:-$(command -v sage)}"; \
    case "$sage_launcher" in */*) ;; *) sage_launcher="$(command -v "$sage_launcher")" ;; esac; \
    sage_launcher="$(readlink -f "$sage_launcher")"; \
    PYTHONPATH=src "$(dirname "$sage_launcher")/python3" \
        -m dzack_research.utilities.test_lint {{paths}}
