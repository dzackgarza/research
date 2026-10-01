"""The text of a record, and the fields of a record that the Gram tensor determines.

`derive` computes every field that the Gram tensor determines and keeps the
other stored fields: the names, the families, the references, the genus
symbol, the order of the isometry group, and the
`root_span` block of a lattice that is not definite when the search for roots
does not decide it. `record_text` writes a record in the layout of the
corpus. A record that is not definite and has no `root_span` block after
`derive` is not decided. `morphisms_text` writes a morphism file.
"""

from fractions import Fraction

import yaml

from latticedb import arithmetic, model, roots
from latticedb.arithmetic import GramTensor, Vector
from latticedb.model import Yaml

KEYS = (
    "tag",
    "name",
    "latex",
    "aliases",
    "rank",
    "gram_tensor",
    "signature",
    "determinant",
    "definiteness",
    "integral",
    "definite",
    "indefinite",
    "root_span",
    "families",
    "related",
    "references",
    "hyperbolic",
)
"""The keys of a record, in the order in which a record lists them."""


class Flow(list[Yaml]):
    """A list that YAML writes on one line."""


yaml.add_representer(Flow, lambda dumper, data: dumper.represent_sequence("tag:yaml.org,2002:seq", data, flow_style=True))


def _is_scalar(value: Yaml) -> bool:
    match value:
        case list() | dict():
            return False
        case _:
            return True


def _styled(value: Yaml) -> Yaml:
    """Return the value with each list of scalars as a `Flow`: the layout of a record."""
    match value:
        case dict():
            return {key: _styled(item) for key, item in value.items()}
        case list() if all(_is_scalar(item) for item in value):
            return Flow(value)
        case list():
            return [_styled(item) for item in value]
        case _:
            return value


def record_text(record: dict[str, Yaml], prose: str) -> str:
    """Return the text of the file of a record."""
    assert set(record) <= set(KEYS), set(record) - set(KEYS)
    ordered = {key: _styled(record[key]) for key in KEYS if key in record}
    return "---\n" + yaml.dump(ordered, sort_keys=False, allow_unicode=True, width=100000) + "---\n" + _body(prose)


def _body(prose: str) -> str:
    """The prose after the front matter: nothing when there is no prose, else a blank line and the prose."""
    return "\n" + prose + "\n" if prose else ""


MORPHISM_KEYS = ("name", "description", "matrix", "row_subdivisions", "column_subdivisions")
"""The keys of a morphism, in the order in which a morphism file lists them."""


def morphisms_text(source: str, target: str, morphisms: list[dict[str, Yaml]], prose: str) -> str:
    """Return the text of the file `morphisms/<source>-<target>.md`."""
    assert all(set(morphism) <= set(MORPHISM_KEYS) for morphism in morphisms)
    ordered = [{key: _styled(morphism[key]) for key in MORPHISM_KEYS if key in morphism} for morphism in morphisms]
    document = {"source": source, "target": target, "morphisms": ordered}
    return "---\n" + yaml.dump(document, sort_keys=False, allow_unicode=True, width=100000) + "---\n" + _body(prose)


def rational(value: Fraction) -> int | str:
    """Return the value as a record writes it: an integer, or a string `p/q`."""
    return int(value) if value.denominator == 1 else str(value)


def gram_tensor(rows: Yaml) -> GramTensor:
    """Read the `gram_tensor` field of a record: rows of integers or strings `p/q`."""
    match rows:
        case list():
            return tuple(_row(row) for row in rows)
        case _:
            raise AssertionError("gram_tensor is a list of rows")


def _row(row: Yaml) -> tuple[Fraction, ...]:
    match row:
        case list():
            return tuple(model.rational(value) for value in row)
        case _:
            raise AssertionError("each row of gram_tensor is a list")


def _block(record: dict[str, Yaml], key: str) -> dict[str, Yaml]:
    match record.get(key):
        case dict() as block:
            return block
        case _:
            return {}


def _ordered(block: dict[str, Yaml], fields: tuple[str, ...]) -> dict[str, Yaml]:
    assert set(block) <= set(fields), set(block) - set(fields)
    return {field: block[field] for field in fields if field in block}


def _integral(record: dict[str, Yaml], gram: GramTensor) -> dict[str, Yaml]:
    rank = len(gram)
    declared = _block(record, "integral")
    block: dict[str, Yaml] = {"parity": "even" if all(gram[i][i] % 2 == 0 for i in range(rank)) else "odd"}
    if arithmetic.determinant(gram) != 0:
        block["discriminant_group"] = list(arithmetic.discriminant_invariants(gram))
        count = arithmetic.overlattice_count(gram)
        if count is not None:
            block["overlattice_count"] = count
        if "genus_symbol" in declared:
            block["genus_symbol"] = declared["genus_symbol"]
    return _ordered(block, tuple(model.IntegralData.model_fields))


def _definite(record: dict[str, Yaml], gram: GramTensor) -> dict[str, Yaml]:
    declared = _block(record, "definite")
    minimum, kissing_number = arithmetic.minimum_and_kissing_number(gram)
    block: dict[str, Yaml] = {"minimum": rational(minimum), "kissing_number": kissing_number}
    if "automorphism_group_order" in declared:
        block["automorphism_group_order"] = declared["automorphism_group_order"]
    positive_roots = arithmetic.definite_roots(gram)
    if arithmetic.is_integer_valued(gram):
        bound = model.theta_bound(len(gram), minimum)
        match declared.get("theta_series"):
            case list() as stated:
                bound = max(bound, len(stated) - 1)
        block["theta_series"] = list(arithmetic.theta_coefficients(gram, bound))
        block["root_system"] = list(roots.norm_two_types(gram, positive_roots))
    block["roots"] = [{"type": root_type, "scale": rational(scale), "simple_roots": [list(r) for r in simple]} for root_type, scale, simple in roots.root_system(gram)]
    return _ordered(block, tuple(model.DefiniteData.model_fields))


def _indefinite(gram: GramTensor) -> dict[str, Yaml]:
    isotropic = arithmetic.determinant(gram) == 0 or arithmetic.is_isotropic(gram)
    return {"isotropic": isotropic}


def _root_span(record: dict[str, Yaml], gram: GramTensor) -> dict[str, Yaml] | None:
    """The declared `root_span` block; else the roots found when they generate `L`; else `None`."""
    if "root_span" in record:
        return _block(record, "root_span")
    rank = len(gram)
    found: list[Vector] = roots.small_roots(gram)
    if not arithmetic.generate(found, rank):
        return None
    return {"roots": [list(r) for r in roots.generating_roots(found, rank)]}


def derive(record: dict[str, Yaml]) -> dict[str, Yaml]:
    """Return the record with every field that the Gram tensor determines computed from it.

    The fields `rank`, `signature`, `determinant` and `definiteness`; the
    blocks `integral`, `definite` and `indefinite`, each present exactly when
    its hypothesis holds; and `root_span` when the record has none and the
    roots that `roots.small_roots` finds generate `L`.
    """
    gram = gram_tensor(record["gram_tensor"])
    rank = len(gram)
    n_plus, n_minus, n_zero = arithmetic.inertia(gram)
    definiteness = model.definiteness(n_plus, n_minus, n_zero)
    derived: dict[str, Yaml] = {
        **record,
        "rank": rank,
        "signature": [n_plus, n_minus],
        "determinant": rational(arithmetic.determinant(gram)),
        "definiteness": definiteness,
    }
    for key in ("integral", "definite", "indefinite", "root_span"):
        derived.pop(key, None)
    if arithmetic.is_integer_valued(gram):
        derived["integral"] = _integral(record, gram)
    if definiteness in ("positive_definite", "negative_definite"):
        derived["definite"] = _definite(record, gram)
    else:
        span = _root_span(record, gram)
        if span is not None:
            derived["root_span"] = _ordered(span, tuple(model.RootSpan.model_fields))
    if definiteness == "indefinite":
        derived["indefinite"] = _indefinite(gram)
    return {key: derived[key] for key in KEYS if key in derived}
