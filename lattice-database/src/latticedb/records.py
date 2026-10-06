"""Card serialization and orchestration of preamble-owned lattice operations.

`derive` constructs the corresponding preamble formed/lattice objects, calls
their public operations, and serializes returned values while preserving other
stored fields. It contains no independent lattice algorithm.

`record_text` writes a lattice card, including the morphisms whose domain is that card.
"""

from collections.abc import Mapping
from fractions import Fraction
import yaml

from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.rings import session_ring_objects

from latticedb import model
from latticedb.model import GramTensor, Lattice, Yaml

_SESSION_RINGS = session_ring_objects()
ZZ = _SESSION_RINGS["ZZ"]
QQ = _SESSION_RINGS["QQ"]

KEYS = (
    "tag",
    "name",
    "latex",
    "aliases",
    "certifications",
    "rank",
    "gram_tensor",
    "signature",
    "determinant",
    "definiteness",
    "dual_gram_tensor",
    "integral",
    "definite",
    "indefinite",
    "root_span",
    "root_sublattice",
    "morphisms",
    "orthogonal_group",
    "arithmetic_groups",
    "families",
    "related",
    "references",
    "hyperbolic",
)
"""The keys of a record, in the order in which a record lists them."""


class Flow(list[Yaml]):
    """A list that YAML writes on one line."""


yaml.add_representer(
    Flow,
    lambda dumper, data: dumper.represent_sequence(
        "tag:yaml.org,2002:seq", data, flow_style=True
    ),
)


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
    return (
        "---\n"
        + yaml.dump(ordered, sort_keys=False, allow_unicode=True, width=100000)
        + "---\n"
        + _body(prose)
    )


def _body(prose: str) -> str:
    """The prose after the front matter, in the form the Markdown formatter flowmark keeps.

    That is two blank lines when there is no prose, else a blank line and the prose.
    """
    return "\n" + prose + "\n" if prose else "\n\n"


MORPHISM_KEYS = (
    "target",
    "name",
    "description",
    "matrix",
    "scale",
    "row_subdivisions",
    "column_subdivisions",
)
"""The keys of a morphism, in the order in which a lattice card lists them."""


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


def _integral(
    record: dict[str, Yaml],
    gram: GramTensor,
    lattice,
) -> dict[str, Yaml]:
    rank = len(gram)
    declared = _block(record, "integral")
    block: dict[str, Yaml] = {
        "parity": "even" if lattice.is_even() else "odd"
    }
    if lattice.determinant() != 0:
        invariants = tuple(
            abs(int(factor))
            for factor in lattice.discriminant_group().invariant_factors()
            if abs(int(factor)) > 1
        )
        block["discriminant_group"] = list(invariants)
        if block["parity"] == "even" and all(factor == 2 for factor in invariants):
            block["delta"] = int(lattice.delta())
        block["bad_reduction_primes"] = [
            int(prime) for prime in lattice.bad_reduction_primes()
        ]
        if rank % 2 == 0:
            block["quadratic_character"] = int(
                lattice.discriminant_character_discriminant()
            )
        # Other stored invariants are preserved; their computation has separate preamble owners.
        for field in model.IntegralData.model_fields:
            if field not in block and field in declared:
                block[field] = declared[field]
    return _ordered(block, tuple(model.IntegralData.model_fields))


def _definite(
    record: dict[str, Yaml],
    gram: GramTensor,
    integral_lattice,
) -> dict[str, Yaml]:
    declared = _block(record, "definite")
    block: dict[str, Yaml] = dict(declared)
    if integral_lattice is not None:
        minimum_value = integral_lattice.minimum()
        minimum = Fraction(
            int(abs(minimum_value.numerator())),
            int(minimum_value.denominator()),
        )
        block["minimum"] = rational(minimum)
        block["kissing_number"] = int(integral_lattice.kissing_number())
    return _ordered(block, tuple(model.DefiniteData.model_fields))


def _indefinite(gram: GramTensor) -> dict[str, Yaml]:
    return {"isotropic": Lattices(QQ)(gram).is_isotropic()}


def derive(record: dict[str, Yaml]) -> dict[str, Yaml]:
    """Return the card with selected fields supplied by preamble-owned operations.

    The adapter serializes rank, signature, determinant, definiteness, the dual
    Gram tensor, selected integral invariants, definite minimum/kissing number
    and indefinite isotropy from preamble objects. Root-system/root-span/theta
    data are preserved when authored but are not produced here.

    A field not returned by these preamble calls is preserved when already present.
    Expensive exact invariants such as `integral.overlattice_count` are requested
    by separate enrichment/certification orchestration.
    """
    gram = gram_tensor(record["gram_tensor"])
    rank = len(gram)
    formed = ZZ.free_module(rank).equip_bilinear_form(QQ, gram)
    signature = formed.signature_pair()
    n_plus = int(signature.first())
    n_minus = int(signature.second())
    n_zero = rank - n_plus - n_minus
    formed_determinant = formed.determinant()
    determinant = Fraction(
        int(formed_determinant.numerator()),
        int(formed_determinant.denominator()),
    )
    integral_lattice = (
        Lattices(ZZ)(gram)
        if formed.is_base_ring_valued()
        else None
    )
    definiteness = formed.definiteness()
    dual: dict[str, Yaml] = {}
    if determinant != 0:
        dual_gram = Lattices(QQ)(gram).dual_lattice().gram_tensor()
        dual = {
            "dual_gram_tensor": [
                [
                    rational(
                        Fraction(
                            int(dual_gram[i, j].numerator()),
                            int(dual_gram[i, j].denominator()),
                        )
                    )
                    for j in range(rank)
                ]
                for i in range(rank)
            ]
        }
    derived: dict[str, Yaml] = {
        **record,
        "rank": rank,
        "signature": [n_plus, n_minus],
        "determinant": rational(determinant),
        "definiteness": definiteness,
        **dual,
    }
    for key in ("integral", "definite", "indefinite"):
        derived.pop(key, None)
    if integral_lattice is not None:
        derived["integral"] = _integral(record, gram, integral_lattice)
    if definiteness in ("positive_definite", "negative_definite"):
        derived["definite"] = _definite(record, gram, integral_lattice)
    if definiteness == "indefinite":
        derived["indefinite"] = _indefinite(gram)
    return {key: derived[key] for key in KEYS if key in derived}


def derived_projection(record: Mapping[str, Yaml]) -> dict[str, Yaml]:
    """The part of a card supplied by the preamble operations used by `derive`.

    Authored identity, bibliography, families, relations and fields merely
    preserved by `derive` are excluded. This projection is what the aggregate
    `<tag> derive` certificate binds.
    """
    projected: dict[str, Yaml] = {
        key: record[key]
        for key in (
            "rank",
            "signature",
            "determinant",
            "definiteness",
            "dual_gram_tensor",
        )
        if key in record
    }
    for block_name, fields in (
        (
            "integral",
            (
                "parity",
                "discriminant_group",
                "delta",
                "bad_reduction_primes",
                "quadratic_character",
            ),
        ),
        (
            "definite",
            ("minimum", "kissing_number"),
        ),
        ("indefinite", ("isotropic",)),
    ):
        block = record.get(block_name)
        if isinstance(block, dict):
            projected[block_name] = {
                field: block[field] for field in fields if field in block
            }
    return projected
