# Sage IntegralLattice Key Files Reference

This document identifies the location of key files related to Sage's `IntegralLattice` functionality within the Sage repository at `~/gitclones/sage`.

## Core IntegralLattice Files

### Original Implementation File
- **`src/sage/modules/free_quadratic_module_integer_symmetric.py`** ⭐ **CURRENT**
  - Contains the main `IntegralLattice()` factory function (line 88)
  - Contains `IntegralLatticeDirectSum()` function (line 326)  
  - Contains `IntegralLatticeGluing()` function (line 437)
  - Main documentation and examples for integral lattices
  - Authors: Simon Brandhorst (2017), Paolo Menegatti (2018)
  - **Current version** after refactoring parts to `integral_lattice/` subdirectory

- **`src/sage/modules/free_quadratic_module_integer_symmetric.py.original`** 🗂️ **PRE-REFACTORING**
  - **The true original implementation file** before modularization
  - Contains the complete monolithic implementation before code was extracted
  - Preserved as backup/reference during the refactoring process

### Module Export
- **`src/sage/modules/all.py`**
  - Line 39: Lazy import of `IntegralLattice` from the main module
  - Makes `IntegralLattice` available when importing from `sage.modules`

## IntegralLattice Implementation Directory

**Location**: `src/sage/modules/integral_lattice/`

This directory contains the core implementation split across multiple specialized files:

### Core Implementation Files (Extracted from Original)
- **`lattice_class.py`** - Main class `FreeQuadraticModule_integer_symmetric`
  - The actual lattice class that `IntegralLattice()` returns
  - Inherits from `FreeQuadraticModule_submodule_with_basis_pid`, `IndexedGenerators`, and `LatticeGroupActions`
  - **Extracted from the original file for better maintainability**

- **`methods.py`** - Core lattice methods and algorithms

- **`group_actions.py`** - Group action functionality (`LatticeGroupActions` class)

- **`root_sublattice.py`** - Root sublattice operations

- **`standard_lattices.py`** - Standard lattice constructions
  - **Extracted from the original file** (contains global lattice objects and helper functions)

### Testing Files
- **`tests/`** directory contains:
  - `test_simple.sage` and `test_simple.sage.py`
  - `test_group_actions.sage` and `test_group_actions.sage.py`
  - `test_all.sage`

## Related Lattice Files in Sage

### Supporting Modules
- **`src/sage/modules/lattices_common.py`** - Common lattice utilities
- **`src/sage/modules/torsion_quadratic_module.py`** - Uses IntegralLattice

### Specialized Lattice Types
- **`src/sage/geometry/lattice_polytope.py`** - Lattice polytopes
- **`src/sage/geometry/toric_lattice.py`** - Toric lattices
- **`src/sage/crypto/lattice.py`** - Cryptographic lattices
- **`src/sage/stats/distributions/discrete_gaussian_lattice.py`** - Lattice-based distributions

### Category Theory Integration
- **`src/sage/combinat/posets/lattices.py`** - Lattice posets
- **`src/sage/categories/lattice_posets.py`** - Lattice poset categories

## Usage

The main entry point for creating integral lattices:

```python
from sage.modules.all import IntegralLattice

# Create from matrix
M = Matrix(ZZ, [[0,1], [1,0]])
L = IntegralLattice(M)

# Create with basis
G = matrix.identity(3)
basis = [[1,-1,0], [0,1,-1]]
L = IntegralLattice(G, basis)
```

## Key Architectural Notes

1. **Factory Pattern**: `IntegralLattice()` is a factory function that creates instances of `FreeQuadraticModule_integer_symmetric`

2. **Refactoring History**: The implementation has been refactored for better maintainability:
   - **Original**: All code was in `free_quadratic_module_integer_symmetric.py`
   - **Current**: Core implementation extracted to `integral_lattice/` subdirectory
   - Factory functions and main entry points remain in the original file

3. **Modular Design**: Implementation is now split across multiple files in the `integral_lattice/` directory for maintainability

4. **Class Hierarchy**: The actual lattice class inherits from multiple base classes providing quadratic form, indexing, and group action functionality

5. **Integration**: Closely integrated with Sage's matrix, module, and algebraic structure systems