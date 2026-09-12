"""Private CAP/homalg kernel crossing for finitely presented modules.

The public objects remain the repository's owned finitely presented modules.
CAP receives only selected presentation matrices over a supported computable
coefficient ring and returns a kernel embedding.  This module crosses the
returned relation and embedding matrices back to the owned coefficient ring;
no CAP object is part of the public mathematical interface.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass
from functools import cache
from pathlib import Path

from sage.libs.gap.libgap import libgap

_PACKAGE_VERSIONS = {
    "RingsForHomalg": "2026.05-01",
    "CAP": "2026.07-04",
    "ModulePresentationsForCAP": "2026.06-01",
}
_PACKAGE_NAME = re.compile(r'PackageName\s*:=\s*"([^"]+)"')


def _package_root() -> Path:
    configured = os.environ.get("DZACK_RESEARCH_GAP_PACKAGE_DIR")
    if configured:
        return Path(configured).resolve()
    return Path(__file__).resolve().parents[5] / ".gap" / "pkg"


def _installed_package_paths() -> dict[str, tuple[str, Path]]:
    root = _package_root()
    if not root.is_dir():
        raise RuntimeError(
            f"the CAP package directory {root} does not exist; run GAP on .gap-packages.g"
        )
    result = {}
    for info in root.glob("*/PackageInfo.g"):
        if info.parent.name.endswith(".old"):
            continue
        text = info.read_text(encoding="utf-8")
        match = _PACKAGE_NAME.search(text)
        if match is not None:
            result[match.group(1).lower()] = (match.group(1), info.parent.resolve())
    return result


@cache
def _load_packages() -> None:
    installed = _installed_package_paths()
    for actual_name, path in installed.values():
        libgap.SetPackagePath(actual_name, str(path))
    for name, version in _PACKAGE_VERSIONS.items():
        installed_entry = installed.get(name.lower())
        if installed_entry is None:
            raise RuntimeError(f"the exact CAP provider has no installed {name} under {_package_root()}")
        actual_name, path = installed_entry
        loaded = libgap.LoadPackage(actual_name, f"={version}", False)
        if loaded != libgap.true:
            raise RuntimeError(f"failed to load {name} {version} from {path}")
        actual = str(libgap.InstalledPackageVersion(actual_name))
        if actual != version:
            raise RuntimeError(f"loaded {name} {actual}, expected {version}")


@cache
def _polynomial_ring(variable_names: tuple[str, ...]):
    _load_packages()
    integers = libgap.HomalgRingOfIntegersInSage()
    return libgap.PolynomialRing(integers, list(variable_names))


def _homalg_matrix(rows, columns: int, ring):
    rows = tuple(tuple(str(entry) for entry in row) for row in rows)
    if not rows:
        return libgap.HomalgZeroMatrix(0, columns, ring)
    return libgap.HomalgMatrix([list(row) for row in rows], len(rows), columns, ring)


def _matrix_rows(matrix, owned_ring):
    row_count = int(libgap.NumberRows(matrix))
    column_count = int(libgap.NumberColumns(matrix))
    entries = tuple(libgap.EntriesOfHomalgMatrix(matrix))
    if len(entries) != row_count * column_count:
        raise ArithmeticError("CAP returned a matrix with inconsistent dimensions")
    return tuple(
        tuple(
            owned_ring(str(entries[row * column_count + column]))
            for column in range(column_count)
        )
        for row in range(row_count)
    )


@dataclass(frozen=True, eq=False, slots=True)
class CAPKernelPresentation:
    """Private native kernel data with owned-matrix crossings."""

    owned_ring: object
    ring: object
    category: object
    source: object
    target: object
    morphism: object
    embedding: object

    def relation_rows(self):
        return _matrix_rows(
            libgap.UnderlyingMatrix(libgap.Source(self.embedding)),
            self.owned_ring,
        )

    def inclusion_rows(self):
        return _matrix_rows(libgap.UnderlyingMatrix(self.embedding), self.owned_ring)

    def lift_row(self, source_row):
        """Lift one represented source element through the kernel embedding."""
        free_one = libgap.FreeLeftPresentation(1, self.ring)
        tau = libgap.PresentationMorphism(
            free_one,
            _homalg_matrix((tuple(source_row),), len(tuple(source_row)), self.ring),
            self.source,
        )
        lifted = libgap.KernelLift(self.morphism, free_one, tau)
        rows = _matrix_rows(libgap.UnderlyingMatrix(lifted), self.owned_ring)
        if len(rows) != 1:
            raise ArithmeticError("CAP returned a kernel lift with the wrong source rank")
        return rows[0]


def kernel_presentation(
    *,
    variable_names: tuple[str, ...],
    owned_ring,
    source_rank: int,
    target_rank: int,
    source_relation_rows,
    target_relation_rows,
    morphism_rows,
):
    """Return retained private CAP data for a categorical kernel embedding."""
    ring = _polynomial_ring(tuple(variable_names))
    morphism_rows = tuple(tuple(row) for row in morphism_rows)
    source_rank = int(source_rank)
    target_rank = int(target_rank)
    if len(morphism_rows) != source_rank or any(len(row) != target_rank for row in morphism_rows):
        raise ValueError("the CAP morphism matrix has the wrong selected framing dimensions")
    category = libgap.LeftPresentations(ring)
    source = libgap.AsLeftPresentation(
        category,
        _homalg_matrix(source_relation_rows, source_rank, ring),
    )
    target = libgap.AsLeftPresentation(
        category,
        _homalg_matrix(target_relation_rows, target_rank, ring),
    )
    morphism = libgap.PresentationMorphism(
        source,
        _homalg_matrix(morphism_rows, target_rank, ring),
        target,
    )
    embedding = libgap.KernelEmbedding(morphism)
    return CAPKernelPresentation(
        owned_ring, ring, category, source, target, morphism, embedding
    )


__all__ = ["CAPKernelPresentation", "kernel_presentation"]
