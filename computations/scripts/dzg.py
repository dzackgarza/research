import random
from typing import TYPE_CHECKING

from sage.arith.misc import prime_range
from sage.groups.affine_gps.affine_group import AffineGroup
from sage.groups.group import Group
from sage.groups.matrix_gps.finitely_generated import MatrixGroup
from sage.groups.matrix_gps.finitely_generated_gap import FinitelyGeneratedMatrixGroup_gap
from sage.groups.perm_gps.permgroup import PermutationGroup, PermutationGroup_generic
from sage.groups.perm_gps.permgroup_named import (
    CyclicPermutationGroup,
    DihedralGroup,
    SymmetricGroup,
)
from sage.interfaces.gap import GapElement
from sage.libs.gap.libgap import libgap
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ

if TYPE_CHECKING:

    def _typed_permutation_group(value: object) -> PermutationGroup_generic: ...
    def _typed_optional_permutation_group(value: object) -> PermutationGroup_generic | None: ...
    def _typed_integer(value: object) -> Integer: ...
else:

    def _typed_permutation_group(value: object) -> object:
        return value

    def _typed_optional_permutation_group(value: object) -> object:
        return value

    def _typed_integer(value: object) -> object:
        return value


# Terminal color codes
COLOR_GREEN = "\033[92m"
COLOR_RED = "\033[91m"
COLOR_YELLOW = "\033[93m"
COLOR_RESET = "\033[0m"


def print_pass(msg: str) -> None:
    print(f"  {COLOR_GREEN}{msg}{COLOR_RESET}")


def print_fail(msg: str) -> None:
    print(f"  {COLOR_RED}{msg}{COLOR_RESET}")


def print_info(msg: str) -> None:
    print(f"  {COLOR_YELLOW}{msg}{COLOR_RESET}")


def C(n: int) -> PermutationGroup_generic:
    return _typed_permutation_group(CyclicPermutationGroup(n))


def S(n: int) -> PermutationGroup_generic:
    return _typed_permutation_group(SymmetricGroup(n))


def D(n: int) -> PermutationGroup_generic:
    return _typed_permutation_group(DihedralGroup(n))


def prod(G: PermutationGroup_generic, H: PermutationGroup_generic) -> PermutationGroup_generic:
    return G.direct_product(H)[0]


def Ga(n: int) -> PermutationGroup_generic:
    Zn = ZZ.quotient(n * ZZ)
    elements = list(Zn)
    perms = []
    for a in elements:
        perm = [elements.index(a + b) + 1 for b in elements]  # +1 for Sage's 1-based indexing
        perms.append(perm)
    return PermutationGroup(perms)


def Gm(n: int) -> PermutationGroup_generic:
    Zn = IntegerModRing(n)
    units = list(Zn.unit_group())
    # Map each unit to its permutation of the set of units
    perms = []
    for u in units:
        perm = [units.index(u * v) + 1 for v in units]  # +1 for Sage's 1-based indexing
        perms.append(perm)
    return PermutationGroup(perms)


def random_prime(N: int) -> Integer:
    return _typed_integer(random.choice(prime_range(2, N + 1)))


def convert_to_permutation_group(G: Group | GapElement) -> PermutationGroup_generic | None:
    if hasattr(G, "as_AbelianGroup"):
        return _typed_optional_permutation_group(G.as_AbelianGroup().permutation_group())
    elif hasattr(G, "permutation_group"):
        return _typed_optional_permutation_group(G.permutation_group())
    elif hasattr(G, "as_permutation_group"):
        return _typed_optional_permutation_group(G.as_permutation_group())
    elif hasattr(G, "as_finitely_presented_group"):
        # G = G.as_finitely_presented_group()
        return None
    elif "GapElement" in str(type(G)):
        return None
    elif hasattr(G, "as_matrix_group"):
        return _typed_optional_permutation_group(G.as_matrix_group().as_permutation_group())
    else:
        raise ValueError("Could not convert group to a permutation group.")


def group_iso(G: Group | GapElement, H: Group | GapElement) -> bool:
    Gp = convert_to_permutation_group(G)
    Hp = convert_to_permutation_group(H)
    assert Gp is not None and Hp is not None, f"group isomorphism requires permutation-group conversions; left={G}, right={H}"
    return Gp.is_isomorphic(Hp)


def compute_gap_automorphism_group(G: GapElement) -> PermutationGroup_generic:
    """Compute the automorphism group of a GAP group G as a Sage permutation group."""
    gapAut = G.AutomorphismGroup()
    perm = gapAut.IsomorphismPermGroup().Image()
    gens = perm.GeneratorsOfGroup().sage()
    Aut = PermutationGroup(gens)
    return Aut


def aut(G: Group | GapElement) -> PermutationGroup_generic:
    """Compute the automorphism group of a group G as a Sage permutation group if possible."""
    try:
        Gp = libgap(G)
        return compute_gap_automorphism_group(Gp)
    except Exception:
        if "GapElement" in str(type(G)):
            return compute_gap_automorphism_group(G)
        elif hasattr(G, "as_matrix_group"):
            G = G.as_matrix_group().as_permutation_group().as_finitely_presented_group()
            return compute_gap_automorphism_group(libgap(G))
        elif hasattr(G, "as_finitely_presented_group"):
            G = G.as_finitely_presented_group()
            return compute_gap_automorphism_group(libgap(G))
        elif hasattr(G, "as_permutation_group"):
            G = G.as_permutation_group().as_finitely_presented_group()
            return compute_gap_automorphism_group(libgap(G))
        elif hasattr(G, "permutation_group"):
            G = G.permutation_group().as_finitely_presented_group()
            return compute_gap_automorphism_group(libgap(G))
        else:
            raise ValueError("Could not convert group to a type with known automorphism computations")


def get_affine_matrix_group(G_affine: AffineGroup) -> FinitelyGeneratedMatrixGroup_gap:
    mats = list(G_affine._GL)  # Iterate over the GL(1,F) group to get its elements
    vecs = list(G_affine.vector_space())  # Iterate over the vector space to get its elements

    elements_as_matrices = []
    for A_gl in mats:
        for b_vec in vecs:
            # Construct an AffineGroupElement using its element_class
            # Then get its matrix representation.
            affine_element = G_affine.element_class(G_affine, A_gl, b_vec, check=False, convert=False)
            elements_as_matrices.append(affine_element.matrix())
    return MatrixGroup(elements_as_matrices)
