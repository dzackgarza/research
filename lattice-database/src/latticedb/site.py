"""Build the static site from the corpus.

The site has one page for each lattice (`tag/<TAG>.html`), whose tables and
sections come from the record and whose prose comes from the Markdown body;
a database page that filters and sorts `lattices.json`, the union of all
records; an index of tags; one page for each collection in `pages/`; and a
reference page for the fields, generated from the schema.
"""

import json
import re
import shutil
import subprocess
from collections.abc import Iterator
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from fractions import Fraction
from importlib.resources import files
from pathlib import Path
from urllib.parse import urlencode

import frontmatter
from flint import fmpz
from jinja2 import Environment, PackageLoader, StrictUndefined, select_autoescape
from markupsafe import Markup, escape
from pydantic import BaseModel, Field

from latticedb.corpus import Entry, load
from latticedb.model import DefiniteData, HyperbolicData, IndefiniteData, IntegralData, Lattice, Provenance, Record, Reference, Related

type Cell = str | int | float | bool | None | list[str]
type Row = dict[str, Cell]

DEFINITENESS_LABEL = {
    "positive_definite": "positive definite",
    "negative_definite": "negative definite",
    "indefinite": "indefinite",
    "positive_semidefinite": "positive semidefinite",
    "negative_semidefinite": "negative semidefinite",
    "zero": "zero",
}
PANES = {"rank": "rank", "definiteness": "definiteness", "property": "properties", "family": "families"}
"""Query parameter of the database page -> the row key whose filter pane it selects."""


class Collection(Record):
    """A page that lists the lattices whose database row satisfies `where`."""

    title: str = Field(description="Title of the page. Dollar signs mark TeX.")
    summary: str = Field(description="One sentence that says which lattices the page lists. Dollar signs mark TeX.")
    where: dict[str, int | str | bool | list[str]] = Field(
        description=(
            "Key of a row of `lattices.json` -> required value. A lattice is listed when every condition holds. "
            "For a key whose value is a list, such as `properties`, the list must contain the required value, or each of the required values."
        )
    )


@dataclass(frozen=True)
class CollectionPage:
    slug: str
    collection: Collection
    prose: str
    members: tuple[Entry, ...]


def rational_tex(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{'-' if value < 0 else ''}\\tfrac{{{abs(value.numerator)}}}{{{value.denominator}}}"


def group_text(factors: tuple[int, ...]) -> str:
    """`Z/2^3 + Z/4` for the invariant factors (2, 2, 2, 4); `0` for the trivial group."""
    runs = [(factor, factors.count(factor)) for factor in dict.fromkeys(factors)]
    return " + ".join(f"(Z/{factor})^{count}" if count > 1 else f"Z/{factor}" for factor, count in runs) or "0"


def group_tex(factors: tuple[int, ...]) -> str:
    runs = [(factor, factors.count(factor)) for factor in dict.fromkeys(factors)]
    return " \\oplus ".join(f"(\\mathbb{{Z}}/{factor})^{{{count}}}" if count > 1 else f"\\mathbb{{Z}}/{factor}" for factor, count in runs) or "0"


def elementary_prime(factors: tuple[int, ...]) -> int | None:
    """The prime `p` when the group is `(Z/p)^a` with `a >= 1`."""
    if factors and len(set(factors)) == 1 and fmpz(factors[0]).is_prime():
        return factors[0]
    return None


def factorisation_tex(value: int) -> str:
    return " \\cdot ".join(f"{int(prime)}^{{{int(exponent)}}}" if exponent > 1 else str(int(prime)) for prime, exponent in fmpz(value).factor())


def genus_tex(symbol: str) -> str:
    """TeX for a stored genus symbol such as `II_{1,9} (2: 2^10)`."""
    head, _, local = symbol.partition(" (")
    letters, _, signature = head.partition("_")
    tex = f"\\mathrm{{{letters}}}_{signature}"
    if not local:
        return tex
    parts = []
    for part in local.removesuffix(")").split("; "):
        prime, _, body = part.partition(": ")
        body = re.sub(r"\^(-?\d+)", r"^{\1}", body)
        body = re.sub(r"\]_(\d+)", r"]_{\1}", body)
        parts.append(f"{prime}\\colon {body.replace(' ', '\\,')}")
    return f"{tex}\\ \\bigl({';\\ '.join(parts)}\\bigr)"


def root_system_tex(components: tuple[str, ...]) -> str:
    """`D_{4} \\oplus A_{1}^{3}` for the irreducible components (D4, A1, A1, A1)."""
    runs = [(component, components.count(component)) for component in dict.fromkeys(components)]
    return " \\oplus ".join(f"{component[0]}_{{{component[1:]}}}" + (f"^{{{count}}}" if count > 1 else "") for component, count in runs)


def set_tex(values: tuple[Fraction, ...]) -> str:
    """`\\{-2, \\tfrac{2}{3}\\}` for the set of the values."""
    return f"\\{{{', '.join(rational_tex(value) for value in sorted(set(values)))}\\}}"


def inline_markup(text: str) -> Markup:
    """HTML for one line of copy, in which backticks mark code and dollar signs mark TeX."""
    code = re.sub(r"`([^`]+)`", r"<code>\1</code>", str(escape(text)))
    return Markup(re.sub(r"\$([^$]+)\$", r"\\(\1\\)", code))


def theta_tex(theta: tuple[int, ...]) -> str:
    terms = ["1", *(f"{count}q^{{{power}}}" if power > 1 else f"{count}q" for power, count in enumerate(theta) if power > 0 and count > 0)]
    return " + ".join([*terms, f"O(q^{{{len(theta)}}})"])


PROPERTY_MEANINGS = {
    "integral": "Every $b(e_i, e_j)$ is an integer.",
    "not integral": "Some $b(e_i, e_j)$ is not an integer.",
    "even": "Integral, and every $b(x, x)$ is even.",
    "odd": "Integral, and some $b(x, x)$ is odd.",
    "unimodular": "Integral, with determinant $1$ or $-1$.",
    "p-elementary": "Integral and nondegenerate, with discriminant group $(\\mathbb{Z}/p)^a$ for a prime $p$ and $a \\geq 1$. The label states the prime: `2-elementary`.",
    "root lattice": (
        "$L = \\mathbb{Z}\\Phi(L)$, where $\\Phi(L)$ is the set of roots of $L$: the primitive $r$ with $b(r, r) \\neq 0$ and $s_r \\in O(L)$. "
        "A lattice has the label when the build finds roots that generate it. A lattice without the label is not decided."
    ),
    "degenerate": "Some nonzero $x$ has $b(x, y) = 0$ for every $y$.",
    "hyperbolic": "Nondegenerate of rank at least 2, with signature $(1, n)$ or $(n, 1)$.",
    "isotropic": "Indefinite, and $b(x, x) = 0$ for some nonzero $x$.",
    "anisotropic": "Indefinite, and $b(x, x) \\neq 0$ for every nonzero $x$.",
    "reflective": "Hyperbolic, and the subgroup generated by reflections has finite index in the isometry group.",
    "not reflective": "Hyperbolic, and the subgroup generated by reflections has infinite index in the isometry group.",
}
"""Property label of the database -> its definition. `p-elementary` stands for the labels that state a prime."""


def properties(lattice: Lattice) -> list[str]:
    """The properties of a lattice that the database filters by. Each one follows from the record."""
    found = []
    if lattice.integral is None:
        found.append("not integral")
    else:
        found.extend(["integral", lattice.integral.parity])
        if lattice.is_unimodular:
            found.append("unimodular")
        prime = elementary_prime(lattice.integral.discriminant_group or ())
        if prime is not None:
            found.append(f"{prime}-elementary")
    if lattice.is_root_lattice:
        found.append("root lattice")
    if not lattice.is_nondegenerate:
        found.append("degenerate")
    if lattice.is_hyperbolic:
        found.append("hyperbolic")
    if lattice.indefinite is not None:
        found.append("isotropic" if lattice.indefinite.isotropic else "anisotropic")
    if lattice.hyperbolic is not None:
        found.append("reflective" if lattice.hyperbolic.reflective else "not reflective")
    return found


def row(lattice: Lattice) -> Row:
    """The row of a lattice in `lattices.json`."""
    integral, definite = lattice.integral, lattice.definite
    group = integral.discriminant_group if integral else None
    order = definite.automorphism_group_order if definite else None
    return {
        "tag": lattice.tag,
        "url": f"tag/{lattice.tag}.html",
        "name": lattice.name,
        "latex": lattice.latex,
        "aliases": list(lattice.aliases),
        "rank": lattice.rank,
        "n_plus": lattice.signature[0],
        "n_minus": lattice.signature[1],
        "signature": f"({lattice.signature[0]}, {lattice.signature[1]})",
        "determinant": str(lattice.determinant),
        "determinant_value": float(lattice.determinant),
        "definiteness": DEFINITENESS_LABEL[lattice.definiteness],
        "properties": properties(lattice),
        "discriminant_group": group_text(group) if group is not None else None,
        "discriminant_group_tex": group_tex(group) if group is not None else None,
        "genus_symbol": integral.genus_symbol if integral else None,
        "minimum": str(definite.minimum) if definite else None,
        "minimum_value": float(definite.minimum) if definite else None,
        "kissing_number": definite.kissing_number if definite else None,
        "automorphism_group_order": str(order) if order is not None else None,
        "automorphism_group_order_value": float(order) if order is not None else None,
        "root_system": " ".join(definite.root_system) if definite and definite.root_system is not None else None,
        "root_system_tex": root_system_tex(definite.root_system) if definite and definite.root_system else None,
        "families": list(lattice.families),
    }


def _satisfies(record: Row, key: str, required: int | str | bool | list[str]) -> bool:
    match record[key], required:
        case list() as values, list() as wanted:
            return all(item in values for item in wanted)
        case list() as values, _:
            return required in values
        case value, _:
            return value == required


def collections(directory: Path, entries: tuple[Entry, ...]) -> tuple[CollectionPage, ...]:
    rows = {entry.lattice.tag: row(entry.lattice) for entry in entries}
    keys = set(next(iter(rows.values())))
    pages = []
    for path in sorted(directory.glob("*.md")):
        document = frontmatter.load(str(path))
        collection = Collection.model_validate(document.metadata)
        assert set(collection.where) <= keys, f"{path}: unknown row keys {sorted(set(collection.where) - keys)}"
        members = tuple(entry for entry in entries if all(_satisfies(rows[entry.lattice.tag], key, value) for key, value in collection.where.items()))
        assert members, f"{path}: no lattice satisfies the conditions"
        pages.append(CollectionPage(path.stem, collection, document.content, members))
    return tuple(pages)


def database_query(collection: Collection) -> str | None:
    """The query string that selects the members of a collection on the database page, when its conditions are filter panes."""
    parameters = {}
    for parameter, key in PANES.items():
        match collection.where.get(key):
            case None:
                continue
            case list() as wanted:
                parameters[parameter] = ",".join(wanted)
            case value:
                parameters[parameter] = str(value)
    return urlencode(parameters) if len(parameters) == len(collection.where) else None


def markdown_to_html(texts: list[str]) -> list[Markup]:
    """HTML for each Markdown text. TeX stays as `\\(...\\)` for MathJax."""

    def convert(text: str) -> Markup:
        done = subprocess.run(["pandoc", "--from=markdown", "--to=html", "--mathjax"], input=text, capture_output=True, text=True, check=True)
        return Markup(done.stdout)

    with ThreadPoolExecutor() as pool:
        return list(pool.map(convert, texts))


def fields() -> Iterator[tuple[str, str | None, type[BaseModel]]]:
    """The models of the schema: heading, block key, model."""
    yield "Every lattice", None, Lattice
    yield "Integral lattice", "integral", IntegralData
    yield "Definite lattice", "definite", DefiniteData
    yield "Indefinite lattice", "indefinite", IndefiniteData
    yield "Hyperbolic lattice", "hyperbolic", HyperbolicData
    yield "Related lattice", "related[]", Related
    yield "Reference", "references[]", Reference
    yield "Provenance", "provenance", Provenance


def build(root: Path, target: Path) -> int:
    """Write the site for the corpus under `root` to `target`. Returns the number of lattices."""
    entries = load(root / "lattices")
    pages = collections(root / "pages", entries)
    by_tag = {entry.lattice.tag: entry for entry in entries}
    environment = Environment(loader=PackageLoader("latticedb"), autoescape=select_autoescape(["html", "j2"]), undefined=StrictUndefined, trim_blocks=True, lstrip_blocks=True)
    environment.filters["inline_markup"] = inline_markup
    environment.globals.update(
        rational_tex=rational_tex,
        group_tex=group_tex,
        factorisation_tex=factorisation_tex,
        genus_tex=genus_tex,
        theta_tex=theta_tex,
        root_system_tex=root_system_tex,
        set_tex=set_tex,
        properties=properties,
        definiteness_label=DEFINITENESS_LABEL,
        collections=pages,
        total=len(entries),
    )

    if target.exists():
        assert (target / "lattices.json").exists(), f"{target} exists and is not a site that this command built"
        shutil.rmtree(target)
    (target / "tag").mkdir(parents=True)
    (target / "collection").mkdir()
    shutil.copytree(str(files("latticedb") / "assets"), target / "assets")

    ranks = sorted({entry.lattice.rank for entry in entries})
    by_rank = {rank: [entry for entry in entries if entry.lattice.rank == rank] for rank in ranks}
    prose = markdown_to_html([entry.prose for entry in entries] + [page.prose for page in pages])
    lattice_page = environment.get_template("lattice.html.j2")
    for index, entry in enumerate(entries):
        lattice = entry.lattice
        components = json.dumps([[int(value) if value.denominator == 1 else str(value) for value in components_row] for components_row in lattice.gram_tensor])
        (target / "tag" / f"{lattice.tag}.html").write_text(
            lattice_page.render(
                root="../",
                lattice=lattice,
                prose=prose[index],
                components_text=components.replace('"', ""),
                related=[(by_tag[related.tag].lattice, related.relation) for related in lattice.related],
                previous=entries[index - 1].lattice if index > 0 else None,
                following=entries[index + 1].lattice if index + 1 < len(entries) else None,
            )
        )
    collection_page = environment.get_template("collection.html.j2")
    for index, page in enumerate(pages):
        html = collection_page.render(root="../", page=page, prose=prose[len(entries) + index], query=database_query(page.collection))
        (target / "collection" / f"{page.slug}.html").write_text(html)
    models = [(heading, key, model.__doc__, list(model.model_fields.items())) for heading, key, model in fields()]
    (target / "index.html").write_text(environment.get_template("index.html.j2").render(root="./", by_rank=by_rank))
    (target / "tags.html").write_text(environment.get_template("tags.html.j2").render(root="./", by_rank=by_rank))
    (target / "database.html").write_text(environment.get_template("database.html.j2").render(root="./"))
    (target / "fields.html").write_text(environment.get_template("fields.html.j2").render(root="./", models=models, property_meanings=PROPERTY_MEANINGS))
    (target / "lattices.json").write_text(json.dumps({"rows": [row(entry.lattice) for entry in entries]}, separators=(",", ":")))
    return len(entries)
