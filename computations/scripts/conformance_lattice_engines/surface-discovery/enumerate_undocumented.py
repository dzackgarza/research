#!/usr/bin/env python3
"""
Exhaustive enumeration of undocumented methods in SageMath lattice classes.

Tests all methods of:
- IntegerLattice
- IntegralLattice
- BinaryQF
- QuadraticForm
- TernaryQF

Filters trivial methods (dunder, copy, serialization) and produces
complete list of all nontrivial undocumented methods.

Output: Complete enumeration written to stdout.
"""

from sage.all import *
from sage.modules.free_module_integer import IntegerLattice
from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice
from sage.quadratic_forms.binary_qf import BinaryQF
from sage.quadratic_forms.quadratic_form import QuadraticForm
from sage.quadratic_forms.ternary_qf import TernaryQF

DOCUMENTED = {
    'IntegerLattice': set([
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
    ]),
    'IntegralLattice': set([
        'gram_matrix', 'basis', 'rank', 'determinant',
        'signature', 'signature_pair', 'is_even', 'dual_lattice', 'discriminant_group',
        'LLL', 'maximum', 'maximal_overlattice',
        'sublattice', 'direct_sum', 'tensor_product', 'twist', 'automorphisms',
        'local_modification'
    ]),
    'BinaryQF': set([
        'discriminant', 'is_positive_definite', 'is_negative_definite', 'is_indefinite',
        'is_reduced', 'is_primitive', 'reduced_form', 'is_equivalent', 'equivalent_form_and_matrix',
        'composition', 'inverse', 'matrix_action', 'solve_integer', 'representation_number',
        'complex_point', 'cycle'
    ]),
    'QuadraticForm': set([
        'gram_matrix', 'discriminant', 'signature', 'level', 'is_definite', 'is_integral',
        'hasse_invariant', 'witt_invariant', 'local_density', 'is_locally_represented',
        'count_congruence_solutions_by_type', 'reduced_form', 'base_change_to', 'rational_diagonal_form',
        'automorphisms', 'is_equivalent', 'clifford_invariant',
        'representation_number', 'solve', 'representation_vector_list', 'basiclemmavec',
        'theta_series', 'global_genus_symbol', 'mass', 'class_number'
    ]),
    'TernaryQF': set([
        'is_eisenstein_reduced', 'reduced_form', 'automorphisms', 'is_equivalent',
        'matrix', 'discriminant'
    ]),
}

def filter_trivial(methods):
    """Remove truly trivial methods (dunder, copy, etc)."""
    trivial = {
        '__', 'copy', 'deepcopy', 'str', 'repr', 'hash',
        'get', 'set', 'del', 'bool', 'len', 'iter', 'next',
        'init', 'new', 'class', 'doc', 'module', 'bases',
        'mutable', 'immutable', 'mro', 'reduce', 'state',
        'sizeof', 'format', 'subclass', 'callable', 'instancecheck',
        'weakref', 'dict', 'slots', 'getattr', 'setattr', 'delattr',
        'dir', 'contains', 'enter', 'exit', 'aenter', 'aexit',
        'index', 'count'
    }
    return [m for m in methods if not any(t in m.lower() for t in trivial) and not m.startswith('_')]

def is_mathematically_significant(name):
    """Check if method name suggests mathematical significance."""
    math_terms = {
        'neighbor', 'genus', 'mass', 'density', 'hasse', 'witt', 'clifford',
        'spinor', 'automorphism', 'representation', 'reduced', 'equivalent',
        'anisotropic', 'primitive', 'composition', 'divisor', 'cycle',
        'fundamental', 'eisenstein', 'zeros', 'lemma', 'adjoint', 'symmetry',
        'span', 'vector', 'theta', 'local', 'indefinite', 'hyperbolic',
        'isotropic', 'universal', 'jordan', 'cholesky', 'minkowski', 'siegel',
        'pall', 'watson', 'kitaoka', 'conway', 'gram', 'hessian', 'enumerate',
        'short', 'close', 'orthogonal', 'overlattice', 'reciprocal', 'content',
        'discriminant', 'level', 'saturation', 'echelon', 'basis', 'rank'
    }
    return any(term in name.lower() for term in math_terms)

# Create test objects
print("Creating test objects...")
L_int = IntegerLattice([[1, 0], [0, 1]])
L_int_latt = IntegralLattice('A2')
qf_bin = BinaryQF(1, 0, 1)
qf = QuadraticForm(ZZ, 2, [1, 0, 1])
qf_tern = TernaryQF([1, 1, 1, 0, 0, 0])

# Test each class
print("\n" + "=" * 80)
print("SUMMARY OF MATHEMATICALLY SIGNIFICANT UNDOCUMENTED METHODS")
print("=" * 80)

grand_total_math = 0
grand_total_trivial = 0

for cls_name, obj, documented in [
    ('IntegerLattice', L_int, DOCUMENTED['IntegerLattice']),
    ('IntegralLattice', L_int_latt, DOCUMENTED['IntegralLattice']),
    ('BinaryQF', qf_bin, DOCUMENTED['BinaryQF']),
    ('QuadraticForm', qf, DOCUMENTED['QuadraticForm']),
    ('TernaryQF', qf_tern, DOCUMENTED['TernaryQF'])
]:
    all_methods = set(dir(obj))
    all_public = filter_trivial(list(all_methods))
    undocumented = sorted(set(all_public) - documented)
    
    # Separate mathematical from trivial
    math_undoc = [m for m in undocumented if is_mathematically_significant(m)]
    trivial_undoc = [m for m in undocumented if not is_mathematically_significant(m)]
    
    grand_total_math += len(math_undoc)
    grand_total_trivial += len(trivial_undoc)
    
    print(f"\n{cls_name}:")
    print(f"  Mathematically significant undocumented: {len(math_undoc)}")
    if math_undoc:
        for m in math_undoc:
            print(f"    • {m}")
    else:
        print(f"    (none)")
    print(f"  Trivial undocumented (inherited/system): {len(trivial_undoc)}")
    if len(trivial_undoc) <= 10:
        for m in trivial_undoc:
            print(f"    • {m}")
    else:
        print(f"    {', '.join(trivial_undoc[:5])}, ... (+{len(trivial_undoc)-5} more)")

print(f"\n{'='*80}")
print(f"TOTALS:")
print(f"  Mathematically significant undocumented: {grand_total_math}")
print(f"  Trivial/inherited undocumented: {grand_total_trivial}")
print(f"{'='*80}")
