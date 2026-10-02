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
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from fractions import Fraction
from html.parser import HTMLParser
from importlib.resources import files
from pathlib import Path
from urllib.parse import urlencode, urlsplit

import frontmatter
from flint import fmpz
from jinja2 import Environment, PackageLoader, StrictUndefined, select_autoescape
from markupsafe import Markup, escape
from pydantic import BaseModel, Field

from latticedb import root_systems
from latticedb.arithmetic import Vector
from latticedb.corpus import Entry, hyperbolic_index_bounds, load
from latticedb.model import (
    DefiniteData,
    HyperbolicData,
    IndefiniteData,
    IntegralData,
    Lattice,
    Morphism,
    Morphisms,
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


class Article(Record):
    """A page of `theory/`: the one place where the site explains a part of the theory, which the other pages link to."""

    title: str = Field(description="Title of the page. Dollar signs mark TeX.")
    summary: str = Field(description="One sentence that says what the page explains. Dollar signs mark TeX.")
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


def orbit_group_tex(group: OrbitGroup) -> str:
    """TeX for a key of `integral.primitive_orbits`, such as `\\widetilde{SO}^+(L)` for `SOtilde+`."""
    name, plus = group.removesuffix("+"), "^+" if group.endswith("+") else ""
    letters = name.removesuffix("tilde")
    return f"\\widetilde{{{letters}}}{plus}(L)" if name.endswith("tilde") else f"\\mathrm{{{letters}}}{plus}(L)"


def orbit_series_tex(series: PrimitiveOrbitSeries) -> str:
    """TeX for $F_{L,\\Gamma}(z, w)$: the stated nonzero terms, `?` for each coefficient that is not stated, and the order to which the series is stated."""
    terms = []
    for n in sorted(series.degrees, key=lambda n: (abs(n), -n)):
        count = series.coefficient(n)
        if count == 0:
            continue
        variable = "" if n == 0 else ("z" if n > 0 else "w") + (f"^{{{abs(n)}}}" if abs(n) > 1 else "")
        coefficient = "?" if count is None else str(count)
        terms.append(coefficient if not variable else (variable if coefficient == "1" else f"{coefficient}\\,{variable}"))
    order = f"O(z^{{{len(series.z) + 1}}}, w^{{{len(series.w) + 1}}})"
    return " + ".join([*terms, order])


def _argument(shift: int) -> str:
    """TeX for $s - k$."""
    return "s" if shift == 0 else f"s - {shift}" if shift > 0 else f"s + {-shift}"


def _l_tex(shift: int, discriminant: str) -> str:
    """TeX for $L^\\Sigma(s - k, \\chi_d)$, which is $\\zeta^\\Sigma(s - k)$ for the trivial character."""
    if discriminant == "1":
        return f"\\zeta^\\Sigma({_argument(shift)})"
    return f"L^\\Sigma({_argument(shift)}, \\chi_{{{discriminant}}})"


def zeta_tex(lattice: Lattice, cone: bool) -> str:
    """TeX for $\\zeta^\\Sigma(X_n, s)$ of $X_n : Q(x) = n$: for $n = 0$ when `cone`, and for $n \\neq 0$ otherwise (theory page `zeta`)."""
    assert lattice.integral is not None and lattice.determinant != 0
    m = lattice.rank // 2
    if lattice.rank % 2 == 1:
        if cone:
            return _l_tex(2 * m, "1")
        coefficient = (-1) ** m * int(lattice.determinant)
        discriminant = "n" if coefficient == 1 else "-n" if coefficient == -1 else f"{coefficient}n"
        return f"{_l_tex(2 * m, '1')}\\, {_l_tex(m, discriminant)}"
    character = str(lattice.integral.quadratic_character)
    if cone:
        return f"\\frac{{{_l_tex(2 * m - 1, '1')}\\, {_l_tex(m, character)}}}{{{_l_tex(m - 1, character)}}}"
    return f"\\frac{{{_l_tex(2 * m - 1, '1')}}}{{{_l_tex(m - 1, character)}}}"


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
    return ("-" if first_sign == "-" else "") + first + "".join(f" {sign} {term}" for sign, term in terms[1:])


def _runs(names: list[str]) -> list[tuple[str, int]]:
    return [(name, names.count(name)) for name in dict.fromkeys(names)]


def component_lattice(component: RootSystemComponent) -> tuple[str, int, Fraction]:
    """`(letter, rank, k)`: the root lattice of the component is the standard lattice of that letter and rank with the form `k b`."""
    letter, rank, factor = root_systems.root_lattice(component.type)
    return letter, rank, factor * component.scale


def component_lattice_tex(component: RootSystemComponent) -> str:
    """`E_{8}`, `D_{4}(2)`, `\\mathrm{I}_{10,0}`, and `\\langle 4 \\rangle` for `A_1(2)`."""
    letter, rank, scale = component_lattice(component)
    if (letter, rank) == ("A", 1):
        return f"\\langle {rational_tex(2 * scale)} \\rangle"
    name = f"\\mathrm{{I}}_{{{rank},0}}" if letter == "I" else f"{letter}_{{{rank}}}"
    return name if scale == 1 else f"{name}({rational_tex(scale)})"


def component_lattice_text(component: RootSystemComponent) -> str:
    """`E8`, `D4(2)`, `I_{10,0}`, and `<4>` for `A1(2)`."""
    letter, rank, scale = component_lattice(component)
    if (letter, rank) == ("A", 1):
        return f"<{2 * scale}>"
    name = f"I_{{{rank},0}}" if letter == "I" else f"{letter}{rank}"
    return name if scale == 1 else f"{name}({scale})"


def root_span_tex(components: tuple[RootSystemComponent, ...]) -> str:
    """`D_{4}(2)^{2} \\oplus \\langle 4 \\rangle`: the orthogonal sum of the root lattices of the components; `0` for no component."""
    runs = _runs([component_lattice_tex(component) for component in components])
    return " \\oplus ".join(f"{name}^{{{count}}}" if count > 1 else name for name, count in runs) or "0"


def root_span_text(components: tuple[RootSystemComponent, ...]) -> str:
    runs = _runs([component_lattice_text(component) for component in components])
    return " + ".join(f"{name}^{count}" if count > 1 else name for name, count in runs) or "0"


def component_norms(component: RootSystemComponent) -> tuple[Fraction, ...]:
    """The values `b(\\alpha_i, \\alpha_i) = k (\\alpha_i, \\alpha_i)` on the simple roots; each root of the component is the image of a simple root under the Weyl group."""
    gram = root_systems.simple_root_gram(component.type)
    return tuple(component.scale * gram[i][i] for i in range(component.rank))


def orthogonal_blocks(lattice: Lattice) -> list[list[int]]:
    """The finest partition of the indices $1, \\dots, n$ such that $b(e_i, e_j) = 0$ for $i$, $j$ in different parts.

    The parts are the connected components of the graph on the basis vectors with an edge where $b(e_i, e_j) \\neq 0$.
    The record fixes the orthogonal decomposition of $L$ into the sublattices that the parts generate.
    """
    blocks: list[list[int]] = []
    for index, components_row in enumerate(lattice.gram_tensor, start=1):
        linked = [block for block in blocks if any(components_row[other - 1] != 0 for other in block)]
        blocks = [block for block in blocks if block not in linked] + [sorted([*(other for block in linked for other in block), index])]
    return sorted(blocks)


def block_tex(block: list[int], symbol: str = "e") -> str:
    """`e_{3}, \\dots, e_{10}` for the indices 3 to 10; each vector for fewer than four indices or a block with a gap."""
    if len(block) > 3 and block[-1] - block[0] == len(block) - 1:
        return f"{symbol}_{{{block[0]}}}, \\dots, {symbol}_{{{block[-1]}}}"
    return ", ".join(f"{symbol}_{{{index}}}" for index in block)


def matrix_tex(morphism: Morphism) -> str:
    """The matrix as a TeX `array`, with a vertical line at each column subdivision and `\\hline` at each row subdivision."""
    columns = len(morphism.matrix[0])
    bounds = (0, *morphism.column_subdivisions, columns)
    alignment = "|".join("r" * (high - low) for low, high in zip(bounds, bounds[1:], strict=False))
    lines = []
    for index, matrix_row in enumerate(morphism.matrix):
        if index in morphism.row_subdivisions:
            lines.append("\\hline")
        lines.append(" & ".join(str(value) for value in matrix_row) + " \\\\")
    return f"\\left(\\begin{{array}}{{{alignment}}}\n" + "\n".join(lines) + "\n\\end{array}\\right)"


def matrix_text(morphism: Morphism) -> str:
    """The matrix and its subdivisions as JSON, one row per line, in the form that `latticedb morphism` reads."""
    rows = ",\n  ".join(json.dumps(list(matrix_row)) for matrix_row in morphism.matrix)
    row_lines = json.dumps(list(morphism.row_subdivisions))
    column_lines = json.dumps(list(morphism.column_subdivisions))
    return f'{{"matrix": [\n  {rows}\n],\n "row_subdivisions": {row_lines},\n "column_subdivisions": {column_lines}}}'


def summand_name(record: Lattice, scale: int) -> tuple[str, str]:
    """The name of $M(k)$ as text and as TeX: `<ka>` for the rank-one record `<a>`, the name of `M` for `k = 1`, and `M(k)` otherwise."""
    if record.rank == 1:
        value = scale * record.gram_tensor[0][0]
        return f"<{value}>", f"\\langle {rational_tex(value)} \\rangle"
    if scale == 1:
        return record.name, record.latex
    return f"{record.name}({scale})", f"{record.latex}({scale})"


def span_summands(lattice: Lattice, lattices: dict[str, Lattice]) -> list[tuple[Lattice, str]]:
    """`(M, name of M(k) as TeX)` for each summand $M(k)$ of `root_span.summands`."""
    span = lattice.root_span
    if span is None or span.summands is None:
        return []
    return [(lattices[summand.tag], summand_name(lattices[summand.tag], summand.scale)[1]) for summand in span.summands]


def summand_images(lattice: Lattice, lattices: dict[str, Lattice]) -> list[tuple[Lattice, str, int, Vector]]:
    """`(M, name of M(k) as TeX, j, x)` for each row `x` of `root_span.embedding`: the embedding sends the basis vector $e_j$ of the summand $M(k)$ to `x`."""
    span = lattice.root_span
    if span is None or span.summands is None or span.embedding is None:
        return []
    sources = [(record, name, j) for record, name in span_summands(lattice, lattices) for j in range(1, record.rank + 1)]
    return [(record, name, j, image) for (record, name, j), image in zip(sources, span.embedding, strict=True)]


def inline_markup(text: str) -> Markup:
    """HTML for one line of copy, in which backticks mark code and dollar signs mark TeX."""
    code = re.sub(r"`([^`]+)`", r"<code>\1</code>", str(escape(text)))
    return Markup(re.sub(r"\$([^$]+)\$", r"\\(\1\\)", code))


def theta_tex(theta: tuple[int, ...]) -> str:
    terms = ["1", *(f"{count}q^{{{power}}}" if power > 1 else f"{count}q" for power, count in enumerate(theta) if power > 0 and count > 0)]
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
    "isotropic": ("indefinite-lattices", "isotropic", "$L$ is indefinite and isotropic."),
    "anisotropic": ("indefinite-lattices", "isotropic", "$L$ is indefinite and not isotropic."),
    "reflective": ("indefinite-lattices", "reflective", "$L$ is reflective."),
    "not reflective": ("indefinite-lattices", "reflective", "$L$ is hyperbolic and not reflective."),
}
"""Property label of the database -> (theory page, anchor of the definition, the condition). `p-elementary` stands for the labels that state a prime."""


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
    match lattice.is_root_lattice:
        case True:
            found.append("root lattice")
        case False:
            found.append("not a root lattice")
    if not lattice.is_nondegenerate:
        found.append("degenerate")
    if lattice.is_hyperbolic:
        found.append("hyperbolic")
    if lattice.indefinite is not None:
        found.append("isotropic" if lattice.indefinite.isotropic else "anisotropic")
    if lattice.hyperbolic is not None:
        found.append("reflective" if lattice.hyperbolic.reflective else "not reflective")
    return found


def root_span_name(lattice: Lattice, lattices: dict[str, Lattice]) -> tuple[str, str] | None:
    """A lattice isometric to $\\mathbb{Z}\\Phi(L)$, as text and as TeX; `None` when the record does not state one.

    Definite lattice: the orthogonal sum of the root lattices of the components
    of `definite.roots`. Other lattice: the orthogonal sum of the records of
    `root_span.summands`, `0` when the lattice has no roots, and `L` when the
    rows of `root_span.roots` generate `L`.
    """
    if lattice.definite is not None and lattice.definite.roots is not None:
        return root_span_text(lattice.definite.roots), root_span_tex(lattice.definite.roots)
    span = lattice.root_span
    if span is None:
        return None
    if span.summands is not None:
        names = [summand_name(lattices[summand.tag], summand.scale) for summand in span.summands]
        return " + ".join(text for text, _ in names), " \\oplus ".join(tex for _, tex in names)
    if not span.roots:
        return "0", "0"
    return ("L", "L") if lattice.is_root_lattice else None


def root_span_primitive(lattice: Lattice) -> str:
    """Whether $R(L) = \\mathbb{Z}\\Phi(L)$ is primitive in $L$, as the text of a cell."""
    match lattice.root_span_is_primitive:
        case True:
            return "yes"
        case False:
            return "no"
        case None:
            return "not decided"


def row(lattice: Lattice, lattices: dict[str, Lattice]) -> Row:
    """The row of a lattice in `lattices.json`. `lattices` maps each tag of the corpus to its lattice."""
    integral, definite = lattice.integral, lattice.definite
    group = integral.discriminant_group if integral else None
    order = definite.automorphism_group_order if definite else None
    phi = tuple(component.type for component in definite.roots) if definite and definite.roots is not None else None
    span_name = root_span_name(lattice, lattices)
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
        "genus_class_count": integral.genus_class_count if integral else None,
        "hyperbolic_index": integral.hyperbolic_index if integral else None,
        "overlattice_count": integral.overlattice_count if integral else None,
        "delta": integral.delta if integral else None,
        "minimum": str(definite.minimum) if definite else None,
        "minimum_value": float(definite.minimum) if definite else None,
        "kissing_number": definite.kissing_number if definite else None,
        "automorphism_group_order": str(order) if order is not None else None,
        "automorphism_group_order_value": float(order) if order is not None else None,
        "root_system": " ".join(definite.root_system) if definite and definite.root_system is not None else None,
        "root_system_tex": root_system_tex(definite.root_system) if definite and definite.root_system else None,
        "phi_type": " ".join(phi) if phi is not None else None,
        "phi_type_tex": (root_system_tex(phi) or "\\varnothing") if phi is not None else None,
        "root_span": span_name[0] if span_name else None,
        "root_span_tex": span_name[1] if span_name else None,
        "root_span_rank": lattice.root_span_rank,
        "root_span_index": lattice.root_span_index if lattice.root_span_rank == lattice.rank else None,
        "root_span_primitive": root_span_primitive(lattice),
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
    lattices = {entry.lattice.tag: entry.lattice for entry in entries}
    rows = {tag: row(lattice, lattices) for tag, lattice in lattices.items()}
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


def articles(directory: Path) -> tuple[ArticlePage, ...]:
    pages = []
    for path in directory.glob("*.md"):
        document = frontmatter.load(str(path))
        pages.append(ArticlePage(path.stem, Article.model_validate(document.metadata), document.content))
    orders = [page.article.order for page in pages]
    assert len(set(orders)) == len(orders), f"{directory}: two theory pages have one order"
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
            if not destination.exists() or (parts.fragment and parts.fragment not in pages[destination].ids):
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


def markdown_to_html(texts: list[str], bibliography: Path | None = None) -> list[Markup]:
    """HTML for each Markdown text. TeX stays as `\\(...\\)` for MathJax."""

    def convert(text: str) -> Markup:
        command = ["pandoc", "--from=markdown", "--to=html", "--mathjax"]
        if bibliography is not None:
            command += ["--citeproc", "--fail-if-warnings", f"--bibliography={bibliography}"]
        done = subprocess.run(command, input=text, capture_output=True, text=True, check=True)
        return Markup(done.stdout)

    with ThreadPoolExecutor() as pool:
        return list(pool.map(convert, texts))


def fields() -> Iterator[tuple[str, str | None, type[BaseModel]]]:
    """The models of the schema: heading, block key, model."""
    yield "Every lattice", None, Lattice
    yield "Integral lattice", "integral", IntegralData
    yield "Series of orbits of primitive vectors", "integral.primitive_orbits.<group>", PrimitiveOrbitSeries
    yield "Definite lattice", "definite", DefiniteData
    yield "Component of the root system of a definite lattice", "definite.roots[]", RootSystemComponent
    yield "Indefinite lattice", "indefinite", IndefiniteData
    yield "Hyperbolic lattice", "hyperbolic", HyperbolicData
    yield "Roots of a lattice that is not definite", "root_span", RootSpan
    yield "Related lattice", "related[]", Related
    yield "Reference", "references[]", Reference
    yield "Morphisms between two lattices", "morphisms/<S>-<T>.md", Morphisms
    yield "Morphism", "morphisms[]", Morphism


def build(root: Path, target: Path) -> int:
    """Write the site for the corpus under `root` to `target`. Returns the number of lattices."""
    corpus = load(root)
    entries = corpus.entries
    pages = collections(root / "pages", entries)
    theory = articles(root / "theory")
    by_tag = {entry.lattice.tag: entry for entry in entries}
    lattices = {tag: entry.lattice for tag, entry in by_tag.items()}
    environment = Environment(loader=PackageLoader("latticedb"), autoescape=select_autoescape(["html", "j2"]), undefined=StrictUndefined, trim_blocks=True, lstrip_blocks=True)
    environment.filters["inline_markup"] = inline_markup
    environment.globals.update(
        rational_tex=rational_tex,
        group_tex=group_tex,
        factorisation_tex=factorisation_tex,
        genus_tex=genus_tex,
        orbit_group_tex=orbit_group_tex,
        orbit_series_tex=orbit_series_tex,
        zeta_tex=zeta_tex,
        theta_tex=theta_tex,
        root_system_tex=root_system_tex,
        set_tex=set_tex,
        combination_tex=combination_tex,
        component_lattice_tex=component_lattice_tex,
        component_norms=component_norms,
        block_tex=block_tex,
        root_count=root_systems.root_count,
        properties=properties,
        definiteness_label=DEFINITENESS_LABEL,
        collections=pages,
        theory=theory,
        families=corpus.families,
        total=len(entries),
    )

    if target.exists():
        assert (target / "lattices.json").exists(), f"{target} exists and is not a site that this command built"
        shutil.rmtree(target)
    (target / "tag").mkdir(parents=True)
    (target / "collection").mkdir()
    (target / "morphism").mkdir()
    (target / "theory").mkdir()
    shutil.copytree(str(files("latticedb") / "assets"), target / "assets")

    ranks = sorted({entry.lattice.rank for entry in entries})
    by_rank = {rank: [entry for entry in entries if entry.lattice.rank == rank] for rank in ranks}
    morphism_files = [entry.morphisms for entry in corpus.morphisms]
    geometric = corpus.geometric
    geometric_families = corpus.geometric_families
    prose = markdown_to_html(
        [entry.prose for entry in entries] + [page.prose for page in pages] + [entry.prose for entry in corpus.morphisms] + [page.prose for page in theory]
    )
    lattice_page = environment.get_template("lattice.html.j2")
    bounds = hyperbolic_index_bounds(corpus.morphisms, entries)
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
                span_name=root_span_name(lattice, lattices),
                span_summands=span_summands(lattice, lattices),
                span_images=summand_images(lattice, lattices),
                blocks=orthogonal_blocks(lattice),
                hyperbolic_bound=bounds.get(lattice.tag),
                lattices=lattices,
                morphism_files=[file for file in morphism_files if lattice.tag in (file.source, file.target)],
                geometric_objects=[entry.geometric for entry in geometric if any(link.tag == lattice.tag for link in entry.geometric.cohomology_lattices)],
                previous=entries[index - 1].lattice if index > 0 else None,
                following=entries[index + 1].lattice if index + 1 < len(entries) else None,
            )
        )
    collection_page = environment.get_template("collection.html.j2")
    for index, page in enumerate(pages):
        html = collection_page.render(root="../", page=page, prose=prose[len(entries) + index], query=database_query(page.collection))
        (target / "collection" / f"{page.slug}.html").write_text(html)
    morphism_page = environment.get_template("morphism.html.j2")
    for index, file in enumerate(morphism_files):
        html = morphism_page.render(
            root="../",
            file=file,
            source=lattices[file.source],
            target=lattices[file.target],
            prose=prose[len(entries) + len(pages) + index],
            morphisms=[(morphism, matrix_tex(morphism), matrix_text(morphism)) for morphism in file.morphisms],
        )
        (target / "morphism" / f"{file.source}-{file.target}.html").write_text(html)
    article_page = environment.get_template("article.html.j2")
    for index, article in enumerate(theory):
        html = article_page.render(root="../", page=article, prose=prose[len(entries) + len(pages) + len(morphism_files) + index])
        (target / "theory" / f"{article.slug}.html").write_text(html)
    (target / "theory.html").write_text(environment.get_template("theory.html.j2").render(root="./"))
    (target / "morphisms.html").write_text(environment.get_template("morphisms.html.j2").render(root="./", files=morphism_files, lattices=lattices))
    (target / "geometric-objects").mkdir()
    bibliography = root / "geometric-bibliography.bib"
    geometric_prose = markdown_to_html([entry.prose for entry in geometric], bibliography)
    geometric_page = environment.get_template("geometric-object.html.j2")
    for geometric_entry, rendered_prose in zip(geometric, geometric_prose, strict=True):
        record = geometric_entry.geometric
        rows = [
            [record.hodge_number(p, degree - p) for p in range(max(0, degree - record.dimension), min(degree, record.dimension) + 1)]
            for degree in range(2 * record.dimension + 1)
        ]
        (target / "geometric-objects" / f"{record.slug}.html").write_text(
            geometric_page.render(
                root="../",
                geometric=record,
                rows=rows,
                lattices=lattices,
                families={entry.family.slug: entry.family for entry in geometric_families},
                prose=rendered_prose,
            )
        )
    (target / "geometric-families").mkdir()
    family_prose = markdown_to_html([entry.prose for entry in geometric_families], bibliography)
    family_page = environment.get_template("geometric-family.html.j2")
    for family_entry, rendered_prose in zip(geometric_families, family_prose, strict=True):
        family = family_entry.family
        instances = [entry.geometric for entry in geometric if entry.geometric.family == family.slug]
        (target / "geometric-families" / f"{family.slug}.html").write_text(family_page.render(root="../", family=family, instances=instances, prose=rendered_prose))
    (target / "geometric-objects.html").write_text(
        environment.get_template("geometric-objects.html.j2").render(root="./", geometric=geometric, geometric_families=geometric_families)
    )
    models = [(heading, key, model.__doc__, list(model.model_fields.items())) for heading, key, model in fields()]
    (target / "index.html").write_text(environment.get_template("index.html.j2").render(root="./", by_rank=by_rank))
    (target / "tags.html").write_text(environment.get_template("tags.html.j2").render(root="./", by_rank=by_rank))
    (target / "database.html").write_text(environment.get_template("database.html.j2").render(root="./"))
    family_counts = {family: sum(family in entry.lattice.families for entry in entries) for family in corpus.families}
    fields_page = environment.get_template("fields.html.j2")
    (target / "fields.html").write_text(fields_page.render(root="./", models=models, property_meanings=PROPERTY_MEANINGS, family_counts=family_counts))
    (target / "lattices.json").write_text(json.dumps({"rows": [row(entry.lattice, lattices) for entry in entries]}, separators=(",", ":")))
    broken = broken_links(target)
    assert not broken, "links to a missing page or anchor:\n" + "\n".join(broken)
    return len(entries)
