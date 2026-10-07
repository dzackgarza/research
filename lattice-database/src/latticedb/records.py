"""Card serialization and orchestration of preamble-owned lattice operations.

`derive` constructs the corresponding preamble formed/lattice objects, calls
their public operations, and serializes returned values while preserving other
stored fields. It contains no independent lattice algorithm.

`record_text` writes a lattice card, including the morphisms whose domain is that card.
"""

from collections.abc import Mapping, Sequence
from fractions import Fraction
from itertools import combinations
import yaml

from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.sets.finite_families import finite_family
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


def _fraction_of(value) -> Fraction:
    """A rational value of the preamble, as the `Fraction` a card stores."""
    return Fraction(int(value.numerator()), int(value.denominator()))


def _integral_twist(formed):
    """The twist `L(m)` of `formed` by the denominator `m` of its scale, as a ZZ-lattice, and `m`.

    `formed` is a finite free ZZ-module with a QQ-valued bilinear form.  Its twist by
    the denominator of its scale is integral, and a twist does not change which
    vectors define reflections; card fields stated in the original scale divide by `m`.
    """
    multiplier = ZZ(int(formed.scale_submodule().principal_generator().denominator()))
    gram = formed.twist(multiplier).gram_tensor().change_ring(ZZ)
    return Lattices(ZZ)(gram), int(multiplier)


def _theta_series_prefix(lattice, minimum: Fraction, existing_length: int) -> tuple[int, ...]:
    """The coefficients of the theta series that a card stores.

    The card stores the coefficients up to 12 in rank at most 4, 8 in rank at most 8,
    6 in rank at most 12 and 4 above, never fewer than the minimum asks for and never
    fewer than a prefix already stored on the card.
    """
    rank = int(lattice.module_rank())
    match rank:
        case _ if rank <= 4:
            default = 12
        case _ if rank <= 8:
            default = 8
        case _ if rank <= 12:
            default = 6
        case _:
            default = 4
    bound = max(int(minimum), default, max(0, existing_length - 1))
    series = lattice.theta_series(precision=bound + 1)
    return tuple(int(series[index]) for index in range(bound + 1))


def _norm_two_root_types(lattice) -> tuple[str, ...]:
    """The ADE types of the roots of square 2 (square -2 when negative definite), as `E8`, `A2`.

    The preamble recognizes the type on the root sublattice of the negative-definite
    model; the card lists the irreducible components by decreasing rank.
    """
    negative = lattice if lattice.is_negative_definite() else lattice.twist(-1)
    root_sublattice = negative.root_sublattice()
    if root_sublattice.module_rank() == 0:
        return ()
    components = root_sublattice.dynkin_diagram().connected_components()
    ranked = sorted(
        (-int(component.cardinality()), component.label()) for component in components
    )
    return tuple(name for _rank, name in ranked)


def _smith_factors(rows: tuple[tuple[int, ...], ...], rank: int) -> tuple[int, ...]:
    """The nonzero invariant factors of the integer matrix with these rows."""
    if not rows:
        return ()
    matrix = ZZ.matrix_space(len(rows), rank).from_rows(rows)
    return tuple(abs(int(factor)) for factor in matrix.invariant_factors())


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
        if lattice.is_even() and lattice.is_p_elementary(2):
            block["delta"] = int(lattice.delta())
        block["bad_reduction_primes"] = [
            int(prime) for prime in lattice.bad_reduction_primes()
        ]
        if rank % 2 == 0:
            block["quadratic_character"] = int(
                lattice.discriminant_character_discriminant()
            )
        if lattice.is_even():
            block["level"] = int(lattice.level())
        # Other stored invariants are preserved; their computation has separate preamble owners.
        for field in model.IntegralData.model_fields:
            if field not in block and field in declared:
                block[field] = declared[field]
    return _ordered(block, tuple(model.IntegralData.model_fields))


def _root_component(
    lattice, component, rescaling: Fraction
) -> tuple[str, Fraction, tuple[tuple[int, ...], ...]]:
    """Serialize one root-system component: its type, signed scale and ordered simple roots.

    The simple roots are listed in the vertex order of the diagram of the component's
    type, in the coordinates of the lattice's module generators.  The card names the
    rank-two type B2, where the preamble's diagram of that type is C2.
    """
    isomorphism_from_type_diagram = component.isomorphism_from_type_diagram()
    labels = tuple(lattice.module_generating_set())
    roots = tuple(
        tuple(
            int(component.root(isomorphism_from_type_diagram(vertex)).to_vector()(label))
            for label in labels
        )
        for vertex in isomorphism_from_type_diagram.domain().vertices()
    )
    scale = component.root_scale()
    root_type = "B2" if component.label() == "C2" else component.label()
    return (
        root_type,
        Fraction(int(scale.numerator()), int(scale.denominator())) / rescaling,
        roots,
    )


def _definite(
    record: dict[str, Yaml],
    gram: GramTensor,
    formed,
    computation_lattice,
    rescaling: Fraction,
    integral_lattice=None,
) -> dict[str, Yaml]:
    declared = _block(record, "definite")
    labels = tuple(computation_lattice.module_generating_set())
    minimum_value = computation_lattice.minimum()
    minimum = Fraction(
        int(abs(minimum_value.numerator())),
        int(minimum_value.denominator()),
    ) / rescaling
    block: dict[str, Yaml] = {
        "minimum": rational(minimum),
        "kissing_number": int(computation_lattice.kissing_number()),
        # A twist L(m) has the vectors of L and rescales the form, so it keeps the minimal shell and perfection.
        "minimal_vectors": sorted(
            [int(vector.to_vector()(label)) for label in labels]
            for vector in computation_lattice.shortest_vectors()
        ),
        "perfect": bool(computation_lattice.is_voronoi_perfect()),
    }
    if integral_lattice is not None:
        stored_theta = declared.get("theta_series")
        existing_length = len(stored_theta) if isinstance(stored_theta, list) else 0
        block["theta_series"] = list(
            _theta_series_prefix(integral_lattice, minimum, existing_length)
        )
        block["root_system"] = list(_norm_two_root_types(integral_lattice))
    block["roots"] = [
        {"type": root_type, "scale": rational(scale), "simple_roots": [list(root) for root in roots]}
        for root_type, scale, roots in sorted(
            (
                _root_component(computation_lattice, component, rescaling)
                for component in computation_lattice.reflective_root_system_components()
            ),
            key=lambda entry: (-len(entry[2]), entry[0], entry[2]),
        )
    ]
    for field in model.DefiniteData.model_fields:
        if field not in block and field in declared:
            block[field] = declared[field]
    return _ordered(block, tuple(model.DefiniteData.model_fields))


def _root_span(
    record: dict[str, Yaml], formed
) -> tuple[dict[str, Yaml], tuple[tuple[int, ...], ...]] | None:
    """Serialize the authored roots spanning the root sublattice, with their norms."""
    match record.get("root_span"):
        case dict() as authored:
            block = dict(authored)
            roots = tuple(tuple(int(entry) for entry in row) for row in block["roots"])
        case _:
            return None
    block["norms"] = [rational(_fraction_of(formed(root).q())) for root in roots]
    return _ordered(block, tuple(model.RootSpan.model_fields)), roots


def _root_sublattice(formed, roots) -> dict[str, Yaml]:
    """Serialize the invariant factors of the root rows and, when the roots span, the norms that suffice.

    The stored norms are the fewest distinct root norms, smallest first, whose roots
    alone still span the lattice.
    """
    rank = int(formed.module_rank())
    norm_of = {root: _fraction_of(formed(root).q()) for root in roots}
    factors = _smith_factors(roots, rank)
    block: dict[str, Yaml] = {"invariant_factors": list(factors)}
    unimodular_span = (1,) * rank
    if factors != unimodular_span:
        return block
    norms = sorted(set(norm_of.values()), key=lambda norm: (abs(norm), norm))
    selected = next(
        subset
        for size in range(1, len(norms) + 1)
        for subset in combinations(norms, size)
        if _smith_factors(tuple(root for root in roots if norm_of[root] in subset), rank)
        == unimodular_span
    )
    block["norms"] = [rational(norm) for norm in selected]
    return block


def _indefinite(gram: GramTensor) -> dict[str, Yaml]:
    return {"isotropic": Lattices(QQ)(gram).is_isotropic()}


def derive(record: dict[str, Yaml]) -> dict[str, Yaml]:
    """Return the card with selected fields supplied by preamble-owned operations.

    The adapter serializes rank, signature, determinant, definiteness, the dual
    Gram tensor, selected integral invariants including the level of an even
    lattice, the definite minimum, kissing number, minimal shell and Voronoi
    perfection, indefinite isotropy, theta prefixes and root-system/root-sublattice data from
    preamble objects.

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
    match integral_lattice:
        case None:
            integral_twist, twist_multiplier = _integral_twist(formed)
        case _:
            integral_twist, twist_multiplier = integral_lattice, 1
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
    for key in ("integral", "definite", "indefinite", "root_span", "root_sublattice"):
        derived.pop(key, None)
    if integral_lattice is not None:
        derived["integral"] = _integral(record, gram, integral_lattice)
    if definiteness in ("positive_definite", "negative_definite"):
        derived["definite"] = _definite(
            record,
            gram,
            formed,
            integral_twist,
            Fraction(twist_multiplier),
            integral_lattice,
        )
        labels = tuple(integral_twist.module_generating_set())
        reflective_roots = tuple(
            tuple(int(root.to_vector()(label)) for label in labels)
            for root in integral_twist.reflective_roots()
        )
        derived["root_sublattice"] = _root_sublattice(formed, reflective_roots)
    else:
        found = _root_span(record, formed)
        if found is not None:
            span, spanning = found
            derived["root_span"] = span
            derived["root_sublattice"] = _root_sublattice(formed, spanning)
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
                "level",
            ),
        ),
        (
            "definite",
            (
                "minimum",
                "kissing_number",
                "minimal_vectors",
                "perfect",
                "theta_series",
                "root_system",
                "roots",
            ),
        ),
        ("indefinite", ("isotropic",)),
    ):
        block = record.get(block_name)
        if isinstance(block, dict):
            projected[block_name] = {
                field: block[field] for field in fields if field in block
            }
    if isinstance(record.get("definite"), dict) and "root_sublattice" in record:
        projected["root_sublattice"] = record["root_sublattice"]
    return projected


def gram_problems(gram: GramTensor) -> list[str]:
    """Structural problems of a Gram tensor stored on a lattice card."""
    rank = len(gram)
    if any(len(row) != rank for row in gram):
        return [
            f"gram_tensor: a (0,2)-tensor on a module of rank {rank} has {rank} rows of {rank} components"
        ]
    if any(gram[i][j] != gram[j][i] for i in range(rank) for j in range(i)):
        return ["gram_tensor: b(e_i, e_j) differs from b(e_j, e_i) for some i, j"]
    return []


def _generator_blocks(formed, lines):
    """The module generators of `formed`, cut into consecutive blocks at the card's subdivision lines."""
    bounds = (0, *lines, int(formed.module_rank()))
    labels = tuple(formed.module_generating_set())
    return tuple(
        tuple(formed.module_generator(label) for label in labels[low:high])
        for low, high in zip(bounds, bounds[1:], strict=False)
    )


def _mutually_orthogonal(blocks) -> bool:
    """Whether every element of each block is orthogonal to every element of every later block."""
    return all(
        left.is_orthogonal_to(right)
        for index, block in enumerate(blocks)
        for later in blocks[index + 1 :]
        for left in block
        for right in later
    )


def _preserves_forms(source, target, images) -> bool:
    """Whether the module map `source -> target` with these generator images preserves the forms."""
    module_map = source.module_category().Mor(source, target)(images)
    return source.Mor(target).preserves_forms(module_map)


def local_admission_problems(lattice: Lattice) -> list[str]:
    """Mathematical problems of one card, decided by preamble-owned operations."""
    if lattice.rank is None or lattice.gram_tensor is None:
        return []
    found: list[str] = []
    gram = lattice.gram_tensor
    formed = ZZ.free_module(lattice.rank).equip_bilinear_form(QQ, gram)
    integral = lattice.integral
    if integral is not None:
        if not formed.is_base_ring_valued():
            found.append(
                "integral: the stored integral block requires the form to take values in ZZ"
            )
        else:
            owned = Lattices(ZZ)(gram)
            if owned.determinant() != 0:
                if integral.level is not None and integral.level != int(owned.level()):
                    found.append(
                        "integral.level: the stated level does not equal the preamble-computed level"
                    )
                if integral.bad_reduction_primes is not None:
                    primes = tuple(int(prime) for prime in owned.bad_reduction_primes())
                    if tuple(integral.bad_reduction_primes) != primes:
                        found.append(
                            f"integral.bad_reduction_primes: stated {integral.bad_reduction_primes}, computed {primes}"
                        )
                if integral.quadratic_character is not None:
                    character = (
                        int(owned.discriminant_character_discriminant())
                        if lattice.rank % 2 == 0
                        else None
                    )
                    if integral.quadratic_character != character:
                        found.append(
                            f"integral.quadratic_character: stated {integral.quadratic_character}, computed {character}"
                        )
                if integral.discriminant_group is not None:
                    factors = tuple(
                        abs(int(factor))
                        for factor in owned.discriminant_group().invariant_factors()
                        if abs(int(factor)) > 1
                    )
                    if tuple(integral.discriminant_group) != factors:
                        found.append(
                            f"integral.discriminant_group: stated {integral.discriminant_group}, computed {factors}"
                        )
                if integral.delta is not None:
                    if not (owned.is_even() and owned.is_p_elementary(2)):
                        found.append(
                            "integral.delta: delta is defined only for an even 2-elementary lattice"
                        )
                    elif integral.delta != int(owned.delta()):
                        found.append(
                            f"integral.delta: stated {integral.delta}, computed {int(owned.delta())}"
                        )
    definite = lattice.definite
    if definite is not None:
        if formed.definiteness() not in ("positive_definite", "negative_definite"):
            found.append("definite: the stored definite block requires a definite form")
        if definite.perfect is not None:
            integral_twist, _multiplier = _integral_twist(formed)
            if definite.perfect != integral_twist.is_voronoi_perfect():
                found.append(
                    "definite.perfect: the stated value differs from L.is_voronoi_perfect()"
                )
        if (
            definite.automorphism_group_order is not None
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
        integral_twist, _multiplier = _integral_twist(formed)
        found.extend(
            f"root_span.roots: {list(row)} is not a root of L"
            for row in span.roots
            if not integral_twist(row).is_root()
        )
        if span.embedding is not None:
            ambient = ZZ.free_module(lattice.rank)
            embedding_span = ambient.subobject_on(
                tuple(ambient(row) for row in span.embedding)
            )
            root_span = ambient.subobject_on(tuple(ambient(row) for row in span.roots))
            if (
                int(embedding_span.module_rank()) != len(span.embedding)
                or any(ambient(row) not in root_span for row in span.embedding)
                or any(ambient(row) not in embedding_span for row in span.roots)
            ):
                found.append(
                    "root_span.embedding: the rows are not a basis of the sublattice generated by root_span.roots"
                )
    return found


def relational_admission_problems(
    lattice: Lattice, written: Mapping[str, Lattice]
) -> list[str]:
    """Mathematical problems relating one card to other cards, via preamble objects."""
    if lattice.rank is None or lattice.gram_tensor is None:
        return []
    found: list[str] = []
    span = lattice.root_span
    if span is not None and span.embedding is not None and span.summands is not None:
        missing = [summand.tag for summand in span.summands if summand.tag not in written]
        found.extend(
            f"root_span.summands: the tag {tag} is not in the corpus" for tag in missing
        )
        if not missing and span.summands:
            target = ZZ.free_module(lattice.rank).equip_bilinear_form(QQ, lattice.gram_tensor)
            offset = 0
            blocks = []
            valid = True
            for summand in span.summands:
                source_record = written[summand.tag]
                if source_record.rank is None or source_record.gram_tensor is None:
                    valid = False
                    break
                if offset + source_record.rank > len(span.embedding):
                    valid = False
                    break
                source = ZZ.free_module(source_record.rank).equip_bilinear_form(
                    QQ, source_record.gram_tensor
                ).twist(summand.scale)
                rows = span.embedding[offset : offset + source_record.rank]
                images = tuple(target(row) for row in rows)
                offset += source_record.rank
                if not _preserves_forms(source, target, images):
                    valid = False
                blocks.append(images)
            if offset != len(span.embedding):
                valid = False
            if valid and not _mutually_orthogonal(blocks):
                valid = False
            if not valid:
                found.append(
                    "root_span.embedding: the rows do not realize the stated orthogonal sum"
                )
    return found


def admission_problems(lattice: Lattice, written: Mapping[str, Lattice]) -> list[str]:
    """All preamble-backed admission problems of one lattice card."""
    return [
        *local_admission_problems(lattice),
        *relational_admission_problems(lattice, written),
    ]


def definite_isometry_problems(lattices: Sequence[Lattice]) -> dict[str, list[str]]:
    """The definite cards isometric to another card in another basis, by tag.

    A card's form `L` is isometric to another's `L'` exactly when the denominators
    `m` of their scales agree and the integral twists `L(m)`, `L'(m)` are isometric.
    The preamble partitions the twists into isometry classes in one call; each class
    is then split by `m`, and every card after the first of a part is reported against
    that first card. A card whose Gram tensor equals that of the first card is reported
    by the check of repeated Gram tensors instead.
    """
    definite = tuple(
        lattice
        for lattice in lattices
        if lattice.definite is not None
        and lattice.rank is not None
        and lattice.gram_tensor is not None
    )
    models = tuple(
        _integral_twist(
            ZZ.free_module(lattice.rank).equip_bilinear_form(QQ, lattice.gram_tensor)
        )
        for lattice in definite
    )
    classes = Lattices(ZZ).isometry_classes(
        finite_family(tuple(model for model, _multiplier in models))
    )
    found: dict[str, list[str]] = {}
    for block in classes:
        first_of_multiplier: dict[int, Lattice] = {}
        for index in block:
            lattice = definite[int(index)]
            first = first_of_multiplier.setdefault(models[int(index)][1], lattice)
            if first is lattice or first.gram_tensor == lattice.gram_tensor:
                continue
            found.setdefault(lattice.tag, []).append(
                f"the lattice is isometric to {first.tag} ({first.name}), in another basis"
            )
    return found


def morphism_problems(morphism, source: Lattice, target: Lattice) -> list[str]:
    """Mathematical problems of a stored lattice morphism, delegated to preamble Mor."""
    if (
        source.rank is None
        or source.gram_tensor is None
        or target.rank is None
        or target.gram_tensor is None
    ):
        return []
    if len(morphism.matrix) != target.rank or len(morphism.matrix[0]) != source.rank:
        return [
            f"{morphism.name}: the matrix must have {target.rank} rows and {source.rank} columns"
        ]
    source_formed = ZZ.free_module(source.rank).equip_bilinear_form(
        QQ, source.gram_tensor
    ).twist(morphism.scale)
    target_formed = ZZ.free_module(target.rank).equip_bilinear_form(
        QQ, target.gram_tensor
    )
    found: list[str] = []
    if not _preserves_forms(
        source_formed,
        target_formed,
        tuple(target_formed(image) for image in morphism.images),
    ):
        found.append(
            f"{morphism.name}: the matrix does not define the stated form-preserving morphism"
        )
    if not _mutually_orthogonal(_generator_blocks(target_formed, morphism.row_subdivisions)):
        found.append(
            f"{morphism.name}: row_subdivisions do not cut orthogonal summands of the target"
        )
    if not _mutually_orthogonal(
        _generator_blocks(source_formed, morphism.column_subdivisions)
    ):
        found.append(
            f"{morphism.name}: column_subdivisions do not cut orthogonal summands of the source"
        )
    return found
