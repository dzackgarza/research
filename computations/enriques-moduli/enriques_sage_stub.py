#!/usr/bin/env sage

"""
Enriques Surface Orbit Computation - SageMath Implementation Stub

This script creates the fundamental lattice building blocks and constructs
all test cases from the Dutour Sikirić & Hulek paper using raw Gram matrices
and SageMath's matrix framework for indefinite lattices.

Convention verification: 2U means 2 * U (scaling), not U ⊕ U (direct sum)
"""

from typing import NotRequired, TypedDict

from sage.matrix.constructor import matrix as Matrix
from sage.modules.free_quadratic_module_integer_symmetric import (
    FreeQuadraticModule_integer_symmetric,
    IntegralLattice,
)
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ


class _LatticeProperties(TypedDict):
    dimension: Integer
    rank: Integer
    signature: tuple[int, int]
    zero_eigenvalues: int
    gram_matrix_rank: int
    is_definite: bool
    is_indefinite: bool
    signature_matches: NotRequired[bool]


class _TestCaseResult(TypedDict):
    k_dimension: int
    lattice: NotRequired[FreeQuadraticModule_integer_symmetric]
    verification: NotRequired[_LatticeProperties]
    error: NotRequired[str]


def classical_lattice(name: str) -> FreeQuadraticModule_integer_symmetric:
    """
    Build classical lattices matching the GAP convention from common.g
    
    Args:
        name (str): Lattice name like "U", "E8", "E7", "E6", "A2", "D4", etc.
        
    Returns:
        IntegralLattice: The corresponding lattice
    """
    if name == "U":
        # Hyperbolic plane [[0,1],[1,0]]
        gram_matrix = Matrix(ZZ, [[0, 1], [1, 0]])
        hyperbolic_lattice = IntegralLattice(gram_matrix)
        return hyperbolic_lattice
    
    elif name == "E8":
        # E8 root lattice from common.g lines 301-305
        gram_matrix = Matrix(ZZ, [
            [2, 0, 0, 0, 0, 0, 1, 0],
            [0, 2, -1, 0, -1, 1, 0, 1],
            [0, -1, 2, 1, 0, 0, 0, -1],
            [0, 0, 1, 2, 0, 0, 1, -1],
            [0, -1, 0, 0, 2, -1, 1, -1],
            [0, 1, 0, 0, -1, 2, 0, 0],
            [1, 0, 0, 1, 1, 0, 2, -1],
            [0, 1, -1, -1, -1, 0, -1, 2]
        ])
        e8_lattice = IntegralLattice(gram_matrix)
        return e8_lattice
    
    elif name == "E7":
        # E7 root lattice from common.g lines 295-299
        gram_matrix = Matrix(ZZ, [
            [4, 3, 2, 3, 1, 1, 1],
            [3, 4, 3, 3, 1, 1, 1],
            [2, 3, 4, 3, 2, 2, 1],
            [3, 3, 3, 4, 2, 1, 2],
            [1, 1, 2, 2, 2, 1, 1],
            [1, 1, 2, 1, 1, 2, 0],
            [1, 1, 1, 2, 1, 0, 2]
        ])
        e7_lattice = IntegralLattice(gram_matrix)
        return e7_lattice
    
    elif name == "E6":
        # E6 root lattice from common.g lines 290-293
        gram_matrix = Matrix(ZZ, [
            [2, 1, 1, 0, 1, 1],
            [1, 4, 1, 1, 1, 3],
            [1, 1, 2, 1, 1, 1],
            [0, 1, 1, 2, 1, 2],
            [1, 1, 1, 1, 2, 2],
            [1, 3, 1, 2, 2, 4]
        ])
        e6_lattice = IntegralLattice(gram_matrix)
        return e6_lattice
    
    elif name.startswith("A") and name[1:].isdigit():
        # A_n root lattices from common.g lines 240-255
        n = int(name[1:])
        gram_matrix = Matrix(QQ, n, n)
        
        # Diagonal entries are 2
        for i in range(n):
            gram_matrix[i, i] = 2
        
        # Off-diagonal entries are -1 for adjacent nodes
        for i in range(n - 1):
            gram_matrix[i, i + 1] = -1
            gram_matrix[i + 1, i] = -1
            
        a_lattice = IntegralLattice(gram_matrix)
        return a_lattice
    
    elif name.startswith("D") and name[1:].isdigit():
        # D_n root lattices from common.g lines 257-277
        n = int(name[1:])
        gram_matrix = Matrix(QQ, n, n)
        
        # Diagonal entries are 2
        for i in range(n):
            gram_matrix[i, i] = 2
        
        # D_n structure: edges (1,3), (2,3), and linear chain from 3 onwards
        edges = [(0, 2), (1, 2)]  # 0-indexed: (1,3) and (2,3)
        for i in range(3, n):     # Linear chain from node 4 onwards
            edges.append((i - 1, i))
        
        # Set off-diagonal entries
        for i, j in edges:
            gram_matrix[i, j] = -1
            gram_matrix[j, i] = -1
            
        d_lattice = IntegralLattice(gram_matrix)
        return d_lattice
    
    else:
        raise ValueError(f"Unknown lattice name: {name}")


def scaled_lattice(
    lattice: FreeQuadraticModule_integer_symmetric, scale_factor: int
) -> FreeQuadraticModule_integer_symmetric:
    """
    Create a scaled version of a lattice (like 2U, 2E8, etc.)
    
    Args:
        lattice (IntegralLattice): Base lattice
        scale_factor (int): Scaling factor
        
    Returns:
        IntegralLattice: Scaled lattice with Gram matrix multiplied by scale_factor
    """
    scaled_gram = scale_factor * lattice.gram_matrix()
    scaled_lattice = IntegralLattice(scaled_gram)
    return scaled_lattice


def parse_lattice_spec(spec_string: str) -> FreeQuadraticModule_integer_symmetric:
    """
    Parse a lattice specification string like "2U", "2E8", "A3", etc.
    
    Args:
        spec_string (str): Specification like "U", "2U", "E8", "2E8", "A3", etc.
        
    Returns:
        IntegralLattice: The corresponding lattice
    """
    if spec_string[0].isdigit():
        # Extract scale factor and base lattice name
        scale_factor = int(spec_string[0])
        base_name = spec_string[1:]
        base_lattice = classical_lattice(base_name)
        return scaled_lattice(base_lattice, scale_factor)
    else:
        # No scaling, just the base lattice
        return classical_lattice(spec_string)


def build_lattice_from_spec(spec_list: list[str]) -> FreeQuadraticModule_integer_symmetric:
    """
    Build lattice from specification list using direct sum.
    
    This matches the GetGramMatrixFromList function in common.g
    
    Args:
        spec_list (list): List of lattice specifications like ["U", "2U", "2E8"]
        
    Returns:
        IntegralLattice: Direct sum of the specified lattices
    """
    if len(spec_list) == 0:
        raise ValueError("Empty specification list")
    
    if len(spec_list) == 1:
        return parse_lattice_spec(spec_list[0])
    
    # Build direct sum by concatenating Gram matrices block-diagonally
    lattices = [parse_lattice_spec(spec) for spec in spec_list]
    gram_matrices = [L.gram_matrix() for L in lattices]
    
    # Calculate total dimension
    total_dim = sum(M.nrows() for M in gram_matrices)
    
    # Create block diagonal matrix
    combined_gram = Matrix(QQ, total_dim, total_dim)
    row_offset = 0
    
    for gram_matrix in gram_matrices:
        dim = gram_matrix.nrows()
        for i in range(dim):
            for j in range(dim):
                combined_gram[row_offset + i, row_offset + j] = gram_matrix[i, j]
        row_offset += dim
    
    lattice = IntegralLattice(combined_gram)
    return lattice


def verify_lattice_properties(
    lattice: FreeQuadraticModule_integer_symmetric,
    expected_signature: tuple[int, int] | None = None,
) -> _LatticeProperties:
    """
    Verify basic properties of a lattice
    
    Args:
        lattice (IntegralLattice): Lattice to verify
        expected_signature (tuple): Expected (positive, negative) signature
        
    Returns:
        dict: Verification results
    """
    gram = lattice.gram_matrix()
    positive, negative = lattice.signature_pair()
    zero = gram.nrows() - positive - negative
    
    result: _LatticeProperties = {
        'dimension': lattice.dimension(),
        'rank': lattice.rank(),
        'signature': (positive, negative),
        'zero_eigenvalues': zero,
        'gram_matrix_rank': gram.rank(),
        'is_definite': negative == 0 or positive == 0,
        'is_indefinite': positive > 0 and negative > 0
    }
    
    if expected_signature is not None:
        result['signature_matches'] = result['signature'] == expected_signature
    
    return result


# Test cases from AllTests.g lines 164-169
TEST_CASES: list[tuple[list[str], int]] = [
    (["U", "2U"], 2),                    # Basic hyperbolic case
    (["U", "2U", "A2"], 2),              # With A₂ root lattice  
    (["U", "2U", "A3"], 2),              # With A₃ root lattice
    (["U", "2U", "A2", "A2"], 2),        # Multiple root lattices
    (["U", "U", "E7"], 2),               # E₇ case
    (["U", "2U", "2E8"], 2),             # Enriques case (main result)
]


def build_all_test_case_lattices() -> dict[tuple[str, ...], _TestCaseResult]:
    """
    Build all test case lattices and verify their properties
    
    Returns:
        dict: Dictionary mapping spec_list to (lattice, verification_info)
    """
    results: dict[tuple[str, ...], _TestCaseResult] = {}
    
    print("Building and verifying all test case lattices...")
    print("=" * 50)
    
    for spec_list, k_dim in TEST_CASES:
        spec_str = " ⊕ ".join(spec_list)
        print(f"\nBuilding: {spec_str}")
        
        try:
            lattice = build_lattice_from_spec(spec_list)
            verification = verify_lattice_properties(lattice)
            
            print(f"  Dimension: {verification['dimension']}")
            print(f"  Rank: {verification['rank']}")
            print(f"  Signature: {verification['signature']}")
            print(f"  Indefinite: {verification['is_indefinite']}")
            
            # Store results
            results[tuple(spec_list)] = {
                'lattice': lattice,
                'verification': verification,
                'k_dimension': k_dim
            }
            
        except Exception as e:
            print(f"  ERROR: {e}")
            results[tuple(spec_list)] = {
                'error': str(e),
                'k_dimension': k_dim
            }
    
    return results


def demonstrate_basic_usage() -> None:
    """
    Demonstrate basic usage of the lattice construction functions
    """
    print("\n" + "=" * 60)
    print("DEMONSTRATION: Basic Lattice Construction")
    print("=" * 60)
    
    # Individual lattices
    print("\n1. Individual Classical Lattices:")
    print("-" * 35)
    
    U = classical_lattice("U")
    print("U (hyperbolic plane):")
    print(f"  Gram matrix: {U.gram_matrix()}")
    print(f"  Signature: {verify_lattice_properties(U)['signature']}")
    
    E8 = classical_lattice("E8")
    print("\nE8 root lattice:")
    print(f"  Dimension: {E8.dimension()}")
    print(f"  Signature: {verify_lattice_properties(E8)['signature']}")
    
    A2 = classical_lattice("A2")
    print("\nA2 root lattice:")
    print(f"  Gram matrix: {A2.gram_matrix()}")
    print(f"  Signature: {verify_lattice_properties(A2)['signature']}")
    
    # Scaled lattices
    print("\n2. Scaled Lattices:")
    print("-" * 20)
    
    U2 = parse_lattice_spec("2U")
    print("2U (scaled hyperbolic plane):")
    print(f"  Gram matrix: {U2.gram_matrix()}")
    
    E8_scaled = parse_lattice_spec("2E8")
    print("\n2E8 (scaled E8):")
    print(f"  Dimension: {E8_scaled.dimension()}")
    print(f"  First diagonal entry: {E8_scaled.gram_matrix()[0,0]}")
    
    # Direct sums
    print("\n3. Direct Sum Construction:")
    print("-" * 30)
    
    simple_case = build_lattice_from_spec(["U", "A2"])
    verification = verify_lattice_properties(simple_case)
    print("U ⊕ A2:")
    print(f"  Dimension: {verification['dimension']}")
    print(f"  Signature: {verification['signature']}")
    
    # Enriques lattice
    print("\n4. Enriques Lattice (Main Target):")
    print("-" * 35)
    
    enriques = build_lattice_from_spec(["U", "2U", "2E8"])
    enriques_verification = verify_lattice_properties(enriques, expected_signature=(2, 18))
    print("U ⊕ 2U ⊕ 2E8:")
    print(f"  Dimension: {enriques_verification['dimension']}")
    print(f"  Signature: {enriques_verification['signature']}")
    print(f"  Expected signature (2,18): {enriques_verification['signature_matches']}")
    print(f"  Is indefinite: {enriques_verification['is_indefinite']}")


if __name__ == "__main__":
    # Run demonstration
    demonstrate_basic_usage()
    
    # Build all test cases
    print("\n" + "=" * 60)
    print("BUILDING ALL TEST CASES")
    print("=" * 60)
    
    test_results = build_all_test_case_lattices()
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    successful = sum(1 for result in test_results.values() if 'lattice' in result)
    failed = len(test_results) - successful
    
    print(f"Successfully built: {successful}/{len(test_results)} lattices")
    if failed > 0:
        print(f"Failed to build: {failed} lattices")
        for spec, result in test_results.items():
            if 'error' in result:
                print(f"  {' ⊕ '.join(spec)}: {result['error']}")
    
    print("\nAll test case lattices ready for orbit computation!")
