"""Command line of the lattice database: add records, validate the corpus, build the site, deploy it."""

import json
import sys
from importlib.metadata import version
from pathlib import Path
from typing import Annotated
from urllib.request import Request, urlopen

import frontmatter
from cyclopts import App, Parameter
from pydantic import ValidationError

from latticedb import certificates, corpus, genus, hashimoto, hoehn_mason, nebe_sloane, records, site
from latticedb.model import Lattice, Morphisms, Yaml

SERVED = Path("/var/www/static-sites/lattice-database")
ADDRESS = "http://127.0.0.1/"
HOST = "lattice-database.localhost"

app = App(name="latticedb", help=__doc__)

Root = Annotated[Path, Parameter(help="Directory that holds `lattices/` and `pages/`.")]
Aliases = Annotated[tuple[str, ...], Parameter(name="--alias", help="Another name of the lattice, as plain text; repeat for each one.")]
Families = Annotated[tuple[str, ...], Parameter(name="--family", help="A family that contains the lattice; repeat for each one.")]


def _record_problems(error: ValidationError) -> list[str]:
    return [f"{'.'.join(str(part) for part in problem['loc']) or 'record'}: {problem['msg']} [{problem['type']}]" for problem in error.errors()]


def _refuse(found: list[str]) -> None:
    """Print the problems and exit with status 1 when there are any."""
    if found:
        print("\n".join(found), file=sys.stderr)
        sys.exit(1)


def _admit(root: Root, declared: dict[str, Yaml], prose: str) -> Path:
    """Compute the values of a new record once, check it against its declared values and the corpus, and write it under the next tag."""
    loaded = corpus.load(root)
    tag = corpus.next_tag(loaded)
    match declared["families"]:
        case list() as families:
            _refuse(records.gram_problems(records.gram_tensor(declared["gram_tensor"]), tuple(str(family) for family in families)))
        case _:
            raise AssertionError("families is a list of keys of families.yaml")
    record = records.derive({"tag": tag, **declared})
    # Pydantic reports the problems of a record only through this exception.
    try:
        lattice = Lattice.model_validate(record)
    except ValidationError as error:
        _refuse(_record_problems(error))
        sys.exit(1)
    path = root / "lattices" / f"{tag}.md"
    _refuse(records.admission_problems(lattice, {entry.lattice.tag: entry.lattice for entry in loaded.entries}))
    _refuse(corpus.problems([*loaded.entries, corpus.Entry(lattice, prose, path)], loaded.families, loaded.retired))
    path.write_text(records.record_text(record, prose))
    held = certificates.load(root)
    held[f"{tag} derive"] = certificates.Certificate(inputs=certificates.gram_digest(lattice), by=LATTICEDB)
    certificates.save(root, held)
    return path


@app.command
def new(
    *,
    gram: Annotated[str, Parameter(help="The components b(e_i, e_j) as JSON rows of integers or strings `p/q`: `[[2, 1], [1, 2]]`.")],
    name: Annotated[str, Parameter(help="Name as plain text.")],
    latex: Annotated[str, Parameter(help="Name as TeX, without math delimiters.")],
    alias: Aliases = (),
    family: Families = (),
    reference: Annotated[tuple[str, ...], Parameter(help="A bibliographic citation as plain text; repeat for each one.")] = (),
    prose: Annotated[str, Parameter(help="The notes of the record, in Pandoc Markdown.")] = "",
    root: Root = Path(),
) -> None:
    """Write the record of a new lattice: the fields that the Gram tensor determines are computed, the others are the options."""
    declared: dict[str, Yaml] = {
        "name": name,
        "latex": latex,
        "aliases": list(alias),
        "gram_tensor": json.loads(gram),
        "families": list(family),
        "related": [],
        "references": [{"citation": citation} for citation in reference],
    }
    print(_admit(root, declared, prose))


@app.command(name="nebe-sloane")
def nebe_sloane_entry(
    entry: Annotated[str, Parameter(help="Name of the entry in the catalogue: `LAMBDA10`, `K12`, ...")],
    *,
    name: Annotated[str, Parameter(help="Name as plain text.")],
    latex: Annotated[str, Parameter(help="Name as TeX, without math delimiters.")],
    alias: Aliases = (),
    family: Families = (),
    root: Root = Path(),
) -> None:
    """Write the record of an entry of the Catalogue of Lattices (G. Nebe, N. J. A. Sloane).

    The entry is read from `sources/nebe_sloane/<ENTRY>.json`, and fetched into that file first when the file does not exist.
    The invariants that the catalogue states are checked against the ones computed from the Gram tensor.
    """
    stored = nebe_sloane.stored(root / "sources" / "nebe_sloane", entry)
    declared, prose = nebe_sloane.record(stored, name, latex, alias, family)
    nebe_sloane.check(stored, records.derive({"tag": "0000", **declared}))
    print(_admit(root, declared, prose))


@app.command
def morphism(
    source: Annotated[str, Parameter(help="Tag of the source lattice.")],
    target: Annotated[str, Parameter(help="Tag of the target lattice.")],
    *,
    name: Annotated[str, Parameter(help="Name as plain text; TeX between `$` signs is rendered.")],
    matrix: Annotated[str, Parameter(help="JSON rows of integers, rank(target) rows by rank(source) columns: column j is the image of e_j.")],
    description: Annotated[str | None, Parameter(help="One or two sentences on the morphism.")] = None,
    scale: Annotated[int, Parameter(help="The integer c with b_T(phi x, phi y) = c b_S(x, y): a morphism S(c) -> T.")] = 1,
    row_subdivisions: Annotated[str, Parameter(help="JSON list of the lines between rows, as SageMath's `M.subdivisions()[0]`.")] = "[]",
    column_subdivisions: Annotated[str, Parameter(help="JSON list of the lines between columns, as SageMath's `M.subdivisions()[1]`.")] = "[]",
    prose: Annotated[str | None, Parameter(help="Notes of the file in Pandoc Markdown; replaces the notes that are there.")] = None,
    root: Root = Path(),
) -> None:
    """Add a morphism to `morphisms/<SOURCE>-<TARGET>.md`, after a check that it preserves the forms and that the subdivisions cut orthogonal summands."""
    loaded = corpus.load(root)
    path = root / "morphisms" / f"{source}-{target}.md"
    present = [entry for entry in loaded.morphisms if entry.path == path]
    added: dict[str, Yaml] = {
        "name": name,
        "matrix": json.loads(matrix),
        "row_subdivisions": json.loads(row_subdivisions),
        "column_subdivisions": json.loads(column_subdivisions),
    }
    if description is not None:
        added["description"] = description
    if scale != 1:
        added["scale"] = scale
    listed: list[dict[str, Yaml]] = [morphism.model_dump(mode="json", exclude_defaults=True) for entry in present for morphism in entry.morphisms.morphisms]
    notes = prose if prose is not None else (present[0].prose if present else "")
    # Pydantic reports the problems of a record only through this exception.
    try:
        record = Morphisms.model_validate({"source": source, "target": target, "morphisms": [*listed, added]})
    except ValidationError as error:
        _refuse(_record_problems(error))
        sys.exit(1)
    others = [entry for entry in loaded.morphisms if entry.path != path]
    _refuse(corpus.morphism_problems([*others, corpus.MorphismEntry(record, notes, path)], list(loaded.entries), loaded.retired))
    by_tag = {entry.lattice.tag: entry.lattice for entry in loaded.entries}
    _refuse(records.morphism_problems(record.morphisms[-1], by_tag[source], by_tag[target]))
    path.parent.mkdir(exist_ok=True)
    path.write_text(records.morphisms_text(source, target, [*listed, added], notes))
    print(path)


SOURCES = {"hashimoto": (hashimoto.stored_problems, ("hashimoto",)), "hoehn_mason": (hoehn_mason.stored_problems, ("hashimoto", "hoehn_mason"))}
"""Each source checked against the corpus, with its check and the directories under `sources/` that it reads."""

LATTICEDB = f"latticedb {version('latticedb')}"


def _source_inputs(root: Path, loaded: corpus.Corpus, directories: tuple[str, ...]) -> str:
    """The digest of the files of `directories` under `sources/`, the Gram tensors of the records and the morphism files: the inputs of a source check."""
    files = sorted(path for directory in directories for path in (root / "sources" / directory).rglob("*") if path.is_file())
    parts = [path.read_text() for path in files]
    parts += [certificates.gram_digest(entry.lattice) for entry in loaded.entries]
    parts += [entry.path.read_text() for entry in loaded.morphisms]
    return certificates.digest("\n".join(parts))


def _pending(root: Path, loaded: corpus.Corpus, held: certificates.Certificates, seconds: int) -> list[str]:
    """The names of the computations without a certificate for their present inputs."""
    derived = {f"{entry.lattice.tag} derive": certificates.gram_digest(entry.lattice) for entry in loaded.entries}
    checked = {f"source {source}": _source_inputs(root, loaded, directories) for source, (_, directories) in SOURCES.items()}
    names = [name for name, inputs in (derived | checked).items() if not certificates.is_certified(held, name, inputs)]
    names += [genus.name(str(request["tag"]), str(field)) for request in genus.requests(loaded, held, (), seconds) for field in request["fields"]]
    return names


@app.command
def check(root: Root = Path(), seconds: Annotated[int, Parameter(help="Time limit of the computations that `certify` carries out.")] = 120) -> None:
    """Validate every record of the corpus and list the computations without a certificate. Computes nothing; exits with status 1 when a record is not valid."""
    try:
        loaded = corpus.load(root)
    except corpus.CorpusInvalid as invalid:
        print("\n".join(invalid.problems), file=sys.stderr)
        print(f"{len(invalid.problems)} problems", file=sys.stderr)
        sys.exit(1)
    pending = _pending(root, loaded, certificates.load(root), seconds)
    print("\n".join(pending))
    print(f"{len(loaded.entries)} lattices and {len(loaded.morphisms)} morphism files, all records valid; {len(pending)} computations without a certificate")


@app.command
def certify(
    *,
    tag: Annotated[tuple[str, ...], Parameter(help="Tag of a record to compute; repeat for each one. All records and the sources when absent.")] = (),
    seconds: Annotated[int, Parameter(help="Time limit of SageMath for one value of one record.")] = 120,
    root: Root = Path(),
) -> None:
    """Carry out each computation without a certificate for its present inputs, store its values, and write its certificate.

    The fields that `records.derive` computes from the Gram tensor, the checks of the sources against the
    corpus, and the values that SageMath computes. A certified computation is never carried out again.
    """
    loaded = corpus.load(root)
    held = certificates.load(root)
    found: list[str] = []
    for entry in loaded.entries:
        lattice = entry.lattice
        inputs = certificates.gram_digest(lattice)
        if (tag and lattice.tag not in tag) or certificates.is_certified(held, f"{lattice.tag} derive", inputs):
            continue
        text = entry.path.read_text()
        document = frontmatter.loads(text)
        updated = records.record_text(records.derive(document.metadata), document.content)
        if updated != text:
            entry.path.write_text(updated)
            print(f"{entry.path}: derived values written")
        held[f"{lattice.tag} derive"] = certificates.Certificate(inputs=inputs, by=LATTICEDB)
        certificates.save(root, held)
    for source, (stored_problems, directories) in SOURCES.items() if not tag else ():
        inputs = _source_inputs(root, loaded, directories)
        if certificates.is_certified(held, f"source {source}", inputs):
            continue
        problems = stored_problems(root, loaded)
        found.extend(problems)
        if not problems:
            held[f"source {source}"] = certificates.Certificate(inputs=inputs, by=LATTICEDB)
            certificates.save(root, held)
            print(f"sources/{source} agrees with the corpus")
    found.extend(genus.certify(root, loaded, held, tag, seconds))
    _refuse(found)


@app.command
def build(root: Root = Path(), target: Annotated[Path, Parameter(help="Directory for the site. The command replaces it.")] = Path("_site")) -> None:
    """Build the site from the corpus."""
    count = site.build(root, target)
    print(f"{count} lattices -> {target}")


@app.command
def deploy(root: Root = Path()) -> None:
    """Build the site, link it into the directory that nginx serves, and check that nginx serves it."""
    target = (root / "_site").resolve()
    site.build(root, target)
    if not SERVED.is_symlink():
        SERVED.symlink_to(target)
    assert SERVED.resolve() == target, f"{SERVED} links to {SERVED.resolve()}, not to {target}"
    with urlopen(Request(ADDRESS, headers={"Host": HOST})) as response:
        assert response.status == 200, f"{ADDRESS} with host {HOST} returned {response.status}"
    print(f"http://{HOST}/")


@app.command
def next_tag(root: Root = Path()) -> None:
    """Print the tag for the next new record."""
    print(corpus.next_tag(corpus.load(root)))
