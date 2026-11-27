import sys
from pathlib import Path

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.cat import Cat
from category_specs.modules import Modules
from category_specs.tensor_algebra_components import TensorAlgebraComponents
from category_specs.types import Tensor
from category_specs.utils import assert_smoke_statements


C = TensorAlgebraComponents(ZZ)
M = FiniteRankFreeModule(ZZ, 2, name="M")
preferred_generators = M.basis("e")
constructors = C.Constructors()


def identity_tensor():
    return constructors.from_multidimensional_list(M, (1, 1), [[1, 0], [0, 1]], name="t")


def multiplication_tensor():
    return constructors.from_module_element_matrix(
        M,
        [
            [preferred_generators[0], 2 * preferred_generators[0] + 3 * preferred_generators[1]],
            [
                5 * preferred_generators[0] + 7 * preferred_generators[1],
                11 * preferred_generators[0] + 13 * preferred_generators[1],
            ],
        ],
        name="mu",
    )


def scalar_matrix_tensor():
    return constructors.from_matrix(M, matrix(ZZ, [[2, 1], [1, 3]]), name="b")


def legacy_matrix_list_tensor():
    return constructors.from_matrices(
        M,
        (1, 2),
        [matrix(ZZ, [[1, 0], [0, 1]]), matrix(ZZ, [[0, 1], [1, 0]])],
        name="mu_legacy",
    )

SMOKE_STATEMENTS = (
    ("TensorAlgebraComponents(ZZ) is an object of Cat()", lambda _: C in Cat()),
    (
        "TensorAlgebraComponents(ZZ) is below Modules(ZZ).TensorProducts()",
        lambda _: C.is_subcategory(Modules(ZZ).TensorProducts()),
    ),
    (
        "TensorAlgebraComponents(ZZ) is below finite-rank free modules",
        lambda _: C.is_subcategory(Modules(ZZ).Free().FiniteRank()),
    ),
    (
        "Modules(ZZ).TensorProducts().TensorAlgebraComponents() returns the tensor component subtree",
        lambda _: Modules(ZZ).TensorProducts().TensorAlgebraComponents() == C,
    ),
    ("component_module(M, (1, 1)) refines to tensor components", lambda _: constructors.component_module(M, (1, 1)) in C),
    ("tensor(M, (1, 1)) has tensor-component parent", lambda _: constructors.tensor(M, (1, 1), name="u").parent() in C),
    (
        "from_multidimensional_list(M, (1, 1), ...) returns a (1,1) tensor",
        lambda _: constructors.from_multidimensional_list(M, (1, 1), [[1, 0], [0, 1]], name="c").tensor_type()
        == (1, 1),
    ),
    ("component module recovers base module", lambda _: identity_tensor().parent().base_module() is M),
    ("component module has tensor type", lambda _: identity_tensor().parent().tensor_type() == (1, 1)),
    ("tensor element has tensor type", lambda _: identity_tensor().tensor_type() == (1, 1)),
    ("Tensor is the tensor element type surface", lambda _: isinstance(Tensor, type)),
    ("matrix constructor returns a (0,2) tensor", lambda _: scalar_matrix_tensor().tensor_type() == (0, 2)),
    ("matrix constructor leaves parent recoverable", lambda _: scalar_matrix_tensor().parent().base_module() is M),
    ("module-element matrix constructor returns a (1,2) tensor", lambda _: multiplication_tensor().tensor_type() == (1, 2)),
    ("module-element matrix constructor leaves parent recoverable", lambda _: multiplication_tensor().parent().base_module() is M),
    (
        "module-element matrix tensor exposes multiplication structure constants",
        lambda _: tuple(multiplication_tensor().structure_constants())
        == (
            matrix(ZZ, [[1, 2], [5, 11]]),
            matrix(ZZ, [[0, 3], [7, 13]]),
        ),
    ),
    ("matrix-list constructor remains tensor interop", lambda _: legacy_matrix_list_tensor().tensor_type() == (1, 2)),
)

assert_smoke_statements(SMOKE_STATEMENTS)
