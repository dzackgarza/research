"""The seeding of the corpus: the values of a record are computed here once, when the record is written.

`derive` computes every field that the Gram tensor determines and keeps the
other stored fields: the names, the families, the references, the values
that `latticedb certify` computes with SageMath, and the
`root_span` block of a lattice that is not definite when the search for roots
does not decide it. A record that is not definite and has no `root_span`
block after `derive` is not decided.

`gram_problems`, `admission_problems` and `morphism_problems` check a new
record or morphism before it is written: the Gram tensor, the declared values,
and the statements against the records already written. Reading the corpus
does none of this again.

`record_text` writes a lattice card, including the morphisms whose domain is that card.
"""

from collections.abc import Mapping
from fractions import Fraction
from itertools import combinations

import yaml

from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.rings import session_ring_objects

from latticedb import model, roots
from flint import fmpq, fmpq_mat
from latticedb.model import AdeType, Definiteness, GramTensor, Lattice, Morphism, Vector, Yaml

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


def _vectors(rows: Yaml) -> list[Vector]:
    """Read a matrix of integers from a record: one vector for each row."""
    match rows:
        case list():
            return [_vector(row) for row in rows]
        case _:
            raise AssertionError("a matrix is a list of rows")


def _vector(row: Yaml) -> Vector:
    match row:
        case list():
            return tuple(int(model.rational(entry)) for entry in row)
        case _:
            raise AssertionError("each row of a matrix is a list")


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
        # Expensive exact invariants computed by enrichment are preserved.
        for field in model.IntegralData.model_fields:
            if field not in block and field in declared:
                block[field] = declared[field]
    return _ordered(block, tuple(model.IntegralData.model_fields))


def _definite(
    record: dict[str, Yaml],
    gram: GramTensor,
    positive_roots: Mapping[Vector, Fraction],
    formed,
    computation_lattice,
    rescaling: Fraction,
    integral_lattice=None,
) -> dict[str, Yaml]:
    declared = _block(record, "definite")
    minimum = Fraction(int(abs(computation_lattice.minimum()))) / rescaling
    kissing_number = int(computation_lattice.kissing_number())
    block: dict[str, Yaml] = {
        "minimum": rational(minimum),
        "kissing_number": kissing_number,
    }
    if integral_lattice is not None:
        bound = model.theta_bound(len(gram), minimum)
        match declared.get("theta_series"):
            case list() as stated:
                bound = max(bound, len(stated) - 1)
        series = integral_lattice.theta_series(precision=bound + 1)
        block["theta_series"] = [int(series[index]) for index in range(bound + 1)]
        block["root_system"] = list(roots.norm_two_types(formed, dict(positive_roots)))
    block["roots"] = [
        {
            "type": root_type,
            "scale": rational(scale),
            "simple_roots": [list(r) for r in simple],
        }
        for root_type, scale, simple in roots.root_system(formed, dict(positive_roots))
    ]
    for field in model.DefiniteData.model_fields:
        if field not in block and field in declared:
            block[field] = declared[field]
    return _ordered(block, tuple(model.DefiniteData.model_fields))


def _indefinite(gram: GramTensor) -> dict[str, Yaml]:
    rational_space = Lattices(QQ)(gram)
    isotropic = rational_space.determinant() == 0 or int(rational_space.witt_index()) > 0
    return {"isotropic": isotropic}


def _root_span(
    record: dict[str, Yaml], gram: GramTensor, formed, lattice=None
) -> tuple[dict[str, Yaml], list[Vector]] | None:
    """The declared `root_span` block, else the roots found when they generate `L`, with the norms of the roots; else `None`."""
    if "root_span" in record:
        block = dict(_block(record, "root_span"))
        spanning = _vectors(block["roots"])
    else:
        rank = len(gram)
        found: list[Vector] = roots.small_roots(gram, lattice=lattice)
        ambient = ZZ.free_module(rank)
        found_span = ambient.subobject_on(tuple(ambient(vector) for vector in found))
        if any(
            ambient.module_generator(label) not in found_span
            for label in ambient.module_generating_set()
        ):
            return None
        spanning = list(roots.generating_roots(found, rank))
        block = {"roots": [list(r) for r in spanning]}
    block["norms"] = [
        rational(
            Fraction(
                int(formed(r).q().numerator()),
                int(formed(r).q().denominator()),
            )
        )
        for r in spanning
    ]
    return _ordered(block, tuple(model.RootSpan.model_fields)), spanning


def _root_sublattice(
    gram: GramTensor, spanning: Mapping[Vector, Fraction]
) -> dict[str, Yaml]:
    """The invariant factors of $R(L)$ in $L$, for roots that generate $R(L)$; for a root lattice, also a set $S$ with $L = \\mathbb{Z}\\Phi_S(L)$."""
    rank = len(gram)
    matrix = ZZ.matrix_space(len(spanning), rank).from_rows(tuple(spanning))
    factors = tuple(abs(int(factor)) for factor in matrix.invariant_factors())
    block: dict[str, Yaml] = {"invariant_factors": list(factors)}
    if factors == (1,) * rank:
        norms = sorted(set(spanning.values()), key=lambda norm: (abs(norm), norm))
        ambient = ZZ.free_module(rank)
        selected = next(
            subset
            for size in range(1, len(norms) + 1)
            for subset in combinations(norms, size)
            if all(
                ambient.module_generator(label)
                in ambient.subobject_on(
                    tuple(
                        ambient(root)
                        for root, norm in spanning.items()
                        if norm in subset
                    )
                )
                for label in ambient.module_generating_set()
            )
        )
        block["norms"] = [rational(norm) for norm in selected]
    return block


def derive(record: dict[str, Yaml]) -> dict[str, Yaml]:
    """Return the record with every field that the Gram tensor determines computed from it.

    The fields `rank`, `signature`, `determinant` and `definiteness`; the
    inverse Gram tensor `dual_gram_tensor` when the determinant is not zero; the
    blocks `integral`, `definite` and `indefinite`, each present exactly when
    its hypothesis holds; `root_span` when the record has none and the roots
    that `roots.small_roots` finds generate `L`, with the norms of its roots;
    and `root_sublattice` when the roots of `L` are stated.

    A field not computed here is preserved when already present. In particular,
    exact invariants whose computation may be expensive, such as
    `integral.overlattice_count`, are produced by enrichment rather than by
    ordinary record derivation.
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
        if all(QQ(value) in ZZ for row in gram for value in row)
        else None
    )
    match integral_lattice:
        case None:
            scale_generator = formed.scale_submodule().principal_generator()
            reflection_multiplier = ZZ(int(scale_generator.denominator()))
            reflection_lattice = Lattices(ZZ)(
                formed.twist(reflection_multiplier).gram_tensor().change_ring(ZZ)
            )
        case _:
            reflection_multiplier = ZZ.one()
            reflection_lattice = integral_lattice
    definiteness = model.definiteness(n_plus, n_minus, n_zero)
    dual: dict[str, Yaml] = {}
    if determinant != 0:
        inverse = fmpq_mat(
            [
                [fmpq(value.numerator, value.denominator) for value in row]
                for row in gram
            ]
        ).inv()
        dual = {
            "dual_gram_tensor": [
                [
                    rational(
                        Fraction(int(value.numerator), int(value.denominator))
                    )
                    for value in row
                ]
                for row in (
                    [inverse[i, j] for j in range(rank)] for i in range(rank)
                )
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
    for key in ("integral", "definite", "indefinite", "root_span", "root_sublattice"):
        derived.pop(key, None)
    if integral_lattice is not None:
        derived["integral"] = _integral(record, gram, integral_lattice)
    if definiteness in ("positive_definite", "negative_definite"):
        labels = tuple(reflection_lattice.module_generating_set())
        positive_roots = {}
        for root in reflection_lattice.reflective_roots():
            coordinates = root.to_vector()
            vector = tuple(int(coordinates(label)) for label in labels)
            if next(coefficient for coefficient in vector if coefficient) < 0:
                continue
            value = formed(vector).q()
            positive_roots[vector] = Fraction(
                int(value.numerator()), int(value.denominator())
            )
        derived["definite"] = _definite(
            record,
            gram,
            positive_roots,
            formed,
            reflection_lattice,
            Fraction(int(reflection_multiplier)),
            integral_lattice,
        )
        derived["root_sublattice"] = _root_sublattice(gram, positive_roots)
    else:
        found = _root_span(record, gram, formed, reflection_lattice)
        if found is not None:
            span, spanning = found
            derived["root_span"] = span
            derived["root_sublattice"] = _root_sublattice(
                gram,
                {
                    r: Fraction(
                        int(formed(r).q().numerator()),
                        int(formed(r).q().denominator()),
                    )
                    for r in spanning
                },
            )
    if definiteness == "indefinite":
        derived["indefinite"] = _indefinite(gram)
    return {key: derived[key] for key in KEYS if key in derived}


def derived_projection(record: Mapping[str, Yaml]) -> dict[str, Yaml]:
    """The part of a record whose value is computed by `derive`.

    Authored identity, bibliography, families, relations and expensive
    SageMath enrichment fields are excluded. This projection is what the
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
            ("minimum", "kissing_number", "theta_series", "root_system", "roots"),
        ),
        ("indefinite", ("isotropic",)),
    ):
        block = record.get(block_name)
        if isinstance(block, dict):
            projected[block_name] = {
                field: block[field] for field in fields if field in block
            }
    # For a definite lattice, `derive` computes the complete root system and
    # hence its root sublattice from the Gram tensor. For an indefinite
    # lattice, a `root_span` can instead be authored input to a partial root
    # search, so neither it nor the root sublattice obtained from it belongs
    # in the aggregate Gram-derived certificate.
    if isinstance(record.get("definite"), dict) and "root_sublattice" in record:
        projected["root_sublattice"] = record["root_sublattice"]
    return projected


def gram_problems(gram: GramTensor) -> list[str]:
    """The shape problems of a Gram tensor of a lattice card.

    Scaling is not an equivalence relation in the catalogue: $L$ and $L(n)$ are
    different bilinear lattices, including $n=-1$. This check therefore imposes
    no primitive-scale or sign normalization.
    """
    rank = len(gram)
    if any(len(row) != rank for row in gram):
        return [
            f"gram_tensor: a (0,2)-tensor on a module of rank {rank} has {rank} rows of {rank} components"
        ]
    if any(gram[i][j] != gram[j][i] for i in range(rank) for j in range(i)):
        return ["gram_tensor: b(e_i, e_j) differs from b(e_j, e_i) for some i, j"]
    return []


IsometryInvariants = tuple[
    int,
    Definiteness,
    Fraction,
    Fraction,
    int,
    tuple[AdeType, ...] | None,
    tuple[int, ...] | None,
    tuple[int, ...] | None,
]
"""Rank, definiteness, determinant, minimum, kissing number, root system, theta series and discriminant group of a definite record."""


def isometry_invariants(lattice: Lattice) -> IsometryInvariants:
    definite = lattice.definite
    assert definite is not None, "only a definite record is compared by isometry class"
    integral = lattice.integral
    discriminant_group = None if integral is None else integral.discriminant_group
    return (
        lattice.rank,
        lattice.definiteness,
        lattice.determinant,
        definite.minimum,
        definite.kissing_number,
        definite.root_system,
        definite.theta_series,
        discriminant_group,
    )


def local_admission_problems(lattice: Lattice) -> list[str]:
    """Admission problems whose truth depends only on one lattice record."""
    found = []
    gram = lattice.gram_tensor
    integral = lattice.integral
    definite = lattice.definite
    if integral is not None and lattice.determinant != 0:
        owned = Lattices(ZZ)(gram)
        if integral.level is not None and integral.level != int(owned.level()):
            found.append(
                "integral.level: the stated level does not equal the level of the dual quadratic form"
            )
        primes = tuple(int(prime) for prime in owned.bad_reduction_primes())
        if integral.bad_reduction_primes != primes:
            found.append(
                f"integral.bad_reduction_primes: stated {integral.bad_reduction_primes}, computed {primes}"
            )
        character = (
            int(owned.discriminant_character_discriminant())
            if lattice.rank % 2 == 0
            else None
        )
        if integral.quadratic_character != character:
            found.append(
                f"integral.quadratic_character: stated {integral.quadratic_character}, computed {character}"
            )
    if definite is not None and definite.perfect is not None and definite.minimal_vectors is not None:
        formed = ZZ.free_module(lattice.rank).equip_bilinear_form(QQ, gram)
        scale_generator = formed.scale_submodule().principal_generator()
        multiplier = ZZ(int(scale_generator.denominator()))
        owned = Lattices(ZZ)(formed.twist(multiplier).gram_tensor())
        if definite.perfect != owned.is_voronoi_perfect():
            found.append(
                "definite.perfect: minimal-vector tensors give a different perfectness value"
            )
    if (
        definite is not None
        and definite.automorphism_group_order is not None
        and (
            definite.automorphism_group_order <= 0
            or definite.automorphism_group_order % 2 == 1
        )
    ):
        found.append(
            "definite.automorphism_group_order: x -> -x is an isometry of order 2, so the order is even"
        )
    span = lattice.root_span
    if span is not None:
        formed = ZZ.free_module(lattice.rank).equip_bilinear_form(QQ, gram)
        scale_generator = formed.scale_submodule().principal_generator()
        multiplier = ZZ(int(scale_generator.denominator()))
        owned_lattice = Lattices(ZZ)(
            formed.twist(multiplier).gram_tensor().change_ring(ZZ)
        )
        found.extend(
            f"root_span.roots: {list(row)} is not a root of L"
            for row in span.roots
            if not owned_lattice(row).is_root()
        )
        if span.embedding is not None:
            ambient = ZZ.free_module(lattice.rank)
            embedding_elements = tuple(ambient(row) for row in span.embedding)
            root_elements = tuple(ambient(row) for row in span.roots)
            embedding_span = ambient.subobject_on(embedding_elements)
            root_span = ambient.subobject_on(root_elements)
            if (
                int(embedding_span.module_rank()) != len(span.embedding)
                or any(element not in root_span for element in embedding_elements)
                or any(element not in embedding_span for element in root_elements)
            ):
                found.append(
                    "root_span.embedding: the rows are not a basis of the sublattice that the rows of `roots` generate"
                )
    return found


def relational_admission_problems(
    lattice: Lattice,
    written: Mapping[str, Lattice],
    *,
    isometry_records: Mapping[str, Lattice] | None = None,
) -> list[str]:
    """Admission problems that compare one lattice with other lattice records."""
    found = []
    gram = lattice.gram_tensor
    definite = lattice.definite
    span = lattice.root_span
    if span is not None and span.embedding is not None and span.summands is not None:
        missing = [
            summand.tag for summand in span.summands if summand.tag not in written
        ]
        found.extend(
            f"root_span.summands: the tag {tag} is not in the corpus" for tag in missing
        )
        if not missing:
            if lattice.is_integer_valued and all(
                written[summand.tag].is_integer_valued for summand in span.summands
            ):
                # An empty sum is the rank-zero lattice, which the biproduct
                # constructor does not build: any embedding rows mismatch it.
                if not span.summands:
                    if span.embedding:
                        found.append(
                            "root_span.embedding: the rows do not have the Gram tensor of the orthogonal sum of the summands"
                        )
                else:
                    target_lattice = Lattices(ZZ)(gram)
                    summand_lattices = tuple(
                        Lattices(ZZ)(written[summand.tag].gram_tensor).twist(summand.scale)
                        for summand in span.summands
                    )
                    source_lattice = Lattices(ZZ).biproduct(summand_lattices)
                    try:
                        source_lattice.Mor(target_lattice)(
                            tuple(target_lattice(row) for row in span.embedding)
                        )
                    except ValueError:
                        found.append(
                            "root_span.embedding: the rows do not have the Gram tensor of the orthogonal sum of the summands"
                        )
            else:
                target_formed = ZZ.free_module(lattice.rank).equip_bilinear_form(QQ, gram)
                offset = 0
                image_blocks = []
                valid = True
                for summand in span.summands:
                    source_record = written[summand.tag]
                    source_formed = ZZ.free_module(source_record.rank).equip_bilinear_form(
                        QQ, source_record.gram_tensor
                    ).twist(summand.scale)
                    block_rows = span.embedding[offset : offset + source_record.rank]
                    block_images = tuple(target_formed(row) for row in block_rows)
                    offset += source_record.rank
                    try:
                        source_formed.Mor(target_formed)(block_images)
                    except ValueError:
                        valid = False
                    image_blocks.append(block_images)
                if offset != len(span.embedding):
                    valid = False
                if valid and any(
                    left.b(right) != 0
                    for left_index, left_block in enumerate(image_blocks)
                    for right_block in image_blocks[left_index + 1 :]
                    for left in left_block
                    for right in right_block
                ):
                    valid = False
                if not valid:
                    found.append(
                        "root_span.embedding: the rows do not have the Gram tensor of the orthogonal sum of the summands"
                    )
    if definite is not None:
        invariants = isometry_invariants(lattice)
        compared = written if isometry_records is None else isometry_records
        source_formed = ZZ.free_module(lattice.rank).equip_bilinear_form(QQ, gram)
        source_scale = source_formed.scale_submodule().principal_generator()
        source_multiplier = ZZ(int(source_scale.denominator()))
        source_owned = Lattices(ZZ)(
            source_formed.twist(source_multiplier).gram_tensor().change_ring(ZZ)
        )
        for other in compared.values():
            if (
                other.definite is None
                or isometry_invariants(other) != invariants
                or other.gram_tensor == gram
            ):
                continue
            other_formed = ZZ.free_module(other.rank).equip_bilinear_form(QQ, other.gram_tensor)
            other_scale = other_formed.scale_submodule().principal_generator()
            if source_scale != other_scale:
                continue
            other_multiplier = ZZ(int(other_scale.denominator()))
            other_owned = Lattices(ZZ)(
                other_formed.twist(other_multiplier).gram_tensor().change_ring(ZZ)
            )
            if source_owned.is_isometric(other_owned):
                found.append(
                    f"the lattice is isometric to {other.tag} ({other.name}), in another basis"
                )
    return found


def admission_problems(
    lattice: Lattice,
    written: Mapping[str, Lattice],
    *,
    isometry_records: Mapping[str, Lattice] | None = None,
) -> list[str]:
    """All local and relational admission problems of a lattice record."""
    return [
        *local_admission_problems(lattice),
        *relational_admission_problems(
            lattice, written, isometry_records=isometry_records
        ),
    ]


def _crosses_parts(gram: GramTensor, lines: tuple[int, ...]) -> bool:
    """Whether $b(e_i, e_j) \\neq 0$ for some $i$, $j$ in different parts of the indices that the lines cut."""
    bounds = (0, *lines, len(gram))
    part = [
        index
        for index, (low, high) in enumerate(zip(bounds, bounds[1:], strict=False))
        for _ in range(low, high)
    ]
    return any(
        gram[i][j] != 0
        for i in range(len(gram))
        for j in range(len(gram))
        if part[i] != part[j]
    )


def morphism_problems(
    morphism: Morphism, source: Lattice, target: Lattice
) -> list[str]:
    """The problems of a new morphism: a matrix whose shape is not (rank of the target) by (rank of the source),
    a matrix that does not preserve the forms, and a subdivision whose parts are not orthogonal summands."""
    if len(morphism.matrix) != target.rank or len(morphism.matrix[0]) != source.rank:
        return [
            f"{morphism.name}: the matrix has {target.rank} rows and {source.rank} columns, the ranks of the target and the source"
        ]
    found = []
    if source.is_integer_valued and target.is_integer_valued:
        source_lattice = Lattices(ZZ)(source.gram_tensor).twist(morphism.scale)
        target_lattice = Lattices(ZZ)(target.gram_tensor)
        try:
            source_lattice.Mor(target_lattice)(
                tuple(target_lattice(image) for image in morphism.images)
            )
        except ValueError:
            found.append(
                f"{morphism.name}: the matrix does not preserve the forms, since M^T G_target M is not {morphism.scale} G_source"
            )
    else:
        source_formed = ZZ.free_module(source.rank).equip_bilinear_form(QQ, source.gram_tensor).twist(morphism.scale)
        target_formed = ZZ.free_module(target.rank).equip_bilinear_form(QQ, target.gram_tensor)
        try:
            source_formed.Mor(target_formed)(
                tuple(target_formed(image) for image in morphism.images)
            )
        except ValueError:
            found.append(
                f"{morphism.name}: the matrix does not preserve the forms, since M^T G_target M is not {morphism.scale} G_source"
            )
    if _crosses_parts(target.gram_tensor, morphism.row_subdivisions):
        found.append(
            f"{morphism.name}: the parts of row_subdivisions are not orthogonal summands of the target"
        )
    if _crosses_parts(source.gram_tensor, morphism.column_subdivisions):
        found.append(
            f"{morphism.name}: the parts of column_subdivisions are not orthogonal summands of the source"
        )
    return found
