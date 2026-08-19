#!/usr/bin/env python3
"""Test all documented sage methods and discover undocumented ones."""

from sage.all import *
from sage.modules.free_module_integer import IntegerLattice
from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice
from sage.quadratic_forms.binary_qf import BinaryQF
from sage.quadratic_forms.quadratic_form import QuadraticForm
from sage.quadratic_forms.ternary_qf import TernaryQF

def get_all_methods(obj):
    """Get all non-private methods of an object."""
    return [m for m in dir(obj) if not m.startswith('_')]

def is_mathematically_nontrivial(method_name: str) -> bool:
    """Check if method name suggests mathematical nontriviality."""
    trivial_patterns = [
        'help', 'copy', 'deepcopy', 'str', 'repr', 'hash',
        'eq', 'ne', 'lt', 'le', 'gt', 'ge', 'bool', 'len', 'getitem',
        'setitem', 'delitem', 'contains', 'iter', 'next', 'add',
        'sub', 'mul', 'div', 'mod', 'pow', 'neg', 'pos', 'abs',
        'invert', 'and', 'or', 'xor', 'lshift', 'rshift',
        'call', 'init', 'new', 'del', 'reduce', 'setstate', 'getstate',
        'sizeof', 'format', 'subclasshook', 'class', 'module', 'qualname',
        'doc', 'dict', 'weakref', 'reduce_ex', 'dir', 'getattr', 'setattr',
        'delattr', 'isinstance', 'issubclass', 'callable', 'instancecheck',
        'subclasscheck', 'mro', 'bases', 'mutable', 'category',
        'is_immutable', 'set_immutable', 'is_mutable', 'parent', 'element_class'
    ]
    return not any(pattern in method_name.lower() for pattern in trivial_patterns)

def test_integer_lattice():
    """Test IntegerLattice methods."""
    print("=" * 80)
    print("TESTING IntegerLattice")
    print("=" * 80)
    
    documented = [
        'LLL', 'BKZ', 'HKZ', 'update_reduced_basis',
        'shortest_vector', 'closest_vector', 'approximate_closest_vector', 'babai',
        'volume', 'discriminant', 'gaussian_heuristic', 'hadamard_ratio',
        'voronoi_cell', 'voronoi_relevant_vectors',
        'basis', 'echelonized_basis', 'echelonized_basis_matrix', 'basis_matrix',
        'matrix', 'has_user_basis', 'user_to_echelon_matrix',
        'ambient', 'ambient_module', 'ambient_vector_space', 'vector_space',
        'nonembedded_free_module',
        'intersection', 'quotient_module', 'saturation', 'span_of_basis',
        'submodule_with_basis', 'zero_submodule', 'direct_sum',
        'denominator', 'index_in', 'index_in_saturation',
        'vector_space_span', 'vector_space_span_of_basis',
        'change_ring', 'construction', 'lift', 'retract', 
        'linear_combination_of_basis', 'relations',
        'rank', 'dimension', 'degree', 'ngens', 'codimension', 'cardinality',
        'base_ring', 'coordinate_ring', 'inner_product_matrix', 'gram_matrix',
        'is_ambient', 'is_submodule', 'uses_ambient_inner_product',
        'hom'
    ]
    
    L = IntegerLattice([[1, 0], [0, 1]])
    all_methods = get_all_methods(L)
    nontrivial_methods = [m for m in all_methods if is_mathematically_nontrivial(m)]
    
    undocumented = [m for m in nontrivial_methods if m not in documented]
    
    print(f"Total methods: {len(all_methods)}")
    print(f"Nontrivial methods: {len(nontrivial_methods)}")
    print(f"Documented nontrivial methods: {len([m for m in nontrivial_methods if m in documented])}")
    print(f"Undocumented nontrivial methods: {len(undocumented)}")
    print(f"\nUndocumented nontrivial methods:")
    for m in sorted(undocumented):
        print(f"  - {m}")
        try:
            method = getattr(L, m)
            if callable(method):
                print(f"    Signature: {str(method.__doc__)[:100]}")
        except Exception as e:
            print(f"    Error: {e}")

def test_integral_lattice():
    """Test IntegralLattice methods."""
    print("\n" + "=" * 80)
    print("TESTING IntegralLattice")
    print("=" * 80)
    
    documented = [
        'gram_matrix', 'basis', 'rank', 'determinant',
        'signature', 'signature_pair', 'is_even', 'dual_lattice', 'discriminant_group',
        'LLL',
        'maximum', 'maximal_overlattice',
        'sublattice', 'direct_sum', 'tensor_product', 'twist', 'automorphisms',
        'local_modification'
    ]
    
    try:
        L = IntegralLattice(3)
        all_methods = get_all_methods(L)
        nontrivial_methods = [m for m in all_methods if is_mathematically_nontrivial(m)]
        
        undocumented = [m for m in nontrivial_methods if m not in documented]
        
        print(f"Total methods: {len(all_methods)}")
        print(f"Nontrivial methods: {len(nontrivial_methods)}")
        print(f"Documented nontrivial methods: {len([m for m in nontrivial_methods if m in documented])}")
        print(f"Undocumented nontrivial methods: {len(undocumented)}")
        print(f"\nUndocumented nontrivial methods:")
        for m in sorted(undocumented):
            print(f"  - {m}")
            try:
                method = getattr(L, m)
                if callable(method):
                    doc_str = str(method.__doc__ or "")[:100]
                    if doc_str:
                        print(f"    Doc: {doc_str}")
            except Exception as e:
                pass
    except Exception as e:
        print(f"Error testing IntegralLattice: {e}")

def test_binary_qf():
    """Test BinaryQF methods."""
    print("\n" + "=" * 80)
    print("TESTING BinaryQF")
    print("=" * 80)
    
    documented = [
        'discriminant', 'is_positive_definite', 'is_negative_definite', 'is_indefinite',
        'is_reduced', 'is_primitive',
        'reduced_form', 'is_equivalent', 'equivalent_form_and_matrix',
        'composition', 'inverse', 'matrix_action',
        'solve_integer', 'representation_number',
        'complex_point', 'cycle'
    ]
    
    Q = BinaryQF(1, 0, 1)
    all_methods = get_all_methods(Q)
    nontrivial_methods = [m for m in all_methods if is_mathematically_nontrivial(m)]
    
    undocumented = [m for m in nontrivial_methods if m not in documented]
    
    print(f"Total methods: {len(all_methods)}")
    print(f"Nontrivial methods: {len(nontrivial_methods)}")
    print(f"Documented nontrivial methods: {len([m for m in nontrivial_methods if m in documented])}")
    print(f"Undocumented nontrivial methods: {len(undocumented)}")
    print(f"\nUndocumented nontrivial methods:")
    for m in sorted(undocumented):
        print(f"  - {m}")
        try:
            method = getattr(Q, m)
            if callable(method):
                doc_str = str(method.__doc__ or "")[:100]
                if doc_str:
                    print(f"    Doc: {doc_str}")
        except Exception as e:
            pass

def test_quadratic_form():
    """Test QuadraticForm methods."""
    print("\n" + "=" * 80)
    print("TESTING QuadraticForm")
    print("=" * 80)
    
    documented = [
        'gram_matrix', 'discriminant', 'signature', 'level', 'is_definite', 'is_integral',
        'hasse_invariant', 'witt_invariant', 'local_density', 'is_locally_represented',
        'count_congruence_solutions_by_type',
        'reduced_form', 'base_change_to', 'rational_diagonal_form', 'automorphisms',
        'is_equivalent', 'clifford_invariant',
        'representation_number', 'solve', 'representation_vector_list', 'basiclemmavec',
        'theta_series',
        'global_genus_symbol', 'mass', 'class_number'
    ]
    
    Q = QuadraticForm(ZZ, 2, [1, 0, 1])
    all_methods = get_all_methods(Q)
    nontrivial_methods = [m for m in all_methods if is_mathematically_nontrivial(m)]
    
    undocumented = [m for m in nontrivial_methods if m not in documented]
    
    print(f"Total methods: {len(all_methods)}")
    print(f"Nontrivial methods: {len(nontrivial_methods)}")
    print(f"Documented nontrivial methods: {len([m for m in nontrivial_methods if m in documented])}")
    print(f"Undocumented nontrivial methods: {len(undocumented)}")
    print(f"\nUndocumented nontrivial methods:")
    for m in sorted(undocumented):
        print(f"  - {m}")
        try:
            method = getattr(Q, m)
            if callable(method):
                doc_str = str(method.__doc__ or "")[:100]
                if doc_str:
                    print(f"    Doc: {doc_str}")
        except Exception as e:
            pass

def test_ternary_qf():
    """Test TernaryQF methods."""
    print("\n" + "=" * 80)
    print("TESTING TernaryQF")
    print("=" * 80)
    
    documented = [
        'is_eisenstein_reduced', 'reduced_form', 'automorphisms', 'is_equivalent',
        'matrix', 'discriminant'
    ]
    
    try:
        Q = TernaryQF([1, 1, 1, 0, 0, 0])
        all_methods = get_all_methods(Q)
        nontrivial_methods = [m for m in all_methods if is_mathematically_nontrivial(m)]
        
        undocumented = [m for m in nontrivial_methods if m not in documented]
        
        print(f"Total methods: {len(all_methods)}")
        print(f"Nontrivial methods: {len(nontrivial_methods)}")
        print(f"Documented nontrivial methods: {len([m for m in nontrivial_methods if m in documented])}")
        print(f"Undocumented nontrivial methods: {len(undocumented)}")
        print(f"\nUndocumented nontrivial methods:")
        for m in sorted(undocumented):
            print(f"  - {m}")
            try:
                method = getattr(Q, m)
                if callable(method):
                    doc_str = str(method.__doc__ or "")[:100]
                    if doc_str:
                        print(f"    Doc: {doc_str}")
            except Exception as e:
                pass
    except Exception as e:
        print(f"Error testing TernaryQF: {e}")

def test_genus():
    """Test Genus methods."""
    print("\n" + "=" * 80)
    print("TESTING Genus")
    print("=" * 80)
    
    documented = [
        'dimension', 'determinant', 'signature', 'level', 'is_even', 'is_unimodular',
        'local_symbol', 'local_symbols', 'prime_divisors',
        'mass', 'spinor_generators', 'discriminant_form',
        'direct_sum', 'representative'
    ]
    
    try:
        Q = QuadraticForm(ZZ, 2, [1, 0, 1])
        G = Q.global_genus_symbol()
        all_methods = get_all_methods(G)
        nontrivial_methods = [m for m in all_methods if is_mathematically_nontrivial(m)]
        
        undocumented = [m for m in nontrivial_methods if m not in documented]
        
        print(f"Total methods: {len(all_methods)}")
        print(f"Nontrivial methods: {len(nontrivial_methods)}")
        print(f"Documented nontrivial methods: {len([m for m in nontrivial_methods if m in documented])}")
        print(f"Undocumented nontrivial methods: {len(undocumented)}")
        print(f"\nUndocumented nontrivial methods:")
        for m in sorted(undocumented):
            print(f"  - {m}")
            try:
                method = getattr(G, m)
                if callable(method):
                    doc_str = str(method.__doc__ or "")[:100]
                    if doc_str:
                        print(f"    Doc: {doc_str}")
            except Exception as e:
                pass
    except Exception as e:
        print(f"Error testing Genus: {e}")

def main():
    """Run all tests."""
    test_integer_lattice()
    test_integral_lattice()
    test_binary_qf()
    test_quadratic_form()
    test_ternary_qf()
    test_genus()
    
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print("All tested classes checked for undocumented nontrivial methods.")
    print("See output above for detailed results.")

if __name__ == '__main__':
    main()
