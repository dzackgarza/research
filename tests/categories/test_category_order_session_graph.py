from __future__ import annotations

import json
import subprocess
import sys

_SESSION_SCRIPT = r'''
import json
import sys

from dzack_research.preamble.all import (
    AffineSpaces,
    Lattices,
    QQ,
    ZZ,
)
from dzack_research.preamble.categories.sets import finite_ordered_set
from dzack_research.preamble.owned_category import (
    _category_graph_signature,
    _category_parameter_signature,
    _stable_signature_integer,
)


def category_key(obj):
    category = obj.category()
    return _stable_signature_integer(
        (_category_graph_signature(category), _category_parameter_signature(category))
    )


def affine_open():
    line = AffineSpaces(QQ)(1, names=("x",))
    ring = line.coordinate_ring()
    x = ring.algebra_generator("x")
    open_x = line.distinguished_open(x)
    inclusion = open_x.inclusion()
    return {
        "scheme_category": category_key(open_x),
        "algebra_category": category_key(open_x.coordinate_algebra()),
        "inclusion_hom_category": category_key(inclusion.parent()),
        "is_open": bool(open_x.is_distinguished_open()),
    }


def matrix_hom():
    source = ZZ.free_module(finite_ordered_set(("e0", "e1")))
    target = ZZ.free_module(finite_ordered_set(("f0", "f1")))
    f0, f1 = target.module_generators()
    morphism = source.module_category().Mor(source, target)(
        {"e0": f0 + 2 * f1, "e1": 3 * f0 - f1}
    )
    e0, e1 = source.module_generators()
    return {
        "mor_category": category_key(morphism.parent()),
        "source_category": category_key(source),
        "target_category": category_key(target),
        "e0_image": [
            int(target.framing_coefficients(morphism(e0)).get(label, ZZ.zero()))
            for label in target.module_generating_set()
        ],
        "e1_image": [
            int(target.framing_coefficients(morphism(e1)).get(label, ZZ.zero()))
            for label in target.module_generating_set()
        ],
    }


def lattice_rank():
    lattice = Lattices(ZZ)("U") + Lattices(ZZ)("A2")
    return {
        "category": category_key(lattice),
        "rank": int(lattice.module_rank()),
        "determinant": int(lattice.determinant()),
    }


def a2_discriminant():
    discriminant = Lattices(ZZ)("A2").discriminant_group()
    return {
        "category": category_key(discriminant),
        "cardinality": int(discriminant.cardinality()),
        "invariants": [int(entry) for entry in discriminant.invariant_factors()],
    }


def isotropic_overlattice():
    a1 = Lattices(ZZ)("A1")
    lattice = a1 + a1 + a1 + a1
    discriminant = lattice.discriminant_module()
    diagonal = sum(discriminant.module_generators(), discriminant.zero())
    if diagonal.q() != discriminant.quadratic_value_module().zero():
        raise ArithmeticError("the selected diagonal class is not isotropic")
    inclusion = lattice.overlattice(diagonal)
    overlattice = inclusion.codomain()
    return {
        "source_category": category_key(lattice),
        "target_category": category_key(overlattice),
        "mor_category": category_key(inclusion.parent()),
        "index": int(inclusion.index()),
        "rank": int(overlattice.module_rank()),
        "determinant": int(overlattice.determinant()),
    }


constructors = {
    "affine_open": affine_open,
    "matrix_hom": matrix_hom,
    "lattice_rank": lattice_rank,
    "a2_discriminant": a2_discriminant,
    "isotropic_overlattice": isotropic_overlattice,
}
order = sys.argv[1].split(",")
result = {}
for name in order:
    result[name] = constructors[name]()
print(json.dumps(result, sort_keys=True))
'''


def _run_order(order: tuple[str, ...]) -> dict[str, object]:
    completed = subprocess.run(
        [sys.executable, "-c", _SESSION_SCRIPT, ",".join(order)],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(completed.stdout)


def test_actual_session_graph_is_independent_of_construction_order() -> None:
    forward = (
        "affine_open",
        "matrix_hom",
        "lattice_rank",
        "a2_discriminant",
        "isotropic_overlattice",
    )
    reverse = tuple(reversed(forward))

    first = _run_order(forward)
    second = _run_order(reverse)

    assert first == second
    assert first["affine_open"]["is_open"] is True
    assert first["matrix_hom"]["e0_image"] == [1, 2]
    assert first["matrix_hom"]["e1_image"] == [3, -1]
    assert first["lattice_rank"]["rank"] == 4
    assert first["a2_discriminant"]["cardinality"] == 3
    assert first["a2_discriminant"]["invariants"] == [3]
    assert first["isotropic_overlattice"]["index"] == 2
    assert first["isotropic_overlattice"]["rank"] == 4
    assert abs(first["isotropic_overlattice"]["determinant"]) == 4
