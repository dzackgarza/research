# SageMath Wrapper Specification for Enriques Orbit Computation

**Version**: 1.0\
**Priority**: PRIMARY - This specification drives all backend implementation decisions\
**Philosophy**: The SageMath interface should feel native, intuitive, and mathematically natural

* * *

## 1. User Experience Goals

### 1.1 Principle: "One-Line Accessibility"

```python
# The most common use case should be this simple:
sage: from enriques_moduli import enriques_surface_orbits
sage: orbits = enriques_surface_orbits()
sage: len(orbits)
7  # or whatever the actual count is

# With slightly more control:
sage: orbits = enriques_surface_orbits(degree=2, show_progress=True)
Computing orbit representatives for Enriques lattice U ⊕ 2U ⊕ 2E₈(-1)...
Found 7 orbit representatives in 2.3 seconds.
```

### 1.2 Principle: "SageMath Native Feel"

- All return types should be standard SageMath objects
- Integration with existing SageMath lattice functionality
- Follow SageMath naming conventions and patterns
- Support SageMath's standard `_repr_`, `_latex_`, plotting, etc.

### 1.3 Principle: "Progressive Complexity"

- Simple interface for standard cases
- Rich options for advanced users
- Expert-level access to all underlying algorithms

* * *

## 2. Core Interface Design

### 2.1 Primary Entry Point

```python
def enriques_surface_orbits(degree=2, lattice_type="standard", **kwargs):
    """
    Compute orbit representatives of isotropic vectors for Enriques surfaces.

    PARAMETERS:
    -----------
    degree : int (default: 2)
        Degree of the polarization
    lattice_type : str (default: "standard") 
        - "standard": U ⊕ 2U ⊕ 2E₈(-1) 
        - "custom": specify custom lattice via lattice= parameter
    method : str (default: "auto")
        - "auto": choose best method automatically
        - "approximate": use approximate models (fast)
        - "exact": exact computation (slower but guaranteed)
    show_progress : bool (default: False)
        Show computation progress
    max_time : int (default: 300)  
        Maximum computation time in seconds

    RETURNS:
    --------
    EnriquesOrbitResult
        Container with orbit representatives and metadata

    EXAMPLES:
    ---------
    sage: orbits = enriques_surface_orbits()
    sage: orbits.representatives()
    [(1, 0, 0, ...), (0, 1, 0, ...), ...]

    sage: orbits.count()  
    7

    sage: orbits.lattice()
    Lattice of degree 20 and rank 20 over Integer Ring
    """
```

### 2.2 Result Object Design

```python
class EnriquesOrbitResult(SageObject):
    """
    Container for orbit computation results with rich SageMath integration.
    """

    def representatives(self):
        """Return list of orbit representative vectors as SageMath vectors."""
        # Return: List[sage.modules.free_module_element.vector]

    def count(self):
        """Number of distinct orbits."""
        # Return: Integer

    def orbit_sizes(self):
        """Size of each orbit (if computed)."""
        # Return: List[Integer] 

    def lattice(self):
        """The underlying lattice as a SageMath IntegralLattice."""
        # Return: sage.modules.lattice_integer.IntegralLattice

    def automorphism_group(self):
        """Automorphism group of the lattice.""" 
        # Return: sage.groups.matrix_gps.matrix_group.MatrixGroup_gap

    def verify(self):
        """Verify that all representatives are actually isotropic and inequivalent."""
        # Return: bool (True if verification passes)

    def plot(self, **kwargs):
        """Visualize the orbit structure (for small cases)."""
        # Return: Graphics object

    def save(self, filename):
        """Save results to file for later analysis."""

    def _repr_(self):
        return f"Orbit computation result: {self.count()} orbits in {self.lattice()}"

    def _latex_(self):
        return rf"\\text{{Orbit representatives for }} {latex(self.lattice())}"
```

### 2.3 Lattice Construction Interface

```python
class IndefiniteLatticeBuilder:
    """
    SageMath-integrated builder for indefinite lattices.
    Should feel like native SageMath lattice construction.
    """

    @staticmethod
    def from_string_spec(spec_list):
        """
        Build lattice from string specification.

        EXAMPLES:
        ---------
        sage: L = IndefiniteLatticeBuilder.from_string_spec(["U", "2U", "2E8"])
        sage: L.gram_matrix()
        20 x 20 dense matrix over Rational Field

        sage: L.signature()
        (2, 18)
        """

    @staticmethod  
    def enriques_lattice(degree=2):
        """Standard Enriques lattice for given polarization degree."""

    @staticmethod
    def from_gram_matrix(matrix):
        """Build from explicit Gram matrix."""

    @staticmethod
    def hyperbolic_plane():
        """The lattice U."""

    @staticmethod
    def root_lattice(type_str):
        """
        Root lattices: 'E8', 'E7', 'E6', 'A5', 'D4', etc.

        EXAMPLES:
        ---------
        sage: E8 = IndefiniteLatticeBuilder.root_lattice('E8')
        sage: E8.rank()
        8
        """

# Convenient aliases that feel natural in SageMath
def enriques_lattice(degree=2):
    return IndefiniteLatticeBuilder.enriques_lattice(degree)

def indefinite_lattice(spec):
    return IndefiniteLatticeBuilder.from_string_spec(spec)
```

### 2.4 Advanced Interface for Power Users

```python
class IndefiniteOrbitComputation:
    """
    Full-featured orbit computation with fine-grained control.
    For advanced users who need access to all parameters.
    """

    def __init__(self, lattice, **kwargs):
        """
        PARAMETERS:
        -----------
        lattice : can be any of:
            - List[str]: ["U", "2U", "2E8"] 
            - sage.modules.lattice_integer.IntegralLattice
            - Matrix (Gram matrix)
            - IndefiniteLattice object
        """

    def compute_orbit_representatives(self, norm=0, **algorithm_params):
        """
        Full algorithm control.

        PARAMETERS:
        -----------
        norm : int/rational (default: 0)
            Target norm for vectors (0 = isotropic)
        method : str
            "approximate_models", "exact_enumeration", "hybrid"
        approximate_bound : int
            Bound for approximate model construction  
        max_iterations : int
            Maximum iterations for iterative algorithms
        use_cached_automorphisms : bool
            Whether to cache automorphism group computations
        parallel : bool/int
            Use parallel computation (True/False or number of threads)
        """

    def compute_automorphism_group(self, **params):
        """Compute just the automorphism group."""

    def verify_orbit_representatives(self, representatives):
        """Verify a set of orbit representatives."""

    def benchmark(self, methods=None):
        """Compare different computation methods."""
```

* * *

## 3. Integration with SageMath Ecosystem

### 3.1 Lattice Integration

```python
# Should work seamlessly with existing SageMath lattices
sage: L = IntegralLattice([[2, 1], [1, 2]])  # Standard SageMath
sage: orbits = compute_orbit_representatives(L, norm=0)
sage: orbits.count()

# And vice versa
sage: enriques_orbits = enriques_surface_orbits()
sage: sage_lattice = enriques_orbits.lattice()
sage: sage_lattice.short_vectors(10)  # Use SageMath methods
```

### 3.2 Group Theory Integration

```python
# Automorphism groups should integrate with SageMath's group theory
sage: orbits = enriques_surface_orbits()
sage: G = orbits.automorphism_group()
sage: G.order()
sage: G.character_table()  # If finite
sage: G.subgroups()  # Standard SageMath group methods
```

### 3.3 Linear Algebra Integration

```python
# Vectors and matrices should be native SageMath objects
sage: orbits = enriques_surface_orbits()
sage: v = orbits.representatives()[0]  
sage: type(v)
<class 'sage.modules.free_module_element.FreeModuleElement_generic_dense'>

sage: v.parent()
Ambient free module of rank 20 over the principal ideal domain Integer Ring

# Should work with SageMath linear algebra
sage: v.norm()  # SageMath's norm function
sage: v * enriques_lattice().gram_matrix() * v  # Should be 0 for isotropic
```

* * *

## 4. Documentation and Examples

### 4.1 Docstring Standard

```python
def enriques_surface_orbits(degree=2, **kwargs):
    r"""
    Compute orbit representatives of isotropic vectors for Enriques surfaces.

    This function implements the algorithms from Dutour Sikirić and Hulek 
    (2023) for computing orbit representatives in the lattice M(1/2) = 
    U ⊕ 2U ⊕ 2E₈(-1), which parametrizes polarized Enriques surfaces.

    INPUT:

    - ``degree`` -- (default: 2) degree of the polarization
    - ``method`` -- (default: "auto") computation method
    - ``show_progress`` -- (default: False) show computation progress

    OUTPUT:

    An ``EnriquesOrbitResult`` object containing the orbit representatives
    and associated data.

    EXAMPLES::

        sage: from enriques_moduli import enriques_surface_orbits
        sage: orbits = enriques_surface_orbits()
        sage: orbits.count()
        7
        sage: v = orbits.representatives()[0]
        sage: v * orbits.lattice().gram_matrix() * v  # Verify isotropic
        0

    You can also work with custom lattices::

        sage: from enriques_moduli import indefinite_lattice, compute_orbit_representatives
        sage: L = indefinite_lattice(["U", "A2"])  
        sage: orbits = compute_orbit_representatives(L, norm=0)
        sage: orbits.count()
        3

    ALGORITHM:

    Uses the approximate models algorithm from [DS2023]_. For the exact
    algorithm details, see :meth:`IndefiniteOrbitComputation.compute_orbit_representatives`.

    REFERENCES:

    .. [DS2023] Dutour Sikirić and Hulek, "Moduli of polarized Enriques 
       surfaces -- computational aspects", arXiv:2302.01679v2, 2023.

    .. SEEALSO::

        :func:`compute_orbit_representatives`, :class:`IndefiniteOrbitComputation`
    """
```

### 4.2 Tutorial Structure

```python
"""
TUTORIAL: Enriques Surface Orbit Computation
============================================

This tutorial demonstrates how to compute orbit representatives for 
isotropic vectors in indefinite lattices, with a focus on applications
to Enriques surfaces.

Basic Usage
-----------

The simplest way to get started:

    sage: from enriques_moduli import enriques_surface_orbits
    sage: orbits = enriques_surface_orbits()
    sage: print(f"Found {orbits.count()} orbit representatives")

Exploring the Results
--------------------

The result object provides rich information:

    sage: orbits.representatives()[:3]  # First 3 representatives
    [(1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
     (0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
     (0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)]

    sage: orbits.verify()  # Check correctness
    True

Working with Custom Lattices
----------------------------

You can also work with your own indefinite lattices:

    sage: from enriques_moduli import indefinite_lattice
    sage: L = indefinite_lattice(["U", "2U", "A3"])
    sage: orbits = compute_orbit_representatives(L)

Advanced Usage
--------------

For fine control over the computation:

    sage: from enriques_moduli import IndefiniteOrbitComputation
    sage: computer = IndefiniteOrbitComputation(enriques_lattice())
    sage: orbits = computer.compute_orbit_representatives(
    ...     norm=0, 
    ...     method="approximate_models",
    ...     show_progress=True,
    ...     max_iterations=1000
    ... )
"""
```

* * *

## 5. Installation and Setup Experience

### 5.1 Installation

```bash
# Goal: Simple pip install that "just works"
pip install sage-enriques-moduli

# Or from SageMath
sage -pip install sage-enriques-moduli

# Or via conda-forge (eventual goal)  
conda install -c conda-forge sage-enriques-moduli
```

### 5.2 Import Experience

```python
# Should work immediately after install
sage: from enriques_moduli import *
sage: enriques_surface_orbits()  # Works immediately

# Alternative explicit imports
sage: from enriques_moduli import (
...     enriques_surface_orbits,
...     indefinite_lattice, 
...     compute_orbit_representatives
... )

# Check installation
sage: import enriques_moduli
sage: enriques_moduli.version()
'1.0.0'
sage: enriques_moduli.test()  # Run basic functionality tests
All tests passed!
```

* * *

## 6. Error Handling and User Experience

### 6.1 Graceful Error Messages

```python
# Bad input should give helpful errors
sage: enriques_surface_orbits(degree=-1)
ValueError: Polarization degree must be positive, got -1

sage: indefinite_lattice(["invalid_lattice"])  
LatticeError: Unknown lattice type 'invalid_lattice'. 
Available types: U, E8, E7, E6, A1, A2, ..., D4, D5, ...
Did you mean 'U'?

# Long computations should be interruptible
sage: orbits = enriques_surface_orbits(show_progress=True)
Computing orbit representatives... Press Ctrl+C to interrupt.
[Progress bar]
KeyboardInterrupt: Computation interrupted after 45.2 seconds.
Partial results have been saved and can be resumed with resume=True.
```

### 6.2 Performance Warnings

```python
# Warn about expensive computations
sage: L = indefinite_lattice(["U"] * 10)  # Very large lattice
sage: compute_orbit_representatives(L)
PerformanceWarning: This lattice has rank 20, which may require significant
computation time (estimated: 30+ minutes). Consider using method="approximate"
for faster results, or set max_time=3600 to allow longer computation.

Continue? [y/N]: 
```

* * *

## 7. Implementation Requirements Derived from Interface

### 7.1 Backend Interface Contract

```python
# The Julia backend must provide these exact function signatures:
def julia_enriques_orbits(degree, method, **params):
    """Returns: (representatives_list, metadata_dict)"""

def julia_orbit_computation(gram_matrix, norm, method, **params):
    """Returns: (representatives_list, orbit_sizes, automorphism_generators)"""

def julia_automorphism_group(gram_matrix):
    """Returns: list of generator matrices"""
```

### 7.2 Type Conversion Requirements

- Julia matrices ↔ SageMath matrices (exact rational arithmetic)
- Julia vectors ↔ SageMath vectors (preserve parent/ambient space)
- Julia integers ↔ SageMath Integers (arbitrary precision)
- Error handling across Julia-Python boundary

### 7.3 Performance Requirements from Interface

- `enriques_surface_orbits()` should complete in < 5 minutes
- Progress reporting should update every 5-10 seconds
- Memory usage should stay below 2GB for standard cases
- Results should be cacheable and resumable

* * *

## 8. Success Criteria

### 8.1 User Experience Success

- [ ] New user can compute Enriques orbits in one line of code
- [ ] Results integrate seamlessly with SageMath workflows
- [ ] Documentation is clear and includes worked examples
- [ ] Error messages are helpful and actionable

### 8.2 Mathematical Success

- [ ] Results match Dutour Sikirić & Hulek paper for test cases
- [ ] Verification functions confirm all representatives are valid
- [ ] Interface supports both standard and custom lattices
- [ ] Advanced users can access all underlying algorithms

### 8.3 Technical Success

- [ ] Installation "just works" on all SageMath platforms
- [ ] Performance meets targets for standard use cases
- [ ] Memory usage is reasonable and predictable
- [ ] Computation can be interrupted and resumed

* * *

**This specification should drive all implementation decisions.
The Julia backend, Python wrapper, and documentation should all be designed to deliver this exact user experience.**
