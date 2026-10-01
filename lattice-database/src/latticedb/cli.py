"""Command line of the lattice database: add records, validate the corpus, build the site, deploy it."""

import json
import sys
from pathlib import Path
from typing import Annotated
from urllib.request import Request, urlopen

import frontmatter
from cyclopts import App, Parameter
from pydantic import ValidationError

from latticedb import corpus, nebe_sloane, records, site
from latticedb.model import Lattice, Yaml

SERVED = Path("/var/www/static-sites/lattice-database")
ADDRESS = "http://127.0.0.1/"
HOST = "lattice-database.localhost"

app = App(name="latticedb", help=__doc__)

Root = Annotated[Path, Parameter(help="Directory that holds `lattices/` and `pages/`.")]
Aliases = Annotated[tuple[str, ...], Parameter(name="--alias", help="Another name of the lattice, as plain text; repeat for each one.")]
Families = Annotated[tuple[str, ...], Parameter(name="--family", help="A family that contains the lattice; repeat for each one.")]


def _record_problems(error: ValidationError) -> list[str]:
    return [f"{'.'.join(str(part) for part in problem['loc']) or 'record'}: {problem['msg']} [{problem['type']}]" for problem in error.errors()]


def _admit(root: Root, declared: dict[str, Yaml], prose: str) -> Path:
    """Compute the derived fields of a new record, check it by itself and against the corpus, and write it under the next tag."""
    loaded = corpus.load(root)
    tag = corpus.next_tag(loaded)
    record = records.derive({"tag": tag, **declared})
    # Pydantic reports the problems of a record only through this exception.
    try:
        lattice = Lattice.model_validate(record)
    except ValidationError as error:
        print("\n".join(_record_problems(error)), file=sys.stderr)
        sys.exit(1)
    path = root / "lattices" / f"{tag}.md"
    found = corpus.problems([*loaded.entries, corpus.Entry(lattice, prose, path)], loaded.families, loaded.retired)
    if found:
        print("\n".join(found), file=sys.stderr)
        sys.exit(1)
    path.write_text(records.record_text(record, prose))
    return path


@app.command
def new(
    *,
    gram: Annotated[str, Parameter(help="The components b(e_i, e_j) as JSON rows of integers or strings `p/q`: `[[2, 1], [1, 2]]`.")],
    name: Annotated[str, Parameter(help="Name as plain text.")],
    latex: Annotated[str, Parameter(help="Name as TeX, without math delimiters.")],
    source: Annotated[str, Parameter(help="Where the Gram tensor comes from, as one or two sentences.")],
    alias: Aliases = (),
    family: Families = (),
    url: Annotated[str | None, Parameter(help="Address of the source.")] = None,
    reference: Annotated[tuple[str, ...], Parameter(help="A bibliographic citation as plain text; repeat for each one.")] = (),
    prose: Annotated[str, Parameter(help="The notes of the record, in Pandoc Markdown.")] = "",
    root: Root = Path(),
) -> None:
    """Write the record of a new lattice: the fields that the Gram tensor determines are computed, the others are the options."""
    provenance: dict[str, Yaml] = {"source": source}
    if url is not None:
        provenance["url"] = url
    declared: dict[str, Yaml] = {
        "name": name,
        "latex": latex,
        "aliases": list(alias),
        "gram_tensor": json.loads(gram),
        "families": list(family),
        "related": [],
        "references": [{"citation": citation} for citation in reference],
        "provenance": provenance,
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
def derive(root: Root = Path()) -> None:
    """Compute again, in every record, each field that the Gram tensor determines, and write the records that change."""
    written = 0
    for path in sorted((root / "lattices").glob("*.md")):
        text = path.read_text()
        document = frontmatter.loads(text)
        updated = records.record_text(records.derive(document.metadata), document.content)
        if updated != text:
            path.write_text(updated)
            written += 1
            print(path)
    print(f"{written} records written")


@app.command
def check(root: Root = Path()) -> None:
    """Validate every record of the corpus. Prints each problem and exits with status 1 when a record is not well defined."""
    try:
        loaded = corpus.load(root)
    except corpus.CorpusInvalid as invalid:
        print("\n".join(invalid.problems), file=sys.stderr)
        print(f"{len(invalid.problems)} problems", file=sys.stderr)
        sys.exit(1)
    print(f"{len(loaded.entries)} lattices, all records valid")


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
