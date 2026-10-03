"""Seed, author, enrich, verify, and publish lattice cards."""

import json
import sys
from importlib.metadata import version
from pathlib import Path
from typing import Annotated
from urllib.request import Request, urlopen

import frontmatter
from cyclopts import App, Parameter

from latticedb import (
    bulk_index,
    bulk_sources,
    certificates,
    checks,
    corpus,
    genus,
    records,
    seed,
    site,
    summands,
)
from latticedb.model import Yaml

SERVED = Path("/var/www/static-sites/lattice-database")
ADDRESS = "http://127.0.0.1/"
HOST = "lattice-database.localhost"

app = App(name="latticedb", help=__doc__)

Root = Annotated[Path, Parameter(help="Directory that holds `lattices/` and `pages/`.")]
Aliases = Annotated[
    tuple[str, ...],
    Parameter(
        name="--alias",
        help="Another name of the lattice, as plain text; repeat for each one.",
    ),
]
Families = Annotated[
    tuple[str, ...],
    Parameter(
        name="--family", help="A family that contains the lattice; repeat for each one."
    ),
]


def _refuse(found: list[str]) -> None:
    """Print the problems and exit with status 1 when there are any."""
    if found:
        print("\n".join(found), file=sys.stderr)
        sys.exit(1)


def _author(root: Root, declared: dict[str, Yaml], prose: str) -> Path:
    """Write a new card with a filename-only tag allocation."""
    tag = corpus.next_tag(root)
    path = root / "lattices" / f"{tag}.md"
    with path.open("x") as output:
        output.write(records.record_text({"tag": tag, **declared}, prose))
    return path


@app.command
def new(
    *,
    gram: Annotated[
        str,
        Parameter(
            help="The components b(e_i, e_j) as JSON rows of integers or strings `p/q`: `[[2, 1], [1, 2]]`."
        ),
    ],
    name: Annotated[str, Parameter(help="Name as plain text.")],
    latex: Annotated[str, Parameter(help="Name as TeX, without math delimiters.")],
    alias: Aliases = (),
    family: Families = (),
    reference: Annotated[
        tuple[str, ...],
        Parameter(help="A bibliographic citation as plain text; repeat for each one."),
    ] = (),
    prose: Annotated[
        str, Parameter(help="The notes of the record, in Pandoc Markdown.")
    ] = "",
    root: Root = Path(),
) -> None:
    """Write a lattice card from authored fields, without computation or verification."""
    declared: dict[str, Yaml] = {
        "name": name,
        "latex": latex,
        "aliases": list(alias),
        "gram_tensor": json.loads(gram),
        "families": list(family),
        "related": [],
        "references": [{"citation": citation} for citation in reference],
    }
    print(_author(root, declared, prose))


@app.command(name="bulk-source-fetch")
def bulk_source_fetch(root: Root = Path()) -> None:
    """Store the published Nipp, Brandt–Intrau, and Watson bulk source tables."""
    for path in bulk_sources.fetch(root):
        print(f"sources/{path}")


@app.command(name="bulk-index")
def bulk_index_write(root: Root = Path()) -> None:
    """Store parsed bulk source rows with their exact Gram tensors and determinants."""
    for source, count in bulk_index.write(root).items():
        print(f"sources/normalized/{source}.jsonl.gz: {count} rows")


@app.command(name="seed")
def seed_cards(*, limit: int | None = None, root: Root = Path()) -> None:
    """Write permanent lattice cards from stored source rows without verification or enrichment."""
    seeded, without_gram = seed.run(root, limit)
    print(
        f"{seeded} lattice cards written; {len(without_gram)} source rows need a defining Gram tensor"
    )


@app.command
def morphism(
    source: Annotated[str, Parameter(help="Tag of the source lattice.")],
    target: Annotated[str, Parameter(help="Tag of the target lattice.")],
    *,
    name: Annotated[
        str, Parameter(help="Name as plain text; TeX between `$` signs is rendered.")
    ],
    matrix: Annotated[
        str,
        Parameter(
            help="JSON rows of integers, rank(target) rows by rank(source) columns: column j is the image of e_j."
        ),
    ],
    description: Annotated[
        str | None, Parameter(help="One or two sentences on the morphism.")
    ] = None,
    scale: Annotated[
        int,
        Parameter(
            help="The integer c with b_T(phi x, phi y) = c b_S(x, y): a morphism S(c) -> T."
        ),
    ] = 1,
    row_subdivisions: Annotated[
        str,
        Parameter(
            help="JSON list of the lines between rows, as SageMath's `M.subdivisions()[0]`."
        ),
    ] = "[]",
    column_subdivisions: Annotated[
        str,
        Parameter(
            help="JSON list of the lines between columns, as SageMath's `M.subdivisions()[1]`."
        ),
    ] = "[]",
    prose: Annotated[
        str | None,
        Parameter(
            help="Notes of the file in Pandoc Markdown; replaces the notes that are there."
        ),
    ] = None,
    root: Root = Path(),
) -> None:
    """Author a morphism in `morphisms/<SOURCE>-<TARGET>.md`."""
    path = root / "morphisms" / f"{source}-{target}.md"
    present = frontmatter.load(str(path)) if path.exists() else None
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
    listed: list[dict[str, Yaml]] = (
        list(present.metadata["morphisms"]) if present else []
    )
    notes = prose if prose is not None else (present.content if present else "")
    path.parent.mkdir(exist_ok=True)
    path.write_text(records.morphisms_text(source, target, [*listed, added], notes))
    print(path)


LATTICEDB = f"latticedb {version('latticedb')}"


def _corpus_inputs(loaded: corpus.Corpus) -> str:
    """The digest of the Gram tensors of the records: the inputs of a computation over the whole corpus."""
    return certificates.digest(
        "\n".join(certificates.gram_digest(entry.lattice) for entry in loaded.entries)
    )


@app.command
def verify(root: Root = Path()) -> None:
    """Report mathematical and source errors without changing lattice cards."""
    try:
        count, problems = checks.run(root)
    except corpus.CorpusInvalid as invalid:
        print("\n".join(invalid.problems), file=sys.stderr)
        print(f"{len(invalid.problems)} problems", file=sys.stderr)
        sys.exit(1)
    _refuse(problems)
    print(f"{count} lattice cards verified")


@app.command
def enrich(
    *,
    tag: Annotated[
        tuple[str, ...],
        Parameter(
            help="Tag of a card to compute; repeat for each one. All cards when absent."
        ),
    ] = (),
    summand_maps: Annotated[
        bool, Parameter(help="Compute orthogonal summand maps over the corpus.")
    ] = False,
    genus_data: Annotated[bool, Parameter(help="Compute SageMath genus data.")] = False,
    seconds: Annotated[
        int, Parameter(help="Time limit of SageMath for one value of one record.")
    ] = 120,
    root: Root = Path(),
) -> None:
    """Compute derived card fields and store their computation certificates."""
    loaded = corpus.load(root)
    held = certificates.load(root)
    selected = set(tag)
    found: list[str] = []
    for entry in loaded.entries:
        lattice = entry.lattice
        if lattice.gram_tensor is None or (selected and lattice.tag not in selected):
            continue
        inputs = certificates.gram_digest(lattice)
        if certificates.is_certified(held, f"{lattice.tag} derive", inputs):
            continue
        text = entry.path.read_text()
        document = frontmatter.loads(text)
        updated = records.record_text(
            records.derive(corpus.front_matter(document)), document.content
        )
        if updated != text:
            entry.path.write_text(updated)
            print(f"{entry.path}: derived values written")
        held[f"{lattice.tag} derive"] = certificates.Certificate(
            inputs=inputs, by=LATTICEDB
        )
    certificates.save(root, held)
    if (
        summand_maps
        and not tag
        and not certificates.is_certified(
            held, summands.CERTIFICATE, _corpus_inputs(loaded)
        )
    ):
        problems = summands.store(root, loaded)
        found.extend(problems)
        if not problems:
            held[summands.CERTIFICATE] = certificates.Certificate(
                inputs=_corpus_inputs(loaded), by=LATTICEDB
            )
            certificates.save(root, held)
    if genus_data:
        found.extend(genus.certify(root, loaded, held, tag, seconds))
    _refuse(found)


@app.command
def build(
    root: Root = Path(),
    target: Annotated[
        Path, Parameter(help="Directory for the site. The command replaces it.")
    ] = Path("_site"),
) -> None:
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
    assert SERVED.resolve() == target, (
        f"{SERVED} links to {SERVED.resolve()}, not to {target}"
    )
    with urlopen(Request(ADDRESS, headers={"Host": HOST})) as response:
        assert response.status == 200, (
            f"{ADDRESS} with host {HOST} returned {response.status}"
        )
    print(f"http://{HOST}/")


@app.command
def next_tag(root: Root = Path()) -> None:
    """Print the tag for the next new record."""
    print(corpus.next_tag(root))
