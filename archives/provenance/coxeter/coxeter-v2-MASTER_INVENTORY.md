<!--
Origin: gitclones/Coxeter-v2/MASTER_INVENTORY.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a PROVENANCE RECORD: a corpus map or superseded design plan, kept
so the routing decisions of the migration stay legible. It is not a
statement about the current repository.
-->

# Master Technical Inventory (Coxeter-v2)

This file tracks the consolidated reports from sovereign inventory workers.

## Sovereign Report 1.1: Core Archive
**Source**: `/home/dzack/gitclones/Coxeter-v2/source_archive/background-research/archive/docs-archive/`
**Report Date**: 2026-03-14

### [MATHEMATICAL_THEORY.md]
- Gram matrix signature inheritance -> MATH_CORE.md
- Field theory and cyclotomic extensions -> MATH_CORE.md
- Negative-diagonal convention ($G_{ii} = -2$) -> MATH_CORE.md
- Definiteness classification criteria (Elliptic, Parabolic, Hyperbolic) -> MATH_CORE.md
- Cartan matrix $A_{ij}$ relationship ($A = -G$ for ADE) -> MATH_CORE.md

### [CONVENTIONS.md]
- Bilinear form vs Inner Product terminology distinction -> MATH_CORE.md
- Orthogonality bifurcation (Left vs Right orthogonal complements) -> MATH_CORE.md
- Symmetric-bilinear pairing ($B(v,w) = B(w,v)$) mandate -> ARCHITECTURE.md
- Exact arithmetic mandate (No float epsilon) -> COMPUTATIONAL_RIGOR.md
- Reflection preserved identity formula -> MATH_CORE.md

### [REPEATED_MISTAKE_PATTERNS.md]
- Parabolicity definition failure (Definitions vs Algorithms) -> COMPUTATIONAL_RIGOR.md
- Determinant check vs Explicit Parabolicity check -> COMPUTATIONAL_RIGOR.md
- AA vs Qbar field preference -> COMPUTATIONAL_RIGOR.md

### [OVERVIEW.md]
- Project Focus (Maximal Parabolic Classification) -> MATH_CORE.md
- Algebraic Lattice Notation (Attribute Access L.e, L.f) -> ARCHITECTURE.md
- Lattice Constructors from LaTeX Strings -> MATH_CORE.md

### [TESTING.md]
- Mathematical Correctness Testing (Invariant-Based) -> COMPUTATIONAL_RIGOR.md
- Cross-Validation Strategy (Independent Methods Comparison) -> COMPUTATIONAL_RIGOR.md
- Eigenvalue Monotonicity Verification -> COMPUTATIONAL_RIGOR.md
- Literature Validation (Lannér classification cross-checks) -> COMPUTATIONAL_RIGOR.md
- Integration Testing (SageMath Category Membership) -> ARCHITECTURE.md
- Regression Testing (Finite/Affine Zero-Parabolic Counts) -> COMPUTATIONAL_RIGOR.md
- Test Data Construction (Sage-First Construction Only) -> COMPUTATIONAL_RIGOR.md

## Sovereign Report 1.3: Sage Planning & Foundations
**Source**:  and 
**Report Date**: 2026-03-14

### [BILINEAR_MODULE_CATEGORY_DESIGN.md]
- Category delegation: Adding bilinear form functionality to existng FreeModules -> ARCHITECTURE.md
- Axiom-based hierarchy: CategoryWithAxiom for Symmetric and Definite types -> ARCHITECTURE.md
- Parent method bilinear_form(x, y) requirement -> ARCHITECTURE.md
- Natural Notation operator overload (v * w) -> ARCHITECTURE.md
- BilinearModule as a Parent encapsulating internal _free_module -> ARCHITECTURE.md
- Constructor Factory Pattern (Gram vs Generator) -> ARCHITECTURE.md

### [BILINEAR_MODULES_TDD_PLAN.md]
- Axiom verification in Affine A1: Hyperbolic submatrix extraction -> COMPUTATIONAL_RIGOR.md
- Linearity doctest: B(v+w, v) identity -> COMPUTATIONAL_RIGOR.md
- Cartan property verification for A2 and E8 -> COMPUTATIONAL_RIGOR.md
- Reflection preserved pairing identity test -> COMPUTATIONAL_RIGOR.md

### [foundations/modules/...]
- SymmetricBilRMod category: Symmetric bilinear pairings -> ARCHITECTURE.md
- IntegralLattices category: General Z-module lattices -> ARCHITECTURE.md
- Lattice Invariants (is_even, is_unimodular, level, minimum, genus) -> MATH_CORE.md
- ElementMethods for Lattices (norm, is_primitive, divisibility) -> ARCHITECTURE.md
- Axiomatic Hierarchy (Symmetric, SkewSymmetric, Alternating, Nondegenerate) -> ARCHITECTURE.md
- Definite Modules Axioms (PositiveDefinite, NegativeDefinite, Indefinite) -> ARCHITECTURE.md

### [Miscellaneous]
- Method Injection Patterns (ParentMethods vs ElementMethods) -> ARCHITECTURE.md
- Module-specific Axioms (Free universal property vs WithBasis structure) -> ARCHITECTURE.md

## Sovereign Report 1.4: Legacy Implementation
**Source**:  and 
**Report Date**: 2026-03-14

### [constructors.py]
- Type B, F, G scaling logic (Integral Gram matrix construction) -> src/coxeter/gram.py

### [lattices/lattice.py]
- Inversion of definiteness bridging logic (-G for Sage compatibility) -> src/coxeter/lattice.py
- Dual lattice construction (^*$ via ^{-1}$) -> src/coxeter/lattice.py
- Sublattice induction (^T G B$) -> src/coxeter/lattice.py

### [hyperbolic_root_lattice.py]
- Simple reflection matrix construction ((e_j)$ formula) -> src/coxeter/root_system.py

### [hyperbolic/hyperbolic_root_lattice.py]
- Maximal parabolic subdiagram search (rank n-1 semidefinite subsets) -> src/coxeter/hyperbolic.py
- Cusp correspondence vs finite-volume (Lanner) criteria -> GEOMETRIC_THEORY.md

### [coxeter_matrices.py]
- Gram-to-Coxeter conversion formula ($\cos(\pi/m)$) -> MATH_CORE.md

### [root_systems/root_lattice.py]
- Fundamental weights as rows of ^{-1}$ -> src/coxeter/root_system.py
I will begin by listing the files in the specified directories to identify all markdown files for analysis.

I will list the contents of the subdirectories within `homotopy_theory/` to ensure I find all relevant markdown files.

I will list the contents of the `explorations/connections/` directory to ensure I haven't missed any markdown files before I begin reading and extracting information.

I will list the contents of the `explorations/connections/homotopy_theory/` directory to check for any markdown files.

I will read the markdown files in `archive/homotopy_theory/` and `explorations/` to extract "Mathematical Idea Blocks" as requested.

I will continue reading the remaining markdown files in `archive/homotopy_theory/` to extract more "Mathematical Idea Blocks."

I will now read the markdown files in the `explorations/` directory to gather additional "Mathematical Idea Blocks" and insights.

### Sovereign Inventory Report: Homotopy & Research Archives

This report identifies and extracts "Mathematical Idea Blocks" from the `homotopy_theory` and `explorations` archives, categorized by their primary technical focus and suggested destinations.

---

#### 1. Categorical & Homotopical Theory ([ARCHITECTURE.md])

*   **[README.md]**: The derived category $D(\text{Bil}R\text{-Mod})$ is the homotopy category of a stable $\infty$-category. $\rightarrow$ **ARCHITECTURE.md**
*   **[README.md]**: Suspension functor $\Sigma M = H \oplus M \oplus H$, where $H$ is the hyperbolic plane. $\rightarrow$ **ARCHITECTURE.md**
*   **[README.md]**: $Sp(\text{Bil}R\text{-Mod})$ is the stabilization ( $\infty$-categorical colimit) of the sequence $\text{Bil}R\text{-Mod} \xrightarrow{\Sigma} \text{Bil}R\text{-Mod} \xrightarrow{\Sigma} \dots$ $\rightarrow$ **ARCHITECTURE.md**
*   **[derived_functor_computations.md]**: Bar construction with hyperbolic planes provides explicit resolutions: $\dots \to H \otimes H \otimes M \to H \otimes M \to M \to 0$. $\rightarrow$ **ARCHITECTURE.md**
*   **[derived_functor_computations.md]**: Simplicial spectral sequence for Ext: $E_1^{p,q} = Ext^q(B_p(M), N) \implies Ext^{p+q}(M, N)$ where $B_p(M) = H^{\otimes p} \otimes M$. $\rightarrow$ **ARCHITECTURE.md**
*   **[dold_kan_bilinear.md]**: Dold-Kan equivalence for bilinear modules: $Ch_{\ge 0}(\text{Bil}R\text{-Mod}) \simeq s\text{Bil}R\text{-Mod}$. $\rightarrow$ **ARCHITECTURE.md**
*   **[dold_kan_bilinear.md]**: Normalized chain complex $N(X)_n = \cap_{i=1}^n \text{ker}(d_i: X_n \to X_{n-1})$. $\rightarrow$ **ARCHITECTURE.md**
*   **[dold_kan_bilinear.md]**: Stable Dold-Kan: $Sp^\Sigma(\text{Bil}R\text{-Mod}) \simeq \text{Fun}(Fin_*, \text{Bil}R\text{-Mod})$. $\rightarrow$ **ARCHITECTURE.md**
*   **[bilinear_infinity_category.md]**: $\text{Bil}R\text{-Mod}^\infty$ is a presentable $\infty$-category, accessible and generated by $\kappa$-compact objects. $\rightarrow$ **ARCHITECTURE.md**
*   **[bilinear_infinity_category.md]**: Derived tensor product $M \otimes^L N$ and derived internal hom $RHom(M, N)$ satisfy tensor-hom adjunction in the $\infty$-category. $\rightarrow$ **ARCHITECTURE.md**
*   **[bilinear_infinity_category.md]**: Standard t-structure on $\text{Bil}R\text{-Mod}^\infty$ with heart equivalent to the abelian category $\text{Bil}R\text{-Mod}$. $\rightarrow$ **ARCHITECTURE.md**
*   **[bilr_mod_model_structure.md]**: Projective model structure on $Ch(\text{Bil}R\text{-Mod})$ where cofibrant objects are "homotopy-free" (built from free cells/hyperbolic disks). $\rightarrow$ **ARCHITECTURE.md**
*   **[bilr_mod_model_structure.md]**: Free bilinear module spectrum on a spectrum $E$ is defined as $\Sigma^\infty(E) \wedge H$. $\rightarrow$ **ARCHITECTURE.md**
*   **[bilr_mod_model_structure.md]**: In the stable setting $Sp(\text{Bil}R\text{-Mod})$, every object becomes "free" after sufficient suspensions as suspension adds hyperbolic summands. $\rightarrow$ **ARCHITECTURE.md**
*   **[bilinear_module_spectra.md]**: Smash product of spectra $E \wedge F = \text{colim}_{i+j \to n} E_i \otimes_{\text{Bil}R} F_j$. $\rightarrow$ **ARCHITECTURE.md**
*   **[bilinear_module_spectra.md]**: Topological Hochschild Homology (THH) for bilinear ring spectra: $THH(R) = R \wedge_{R \wedge R^{op}} R$. $\rightarrow$ **ARCHITECTURE.md**
*   **[suspension_functor.md]**: Stabilization functor $\text{Bil}R\text{-Mod} \to Sp(\text{Bil}R\text{-Mod})$ is the $\infty$-categorical colimit of the suspension diagram. $\rightarrow$ **ARCHITECTURE.md**

---

#### 2. Geometric Conjectures & Explorations ([GEOMETRIC_THEORY.md])

*   **[alternative-approaches.md]**: Galois Theory Approach: Systematic study of Galois actions on classification results to see how field automorphisms permute maximal parabolics. $\rightarrow$ **GEOMETRIC_THEORY.md**
*   **[alternative-approaches.md]**: Topological Methods: Association of simplicial complexes (e.g., order complex of parabolic subdiagram poset) to Coxeter diagrams. $\rightarrow$ **GEOMETRIC_THEORY.md**
*   **[open-questions.md]**: Conjecture: The number of maximal parabolic subdiagrams is Galois-invariant for non-crystallographic types. $\rightarrow$ **GEOMETRIC_THEORY.md**
*   **[open-questions.md]**: Exploration of Motivic Homotopy Theory: Motivic aspects of quadratic forms and $A^1$-homotopy theory over various fields in the context of Coxeter groups. $\rightarrow$ **GEOMETRIC_THEORY.md**
*   **[research-notes.md]**: Investigation into regularized theta series for indefinite/hyperbolic lattices to study their modular properties. $\rightarrow$ **GEOMETRIC_THEORY.md**
*   **[research-notes.md]**: Exploration of the connection between arithmetic properties of finite covolume hyperbolic Coxeter groups and their maximal parabolic structure. $\rightarrow$ **GEOMETRIC_THEORY.md**
