# SageMath Interface Specification: Table Reproduction Focus

**Version**: 1.0  
**Priority**: PRIMARY - Reproduce Dutour Sikirić & Hulek computational results exactly  
**Philosophy**: The interface should enable exact reproduction of every calculation in the paper

---

## 1. Core Mathematical Goal

### 1.1 Target Calculations (from GAP test suite)
The paper's computational results are based on these test cases:

```python
TEST_CASES = [
    (["U", "2U"], 2),                    # Basic hyperbolic case
    (["U", "2U", "A2"], 2),              # With A₂ root lattice  
    (["U", "2U", "A3"], 2),              # With A₃ root lattice
    (["U", "2U", "A2", "A2"], 2),        # Multiple root lattices
    (["U", "U", "E7"], 2),               # E₇ case
    (["U", "2U", "2E8"], 2),             # Enriques case (main result)
]
```

### 1.2 Required Computations for Each Test Case
For each lattice specification `(eList, k)`:

1. **Orbit Representatives for Norm 0** (isotropic vectors)
2. **Orbit Representatives for Norm 2** 
3. **Isotropic k-plane orbits** (both "plane" and "flag" types)
4. **Automorphism group** generators and order
5. **Equivalence testing** (verify lattice invariants)

---

## 2. Primary Interface Design

### 2.1 Core Function: Reproduce Table Entry
```python
def compute_lattice_orbit_data(lattice_spec, k_dim=2, norms=[0, 2]):
    """
    Compute complete orbital data for a lattice, reproducing paper's table entries.
    
    PARAMETERS:
    -----------
    lattice_spec : list of str
        Lattice specification like ["U", "2U", "A2"] or ["U", "2U", "2E8"]
    k_dim : int (default: 2)  
        Dimension for isotropic k-plane computation
    norms : list of int (default: [0, 2])
        Target norms for orbit representative computation
        
    RETURNS:
    --------
    LatticeOrbitData
        Complete computational results matching paper's table format
        
    EXAMPLES:
    ---------
    sage: data = compute_lattice_orbit_data(["U", "2U", "2E8"])
    sage: print(data.summary_table())
    Lattice: U ⊕ 2U ⊕ 2E₈(-1)
    Dimension: 20, Signature: (2, 18)
    
    Orbit Representatives:
      Norm 0 (isotropic): 7 orbits
      Norm 2: 12 orbits
      
    Isotropic 2-planes:
      Plane type: 3 orbits
      Flag type: 5 orbits
      
    Automorphism Group:
      Order: 2^18 * 3^8 * 5^2 * 7 (example)
      Generators: 15 matrices
    """
```

### 2.2 Result Container Class
```python
class LatticeOrbitData(SageObject):
    """
    Container for complete orbital computation results.
    Designed to reproduce paper's table entries exactly.
    """
    
    def __init__(self, lattice_spec, computation_results):
        self.lattice_spec = lattice_spec
        self.lattice = self._build_lattice(lattice_spec)
        self.results = computation_results
        
    # Core data access
    def orbit_representatives(self, norm=0):
        """Get orbit representatives for given norm."""
        # Returns: List[sage.modules.free_module_element.vector]
        
    def orbit_count(self, norm=0):
        """Number of orbits for given norm.""" 
        # Returns: Integer
        
    def isotropic_plane_orbits(self, plane_type="plane"):
        """Isotropic k-plane orbit data."""
        # plane_type: "plane" or "flag"
        # Returns: List[orbit_data]
        
    def automorphism_group_data(self):
        """Complete automorphism group information."""
        # Returns: dict with 'generators', 'order', 'structure'
        
    # Verification functions
    def verify_orbit_representatives(self, norm=0):
        """Verify all representatives have correct norm and are inequivalent."""
        
    def verify_isotropic_condition(self):
        """Verify all norm-0 representatives are actually isotropic."""
        
    def verify_equivalence_invariance(self):
        """Test that orbit counts are preserved under lattice equivalence."""
        
    # Table reproduction
    def summary_table(self):
        """Formatted table matching paper's presentation."""
        
    def latex_table_row(self):
        """LaTeX table row for paper reproduction."""
        
    def gap_format_output(self):
        """Output in GAP format matching original test code."""
        
    # Detailed access
    def lattice_gram_matrix(self):
        """Gram matrix of the lattice."""
        
    def lattice_signature(self):
        """Signature (p, q) of the quadratic form."""
        
    def computation_metadata(self):
        """Timing, method, convergence info."""
```

### 2.3 Test Suite Driver Function
```python
def reproduce_paper_table(test_cases=None, verbose=True):
    """
    Reproduce the complete computational table from the paper.
    
    PARAMETERS:
    -----------
    test_cases : list (optional)
        Specific test cases to run. If None, runs all standard cases.
    verbose : bool (default: True)
        Show progress and detailed output
        
    RETURNS:
    --------
    PaperReproductionResults
        Complete table with all computational data
        
    EXAMPLES:
    ---------
    sage: results = reproduce_paper_table()
    Computing orbit data for all test cases...
    
    Case 1/6: ["U", "2U"] 
      Norm 0: 1 orbit, Norm 2: 3 orbits ✓
      
    Case 2/6: ["U", "2U", "A2"]
      Norm 0: 2 orbits, Norm 2: 7 orbits ✓
      
    ...
      
    Case 6/6: ["U", "2U", "2E8"] (Enriques)  
      Norm 0: 7 orbits, Norm 2: 23 orbits ✓
      
    All computations completed successfully!
    
    sage: print(results.latex_table())  # Get LaTeX for paper
    sage: results.save("paper_reproduction.json")  # Save for analysis
    """
```

### 2.4 Individual Lattice Construction
```python
def build_lattice_from_spec(lattice_spec):
    """
    Build indefinite lattice from string specification.
    
    PARAMETERS:
    -----------
    lattice_spec : list of str
        Components like ["U", "2U", "A2", "2E8"]
        
    EXAMPLES:
    ---------
    sage: L = build_lattice_from_spec(["U", "2U", "2E8"])
    sage: L.gram_matrix().dimensions()
    (20, 20)
    sage: L.signature()
    (2, 18)
    
    # Standard lattices available:
    sage: U = build_lattice_from_spec(["U"])           # Hyperbolic plane
    sage: E8 = build_lattice_from_spec(["E8"])         # E₈ root lattice  
    sage: A2 = build_lattice_from_spec(["A2"])         # A₂ root lattice
    sage: scaled = build_lattice_from_spec(["2E8"])    # 2 * E₈
    """

# Dictionary of all standard lattices used in the paper
STANDARD_LATTICES = {
    "U": hyperbolic_plane_matrix(),
    "E8": e8_root_lattice_matrix(),
    "E7": e7_root_lattice_matrix(), 
    "E6": e6_root_lattice_matrix(),
    "A1": a1_root_lattice_matrix(),
    "A2": a2_root_lattice_matrix(),
    "A3": a3_root_lattice_matrix(),
    # ... complete set from paper
}
```

---

## 3. Computational Algorithm Interface

### 3.1 Core Orbit Computation
```python
def compute_orbit_representatives_exact(gram_matrix, norm=0, method="auto"):
    """
    Compute orbit representatives using exact algorithms from the paper.
    
    This is the core mathematical function that implements Algorithm 2
    from Dutour Sikirić & Hulek.
    
    PARAMETERS:
    -----------
    gram_matrix : Matrix over QQ
        Gram matrix of the indefinite quadratic form
    norm : int/QQ (default: 0)
        Target norm for representatives (0 = isotropic)
    method : str (default: "auto")
        - "auto": choose best method based on lattice size
        - "approximate_models": Algorithm 1 from paper
        - "exact_enumeration": direct enumeration (for small cases)
        
    RETURNS:
    --------
    OrbitComputationResult  
        Raw computational results with representatives, generators, metadata
    """

def compute_isotropic_kplane_orbits(gram_matrix, k_dim, plane_type="plane"):
    """
    Compute orbits of isotropic k-planes (Algorithm 3 variant).
    
    PARAMETERS:
    -----------
    gram_matrix : Matrix over QQ
    k_dim : int
        Dimension of isotropic subspaces
    plane_type : str
        - "plane": just the k-dimensional subspaces
        - "flag": flags of isotropic subspaces
    """

def compute_automorphism_group(gram_matrix):
    """
    Compute automorphism group of indefinite quadratic form.
    
    Uses the most appropriate method based on lattice properties.
    """
```

### 3.2 Backend Interface Requirements
```python
# The Julia/OSCAR backend must provide these exact signatures:

def oscar_orbit_representatives(gram_matrix_rational, target_norm):
    """
    RETURNS: (representatives_list, orbit_metadata)
    representatives_list: List[List[Integer]]  # vectors as integer lists
    orbit_metadata: Dict with keys 'method_used', 'iterations', 'time_seconds'
    """

def oscar_automorphism_group(gram_matrix_rational):
    """  
    RETURNS: (generator_matrices, group_order, group_structure_info)
    generator_matrices: List[List[List[Integer]]]  # matrices as nested lists
    group_order: Integer or "infinite" 
    group_structure_info: Dict with structural information
    """

def oscar_isotropic_kplane_orbits(gram_matrix_rational, k_dim, plane_type):
    """
    RETURNS: (orbit_representatives, plane_metadata)
    """
```

---

## 4. Verification and Testing

### 4.1 Exact Reproduction Tests
```python
def test_reproduce_gap_results():
    """
    Test that our results exactly match the GAP computation from AllTests.g
    """
    # For each test case in the GAP file:
    test_cases = [
        (["U", "2U"], 2),
        (["U", "2U", "A2"], 2), 
        (["U", "2U", "A3"], 2),
        (["U", "2U", "A2", "A2"], 2),
        (["U", "U", "E7"], 2),
        (["U", "2U", "2E8"], 2),  # Main Enriques case
    ]
    
    for lattice_spec, k_dim in test_cases:
        print(f"Testing {lattice_spec}...")
        
        # Compute our results
        data = compute_lattice_orbit_data(lattice_spec, k_dim)
        
        # The original GAP tests verify:
        # 1. TestStab: automorphism group preserves the form
        assert data.verify_automorphism_group()
        
        # 2. TestEquiv: equivalent lattices have same orbit counts  
        assert data.verify_equivalence_invariance()
        
        # 3. TestOrbitRepresentative: orbit counts for norm 0 and 2
        norm_0_count = data.orbit_count(0)
        norm_2_count = data.orbit_count(2)
        print(f"  Norm 0: {norm_0_count} orbits")
        print(f"  Norm 2: {norm_2_count} orbits")
        
        # 4. TestOrbitIsotropic: k-plane orbit counts  
        plane_count = len(data.isotropic_plane_orbits("plane"))
        flag_count = len(data.isotropic_plane_orbits("flag"))
        print(f"  {k_dim}-planes: {plane_count} orbits")
        print(f"  {k_dim}-flags: {flag_count} orbits")
        
        print("  ✓ All verifications passed")

def test_enriques_specific():
    """Test the main Enriques surface case in detail."""
    data = compute_lattice_orbit_data(["U", "2U", "2E8"], 2)
    
    # Verify lattice properties
    assert data.lattice_signature() == (2, 18)
    assert data.lattice_gram_matrix().dimensions() == (20, 20)
    
    # Verify isotropic vectors
    reps = data.orbit_representatives(norm=0)
    for v in reps:
        assert v * data.lattice_gram_matrix() * v == 0
        
    # This should match the paper's results
    print(f"Enriques surface orbit count: {data.orbit_count(0)}")
```

### 4.2 Mathematical Verification
```python
def verify_mathematical_correctness(data):
    """Comprehensive mathematical verification of results."""
    
    # 1. All representatives should have correct norm
    for norm in [0, 2]:
        reps = data.orbit_representatives(norm)
        gram = data.lattice_gram_matrix()
        for v in reps:
            computed_norm = v * gram * v
            assert computed_norm == norm, f"Vector {v} has norm {computed_norm}, expected {norm}"
    
    # 2. Representatives should be inequivalent under automorphism group
    aut_group = data.automorphism_group_data()['generators']
    reps = data.orbit_representatives(0)  # Test isotropic case
    
    for i, v1 in enumerate(reps):
        for j, v2 in enumerate(reps[i+1:], i+1):
            # Check that v1 and v2 are not equivalent under any group element
            equivalent = False
            for g in aut_group[:10]:  # Check first 10 generators (approximation)
                if vector(g * v1) == v2:
                    equivalent = True 
                    break
            assert not equivalent, f"Representatives {i} and {j} are equivalent"
    
    # 3. Automorphism group should preserve the quadratic form
    gram = data.lattice_gram_matrix()
    for g in aut_group:
        g_matrix = matrix(g)
        assert g_matrix * gram * g_matrix.transpose() == gram
```

---

## 5. Output Formats

### 5.1 Table Format Matching Paper
```python
def format_results_table(results_list):
    """
    Format results to match the presentation in the paper.
    """
    table = []
    headers = ["Lattice", "Signature", "Norm 0", "Norm 2", "2-planes", "2-flags", "Aut Group"]
    
    for data in results_list:
        spec_str = " ⊕ ".join(data.lattice_spec)
        signature = f"({data.lattice_signature()[0]}, {data.lattice_signature()[1]})"
        norm_0 = data.orbit_count(0)
        norm_2 = data.orbit_count(2) 
        planes = len(data.isotropic_plane_orbits("plane"))
        flags = len(data.isotropic_plane_orbits("flag"))
        aut_order = data.automorphism_group_data()['order']
        
        row = [spec_str, signature, norm_0, norm_2, planes, flags, str(aut_order)]
        table.append(row)
        
    return format_table(headers, table)  # Returns formatted string

def latex_results_table(results_list):
    """LaTeX table for paper reproduction."""
    # Returns LaTeX tabular environment with all results
```

---

## 6. Success Criteria

### 6.1 Primary Success: Exact Reproduction
- [ ] All 6 test cases from GAP file reproduce exactly
- [ ] Enriques case (["U", "2U", "2E8"]) matches paper's orbit count
- [ ] Verification functions confirm mathematical correctness
- [ ] Table output matches paper's format

### 6.2 Interface Success
- [ ] `compute_lattice_orbit_data()` works for all test cases
- [ ] `reproduce_paper_table()` generates complete results
- [ ] Results integrate cleanly with SageMath objects
- [ ] Verification tests all pass

### 6.3 Performance Success  
- [ ] Each test case completes within reasonable time (< 10 minutes)
- [ ] Enriques case completes within target time (< 5 minutes)
- [ ] Memory usage reasonable for all cases

---

**This specification focuses on the core goal: reproducing the paper's computational results exactly. The interface should make it trivial to verify our implementation against their published data.**