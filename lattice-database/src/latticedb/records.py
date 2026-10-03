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

`record_text` writes a record in the layout of the corpus, and
`morphisms_text` writes a morphism file.
"""

from collections.abc import Mapping
from fractions import Fraction

import yaml

from latticedb import arithmetic, model, roots
from latticedb.arithmetic import GramTensor, Vector
from latticedb.model import AdeType, Definiteness, Lattice, Morphism, Yaml

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
    "root_sublattice",
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
    """The prose after the front matter, in the form the Markdown formatter flowmark keeps.

    That is two blank lines when there is no prose, else a blank line and the prose.
    """
    return "\n" + prose + "\n" if prose else "\n\n"


MORPHISM_KEYS = ("name", "description", "matrix", "scale", "row_subdivisions", "column_subdivisions")
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


def _integral(record: dict[str, Yaml], gram: GramTensor) -> dict[str, Yaml]:
    rank = len(gram)
    declared = _block(record, "integral")
    block: dict[str, Yaml] = {"parity": "even" if all(gram[i][i] % 2 == 0 for i in range(rank)) else "odd"}
    if arithmetic.determinant(gram) != 0:
        invariants = arithmetic.discriminant_invariants(gram)
        block["discriminant_group"] = list(invariants)
        count = arithmetic.overlattice_count(gram)
        if count is not None:
            block["overlattice_count"] = count
        if block["parity"] == "even" and all(factor == 2 for factor in invariants):
            block["delta"] = arithmetic.delta(gram)
        determinant = int(arithmetic.determinant(gram))
        block["bad_reduction_primes"] = list(arithmetic.bad_reduction_primes(determinant))
        if rank % 2 == 0:
            block["quadratic_character"] = arithmetic.quadratic_character(rank, determinant)
        for field in ("genus_symbol", "genus_class_count", "spinor_genus_count", "spinor_genera", "hyperbolic_index", "primitive_orbits"):
            if field in declared:
                block[field] = declared[field]
    return _ordered(block, tuple(model.IntegralData.model_fields))


def _definite(record: dict[str, Yaml], gram: GramTensor, positive_roots: Mapping[Vector, Fraction]) -> dict[str, Yaml]:
    declared = _block(record, "definite")
    minimum, kissing_number = arithmetic.minimum_and_kissing_number(gram)
    block: dict[str, Yaml] = {"minimum": rational(minimum), "kissing_number": kissing_number}
    if "automorphism_group_order" in declared:
        block["automorphism_group_order"] = declared["automorphism_group_order"]
    if arithmetic.is_integer_valued(gram):
        bound = model.theta_bound(len(gram), minimum)
        match declared.get("theta_series"):
            case list() as stated:
                bound = max(bound, len(stated) - 1)
        block["theta_series"] = list(arithmetic.theta_coefficients(gram, bound))
        block["root_system"] = list(roots.norm_two_types(gram, dict(positive_roots)))
    block["roots"] = [{"type": root_type, "scale": rational(scale), "simple_roots": [list(r) for r in simple]} for root_type, scale, simple in roots.root_system(gram)]
    return _ordered(block, tuple(model.DefiniteData.model_fields))


def _indefinite(gram: GramTensor) -> dict[str, Yaml]:
    # The radical of a degenerate form is nonzero and isotropic; `qfsolve` decides a nondegenerate rational form.
    isotropic = arithmetic.determinant(gram) == 0 or arithmetic.is_isotropic(gram)
    return {"isotropic": isotropic}


def _root_span(record: dict[str, Yaml], gram: GramTensor) -> tuple[dict[str, Yaml], list[Vector]] | None:
    """The declared `root_span` block, else the roots found when they generate `L`, with the norms of the roots; else `None`."""
    if "root_span" in record:
        block = dict(_block(record, "root_span"))
        spanning = _vectors(block["roots"])
    else:
        rank = len(gram)
        found: list[Vector] = roots.small_roots(gram)
        if not arithmetic.generate(found, rank):
            return None
        spanning = list(roots.generating_roots(found, rank))
        block = {"roots": [list(r) for r in spanning]}
    block["norms"] = [rational(arithmetic.pairing(gram, r, r)) for r in spanning]
    return _ordered(block, tuple(model.RootSpan.model_fields)), spanning


def _root_sublattice(gram: GramTensor, spanning: Mapping[Vector, Fraction]) -> dict[str, Yaml]:
    """The invariant factors of $R(L)$ in $L$, for roots that generate $R(L)$; for a root lattice, also a set $S$ with $L = \\mathbb{Z}\\Phi_S(L)$."""
    rank = len(gram)
    factors = arithmetic.invariant_factors(list(spanning), rank)
    block: dict[str, Yaml] = {"invariant_factors": list(factors)}
    if factors == (1,) * rank:
        block["norms"] = [rational(norm) for norm in arithmetic.generating_norms(dict(spanning), rank)]
    return block


def derive(record: dict[str, Yaml]) -> dict[str, Yaml]:
    """Return the record with every field that the Gram tensor determines computed from it.

    The fields `rank`, `signature`, `determinant` and `definiteness`; the
    blocks `integral`, `definite` and `indefinite`, each present exactly when
    its hypothesis holds; `root_span` when the record has none and the roots
    that `roots.small_roots` finds generate `L`, with the norms of its roots;
    and `root_sublattice` when the roots of `L` are stated.
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
    for key in ("integral", "definite", "indefinite", "root_span", "root_sublattice"):
        derived.pop(key, None)
    if arithmetic.is_integer_valued(gram):
        derived["integral"] = _integral(record, gram)
    if definiteness in ("positive_definite", "negative_definite"):
        positive_roots = arithmetic.definite_roots(gram)
        derived["definite"] = _definite(record, gram, positive_roots)
        derived["root_sublattice"] = _root_sublattice(gram, positive_roots)
    else:
        found = _root_span(record, gram)
        if found is not None:
            span, spanning = found
            derived["root_span"] = span
            derived["root_sublattice"] = _root_sublattice(gram, {r: arithmetic.pairing(gram, r, r) for r in spanning})
    if definiteness == "indefinite":
        derived["indefinite"] = _indefinite(gram)
    return {key: derived[key] for key in KEYS if key in derived}


TWIST_FAMILY = "nikulin-two-elementary"
"""The family whose twists $M(2)$ are records: the 13 rows $a = r$ of Nikulin's Table 1 are lattices $M(2)$, and the classification names them, not $M$."""


def gram_problems(gram: GramTensor, families: tuple[str, ...]) -> list[str]:
    """The problems of the Gram tensor of a new record: it is not symmetric, or it is a twist that the corpus does not record.

    The corpus records one lattice of each class under scaling $L \\mapsto L(n)$, $n$ a nonzero integer.
    $L$ is admitted when it is not $M(n)$ for a lattice $M$ and an integer $n$ with $|n| \\geq 2$,
    that is, when the scale of $b$ has numerator 1, and when its sign is the conventional one:
    $b$ is positive when it takes one sign, and $n_+ \\leq n_-$ when it takes both.
    The one exception is a twist $M(2)$ in the family `TWIST_FAMILY`.
    The zero form is $M(0)$ for every $M$ and is not admitted.
    """
    rank = len(gram)
    if any(len(row) != rank for row in gram):
        return [f"gram_tensor: a (0,2)-tensor on a module of rank {rank} has {rank} rows of {rank} components"]
    if any(gram[i][j] != gram[j][i] for i in range(rank) for j in range(i)):
        return ["gram_tensor: b(e_i, e_j) differs from b(e_j, e_i) for some i, j"]
    scale = arithmetic.scale(gram)
    if scale == 0:
        return [f"gram_tensor: b = 0 is M(0) for every lattice M of rank {rank}; the corpus records no zero form"]
    found = []
    if scale.numerator != 1 and not (scale.numerator == 2 and TWIST_FAMILY in families):
        found.append(f"gram_tensor: the lattice is M({scale.numerator}) for the lattice M with Gram tensor b/{scale.numerator}; the corpus records M and not its twist")
    n_plus, n_minus, _ = arithmetic.inertia(gram)
    if (n_plus == 0 and n_minus > 0) or (n_plus > n_minus > 0):
        found.append(
            f"gram_tensor: the lattice is M(-1) for the lattice M with Gram tensor -b and signature ({n_minus}, {n_plus}); "
            "the corpus records M: positive when b has one sign, n_plus <= n_minus when it has both"
        )
    return found


IsometryInvariants = tuple[int, Definiteness, Fraction, Fraction, int, tuple[AdeType, ...] | None, tuple[int, ...] | None, tuple[int, ...] | None]
"""Rank, definiteness, determinant, minimum, kissing number, root system, theta series and discriminant group of a definite record."""


def isometry_invariants(lattice: Lattice) -> IsometryInvariants:
    definite = lattice.definite
    assert definite is not None, "only a definite record is compared by isometry class"
    integral = lattice.integral
    discriminant_group = None if integral is None else integral.discriminant_group
    return (lattice.rank, lattice.definiteness, lattice.determinant, definite.minimum, definite.kissing_number, definite.root_system, definite.theta_series, discriminant_group)


def admission_problems(lattice: Lattice, written: Mapping[str, Lattice]) -> list[str]:
    """The problems of a new record against its declared values and the records already written.

    A declared order of $O(L)$ that is not even and positive; a row of `root_span.roots` that is not a root;
    rows of `root_span.embedding` that are not a basis of the sublattice the roots generate, or that do not have
    the Gram tensor of the orthogonal sum of the summands; and a written definite record isometric to the new one,
    decided by `qfisom` when the stated invariants agree. Whether two indefinite lattices are isometric is not decided.
    """
    found = []
    gram = lattice.gram_tensor
    definite = lattice.definite
    if definite is not None and definite.automorphism_group_order is not None and (definite.automorphism_group_order <= 0 or definite.automorphism_group_order % 2 == 1):
        found.append("definite.automorphism_group_order: x -> -x is an isometry of order 2, so the order is even")
    span = lattice.root_span
    if span is not None:
        found.extend(f"root_span.roots: {list(row)} is not a root of L" for row in span.roots if not arithmetic.is_root(gram, row))
        if span.embedding is not None and span.summands is not None:
            basis = arithmetic.span_basis(list(span.embedding))
            if len(basis) != len(span.embedding) or basis != arithmetic.span_basis(list(span.roots)):
                found.append("root_span.embedding: the rows are not a basis of the sublattice that the rows of `roots` generate")
            missing = [summand.tag for summand in span.summands if summand.tag not in written]
            found.extend(f"root_span.summands: the tag {tag} is not in the corpus" for tag in missing)
            summands = tuple(arithmetic.scaled(written[summand.tag].gram_tensor, summand.scale) for summand in span.summands if summand.tag in written)
            if not missing and arithmetic.restriction(gram, span.embedding) != arithmetic.orthogonal_sum(summands):
                found.append("root_span.embedding: the rows do not have the Gram tensor of the orthogonal sum of the summands")
    if definite is not None:
        invariants = isometry_invariants(lattice)
        found.extend(
            f"the lattice is isometric to {other.tag} ({other.name}), in another basis"
            for other in written.values()
            if other.definite is not None and isometry_invariants(other) == invariants and other.gram_tensor != gram and arithmetic.is_isometric(other.gram_tensor, gram)
        )
    return found


def _crosses_parts(gram: GramTensor, lines: tuple[int, ...]) -> bool:
    """Whether $b(e_i, e_j) \\neq 0$ for some $i$, $j$ in different parts of the indices that the lines cut."""
    bounds = (0, *lines, len(gram))
    part = [index for index, (low, high) in enumerate(zip(bounds, bounds[1:], strict=False)) for _ in range(low, high)]
    return any(gram[i][j] != 0 for i in range(len(gram)) for j in range(len(gram)) if part[i] != part[j])


def morphism_problems(morphism: Morphism, source: Lattice, target: Lattice) -> list[str]:
    """The problems of a new morphism: a matrix whose shape is not (rank of the target) by (rank of the source),
    a matrix that does not preserve the forms, and a subdivision whose parts are not orthogonal summands."""
    if len(morphism.matrix) != target.rank or len(morphism.matrix[0]) != source.rank:
        return [f"{morphism.name}: the matrix has {target.rank} rows and {source.rank} columns, the ranks of the target and the source"]
    found = []
    if arithmetic.restriction(target.gram_tensor, morphism.images) != arithmetic.scaled(source.gram_tensor, morphism.scale):
        found.append(f"{morphism.name}: the matrix does not preserve the forms, since M^T G_target M is not {morphism.scale} G_source")
    if _crosses_parts(target.gram_tensor, morphism.row_subdivisions):
        found.append(f"{morphism.name}: the parts of row_subdivisions are not orthogonal summands of the target")
    if _crosses_parts(source.gram_tensor, morphism.column_subdivisions):
        found.append(f"{morphism.name}: the parts of column_subdivisions are not orthogonal summands of the source")
    return found
