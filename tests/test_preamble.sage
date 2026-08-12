r"""Global tests for ``dzack_research.preamble``.

The modules carry assertions internally, but those only fire when something calls
them -- so without this file nothing exercises the port on a schedule. These are the
checks that would catch a regression in the recovered mathematics, chosen for what
they can *falsify* rather than for coverage:

- the catalogue's named lattices against their defining invariants;
- the Sterk configurations against **Sterk's published norm breakdown**, an external
  oracle independent of how the vectors were transcribed;
- the involutions against the six named lattices, two constructions that never
  touched each other;
- the source's own claim block, which never ran before this port.

``.sage`` because several checks need the preparser and Sage's global namespace.
"""


import types


def _ensure_preamble() -> None:
    """Load the mathematical preamble scripts (not notebook ``init.sage``)."""
    if "Lattices" in globals():
        return
    from pathlib import Path
    import dzack_research

    p = Path(dzack_research.__file__).resolve().parent / "preamble"
    from dzack_research.preamble.install import install_preamble
    install_preamble(globals())
    load(str(p / "sterk.sage"))
    Lattices.install(globals())


def _preamble() -> tuple[types.SimpleNamespace, types.SimpleNamespace, type[Sterk]]:
    """Compatibility shim: (catalogue-ns, legacy-empty-ns, Sterk)."""
    _ensure_preamble()
    catalogue = types.SimpleNamespace(
        Lattices=Lattices,
        Embeddings=Embeddings,
        Involutions=Involutions,
        SterkDiagrams=SterkDiagrams,
        TwoElementary=TwoElementary,
    )
    fixtures = types.SimpleNamespace()
    return catalogue, fixtures, Sterk



def _assert_latex_environments_balanced(rendered: str, name: str) -> None:
    import re

    stack = []
    for action, environment in re.findall(r"\\(begin|end)\{([^{}]+)\}", rendered):
        if action == "begin":
            stack.append(environment)
            continue
        assert stack, (
            f"{name} closes {environment!r} without opening it:\n{rendered}"
        )
        opened = stack.pop()
        assert opened == environment, (
            f"{name} opens {opened!r} but closes {environment!r}:\n{rendered}"
        )
    assert not stack, f"{name} leaves LaTeX environments open: {stack!r}\n{rendered}"


_mathjax_full_root_cached: str | None = None


def _mathjax_full_root() -> str:
    import glob
    import os
    import shutil
    import subprocess
    from pathlib import Path

    global _mathjax_full_root_cached
    if _mathjax_full_root_cached is not None:
        return _mathjax_full_root_cached

    candidates = []
    for env_key in ("MATHJAX_FULL_ROOT", "MATHJAX_PATH"):
        if value := os.environ.get(env_key):
            candidates.append(Path(value).expanduser())

    # common npm / temp install locations used in local dev workflows
    for candidate in glob.glob("/tmp/*/node_modules/mathjax-full"):
        candidates.append(Path(candidate))
    for candidate in glob.glob("/tmp/node_modules/mathjax-full"):
        candidates.append(Path(candidate))

    try:
        npm_root = shutil.which("npm")
        if npm_root:
            proc = subprocess.run(
                ["npm", "root", "-g"],
                check=False,
                capture_output=True,
                text=True,
                timeout=10,
            )
            if proc.returncode == 0:
                candidates.append(Path(proc.stdout.strip()) / "mathjax-full")
    except Exception:
        pass

    for root in candidates:
        if root.name == "mathjax-full":
            full_root = root
        else:
            full_root = root / "mathjax-full"
        if full_root.is_dir() and (full_root / "js" / "mathjax.js").is_file():
            _mathjax_full_root_cached = str(full_root)
            return str(full_root)

    raise AssertionError(
        "No MathJax parser available. Set MATHJAX_FULL_ROOT (or MATHJAX_PATH) to "
        "a mathjax-full package root before running this regression."
    )


def _configured_mathjax_max_buffer() -> int | None:
    import json
    import os
    import re
    import urllib.error
    import urllib.request
    from pathlib import Path

    explicit = (
        os.environ.get("MATHJAX_MAX_BUFFER")
        or os.environ.get("JUPYTER_MATHJAX_MAX_BUFFER")
    )
    if explicit:
        try:
            value = int(explicit)
        except ValueError as err:
            raise AssertionError(
                f"Invalid MathJax maxBuffer override value {explicit!r}: {err}"
            ) from err
        if value > 0:
            return value

    def _read_from_html_config(data: str) -> int | None:
        match = re.search(
            r'<script id="jupyter-config-data" type="application/json">(.*?)</script>',
            data,
            re.S,
        )
        if not match:
            return None
        try:
            config = json.loads(match.group(1))
        except Exception:
            return None
        value = config.get("mathjaxMaxBuffer")
        if isinstance(value, int) and value > 0:
            return value
        return None

    # Prefer the live server configuration that the user actually sees.
    for base_url in (
        os.environ.get("JUPYTERLAB_URL"),
        os.environ.get("JUPYTER_URL"),
        "http://127.0.0.1:8888/lab",
    ):
        if not base_url:
            continue
        for suffix in ("", "/"):
            url = base_url.rstrip("/") + suffix
            try:
                with urllib.request.urlopen(url, timeout=2) as response:
                    body = response.read().decode("utf-8", errors="replace")
            except (OSError, urllib.error.URLError, ValueError):
                continue
            html_value: int | None = _read_from_html_config(body)
            if html_value is not None:
                return html_value

    # Fallback to on-disk config if the lab server is not running.
    raw_paths = (
        os.environ.get("JUPYTER_CONFIG_PATH", "").split(":")
        + [str(Path.home() / ".sage" / "jupyter-4.1")]
    )
    seen = set()
    for config_root in raw_paths:
        if not config_root:
            continue
        config_root = config_root.strip()
        if config_root in seen:
            continue
        seen.add(config_root)

        candidate = Path(config_root) / "labconfig" / "page_config.json"
        if not candidate.is_file():
            continue

        try:
            with candidate.open("r", encoding="utf-8") as stream:
                data = json.load(stream)
        except Exception:
            continue

        value = data.get("mathjaxMaxBuffer")
        if isinstance(value, int) and value > 0:
            return value

    return None


def _assert_latex_renders_in_browser_mathjax(rendered: str, name: str) -> None:
    import subprocess
    import tempfile
    from pathlib import Path

    root = _mathjax_full_root()
    with tempfile.TemporaryDirectory() as tmp:
        input_path = Path(tmp) / "mathjax_input.tex"
        input_path.write_text(rendered, encoding="utf-8")

        script = (
            r"""
            const fs = require('fs');
            const rootPath = process.argv[1];
            const inputFile = process.argv[2];
            const latex = fs.readFileSync(inputFile, 'utf8');
            const {mathjax} = require(rootPath + '/js/mathjax.js');
            const AllPackages = require(rootPath + '/js/input/tex/AllPackages.js');
            const {TeX} = require(rootPath + '/js/input/tex.js');
            const {CHTML} = require(rootPath + '/js/output/chtml.js');
            const {LiteAdaptor} = require(rootPath + '/js/adaptors/liteAdaptor.js');
            const {RegisterHTMLHandler} = require(rootPath + '/js/handlers/html.js');

            const adaptor = new LiteAdaptor();
            RegisterHTMLHandler(adaptor);
            const doc = mathjax.document('', {
              InputJax: new TeX({
                processEnvironments: true,
                packages: (Array.isArray(AllPackages.AllPackages)
                  ? AllPackages.AllPackages
                  : AllPackages).concat('require'),
              }),
              OutputJax: new CHTML({}),
            });

            const html = adaptor.innerHTML(doc.convert(latex));
            const hasRenderedMath = html.includes('<mjx-math');
            const hasRenderError = html.includes('mjx-merror');
            if (!hasRenderedMath || hasRenderError) {
                process.exit(1);
            }
            console.log('RENDER_OK');
            """
        )

        result = subprocess.run(
            ["node", "-e", script, root, str(input_path), ""],
            capture_output=True,
            text=True,
            check=False,
            timeout=15,
        )
        if result.returncode != 0:
            raise AssertionError(
                f"{name} did not render correctly in MathJax:\n{result.stderr.strip() or result.stdout.strip()}"
            )


def _assert_latex_sequence_renders_in_browser_mathjax(
    named_latex: list[tuple[str, str]],
    max_buffer: int | None = None,
) -> None:
    import json
    import subprocess
    import tempfile
    from pathlib import Path

    root = _mathjax_full_root()
    with tempfile.TemporaryDirectory() as tmp:
        input_path = Path(tmp) / "mathjax_inputs.json"
        input_path.write_text(json.dumps(named_latex), encoding="utf-8")

        script = (
            r"""
            const fs = require('fs');
            const rootPath = process.argv[1];
            const inputFile = process.argv[2];
            const entries = JSON.parse(fs.readFileSync(inputFile, 'utf8'));
            const {mathjax} = require(rootPath + '/js/mathjax.js');
            const AllPackages = require(rootPath + '/js/input/tex/AllPackages.js');
            const {TeX} = require(rootPath + '/js/input/tex.js');
            const {CHTML} = require(rootPath + '/js/output/chtml.js');
            const {LiteAdaptor} = require(rootPath + '/js/adaptors/liteAdaptor.js');
            const {RegisterHTMLHandler} = require(rootPath + '/js/handlers/html.js');

            const adaptor = new LiteAdaptor();
            RegisterHTMLHandler(adaptor);
            const maxBuffer = process.argv[3] === '' ? null : Number(process.argv[3]);
            const texOptions = {
              processEnvironments: true,
              packages: (Array.isArray(AllPackages.AllPackages)
                ? AllPackages.AllPackages
                : AllPackages).concat('require'),
            };
            if (Number.isInteger(maxBuffer) && maxBuffer > 0) {
              texOptions.maxBuffer = maxBuffer;
            }
            const inputJax = new TeX(texOptions);
            const doc = mathjax.document('', {
              InputJax: inputJax,
              OutputJax: new CHTML({}),
            });
            const effectiveMaxBuffer = inputJax.options.maxBuffer;

            const failures = [];
            for (const [name, latex] of entries) {
              if (Number.isInteger(effectiveMaxBuffer) && latex.length > effectiveMaxBuffer) {
                failures.push({
                  name,
                  rendered: false,
                  error: `payload-size=${latex.length} exceeds MathJax maxBuffer=${effectiveMaxBuffer}`,
                });
                continue;
              }
              try {
                const html = adaptor.innerHTML(doc.convert(latex));
                const hasRenderedMath = html.includes('<mjx-math');
                const hasRenderError = html.includes('mjx-merror');
                if (!hasRenderedMath || hasRenderError) {
                  failures.push({
                    name,
                    rendered: hasRenderedMath,
                    error: hasRenderError,
                  });
                }
              } catch (error) {
                failures.push({
                  name,
                  rendered: false,
                  exception: error && error.message ? error.message : `${error}`,
                });
              }
            }

            if (failures.length > 0) {
              console.log(JSON.stringify({ok: false, failures}));
              process.exit(1);
            }
            console.log(JSON.stringify({ok: true, renderedCount: entries.length}));
            """
        )

        result = subprocess.run(
            [
                "node",
                "-e",
                script,
                root,
                str(input_path),
                "" if max_buffer is None else str(max_buffer),
            ],
            capture_output=True,
            text=True,
            check=False,
            timeout=20,
          )
        if result.returncode != 0:
            details = result.stdout.strip()
            raise AssertionError(
                f"Sequence rendering did not succeed for all standard lattice displays.\n{details}\n"
                f"{result.stderr.strip()}"
            )


def _capture_show_latex_payloads(
    named_lattices: list[tuple[str, object]],
) -> tuple[list[tuple[str, str]], str]:
    import io
    from contextlib import redirect_stdout

    from sage.all import show
    from sage.repl.interpreter import SageTestShell
    from sage.repl.rich_output import get_display_manager
    from sage.repl.rich_output.backend_ipython import BackendIPythonNotebook
    from sage.repl.rich_output.output_basic import OutputBase

    named_lattices = list(named_lattices)
    display_manager = get_display_manager()
    original_backend = display_manager._backend
    display_manager.switch_backend(BackendIPythonNotebook(), shell=SageTestShell())

    captured_outputs: list[tuple[dict[str, str], dict[str, str]]] = []
    original_displayhook = display_manager._backend.displayhook

    def capture_displayhook(plain_text: OutputBase, rich_output: OutputBase) -> tuple[dict[str, str], dict[str, str]]:
        raw = original_displayhook(plain_text, rich_output)
        payload: tuple[dict[str, str], dict[str, str]] = (raw[0], raw[1])
        captured_outputs.append(payload)
        return payload

    display_manager._backend.displayhook = capture_displayhook
    stream_output = io.StringIO()

    try:
        with redirect_stdout(stream_output):
            for _, lattice in named_lattices:
                show(lattice)
                print("-" * 60)
    finally:
        display_manager._backend.displayhook = original_displayhook
        display_manager.switch_backend(original_backend)

    assert len(captured_outputs) == len(named_lattices), (
        f"Expected {len(named_lattices)} rendered payloads, got {len(captured_outputs)}"
    )

    rendered = []
    for name, payload in zip((name for name, _ in named_lattices), captured_outputs):
        rendered_payload, _metadata = payload
        rendered_latex = rendered_payload.get("text/latex")
        assert rendered_latex is not None, (
            f"{name} produced no text/latex payload in notebook display output."
        )
        rendered.append((name, rendered_latex))

    return rendered, stream_output.getvalue()


# --------------------------------------------------------------------------
# catalogue
# --------------------------------------------------------------------------


def test_named_lattices_have_their_defining_invariants() -> None:
    catalogue = _preamble()[0]
    expected = {
        "U": (2, (1, 1)),
        "U_2": (2, (1, 1)),
        "E8": (8, (0, 8)),
        "E8_2": (8, (0, 8)),
        "E10": (10, (1, 9)),
        "E10_2": (10, (1, 9)),
        "LK3": (22, (3, 19)),
        "SEn": (10, (1, 9)),
        "TEn": (12, (2, 10)),
        "LpNik": (14, (3, 11)),
        "LmNik": (8, (0, 8)),
        "TdP": (20, (2, 18)),
        "L_20_2_0": (20, (2, 18)),
    }
    for name, (rank, signature) in expected.items():
        lattice = getattr(catalogue.Lattices, name)
        assert lattice.rank() == rank, f"{name}: rank {lattice.rank()} != {rank}"
        assert lattice.signature_pair() == signature, (
            f"{name}: signature {lattice.signature_pair()} != {signature}"
        )


def test_root_lattices_use_the_negative_definite_convention() -> None:
    """A_n, D_n, E_n are negative definite here; Sage's own are positive."""
    catalogue = _preamble()[0]
    for kind, rank in (("A", 2), ("D", 4), ("E", 8)):
        lattice = catalogue.Lattices.root_lattice(kind, rank)
        assert lattice.signature_pair() == (0, rank), (
            f"{kind}{rank} should be negative definite, got {lattice.signature_pair()}"
        )


def test_k3_degree_2d_family() -> None:
    catalogue = _preamble()[0]
    for degree in (1, 2, 3):
        lattice = catalogue.Lattices.LK3_2d(degree)
        assert lattice.rank() == 21
        assert lattice.signature_pair() == (2, 19)
        assert lattice.gram_matrix().det() == -2 * degree


def test_two_elementary_table_is_nikulins_75() -> None:
    catalogue = _preamble()[0]
    table = catalogue.TwoElementary
    assert len(table) == 75
    filled = 0
    for (rank, a, delta), lattice in table.items():
        assert table[rank, a, delta] is lattice
        if lattice is None:
            continue
        filled += 1
        assert lattice.rank() == rank, f"{(rank, a, delta)}: rank {lattice.rank()}"
        assert lattice.signature_pair() == (1, rank - 1), (rank, a, delta)
    assert filled == 75


def test_two_elementary_filled_entries_match_nikulin_invariants() -> None:
    r"""Every constructed table entry is 2-elementary with the keyed $(r,a,\delta)$."""
    catalogue = _preamble()[0]
    for (rank, a, delta), lattice in catalogue.TwoElementary.items():
        if lattice is None:
            continue
        key = (rank, a, delta)
        assert lattice.is_p_elementary(2), key
        assert lattice.rank() == rank, key
        assert lattice.delta() == delta, key
        disc = lattice.discriminant_group()
        assert len(disc.invariants()) == a, (
            f"{key}: a={a} but disc invariants {disc.invariants()}"
        )
        assert disc.is_p_elementary(2), key


def test_discriminant_bilinear_form_elements_pair() -> None:
    r"""Elements of $\operatorname{coker}(L\to L^\vee)$ pair in $\mathbb Q/\mathbb Z$.

    $A_{A_2}=\mathbb Z/3$ generated by the dual basis, on which $b$ is
    $G^{-1}\bmod 1$.  $A_2$ is negative definite here, so
    $G^{-1}=-\frac13\begin{pmatrix}2&1\\1&2\end{pmatrix}$ and
    $b=\begin{pmatrix}1/3&2/3\\2/3&1/3\end{pmatrix}$ -- which is also what the
    Gram matrix reports, so the two must agree entry by entry.
    """
    catalogue = _preamble()[0]
    A = catalogue.Lattices.root_lattice("A", 2).discriminant_bilinear_form()

    assert A.invariants() == (3,)
    gens = A.module_generators()
    assert gens.cardinality() == 2, "one generator per generator of L, not per invariant factor"

    x, y = gens
    assert x.b(y) == y.b(x)
    assert (x * y).parent() == A.value_module()
    assert x.b(x) == 1 / 3
    assert x.b(y) == 2 / 3
    assert (x + y).b(x) == x.b(x) + y.b(x)
    assert (3 * x).b(y) == 0

    G = A.gram_matrix()
    assert all(
        QQ(G[i][j]) == QQ((gens[i] * gens[j]).lift())
        for i in range(2)
        for j in range(2)
    ), f"Gram matrix {G} disagrees with the pairing"


def test_is_p_elementary_rejects_nearby_non_examples() -> None:
    catalogue = _preamble()[0]
    L = catalogue.Lattices
    assert L.U_2.is_p_elementary(2)
    assert L.E8.is_p_elementary(2)
    assert not L.A2.is_p_elementary(2)
    assert L.A2.discriminant_group().is_p_elementary(3)
    assert not L.Z.twist(4).is_p_elementary(2)


def test_named_lattice_aliases_are_identical_objects() -> None:
    """Aliases are the same parent, not separately constructed copies."""
    L = _preamble()[0].Lattices
    assert L.U is L.H
    assert L.U_2 is L.H_2
    assert L.Sdp is L.U_2
    assert L.SEn is L.E10_2
    assert L.LmNik is L.E8_2


# --------------------------------------------------------------------------
# sterk
# --------------------------------------------------------------------------

_STERK_PUBLISHED_NORM_COUNTS = {
    "Sterk_1": {"total": 12, "norm_-4": 12, "norm_-2": 0},
    "Sterk_2": {"total": 10, "norm_-4": 9, "norm_-2": 1},
    "Sterk_3": {"total": 12, "norm_-4": 10, "norm_-2": 2},
    "Sterk_4": {"total": 11, "norm_-4": 9, "norm_-2": 2},
    "Sterk_5": {"total": 14, "norm_-4": 10, "norm_-2": 4},
}


def test_sterk_configurations_match_published_norm_breakdown() -> None:
    """The external oracle: Sterk's counts *by norm*, not just totals."""
    catalogue, _, sterk = _preamble()
    TdP = catalogue.Lattices.TdP
    configurations = sterk.sterk_roots()
    for name, roots in configurations.items():
        published = _STERK_PUBLISHED_NORM_COUNTS[name]
        minus_four = sum(1 for r in roots if TdP.b(r, r) == -4)
        minus_two = sum(1 for r in roots if TdP.b(r, r) == -2)
        assert len(roots) == published["total"], name
        assert minus_four == published["norm_-4"], f"{name}: {minus_four} roots of norm -4"
        assert minus_two == published["norm_-2"], f"{name}: {minus_two} roots of norm -2"


def test_every_sterk_vector_is_a_root() -> None:
    catalogue, _, sterk = _preamble()
    TdP = catalogue.Lattices.TdP
    for name, roots in sterk.sterk_roots().items():
        for index, root in enumerate(roots, start=1):
            norm = TdP.b(root, root)
            assert norm in (-2, -4), f"{name} root {index}: norm {norm}"


def test_s4_12_is_isotropic_not_a_root() -> None:
    """The vector wrongly dropped as dead code: a cusp, norm 0."""
    catalogue, _, sterk = _preamble()
    vectors = sterk.isotropic_vectors()
    assert "s4_12" in vectors
    assert catalogue.Lattices.TdP.b(vectors["s4_12"], vectors["s4_12"]) == 0


def test_five_selected_isotropic_vectors() -> None:
    """Why there are five Sterk cases."""
    catalogue, _, sterk = _preamble()
    selected_vectors = sterk.selected_isotropic_vectors()
    assert len(selected_vectors) == 5
    TEn = catalogue.Lattices.TEn
    for name, vector_ in selected_vectors.items():
        assert TEn.b(vector_, vector_) == 0, f"{name} is not isotropic"


def test_getsterk5_reproduces_sterk_5_from_a_different_lattice() -> None:
    """Rank 10 here versus rank 20 in ``sterk_roots`` -- independent presentations."""
    _, _, sterk = _preamble()
    lattice, vectors = sterk.sterk5_in_U_E8_2()
    assert lattice.rank() == 10
    assert len(vectors) == 14
    minus_four = sum(1 for v in vectors if lattice.b(v, v) == -4)
    minus_two = sum(1 for v in vectors if lattice.b(v, v) == -2)
    published = _STERK_PUBLISHED_NORM_COUNTS["Sterk_5"]
    assert (minus_four, minus_two) == (published["norm_-4"], published["norm_-2"])


def test_diagonal_embedding_is_e8_2_into_tdp() -> None:
    catalogue, _, sterk = _preamble()
    phi = sterk.diagonal_embedding()
    assert phi is catalogue.Embeddings.E8_2_into_TdP
    assert phi.matrix().dimensions() == (8, 20)


def test_embedding_chain_TCo_TEn_TdP_LK3() -> None:
    """$T_{Co}\\hookrightarrow T_{En}\\hookrightarrow T_{dP}\\hookrightarrow\\Lambda_{K3}$."""
    _ensure_preamble()

    catalogue, _, _ = _preamble()
    E = catalogue.Embeddings
    L = catalogue.Lattices
    assert E.TCo_into_TEn.domain() is L.Tco
    assert E.TCo_into_TEn.codomain() is L.TEn
    assert E.TEn_into_TdP.domain() is L.TEn
    assert E.TEn_into_TdP.codomain() is L.TdP
    # $T=(L^G)^\perp$ is a subobject in $\mathrm{Lat}_G$: asking $\Lambda_{K3}$
    # for it equips $\Lambda_{K3}$ with $\iota$ first, and the ambient of the
    # answer is that $G$-lattice.  It is $\Lambda_{K3}$ once $G$ is forgotten.
    assert E.TdP_into_LK3.structure_morphism().codomain().forget_action() is L.LK3
    assert E.TEn_into_LK3.structure_morphism().codomain().forget_action() is L.LK3
    assert E.TCo_into_TEn.matrix().dimensions() == (11, 12)
    assert E.TEn_into_TdP.matrix().dimensions() == (12, 20)
    assert E.TdP_into_LK3.structure_morphism().matrix().dimensions() == (20, 22)
    assert E.E8_2_into_TdP.matrix().dimensions() == (8, 20)
    # Diagonal piece of TEn→TdP agrees with E8(2)↪TdP on the E8(2) summand.
    ten = list(L.TEn.module_generators())
    for i, gen in enumerate(L.E8_2.module_generators()):
        assert E.TEn_into_TdP(ten[4 + i]) == E.E8_2_into_TdP(gen)


def test_block_hom_Z2_U2_into_U_U2() -> None:
    r"""Block Hom spelling: $\langle 2\rangle\oplus U(2)\to U\oplus U(2)$, $h\mapsto e+f$."""
    _ensure_preamble()

    catalogue, _, _ = _preamble()
    Lcat = catalogue.Lattices
    domain = Lcat.Z_2 + Lcat.U_2
    codomain = Lcat.U + Lcat.U_2
    z1, z2 = domain.summands()
    w1, w2 = codomain.summands()
    w1_gens = w1.embedded_module_generators()
    phi = domain.Hom(codomain)({z1: w1_gens[0] + w1_gens[1], z2: w2})
    assert phi.matrix().dimensions() == (3, 4)
    e, f = codomain.module_generators()[0], codomain.module_generators()[1]
    assert phi(domain.module_generators()[0]) == e + f
    for i in range(2):
        assert phi(domain.module_generators()[1 + i]) == codomain.module_generators()[2 + i]
    # Same matrix as the flat generator-image spelling.
    flat = domain.Hom(codomain)([e + f] + list(codomain.module_generators())[2:])
    assert phi.matrix() == flat.matrix()


def test_block_hom_sum_of_blocks_diagonal() -> None:
    r"""Block Hom columns: ``{a1: b1, a2: b2 + b3}`` is id ⊕ diagonal $U(2)\hookrightarrow U\oplus U$."""
    _ensure_preamble()

    catalogue, _, _ = _preamble()
    Lcat = catalogue.Lattices
    domain = Lcat.U + Lcat.U_2
    codomain = Lcat.U + Lcat.U + Lcat.U
    a1, a2 = domain.summands()
    b1, b2, b3 = codomain.summands()
    a1_gens, a2_gens = a1.embedded_module_generators(), a2.embedded_module_generators()
    b1_gens, b2_gens, b3_gens = (
        b1.embedded_module_generators(),
        b2.embedded_module_generators(),
        b3.embedded_module_generators(),
    )
    diagonal = [b2_gens[i] + b3_gens[i] for i in range(2)]
    phi = domain.Hom(codomain)({a1: b1, a2: diagonal})
    assert phi.matrix().dimensions() == (4, 6)
    for i in range(2):
        assert phi(a1_gens[i]) == b1_gens[i]
        assert phi(a2_gens[i]) == diagonal[i]
    for x in domain.module_generators():
        for y in domain.module_generators():
            assert domain.b(x, y) == codomain.b(phi(x), phi(y))
    # Same as an explicit gen-wise diagonal sequence.
    flat = domain.Hom(codomain)(list(b1_gens) + diagonal)
    assert phi.matrix() == flat.matrix()


# --------------------------------------------------------------------------
# involutions
# --------------------------------------------------------------------------


def test_involutions_are_involutions_and_isometries() -> None:
    catalogue = _preamble()[0]
    named = {
        name: getattr(catalogue.Involutions, name)
        for name in ("I_dP", "I_En", "I_Nik")
    }
    assert sorted(named) == ["I_En", "I_Nik", "I_dP"]
    for name, morphism in named.items():
        assert morphism.is_involution(), name
        assert morphism.domain() is catalogue.Lattices.LK3, name
        assert morphism.parent() is catalogue.Lattices.LK3.Aut(), name


def test_with_action_receives_a_homomorphism_the_caller_constructed() -> None:
    """The only way to act: build $G$, build $\\rho\\in\\mathrm{Hom}(G,O(L))$, hand it over.

    The lattice is given a morphism and equips itself with it; it does not
    assemble one from a group and a list of images.  Constructing $\\rho$ is
    the group homset's business, and the relations of $G$ are checked there.
    Both routes to a $G$-lattice end at this one-argument method, so the
    invariants agree with the involution's own.
    """
    catalogue = _preamble()[0]
    LK3 = catalogue.Lattices.LK3
    involution = catalogue.Involutions.I_En
    acting_group = involution.cyclic_subgroup()
    rho = group_action_homset(acting_group, LK3)(
        [
            LK3.Aut()(
                {
                    label: generator(LK3.module_generator(label))
                    for label in LK3.module_generating_set()
                }
            )
            for generator in acting_group.group_generators()
        ]
    )
    acted = LK3.with_action(rho)
    assert acted.group() is acting_group
    invariants, coinvariants = acted.invariant_lattice(), acted.coinvariant_lattice()
    assert invariants.is_isometric(catalogue.Lattices.SEn)
    assert invariants.rank() + coinvariants.rank() == 22
    # The subgroup names the same $\rho$ by itself, so the lattice-level
    # methods -- which take $\rho$ and nothing weaker -- agree with it.
    assert LK3.invariant_lattice(
        acting_group.inclusion()
    ).rank() == invariants.rank()


def test_coinvariant_lattice_returns_subobject() -> None:
    r"""The coinvariant lattice is one object, and it is a subobject.

    Asked of \(U\) under the swap \(e\leftrightarrow f\), whose coinvariant is
    \(\langle-2\rangle\): both claims are about the construction, not about any
    particular lattice, so the specimen is the smallest one that has a nontrivial
    involution.  The named K3 involutions are exercised where the claim really is
    about them, in
    :func:`test_invariant_and_coinvariant_lattices_reproduce_the_named_lattices`.
    """
    catalogue = _preamble()[0]
    U = catalogue.Lattices.U
    labels = tuple(U.module_generating_set())
    e, f = U.module_generators()
    swap = U.Aut()({labels[0]: f, labels[1]: e})

    acted = U.with_action(swap.cyclic_subgroup().inclusion())
    coinvariant = acted.coinvariant_lattice()
    assert coinvariant is acted.coinvariant_lattice(), "one object, reached twice"
    assert coinvariant.structure_morphism().is_injective(), "a subobject embeds"
    assert coinvariant.rank() == 1, "the anti-invariant part of the swap is rank 1"


def test_invariant_and_coinvariant_lattices_reproduce_the_named_lattices() -> None:
    """Two independent constructions agreeing: direct sums versus signed basis images."""
    catalogue, _, _ = _preamble()
    L = catalogue.Lattices
    I = catalogue.Involutions
    pairs = [
        (I.I_dP, "-", L.TdP),
        (I.I_En, "+", L.SEn),
        (I.I_En, "-", L.TEn),
        (I.I_Nik, "+", L.LpNik),
        (I.I_Nik, "-", L.LmNik),
    ]
    for involution, sign, expected in pairs:
        action = involution.cyclic_subgroup().inclusion()
        lattice = (
            L.LK3.invariant_lattice(action)
            if sign == "+"
            else L.LK3.coinvariant_lattice(action)
        )
        assert lattice.is_isometric(expected), f"{involution} L{sign}"


def test_invariant_and_coinvariant_ranks_sum_to_22() -> None:
    catalogue = _preamble()[0]
    L = catalogue.Lattices
    for name in ("I_dP", "I_En", "I_Nik"):
        action = getattr(catalogue.Involutions, name).cyclic_subgroup().inclusion()
        plus = L.LK3.invariant_lattice(action)
        minus = L.LK3.coinvariant_lattice(action)
        assert plus.rank() + minus.rank() == 22, name


# --------------------------------------------------------------------------
# the source's claim block (old lines 365-388)
# --------------------------------------------------------------------------


def test_source_claim_block_holds() -> None:
    """Eight assertions the source wrote behind ``do_tests = False`` and never ran."""
    catalogue, _, _ = _preamble()
    TEn = catalogue.Lattices.TEn
    TE = catalogue.TwoElementary
    basis, dual = TEn.module_generators(), TEn.dual_basis()
    e, f, ep = basis[0], basis[1], basis[2]
    w1 = dual[4]

    assert TEn.div(e) == 1 and TEn.q(e) == 0
    assert e.e_perp_mod_e().is_isometric(catalogue.Lattices.E10_2)
    assert e.e_perp_mod_e().is_isometric(TE[10, 10, 0])

    assert TEn.div(ep) == 2 and TEn.q(ep) == 0
    assert ep.e_perp_mod_e().is_isometric(
        catalogue.Lattices.U.direct_sum((catalogue.Lattices.E8_2,))
    )
    assert ep.e_perp_mod_e().is_isometric(TE[10, 8, 0])

    assert TEn.I_perp_mod_I([e, ep]).is_isometric(catalogue.Lattices.E8_2)

    # w1 is a dual generator: the sum is formed in TEn^v, with e and f carried
    # there by c, and the lift names the element of TEn it turns out to be.
    c = TEn.correlation()
    vp = c.lift(c(2 * e + 2 * f) + 2 * w1)
    assert TEn.div(vp) == 2 and TEn.q(vp) == 0


def test_the_8_6_0_lattice_has_its_recorded_invariants() -> None:
    """The entry recovered from the claim block; an index-2 overlattice of A1^8."""
    catalogue, _, _ = _preamble()
    TEn = catalogue.Lattices.TEn
    basis, dual = TEn.module_generators(), TEn.dual_basis()
    c = TEn.correlation()
    quotient = TEn.I_perp_mod_I([
        basis[2],
        c.lift(c(2 * basis[0] + 2 * basis[1]) + 2 * dual[4]),
    ])
    assert quotient.rank() == 8
    assert quotient.signature_pair() == (0, 8)
    assert quotient.gram_matrix().det() == 64


# --------------------------------------------------------------------------
# predicates (now ParentMethods on IntegralLattices)
# --------------------------------------------------------------------------


def test_delta_is_zero_on_the_two_elementary_lattices() -> None:
    catalogue, _, _ = _preamble()
    for name in ("U", "U_2", "E8", "E8_2", "E10_2", "TEn"):
        lattice = getattr(catalogue.Lattices, name)
        assert lattice.delta() in (0, 1)
        assert lattice.is_coeven() == (lattice.delta() == 0)
        assert type(lattice).delta.__qualname__ == "IntegralLattices.ParentMethods.delta"


def test_definiteness_predicates() -> None:
    catalogue, _, _ = _preamble()
    assert catalogue.Lattices.E8.is_elliptic()
    assert catalogue.Lattices.E8.is_parabolic()
    assert not catalogue.Lattices.U.is_elliptic()
    assert type(catalogue.Lattices.E8).is_elliptic.__qualname__ == (
        "IntegralLattices.ParentMethods.is_elliptic"
    )


def test_coxeter_diagram_uses_the_owned_sage_parent() -> None:
    """The diagram is a parent in the preamble's own category, not the spike's."""
    _preamble()

    diagram = CoxeterDiagrams().from_cartan_type(["E", 8])

    assert diagram.category().is_subcategory(CoxeterDiagrams())
    assert diagram.coxeter_matrix() == CoxeterMatrix(["E", 8])


def test_diagram_layouts_match_root_counts() -> None:
    catalogue, _, _ = _preamble()
    assert len(catalogue.SterkDiagrams.Sterk_1.preferred_positions()) == 12
    assert len(catalogue.SterkDiagrams.Sterk_2.preferred_positions()) == 10
    assert len(catalogue.SterkDiagrams.Sterk_3.preferred_positions()) == 12
    assert len(catalogue.SterkDiagrams.Sterk_4.preferred_positions()) == 11
    assert len(catalogue.SterkDiagrams.Sterk_5.preferred_positions()) == 14


# --------------------------------------------------------------------------
# newly ported surface: sterks1/2/3, vinberg_algorithm, get_isotropic_type, patch methods
# --------------------------------------------------------------------------


def test_sterks_in_ten_are_root_configurations() -> None:
    """The T_En-coordinate configurations, with their two different dual scalings."""
    catalogue, _, sterk = _preamble()
    configurations = sterk.sterks_in_ten()
    assert sorted(configurations) == ["sterks1", "sterks2", "sterks3"]
    TEn = catalogue.Lattices.TEn
    expected_counts = {"sterks1": 12, "sterks2": 10, "sterks3": 12}
    for name, vectors in configurations.items():
        assert len(vectors) == expected_counts[name], name
        for index, vector_ in enumerate(vectors, start=1):
            norm = TEn.b(vector_, vector_)
            assert norm in (-2, -4), f"{name} vector {index}: norm {norm}"


def test_sterks1_and_sterks3_use_different_dual_scalings() -> None:
    """sterks1 uses $2G^{-1}$ duals; sterks3 uses $G^{-1}$."""
    catalogue, _, sterk = _preamble()
    TEn = catalogue.Lattices.TEn
    dual = TEn.dual_basis()
    ep, fp = TEn.module_generators()[2], TEn.module_generators()[3]
    configs = sterk.sterks_in_ten()
    c = TEn.correlation()
    # index 9 of sterks1 is 2*ep+ad2[8] with ad2 = 2*dual
    assert configs["sterks1"][9] == c.lift(c(2 * ep) + 2 * dual[11])
    # The negative control is stated in TEn^v, where both sides exist: the
    # un-doubled dual generator gives a different vector, and it need not be
    # in c(TEn) at all for that to be sayable.
    assert c(configs["sterks1"][9]) != c(2 * ep) + dual[11]
    # index 8 of sterks3 is 2*fp+2*ad1[8] with ad1 = dual
    assert configs["sterks3"][8] == c.lift(c(2 * fp) + 2 * dual[11])


def test_nothing_from_the_sterk_section_is_unported() -> None:
    _ensure_preamble()

    assert NOT_PORTED == ()


def test_to_lin_comb_generators_labels_elements() -> None:
    catalogue, _, _ = _preamble()
    lattice = catalogue.Lattices.U.direct_sum((catalogue.Lattices.E8,)).with_names("e, f, a1..a8")
    generators = lattice.module_generators()
    assert lattice.to_lin_comb_module_generators(generators[0]) == "e"
    label = lattice.to_lin_comb_module_generators(2 * generators[0] - generators[3])
    assert "2*e" in label and "a2" in label, label


def test_sublattices_is_a_usable_dict() -> None:
    """Old line 358 does ``TEn.sublattices.update({...})`` and needs it to exist."""
    catalogue, _, _ = _preamble()
    lattice = catalogue.Lattices.TEn
    lattice.sublattices.update({"Sterk_1": catalogue.Lattices.E10_2})
    assert "Sterk_1" in lattice.sublattices
    lattice.sublattices.clear()


def test_twist_accepts_names() -> None:
    catalogue, _, _ = _preamble()
    twisted = catalogue.Lattices.E8.twist(2, names=tuple(f"b{i}" for i in range(1, 9)))
    assert twisted.variable_names() == tuple(f"b{i}" for i in range(1, 9))


def test_lattice_latex_representation() -> None:
    catalogue, _, _ = _preamble()
    _ensure_preamble()
    from sage.misc.latex import latex

    u_latex = str(latex(catalogue.Lattices.U))
    assert r"L \in \mathrm{Lattices}(\mathbb{Z})" in u_latex
    assert r"\mathrm{rk}(L) = 2" in u_latex
    assert r"\mathrm{sig}(L) = (1, 1)" in u_latex
    assert r"\mathrm{disc}(L) = -1" in u_latex
    assert r"\cdot" in u_latex
    assert r"A_L = \left\langle e_{1}, e_{2} \;\middle|\;" in u_latex
    assert r"\text{(Finite presentation)}" in u_latex
    assert r"A_L \cong 0 \in \mathrm{Groups}" in u_latex
    assert r"G_{q_{A_L}} = ()" in u_latex

    a2_latex = str(latex(catalogue.Lattices.root_lattice("A", 2)))
    assert r"A_L = \left\langle e_{1}, e_{2} \;\middle|\;" in a2_latex
    assert r"\text{(Finite presentation)}" in a2_latex
    assert r"A_L \cong C_{3} \in \mathrm{Groups}" in a2_latex
    assert r"G_{q_{A_L}} =" in a2_latex

    a2_disc = catalogue.Lattices.root_lattice("A", 2).discriminant_group().gram_matrix()
    assert a2_disc.subdivisions() == ([], [])

    ten_latex = str(latex(catalogue.Lattices.TEn))
    assert r"\mathrm{disc}(L) = 1024 = 2^{10}" in ten_latex

    # $A_L$ is the cokernel on $L$'s dual basis, so it has one generator per
    # generator of $T_{En}=U\oplus U(2)\oplus E_8(2)$ and one block per summand
    # -- including $U$'s, which is trivial.  The two-block reading belonged to
    # the invariant-factor form, which is a different object.
    ten_disc = catalogue.Lattices.TEn.discriminant_group().gram_matrix()
    assert ten_disc.subdivisions() == ([2, 4], [2, 4])
    assert ten_disc.nrows() == catalogue.Lattices.TEn.rank()
    assert (
        catalogue.Lattices.TEn.discriminant_group().invariant_factor_form().invariants()
        == catalogue.Lattices.TEn.discriminant_group().invariants()
    )

    ten_nf = catalogue.Lattices.TEn.discriminant_group().normal_form()
    assert ten_nf.gram_matrix().subdivisions() == ([2, 4, 6, 8], [2, 4, 6, 8])

    set_zero_dots(False)
    u_latex_no_dots = str(latex(catalogue.Lattices.U))
    # Only the Gram matrix line should be affected by zero dots.
    gram_line = [l for l in u_latex_no_dots.split('\n') if 'G_L =' in l][0]
    assert r"\cdot" not in gram_line
    assert "0" in u_latex_no_dots
    set_zero_dots(True)


def test_catalogue_latex_fits_mathjax_and_has_balanced_environments() -> None:
    catalogue, _, _ = _preamble()
    from sage.misc.latex import latex

    # The claim is about the shape of the LaTeX, so the specimens are chosen for
    # distinct shapes and not for size: every named catalogue lattice, since that
    # is what a session displays, plus a few root lattices of each family.  The
    # A_1..A_21 and D_2..D_22 sweeps this replaced rendered forty-two more
    # lattices, each one costing a discriminant group and a node subprocess, to
    # re-check a fact about brace balance that A_2 and D_4 already establish.
    for name, lattice in {
        # The registry, not a scan of the class's attributes: ``Lattices`` is
        # the category as well as the catalogue, so its attributes include the
        # axiom categories, and asking a class whether it is in
        # ``IntegralLattices()`` asks a class for its ``category()``.
        **catalogue.Lattices.namespace(),
        **{f"A{n}": catalogue.Lattices.root_lattice("A", n) for n in (1, 2, 5)},
        **{f"D{n}": catalogue.Lattices.root_lattice("D", n) for n in (4, 5)},
    }.items():
        rendered = str(latex(lattice))
        _assert_latex_environments_balanced(rendered, name)
        _assert_latex_renders_in_browser_mathjax(rendered, name)


def test_standard_lattice_show_pattern_renders_correctly_in_mathjax() -> None:
    catalogue, _, _ = _preamble()
    named_examples = {
        "U": catalogue.Lattices.U,
        "E8": catalogue.Lattices.E8,
        "E10": catalogue.Lattices.E10,
        "K3": catalogue.Lattices.LK3,
    }
    rendered, stream_output = _capture_show_latex_payloads(list(named_examples.items()))
    max_buffer = _configured_mathjax_max_buffer()
    assert stream_output.count("-" * 60) == len(named_examples), (
        "Expected a separator line after each lattice display in the one-cell pattern."
    )
    _assert_latex_sequence_renders_in_browser_mathjax(rendered, max_buffer=max_buffer)


def test_direct_sum_subdivides_gram_matrix() -> None:
    catalogue, _, _ = _preamble()
    direct_sum_lattice = catalogue.Lattices.U.direct_sum((catalogue.Lattices.E8,))
    assert direct_sum_lattice.gram_matrix().subdivisions() == ([2], [2])
    assert catalogue.Lattices.LK3.gram_matrix().subdivisions() == ([2, 4, 6, 14], [2, 4, 6, 14])
    assert catalogue.Lattices.LK3_2d(3).gram_matrix().subdivisions() == ([1, 3, 5, 13], [1, 3, 5, 13])


def test_lattice_element_multiplication_and_exponentiation() -> None:
    catalogue, _, _ = _preamble()
    a2 = catalogue.Lattices.root_lattice("A", 2)
    alpha1, alpha2 = a2.module_generators()
    assert alpha1 * alpha1 == -2
    assert alpha1 * alpha2 == 1
    assert alpha1 ** 2 == -2
    assert alpha1 ^ 2 == -2
    assert (alpha1 + alpha2) ^ 2 == -2
    assert (alpha1 + 2 * alpha2) * (alpha1 - alpha2) == 3


def test_vinberg_algorithm_negates_roots_when_it_twists() -> None:
    """The source typo (``do_twist`` set, ``doTwist`` tested) disabled this branch."""
    _ensure_preamble()

    catalogue, _, _ = _preamble()
    # D4 is already negative definite here, so U + D4 is (1, 5) -- the repo's
    # own convention, and the signature that makes the twist branch fire.
    d4 = catalogue.Lattices.root_lattice("D", 4)
    lattice = catalogue.Lattices.U.direct_sum((d4,)).with_names("e, f, a1..a4")
    refine(lattice, HyperbolicLattices())
    roots = lattice.vinberg_algorithm()
    root_names = [lattice.to_lin_comb_module_generators(root) for root in roots]
    assert len(roots) == 6, len(roots)
    # Twisting happened, so the roots come back negated -- the branch the typo
    # made unreachable.
    assert any(name.startswith("-") for name in root_names), root_names


def test_get_isotropic_type_classifies() -> None:
    _ensure_preamble()
    import pytest

    catalogue, _, _ = _preamble()
    odd = catalogue.Lattices.U.direct_sum((catalogue.Lattices.U,))
    refine(odd, IntegralLattices())
    assert odd.get_isotropic_type(odd.module_generators()[0]) == "Odd"
    with pytest.raises(AssertionError):
        odd.get_isotropic_type(vector(ZZ, [1, 0, 0, 0]))

    ordinary = catalogue.Lattices.U_2
    refine(ordinary, IntegralLattices())
    # $e/2$, which is $e/\operatorname{div}(e)$ since $\operatorname{div}(e)=2$
    # in $U(2)$ -- built by dividing $c(e)$ rather than from a coordinate row,
    # which the projection refuses and which names no element of $L^\vee$.
    ordinary_class = ordinary.divided_discriminant_class(
        ordinary.module_generators()[0]
    )
    assert not ordinary_class.is_characteristic()
    assert ordinary.get_isotropic_type(ordinary.module_generators()[0]) == "Even ordinary"

    characteristic = catalogue.Lattices.IPQ(1, 1).twist(2)
    refine(characteristic, IntegralLattices())
    # $(e+f)/2$, and $\operatorname{div}(e+f)=\gcd(2,-2)=2$ on $\langle2\rangle
    # \oplus\langle-2\rangle$, so this is the same class the isotropic type
    # below is read from.
    characteristic_class = characteristic.divided_discriminant_class(
        characteristic.module_generators()[0]
        + characteristic.module_generators()[1]
    )
    assert characteristic_class.is_characteristic()
    assert characteristic.get_isotropic_type(
        characteristic.module_generators()[0] + characteristic.module_generators()[1]
    ) == "Even characteristic"


def test_install_hooks_are_idempotent() -> None:
    _ensure_preamble()
    # The hooks ``install.sage`` itself calls.  Integral lattices had one and
    # no longer do: the category is installed by loading its file, so there is
    # no second call to be idempotent about.
    install_finitely_presented_groups()
    install_algebras()
    assert Lattices.U.rank() == 2


def test_lattices_install_binds_specimens_and_lk3_generators() -> None:
    # What ``install`` binds is asked of the objects, not of their type.
    # An ``isinstance`` against the spike's protocol classes says only that a
    # name was declared somewhere; that a bound element lies in LK3 and a
    # bound morphism starts there is what the binding is *for*.
    _ensure_preamble()
    ns: dict = {}
    Lattices.install(ns)
    assert ns["U"] is Lattices.U
    assert ns["LK3"] is Lattices.LK3

    v1 = ns["v1"]
    assert v1.parent() is Lattices.LK3

    i_en = ns["I_En"]
    assert i_en.domain() is Lattices.LK3

    a2 = ns["A2"]
    assert a2.signature_pair() == (0, 2)

    d4 = ns["D4"]
    assert d4.rank() == 4

    assert ns["TdP"] is Lattices.TdP

    e = ns["e"]
    assert e.parent() is Lattices.TdP


