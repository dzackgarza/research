"""Profile invariant-to-coinvariant discriminant transport on two specimens.

Run with Sage's Python and the pinned port acceptance test file:

    sage -python scripts/profile_coinvariant_transport.py PORT_TEST_BOUNDARIES
"""

from __future__ import annotations

import cProfile
import os
import pstats
import sys
import time
from pathlib import Path

from dzack_research.preamble.all import Lattices, ZZ
from dzack_research.preamble.categories.lattice_centralizers import IsometryPrimitiveExtension


def profile_transport(label, action):
    calls = []
    orders = set()
    original = IsometryPrimitiveExtension._coinvariant_discriminant_from_invariant

    def timed(self, automorphism):
        if not orders:
            orders.add((self.invariant.discriminant_group().cardinality(), self.orthogonal_complement.discriminant_group().cardinality()))
        started = time.perf_counter()
        try:
            return original(self, automorphism)
        finally:
            calls.append(time.perf_counter() - started)

    IsometryPrimitiveExtension._coinvariant_discriminant_from_invariant = timed
    profiler = cProfile.Profile()
    try:
        profiler.enable()
        result = action()
    finally:
        profiler.disable()
        IsometryPrimitiveExtension._coinvariant_discriminant_from_invariant = original

    print(f"[{label}] discriminant_orders={sorted(orders)} transport_calls={len(calls)} transport_seconds={sum(calls):.6f} mean_seconds={sum(calls) / max(1, len(calls)):.6f}", flush=True)
    print(f"[{label}] result_type={type(result).__name__}", flush=True)
    stats = pstats.Stats(profiler)
    for needle in (
        "_presented_module_from_morphism",
        "_normalized_form_automorphism",
        "_coinvariant_discriminant_from_invariant",
        "_framing_lift",
        "validate_inverse",
        "validate_form_preservation",
    ):
        rows = [value for key, value in stats.stats.items() if needle in key[2]]
        if rows:
            print(
                f"[{label}] {needle}: calls={sum(row[0] for row in rows)} "
                f"cumulative_seconds={sum(row[3] for row in rows):.6f}",
                flush=True,
            )
    stats.sort_stats("cumulative").print_stats(24)


def small_extension():
    lattice = Lattices(ZZ)(
        [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]
    )
    e, f, u, v = tuple(lattice.module_generators().values())
    involution = lattice.O()({0: u, 1: v, 2: e, 3: f})
    return involution.polarized(e + u + f + v).primitive_extension()


def main(port_test_file: Path) -> None:
    from sage.repl.load import load

    extension = small_extension()
    generators = extension.invariant.discriminant_image().group_generators()
    profile_transport("U+U", lambda: tuple(extension._coinvariant_discriminant_from_invariant(g) for g in generators))

    research_test = Path(__file__).resolve().parents[1] / "tests/lattices/test_polarized_equivariant_lattice.sage"
    load(str(research_test), globals(), attach=False)
    test_coinvariant_discriminant_transport_preserves_inverse_and_glue()
    print("[U+U] inverse/glue regression: PASS", flush=True)

    sys.path.insert(0, str(port_test_file.parents[2]))
    os.chdir(port_test_file.parents[2])
    load(str(port_test_file), globals(), attach=False)
    case = next(case for case in _ENRIQUES if case["case"] == 1)

    profile_transport("Enriques-case-1", lambda: _gamma_h(case["face_polarization"]))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: sage -python scripts/profile_coinvariant_transport.py PORT_TEST_BOUNDARIES")
    main(Path(sys.argv[1]))
