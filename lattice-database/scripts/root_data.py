"""Write the root data of each record of `lattices/`.

A root of a lattice `L` is a primitive `r` with `b(r, r) != 0` such that the
reflection `s_r` is in `O(L)`; `Phi(L)` is the set of roots.

Definite record: the script writes `definite.roots`, the root system `Phi(L)`
as its irreducible components, each with its type and a base. `Phi(L)` is
finite, and `latticedb.arithmetic.definite_roots` lists it.

Other record without a `root_span` block: the script searches the vectors with
coordinates in `{-1, 0, 1}` and at most three nonzero coordinates for roots.
When the roots found generate `L`, it writes them as `root_span.roots`: a basis
of `L` that consists of roots when the search gives one, and otherwise a list
of roots that generate `L`. When they do not generate `L`, the script writes
nothing: `Z Phi(L)` is then not decided, and a proof by hand gives the block.

The model checks each block that the script writes, so a wrong result of this
script is a validation error and not a wrong record.
"""

from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

import frontmatter
import yaml

from latticedb import arithmetic, corpus, root_systems
from latticedb.arithmetic import GramTensor, Vector
from latticedb.model import Yaml

CORPUS = Path("lattices")
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
    "provenance",
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
    return "---\n" + yaml.dump(ordered, sort_keys=False, allow_unicode=True, width=100000) + "---\n\n" + prose + "\n"


def rational(value: Fraction) -> int | str:
    return int(value) if value.denominator == 1 else str(value)


def simple_roots(positive: list[Vector]) -> list[Vector]:
    """Return the base of the positive system `positive` of a reduced root system.

    `positive` holds, of each pair `r`, `-r`, the root whose first nonzero
    coordinate is positive. That is the positive system of the lexicographic
    order on the coordinates, a total order that addition respects. Its base is
    the set of positive roots that are not a sum of two positive roots.
    """
    sums = {tuple(a + b for a, b in zip(r, s, strict=True)) for r, s in combinations(positive, 2)}
    return [r for r in positive if r not in sums]


def irreducible_components(gram_tensor: GramTensor, base: list[Vector]) -> list[list[Vector]]:
    """Return the classes of the base under the relation that `b(r, s) != 0` generates."""
    components: list[list[Vector]] = []
    for r in base:
        linked = [component for component in components if any(arithmetic.pairing(gram_tensor, r, s) != 0 for s in component)]
        components = [component for component in components if component not in linked]
        components.append([*(s for component in linked for s in component), r])
    return components


def _numbering(gram: tuple[tuple[Fraction, ...], ...], expected: tuple[tuple[int, ...], ...], chosen: tuple[int, ...]) -> tuple[int, ...] | None:
    """Return an order `p` of the indices with `gram[p[i]][p[j]] == expected[i][j]`, that starts with `chosen`; `None` when there is none."""
    position = len(chosen)
    if position == len(expected):
        return chosen
    for index in range(len(expected)):
        if index in chosen or gram[index][index] != expected[position][position]:
            continue
        if all(gram[index][chosen[other]] == expected[position][other] for other in range(position)):
            numbering = _numbering(gram, expected, (*chosen, index))
            if numbering is not None:
                return numbering
    return None


def typed_component(gram_tensor: GramTensor, base: list[Vector]) -> tuple[str, Fraction, list[Vector]]:
    """Return the type, the scale and the simple roots, in the numbering of the type, of an irreducible component with the given base."""
    norms = [arithmetic.pairing(gram_tensor, r, r) for r in base]
    scale = min(norms, key=abs) / 2
    gram = tuple(tuple(value / scale for value in row) for row in arithmetic.restriction(gram_tensor, tuple(base)))
    for letter in "ABCDEFG":
        root_type = f"{letter}{len(base)}"
        if root_systems.is_type(root_type):
            numbering = _numbering(gram, root_systems.simple_root_gram(root_type), ())
            if numbering is not None:
                return root_type, scale, [base[index] for index in numbering]
    raise AssertionError(f"no type for the base {base}")


def root_system(gram_tensor: GramTensor) -> list[Yaml]:
    """Return `Phi(L)` for a definite lattice as its irreducible components, the greatest rank first."""
    base = simple_roots(list(arithmetic.definite_roots(gram_tensor)))
    components = [typed_component(gram_tensor, component) for component in irreducible_components(gram_tensor, base)]
    components.sort(key=lambda component: (-len(component[2]), component[0], component[2]))
    return [{"type": root_type, "scale": rational(scale), "simple_roots": [list(r) for r in rows]} for root_type, scale, rows in components]


def small_roots(gram_tensor: GramTensor) -> list[Vector]:
    """Return the roots with coordinates in `{-1, 0, 1}`, at most three of them nonzero and the first of those equal to 1."""
    rank = len(gram_tensor)
    roots = []
    for size in range(1, min(rank, 3) + 1):
        for support in combinations(range(rank), size):
            for signs in product((1, -1), repeat=size - 1):
                coefficients = dict(zip(support, (1, *signs), strict=True))
                r = tuple(coefficients.get(index, 0) for index in range(rank))
                if arithmetic.is_root(gram_tensor, r):
                    roots.append(r)
    return roots


def generating_roots(roots: list[Vector], rank: int) -> list[Vector]:
    """Return a basis of `L` that is a sublist of `roots` when the greedy choice gives one, and otherwise a sublist that generates `L`. `roots` must generate `L`.

    The greedy choice takes a root when the roots taken, with it, are a basis
    of a primitive sublattice. The other choice takes a root when it is not in
    the sublattice that the roots taken generate.
    """
    basis: list[Vector] = []
    for r in roots:
        if arithmetic.invariant_factors([*basis, r], rank) == (1,) * (len(basis) + 1):
            basis.append(r)
    if len(basis) == rank:
        return basis
    taken: list[Vector] = []
    for r in roots:
        if arithmetic.span_basis([*taken, r]) != arithmetic.span_basis(taken):
            taken.append(r)
    return taken


def main() -> None:
    written = 0
    for entry in corpus.load(CORPUS):
        lattice = entry.lattice
        text = entry.path.read_text()
        record: dict[str, Yaml] = frontmatter.loads(text).metadata
        assert record_text(record, entry.prose) == text, f"{entry.path} does not have the layout that this script writes"
        if lattice.is_definite:
            match record["definite"]:
                case dict() as definite:
                    record["definite"] = {**definite, "roots": root_system(lattice.gram_tensor)}
        elif lattice.root_span is None:
            roots = small_roots(lattice.gram_tensor)
            if not arithmetic.generate(roots, lattice.rank):
                print(f"{lattice.tag} {lattice.name}: the roots found do not generate L; Z Phi(L) is not decided")
                continue
            record["root_span"] = {"roots": [list(r) for r in generating_roots(roots, lattice.rank)]}
        updated = record_text(record, entry.prose)
        if updated != text:
            entry.path.write_text(updated)
            written += 1
    print(f"{written} records written")


if __name__ == "__main__":
    main()
