#!/usr/bin/env python3
"""
Test script to verify SageMath documentation indexing.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

def test_sagemath_files():
    """Test that we can find and process SageMath files."""
    
    load_dotenv()
    
    # Import utility functions
    from sagemath_utils import get_sage_path, get_sagemath_patterns, extract_python_docstrings
    
    SAGE_PATH = get_sage_path()
    
    print("=== SageMath Documentation Test ===")
    print(f"Looking for SageMath at: {SAGE_PATH}")
    
    if not SAGE_PATH.exists():
        print("❌ SageMath directory not found!")
        print("Expected location:", SAGE_PATH.absolute())
        return False
    
    print("✓ SageMath directory found")
    
    # Test patterns
    patterns = get_sagemath_patterns()
    
    total_files = 0
    for pattern in patterns:
        files = list(SAGE_PATH.glob(pattern))
        print(f"Pattern {pattern}: {len(files)} files")
        total_files += len(files)
        
        # Show first few files as examples
        for i, f in enumerate(files[:3]):
            try:
                size = f.stat().st_size / 1024  # KB
                print(f"  Example: {f.relative_to(SAGE_PATH)} ({size:.1f} KB)")
            except:
                print(f"  Example: {f.relative_to(SAGE_PATH)} (size unknown)")
    
    print(f"\nTotal files found: {total_files}")
    
    if total_files == 0:
        print("❌ No SageMath documentation files found!")
        return False
    
    print("✓ SageMath documentation files found")
    
    # Test docstring extraction on a Python file
    python_files = list(SAGE_PATH.glob("./src/sage/**/*.py"))
    if python_files:
        test_file = python_files[0]
        print(f"\nTesting docstring extraction on: {test_file.relative_to(SAGE_PATH)}")
        
        try:
            docstrings = extract_python_docstrings(test_file)
            print(f"Extracted {len(docstrings)} characters of docstrings/content")
            print("First 200 characters:", docstrings[:200] + "..." if len(docstrings) > 200 else docstrings)
            print("✓ Docstring extraction working")
            
        except Exception as e:
            print(f"❌ Docstring extraction failed: {e}")
            return False
    
    return True

if __name__ == "__main__":
    success = test_sagemath_files()
    print(f"\nTest {'PASSED' if success else 'FAILED'}")
    exit(0 if success else 1) 