import random

from sage.all import *
from sage.all import PermutationGroup, prime_range
from sage.groups.perm_gps.permgroup import PermutationGroup
from sage.groups.perm_gps.permgroup_named import DihedralGroup, SymmetricGroup
from sage.libs.gap.libgap import libgap
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing

# Terminal color codes
COLOR_GREEN = "\033[92m"
COLOR_RED = "\033[91m"
COLOR_YELLOW = "\033[93m"
COLOR_RESET = "\033[0m"

def print_pass(msg):
    print(f"  {COLOR_GREEN}{msg}{COLOR_RESET}")

def print_fail(msg):
    print(f"  {COLOR_RED}{msg}{COLOR_RESET}")

def print_info(msg):
    print(f"  {COLOR_YELLOW}{msg}{COLOR_RESET}")


def C(n):
    return CyclicPermutationGroup(n)

def S(n):
    return SymmetricGroup(n)

def D(n):
    return DihedralGroup(n)

def prod(G, H):
    return G.direct_product(H)[0]

def Ga(n):
    Zn = ZZ.quotient(n*ZZ)
    elements = list(Zn)
    perms = []
    for a in elements:
        perm = [elements.index(a + b) + 1 for b in elements]  # +1 for Sage's 1-based indexing
        perms.append(perm)
    return PermutationGroup(perms)

def Gm(n):
    Zn = IntegerModRing(n)
    units = list(Zn.unit_group())
    # Map each unit to its permutation of the set of units
    perms = []
    for u in units:
        perm = [units.index(u*v) + 1 for v in units]  # +1 for Sage's 1-based indexing
        perms.append(perm)
    return PermutationGroup(perms)

def random_prime(N):
    return random.choice( prime_range(2, N + 1))

def convert_to_permutation_group(G):
    if hasattr(G, "as_AbelianGroup"):
        G = G.as_AbelianGroup()
    elif hasattr(G, "permutation_group"):
        return G.permutation_group()
    elif hasattr(G, "as_permutation_group"):
        return G.as_permutation_group()
    elif hasattr(G, "as_finitely_presented_group"):
        #G = G.as_finitely_presented_group()
        return None
    elif "GapElement" in str(type(G)):
        return None
    elif hasattr(G, 'as_matrix_group'):
        return G.as_matrix_group().as_permutation_group()
    else:
        raise ValueError("Could not convert group to a permutation group.")


def group_iso(G, H):
    Gp = convert_to_permutation_group(G)
    Hp = convert_to_permutation_group(H)
    return Gp.is_isomorphic(Hp)
    

def compute_gap_automorphism_group(G):
    """Compute the automorphism group of a GAP group G as a Sage permutation group."""
    gapAut = G.AutomorphismGroup()
    perm = gapAut.IsomorphismPermGroup().Image()
    gens = perm.GeneratorsOfGroup().sage()
    Aut = PermutationGroup(gens)
    return Aut

def aut(G):
    """Compute the automorphism group of a group G as a Sage permutation group if possible."""
    try:
        Gp = libgap(G)
        return compute_gap_automorphism_group(Gp)
    except Exception:
        if "GapElement" in str(type(G)):
            return compute_gap_automorphism_group(G)
        elif hasattr(G, 'as_matrix_group'):
            G = G.as_matrix_group().as_permutation_group().as_finitely_presented_group()
            return compute_gap_automorphism_group(libgap(G))
        elif hasattr(G, 'as_finitely_presented_group'):
            G = G.as_finitely_presented_group()
            return compute_gap_automorphism_group(libgap(G))
        elif hasattr(G, 'as_permutation_group'):
            G = G.as_permutation_group().as_finitely_presented_group()
            return compute_gap_automorphism_group(libgap(G))
        elif hasattr(G, 'permutation_group'):
            G = G.permutation_group().as_finitely_presented_group()
            return compute_gap_automorphism_group(libgap(G))
        else:
            raise ValueError("Could not convert group to a type with known automorphism computations")

def get_affine_matrix_group(G_affine):
    mats = list(G_affine._GL) # Iterate over the GL(1,F) group to get its elements
    vecs = list(G_affine.vector_space()) # Iterate over the vector space to get its elements

    elements_as_matrices = []
    for A_gl in mats:
        for b_vec in vecs:
            # Construct an AffineGroupElement using its element_class
            # Then get its matrix representation.
            affine_element = G_affine.element_class(G_affine, A_gl, b_vec, check=False, convert=False)
            elements_as_matrices.append(affine_element.matrix())
    return MatrixGroup(elements_as_matrices)
