"""
Global test fixtures and configuration for Coxeter test suite.

This file contains fixtures that are available to all test types.
"""

import pytest
from pathlib import Path


@pytest.fixture(scope="session")
def test_data_dir():
    """Path to test data directory."""
    return Path(__file__).parent / "data"


@pytest.fixture(scope="session")
def project_root():
    """Path to project root directory."""
    return Path(__file__).parent.parent


@pytest.fixture(scope="session")
def src_dir():
    """Path to source directory."""
    return Path(__file__).parent.parent / "src"


@pytest.fixture
def sample_coxeter_types():
    """Sample Coxeter types for testing."""
    return [
        ['A', 1], ['A', 2], ['A', 3], ['A', 4],
        ['B', 2], ['B', 3], ['B', 4],
        ['C', 2], ['C', 3], ['C', 4],
        ['D', 4], ['D', 5], ['D', 6],
        ['E', 6], ['E', 7], ['E', 8],
        ['F', 4],
        ['G', 2],
        ['H', 3], ['H', 4],
        ['I', 5], ['I', 6], ['I', 8]
    ]


@pytest.fixture
def sample_affine_types():
    """Sample affine Coxeter types for testing."""
    return [
        ['A', 1, 1], ['A', 2, 1], ['A', 3, 1],
        ['B', 2, 1], ['B', 3, 1], ['B', 4, 1],
        ['C', 2, 1], ['C', 3, 1], ['C', 4, 1],
        ['D', 4, 1], ['D', 5, 1],
        ['E', 6, 1], ['E', 7, 1], ['E', 8, 1],
        ['F', 4, 1],
        ['G', 2, 1]
    ]


@pytest.fixture
def numerical_tolerance():
    """Numerical tolerance for floating point comparisons (when unavoidable)."""
    return 1e-12


@pytest.fixture
def exact_fields():
    """Dictionary of exact fields for different Coxeter types."""
    from sage.all import ZZ, QQ, QuadraticField, CyclotomicField
    
    return {
        'ZZ': ZZ,
        'QQ': QQ,
        'golden_ratio': QuadraticField(5, 'phi'),  # Q(√5) for H3, H4
        'sqrt2': QuadraticField(2, 'sqrt2'),       # Q(√2) for B_n, C_n
        'cyclotomic_5': CyclotomicField(5),        # For cos(π/5)
        'cyclotomic_10': CyclotomicField(10),      # For cos(π/10) 
        'cyclotomic_12': CyclotomicField(12)       # For cos(π/12)
    }


@pytest.fixture
def matrix_factories():
    """Factory functions for creating matrices in exact fields."""
    from sage.all import matrix, ZZ, QQ
    
    def create_matrix(data, field=QQ):
        """Create matrix in specified field."""
        return matrix(field, data)
    
    def create_gram_matrix(coxeter_type):
        """Create Gram matrix for given Coxeter type."""
        # This will be implemented once our constructors exist
        raise NotImplementedError("GramMatrix.from_coxeter_type not yet implemented")
    
    return {
        'matrix': create_matrix,
        'gram_matrix': create_gram_matrix
    }


@pytest.fixture
def expected_finite_orders():
    """Dictionary of known finite Coxeter group orders."""
    return {
        ('A', 1): 2,
        ('A', 2): 6,
        ('A', 3): 24,
        ('A', 4): 120,
        ('B', 2): 8,
        ('B', 3): 48,
        ('B', 4): 384,
        ('C', 2): 8,
        ('C', 3): 48,
        ('C', 4): 384,
        ('D', 4): 192,
        ('D', 5): 1920,
        ('E', 6): 51840,
        ('E', 7): 2903040,
        ('E', 8): 696729600,
        ('F', 4): 1152,
        ('G', 2): 12,
        ('H', 3): 120,
        ('H', 4): 14400,
        ('I', 3): 6,
        ('I', 4): 8,
        ('I', 5): 10,
        ('I', 6): 12
    }


@pytest.fixture
def literature_sources():
    """Metadata about literature sources used in tests."""
    return {
        'wikiwand_schlafli': {
            'url': 'https://www.wikiwand.com/en/articles/Schläfli_matrix',
            'title': 'Schläfli matrix - Wikiwand',
            'accessed': '2024'
        },
        'wikipedia_coxeter': {
            'url': 'https://en.wikipedia.org/wiki/Coxeter_group',
            'title': 'Coxeter group - Wikipedia',
            'accessed': '2024'
        },
        'wikipedia_weyl': {
            'url': 'https://en.wikipedia.org/wiki/Weyl_group',
            'title': 'Weyl group - Wikipedia', 
            'accessed': '2024'
        },
        'wikipedia_dynkin': {
            'url': 'https://en.wikipedia.org/wiki/Dynkin_diagram',
            'title': 'Dynkin diagram - Wikipedia',
            'accessed': '2024'
        }
    }