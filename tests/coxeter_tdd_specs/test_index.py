"""
Master Test Index for Coxeter Test Suite

This file provides a comprehensive index of all tests in the suite,
organized by mathematical content and implementation status.

Run this file to see the current state of the test suite.
"""

import sys
import os
from pathlib import Path


def analyze_test_file(filepath):
    """Analyze a test file and extract information."""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Count test methods
        test_methods = content.count('def test_')
        
        # Count test classes  
        test_classes = content.count('class Test')
        
        # Check for markers
        markers = []
        for marker in ['@pytest.mark.tdd', '@pytest.mark.verification', '@pytest.mark.integration']:
            if marker in content:
                markers.append(marker.split('.')[-1])
        
        # Get docstring description
        lines = content.split('\n')
        docstring_start = None
        for i, line in enumerate(lines):
            if '"""' in line and 'Test' in line:
                docstring_start = i
                break
        
        description = "No description"
        if docstring_start is not None:
            for i in range(docstring_start + 1, min(docstring_start + 10, len(lines))):
                line = lines[i].strip()
                if line and not line.startswith('"""') and not line.startswith('This file'):
                    description = line
                    break
        
        return {
            'test_methods': test_methods,
            'test_classes': test_classes, 
            'markers': markers,
            'description': description
        }
    except Exception as e:
        return {
            'test_methods': 0,
            'test_classes': 0,
            'markers': [],
            'description': f"Error reading file: {e}"
        }


def generate_test_index():
    """Generate comprehensive test index."""
    base_path = Path(__file__).parent
    
    print("=" * 80)
    print("COXETER GROUP TEST SUITE INDEX")  
    print("=" * 80)
    print()
    
    # Organize by category
    categories = {
        "Core Theory": {
            "path": "core_theory/",
            "description": "Fundamental mathematical objects and properties"
        },
        "Group Theory": {
            "path": "group_theory/", 
            "description": "Advanced group-theoretic properties"
        },
        "Computational Theory": {
            "path": "computational_theory/",
            "description": "Algorithmic and computational aspects"
        },
        "Specific Examples": {
            "path": "specific_examples/",
            "description": "Concrete examples from mathematical literature"
        },
        "Verification": {
            "path": "verification/",
            "description": "Cross-validation with Sage implementations"
        },
        "Integration": {
            "path": "integration/",
            "description": "Integration and system tests"
        }
    }
    
    total_files = 0
    total_methods = 0
    total_classes = 0
    
    for category_name, category_info in categories.items():
        category_path = base_path / category_info["path"]
        
        print(f"{category_name.upper()}")
        print("-" * len(category_name))
        print(f"Description: {category_info['description']}")
        print()
        
        if not category_path.exists():
            print("  [Directory not found]")
            print()
            continue
            
        test_files = sorted(category_path.glob("test_*.py"))
        
        if not test_files:
            print("  [No test files]")
            print()
            continue
            
        category_methods = 0
        category_classes = 0
        
        for test_file in test_files:
            info = analyze_test_file(test_file)
            
            print(f"  📁 {test_file.name}")
            print(f"     {info['description']}")
            print(f"     Classes: {info['test_classes']}, Methods: {info['test_methods']}")
            
            if info['markers']:
                print(f"     Markers: {', '.join(info['markers'])}")
            
            print()
            
            category_methods += info['test_methods']
            category_classes += info['test_classes']
            total_files += 1
            
        print(f"  📊 Category totals: {len(test_files)} files, {category_classes} classes, {category_methods} methods")
        print()
        
        total_methods += category_methods
        total_classes += category_classes
    
    # Overall summary
    print("=" * 80)
    print("OVERALL SUMMARY")
    print("=" * 80)
    print(f"Total test files: {total_files}")
    print(f"Total test classes: {total_classes}")
    print(f"Total test methods: {total_methods}")
    print()
    
    # Mathematical coverage
    print("MATHEMATICAL COVERAGE")
    print("-" * 20)
    
    coverage_areas = [
        "✓ Finite Coxeter Groups (A, B, C, D, E, F, G, H, I series)",
        "✓ Affine Coxeter Groups (Extended Dynkin diagrams)", 
        "✓ Hyperbolic Coxeter Groups (Indefinite lattices)",
        "✓ Root Systems (Crystallographic and non-crystallographic)",
        "✓ Weyl Groups (Geometric and algebraic properties)",
        "✓ Dynkin Diagrams (Classification and invariants)",
        "✓ Gram Matrices (Construction and properties)",
        "✓ Group Theory (Homology, orders, automorphisms)",
        "✓ Computational Theory (Algorithms, complexity, decidability)",
        "✓ Literature Examples (Wikiwand, Wikipedia sources)"
    ]
    
    for area in coverage_areas:
        print(f"  {area}")
    
    print()
    
    # Implementation status
    print("IMPLEMENTATION STATUS")
    print("-" * 20)
    print("🔴 Not Started: All tests currently fail (TDD approach)")
    print("🟡 In Progress: Implementation will begin after test completion")
    print("🟢 Complete: Cross-validation with Sage will verify correctness")
    print()
    
    # Usage instructions
    print("USAGE INSTRUCTIONS")
    print("-" * 17)
    print("Run specific categories:")
    print("  python run_tests.py --category core")
    print("  python run_tests.py --category group")
    print("  python run_tests.py --category computational")
    print()
    print("Run by mathematical topic:")
    print("  python run_tests.py --topic weyl_groups")
    print("  python run_tests.py --topic dynkin_diagrams")
    print("  python run_tests.py --topic hyperbolic")
    print()
    print("Run by test type:")
    print("  python run_tests.py --type tdd")
    print("  python run_tests.py --type verification")
    print("  python run_tests.py --type literature")
    print()


if __name__ == "__main__":
    generate_test_index()