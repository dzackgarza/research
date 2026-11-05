"""Caller-visible acceptance survey for research#219.

Each check answers one question about one boundary: when the requested operation fails,
can the *caller* tell?  Where the failure is not a bug -- an unparseable ``.pyx``, a bulk
scan that meets one unreadable file -- the check is that the recovery is carried on the
result, so recovery is distinguishable from success.

The catalogue follows the population listed in the issue's "Remaining work and
acceptance".  The three checks marked (audit) are the sites the independent review named
after 30df268; b15 is the one that matters most, because the previous survey reached the
fixed ``_add_source_list`` catch only through ``_process_inline_citations``, which raises
first and therefore never tested it.
"""

import ast
import os
import shutil
import sys
import tempfile
import traceback
import types
from pathlib import Path

HERE = Path(__file__).resolve()
REPO = HERE.parents[2]
SCRIPTS = REPO / "computations" / "scripts"
sys.path.insert(0, str(SCRIPTS))
sys.path.insert(0, str(SCRIPTS / "sagemath_doc_search"))

TMP = REPO / ".scratch" / "acceptance-219"
if TMP.exists():
    shutil.rmtree(TMP)
TMP.mkdir(parents=True)
tempfile.tempdir = str(TMP)

# Use the real haystack Document when it is installed: the survey should exercise what
# the search app constructs, and only fall back to a stub when the dependency is absent.
try:
    from haystack.dataclasses import Document

    DOCUMENT_SOURCE = "haystack"
except ImportError:  # pragma: no cover - depends on the environment
    _hay = types.ModuleType("haystack")
    _haydc = types.ModuleType("haystack.dataclasses")

    class Document:  # type: ignore[no-redef]
        def __init__(self, content=None, meta=None):
            self.content, self.meta = content, meta or {}

    _haydc.Document = Document
    _hay.dataclasses = _haydc
    sys.modules["haystack"] = _hay
    sys.modules["haystack.dataclasses"] = _haydc
    DOCUMENT_SOURCE = "stub"

_pkg = types.ModuleType("sagemath_doc_search")
_pkg.__path__ = [str(SCRIPTS / "sagemath_doc_search")]
sys.modules.setdefault("sagemath_doc_search", _pkg)

import citation_utils as cu  # noqa: E402
import inline_citation_enhancer as ice  # noqa: E402
import sagemath_utils as su  # noqa: E402

sys.modules["sagemath_doc_search.citation_utils"] = cu
# The package stub has to answer `from sagemath_doc_search import ...` with the same
# module objects the survey uses elsewhere, or a failure would surface as a second,
# unrelated error class.
_pkg.extract_python_docstrings = su.extract_python_docstrings
_pkg.get_sage_path = su.get_sage_path
_pkg.get_sagemath_patterns = su.get_sagemath_patterns


# --------------------------------------------------------------------------- harness

RESULTS = []


def check(label, fn):
    try:
        fn()
    except AssertionError as exc:
        RESULTS.append((label, False, str(exc) or "assertion failed"))
    except Exception as exc:  # an unexpected exception is a failed check, not a crash
        RESULTS.append((label, False, "%s: %s" % (type(exc).__name__, exc)))
    else:
        RESULTS.append((label, True, ""))


def expect(exc_type, fn, *args, **kwargs):
    """Run fn, returning the raised exc_type; any other outcome fails the check."""
    try:
        out = fn(*args, **kwargs)
    except exc_type as exc:
        return exc
    except Exception as exc:
        raise AssertionError(
            "raised %s(%s), expected %s" % (type(exc).__name__, exc, exc_type.__name__)
        )
    raise AssertionError("returned %r, expected %s" % (out, exc_type.__name__))


def innermost(tb):
    frames = traceback.extract_tb(tb)
    return frames[-1].name if frames else ""


class sage_root:
    """Point the scan at a temporary Sage tree, restoring SAGE_PATH afterwards."""

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.saved = os.environ.get("SAGE_PATH")
        os.environ["SAGE_PATH"] = str(self.path)
        return self.path

    def __exit__(self, *exc_info):
        if self.saved is None:
            os.environ.pop("SAGE_PATH", None)
        else:
            os.environ["SAGE_PATH"] = self.saved
        return False


class ctags_index:
    """Point symbol lookup at a temporary index path, restoring it afterwards."""

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.saved = su.CTAGS_INDEX_PATH
        su.CTAGS_INDEX_PATH = self.path
        return self.path

    def __exit__(self, *exc_info):
        su.CTAGS_INDEX_PATH = self.saved
        return False


def sample_docs():
    return [
        ice.Document(
            content="class Lattice:\n    def discriminant(self):\n        pass\n",
            meta={
                "citation_id": "src1",
                "relative_path": "src/sage/modules/lattice.py",
                "citation_display": "lattice.py (Lattice)",
            },
        ),
        ice.Document(
            content="Tutorial on Lattices\n====================\n\nLattices are lattices.\n",
            meta={
                "citation_id": "src2",
                "relative_path": "src/doc/en/tutorial/lattices.rst",
                "citation_display": "lattices, Tutorial on Lattices",
            },
        ),
    ]


def broken_link(*args, **kwargs):
    raise KeyError("badlink")


# The short-response citation path is bypassed only by a response that is both long and
# free of (srcN) markers; anything shorter is rewritten by _add_single_citation first.
LONG_WITHOUT_CITATION = (
    "This answer is deliberately long and carries no inline citation marker at all, so "
    "post-processing goes straight to the source list."
)


# Stand-in for universal-ctags, which this machine does not have. It honours the CLI
# surface the index builder actually uses and writes the real tags format, so the check
# exercises our subprocess call, success branch and parser rather than the tool.
FAKE_CTAGS = '''#!/usr/bin/env python3
"""Stand-in for universal-ctags: the CLI surface the index builder uses."""
import os
import sys
from pathlib import Path

argv = sys.argv[1:]
out = Path(argv[argv.index("-f") + 1])
root = Path(argv[-1])
sep = chr(9)
log = os.environ.get("CTAGS_STUB_LOG")
if log:
    with open(log, "a", encoding="utf-8") as fh:
        fh.write("call\\n")
lines = ["!_TAG_FILE_FORMAT" + sep + "2"]
for source in sorted(root.rglob("*.py")):
    for number, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
        stripped = line.strip()
        if stripped.startswith("class "):
            name = stripped[6:].split("(")[0].split(":")[0].strip()
            relative = source.relative_to(root.parent.parent)
            lines.append(
                name + sep + str(relative) + sep + "/^" + stripped + "$/" + sep
                + "line:" + str(number))
out.write_text("\\n".join(lines) + "\\n", encoding="utf-8")
'''


def _stub_streamlit(recorded):
    """A recording stand-in for the Streamlit calls the indexing path makes."""

    class _Call:
        def __init__(self, name):
            self._name = name

        def __getattr__(self, name):
            return _Call(self._name + "." + name)

        def __call__(self, *args, **kwargs):
            recorded.append((self._name, args))
            if self._name == "cache_data":
                if args and callable(args[0]):
                    return args[0]
                return lambda fn: fn
            if self._name.split(".")[-1] in ("expander", "spinner", "status"):
                class _Context:
                    def __enter__(self):
                        return self

                    def __exit__(self, *exc_info):
                        return False

                return _Context()
            return None

    class _Module(types.ModuleType):
        def __getattr__(self, name):
            return _Call(name)

    module = _Module("streamlit")
    module.session_state = {}
    return module


def exec_module_functions(path):
    """Execute a script's imports and top-level defs, skipping its application body.

    `HayStack_Doc_Search` is a Streamlit script: its app body runs at import, so a plain
    import launches the app.  This runs the module's own source for the pieces under test
    -- the shipped code, not a transcription of it.
    """
    tree = ast.parse(path.read_text())
    keep = [
        node
        for node in tree.body
        if isinstance(node, (ast.Import, ast.ImportFrom, ast.FunctionDef))
    ]
    namespace = {"__name__": path.stem + "_functions", "__file__": str(path)}
    exec(compile(ast.Module(body=keep, type_ignores=[]), str(path), "exec"), namespace)
    return namespace


# ------------------------------------------------------- sagemath_utils: read/parse

def b0_docstrings_still_work():
    doc = su.extract_python_docstrings(Path(su.__file__))
    assert isinstance(doc, str) and doc.extraction == "docstrings", doc.extraction
    assert len(doc) > 200, "extraction returned %d characters" % len(doc)


def b1_read_failure():
    missing = TMP / "absent.py"
    exc = expect(su.DocumentationReadError, su.extract_python_docstrings, missing)
    assert "absent.py" in str(exc) and "FileNotFoundError" in str(exc), str(exc)
    assert isinstance(exc.original, FileNotFoundError), exc.original

    class Ghost:
        name = "ghost.py"

    # A non-path argument fails at open(): the object itself, not a guessed name, is what
    # the caller is told about.
    exc = expect(su.DocumentationReadError, su.extract_python_docstrings, Ghost())
    assert "Ghost" in str(exc) and "TypeError" in str(exc), str(exc)


def b2_syntax_recovery_is_flagged():
    p = TMP / "things.pyx"
    p.write_text('cdef int f(int x):\n    """Double x."""\n    return 2 * x\n')
    doc = su.extract_python_docstrings(p)
    assert doc.extraction == "raw-syntax-error", doc.extraction
    assert isinstance(doc.recovered_from, SyntaxError), doc.recovered_from
    assert isinstance(doc, str)


def b3_no_docstring_recovery_is_flagged():
    p = TMP / "bare.py"
    p.write_text("X = 1\n")
    doc = su.extract_python_docstrings(p)
    assert doc.extraction == "raw-no-docstrings", doc.extraction
    assert doc.recovered_from is None, doc.recovered_from


def b4_empty_file_is_flagged():
    p = TMP / "empty.py"
    p.write_text("\n\n")
    doc = su.extract_python_docstrings(p)
    assert doc == "" and doc.extraction == "empty-file", doc.extraction


def b5_missing_sage_root():
    with sage_root(TMP / "no-sage-here"):
        exc = expect(su.DocumentationReadError, su.find_sagemath_files)
    assert "no-sage-here" in str(exc), str(exc)


def b6_per_file_skip_is_carried():
    root = TMP / "sage-tree"
    modules = root / "src" / "sage" / "modules"
    modules.mkdir(parents=True)
    (modules / "lattice.py").write_text('class Lattice:\n    """A lattice."""\n')
    (modules / "broken.py").symlink_to(TMP / "gone.py")

    with sage_root(root):
        catalog = su.find_sagemath_files()

    assert len(catalog) == 1, [str(d["path"]) for d in catalog]
    assert len(catalog.skipped) == 1, catalog.skipped
    skipped_path, skipped_exc = catalog.skipped[0]
    assert skipped_path.name == "broken.py", skipped_path
    assert isinstance(skipped_exc, FileNotFoundError), skipped_exc
    # The recovery is a convenience, not a way to hide a scan that read nothing.
    assert catalog.raise_if_nothing_read() is catalog

    only_broken = TMP / "sage-tree-broken"
    (only_broken / "src" / "sage").mkdir(parents=True)
    (only_broken / "src" / "sage" / "gone.py").symlink_to(TMP / "gone-again.py")
    with sage_root(only_broken):
        catalog = su.find_sagemath_files()
    assert len(catalog) == 0 and len(catalog.skipped) == 1, catalog.skipped
    exc = expect(su.DocumentationReadError, catalog.raise_if_nothing_read)
    assert "gone.py" in str(exc), str(exc)


# ---------------------------------------------------------- sagemath_utils: ctags

def _tags_file():
    f = TMP / "tags"
    f.write_text(
        "Lattice\tsrc/sage/modules/lattice.py\t/^class Lattice:$/\tline:12\n",
        encoding="utf-8",
    )
    return f


def b7_ctags_build_failure():
    with sage_root(TMP / "no-sage-for-ctags"):
        exc = expect(su.CtagsIndexError, su.create_sage_ctags_index)
    assert "no-sage-for-ctags" in str(exc), str(exc)


def b8_ctags_read_failure():
    unreadable = TMP / "ctags-as-directory"
    unreadable.mkdir()
    with ctags_index(unreadable):
        exc = expect(su.CtagsIndexError, su.find_symbol_line_with_sage_index, "Lattice")
    assert "ctags-as-directory" in str(exc), str(exc)
    assert isinstance(exc.original, OSError), exc.original


def b9_ctags_true_negative():
    with ctags_index(_tags_file()):
        found = su.find_symbol_line_with_sage_index("Lattice")
        absent = su.find_symbol_line_with_sage_index("NotThere")
    assert found == (12, "src/sage/modules/lattice.py"), found
    assert absent == (None, None), absent


def b10_line_number_is_not_estimated():
    with ctags_index(_tags_file()):
        assert su.get_primary_line_number("see line 42 for the detail", "a.py") == 42
        assert (
            su.get_primary_line_number("class Nope:\n    pass\n", "src/sage/x.py") is None
        )


# --------------------------------------------------------------- citation_utils

def b11_unknown_line_is_none():
    assert cu.get_primary_line_number("", "src/x.py") is None
    assert cu.get_primary_line_number("no definitions here", "src/x.py") is None
    assert cu.get_primary_line_number("class A:\n    pass\n", "src/x.py") == 1


def b12_unknown_line_emits_no_anchor():
    github = cu.create_file_link("src/x.py", None, "github")
    local = cu.create_file_link("src/x.py", None, "local")
    assert "#L" not in github and ":None" not in github, github
    assert ":None" not in local, local
    assert "#L7" in cu.create_file_link("src/x.py", 7, "github")


def b13_source_without_path():
    doc = types.SimpleNamespace(meta={"citation_id": "src1", "citation_display": "X"})
    exc = expect(cu.CitationSourceError, cu.create_sources_section, [], [doc])
    assert "src1" in str(exc), str(exc)


# ---------------------------------------------------- inline_citation_enhancer

def b14_enhancement_failure():
    class BadMeta(dict):
        def copy(self):
            raise RuntimeError("boom")

    doc = types.SimpleNamespace(content="x", meta=BadMeta())
    exc = expect(
        ice.DocumentationEnhancementError,
        ice.InlineCitationEnhancer().enhance_document_metadata,
        [doc],
    )
    assert "boom" in str(exc), str(exc)


def b15_source_list_link_failure():
    """(audit) The fixed catch in _add_source_list, reached without _process_inline_citations."""
    enhancer = ice.InlineCitationEnhancer()
    saved = cu.create_file_link
    cu.create_file_link = broken_link
    try:
        exc = expect(
            ice.CitationLinkError,
            enhancer.post_process_response_citations,
            LONG_WITHOUT_CITATION,
            sample_docs(),
        )
        direct = expect(
            ice.CitationLinkError, enhancer._add_source_list, "text", sample_docs()
        )
    finally:
        cu.create_file_link = saved

    for raised in (exc, direct):
        assert "src/sage/modules/lattice.py" in str(raised), str(raised)
        assert "badlink" in str(raised), str(raised)
        origin = innermost(raised.__traceback__)
        assert origin == "_add_source_list", "exception was formed in %r" % origin


def b16_inline_link_failure():
    enhancer = ice.InlineCitationEnhancer()
    saved = cu.create_file_link
    cu.create_file_link = broken_link
    try:
        exc = expect(
            ice.CitationLinkError,
            enhancer.post_process_response_citations,
            "answer (src1).",
            sample_docs(),
        )
    finally:
        cu.create_file_link = saved
    origin = innermost(exc.__traceback__)
    assert origin == "replace_citation", "exception was formed in %r" % origin


def b17_missing_citation_utils_is_not_line_one():
    """(audit) _get_line_number: a broken installation is not an unknown line."""
    keys = ("sagemath_doc_search.citation_utils", "citation_utils")
    saved = {k: sys.modules.get(k) for k in keys}
    for k in keys:
        sys.modules[k] = None
    try:
        exc = expect(
            ImportError, ice.InlineCitationEnhancer()._get_line_number, "x", "src/x.py"
        )
    finally:
        for k, v in saved.items():
            if v is None:
                sys.modules.pop(k, None)
            else:
                sys.modules[k] = v
    assert "citation_utils" in str(exc), str(exc)


def b18_happy_path_still_links():
    out = ice.InlineCitationEnhancer().post_process_response_citations(
        "See (src1) and (src2).", sample_docs()
    )
    # The inline markers resolve to the source-list entries, which carry the real links.
    assert 'href="#ref-src1"' in out and 'href="#ref-src2"' in out, out
    assert 'id="ref-src1"' in out and 'id="ref-src2"' in out, out
    assert 'href="file://' in out, out
    assert "doc.sagemath.org/html/en/tutorial/lattices.html" in out, out
    assert "src/sage/modules/lattice.py:1" in out, out


def b19_ctags_success_path():
    """The ctags build succeeds: index written, consumed, and reused without a rebuild.

    This machine has no `ctags`, so the executable is a stand-in that honours the CLI
    surface the builder uses (`-f <out>`, source dir last) and writes the real tags
    format.  What is under test is our side of that contract: the subprocess call, the
    success branch, and the parser reading the file it produced.
    """
    tree = TMP / "ctags-sage"
    (tree / "src" / "sage" / "modules").mkdir(parents=True)
    # Six filler lines put the class on line 7, so the line number proves the index was
    # read rather than defaulted.
    (tree / "src" / "sage" / "modules" / "lattice.py").write_text(
        "# filler\n" * 6 + 'class Lattice:\n    """A lattice."""\n'
    )
    bin_dir = TMP / "bin"
    bin_dir.mkdir()
    stub = bin_dir / "ctags"
    stub.write_text(FAKE_CTAGS)
    stub.chmod(0o755)
    log = TMP / "ctags-calls.log"
    index = TMP / "tags-success"
    saved_path = os.environ.get("PATH", "")
    os.environ["PATH"] = str(bin_dir) + os.pathsep + saved_path
    os.environ["CTAGS_STUB_LOG"] = str(log)
    try:
        with sage_root(tree), ctags_index(index):
            assert su.create_sage_ctags_index() is True
            assert index.exists() and index.stat().st_size > 0, "the index was not written"
            found = su.find_symbol_line_with_sage_index("Lattice")
            line = su.get_primary_line_number(
                "class Lattice:\n    pass\n", "src/sage/modules/lattice.py"
            )
            assert su.create_sage_ctags_index() is True
    finally:
        os.environ["PATH"] = saved_path
        os.environ.pop("CTAGS_STUB_LOG", None)
    assert found == (7, "src/sage/modules/lattice.py"), found
    assert line == 7, line
    # The second call found a fresh index and must not have shelled out again.
    assert log.read_text().count("call") == 1, log.read_text()


def b20_runtime_warning_path():
    """A per-file failure reaches the Streamlit warning, and the scan keeps going.

    `HayStack_Doc_Search` is a Streamlit script whose app body runs at import time, so
    importing it would launch the app.  The check instead executes the module's own
    source for its imports and function definitions -- the shipped code, not a
    transcription -- with only the UI and the LLM generator stubbed.
    """
    saved = {k: sys.modules.get(k) for k in ("streamlit", "dotenv")}
    saved.update(
        {k: v for k, v in sys.modules.items() if k.startswith("haystack.components.generators")}
    )
    recorded = []
    stub_keys = ("streamlit", "dotenv", "haystack.components.generators.openai")
    try:
        sys.modules["streamlit"] = _stub_streamlit(recorded)
        _dotenv = types.ModuleType("dotenv")
        _dotenv.load_dotenv = lambda *a, **k: None
        sys.modules["dotenv"] = _dotenv
        _gen = types.ModuleType("haystack.components.generators.openai")

        class _OpenAIGenerator:
            def __init__(self, *a, **k):
                pass

        _gen.OpenAIGenerator = _OpenAIGenerator
        sys.modules["haystack.components.generators.openai"] = _gen

        module_path = SCRIPTS / "HayStack_Doc_Search.py"
        namespace = exec_module_functions(module_path)
        cache = TMP / "doc-cache"
        cache.mkdir()
        namespace["CACHE_PATH"] = cache

        tree = TMP / "warn-tree"
        tree.mkdir()
        good = tree / "lattices.rst"
        good.write_text("Tutorial\n========\n\nA lattice is a poset with meets and joins.\n")
        broken = tree / "missing.py"
        entry = lambda p, rel, suffix: {
            "path": p,
            "meta": {
                "source": "SageMath Local",
                "relative_path": rel,
                "suffix": suffix,
                "url_source": "file://" + rel,
            },
        }

        store = namespace["InMemoryDocumentStore"]()
        stats = namespace["index_files"](
            [entry(broken, "missing.py", ".py"), entry(good, "lattices.rst", ".rst")],
            store,
            "acceptance-warning",
        )
        warnings = [a[0] for name, a in recorded if name.endswith("warning") and a]
        assert stats.get("processed_files") == 1, stats
        assert len(store.filter_documents()) == 1, "the readable file was not indexed"
        assert len(warnings) == 1, warnings
        assert "missing.py" in warnings[0], warnings[0]
        assert "FileNotFoundError" in warnings[0], warnings[0]

        recorded.clear()
        nothing = namespace["index_files"](
            [entry(broken, "missing.py", ".py")],
            namespace["InMemoryDocumentStore"](),
            "acceptance-nothing",
        )
        warnings = [a[0] for name, a in recorded if name.endswith("warning") and a]
        assert nothing == {}, nothing
        assert "No documents were successfully processed." in warnings, warnings
    finally:
        for key, value in saved.items():
            if value is None:
                sys.modules.pop(key, None)
            else:
                sys.modules[key] = value
        for key in stub_keys:
            if key not in saved:
                sys.modules.pop(key, None)



def b21_malformed_line_field_is_not_a_miss():
    """A matching tag entry with a corrupt `line:` field is corruption, not a miss."""
    f = TMP / "tags-corrupt"
    f.write_text(
        "Lattice\tsrc/sage/modules/lattice.py\t/^class Lattice:$/\tline:notanumber\n",
        encoding="utf-8",
    )
    with ctags_index(f):
        exc = expect(su.CtagsIndexError, su.find_symbol_line_with_sage_index, "Lattice")
    assert "tags-corrupt" in str(exc), str(exc)



def b22_unknown_path_yields_no_unknown_links():
    """A doc with no relative_path fails closed; `file://.../unknown` is never emitted."""
    enhancer = ice.InlineCitationEnhancer()
    docs_nopath = [
        ice.Document(
            content="class Thing:\n    def method(self):\n        pass\n",
            meta={"citation_id": "src1", "citation_display": "thing"},
        )
    ]
    # Long citation-free text reaches the source list; (src1) forces the inline path.
    # Either way the boundary is _add_source_list's up-front sentinel check.
    for text in (LONG_WITHOUT_CITATION, "answer (src1)."):
        exc = expect(
            ice.CitationLinkError,
            enhancer.post_process_response_citations,
            text,
            docs_nopath,
        )
        origin = innermost(exc.__traceback__)
        assert origin == "_add_source_list", "exception was formed in %r" % origin
        assert "no relative_path" in str(exc), str(exc)
    exc = expect(ice.CitationLinkError, enhancer._add_source_list, "text", docs_nopath)
    assert "no relative_path" in str(exc), str(exc)



def b23_malformed_index_line_is_not_a_miss():
    """line:0, line:-1, a missing line field, or garbled bytes are corruption, not a miss.

    Each of these used to be accepted (or silently dropped), turning a corrupt index into
    the same answer as a genuine "no such symbol".
    """
    cases = (
        ("zero", "Lattice\tsrc/x.py\t/^class Lattice:$/\tline:0\n"),
        ("negative", "Lattice\tsrc/x.py\t/^class Lattice:$/\tline:-1\n"),
        ("nofield", "Lattice\tsrc/x.py\t/^class Lattice:$/\tkind:class\n"),
    )
    for label, content in cases:
        fixture = TMP / ("tags-line-" + label)
        fixture.write_text(content, encoding="utf-8")
        with ctags_index(fixture):
            exc = expect(
                su.CtagsIndexError, su.find_symbol_line_with_sage_index, "Lattice"
            )
        assert fixture.name in str(exc), (label, str(exc))
    garbled = TMP / "tags-garbled"
    garbled.write_bytes(b"\xff\xfe\x00not utf-8\t\x80\x81")
    with ctags_index(garbled):
        exc = expect(su.CtagsIndexError, su.find_symbol_line_with_sage_index, "Lattice")
    assert "tags-garbled" in str(exc), str(exc)


def b24_none_or_empty_path_yields_no_link():
    """relative_path None/'' meets the same sentinel boundary as the 'unknown' one."""
    enhancer = ice.InlineCitationEnhancer()
    for value in (None, "", "   "):
        docs = [
            ice.Document(
                content="class Thing:\n    pass\n",
                meta={
                    "citation_id": "src1",
                    "citation_display": "thing",
                    "relative_path": value,
                },
            )
        ]
        exc = expect(ice.CitationLinkError, enhancer._add_source_list, "text", docs)
        assert "no relative_path" in str(exc), (repr(value), str(exc))



def b25_renderer_rejects_every_pathless_form():
    """create_sources_section must not render absent/None/blank/sentinel paths."""
    for value in (None, "", "   ", "unknown"):
        doc = types.SimpleNamespace(
            meta={
                "citation_id": "src1",
                "citation_display": "thing",
                "relative_path": value,
            }
        )
        exc = expect(cu.CitationSourceError, cu.create_sources_section, [], [doc])
        assert "src1" in str(exc), (repr(value), str(exc))
    # and a real path still renders
    good = types.SimpleNamespace(
        meta={
            "citation_id": "src2",
            "citation_display": "lattice.py (discriminant)",
            "relative_path": "src/sage/modules/lattice.py",
        },
    )
    good.content = "class Lattice:\n    pass\n"
    out = cu.create_sources_section([], [good])
    assert "src/sage/modules/lattice.py:1" in out, out


def b26_blank_path_never_becomes_a_working_directory_link():
    """create_file_link("") used to resolve to the cwd, looking like a real file."""
    for value in ("", "   "):
        exc = expect(ValueError, cu.create_file_link, value, None, "local")
        assert "real path" in str(exc), (repr(value), str(exc))
    # the renderer and the primitive agree about the same failure class
    for text, a_kind in (("github", "#L"), ("local", "")):
        link = cu.create_file_link("src/sage/modules/lattice.py", 1, text)
        assert "src/sage/modules/lattice.py" in link, link
    exc = expect(ValueError, cu.create_file_link, "", 7, "github")



def b27_short_matching_record_is_not_a_miss():
    """Short malformed records for the requested symbol raise; for others, they don't.

    The old field-count gate let a matching 2- or 3-field record bypass every check and
    read as "symbol absent".  The same corruption for a *different* symbol is tolerated,
    and an absent symbol is still the true negative.
    """
    short_cases = (
        ("two-fields", "Lattice\tsrc/x.py\n"),
        ("three-fields", "Lattice\tsrc/x.py\t/^class Lattice:$/\n"),
        ("empty-file", "Lattice\t\t/^class Lattice:$/\tline:5\n"),
    )
    for label, content in short_cases:
        fixture = TMP / ("tags-short-" + label)
        fixture.write_text(content, encoding="utf-8")
        with ctags_index(fixture):
            exc = expect(
                su.CtagsIndexError, su.find_symbol_line_with_sage_index, "Lattice"
            )
        assert fixture.name in str(exc), (label, str(exc))
    # corruption in a record for a different symbol must not break this lookup
    mixed = TMP / "tags-mixed"
    mixed.write_text(
        "Other\tsrc/y.py\n"
        "Lattice\tsrc/x.py\t/^class Lattice:$/\tline:7\n",
        encoding="utf-8",
    )
    with ctags_index(mixed):
        assert su.find_symbol_line_with_sage_index("Lattice") == (7, "src/x.py")
    # and an absent symbol is still the honest miss
    with ctags_index(mixed):
        assert su.find_symbol_line_with_sage_index("NotThere") == (None, None)


# --------------------------------------------------------------------------- run

CATALOGUE = [
    ("b0  docstring extraction still works", b0_docstrings_still_work),
    ("b1  read/parse failure -> DocumentationReadError", b1_read_failure),
    ("b2  (audit) unparseable file -> flagged recovery", b2_syntax_recovery_is_flagged),
    ("b3  parsed, no docstrings -> flagged recovery", b3_no_docstring_recovery_is_flagged),
    ("b4  empty file -> flagged, not a silent ''", b4_empty_file_is_flagged),
    ("b5  missing Sage root -> DocumentationReadError", b5_missing_sage_root),
    ("b6  per-file skip carried on the catalog", b6_per_file_skip_is_carried),
    ("b7  (audit) ctags build failure -> CtagsIndexError", b7_ctags_build_failure),
    ("b8  ctags read failure -> CtagsIndexError", b8_ctags_read_failure),
    ("b9  symbol absent -> (None, None) true negative", b9_ctags_true_negative),
    ("b10 undeterminable line -> None, never an estimate", b10_line_number_is_not_estimated),
    ("b11 unknown line -> None, never 1", b11_unknown_line_is_none),
    ("b12 unknown line emits no #LNone anchor", b12_unknown_line_emits_no_anchor),
    ("b13 source without a path -> CitationSourceError", b13_source_without_path),
    ("b14 enhancement failure -> DocumentationEnhancementError", b14_enhancement_failure),
    ("b15 (audit) source-list catch -> CitationLinkError", b15_source_list_link_failure),
    ("b16 inline-link catch -> CitationLinkError", b16_inline_link_failure),
    ("b17 (audit) missing citation_utils -> ImportError", b17_missing_citation_utils_is_not_line_one),
    ("b18 happy path keeps the source-list links", b18_happy_path_still_links),
    ("b19 ctags build succeeds and the index is consumed", b19_ctags_success_path),
    ("b20 per-file failure reaches the Streamlit warning", b20_runtime_warning_path),
    ("b21 corrupt line: field -> CtagsIndexError, not a miss", b21_malformed_line_field_is_not_a_miss),
    ("b22 no relative_path -> CitationLinkError, no unknown link", b22_unknown_path_yields_no_unknown_links),
    ("b23 zero/negative/missing/garbled line -> CtagsIndexError", b23_malformed_index_line_is_not_a_miss),
    ("b24 None/empty relative_path -> CitationLinkError", b24_none_or_empty_path_yields_no_link),
    ("b25 renderer rejects absent/None/blank/sentinel path", b25_renderer_rejects_every_pathless_form),
    ("b26 blank path -> ValueError, not a cwd link", b26_blank_path_never_becomes_a_working_directory_link),
    ("b27 short matching record -> CtagsIndexError, others tolerated", b27_short_matching_record_is_not_a_miss),
]

try:
    for label, fn in CATALOGUE:
        check(label, fn)
finally:
    shutil.rmtree(TMP, ignore_errors=True)

width = max(len(label) for label, _ in CATALOGUE)
print("research#219 acceptance survey (Document: %s)" % DOCUMENT_SOURCE)
for label, ok, detail in RESULTS:
    print("  %-*s  %s%s" % (width, label, "PASS" if ok else "FAIL", "" if ok else ": " + detail))

failed = [label for label, ok, _ in RESULTS if not ok]
print(
    "ACCEPTANCE #219: %s (%d/%d)"
    % ("PASS" if not failed else "FAIL: " + "; ".join(failed), len(RESULTS) - len(failed), len(RESULTS))
)
sys.exit(1 if failed else 0)
