<!--
Origin: gitclones/Coxeter/research/explorations/implementation-notes/sagemath_rmodule_deficiencies.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is an ALGORITHM/REQUIREMENT SURVEY written against SageMath as it
stood in the source tree. Rows now owned by the preamble, and errors the
audit recorded, are listed in the README.md of this directory.
-->

# SageMath R-Module Implementation Deficiencies

In SageMath's implementation of **R-modules**, particularly **free modules** via `FreeModule(R, n)`, many core operations are well-supported — but several **mathematically natural operations** are notably **missing** or only partially implemented, especially when working over general commutative rings. Below is a list of **expected features from basic module theory** that are either **missing**, **incomplete**, or require manual implementation.

---

## ❌ Missing or Incomplete Features

### 1. **Tensor product of modules**

* Sage lacks a built-in general `M.tensor_product(N)` method for arbitrary (even free) R-modules.
* Only partially supported for **vector spaces** and certain **multilinear settings** (via `tensor_module(...)`), but **not** for general R-modules.
* No canonical way to compute $M \otimes_R N$ as an R-module.

**Example of what's missing:**
```sage
# This should work but doesn't:
sage: M = FreeModule(ZZ, 2)
sage: N = FreeModule(ZZ, 3)
sage: T = M.tensor_product(N)  # AttributeError
```

### 2. **Hom module: $\mathrm{Hom}_R(M, N)$**

* There is no `hom_module(M, N)` function returning the R-module of R-linear maps from $M \to N$.
* You must define explicit morphisms manually using `module_morphism(...)` and no general structure (e.g., free basis for Hom) is constructed.

**What's missing:**
```sage
# This should work:
sage: M = FreeModule(ZZ, 2)
sage: N = FreeModule(ZZ, 3)
sage: H = hom_module(M, N)  # Should return ZZ^6 ≅ Hom(ZZ^2, ZZ^3)
sage: H.rank()  # Should be 6
```

### 3. **Ext and Tor functors**

* Standard homological constructions like $\mathrm{Ext}^i_R(M, N)$ or $\mathrm{Tor}_i^R(M, N)$ are not available, even over PIDs or $\mathbb{Z}$.
* No built-in projective/injective resolution machinery for modules over general rings.

**Missing homological algebra:**
```sage
# These fundamental functors don't exist:
sage: M = ZZ/6
sage: N = ZZ/4  
sage: Tor(1, M, N)  # Should compute Tor_1^Z(Z/6, Z/4) ≅ Z/2
sage: Ext(1, M, N)  # Should compute Ext_1^Z(Z/6, Z/4) ≅ Z/2
```

### 4. **Dual module $M^* = \mathrm{Hom}_R(M, R)$**

* Not directly implemented. There is no `.dual()` method for modules.
* Users must construct Hom spaces manually using basis extraction and transpose tricks.

**What should work:**
```sage
# This natural operation is missing:
sage: M = FreeModule(ZZ, 3)
sage: M_dual = M.dual()  # Should return Hom_ZZ(M, ZZ) ≅ ZZ^3
sage: M_dual.rank()  # Should be 3
```

### 5. **General submodule lattice operations**

* While `.submodule(...)` exists, there's no built-in:
  * `M.submodules()` (enumerate all submodules, even for small rank)
  * `M.intersection(N)`
  * `M.sum(N)`, `M + N`
* Sage lacks a rich submodule lattice API.

**Missing lattice operations:**
```sage
# These basic operations don't exist:
sage: M = FreeModule(ZZ, 3)
sage: S = M.submodule([M.0 + M.1, M.1 + M.2])
sage: T = M.submodule([M.0 + M.2, 2*M.1])
sage: S.intersection(T)  # AttributeError
sage: S + T  # Should return S.sum(T)
sage: M.submodules()  # Should enumerate submodules (finite for finite rank)
```

### 6. **Exact sequence tools**

* No native support for:
  * Exactness checking
  * Diagram chasing
  * Snake lemma, five lemma, etc.
  * Computing kernels, images, and cokernels together in chain complexes
* All must be done manually via matrices.

**Missing sequence tools:**
```sage
# No exact sequence support:
sage: # Want: is_exact([f1, f2, f3]) for morphisms f1: A→B, f2: B→C, f3: C→D
sage: # Want: snake_lemma(diagram) for commutative diagrams
sage: # Want: ChainComplex([f1, f2, f3]) with homology computation
```

### 7. **Saturation and integral closure** (over Dedekind domains, etc.)

* No saturation operation $\overline{M} \subset R^n$ s.t. $\overline{M} \otimes \mathbb{Q} = M \otimes \mathbb{Q}$.
* Important in applications to modular forms and lattice theory.

**Missing for number theory:**
```sage
# This operation is crucial for lattices:
sage: R = ZZ
sage: M = R^3.submodule([R^3([2, 1, 0]), R^3([0, 3, 1])])
sage: M_sat = M.saturation()  # Should compute integral closure
```

### 8. **Finitely presented module objects**

* There is no standard `FinitelyPresentedModule(R, M_matrix, rel_matrix)` API analogous to `FinitelyPresentedGroup(...)`.
* You must use raw cokernels of matrices in $R^n$, and there's no coherent object to wrap presentations or compute syzygies directly.

**Missing presentation API:**
```sage
# Should be able to define modules by generators and relations:
sage: R = ZZ
sage: # Want: M = FinitelyPresentedModule(R, gens=3, rels=[[2,1,0],[0,3,1]])
sage: # This would represent R^3/(2e1+e2, 3e2+e3) automatically
```

### 9. **Minimal presentation and syzygy modules**

* No method like `M.minimal_presentation()` or `M.syzygy_module()`, unless working over polynomial rings via `Singular`.

**Missing for computational commutative algebra:**
```sage
# These should exist for any finitely generated module:
sage: M = some_module()
sage: P = M.minimal_presentation()  # Minimize generators and relations
sage: S = M.syzygy_module()  # First syzygy module
sage: S2 = M.syzygy_module(2)  # Second syzygy module
```

### 10. **Direct sum decomposition**

* No canonical decomposition of a finitely generated module into indecomposables over $\mathbb{Z}$ or PID.
* For example, computing elementary divisors or invariant factors is possible for matrices, but there's no module abstraction wrapping this.

**Missing structure theorem:**
```sage
# Should automatically decompose modules over PIDs:
sage: M = some_finitely_generated_module_over_ZZ()
sage: decomp = M.primary_decomposition()  # Z/d1 ⊕ Z/d2 ⊕ ... ⊕ Z^r
sage: cyclic_parts = M.cyclic_decomposition()  # Elementary divisor form
sage: invariant_factors = M.invariant_factors()  # [d1, d2, ..., dn]
```

---

## Summary of Notable Gaps

| Operation                    | Status        | Impact |
| ---------------------------- | ------------- | ------ |
| $M \otimes_R N$              | ❌ Missing     | High - fundamental construction |
| $\mathrm{Hom}_R(M, N)$       | ❌ Missing     | High - needed for duality |
| $\mathrm{Ext}, \mathrm{Tor}$ | ❌ Missing     | High - homological algebra |
| Dual module $M^*$            | ❌ Missing     | Medium - linear algebra |
| Submodule intersection/sum   | ⚠ Manual only | Medium - lattice operations |
| Exact sequence tools         | ❌ Missing     | High - fundamental for homology |
| Saturation                   | ❌ Missing     | Medium - number theory applications |
| Syzygy modules               | ❌ Missing     | Medium - commutative algebra |
| Minimal presentations        | ❌ Missing     | Medium - computational optimization |
| Indecomposable decomposition | ❌ Missing     | Medium - structure theory |

---

## Comparison with Other Systems

### Advantages of Other Systems:

* **Macaulay2**: Excellent support for graded modules, syzygies, Ext/Tor over polynomial rings
* **GAP**: Strong homological algebra package, excellent for group cohomology and module theory
* **Magma**: Comprehensive module theory over arbitrary rings, including advanced homological constructions
* **CoCalc/Singular**: Via Sage's Singular interface, some polynomial ring modules are better supported

### Sage's Current Strengths:

* **Matrix computations**: Excellent for concrete linear algebra over various rings
* **Free modules**: Good basic support for $R^n$ with explicit coordinates
* **Vector spaces**: Complete implementation over fields
* **Integration**: Works well with other Sage systems (number theory, algebraic geometry)

---

## Workarounds Currently Required

To compensate for these missing features, users often:

1. **Work over PIDs**: Restrict to $\mathbb{Z}$, $\mathbb{F}_p$, or $\mathbb{Q}$ and manipulate matrices directly
2. **Use Singular integration**: `M.module()` when working over polynomial rings  
3. **Manual implementation**: Implement basic homological algebra manually (e.g., computing Tor via tensoring with free resolutions)
4. **Matrix-based approaches**: Use Smith normal form and matrix operations instead of module abstractions
5. **External packages**: Use specialized packages for specific applications (e.g., lattice packages for number theory)

### Example Manual Implementation:

```sage
# Manual tensor product over ZZ:
def tensor_product_ZZ(M, N):
    """Compute M ⊗_Z N for free Z-modules M, N"""
    if not (M.base_ring() == ZZ and N.base_ring() == ZZ):
        raise ValueError("Only implemented for Z-modules")
    
    m_rank = M.rank()
    n_rank = N.rank()
    
    # Create Z^(m_rank * n_rank)
    T = FreeModule(ZZ, m_rank * n_rank)
    
    # Define the tensor product structure
    def tensor_element(m_coords, n_coords):
        # Kronecker product of coordinate vectors
        return T([m_i * n_j for m_i in m_coords for n_j in n_coords])
    
    return T, tensor_element

# Usage:
sage: M = FreeModule(ZZ, 2)
sage: N = FreeModule(ZZ, 3)  
sage: T, tensor = tensor_product_ZZ(M, N)
sage: T.rank()  # 6, as expected
6
```

---

## Implications for Mathematical Software Development

These deficiencies highlight the need for:

1. **Categorical approach**: Module categories with proper functorial operations
2. **Homological algebra package**: Systematic support for derived functors
3. **General ring support**: Moving beyond the current focus on PIDs and fields
4. **API consistency**: Uniform interface for module operations across different base rings
5. **Performance optimization**: Efficient algorithms for large-scale module computations

The missing features represent significant gaps in SageMath's coverage of standard undergraduate and graduate-level module theory, particularly impacting research in commutative algebra, homological algebra, and algebraic number theory.