#!/usr/bin/env sage

from dzg import *

# Consolidated test cases - all unique test scenarios in one list (excluding Cyclic, Symmetric, and Dihedral group tests)
test_cases = [
    {
        'name': 'Trivial Group',
        'group': PermutationGroup([]),
        'expected_aut': PermutationGroup([]),
        'citation': 'Aut(G) is trivial if G is trivial.',
    },
    {
        'name': 'Cyclic Group C8',
        'group': CyclicPermutationGroup(8),
        'expected_aut': KleinFourGroup(),
        'citation': 'Aut(C_8) ≅ C_2 x C_2. [Wikipedia]',
    },
    {
        'name': 'Quaternion Group Q8',
        'group': QuaternionGroup(),
        'expected_aut': SymmetricGroup(4),
        'citation': 'Aut(Q_8) ≅ S_4. [Wikipedia]',
    },
    {
        'name': 'Finitely Presented Group (C2 x C2)',
        'group': FreeGroup(['a', 'b']) / [
            FreeGroup(['a', 'b']).gen(0)**2,
            FreeGroup(['a', 'b']).gen(1)**2,
            FreeGroup(['a', 'b']).gen(0) * FreeGroup(['a', 'b']).gen(1) *
            FreeGroup(['a', 'b']).gen(0)**-1 * FreeGroup(['a', 'b']).gen(1)**-1
        ],
        'expected_aut': S(3),
        'citation': 'Aut(C_2 x C_2) ≅ S_3. [Groupprops]',
    },
    {
        'name': 'Finitely Presented Group (S3)',
        'group': SymmetricGroup(3).as_finitely_presented_group(),
        'expected_aut': S(3),
        'citation': 'Aut(S_3) ≅ S_3. [Standard result]',
    },
    {
        'name': 'Matrix Group GL(2,2)',
        'group': GL(2,2),
        'expected_aut': S(3),
        'citation': 'GL(2,2) ≅ S_3, so Aut(GL(2,2)) ≅ S_3. [Wikipedia]',
    },
    {
        'name': 'Abelian Group C2 x C3',
        'group': AbelianGroup([2, 3]),
        'expected_aut': C(2),
        'citation': 'Aut(C_2 x C_3) ≅ C_2. [Standard result]',
    },
    {
        'name': 'Abelian Group C2 x C4',
        'group': AbelianGroupGap([2,4]),
        'expected_aut': D(4),
        'expected_order': 8,
        'citation': 'Order of Aut(C_2 x C_4) is 8. [Dummit & Foote, Ex. 6, p.148]',
    },
    {
        'name': 'Mathieu Group M12',
        'group': MathieuGroup(12),
        'expected_aut': None,
        'expected_order': 190080,
        'citation': 'Aut(M12) has order 190080. [Atlas, Wikipedia]',
    },
]


# All Cyclic group tests in one place
cyclic_test_cases = [
    {
        'name': f'Cyclic Group C{n}',
        'group': C(n),
        'expected_aut': Gm(n),
        'citation': f'Aut(C_{n}) ≅ (Z/{n}Z)^* [Standard result]',
    }
    for n in [2, 3, 4, 5, 6, 7, 9, 10, 12]
]

# All Symmetric group tests for n >= 3 in one place
symmetric_test_cases = [
    {
        'name': f'Symmetric Group S{n}',
        'group': S(n),
        'expected_aut': S(n),
        'citation': f'Aut(S_{n}) ≅ S_{n} for n ≥ 3, n ≠ 6. [Wikipedia]',
    }
    for n in [3, 4, 5, 7, 8, 9, 10, 12]
]

# All Dihedral group tests in one place (now including D5)
dihedral_test_cases = [
    {
        'name': f'Dihedral Group D{n}',
        'group': DihedralGroup(n),
        'expected_aut': C(n).holomorph(),
        'citation': f'Aut(D_{n}) ≅ Hol(C_{n}). [Standard result]',
    }
    for n in [3, 5, 7, 9, 11, 13]  # odd n values, now including D5
]

def run_all_automorphism_tests():
    """Run the comprehensive test suite for automorphism group computations."""
    print_info("=== Running Comprehensive Automorphism Group Tests ===\n")
    
    passed = 0
    
    for test_case in test_cases + cyclic_test_cases + symmetric_test_cases + dihedral_test_cases:
        name = test_case['name']
        group = test_case['group']
        expected_aut = test_case.get('expected_aut', None)
        expected_order = test_case.get('expected_order', None)
        citation = test_case.get('citation', 'No citation provided.')
        
        print_info(f"Testing: {name}")
        
        computed_aut = aut(group)
        if expected_aut is not None:
            assert computed_aut.is_isomorphic(expected_aut), print_fail(f"✗ FAIL: Aut({name}) not isomorphic to expected group") or False
            print_pass(f"✓ PASS: Aut({name}) ≅ {expected_aut}")
            passed += 1
        elif expected_order is not None:
            assert computed_aut.order() == expected_order, print_fail(f"✗ FAIL: |Aut({name})|: Expected {expected_order}, got {computed_aut.order()}") or False
            print_pass(f"✓ PASS: |Aut({name})| = {computed_aut.order()}")
            passed += 1
        else:
            print_info(f"✓ INFO: |Aut({name})| = {computed_aut.order()}")
            passed += 1
        print_info(f"Reference: {citation}")
        print()
    
    print_info(f"=== Test Summary ===")
    print_pass(f"Passed: {passed}")
    print_info(f"Total:  {passed}")

def run_random_automorphism_tests(num_tests=20):
    """Run tests for random cyclic groups C_n."""
    print_info(f"=== Running {num_tests} Random Cyclic Group Tests ===\n")
    
    from sage.all import randint
    
    for i in range(num_tests):
        n = randint(2, 10)
        print_info(f"Testing random cyclic group C_{n}")
        computed_aut = aut(C(n))
        assert computed_aut.is_isomorphic(Gm(n)), print_fail(f"✗ FAIL: Aut(C_{n}) not isomorphic to (Z/{n}Z)*") or False
        assert computed_aut.order() == euler_phi(n), print_fail(f"✗ FAIL: |Aut(C_{n})|: Expected {euler_phi(n)}, got {computed_aut.order()}") or False
        print_pass(f"✓ PASS: Aut(C_{n}) ≅ (Z/{n}Z)*")
    print()

def run_direct_product_tests(num_tests=5):
    """Run tests for direct products of cyclic groups C_n x C_m."""
    print_info(f"=== Running {num_tests} Direct Product Tests ===\n")
        
    for i in range(num_tests):
        n = randint(2, 8)
        m = randint(2, 8)
        print_info(f"Testing C_{n} x C_{m}")
        G = AbelianGroup([n, m])
        computed_aut = aut(G)
        if gcd(n, m) == 1:
            expected_order = euler_phi(n * m)
            assert computed_aut.order() == expected_order, print_fail(f"✗ FAIL: |Aut(C_{n} x C_{m})|: Expected {expected_order}, got {computed_aut.order()}") or False
            print_pass(f"✓ PASS: |Aut(C_{n} x C_{m})| = {computed_aut.order()} (coprime case)")
        else:
            print_info(f"✓ INFO: |Aut(C_{n} x C_{m})| = {computed_aut.order()} (non-coprime case)")
    print()

if __name__ == "__main__":
    run_all_automorphism_tests()
    run_random_automorphism_tests()
    run_direct_product_tests()



