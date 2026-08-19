#!/usr/bin/env python3
"""
Coxeter Test Suite Runner

This script provides organized ways to run the comprehensive Coxeter test suite
with different filtering options based on mathematical content, test type, and scope.

Usage:
    python run_tests.py --help                    # Show all options
    python run_tests.py --type unit               # Run unit tests only
    python run_tests.py --type integration        # Run integration tests
    python run_tests.py --type system             # Run system tests  
    python run_tests.py --type sage               # Run Sage verification
    python run_tests.py --type benchmark          # Run performance benchmarks
    python run_tests.py --topic weyl_groups       # Run all Weyl group tests
    python run_tests.py --quick                   # Run fast tests only
"""

import argparse
import subprocess
import sys
import os
from pathlib import Path


def run_pytest_command(args_list):
    """Run pytest with given arguments and return result."""
    cmd = ["python", "-m", "pytest"] + args_list
    print(f"Running: {' '.join(cmd)}")
    return subprocess.run(cmd, cwd=Path(__file__).parent)


def main():
    parser = argparse.ArgumentParser(
        description="Organized test runner for Coxeter test suite",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    # Test types (primary organization)
    parser.add_argument(
        "--type", "-t",
        choices=["unit", "integration", "system", "sage", "benchmark", "all"],
        help="Run tests by type (primary organization)"
    )
    
    # Mathematical topics
    parser.add_argument(
        "--topic",
        choices=[
            "gram_matrices", "root_systems", "weyl_groups", "dynkin_diagrams", "coxeter_groups",
            "hyperbolic", "crystallographic", "homological", "computational", "automatic_groups"
        ],
        help="Run tests by mathematical topic"
    )
    
    # Speed filters
    parser.add_argument(
        "--speed",
        choices=["fast", "medium", "slow", "very_slow", "all"],
        help="Run tests by speed category"
    )
    
    # Coxeter group types
    parser.add_argument(
        "--coxeter-type",
        choices=["finite", "affine", "indefinite", "all"],
        help="Run tests by Coxeter group type"
    )
    
    # Literature sources
    parser.add_argument(
        "--source",
        choices=["wikiwand", "wikipedia", "bourbaki", "literature", "tdd"],
        help="Run tests by source/methodology"
    )
    
    # Execution modes
    parser.add_argument(
        "--quick", "-q",
        action="store_true",
        help="Run only fast tests (exclude slow tests)"
    )
    
    parser.add_argument(
        "--slow",
        action="store_true", 
        help="Include slow/long-running tests"
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose output"
    )
    
    parser.add_argument(
        "--parallel", "-n",
        type=int,
        metavar="N",
        help="Run tests in parallel with N workers (requires pytest-xdist)"
    )
    
    # Coverage
    parser.add_argument(
        "--coverage",
        action="store_true",
        help="Run with coverage reporting (requires pytest-cov)"
    )
    
    # Specific test patterns
    parser.add_argument(
        "--pattern", "-k",
        help="Run tests matching pattern (pytest -k option)"
    )
    
    parser.add_argument(
        "--file", "-f",
        help="Run specific test file"
    )
    
    # Output options
    parser.add_argument(
        "--summary",
        action="store_true",
        help="Show summary of available tests without running"
    )
    
    parser.add_argument(
        "--list-markers",
        action="store_true",  
        help="List all available test markers"
    )
    
    args = parser.parse_args()
    
    if args.summary:
        show_test_summary()
        return
        
    if args.list_markers:
        show_markers()
        return
    
    # Build pytest arguments
    pytest_args = []
    
    # Add verbosity
    if args.verbose:
        pytest_args.append("-v")
    
    # Add parallel execution
    if args.parallel:
        pytest_args.extend(["-n", str(args.parallel)])
    
    # Add coverage
    if args.coverage:
        pytest_args.extend(["--cov=../src", "--cov-report=html", "--cov-report=term"])
    
    # Handle test type selection (primary organization)
    if args.type:
        if args.type == "all":
            pytest_args.append(".")
        else:
            type_map = {
                "unit": "unit/",
                "integration": "integration/",
                "system": "system/",
                "sage": "sage_verification/",
                "benchmark": "benchmarks/"
            }
            pytest_args.append(type_map[args.type])
    
    # Handle topic selection
    if args.topic:
        pytest_args.extend(["-m", args.topic])
    
    # Handle speed selection
    if args.speed and args.speed != "all":
        pytest_args.extend(["-m", args.speed])
    
    # Handle Coxeter group type
    if args.coxeter_type and args.coxeter_type != "all":
        pytest_args.extend(["-m", args.coxeter_type])
    
    # Handle literature source
    if args.source:
        pytest_args.extend(["-m", args.source])
    
    # Handle quick/slow execution
    if args.quick:
        pytest_args.extend(["-m", "fast"])
    elif args.slow:
        pytest_args.extend(["-m", "slow or very_slow"])
    
    # Handle pattern matching
    if args.pattern:
        pytest_args.extend(["-k", args.pattern])
    
    # Handle specific file
    if args.file:
        pytest_args.append(args.file)
    
    # Default to current directory if no specific target
    if not any([args.type, args.file]):
        pytest_args.append(".")
    
    # Run the tests
    result = run_pytest_command(pytest_args)
    sys.exit(result.returncode)


def show_test_summary():
    """Show summary of available test types and files."""
    print("=== Coxeter Test Suite Summary ===\n")
    
    test_types = {
        "Unit Tests": "unit/",
        "Integration Tests": "integration/", 
        "System Tests": "system/",
        "Sage Verification": "sage_verification/",
        "Benchmarks": "benchmarks/"
    }
    
    base_path = Path(__file__).parent
    
    for type_name, type_path in test_types.items():
        full_path = base_path / type_path
        if full_path.exists():
            test_files = list(full_path.glob("test_*.py"))
            print(f"{type_name} ({len(test_files)} files):")
            for test_file in sorted(test_files):
                print(f"  - {test_file.name}")
            print()
    
    print("Run with --type <type> to run specific test types")
    print("Run with --topic <topic> to filter by mathematical content")
    print("Run with --speed <speed> to filter by execution speed")


def show_markers():
    """Show all available pytest markers."""
    print("=== Available Test Markers ===\n")
    
    markers = {
        "Test Types": ["unit", "integration", "system", "sage", "benchmark"],
        "Speed Categories": ["fast", "medium", "slow", "very_slow"],
        "Mathematical Content": [
            "gram_matrices", "root_systems", "weyl_groups", "dynkin_diagrams", "coxeter_groups",
            "hyperbolic", "crystallographic", "homological", "computational", "automatic_groups"
        ],
        "Coxeter Types": ["finite", "affine", "indefinite"],
        "Sources/Methodology": ["wikiwand", "wikipedia", "bourbaki", "literature", "tdd"],
        "Implementation Status": ["implemented", "not_implemented", "regression"],
        "Complexity": ["simple", "complex", "edge_case"]
    }
    
    for category, marker_list in markers.items():
        print(f"{category}:")
        for marker in marker_list:
            print(f"  - {marker}")
        print()
    
    print("Usage examples:")
    print("  pytest -m 'unit and gram_matrices'       # Unit tests for Gram matrices")
    print("  pytest -m 'fast and not sage'            # Fast tests not requiring Sage")
    print("  pytest -m 'wikiwand or wikipedia'        # Literature-based tests")
    print("  pytest -m 'sage and hyperbolic'          # Sage verification for hyperbolic cases")
    print("  pytest -m 'integration and finite'       # Integration tests for finite types")


if __name__ == "__main__":
    main()