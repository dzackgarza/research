# Coxeter Group Test Suite - Proper Organization

This test suite follows established testing best practices with clear separation between different types of tests and proper organization.

## 📁 Directory Structure (Following Testing Best Practices)

```
tests/
├── README.md                          # This documentation
├── conftest.py                        # Shared fixtures and configuration
├── pytest.ini                        # Pytest configuration
├── run_tests.py                       # Test runner with multiple modes
├── data/                              # Test data files
│   ├── coxeter_matrices/             # Sample Coxeter matrices
│   ├── dynkin_diagrams/              # Sample Dynkin diagrams  
│   └── sage_references/              # Reference data from Sage
├── fixtures/                         # Test fixtures and test data generation
│   ├── __init__.py
│   ├── coxeter_fixtures.py          # Coxeter group test fixtures
│   ├── root_system_fixtures.py      # Root system test fixtures
│   └── matrix_fixtures.py           # Matrix generation fixtures
├── unit/                             # 🔬 Unit Tests - Our Implementation
│   ├── __init__.py
│   ├── conftest.py                   # Unit test specific fixtures
│   ├── test_gram_matrices.py        # Gram matrix class unit tests
│   ├── test_root_systems.py         # Root system class unit tests
│   ├── test_coxeter_groups.py       # Coxeter group class unit tests
│   ├── test_weyl_groups.py          # Weyl group class unit tests
│   ├── test_dynkin_diagrams.py      # Dynkin diagram class unit tests
│   ├── test_constructors.py         # Constructor method unit tests
│   └── test_utilities.py            # Utility function unit tests
├── integration/                      # 🔗 Integration Tests - Component Interaction
│   ├── __init__.py
│   ├── conftest.py                   # Integration specific fixtures
│   ├── test_root_system_integration.py      # Root system + lattice integration
│   ├── test_coxeter_weyl_integration.py     # Coxeter + Weyl group integration
│   ├── test_constructor_integration.py     # Constructor interaction tests
│   ├── test_matrix_computation_integration.py # Matrix computation workflows
│   └── test_diagram_group_integration.py   # Diagram + group integration
├── system/                           # 🎯 System Tests - End-to-End Workflows
│   ├── __init__.py
│   ├── conftest.py                   # System test fixtures
│   ├── test_classification_workflows.py    # Complete classification workflows
│   ├── test_literature_examples.py         # End-to-end literature examples
│   ├── test_mathematical_theorems.py       # Complete theorem verification
│   └── test_user_scenarios.py              # Real user workflow tests
├── sage_verification/                # ✅ Sage Cross-Validation (Separate!)
│   ├── __init__.py
│   ├── conftest.py                   # Sage-specific fixtures
│   ├── test_sage_gram_matrices.py   # Compare our Gram matrices to Sage
│   ├── test_sage_root_systems.py    # Compare our root systems to Sage
│   ├── test_sage_coxeter_groups.py  # Compare our Coxeter groups to Sage
│   ├── test_sage_weyl_groups.py     # Compare our Weyl groups to Sage
│   ├── test_sage_dynkin_diagrams.py # Compare our Dynkin diagrams to Sage
│   └── test_sage_numerical_results.py # Verify numerical computations
└── benchmarks/                       # 📊 Performance Tests
    ├── __init__.py
    ├── conftest.py                   # Benchmark fixtures
    ├── test_performance_gram_matrices.py   # Gram matrix performance
    ├── test_performance_root_systems.py    # Root system performance
    └── test_performance_algorithms.py      # Algorithm complexity tests
```

## 🧪 Test Types and Their Purpose

### Unit Tests (`unit/`) - Test Our Implementation in Isolation

- **Purpose**: Test individual classes and methods in isolation

- **Scope**: Single class or function

- **Dependencies**: Mock external dependencies (including Sage)

- **Speed**: Fast (< 1 second per test)

- **When to Run**: On every code change

**What we test:**

- Individual class constructors and methods

- Edge cases and error handling

- Input validation and type checking

- Mathematical properties of our objects

**What we DON'T test:**

- Sage implementations

- Complex workflows involving multiple components

- Performance characteristics

### Integration Tests (`integration/`) - Test Component Interaction

- **Purpose**: Test how our components work together

- **Scope**: Multiple classes/modules interacting

- **Dependencies**: Use real implementations, minimal mocking

- **Speed**: Medium (1-10 seconds per test)

- **When to Run**: Before committing changes

**What we test:**

- Constructor chains (RootSystem → CoxeterGroup → WeylGroup)

- Data flow between components

- Compatibility between different object types

- Mathematical consistency across components

### System Tests (`system/`) - Test Complete Workflows

- **Purpose**: Test complete mathematical workflows end-to-end

- **Scope**: Full user scenarios and mathematical theorems

- **Dependencies**: Real implementations throughout

- **Speed**: Slow (10+ seconds per test)

- **When to Run**: Before releases, nightly builds

**What we test:**

- Complete classification workflows

- Literature examples from start to finish

- Mathematical theorem verification

- Real user scenarios

### Sage Verification (`sage_verification/`) - Cross-Validation

- **Purpose**: Verify our results match Sage's canonical implementations

- **Scope**: Compare outputs between our code and Sage

- **Dependencies**: Requires Sage installation

- **Speed**: Variable (depends on Sage)

- **When to Run**: After implementation complete, before release

**What we test:**

- Numerical results match Sage exactly

- Mathematical properties are equivalent

- Edge cases produce same results

- Classification results are identical

### Benchmarks (`benchmarks/`) - Performance Testing

- **Purpose**: Measure and track performance characteristics

- **Scope**: Algorithm complexity and execution time

- **Dependencies**: Real implementations

- **Speed**: Variable (some tests may be very slow)

- **When to Run**: Weekly, before performance-critical releases

## 🏷️ Test Markers and Organization

### Test Type Markers

```python
@pytest.mark.unit          # Unit tests of our implementation
@pytest.mark.integration   # Integration tests
@pytest.mark.system        # System/end-to-end tests
@pytest.mark.sage          # Sage verification tests
@pytest.mark.benchmark     # Performance benchmarks
```

### Speed Markers

```python
@pytest.mark.fast          # < 1 second
@pytest.mark.medium        # 1-10 seconds  
@pytest.mark.slow          # > 10 seconds
@pytest.mark.very_slow     # > 60 seconds (benchmarks)
```

### Mathematical Content Markers

```python
@pytest.mark.gram_matrices    # Gram matrix related
@pytest.mark.root_systems     # Root system related
@pytest.mark.coxeter_groups   # Coxeter group related
@pytest.mark.weyl_groups      # Weyl group related
@pytest.mark.dynkin_diagrams  # Dynkin diagram related
@pytest.mark.hyperbolic       # Hyperbolic/indefinite types
@pytest.mark.finite           # Finite types
@pytest.mark.affine           # Affine types
```

## 🚀 Running Tests

### By Test Type (Recommended)

```bash
# Unit tests only (fast, run frequently)
python run_tests.py --type unit

# Integration tests (medium speed)
python run_tests.py --type integration  

# System tests (slow, comprehensive)
python run_tests.py --type system

# Sage verification (requires Sage)
python run_tests.py --type sage

# Performance benchmarks
python run_tests.py --type benchmark
```

### By Speed

```bash
# Fast tests only (development)
python run_tests.py --speed fast

# All tests except very slow
python run_tests.py --exclude very_slow

# Complete test suite (CI/release)
python run_tests.py --all
```

### By Mathematical Content

```bash
# All Gram matrix tests
python run_tests.py --topic gram_matrices

# All root system tests across all test types
python run_tests.py --topic root_systems

# Finite type tests only
python run_tests.py --topic finite
```

### Development Workflow

```bash
# During development (fast feedback)
python run_tests.py --type unit --topic gram_matrices

# Before commit (verify integration)
python run_tests.py --type unit,integration --speed fast,medium

# Before release (comprehensive)
python run_tests.py --all --exclude benchmark
```

## 🔧 Test Configuration

### conftest.py Files

- `tests/conftest.py`: Global fixtures available to all tests

- `tests/unit/conftest.py`: Unit test specific fixtures (mocking utilities)

- `tests/integration/conftest.py`: Integration test fixtures (real objects)

- `tests/system/conftest.py`: System test fixtures (complete workflows)

- `tests/sage_verification/conftest.py`: Sage comparison utilities

- `tests/benchmarks/conftest.py`: Performance measurement utilities

### Fixtures Organization

- **Unit Test Fixtures**: Mock objects, isolated test data

- **Integration Fixtures**: Real objects with controlled interactions

- **System Fixtures**: Complete mathematical examples

- **Sage Fixtures**: Sage object construction and comparison utilities

- **Benchmark Fixtures**: Performance measurement tools

## 📋 Best Practices Implemented

### 1. Proper Separation of Concerns

- ✅ Unit tests test our code in isolation (with mocking)

- ✅ Integration tests test component interaction

- ✅ System tests test complete workflows

- ✅ Sage verification is completely separate

### 2. Fast Feedback Loop

- ✅ Unit tests are fast (< 1 second each)

- ✅ Can run subset of tests during development

- ✅ Clear speed markers for filtering

### 3. Clear Test Organization

- ✅ Tests mirror source code structure

- ✅ Clear naming conventions

- ✅ Proper use of conftest.py for fixtures

### 4. Minimal Mocking

- ✅ Mock only external dependencies in unit tests

- ✅ Use real implementations in integration/system tests

- ✅ Sage is treated as external dependency

### 5. Test Isolation

- ✅ Each test is independent

- ✅ No shared state between tests

- ✅ Clear setup/teardown through fixtures

## 🎯 Testing Philosophy

### Test Our Implementation, Not Sage

- **Unit/Integration/System tests**: Test our code behavior

- **Sage verification tests**: Compare our results to Sage's

- **Clear separation**: Never mix these concerns

### Test Behavior, Not Implementation

- Focus on mathematical properties and contracts

- Test public interfaces, not internal details

- Use mocking sparingly and strategically

### Follow the Testing Pyramid

- **Many unit tests**: Fast, isolated, comprehensive coverage

- **Some integration tests**: Key component interactions

- **Few system tests**: Critical end-to-end workflows

- **Targeted verification**: Compare key results with Sage

This organization ensures maintainable, fast, and reliable tests that follow established software engineering best practices while serving the mathematical rigor required for the Coxeter group project.
