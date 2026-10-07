"""Mathematical predicates on finite weighted graph decorations.

Migrated from ``lattice-database/src/latticedb/graphs.py``. Database graph
cards serialize vertices/edges and delegate Coxeter, Dynkin, Satake and
Vinberg recognition to this preamble-owned object.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class WeightedVertexData:
    id: str
    weight: object = None


@dataclass(frozen=True)
class WeightedEdgeData:
    id: str
    source: str
    target: str
    relation: str
    directed: bool = False
    weight: object = None


def _weight_map(weight) -> dict | None:
    return weight if isinstance(weight, dict) else None


def _integer(value) -> int | None:
    return value if isinstance(value, int) and not isinstance(value, bool) else None


def _fraction(value) -> Fraction | None:
    if isinstance(value, bool) or not isinstance(value, (int, str)):
        return None
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError):
        return None


def _solve(matrix: list[list[Fraction]], values: list[Fraction]) -> list[Fraction]:
    n = len(values)
    rows = [row[:] + [value] for row, value in zip(matrix, values, strict=True)]
    for column in range(n):
        pivot = next(row for row in range(column, n) if rows[row][column])
        rows[column], rows[pivot] = rows[pivot], rows[column]
        factor = rows[column][column]
        rows[column] = [value / factor for value in rows[column]]
        for row in range(n):
            if row != column:
                factor = rows[row][column]
                rows[row] = [
                    value - factor * entry
                    for value, entry in zip(rows[row], rows[column], strict=True)
                ]
    return [row[-1] for row in rows]


def _inertia(matrix: list[list[Fraction]]) -> tuple[int, int, int]:
    positive = negative = zero = 0
    while matrix:
        pivot = next((i for i in range(len(matrix)) if matrix[i][i]), None)
        if pivot is None:
            pair = next(
                (
                    (i, j)
                    for i in range(len(matrix))
                    for j in range(i + 1, len(matrix))
                    if matrix[i][j]
                ),
                None,
            )
            if pair is None:
                zero += len(matrix)
                break
            i, j = pair
            matrix[i] = [
                left + right for left, right in zip(matrix[i], matrix[j], strict=True)
            ]
            for row in matrix:
                row[i] += row[j]
            pivot = i
        diagonal = matrix[pivot][pivot]
        positive += int(diagonal > 0)
        negative += int(diagonal < 0)
        indices = [i for i in range(len(matrix)) if i != pivot]
        matrix = [
            [
                matrix[i][j]
                - matrix[i][pivot] * matrix[pivot][j] / diagonal
                for j in indices
            ]
            for i in indices
        ]
    return positive, negative, zero


class WeightedGraphInvariants:
    """Mathematical interpretation of one finite decorated weighted graph."""

    def __init__(self, vertices, edges):
        self.vertices = tuple(vertices)
        self.edges = tuple(edges)

    def _bond_data(self):
        bonds = {}
        for edge in self.edges:
            if edge.relation == "satake_pair":
                continue
            if edge.relation != "bond" or edge.directed or edge.source == edge.target:
                return None
            pair = frozenset((edge.source, edge.target))
            if pair in bonds:
                return None
            weight = _weight_map(edge.weight)
            if weight is None:
                return None
            cartan_value = weight.get("cartan")
            cartan = None
            if cartan_value is not None:
                if not isinstance(cartan_value, list) or len(cartan_value) != 2:
                    return None
                left, right = (_integer(value) for value in cartan_value)
                if left is None or right is None or left >= 0 or right >= 0:
                    return None
                cartan = (left, right)
            order = weight.get("order")
            if order is not None and not (
                order == "infinity" or (_integer(order) is not None and order >= 3)
            ):
                return None
            if cartan is not None:
                product = cartan[0] * cartan[1]
                derived = {1: 3, 2: 4, 3: 6}.get(product, "infinity")
                if order is not None and order != derived:
                    return None
                order = derived
            if order is None:
                return None
            bonds[pair] = (order, cartan)
        return bonds

    def is_coxeter(self) -> bool:
        return bool(self.vertices) and self._bond_data() is not None

    def cartan_matrix(self) -> tuple[tuple[int, ...], ...] | None:
        if not self.is_coxeter():
            return None
        ids = [vertex.id for vertex in self.vertices]
        positions = {vertex: index for index, vertex in enumerate(ids)}
        matrix = [[2 if i == j else 0 for j in range(len(ids))] for i in range(len(ids))]
        for edge in self.edges:
            if edge.relation != "bond":
                continue
            weight = _weight_map(edge.weight)
            if weight is None or not isinstance(weight.get("cartan"), list):
                return None
            left, right = weight["cartan"]
            i, j = positions[edge.source], positions[edge.target]
            matrix[i][j], matrix[j][i] = left, right
        return tuple(tuple(row) for row in matrix)

    def is_dynkin(self) -> bool:
        cartan = self.cartan_matrix()
        if cartan is None:
            return False
        n = len(cartan)
        factors: list[Fraction | None] = [None] * n
        for start in range(n):
            if factors[start] is not None:
                continue
            factors[start] = Fraction(1)
            pending = [start]
            while pending:
                i = pending.pop()
                for j in range(n):
                    if cartan[i][j] == 0:
                        continue
                    candidate = factors[i] * Fraction(cartan[i][j], cartan[j][i])
                    if factors[j] is None:
                        factors[j] = candidate
                        pending.append(j)
                    elif factors[j] != candidate:
                        return False
        sym = [[factors[i] * cartan[i][j] for j in range(n)] for i in range(n)]
        if any(sym[i][j] != sym[j][i] for i in range(n) for j in range(n)):
            return False
        norms = []
        for vertex in self.vertices:
            weight = _weight_map(vertex.weight)
            value = weight.get("root_length_squared") if weight is not None else None
            norm = _fraction(value) if value is not None else None
            if value is not None and (norm is None or norm <= 0):
                return False
            norms.append(norm)
        for i in range(n):
            for j in range(i + 1, n):
                if (
                    cartan[i][j]
                    and norms[i] is not None
                    and norms[j] is not None
                    and norms[i] * cartan[i][j] != norms[j] * cartan[j][i]
                ):
                    return False
        for pivot in range(n):
            diagonal = sym[pivot][pivot]
            if diagonal <= 0:
                return False
            for i in range(pivot + 1, n):
                for j in range(pivot + 1, n):
                    sym[i][j] -= sym[i][pivot] * sym[pivot][j] / diagonal
        return True

    def is_simply_laced(self) -> bool:
        cartan = self.cartan_matrix()
        return (
            self.is_dynkin()
            and cartan is not None
            and all(
                value in (0, -1)
                for i, row in enumerate(cartan)
                for j, value in enumerate(row)
                if i != j
            )
        )

    def is_rational_coxeter_vinberg(self) -> bool:
        bonds = self._bond_data()
        if bonds is None or len(self.vertices) < 3:
            return False
        norms = []
        for vertex in self.vertices:
            weight = _weight_map(vertex.weight)
            norm = _fraction(weight.get("norm_squared")) if weight is not None else None
            if norm is None or norm <= 0:
                return False
            norms.append(norm)
        positions = {vertex.id: i for i, vertex in enumerate(self.vertices)}
        gram = [
            [norms[i] if i == j else Fraction(0) for j in range(len(norms))]
            for i in range(len(norms))
        ]
        for edge in self.edges:
            if edge.relation != "bond":
                continue
            weight = _weight_map(edge.weight)
            entry = _fraction(weight.get("gram")) if weight is not None else None
            if entry is None or entry >= 0:
                return False
            i, j = positions[edge.source], positions[edge.target]
            ratio = entry * entry / (norms[i] * norms[j])
            order = bonds[frozenset((edge.source, edge.target))][0]
            if order == "infinity":
                if ratio < 1:
                    return False
            elif ratio != {3: Fraction(1, 4), 4: Fraction(1, 2), 6: Fraction(3, 4)}.get(order):
                return False
            gram[i][j] = gram[j][i] = entry
        return _inertia(gram) == (len(norms) - 1, 1, 0)

    def is_satake(self) -> bool:
        if not self.is_dynkin():
            return False
        cartan = self.cartan_matrix()
        assert cartan is not None
        ids = [vertex.id for vertex in self.vertices]
        marks = [
            _weight_map(vertex.weight).get("satake")
            if _weight_map(vertex.weight) is not None
            else None
            for vertex in self.vertices
        ]
        if any(mark not in ("black", "white") for mark in marks):
            return False
        positions = {vertex: index for index, vertex in enumerate(ids)}
        black = [i for i, mark in enumerate(marks) if mark == "black"]
        tau = list(range(len(ids)))
        for edge in self.edges:
            if edge.relation != "satake_pair":
                continue
            i, j = positions[edge.source], positions[edge.target]
            if (
                edge.directed
                or edge.weight is not None
                or i == j
                or marks[i] != "white"
                or marks[j] != "white"
                or tau[i] != i
                or tau[j] != j
            ):
                return False
            tau[i], tau[j] = j, i
        columns = [[int(i == j) for i in range(len(ids))] for j in range(len(ids))]
        while (
            positive := next(
                (j for j in black if all(value >= 0 for value in columns[j])), None
            )
        ) is not None:
            old = columns[positive]
            columns = [
                [value - cartan[positive][i] * old[k] for k, value in enumerate(column)]
                for i, column in enumerate(columns)
            ]
        for i in black:
            opposite = [-value for value in columns[i]]
            if opposite.count(1) != 1 or any(value not in (0, 1) for value in opposite):
                return False
            tau[i] = opposite.index(1)
        if len(set(tau)) != len(tau) or any(tau[tau[i]] != i for i in range(len(ids))):
            return False
        if any(
            cartan[tau[i]][tau[j]] != cartan[i][j]
            for i in range(len(ids))
            for j in range(len(ids))
        ):
            return False
        if black:
            submatrix = [[Fraction(cartan[j][i]) for j in black] for i in black]
            coefficients = _solve(submatrix, [Fraction(1)] * len(black))
            for i, mark in enumerate(marks):
                if (
                    mark == "white"
                    and tau[i] == i
                    and sum(
                        coefficients[j] * cartan[black[j]][i]
                        for j in range(len(black))
                    ).denominator
                    != 1
                ):
                    return False
        return True
