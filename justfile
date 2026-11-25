
ai_review_ci_schema_version := "1"
ai_review_ci_profile := "sage"
ai_review_ci_ref := "main"
ai_review_ci_release_channel := "main"
ai_review_ci_workflow_template_version := "1"
ai_review_ci_local_delegation := "global-justfile"
ai_review_ci_default_branch := "main"
preamble_megadoc_file := "docs/preamble-megadoc.md"

[doc("List available recipes")]
default:
    @just --list

[doc("Preview the interactive Serre spectral sequence article")]
serre-preview port="4193":
    @echo 'http://127.0.0.1:{{port}}/examples/serre/'
    @python3 -m http.server '{{port}}' --bind 127.0.0.1 --directory widgets/spectral-sequence-viewer

[doc("Build the installable Sage research distribution")]
build: _lock
    uv build

[doc("Refresh the docs bibliography and MathJax macro include from the shared ~/.pandoc sources (never frozen in-repo; CI fetches them from the pandoc-config repo). The macros are the generated corpus: the book defines none of its own.")]
docs-assets:
    cp --remove-destination ~/.pandoc/bib/references.bib writing/.assets/references.bib
    cp --remove-destination ~/.pandoc/templates/css/mathjax-macros.html writing/.assets/mathjax-macros.html
    python3 scripts/docs_figures.py

[doc("Rebuild the book and refresh the local static copy at http://lattice-research.localhost/")]
docs-deploy: docs-check
    @just docs-publish

[doc("Publish the finished render. nginx serves /var/www/static-sites/lattice-research for lattice-research.localhost. Quarto empties writing/.book/_site when any render starts, so the served link never points at _site: a stopped, failed or one-page render would take the site down. This copies _site to a new release directory and switches the link to it with one rename, so the site is always a complete, gated render. The previous release is kept and older ones are trashed. Copy the finished render to a release directory and switch the served site to it")]
docs-publish:
    #!/usr/bin/env bash
    set -euo pipefail
    site="$(pwd)/writing/.book/_site"
    releases="$(pwd)/writing/.book/.releases"
    link=/var/www/static-sites/lattice-research
    [ -f "$site/index.html" ] || { echo "docs-publish: $site has no index.html" >&2; exit 1; }
    mkdir -p "$releases"
    new="$releases/$(date +%Y%m%dT%H%M%S)-$(git rev-parse --short HEAD)"
    cp -a "$site" "$new"
    ln -sfn "$new" "$link.next"
    mv -T "$link.next" "$link"
    code=$(curl -s -o /dev/null -w '%{http_code}' -H 'Host: lattice-research.localhost' http://127.0.0.1/)
    [ "$code" = 200 ] || { echo "docs-publish: nginx answered $code for lattice-research.localhost" >&2; exit 1; }
    ls -1d "$releases"/*/ | head -n -2 | while read -r old; do trash "$old"; done
    echo "docs-publish: http://lattice-research.localhost/ is serving $(find "$new" -name '*.html' | wc -l) pages from $new"

[doc("Full gate, the build CI runs on every push: render the docs book twice and fail on undefined citations, unresolved cross-refs, broken anchor links, or dead external links")]
docs-check: docs-assets
    python3 scripts/docs_check.py

[doc("Dependency graph of the book's numbered blocks (edges = @refs in a statement or its proof), written to .tmp/dependency-graph; fails on circular definitions or proofs, orphan proofs, blocks without ids, defined terms used without a citation and pandoc parse warnings")]
docs-deps:
    cd writing/.book && uv run --script ../../scripts/docs_dependency_graph.py --project . --out ../../.tmp/dependency-graph --check

[doc("Query the book's structure (blocks, headings, citations, uses); any subcommand of scripts/docs_query.py. e.g. `just book list --kind theorem --chapter coble`, `just book deps thm:foo --depth 2`. The index is cached in .tmp/docs-query and rebuilt when a chapter changes.")]
[positional-arguments]
book *ARGS:
    @PYTHONWARNINGS=ignore::SyntaxWarning HF_HUB_DISABLE_PROGRESS_BARS=1 TRANSFORMERS_VERBOSITY=error uv run --quiet --script scripts/docs_query.py --cache .tmp/docs-query/index.pickle "$@"

[doc("List the numbered blocks of the given kinds in reading order (no kind: every block), with id, file:line and title. e.g. `just book-blocks definition notation`")]
book-blocks *KINDS:
    @just book list {{ if KINDS == "" { "" } else { "--kind " + KINDS } }}

[doc("List the block ids of the given kinds, one per line (no kind: every id)")]
book-ids *KINDS:
    @just book list --ids {{ if KINDS == "" { "" } else { "--kind " + KINDS } }}

[doc("Print the source of blocks with their proofs. e.g. `just book-show def:universe thm:foo`")]
book-show +IDS:
    @just book show {{IDS}}

[doc("Print the heading tree of the book (or of chapters whose path contains FILTER), with the numbered blocks under each heading")]
book-tree FILTER="":
    @just book tree --blocks {{FILTER}}

[doc("Print only the headings of the book (or of chapters whose path contains FILTER), down to level DEPTH")]
book-toc FILTER="" DEPTH="3":
    @just book tree --depth {{DEPTH}} {{FILTER}}

[doc("Search the blocks by meaning and by words (txtai hybrid index of titles, defined terms, statements and proofs). e.g. `just book-search lattices whose discriminant group is 2-elementary`")]
book-search +QUERY:
    @just book search "{{QUERY}}"

[doc("Find the definition, construction, notation or convention for a notion, by meaning and by words. e.g. `just book-term discriminant form`")]
book-term +QUERY:
    @just book term "{{QUERY}}"

[doc("Locate every @KEY (bibliography key or block id): file:line, enclosing block, statement or proof, locator and section; for a bibliography key, also each cited result and its users")]
book-where KEY:
    @just book where {{KEY}}

[doc("Print the blocks and cited results that block ID uses, transitively, as a tree")]
book-uses ID DEPTH="":
    @just book deps {{ID}} {{ if DEPTH == "" { "" } else { "--depth " + DEPTH } }}

[doc("Print the blocks that use block ID, transitively, as a tree")]
book-used-by ID DEPTH="":
    @just book deps {{ID}} --reverse {{ if DEPTH == "" { "" } else { "--depth " + DEPTH } }}

[doc("Print a shortest chain of uses from block SOURCE down to block TARGET")]
book-path SOURCE TARGET:
    @just book path {{SOURCE}} {{TARGET}}

[doc("Render the uses-neighbourhood of block ID (both directions, DEPTH steps) to .tmp/docs-query/<ID>.svg")]
book-graph ID DEPTH="2":
    #!/usr/bin/env bash
    set -euo pipefail
    out=".tmp/docs-query/$(echo '{{ID}}' | tr -c '[:alnum:]-\n' '_').svg"
    just book graph '{{ID}}' --depth {{DEPTH}} --both | dot -Tsvg -o "$out"
    echo "$out"

[doc("List theorems, lemmas, propositions, corollaries, observations and claims that have no proof after them")]
book-unproved:
    @just book list --unproved

[doc("List logical blocks that no logical block uses")]
book-unused:
    @just book list --unused

[doc("Count the numbered blocks by kind and part of the book")]
book-stats:
    @just book stats

[doc("Every citation that names no result (a whole work, a chapter, a section, a page), in statements, proofs and prose, with its sentence and block, grouped by work; read each and keep it as attribution or tighten it to the result it uses. Report: .tmp/citation-audit.md")]
docs-citation-audit:
    cd writing/.book && uv run --script ../../scripts/docs_citation_audit.py --project . --out ../../.tmp/citation-audit.md

[doc("Local check in seconds: the gate's source checks over the whole book (citation keys, cross-references, path links, heading numbers, inline citation URLs, theorem references), then one page rendered for tikz and markdown syntax errors. e.g. `just docs-lint coble/index.md`")]
docs-lint FILE: docs-assets
    python3 scripts/docs_check.py --source
    cd writing/.book && uvx --from quarto-cli quarto render "{{FILE}}" --to html

[doc("Rename a docs cross-reference/anchor slug everywhere, then prove every reference still resolves. Rewrites {#slug} anchors, @slug crossrefs, and ](…#slug) link fragments in one hyphen-boundary-safe pass (a longer slug is never partially hit) and runs the docs gate. e.g. `just docs-rename-ref def-old-name def-new-name`")]
docs-rename-ref OLD NEW:
    #!/usr/bin/env bash
    set -euo pipefail
    old="{{OLD}}"
    new="{{NEW}}"
    export old new
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

[doc("Add an nLab citation to writing/.assets/refs-web.bib by scraping its canonical /cite page")]
cite-nlab page:
    python3 scripts/cite_add.py nlab "{{page}}"

[doc("Verify a Stacks Project tag resolves (cite as [@stacks-TAG]; links via the global The25 entry)")]
cite-stacks tag:
    python3 scripts/cite_add.py stacks "{{tag}}"

[doc("Regenerate writing/.assets/refs-web.bib from canonical sources (re-scrapes every nLab entry; hand-edits are lost)")]
refs-web-refresh:
    python3 scripts/refs_web_refresh.py

[doc("Regenerate the interactive category graph from its DOT manifest (writing/category-theory/lean/category-graph.dot)")]
graph:
    python3 scripts/build_graph.py

[doc("Regenerate the Sage category inventory pages from the tracked audit data under writing/data/. Rewrites docs/sage-inventory/inventory/ wholesale; edit the data or the generator, never the pages.")]
sage-inventory:
    python3 scripts/build_sage_inventory_site.py

[doc("Serve the docs site locally with live reload (quarto provisioned via uvx)")]
docs-preview: docs-assets
    #!/usr/bin/env bash
    set -euo pipefail
    pkill -f 'quarto preview' || true
    for _ in $(seq 25); do
        ss -ltn 'sport = :7654' | grep -q ':7654' || break
        sleep 0.2
    done
    uvx --from quarto-cli quarto preview writing/.book --no-browser --port 7654

[doc("Survey a live session into the preamble reference, its graph JSON, and the interactive graph")]
preamble-megadoc:
    PYTHONPATH=src "$(just -f ~/ai-review-ci/justfiles/sage.just -d . _sage-python)" \
        -m dzack_research.utilities.megadoc -o "{{preamble_megadoc_file}}"
    uvx --from 'git+https://github.com/dzackgarza/flowmark.git' flowmark \
        --inplace --nobackup --semantic "{{preamble_megadoc_file}}"

[doc("Slice a saved live category survey by category, direction, interval or method (--help)")]
[positional-arguments]
placement *categories:
    PYTHONPATH=src python3 -m dzack_research.utilities.placement "$@"

[doc("Every declared category and its declared supercategories, read from source without importing it -- so it answers on a tree that does not currently load. Inspect declared categories: table, json, slice, audit, shape, cells or topology (--help)")]
[positional-arguments]
category-graph format="table" *args:
    @case "$1" in audit|shape|cells|topology) inspection_python="$(just -f ~/ai-review-ci/justfiles/sage.just -d . _sage-python)" ;; *) inspection_python=python3 ;; esac; inspection_format="$1"; shift; PYTHONPATH=src "$inspection_python" -m dzack_research.utilities.category_graph --format "$inspection_format" "$@"

[doc("Every category's operations, input category -> output category: traced from source, else read from the returned value's class")]
category-constructions *args:
    mkdir -p .tmp
    PYTHONPATH=src "$(just -f ~/ai-review-ci/justfiles/sage.just -d . _sage-python)" \
        -m dzack_research.utilities.category_inference -o .tmp/category-inference.json
    just category-graph constructions --inferred .tmp/category-inference.json {{args}}

[doc("Full typed construction grammar: all category/axiom nodes, operation input ports, guarded source-level result alternatives, recursive closure, and unresolved paths. Pure Python source analysis; no Sage or mathematical tests. Open the generated HTML locally; JSON is suitable for machine review.")]
construction-universe out=".tmp" depth="6":
    mkdir -p "{{out}}"
    PYTHONPATH=src python3 -m dzack_research.utilities.construction_universe \
        --depth "{{depth}}" --json "{{out}}/construction-universe.json" \
        --html "{{out}}/construction-universe.html"
    @echo "Audit browser: {{out}}/construction-universe.html"

[doc("Enumerate candidate type constructions and recursive method-result reachability. Pure source analysis: does not execute the preamble or establish mathematical correctness. Unresolved outcomes and parameter obligations remain explicit.")]
[positional-arguments]
category-universe output=".tmp/construction-closure":
    PYTHONPATH=src python3 -m dzack_research.utilities.construction_closure --output "{{output}}"

[doc("The declared category graph as a rendered image, for reading the shape of it")]
category-graph-svg:
    just category-graph dot > docs/declared-category-graph.dot
    dot -Tsvg docs/declared-category-graph.dot -o docs/declared-category-graph.svg
    @echo "wrote docs/declared-category-graph.svg"

[doc("Intra-package imports that name nothing their module binds, read from source")]
preamble-imports:
    PYTHONPATH=src python3 -m dzack_research.utilities.import_audit src/dzack_research

[doc("Static architecture/complexity inventory for the live preamble")]
preamble-complexity:
    PYTHONPATH=src "$(just -f ~/ai-review-ci/justfiles/sage.just -d . _sage-python)" -m dzack_research.utilities.complexity_analysis

[doc("Index Python symbols for navigation; json emits scoped symbols to stdout")]
[positional-arguments]
tags format="tags" root="src":
    @case "$1" in tags) ctags -R --languages=Python -f tags "$2" ;; json) ctags -R --languages=Python --output-format=json --fields=+n --extras=+q "$2" ;; *) echo 'format must be tags or json' >&2; exit 2 ;; esac

[doc("Link sage-init.sage as Sage's startup file (${DOT_SAGE:-~/.sage}/init.sage), giving every Sage process — terminal REPL and every Jupyter kernel — implicit LaTeX rendering of cell results. Idempotent, and refuses to replace anything it did not create.")]
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

[doc('_sage-plain-kernel: the "SageMath (no preamble)" Jupyter kernel for the notebooks under computations/notebooks/base-sage. It is the sagemath kernel with SAGE_STARTUP_FILE pointed at an empty file, so sage-init.sage and the preamble are never loaded.')]
[private]
_sage-plain-kernel:
    #!/usr/bin/env bash
    set -euo pipefail
    kernels="${JUPYTER_DATA_DIR:-$HOME/.local/share/jupyter}/kernels"
    mkdir -p "${kernels}/sagemath-plain"
    jq '.display_name = "SageMath (no preamble)" | .env = {"SAGE_STARTUP_FILE": "/dev/null"}' \
        "${kernels}/sagemath/kernel.json" > "${kernels}/sagemath-plain/kernel.json"
    echo "sage-init-install: kernel sagemath-plain at ${kernels}/sagemath-plain"

[doc("Prove the installed startup file actually typesets in a real Sage kernel")]
sage-init-check: sage-init-install
    #!/usr/bin/env bash
    set -euo pipefail
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
    "$(just -f ~/ai-review-ci/justfiles/sage.just -d . _sage-python)" \
        -c "exec(open('${probe}').read())"

[doc("Rebuild the Sage-owned research environment.")]
sage-rebuild:
    #!/usr/bin/env bash
    set -euo pipefail
    sage_root="${SAGE_DEV_ROOT:-/home/dzack/gitclones/sage-dev-allopts}"
    just --justfile "${sage_root}/justfile" research-environment-sync

[private]
_lock:
    uv lock

[doc("Development commits inspect staged source syntax only.")]
test-commit:
    @just -f ~/ai-review-ci/justfiles/sage.just -d . test-commit

[doc("No full-tree scan, test suite, or site deployment on the publication path.")]
test-push:
    @just -f ~/ai-review-ci/justfiles/sage.just -d . test-push

[doc("Run the CI suites.")]
test-ci:
    @just -f ~/ai-review-ci/justfiles/sage.just -d . test-ci

[doc("The scheduled whole-tree audit.")]
ambient:
    @just -f ~/ai-review-ci/justfiles/sage.just -d . ambient

[doc("Survey an operation before changing what it returns or renaming it. Reports every definition with its owner and return expressions, flags divergent codomains (CONTRIBUTING.md LEX-11), and censuses the call sites by syntactic shape, which is the plan for the change (DEF-07, CON-15). just refactor-survey signature_pair just refactor-survey tensor_valence tensor_shape Inspect definitions, callers, constructors, private accesses or duplicate bodies (--help)")]
[positional-arguments]
refactor-survey *args:
    PYTHONPATH=src python3 -m dzack_research.utilities.refactor_survey "$@"

[doc("Assemble the LLM-review context packet (review-packet.tar). The packet is the extensible context surface for the advisory review workflows (.github/workflows/review-*.yml): a PROMPT.md plus whatever reference documents the reviews should be sensitive to, organized below. Only the tar is tracked — the exploded tree exists solely for the CI reviewer, which unpacks it into .review-context/ and inlines PROMPT.md and every packet *.md into the reviewer prompt. Sources may be untracked in this repo (e.g. vault memory files reached through the .agents symlink); assembling locally is what makes them available to CI. To change review context: edit the declaration below, run `just review-packet`, and commit the tar. The archive is byte-deterministic, so git sees a change only when content changed.")]
review-packet:
    #!/usr/bin/env bash
    set -euo pipefail
    staging="$(mktemp -d)"
    trap 'rm -rf "$staging"' EXIT

    cat > "$staging/PROMPT.md" <<'PROMPT'

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

    for section in decisions traps advice context; do
        mkdir -p "$staging/vault/$section"
        cp .agents/"$section"/*.md "$staging/vault/$section/"
    done

    tar --sort=name --owner=0 --group=0 --numeric-owner \
        --mtime='UTC 2020-01-01' --format=gnu \
        -cf review-packet.tar -C "$staging" .
    echo "review-packet.tar: $(tar -tf review-packet.tar | grep -c -v '/$') files"

[doc("Sterk formalization: link the authored Lean files into the Prove2Me workspace.")]
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

[doc("Sterk formalization: check that every proved solution in the Prove2Me workspace rests only on the three standard Lean axioms.")]
sterk-check workspace=(justfile_directory() / "formalization/prove2me_workspace"):
    @formalization/sterk-enriques/verification/check_axioms.sh {{workspace}}

