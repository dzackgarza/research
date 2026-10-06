"""The embeddings of a lattice into a record that is an orthogonal sum of its summands, found by combinatorics.

The orthogonal summands of a record $T$ are the connected components of the graph on its basis in which
$e_i$ and $e_j$ are adjacent when $b(e_i, e_j) \\neq 0$. Group the summands with one Gram matrix $G_M$: $T
\\cong \\bigoplus_M M^{n_M}$. Let a part of size $k$ be a set of $k$ summands of one group. Then the
diagonal $x \\mapsto (x, \\ldots, x)$ is an embedding $M(k) \\to M^k$, since $b(\\sum_i x, \\sum_i y) = k \\,
b_M(x, y)$. For each group $M$ and each partition $\\lambda$ of an integer $m \\leq n_M$, the parts of
$\\lambda$ placed on consecutive summands of the group give an embedding $\\bigoplus_M \\bigoplus_j
M(\\lambda_j) \\to T$. Up to the permutations of the summands of each group, these are all the embeddings
whose matrix restricted to each source summand is a diagonal of identity blocks; there are $\\prod_M
\\sum_{m \\leq n_M} p(m)$ of them, with $p$ the partition function, the identity of $T$ among them.

A source with the parts $\\lambda_j$ and $g = \\gcd_j \\lambda_j$ is the twist by $g$ of the lattice with the
Gram matrices $(\\lambda_j / g) G_M$, so the embedding is a morphism of scale $g$ from a record with these
summands, when the corpus has one.
"""

from collections import Counter
from collections.abc import Iterator, Sequence
from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from pathlib import Path

import cypari2
import frontmatter
from pydantic import TypeAdapter

from latticedb import corpus, records
from latticedb.corpus import Corpus, Entry
from latticedb.model import GramTensor, Morphism, Tag, Yaml

pari = cypari2.Pari()

Block = tuple[tuple[Fraction, ...], ...]
"""The Gram matrix of one orthogonal summand, in the basis vectors of the record that span it."""


@dataclass(frozen=True)
class Embedding:
    source: Tag
    target: Tag
    matrix: tuple[tuple[int, ...], ...]
    scale: int
    parts: tuple[tuple[int, ...], ...]
    """For each summand of the source, in the order of its basis, the summands of the target (counted from 1) into which it maps diagonally."""


def summands(gram: GramTensor) -> list[tuple[int, ...]]:
    """The basis indices of each orthogonal summand, ordered by the first index: the connected components of the graph of the nonzero entries.

    The search is breadth-first search (Cormen et al., Introduction to Algorithms, 22.2).
    """
    found: list[tuple[int, ...]] = []
    seen: set[int] = set()
    for start in range(len(gram)):
        if start in seen:
            continue
        component = [start]
        seen.add(start)
        for index in component:
            for other in range(len(gram)):
                if other not in seen and gram[index][other] != 0:
                    seen.add(other)
                    component.append(other)
        found.append(tuple(sorted(component)))
    return found


def block(gram: GramTensor, indices: tuple[int, ...]) -> Block:
    return tuple(tuple(gram[i][j] for j in indices) for i in indices)


def scaled(gram: Block, factor: int) -> Block:
    return tuple(tuple(factor * entry for entry in row) for row in gram)


def _partitions(n: int) -> Iterator[tuple[int, ...]]:
    """The partitions of the integers 0, ..., n, by `partitions` of PARI/GP."""
    for m in range(n + 1):
        for partition in pari.partitions(m):
            yield tuple(int(part) for part in partition)


def _choices(groups: Sequence[Sequence[int]]) -> Iterator[list[tuple[int, ...]]]:
    """For each choice of a partition per group, the parts as tuples of positions of summands: consecutive summands of the group."""
    if not groups:
        yield []
        return
    first, rest = groups[0], groups[1:]
    for partition in _partitions(len(first)):
        parts, start = [], 0
        for part in partition:
            parts.append(tuple(first[start : start + part]))
            start += part
        for others in _choices(rest):
            yield parts + others


def embeddings(target: Entry, by_summands: dict[tuple[Block, ...], list[Entry]]) -> Iterator[Embedding]:
    """The embeddings into `target` of the module docstring whose source, up to its twist, is a record of `by_summands`, other than the identity."""
    gram = target.lattice.gram_tensor
    components = summands(gram)
    blocks = [block(gram, indices) for indices in components]
    groups: dict[Block, list[int]] = {}
    for position, summand in enumerate(blocks):
        groups.setdefault(summand, []).append(position)
    for parts in _choices(list(groups.values())):
        if not parts or (len(parts) == len(components) and all(len(part) == 1 for part in parts)):
            continue
        twist = gcd(*(len(part) for part in parts))
        wanted = [scaled(blocks[part[0]], len(part) // twist) for part in parts]
        for source in by_summands.get(_key(wanted), []):
            yield _embedding(source, target, components, parts, wanted, twist)


def _key(blocks: Sequence[Block]) -> tuple[Block, ...]:
    return tuple(sorted(blocks))


def _embedding(source: Entry, target: Entry, components: list[tuple[int, ...]], parts: list[tuple[int, ...]], wanted: list[Block], twist: int) -> Embedding:
    """The matrix that sends each summand of `source` diagonally into the summands of `target` of the part with its Gram matrix."""
    gram = source.lattice.gram_tensor
    free = Counter(range(len(parts)))
    columns: list[list[int]] = []
    order: list[tuple[int, ...]] = []
    for indices in summands(gram):
        part = next(p for p in free if free[p] and wanted[p] == block(gram, indices))
        free[part] -= 1
        order.append(tuple(position + 1 for position in parts[part]))
        for local in range(len(indices)):
            column = [0] * len(target.lattice.gram_tensor)
            for position in parts[part]:
                column[components[position][local]] = 1
            columns.append(column)
    matrix = tuple(tuple(column[row] for column in columns) for row in range(len(target.lattice.gram_tensor)))
    return Embedding(source.lattice.tag, target.lattice.tag, matrix, twist, tuple(order))


def all_embeddings(entries: Sequence[Entry]) -> list[Embedding]:
    """The embeddings of the module docstring between the records of `entries`."""
    by_summands: dict[tuple[Block, ...], list[Entry]] = {}
    for entry in entries:
        gram = entry.lattice.gram_tensor
        by_summands.setdefault(_key([block(gram, indices) for indices in summands(gram)]), []).append(entry)
    return [embedding for entry in entries for embedding in embeddings(entry, by_summands)]


CERTIFICATE = "corpus summands"
"""The name of the computation of the embeddings between the records; its inputs are the Gram tensors of the corpus."""

def _morphism(embedding: Embedding) -> dict[str, Yaml]:
    sets = " \\sqcup ".join("\\{" + ", ".join(str(position) for position in part) + "\\}" for part in embedding.parts)
    morphism: dict[str, Yaml] = {
        "target": embedding.target,
        "name": f"Diagonal into the summands ${sets}$",
        "description": (
            "Summand $j$ of the source maps by $x \\mapsto (x, \\ldots, x)$ into the orthogonal summands of the target in set $j$, "
            "which are counted from 1 in the order of the basis."
        ),
        "matrix": [list(row) for row in embedding.matrix],
    }
    if embedding.scale != 1:
        morphism["scale"] = embedding.scale
    return morphism


def store(root: Path, loaded: Corpus) -> list[str]:
    """Write each new summand embedding on its source lattice card."""
    by_tag = {entry.lattice.tag: entry.lattice for entry in loaded.entries}
    found: list[str] = []
    new: dict[Tag, list[dict[str, Yaml]]] = {}
    for embedding in all_embeddings(loaded.entries):
        morphism = _morphism(embedding)
        found.extend(records.morphism_problems(Morphism.model_validate(morphism), by_tag[embedding.source], by_tag[embedding.target]))
        held = by_tag[embedding.source].morphisms
        if not any(m.matrix == embedding.matrix and m.scale == embedding.scale for m in held):
            new.setdefault(embedding.source, []).append(morphism)
    if found:
        return found
    for source, morphisms in new.items():
        path = root / "lattices" / f"{source}.md"
        document = frontmatter.load(str(path))
        metadata = corpus.front_matter(document)
        stored = TypeAdapter(list[dict[str, Yaml]]).validate_python(metadata.get("morphisms", []))
        metadata["morphisms"] = stored + morphisms
        path.write_text(records.record_text(metadata, document.content))
    print(f"{sum(len(m) for m in new.values())} embeddings of orthogonal summands written to {len(new)} source lattice cards")
    return []
