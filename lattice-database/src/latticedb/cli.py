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
    """Write a lattice card from authored fields, without computation or verification.

    Refuses a Gram tensor that a card of the corpus already states: the
    corpus records a lattice once, so a second card with the same tensor is
    never written.
    """
    try:
        parsed = records.gram_tensor(json.loads(gram))
    except AssertionError as error:
        print(f"--gram: {error}", file=sys.stderr)
        sys.exit(1)
    key = corpus.gram_key(parsed)
    index = corpus.gram_index(root)
    if index.get(key):
        print(
            f"gram_tensor: the corpus already holds this tensor at {' '.join(index[key])}",
            file=sys.stderr,
        )
        sys.exit(1)
    declared: dict[str, Yaml] = {
        "name": name,
        "latex": latex,
        "aliases": list(alias),
        "gram_tensor": json.loads(gram),
        "families": list(family),
        "related": [],
        "references": [{"citation": citation} for citation in reference],
    }
    path = _author(root, declared, prose)
    corpus.append_index(root, path.stem, parsed)
    print(path)


@app.command(name="bulk-source-fetch")
def bulk_source_fetch(root: Root = Path()) -> None:
    """Store the published Nipp, Brandt–Intrau, and Watson bulk source tables."""
    for path in bulk_sources.fetch(root):
        print(f"sources/{path}")


@app.command(name="bulk-index")
def bulk_index_write(root: Root = Path()) -> None:
    """Store parsed bulk source rows without deriving mathematical invariants."""
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
    root: Root = Path(),
) -> None:
    """Author a morphism on the source lattice card."""
    path = root / "lattices" / f"{source}.md"
    document = frontmatter.load(str(path))
    added: dict[str, Yaml] = {
        "target": target,
        "name": name,
        "matrix": json.loads(matrix),
        "row_subdivisions": json.loads(row_subdivisions),
        "column_subdivisions": json.loads(column_subdivisions),
    }
    if description is not None:
        added["description"] = description
    if scale != 1:
        added["scale"] = scale
    metadata = corpus.front_matter(document)
    metadata["morphisms"] = [*metadata.get("morphisms", []), added]
    path.write_text(records.record_text(metadata, document.content))
    print(path)


LATTICEDB = f"latticedb {version('latticedb')}"


@app.command
def verify(root: Root = Path()) -> None:
    """Report stored-card inconsistencies without changing cards; mathematics is delegated to the preamble."""
    try:
        count, problems = checks.run(root)
    except corpus.CorpusInvalid as invalid:
        print("\n".join(invalid.problems), file=sys.stderr)
        print(f"{len(invalid.problems)} problems", file=sys.stderr)
        sys.exit(1)
    _refuse(problems)
    print(f"{count} lattice cards structurally verified")


@app.command
def duplicates(root: Root = Path()) -> None:
    """List the tags that share a Gram tensor, without changing lattice cards."""
    index = corpus.gram_index(root)
    found = {gram: tags for gram, tags in index.items() if len(tags) > 1}
    for tags in found.values():
        print(f"{' '.join(tags)}")
    if found:
        print(
            f"{sum(len(tags) for tags in found.values())} cards share a Gram tensor",
            file=sys.stderr,
        )
        sys.exit(1)
    print(
        f"{sum(len(tags) for tags in index.values())} lattice cards have distinct Gram tensors"
    )


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
    root: Root = Path(),
) -> None:
    """Compute ordinary derived card fields without certifying them."""
    loaded = corpus.load(root)
    selected = set(tag)
    found: list[str] = []
    for entry in loaded.entries:
        lattice = entry.lattice
        if lattice.gram_tensor is None or (selected and lattice.tag not in selected):
            continue
        text = entry.path.read_text()
        document = frontmatter.loads(text)
        metadata = corpus.front_matter(document)
        derived = records.derive(metadata)
        updated = records.record_text(derived, document.content)
        if updated != text:
            entry.path.write_text(updated)
            print(f"{entry.path}: derived values written")
    if summand_maps and not tag:
        problems = summands.store(root, loaded)
        found.extend(problems)
    _refuse(found)


@app.command
def certify(
    *,
    tag: Annotated[
        tuple[str, ...],
        Parameter(
            help="Tag of a card to certify; repeat for each one. All cards when absent."
        ),
    ] = (),
    root: Root = Path(),
) -> None:
    """Compute uncertified card values, replace disagreements, and certify the computed results."""
    loaded = corpus.load(root)
    held = certificates.load(root)
    selected = set(tag)
    for entry in loaded.entries:
        lattice = entry.lattice
        if lattice.gram_tensor is None or (selected and lattice.tag not in selected):
            continue
        document = frontmatter.load(str(entry.path))
        metadata = corpus.front_matter(document)
        computation = f"{lattice.tag} derive"
        cited = metadata.get("certifications")
        cited_hash = cited.get("derive") if isinstance(cited, dict) else None
        expected_hash = certificates.certification_hash(
            computation, lattice, records.derived_projection(metadata)
        )
        if certificates.is_certified(held, computation, cited_hash, expected_hash):
            continue
        computed = records.derive(metadata)
        certificate_hash = certificates.certification_hash(
            computation, lattice, records.derived_projection(computed)
        )
        card_certifications = dict(computed.get("certifications") or {})
        card_certifications["derive"] = certificate_hash
        computed["certifications"] = card_certifications
        entry.path.write_text(records.record_text(computed, document.content))
        held[computation] = certificates.Certificate(
            hash=certificate_hash, by=LATTICEDB
        )
        certificates.save(root, held)
    genus.certify(root, corpus.load(root), held, tag)


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
