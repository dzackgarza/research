"""
Unit test specific fixtures and mocking utilities.

Unit tests should test our implementation in isolation with minimal dependencies.
"""

import pytest
# REMOVED: Mock imports - use real Sage data instead of mock theater
# from unittest.mock import Mock, MagicMock, patch


@pytest.fixture
def mock_sage():
    """Mock Sage imports for true unit tests that need complete isolation.
    
    WARNING: Only use this when testing our own logic in complete isolation.
    Do NOT use this to create mock theater that tests nothing.
    Most tests should use real Sage objects or skip if Sage is not available.
    """
    with patch.dict('sys.modules', {
        'sage': MagicMock(),
        'sage.all': MagicMock(),
        'sage.matrix': MagicMock(),
        'sage.rings': MagicMock(),
        'sage.combinat': MagicMock(),
        'sage.geometry': MagicMock(),
        'sage.groups': MagicMock(),
        'sage.algebras': MagicMock()
    }):
        yield


# REMOVED: mock_gram_matrix fixture that encouraged mock theater
# Tests should use real GramMatrix implementations or skip if not available


# REMOVED: Excessive mock fixtures (mock_root_system, mock_coxeter_group, etc.)
# These encouraged mock theater where tests verify mock behavior instead of real code.
# 
# GUIDELINE: Tests should either:
# 1. Use real Sage objects to test mathematical properties
# 2. Test our own implementations with minimal mocking
# 3. Skip with pytest.skip() if dependencies are not available
#
# BAD: mock_obj.method.return_value = 42; assert obj.method() == 42
# GOOD: obj = RealClass(data); assert obj.method() == expected_mathematical_result


@pytest.fixture
def unit_test_data():
    """Test data specifically designed for unit tests."""
    from tests.helpers.sage_extraction import get_expected_gram_for_test
    
    # Extract canonical matrices from Sage
    test_types = [['A', 1], ['A', 2], ['B', 2], ['G', 2]]
    simple_matrices = {}
    expected_determinants = {}
    expected_eigenvalues = {}
    
    for coxeter_type in test_types:
        type_key = ''.join(str(x) for x in coxeter_type)
        gram = get_expected_gram_for_test(coxeter_type)
        
        simple_matrices[type_key] = gram.list()
        expected_determinants[type_key] = gram.det()
        expected_eigenvalues[type_key] = gram.eigenvalues()
    
    return {
        'simple_matrices': simple_matrices,
        'expected_determinants': expected_determinants,
        'expected_eigenvalues': expected_eigenvalues
    }


# REMOVED: mock_matrix_constructor fixture
# Creating mock matrices with pre-determined behavior defeats the purpose of testing.
# Use real Sage matrices or our own matrix implementations instead.


# REMOVED: isolated_test_environment fixture
# Overly broad mocking leads to tests that don't test real behavior.
# If you need isolation, mock specific imports in the test itself.


@pytest.fixture(autouse=True)
def unit_test_markers(request):
    """Automatically apply unit test marker and check isolation."""
    # Ensure this is marked as a unit test
    if not any(mark.name == 'unit' for mark in request.node.iter_markers()):
        pytest.fail("Unit tests must be marked with @pytest.mark.unit")
    
    # Could add additional isolation checks here
    yield