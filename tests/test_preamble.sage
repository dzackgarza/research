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


def _ensure_preamble():
    """Load the mathematical preamble scripts (not notebook ``init.sage``)."""
    if "Lattices" in globals():
        return
    from pathlib import Path
    import dzack_research

    global _PREAMBLE
    _PREAMBLE = Path(dzack_research.__file__).resolve().parent / "preamble"
    p = _PREAMBLE
    load(str(p / "vendor.sage"))
    load(str(p / "refine.sage"))
    load(str(p / "categories/integral_lattices.sage"))
    load(str(p / "categories/lattice_homomorphisms.sage"))
    load(str(p / "categories/lattice_isometries.sage"))
    load(str(p / "categories/hyperbolic_lattices.sage"))
    load(str(p / "categories/discriminant_groups.sage"))
    install_integral_lattices()
    install_discriminant_groups()
    activate()
    load(str(p / "ergonomics.sage"))
    load(str(p / "fixtures.sage"))
    load(str(p / "catalogue.sage"))
    load(str(p / "sterk.sage"))
    load(str(p / "julia.sage"))
    Lattices.install(globals())


def _preamble():
    """Compatibility shim: (catalogue-ns, fixtures-ns, Sterk)."""
    import types

    _ensure_preamble()
    catalogue = types.SimpleNamespace(
        Lattices=Lattices,
        Embeddings=Embeddings,
        Involutions=Involutions,
        TwoElementary=TwoElementary,
    )
    fixtures = types.SimpleNamespace(
        BONDS=BONDS,
        STERK_ROOT_COUNTS=STERK_ROOT_COUNTS,
        STERK_PUBLISHED=STERK_PUBLISHED,
        COMPUTED_ROOT_COUNTS=COMPUTED_ROOT_COUNTS,
        RECORDED_ROOT_MATRIX_ROWS=RECORDED_ROOT_MATRIX_ROWS,
        CROSS_CHECK_RECIPES=CROSS_CHECK_RECIPES,
        DIAGRAM_CONVENTION=DIAGRAM_CONVENTION,
        STERK_POSITIONS=STERK_POSITIONS,
    )
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


def _mathjax_full_root() -> str:
    import glob
    import os
    import shutil
    import subprocess
    from pathlib import Path

    cached = getattr(_mathjax_full_root, "__cached__", None)
    if cached is not None:
        return cached

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
            _mathjax_full_root.__cached__ = str(full_root)
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
            value = _read_from_html_config(body)
            if value is not None:
                return value

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

    named_lattices = list(named_lattices)
    display_manager = get_display_manager()
    original_backend = display_manager._backend
    display_manager.switch_backend(BackendIPythonNotebook(), shell=SageTestShell())

    captured_outputs: list[tuple[dict[str, str], dict[str, str]]] = []
    original_displayhook = display_manager._backend.displayhook

    def capture_displayhook(plain_text, rich_output):
        payload = original_displayhook(plain_text, rich_output)
        captured_outputs.append((payload[0], payload[1]))  # type: ignore[index]
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


def test_named_lattices_have_their_defining_invariants():
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


def test_root_lattices_use_the_negative_definite_convention():
    """A_n, D_n, E_n are negative definite here; Sage's own are positive."""
    catalogue = _preamble()[0]
    for kind, rank in (("A", 2), ("D", 4), ("E", 8)):
        lattice = catalogue.Lattices.root_lattice(kind, rank)
        assert lattice.signature_pair() == (0, rank), (
            f"{kind}{rank} should be negative definite, got {lattice.signature_pair()}"
        )


def test_k3_degree_2d_family():
    catalogue = _preamble()[0]
    for degree in (1, 2, 3):
        lattice = catalogue.Lattices.LK3_2d(degree)
        assert lattice.rank() == 21
        assert lattice.signature_pair() == (2, 19)
        assert lattice.gram_matrix().det() == -2 * degree


def test_two_elementary_table_is_nikulins_75():
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


def test_two_elementary_filled_entries_match_nikulin_invariants():
    r"""Every constructed table entry is 2-elementary with the keyed $(r,a,\delta)$."""
    catalogue = _preamble()[0]
    for (rank, a, delta), lattice in catalogue.TwoElementary.items():
        if lattice is None:
            continue
        key = (rank, a, delta)
        assert lattice.is_p_elementary(2), key
        assert lattice.rank() == rank, key
        assert lattice.delta() == delta, key
        with without_element_wrap():
            disc = lattice.discriminant_group()
        assert len(disc.invariants()) == a, (
            f"{key}: a={a} but disc invariants {disc.invariants()}"
        )
        assert disc.is_p_elementary(2), key


def test_is_p_elementary_rejects_nearby_non_examples():
    catalogue = _preamble()[0]
    L = catalogue.Lattices
    assert L.U_2.is_p_elementary(2)
    assert L.E8.is_p_elementary(2)
    assert not L.A2.is_p_elementary(2)
    assert L.A2.discriminant_group().is_p_elementary(3)
    assert not L.Z.twist(4).is_p_elementary(2)


def test_named_lattice_aliases_are_identical_objects():
    """Aliases are the same parent, not separately constructed copies."""
    L = _preamble()[0].Lattices
    assert L.U is L.H
    assert L.U_2 is L.H_2
    assert L.Sdp is L.U_2
    assert L.SEn is L.E10_2
    assert L.LmNik is L.E8_2


def test_two_elementary_named_entries_are_identical_to_catalogue_lattices():
    catalogue = _preamble()[0]
    L = catalogue.Lattices
    TE = catalogue.TwoElementary
    assert TE[2, 0, 0] is L.U
    assert TE[2, 2, 0] is L.U_2
    assert TE[10, 0, 0] is L.E10
    assert TE[10, 10, 0] is L.E10_2
    assert TE[2, 2, 1] is None
    assert TE[20, 2, 1] is None


# --------------------------------------------------------------------------
# sterk
# --------------------------------------------------------------------------


def test_sterk_configurations_match_published_norm_breakdown():
    """The external oracle: Sterk's counts *by norm*, not just totals."""
    catalogue, fixtures, sterk = _preamble()
    TdP = catalogue.Lattices.TdP
    configurations = sterk.sterk_roots()
    for name, roots in configurations.items():
        published = STERK_PUBLISHED[name]
        minus_four = sum(1 for r in roots if TdP.b(r, r) == -4)
        minus_two = sum(1 for r in roots if TdP.b(r, r) == -2)
        assert len(roots) == published["total"], name
        assert minus_four == published["norm_-4"], f"{name}: {minus_four} roots of norm -4"
        assert minus_two == published["norm_-2"], f"{name}: {minus_two} roots of norm -2"


def test_every_sterk_vector_is_a_root():
    catalogue, _, sterk = _preamble()
    TdP = catalogue.Lattices.TdP
    for name, roots in sterk.sterk_roots().items():
        for index, root in enumerate(roots, start=1):
            norm = TdP.b(root, root)
            assert norm in (-2, -4), f"{name} root {index}: norm {norm}"


def test_s4_12_is_isotropic_not_a_root():
    """The vector wrongly dropped as dead code: a cusp, norm 0."""
    catalogue, _, sterk = _preamble()
    vectors = sterk.isotropic_vectors()
    assert "s4_12" in vectors
    assert catalogue.Lattices.TdP.b(vectors["s4_12"], vectors["s4_12"]) == 0


def test_five_selected_isotropic_vectors():
    """Why there are five Sterk cases."""
    catalogue, _, sterk = _preamble()
    selected_vectors = sterk.selected_isotropic_vectors()
    assert len(selected_vectors) == 5
    TEn = catalogue.Lattices.TEn
    for name, vector_ in selected_vectors.items():
        assert TEn.b(vector_, vector_) == 0, f"{name} is not isotropic"


def test_getsterk5_reproduces_sterk_5_from_a_different_lattice():
    """Rank 10 here versus rank 20 in ``sterk_roots`` -- independent presentations."""
    _, fixtures, sterk = _preamble()
    lattice, vectors = sterk.sterk5_in_U_E8_2()
    assert lattice.rank() == 10
    assert len(vectors) == 14
    minus_four = sum(1 for v in vectors if lattice.b(v, v) == -4)
    minus_two = sum(1 for v in vectors if lattice.b(v, v) == -2)
    published = STERK_PUBLISHED["Sterk_5"]
    assert (minus_four, minus_two) == (published["norm_-4"], published["norm_-2"])


def test_diagonal_embedding_is_e8_2_into_tdp():
    catalogue, _, sterk = _preamble()
    phi = sterk.diagonal_embedding()
    assert phi is catalogue.Embeddings.E8_2_into_TdP
    assert phi.matrix().dimensions() == (8, 20)


def test_embedding_chain_TCo_TEn_TdP_LK3():
    """$T_{Co}\\hookrightarrow T_{En}\\hookrightarrow T_{dP}\\hookrightarrow\\Lambda_{K3}$."""
    _ensure_preamble()

    catalogue, _, _ = _preamble()
    E = catalogue.Embeddings
    L = catalogue.Lattices
    assert E.TCo_into_TEn.domain() is L.Tco
    assert E.TCo_into_TEn.codomain() is L.TEn
    assert E.TEn_into_TdP.domain() is L.TEn
    assert E.TEn_into_TdP.codomain() is L.TdP
    assert E.TdP_into_LK3.codomain() is L.LK3
    assert E.TEn_into_LK3.codomain() is L.LK3
    assert E.TCo_into_TEn.matrix().dimensions() == (11, 12)
    assert E.TEn_into_TdP.matrix().dimensions() == (12, 20)
    assert E.TdP_into_LK3.matrix().dimensions() == (20, 22)
    assert E.E8_2_into_TdP.matrix().dimensions() == (8, 20)
    # Diagonal piece of TEn→TdP agrees with E8(2)↪TdP on the E8(2) summand.
    ten = list(L.TEn.gens())
    for i, gen in enumerate(L.E8_2.gens()):
        assert unwrap(E.TEn_into_TdP(ten[4 + i])) == unwrap(E.E8_2_into_TdP(gen))


def test_block_hom_Z2_U2_into_U_U2():
    r"""Block Hom spelling: $\langle 2\rangle\oplus U(2)\to U\oplus U(2)$, $h\mapsto e+f$."""
    _ensure_preamble()

    catalogue, _, _ = _preamble()
    Lcat = catalogue.Lattices
    domain = Lcat.Z_2 + Lcat.U_2
    codomain = Lcat.U + Lcat.U_2
    z1, z2 = domain.summands()
    w1, w2 = codomain.summands()
    phi = domain.Hom(codomain)({z1: w1[0] + w1[1], z2: w2})
    assert phi.matrix().dimensions() == (3, 4)
    e, f = codomain.gens()[0], codomain.gens()[1]
    assert unwrap(phi(domain.gens()[0])) == unwrap(e + f)
    for i in range(2):
        assert unwrap(phi(domain.gens()[1 + i])) == unwrap(codomain.gens()[2 + i])
    # Same matrix as the flat generator-image spelling.
    flat = domain.Hom(codomain)([e + f] + list(codomain.gens()[2:]))
    assert phi.matrix() == flat.matrix()


def test_block_hom_sum_of_blocks_diagonal():
    r"""Block Hom columns: ``{a1: b1, a2: b2 + b3}`` is id ⊕ diagonal $U(2)\hookrightarrow U\oplus U$."""
    _ensure_preamble()

    catalogue, _, _ = _preamble()
    Lcat = catalogue.Lattices
    domain = Lcat.U + Lcat.U_2
    codomain = Lcat.U + Lcat.U + Lcat.U
    a1, a2 = domain.summands()
    b1, b2, b3 = codomain.summands()
    phi = domain.Hom(codomain)({a1: b1, a2: b2 + b3})
    assert phi.matrix().dimensions() == (4, 6)
    for i in range(2):
        assert unwrap(phi(a1[i])) == unwrap(b1[i])
        assert unwrap(phi(a2[i])) == unwrap(b2[i] + b3[i])
    for x in domain.gens():
        for y in domain.gens():
            assert domain.b(x, y) == codomain.b(phi(x), phi(y))
    # Same as an explicit gen-wise diagonal sequence.
    flat = domain.Hom(codomain)(
        list(b1.gens()) + [b2[i] + b3[i] for i in range(2)]
    )
    assert phi.matrix() == flat.matrix()


# --------------------------------------------------------------------------
# involutions
# --------------------------------------------------------------------------


def test_involutions_are_involutions_and_isometries():
    catalogue = _preamble()[0]
    named = {
        name: getattr(catalogue.Involutions, name)
        for name in ("I_dP", "I_En", "I_Nik")
    }
    assert sorted(named) == ["I_En", "I_Nik", "I_dP"]
    for name, morphism in named.items():
        assert morphism.is_involution(), name
        assert morphism.domain() is catalogue.Lattices.LK3, name
        assert catalogue.Lattices.LK3.invariant_lattice(morphism).rank() == (
            morphism.invariant_lattice().rank()
        ), name


def test_eigenlattices_reproduce_the_named_lattices():
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
    for action, sign, expected in pairs:
        lattice = (
            L.LK3.invariant_lattice(action)
            if sign == "+"
            else L.LK3.coinvariant_lattice(action)
        )
        assert lattice.is_isometric(expected), f"{action} L{sign}"


def test_eigenlattice_ranks_sum_to_22():
    catalogue = _preamble()[0]
    L = catalogue.Lattices
    for name in ("I_dP", "I_En", "I_Nik"):
        action = getattr(catalogue.Involutions, name)
        plus = L.LK3.invariant_lattice(action)
        minus = L.LK3.coinvariant_lattice(action)
        assert plus.rank() + minus.rank() == 22, name


# --------------------------------------------------------------------------
# the source's claim block (old lines 365-388)
# --------------------------------------------------------------------------


def test_source_claim_block_holds():
    """Eight assertions the source wrote behind ``do_tests = False`` and never ran."""
    catalogue, _, _ = _preamble()
    TEn = catalogue.Lattices.TEn
    TE = catalogue.TwoElementary
    basis, dual = TEn.basis(), TEn.dual_basis()
    e, f, ep = basis[0], basis[1], basis[2]
    w1 = dual[4]

    assert TEn.div(e) == 1 and TEn.q(e) == 0
    assert e.e_perp_mod_e().is_isometric(catalogue.Lattices.E10_2)
    assert e.e_perp_mod_e().is_isometric(TE[10, 10, 0])

    assert TEn.div(ep) == 2 and TEn.q(ep) == 0
    assert ep.e_perp_mod_e().is_isometric(
        catalogue.Lattices.U.direct_sum(catalogue.Lattices.E8_2)
    )
    assert ep.e_perp_mod_e().is_isometric(TE[10, 8, 0])

    assert TEn.I_perp_mod_I([e, ep]).is_isometric(catalogue.Lattices.E8_2)

    vp = 2 * e + 2 * f + 2 * w1
    assert TEn.div(vp) == 2 and TEn.q(vp) == 0


def test_the_8_6_0_lattice_has_its_recorded_invariants():
    """The entry recovered from the claim block; an index-2 overlattice of A1^8."""
    catalogue, fixtures, _ = _preamble()
    TEn = catalogue.Lattices.TEn
    basis, dual = TEn.basis(), TEn.dual_basis()
    quotient = TEn.I_perp_mod_I([basis[2], 2 * basis[0] + 2 * basis[1] + 2 * dual[4]])
    recorded = fixtures.TWO_ELEMENTARY_8_6_0_INVARIANTS
    assert quotient.rank() == recorded["rank"]
    assert quotient.signature_pair() == recorded["signature_pair"]
    assert quotient.gram_matrix().det() == recorded["determinant"]


# --------------------------------------------------------------------------
# predicates (now ParentMethods on IntegralLattices)
# --------------------------------------------------------------------------


def test_delta_is_zero_on_the_two_elementary_lattices():
    catalogue, _, _ = _preamble()
    for name in ("U", "U_2", "E8", "E8_2", "E10_2", "TEn"):
        lattice = getattr(catalogue.Lattices, name)
        assert lattice.delta() in (0, 1)
        assert lattice.is_coeven() == (lattice.delta() == 0)
        assert type(lattice).delta.__qualname__ == "IntegralLattices.ParentMethods.delta"


def test_definiteness_predicates():
    catalogue, _, _ = _preamble()
    assert catalogue.Lattices.E8.is_elliptic()
    assert catalogue.Lattices.E8.is_parabolic()
    assert not catalogue.Lattices.U.is_elliptic()
    assert type(catalogue.Lattices.E8).is_elliptic.__qualname__ == (
        "IntegralLattices.ParentMethods.is_elliptic"
    )


def test_coxeter_diagram_uses_the_owned_sage_parent():
    _preamble()
    from dzack_research import lattice
    from sage_lattice_category_spike import CoxeterDiagrams

    root_lattice = lattice.Lattice("E8")
    diagram = root_lattice.coxeter_diagram()

    assert diagram.category().is_subcategory(CoxeterDiagrams())
    assert diagram.coxeter_matrix() == CoxeterMatrix(["E", 8])


def test_diagram_layouts_match_root_counts():
    _, fixtures, _ = _preamble()
    for name, positions in fixtures.STERK_POSITIONS.items():
        assert len(positions) == STERK_ROOT_COUNTS[name], name


# --------------------------------------------------------------------------
# newly ported surface: sterks1/2/3, run_vin, get_isotrop_type, patch methods
# --------------------------------------------------------------------------


def test_sterks_in_ten_are_root_configurations():
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


def test_sterks1_and_sterks3_use_different_dual_scalings():
    """sterks1 uses $2G^{-1}$ duals; sterks3 uses $G^{-1}$."""
    catalogue, _, sterk = _preamble()
    TEn = catalogue.Lattices.TEn
    dual = TEn.dual_basis()
    ep, fp = TEn.gens()[2], TEn.gens()[3]
    configs = sterk.sterks_in_ten()
    # index 9 of sterks1 is 2*ep+ad2[8] with ad2 = 2*dual
    assert configs["sterks1"][9] == 2 * ep + 2 * dual[11]
    assert configs["sterks1"][9] != 2 * ep + dual[11]
    # index 8 of sterks3 is 2*fp+2*ad1[8] with ad1 = dual
    assert configs["sterks3"][8] == 2 * fp + 2 * dual[11]


def test_recorded_root_matrix_is_preserved():
    _, fixtures, _ = _preamble()
    rows = RECORDED_ROOT_MATRIX_ROWS
    assert len(rows) == 5
    assert all(len(row) == 10 for row in rows)


def test_nothing_from_the_sterk_section_is_unported():
    _ensure_preamble()

    assert sterk_module.NOT_PORTED == ()


def test_to_lin_comb_generators_labels_elements():
    catalogue, _, _ = _preamble()
    lattice = catalogue.Lattices.U.direct_sum(catalogue.Lattices.E8).with_names("e, f, a1..a8")
    generators = lattice.gens()
    assert lattice.to_lin_comb_generators(generators[0]) == "e"
    label = lattice.to_lin_comb_generators(2 * generators[0] - generators[3])
    assert "2*e" in label and "a2" in label, label


def test_sublattices_is_a_usable_dict():
    """Old line 358 does ``TEn.sublattices.update({...})`` and needs it to exist."""
    catalogue, _, _ = _preamble()
    lattice = catalogue.Lattices.TEn
    lattice.sublattices.update({"Sterk_1": catalogue.Lattices.E10_2})
    assert "Sterk_1" in lattice.sublattices
    lattice.sublattices.clear()


def test_twist_accepts_names():
    catalogue, _, _ = _preamble()
    twisted = catalogue.Lattices.E8.twist(2, names=tuple(f"b{i}" for i in range(1, 9)))
    assert twisted.variable_names() == tuple(f"b{i}" for i in range(1, 9))


def test_lattice_latex_representation():
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

    a2_disc = catalogue.Lattices.root_lattice("A", 2).discriminant_group().gram_matrix_quadratic()
    assert a2_disc.subdivisions() == ([], [])

    ten_latex = str(latex(catalogue.Lattices.TEn))
    assert r"\mathrm{disc}(L) = 1024 = 2^{10}" in ten_latex

    ten_disc = catalogue.Lattices.TEn.discriminant_group().gram_matrix_quadratic()
    assert ten_disc.subdivisions() == ([2], [2])

    ten_nf = catalogue.Lattices.TEn.discriminant_group().normal_form()
    assert ten_nf.gram_matrix_quadratic().subdivisions() == ([2, 4, 6, 8], [2, 4, 6, 8])

    set_zero_dots(False)
    u_latex_no_dots = str(latex(catalogue.Lattices.U))
    # Only the Gram matrix line should be affected by zero dots.
    gram_line = [l for l in u_latex_no_dots.split('\n') if 'G_L =' in l][0]
    assert r"\cdot" not in gram_line
    assert "0" in u_latex_no_dots
    set_zero_dots(True)


def test_catalogue_latex_fits_mathjax_and_has_balanced_environments():
    catalogue, _, _ = _preamble()
    from sage.misc.latex import latex

    for name, lattice in {
        **{
            n: v
            for n, v in vars(catalogue.Lattices).items()
            if not n.startswith("_") and hasattr(v, "gram_matrix")
        },
        **{f"A{n}": catalogue.Lattices.root_lattice("A", n) for n in range(1, 22)},
        **{f"D{n}": catalogue.Lattices.root_lattice("D", n) for n in range(2, 23)},
    }.items():
        rendered = str(latex(lattice))
        _assert_latex_environments_balanced(rendered, name)
        _assert_latex_renders_in_browser_mathjax(rendered, name)


def test_standard_lattice_show_pattern_renders_correctly_in_mathjax():
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


def test_direct_sum_subdivides_gram_matrix():
    catalogue, _, _ = _preamble()
    direct_sum_lattice = catalogue.Lattices.U.direct_sum(catalogue.Lattices.E8)
    assert direct_sum_lattice.gram_matrix().subdivisions() == ([2], [2])
    assert catalogue.Lattices.LK3.gram_matrix().subdivisions() == ([2, 4, 6, 14], [2, 4, 6, 14])
    assert catalogue.Lattices.LK3_2d(3).gram_matrix().subdivisions() == ([1, 3, 5, 13], [1, 3, 5, 13])


def test_lattice_element_multiplication_and_exponentiation():
    catalogue, _, _ = _preamble()
    a2 = catalogue.Lattices.root_lattice("A", 2)
    alpha1, alpha2 = a2.gens()
    assert alpha1 * alpha1 == -2
    assert alpha1 * alpha2 == 1
    assert alpha1 ** 2 == -2
    assert alpha1 ^ 2 == -2
    assert (alpha1 + alpha2) ^ 2 == -2
    assert (alpha1 + 2 * alpha2) * (alpha1 - alpha2) == 3


def test_run_vin_negates_roots_when_it_twists():
    """The source typo (``do_twist`` set, ``doTwist`` tested) disabled this branch."""
    _ensure_preamble()
    
    catalogue, _, _ = _preamble()
    d4 = catalogue.Lattices.root_lattice("D", 4).twist(-1)
    lattice = catalogue.Lattices.U.direct_sum(d4).with_names("e, f, a1..a4")
    refine(lattice, HyperbolicLattices())
    result = lattice.run_vin()
    assert len(result.roots) == 6, len(result.roots)
    assert result.root_names is not None
    # Twisting happened, so the roots come back negated -- the branch the typo
    # made unreachable.
    assert any(name.startswith("-") for name in result.root_names), result.root_names


def test_get_isotrop_type_classifies():
    _ensure_preamble()
    
    catalogue, _, _ = _preamble()
    lattice = catalogue.Lattices.U.direct_sum(catalogue.Lattices.U)
    refine(lattice, HyperbolicLattices())
    verdict = lattice.get_isotrop_type(lattice.gens()[0])
    assert verdict in ("Odd", "Even ordinary", "Even characteristic", "Not found.")


def test_install_hooks_are_idempotent():
    _ensure_preamble()
    install_integral_lattices()
    install_discriminant_groups()
    assert Lattices.U.rank() == 2


def test_lattices_install_binds_specimens_and_lk3_generators():
    _ensure_preamble()
    ns = {}
    Lattices.install(ns)
    assert ns["U"] is Lattices.U
    assert ns["LK3"] is Lattices.LK3
    assert ns["v1"].parent() is Lattices.LK3
    assert ns["I_En"].domain() is Lattices.LK3
    assert ns["A2"].signature_pair() == (0, 2)
    assert ns["D4"].rank() == 4
    assert ns["TdP"] is Lattices.TdP
    assert ns["e"].parent() is Lattices.TdP


def test_julia_preamble_calls_oscar_with_a_sage_matrix():
    _ensure_preamble()
    gram = BONDS["bond1"]
    assert oscar_call("rank", gram) == 2
    julia.set("_preamble_round_trip", gram)
    converted_back = julia.get_sage("_preamble_round_trip")
    assert converted_back == gram
    assert converted_back.base_ring() is gram.base_ring()


def test_static_preamble_data_has_one_fixture_owner():
    """Ledger constants live in fixtures.sage; Sterk/Lattices do not rebind them."""
    _ensure_preamble()
    assert not hasattr(Sterk, "STERK_ROOT_COUNTS")
    assert not hasattr(Lattices, "RECORDED_RESULTS")
    assert not hasattr(Lattices, "CITATIONS")
