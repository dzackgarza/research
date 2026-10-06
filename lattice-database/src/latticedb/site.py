"""Build the static site from the corpus.

The site has one page for each lattice (`tag/<TAG>.html`), whose tables and
sections come from the record and whose prose comes from the Markdown body;
a database page that filters and sorts `lattices.json`, the union of all
records; an index of tags; one page for each collection in `pages/`; one page for each
part of the theory in `theory/`, which the other pages link to; and a
reference page for the fields, generated from the schema.
"""

import json
import re
import shutil
import subprocess
from collections.abc import Iterator
from dataclasses import dataclass
from fractions import Fraction
from html.parser import HTMLParser
from importlib.resources import files
from pathlib import Path
from urllib.parse import urlencode, urlsplit

import frontmatter
from jinja2 import Environment, PackageLoader, StrictUndefined, select_autoescape
from markdown_it import MarkdownIt
from markupsafe import Markup, escape
from pydantic import BaseModel, Field

from latticedb.catalogues import ArithmeticGroup, LieGroup
from latticedb.corpus import Entry, load
from latticedb.geometric import ProjectiveComplexVariety, RiemannianSymmetricSpace
from latticedb.model import (
    DefiniteData,
    HyperbolicData,
    IndefiniteData,
    IntegralData,
    Lattice,
    Vector,
    Morphism,
    OrbitGroup,
    PrimitiveOrbitSeries,
    Record,
    Reference,
    Related,
    RootSpan,
    RootSystemComponent,
)

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
PANES = {
    "rank": "rank",
    "definiteness": "definiteness",
    "property": "properties",
    "family": "families",
}
"""Query parameter of the database page -> the row key whose filter pane it selects."""


class Collection(Record):
    """A page that lists the lattices whose database row satisfies `where`."""

    title: str = Field(description="Title of the page. Dollar signs mark TeX.")
    summary: str = Field(
        description="One sentence that says which lattices the page lists. Dollar signs mark TeX."
    )
    where: dict[str, int | str | bool | list[str]] = Field(
        description=(
            "Key of a row of `lattices.json` -> required value. A lattice is listed when every condition holds. "
            "For a key whose value is a list, such as `properties`, the list must contain the required value, or each of the required values."
        )
    )


class Article(Record):
    """A page of `theory/`: the one place where the site explains a part of the theory, which the other pages link to."""

    title: str = Field(description="Title of the page. Dollar signs mark TeX.")
    summary: str = Field(
        description="One sentence that says what the page explains. Dollar signs mark TeX."
    )
    order: int = Field(description="Position of the page in the list of theory pages.")


@dataclass(frozen=True)
class ArticlePage:
    slug: str
    article: Article
    prose: str


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
    return (
        " + ".join(
            f"(Z/{factor})^{count}" if count > 1 else f"Z/{factor}"
            for factor, count in runs
        )
        or "0"
    )


def group_tex(factors: tuple[int, ...]) -> str:
    runs = [(factor, factors.count(factor)) for factor in dict.fromkeys(factors)]
    return (
        " \\oplus ".join(
            f"(\\mathbb{{Z}}/{factor})^{{{count}}}"
            if count > 1
            else f"\\mathbb{{Z}}/{factor}"
            for factor, count in runs
        )
        or "0"
    )


def orbit_group_tex(group: OrbitGroup) -> str:
    """TeX for a key of `integral.primitive_orbits`, such as `\\widetilde{SO}^+(L)` for `SOtilde+`."""
    name, plus = group.removesuffix("+"), "^+" if group.endswith("+") else ""
    letters = name.removesuffix("tilde")
    return (
        f"\\widetilde{{{letters}}}{plus}(L)"
        if name.endswith("tilde")
        else f"\\mathrm{{{letters}}}{plus}(L)"
    )


ORBIT_GROUP_KEYS = ("O", "SO", "O+", "SO+", "Otilde", "SOtilde", "Otilde+", "SOtilde+")
"""The eight standard subgroup keys of $O(L)$: the keys of `integral.primitive_orbits`."""


def subgroup_tex(key: str) -> str:
    """TeX for a standard arithmetic-subgroup name or a named subgroup such as `Gamma_En_2`."""
    return orbit_group_tex(key) if key in ORBIT_GROUP_KEYS else key.replace("_", "\\_")


def cardinality_tex(cardinality: int | str) -> str:
    """TeX for a stored finite or countably infinite group cardinality."""
    if cardinality == "aleph0":
        return "\\aleph_0"
    return str(cardinality)


def orbit_series_tex(series: PrimitiveOrbitSeries) -> str:
    """TeX for $F_{L,\\Gamma}(z, w)$: the stated nonzero terms, `?` for each coefficient that is not stated, and the order to which the series is stated."""
    terms = []
    for n in sorted(series.degrees, key=lambda n: (abs(n), -n)):
        count = series.coefficient(n)
        if count == 0:
            continue
        variable = (
            ""
            if n == 0
            else ("z" if n > 0 else "w") + (f"^{{{abs(n)}}}" if abs(n) > 1 else "")
        )
        coefficient = "?" if count is None else str(count)
        terms.append(
            coefficient
            if not variable
            else (variable if coefficient == "1" else f"{coefficient}\\,{variable}")
        )
    order = f"O(z^{{{len(series.z) + 1}}}, w^{{{len(series.w) + 1}}})"
    return " + ".join([*terms, order])


def _argument(shift: int) -> str:
    return "s" if shift == 0 else f"s - {shift}" if shift > 0 else f"s + {-shift}"


def _character_tex(character) -> str:
    coefficient = int(character.coefficient)
    if not character.times_norm_parameter:
        return str(coefficient)
    return "n" if coefficient == 1 else "-n" if coefficient == -1 else f"{coefficient}n"


def _l_factor_tex(factor) -> str:
    argument = _argument(int(factor.shift))
    character = factor.character
    if int(character.coefficient) == 1 and not character.times_norm_parameter:
        return f"\\zeta^\\Sigma({argument})"
    return f"L^\\Sigma({argument}, \\chi_{{{_character_tex(character)}}})"


def zeta_tex(lattice: Lattice, cone: bool) -> str:
    """Render the preamble-owned affine-quadric zeta factorization."""
    from dzack_research.preamble.categories.lattices import Lattices
    from dzack_research.preamble.rings import session_ring_objects

    integers = session_ring_objects()["ZZ"]
    owned = Lattices(integers)(lattice.gram_tensor)
    factorization = owned.quadratic_hypersurface_zeta_factorization(cone=cone)
    numerator = "\\, ".join(_l_factor_tex(factor) for factor in factorization.numerator)
    if not factorization.denominator:
        return numerator
    denominator = "\\, ".join(_l_factor_tex(factor) for factor in factorization.denominator)
    return f"\\frac{{{numerator}}}{{{denominator}}}"


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
    runs = [
        (component, components.count(component))
        for component in dict.fromkeys(components)
    ]
    return " \\oplus ".join(
        f"{component[0]}_{{{component[1:]}}}" + (f"^{{{count}}}" if count > 1 else "")
        for component, count in runs
    )


def set_tex(values: tuple[Fraction, ...]) -> str:
    """`\\{-2, \\tfrac{2}{3}\\}` for the set of the values."""
    return f"\\{{{', '.join(rational_tex(value) for value in sorted(set(values)))}\\}}"


def combination_tex(coordinates: Vector, symbol: str = "e") -> str:
    """`e_{1} - 2e_{3}` for the coordinates (1, 0, -2); `0` for the zero vector."""
    terms = []
    for index, coefficient in enumerate(coordinates, start=1):
        if coefficient == 0:
            continue
        sign = "-" if coefficient < 0 else "+"
        size = "" if abs(coefficient) == 1 else str(abs(coefficient))
        terms.append((sign, f"{size}{symbol}_{{{index}}}"))
    if not terms:
        return "0"
    first_sign, first = terms[0]
    return (
        ("-" if first_sign == "-" else "")
        + first
        + "".join(f" {sign} {term}" for sign, term in terms[1:])
    )


def _runs(names: list[str]) -> list[tuple[str, int]]:
    return [(name, names.count(name)) for name in dict.fromkeys(names)]


def root_span_tex(components: tuple[RootSystemComponent, ...]) -> str:
    """Render the stored component types and scales, without deriving another lattice identification."""
    names = [
        component.type if component.scale == 1 else f"{component.type}({rational_tex(component.scale)})"
        for component in components
    ]
    runs = _runs(names)
    return (
        " \\oplus ".join(
            f"{name}^{{{count}}}" if count > 1 else name for name, count in runs
        )
        or "0"
    )


def root_span_text(components: tuple[RootSystemComponent, ...]) -> str:
    names = [
        component.type if component.scale == 1 else f"{component.type}({component.scale})"
        for component in components
    ]
    runs = _runs(names)
    return (
        " + ".join(f"{name}^{count}" if count > 1 else name for name, count in runs)
        or "0"
    )


def block_tex(block: list[int], symbol: str = "e") -> str:
    """`e_{3}, \\dots, e_{10}` for the indices 3 to 10; each vector for fewer than four indices or a block with a gap."""
    if len(block) > 3 and block[-1] - block[0] == len(block) - 1:
        return f"{symbol}_{{{block[0]}}}, \\dots, {symbol}_{{{block[-1]}}}"
    return ", ".join(f"{symbol}_{{{index}}}" for index in block)


def matrix_tex(morphism: Morphism) -> str:
    """The matrix as a TeX `array`, with a vertical line at each column subdivision and `\\hline` at each row subdivision."""
    columns = len(morphism.matrix[0])
    bounds = (0, *morphism.column_subdivisions, columns)
    alignment = "|".join(
        "r" * (high - low) for low, high in zip(bounds, bounds[1:], strict=False)
    )
    lines = []
    for index, matrix_row in enumerate(morphism.matrix):
        if index in morphism.row_subdivisions:
            lines.append("\\hline")
        lines.append(" & ".join(str(value) for value in matrix_row) + " \\\\")
    return (
        f"\\left(\\begin{{array}}{{{alignment}}}\n"
        + "\n".join(lines)
        + "\n\\end{array}\\right)"
    )


def matrix_text(morphism: Morphism) -> str:
    """The matrix and its subdivisions as JSON, one row per line, in the form that `latticedb morphism` reads."""
    rows = ",\n  ".join(json.dumps(list(matrix_row)) for matrix_row in morphism.matrix)
    row_lines = json.dumps(list(morphism.row_subdivisions))
    column_lines = json.dumps(list(morphism.column_subdivisions))
    return f'{{"matrix": [\n  {rows}\n],\n "row_subdivisions": {row_lines},\n "column_subdivisions": {column_lines}}}'


def summand_name(record: Lattice, scale: int) -> tuple[str, str]:
    """The stored card name for $M$, with ``(k)`` appended for a nontrivial twist."""
    if scale == 1:
        return record.name, record.latex
    return f"{record.name}({scale})", f"{record.latex}({scale})"


def span_summands(
    lattice: Lattice, lattices: dict[str, Lattice]
) -> list[tuple[Lattice, str]]:
    """`(M, name of M(k) as TeX)` for each summand $M(k)$ of `root_span.summands`."""
    span = lattice.root_span
    if span is None or span.summands is None:
        return []
    return [
        (lattices[summand.tag], summand_name(lattices[summand.tag], summand.scale)[1])
        for summand in span.summands
    ]


def summand_images(
    lattice: Lattice, lattices: dict[str, Lattice]
) -> list[tuple[Lattice, str, int, Vector]]:
    """`(M, name of M(k) as TeX, j, x)` for each row `x` of `root_span.embedding`: the embedding sends the basis vector $e_j$ of the summand $M(k)$ to `x`."""
    span = lattice.root_span
    if span is None or span.summands is None or span.embedding is None:
        return []
    sources = [
        (record, name, j)
        for record, name in span_summands(lattice, lattices)
        for j in range(1, record.rank + 1)
    ]
    return [
        (record, name, j, image)
        for (record, name, j), image in zip(sources, span.embedding, strict=True)
    ]


def inline_markup(text: str) -> Markup:
    """HTML for one line of copy, in which backticks mark code and dollar signs mark TeX."""
    code = re.sub(r"`([^`]+)`", r"<code>\1</code>", str(escape(text)))
    return Markup(re.sub(r"\$([^$]+)\$", r"\\(\1\\)", code))


def theta_tex(theta: tuple[int, ...]) -> str:
    terms = [
        "1",
        *(
            f"{count}q^{{{power}}}" if power > 1 else f"{count}q"
            for power, count in enumerate(theta)
            if power > 0 and count > 0
        ),
    ]
    return " + ".join([*terms, f"O(q^{{{len(theta)}}})"])


PROPERTY_MEANINGS = {
    "integral": ("lattices", "integral", "$L$ is integral."),
    "not integral": ("lattices", "integral", "$L$ is not integral."),
    "even": ("lattices", "integral", "$L$ is integral and even."),
    "odd": ("lattices", "integral", "$L$ is integral and odd."),
    "unimodular": ("discriminant-forms", "unimodular", "$L$ is unimodular."),
    "p-elementary": (
        "discriminant-forms",
        "two-elementary",
        "$A_L \\cong (\\mathbb{Z}/p)^a$ for a prime $p$ and $a \\geq 1$; the label states the prime, as in `2-elementary`.",
    ),
    "root lattice": ("roots", "roots", "$L = \\mathbb{Z}\\Phi(L)$."),
    "not a root lattice": ("roots", "roots", "$L \\neq \\mathbb{Z}\\Phi(L)$."),
    "degenerate": ("lattices", "degenerate", "$L$ is degenerate."),
    "hyperbolic": ("indefinite-lattices", "hyperbolic", "$L$ is hyperbolic."),
    "isotropic": (
        "indefinite-lattices",
        "isotropic",
        "$L$ is indefinite and isotropic.",
    ),
    "anisotropic": (
        "indefinite-lattices",
        "isotropic",
        "$L$ is indefinite and not isotropic.",
    ),
    "reflective": ("indefinite-lattices", "reflective", "$L$ is reflective."),
    "not reflective": (
        "indefinite-lattices",
        "reflective",
        "$L$ is hyperbolic and not reflective.",
    ),
}
"""Property label of the database -> (theory page, anchor of the definition, the condition). `p-elementary` stands for the labels that state a prime."""


def properties(lattice: Lattice) -> list[str]:
    """Property labels explicitly supported by stored card fields."""
    found = []
    if lattice.integral is not None:
        found.extend(["integral", lattice.integral.parity])
    if lattice.root_sublattice is not None and lattice.root_sublattice.norms is not None:
        found.append("root lattice")
    if lattice.hyperbolic is not None:
        found.append("hyperbolic")
    if lattice.indefinite is not None:
        found.append("isotropic" if lattice.indefinite.isotropic else "anisotropic")
    if lattice.hyperbolic is not None:
        found.append(
            "reflective" if lattice.hyperbolic.reflective else "not reflective"
        )
    return found


def root_span_name(
    lattice: Lattice, lattices: dict[str, Lattice]
) -> tuple[str, str] | None:
    """A lattice isometric to $\\mathbb{Z}\\Phi(L)$, as text and as TeX; `None` when the record does not state one.

    Definite lattice: the orthogonal sum of the root lattices of the components
    of `definite.roots`. Other lattice: the orthogonal sum of the records of
    `root_span.summands`, `0` when the lattice has no roots, and `L` when the
    rows of `root_span.roots` generate `L`.
    """
    if lattice.definite is not None and lattice.definite.roots is not None:
        return root_span_text(lattice.definite.roots), root_span_tex(
            lattice.definite.roots
        )
    span = lattice.root_span
    if span is None:
        return None
    if span.summands is not None:
        names = [
            summand_name(lattices[summand.tag], summand.scale)
            for summand in span.summands
        ]
        return " + ".join(text for text, _ in names), " \\oplus ".join(
            tex for _, tex in names
        )
    if not span.roots:
        return "0", "0"
    return None


def row(lattice: Lattice, lattices: dict[str, Lattice]) -> Row:
    """The row of a lattice in `lattices.json`. `lattices` maps each tag of the corpus to its lattice."""
    integral, definite = lattice.integral, lattice.definite
    group = integral.discriminant_group if integral else None
    order = definite.automorphism_group_order if definite else None
    phi = (
        tuple(component.type for component in definite.roots)
        if definite and definite.roots is not None
        else None
    )
    span_name = root_span_name(lattice, lattices)
    return {
        "tag": lattice.tag,
        "url": f"tag/{lattice.tag}.html",
        "name": lattice.name,
        "latex": lattice.latex,
        "aliases": list(lattice.aliases),
        "rank": lattice.rank,
        "n_plus": lattice.signature[0] if lattice.signature else None,
        "n_minus": lattice.signature[1] if lattice.signature else None,
        "signature": f"({lattice.signature[0]}, {lattice.signature[1]})"
        if lattice.signature
        else None,
        "determinant": str(lattice.determinant)
        if lattice.determinant is not None
        else None,
        "determinant_value": float(lattice.determinant)
        if lattice.determinant is not None
        else None,
        "definiteness": DEFINITENESS_LABEL[lattice.definiteness]
        if lattice.definiteness
        else None,
        "properties": properties(lattice),
        "discriminant_group": group_text(group) if group is not None else None,
        "discriminant_group_tex": group_tex(group) if group is not None else None,
        "genus_symbol": integral.genus_symbol if integral else None,
        "genus_class_count": integral.genus_class_count if integral else None,
        "hyperbolic_index": integral.hyperbolic_index if integral else None,
        "overlattice_count": integral.overlattice_count if integral else None,
        "delta": integral.delta if integral else None,
        "minimum": str(definite.minimum) if definite and definite.minimum is not None else None,
        "minimum_value": float(definite.minimum) if definite and definite.minimum is not None else None,
        "kissing_number": definite.kissing_number if definite else None,
        "automorphism_group_order": str(order) if order is not None else None,
        "automorphism_group_order_value": float(order) if order is not None else None,
        "root_system": " ".join(definite.root_system)
        if definite and definite.root_system is not None
        else None,
        "root_system_tex": root_system_tex(definite.root_system)
        if definite and definite.root_system
        else None,
        "phi_type": " ".join(phi) if phi is not None else None,
        "phi_type_tex": (root_system_tex(phi) or "\\varnothing")
        if phi is not None
        else None,
        "root_span": span_name[0] if span_name else None,
        "root_span_tex": span_name[1] if span_name else None,
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


def collections(
    directory: Path, entries: tuple[Entry, ...]
) -> tuple[CollectionPage, ...]:
    lattices = {entry.lattice.tag: entry.lattice for entry in entries}
    rows = {tag: row(lattice, lattices) for tag, lattice in lattices.items()}
    keys = set(next(iter(rows.values())))
    pages = []
    for path in sorted(directory.glob("*.md")):
        document = frontmatter.load(str(path))
        collection = Collection.model_validate(document.metadata)
        assert set(collection.where) <= keys, (
            f"{path}: unknown row keys {sorted(set(collection.where) - keys)}"
        )
        members = tuple(
            entry
            for entry in entries
            if all(
                _satisfies(rows[entry.lattice.tag], key, value)
                for key, value in collection.where.items()
            )
        )
        assert members, f"{path}: no lattice satisfies the conditions"
        pages.append(CollectionPage(path.stem, collection, document.content, members))
    return tuple(pages)


def articles(directory: Path) -> tuple[ArticlePage, ...]:
    pages = []
    for path in directory.glob("*.md"):
        document = frontmatter.load(str(path))
        pages.append(
            ArticlePage(
                path.stem, Article.model_validate(document.metadata), document.content
            )
        )
    orders = [page.article.order for page in pages]
    assert len(set(orders)) == len(orders), (
        f"{directory}: two theory pages have one order"
    )
    return tuple(sorted(pages, key=lambda page: page.article.order))


class _Anchors(HTMLParser):
    """The internal links (`href` and `src` without a scheme) and the element ids of one HTML page."""

    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            match name, value:
                case "id", str():
                    self.ids.add(value)
                case "href" | "src", str() if not urlsplit(value).scheme:
                    self.links.append(value)


def broken_links(target: Path) -> list[str]:
    """Each internal link of the site under `target` whose file, or whose anchor in that file, does not exist."""
    pages = {}
    for path in target.rglob("*.html"):
        parser = _Anchors()
        parser.feed(path.read_text())
        pages[path.resolve()] = parser
    broken = []
    for path, parser in pages.items():
        for link in parser.links:
            parts = urlsplit(link)
            destination = (path.parent / parts.path).resolve() if parts.path else path
            if not destination.exists() or (
                parts.fragment and parts.fragment not in pages[destination].ids
            ):
                broken.append(f"{path.relative_to(target.resolve())}: {link}")
    return broken


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


def markdown_to_html(
    texts: list[str], bibliography: Path | None = None
) -> list[Markup]:
    """HTML for each Markdown text. TeX stays as `\\(...\\)` for MathJax."""
    local_markdown = MarkdownIt("commonmark")

    def convert(text: str) -> Markup:
        if bibliography is None and text.startswith(
            ("Source entry `", "Catalogue of Lattices archive entry `")
        ):
            return Markup(local_markdown.render(text))
        command = ["pandoc", "--from=markdown", "--to=html", "--mathjax"]
        if bibliography is not None:
            command += [
                "--citeproc",
                "--fail-if-warnings",
                f"--bibliography={bibliography}",
            ]
        done = subprocess.run(
            command, input=text, capture_output=True, text=True, check=True
        )
        return Markup(done.stdout)

    return [convert(text) for text in texts]


def fields() -> Iterator[tuple[str, str | None, type[BaseModel]]]:
    """The models of the schema: heading, block key, model."""
    yield "Every lattice", None, Lattice
    yield "Integral lattice", "integral", IntegralData
    yield (
        "Series of orbits of primitive vectors",
        "integral.primitive_orbits.<group>",
        PrimitiveOrbitSeries,
    )
    yield (
        "Series of orbits on the discriminant group",
        "integral.discriminant_orbits.<group>",
        PrimitiveOrbitSeries,
    )
    yield "Definite lattice", "definite", DefiniteData
    yield (
        "Component of the root system of a definite lattice",
        "definite.roots[]",
        RootSystemComponent,
    )
    yield "Indefinite lattice", "indefinite", IndefiniteData
    yield "Hyperbolic lattice", "hyperbolic", HyperbolicData
    yield "Roots of a lattice that is not definite", "root_span", RootSpan
    yield "Related lattice", "related[]", Related
    yield "Reference", "references[]", Reference
    yield "Morphism", "morphisms[]", Morphism
    yield "Lie group card", "lie-groups/<slug>.md", LieGroup
    yield "Arithmetic group card", "arithmetic-groups/<slug>.md", ArithmeticGroup


def orthogonal_groups(
    target: Path,
    environment: Environment,
    lattices: dict[str, Lattice],
    groups: dict[str, LieGroup],
    arithmetic_groups: dict[str, ArithmeticGroup],
) -> None:
    """Write the Lie-group index from explicit lattice -> arithmetic -> Lie-group links."""
    counts: dict[tuple[int, int], int] = {}
    for lattice in lattices.values():
        if lattice.orthogonal_group is None:
            continue
        arithmetic = arithmetic_groups.get(lattice.orthogonal_group)
        if arithmetic is None:
            continue
        ambient = groups.get(arithmetic.ambient_lie_group)
        if ambient is None or ambient.orthogonal_signature is None:
            continue
        key = tuple(ambient.orthogonal_signature)
        counts[key] = counts.get(key, 0) + 1
    orthogonal = {
        tuple(group.orthogonal_signature): group
        for group in groups.values()
        if group.orthogonal_signature is not None
    }
    limit = max((q for _, q in orthogonal), default=0)
    columns = list(range(limit + 1))
    rows = [
        (
            p,
            [
                (q, orthogonal.get((p, q)), counts.get((p, q), 0))
                if q >= p
                else (q, None, None)
                for q in columns
            ],
        )
        for p in columns
    ]
    rendered = environment.get_template("orthogonal-groups.html.j2").render(
        root="./",
        columns=columns,
        rows=rows,
        groups=tuple(sorted(groups.values(), key=lambda group: group.slug)),
    )
    (target / "orthogonal-groups.html").write_text(rendered)
    (target / "lie-groups.html").write_text(rendered)


def build(root: Path, target: Path) -> int:
    """Write the site for the corpus under `root` to `target`. Returns the number of lattices."""
    corpus = load(root)
    entries = corpus.entries
    pages = collections(root / "pages", entries)
    theory = articles(root / "theory")
    by_tag = {entry.lattice.tag: entry for entry in entries}
    lattices = {tag: entry.lattice for tag, entry in by_tag.items()}
    environment = Environment(
        loader=PackageLoader("latticedb"),
        autoescape=select_autoescape(["html", "j2"]),
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    environment.filters["inline_markup"] = inline_markup
    environment.globals.update(
        rational_tex=rational_tex,
        group_tex=group_tex,
        genus_tex=genus_tex,
        orbit_group_tex=orbit_group_tex,
        subgroup_tex=subgroup_tex,
        cardinality_tex=cardinality_tex,
        orbit_series_tex=orbit_series_tex,
        zeta_tex=zeta_tex,
        theta_tex=theta_tex,
        root_system_tex=root_system_tex,
        set_tex=set_tex,
        combination_tex=combination_tex,
        block_tex=block_tex,
        properties=properties,
        definiteness_label=DEFINITENESS_LABEL,
        collections=pages,
        theory=theory,
        families=corpus.families,
        total=len(entries),
    )

    if target.exists():
        assert (target / "lattices.json").exists(), (
            f"{target} exists and is not a site that this command built"
        )
        shutil.rmtree(target)
    (target / "tag").mkdir(parents=True)
    (target / "collection").mkdir()
    (target / "theory").mkdir()
    (target / "lie-group").mkdir()
    (target / "arithmetic-group").mkdir()
    shutil.copytree(str(files("latticedb") / "assets"), target / "assets")

    ranks = sorted(
        {entry.lattice.rank for entry in entries if entry.lattice.rank is not None}
    )
    if any(entry.lattice.rank is None for entry in entries):
        ranks.append(None)
    by_rank = {
        rank: [entry for entry in entries if entry.lattice.rank == rank]
        for rank in ranks
    }
    geometric = corpus.geometric
    geometric_families = corpus.geometric_families
    graphs = corpus.graphs
    lie_groups = {entry.value.slug: entry.value for entry in corpus.lie_groups}
    arithmetic_groups = {entry.value.slug: entry.value for entry in corpus.arithmetic_groups}
    prose = markdown_to_html(
        [entry.prose for entry in entries]
        + [page.prose for page in pages]
        + [page.prose for page in theory]
    )
    lattice_page = environment.get_template("lattice.html.j2")
    incoming_by_tag: dict[str, list[tuple[Lattice, Morphism]]] = {}
    for source in lattices.values():
        for morphism in source.morphisms:
            incoming_by_tag.setdefault(morphism.target, []).append((source, morphism))
    for index, entry in enumerate(entries):
        lattice = entry.lattice
        components = json.dumps(
            [
                [
                    int(value) if value.denominator == 1 else str(value)
                    for value in components_row
                ]
                for components_row in lattice.gram_tensor or ()
            ]
        )
        (target / "tag" / f"{lattice.tag}.html").write_text(
            lattice_page.render(
                root="../",
                lattice=lattice,
                prose=prose[index],
                components_text=components.replace('"', ""),
                related=[
                    (by_tag[related.tag].lattice, related.relation)
                    for related in lattice.related
                ],
                span_name=root_span_name(lattice, lattices),
                span_summands=span_summands(lattice, lattices),
                span_images=summand_images(lattice, lattices),
                lattices=lattices,
                incoming_morphisms=incoming_by_tag.get(lattice.tag, ()),
                outgoing_morphisms=[
                    (morphism, lattices[morphism.target], matrix_tex(morphism), matrix_text(morphism))
                    for morphism in lattice.morphisms
                    if morphism.target in lattices
                ],
                geometric_objects=[
                    entry.geometric
                    for entry in geometric
                    if isinstance(entry.geometric, ProjectiveComplexVariety)
                    and any(
                        link.tag == lattice.tag
                        for link in entry.geometric.cohomology_lattices
                    )
                ],
                ambient_lie_group=(
                    lie_groups.get(arithmetic_groups[lattice.orthogonal_group].ambient_lie_group)
                    if lattice.orthogonal_group is not None
                    and lattice.orthogonal_group in arithmetic_groups
                    else None
                ),
                orthogonal_group=(
                    arithmetic_groups.get(lattice.orthogonal_group)
                    if lattice.orthogonal_group is not None
                    else None
                ),
                arithmetic_groups=[
                    arithmetic_groups[slug]
                    for slug in lattice.arithmetic_groups
                    if slug in arithmetic_groups
                ],
                previous=entries[index - 1].lattice if index > 0 else None,
                following=entries[index + 1].lattice
                if index + 1 < len(entries)
                else None,
            )
        )
    collection_page = environment.get_template("collection.html.j2")
    for index, page in enumerate(pages):
        html = collection_page.render(
            root="../",
            page=page,
            prose=prose[len(entries) + index],
            query=database_query(page.collection),
        )
        (target / "collection" / f"{page.slug}.html").write_text(html)
    article_page = environment.get_template("article.html.j2")
    for index, article in enumerate(theory):
        html = article_page.render(
            root="../",
            page=article,
            prose=prose[len(entries) + len(pages) + index],
        )
        (target / "theory" / f"{article.slug}.html").write_text(html)
    (target / "theory.html").write_text(
        environment.get_template("theory.html.j2").render(root="./")
    )
    orthogonal_groups(target, environment, lattices, lie_groups, arithmetic_groups)
    lie_group_prose = markdown_to_html([entry.prose for entry in corpus.lie_groups])
    lie_group_page = environment.get_template("lie-group.html.j2")
    for entry, rendered_prose in zip(corpus.lie_groups, lie_group_prose, strict=True):
        group = entry.value
        member_lattices = [
            lattice
            for lattice in lattices.values()
            if lattice.orthogonal_group is not None
            and lattice.orthogonal_group in arithmetic_groups
            and arithmetic_groups[lattice.orthogonal_group].ambient_lie_group == group.slug
        ]
        (target / "lie-group" / f"{group.slug}.html").write_text(
            lie_group_page.render(
                root="../",
                group=group,
                prose=rendered_prose,
                lattices=member_lattices,
                lie_groups=lie_groups,
            )
        )
    arithmetic_prose = markdown_to_html([entry.prose for entry in corpus.arithmetic_groups])
    arithmetic_group_page = environment.get_template("arithmetic-group.html.j2")
    for entry, rendered_prose in zip(corpus.arithmetic_groups, arithmetic_prose, strict=True):
        group = entry.value
        (target / "arithmetic-group" / f"{group.slug}.html").write_text(
            arithmetic_group_page.render(
                root="../",
                group=group,
                prose=rendered_prose,
                lattice=lattices[group.lattice],
                ambient=lie_groups[group.ambient_lie_group],
                parent=arithmetic_groups.get(group.parent_group) if group.parent_group else None,
            )
        )
    (target / "arithmetic-groups.html").write_text(
        environment.get_template("arithmetic-groups.html.j2").render(
            root="./",
            groups=tuple(sorted(arithmetic_groups.values(), key=lambda group: group.slug)),
            by_slug=arithmetic_groups,
            lie_groups=lie_groups,
        )
    )
    (target / "hodge-diamonds.html").write_text(
        environment.get_template("hodge-diamonds.html.j2").render(
            root="./",
            has_k3=any(entry.geometric.slug == "k3-surface" for entry in geometric),
        )
    )
    (target / "geometric-objects").mkdir()
    bibliography = root / "geometric-bibliography.bib"
    geometric_prose = markdown_to_html(
        [entry.prose for entry in geometric], bibliography
    )
    variety_page = environment.get_template("geometric-object.html.j2")
    space_page = environment.get_template("geometric-space.html.j2")
    for geometric_entry, rendered_prose in zip(geometric, geometric_prose, strict=True):
        record = geometric_entry.geometric
        if isinstance(record, ProjectiveComplexVariety):
            rows = [
                [
                    record.hodge_number(p, degree - p)
                    for p in range(
                        max(0, degree - record.dimension),
                        min(degree, record.dimension) + 1,
                    )
                ]
                for degree in range(2 * record.dimension + 1)
            ]
            html = variety_page.render(
                root="../",
                geometric=record,
                rows=rows,
                lattices=lattices,
                families={
                    entry.family.slug: entry.family for entry in geometric_families
                },
                prose=rendered_prose,
            )
        else:
            html = space_page.render(root="../", geometric=record, prose=rendered_prose)
        (target / "geometric-objects" / f"{record.slug}.html").write_text(html)
    (target / "geometric-families").mkdir()
    family_prose = markdown_to_html(
        [entry.prose for entry in geometric_families], bibliography
    )
    family_page = environment.get_template("geometric-family.html.j2")
    for family_entry, rendered_prose in zip(
        geometric_families, family_prose, strict=True
    ):
        family = family_entry.family
        instances = [
            entry.geometric
            for entry in geometric
            if entry.geometric.family == family.slug
        ]
        (target / "geometric-families" / f"{family.slug}.html").write_text(
            family_page.render(
                root="../", family=family, instances=instances, prose=rendered_prose
            )
        )
    (target / "geometric-objects.html").write_text(
        environment.get_template("geometric-objects.html.j2").render(
            root="./", geometric=geometric, geometric_families=geometric_families
        )
    )
    (target / "graphs").mkdir()
    graph_prose = markdown_to_html([entry.prose for entry in graphs], bibliography)
    graph_page = environment.get_template("graph.html.j2")
    for graph_entry, rendered_prose in zip(graphs, graph_prose, strict=True):
        graph = graph_entry.graph
        objects = [
            entry.geometric
            for entry in geometric
            if isinstance(entry.geometric, RiemannianSymmetricSpace)
            and graph.slug in entry.geometric.diagrams
        ]
        (target / "graphs" / f"{graph.slug}.html").write_text(
            graph_page.render(
                root="../", graph=graph, objects=objects, prose=rendered_prose
            )
        )
    (target / "graphs.html").write_text(
        environment.get_template("graphs.html.j2").render(root="./", graphs=graphs)
    )
    models = [
        (heading, key, model.__doc__, list(model.model_fields.items()))
        for heading, key, model in fields()
    ]
    (target / "index.html").write_text(
        environment.get_template("index.html.j2").render(root="./", by_rank=by_rank)
    )
    (target / "tags.html").write_text(
        environment.get_template("tags.html.j2").render(root="./", by_rank=by_rank)
    )
    (target / "database.html").write_text(
        environment.get_template("database.html.j2").render(root="./")
    )
    family_counts = {
        family: sum(family in entry.lattice.families for entry in entries)
        for family in corpus.families
    }
    fields_page = environment.get_template("fields.html.j2")
    (target / "fields.html").write_text(
        fields_page.render(
            root="./",
            models=models,
            property_meanings=PROPERTY_MEANINGS,
            family_counts=family_counts,
        )
    )
    (target / "lattices.json").write_text(
        json.dumps(
            {"rows": [row(entry.lattice, lattices) for entry in entries]},
            separators=(",", ":"),
        )
    )
    broken = broken_links(target)
    assert not broken, "links to a missing page or anchor:\n" + "\n".join(broken)
    return len(entries)
