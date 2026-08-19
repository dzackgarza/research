<!-- Absorbed from the Coxeter research corpus on 2026-08-20 under
     PLAN-coxeter-deletion-audit-registry (reader H). The body below is the
     source document, unchanged. -->

> **Origin.** `Coxeter/research/explorations/connections/homotopy_theory/dold_kan/dold_kan_bilinear.md`
>
> **Preamble status.** Absent. Neither simplicial objects nor chain complexes exist in the preamble.
>
> **Recorded error.** The Dold-Kan correspondence is an equivalence between simplicial objects and non-negatively graded chain complexes in an *abelian* category; its normalization is an intersection of kernels and its differential is an alternating sum of face maps, both of which require an additive structure on the homsets. The document applies it to the formed-module category without establishing that hypothesis, and it does not hold with form-preserving morphisms (INDEX.md).

---

# Dold-Kan Correspondence for Bilinear Modules

The Dold-Kan correspondence provides an equivalence between non-negative chain complexes and simplicial objects, adapted here for bilinear modules.

## The Basic Correspondence

```python
class DoldKanEquivalence:
    r"""
    The Dold-Kan equivalence for bilinear modules:
    
    Ch≥0(BilR-Mod) ≃ sBilR-Mod
    
    Between non-negative chain complexes and simplicial bilinear modules.
    """
    
    @staticmethod
    def normalized_chains(X):
        r"""
        The normalized chain complex N(X) of a simplicial bilinear module.
        
        N(X)_n = ∩_{i=1}^n ker(d_i: X_n → X_{n-1})
        
        This is the submodule of non-degenerate n-simplices.
        
        The differential is d_0: N(X)_n → N(X)_{n-1}.
        
        EXAMPLES::
        
            sage: # Simplicial bilinear module from nerve of category
            sage: X = nerve_of_category(BilR_Mod_finite)
            sage: NX = DoldKanEquivalence.normalized_chains(X)
            sage: 
            sage: # NX is a chain complex
            sage: # NX_0 = objects (bilinear modules)
            sage: # NX_1 = morphisms
            sage: # NX_2 = composable pairs
            sage: # with appropriate differentials
        """
        # Extract non-degenerate simplices
        N_n = X.non_degenerate_simplices(n)
        # Differential is remaining face map
        d = X.face_map(0)
        return ChainComplex(N_n, d)
    
    @staticmethod
    def denormalization(C):
        r"""
        Convert chain complex C to simplicial bilinear module K(C).
        
        K(C)_n = ⊕_{[n] ↠ [p]} C_p
        
        The sum is over all surjections [n] → [p] in Δ.
        
        EXAMPLES::
        
            sage: # Start with projective resolution
            sage: M = BilinearModule(matrix(ZZ, [[6]]))
            sage: P = M.projective_resolution()  # ... → H → H → M → 0
            sage: 
            sage: # Convert to simplicial object
            sage: X = DoldKanEquivalence.denormalization(P)
            sage: # X_n has many copies of each P_i
            sage: # Organized by degeneracy operators
        """
        def K_n(n):
            # Direct sum over surjections [n] → [p]
            result = BilinearModule.zero()
            for p in range(n+1):
                for surj in surjections(n, p):
                    result = result.direct_sum(C[p])
            return result
        
        # Define face and degeneracy maps
        return SimplicialBilinearModule(K_n, faces, degeneracies)
```

## Simplicial Bilinear Modules

```python
class SimplicialBilinearModule:
    r"""
    A simplicial object in BilR-Mod.
    
    This is a functor X: Δ^op → BilR-Mod where Δ is the simplex category.
    """
    
    def __init__(self, objects, face_maps, degeneracy_maps):
        """
        INPUT:
        - objects: Function n ↦ X_n (bilinear module of n-simplices)
        - face_maps: d_i: X_n → X_{n-1} for 0 ≤ i ≤ n
        - degeneracy_maps: s_i: X_n → X_{n+1} for 0 ≤ i ≤ n
        """
        self.objects = objects
        self.face_maps = face_maps
        self.degeneracy_maps = degeneracy_maps
        self._check_simplicial_identities()
    
    def geometric_realization(self):
        r"""
        The geometric realization |X| as a bilinear module spectrum.
        
        |X| = colim_Δ (X_n × Δ^n)
        
        where Δ^n is the standard n-simplex.
        
        This gives a bilinear module spectrum whose homotopy groups
        are the homology of the associated chain complex.
        """
        # Take coend over simplex category
        pass
    
    def moore_complex(self):
        r"""
        The Moore complex - non-normalized version of chain complex.
        
        M(X)_n = X_n
        d = Σ_{i=0}^n (-1)^i d_i
        
        Quasi-isomorphic to normalized chains N(X).
        """
        pass
```

## Kan Complexes in BilR-Mod

```python
class KanBilinearModule(SimplicialBilinearModule):
    r"""
    A Kan complex in BilR-Mod - a simplicial bilinear module satisfying
    the Kan extension condition.
    
    These are the fibrant objects in the model structure on sBilR-Mod.
    """
    
    def is_kan(self):
        r"""
        Check if this satisfies the Kan extension property.
        
        For every horn Λ^n_k → X, there exists a filler Δ^n → X.
        
        In BilR-Mod context: Given n-1 faces of a simplex that match
        on overlaps, can we fill in the missing face and interior?
        """
        # Check horn filling for all dimensions and faces
        pass
    
    def homotopy_groups(self, basepoint):
        r"""
        The homotopy groups π_n(X, x) for a Kan complex.
        
        π_n(X, x) = [(Δ^n, ∂Δ^n), (X, x)]
        
        These are bilinear modules, not just abelian groups!
        
        EXAMPLES::
        
            sage: # Kan complex from classifying space
            sage: X = classifying_space_bilinear(OrthogonalGroup(H))
            sage: pi_1 = X.homotopy_groups(1, basepoint=H)
            sage: # π_1 ≅ O(H) as a group
            sage: 
            sage: pi_2 = X.homotopy_groups(2, basepoint=H)
            sage: # π_2 measures automorphisms of automorphisms
        """
        pass
```

## Applications to Free Resolutions

```python
class DoldKanResolutions:
    r"""
    Use Dold-Kan to understand resolutions in BilR-Mod.
    """
    
    @staticmethod
    def bar_resolution_simplicial(M):
        r"""
        The bar resolution as a simplicial bilinear module.
        
        B(M)_n = H^{⊗(n+1)} ⊗ M
        
        where H is the hyperbolic plane (our "free" module).
        
        Face maps: d_i removes the i-th tensor factor
        Degeneracy maps: s_i doubles the i-th tensor factor
        
        EXAMPLES::
        
            sage: M = BilinearModule(matrix(ZZ, [[2]]))
            sage: B = DoldKanResolutions.bar_resolution_simplicial(M)
            sage: 
            sage: # B is a simplicial resolution of M by free modules
            sage: # Taking normalized chains gives projective resolution
            sage: P = DoldKanEquivalence.normalized_chains(B)
            sage: # P: ... → H⊗H⊗M → H⊗M → M
        """
        def B_n(n):
            # n+1 tensor factors of H, then tensor with M
            H = BilinearModule.hyperbolic_plane()
            result = M
            for i in range(n+1):
                result = H.tensor_product(result)
            return result
        
        # Standard bar construction face/degeneracy maps
        return SimplicialBilinearModule(B_n, bar_faces, bar_degeneracies)
    
    @staticmethod
    def kan_extension_resolution(M):
        r"""
        Build a resolution using Kan extension property.
        
        Start with M in degree 0, then use Kan extension to fill in
        higher degrees with free modules.
        
        This gives a "minimal" way to resolve M by free modules.
        """
        pass
```

## Homotopy Theory via Dold-Kan

```python
class HomotopyViaDoldKan:
    r"""
    Use Dold-Kan to do homotopy theory of bilinear modules.
    """
    
    @staticmethod
    def eilenberg_maclane_bilinear(M, n):
        r"""
        The Eilenberg-MacLane object K(M, n) in sBilR-Mod.
        
        This is a Kan complex with:
        - π_n(K(M, n)) = M
        - π_i(K(M, n)) = 0 for i ≠ n
        
        Under Dold-Kan, this corresponds to M concentrated in degree n.
        
        EXAMPLES::
        
            sage: # K(Z, 1) with form [2]
            sage: M = BilinearModule(matrix(ZZ, [[2]]))
            sage: K_M_1 = HomotopyViaDoldKan.eilenberg_maclane_bilinear(M, 1)
            sage: 
            sage: # This represents cohomology with coefficients in M
            sage: # H^1(X; M) = [X, K(M, 1)]
        """
        # Chain complex with M in degree n only
        C = ChainComplex({n: M})
        # Convert to simplicial via Dold-Kan
        return DoldKanEquivalence.denormalization(C)
    
    @staticmethod
    def postnikov_tower_simplicial(X):
        r"""
        Build Postnikov tower using simplicial techniques.
        
        ... → P_2 X → P_1 X → P_0 X
        
        where P_n X has π_i = 0 for i > n.
        
        Each stage is a principal fibration with fiber K(π_n(X), n).
        """
        pass
    
    @staticmethod
    def spectral_sequence_from_simplicial(X):
        r"""
        The spectral sequence of a simplicial bilinear module.
        
        E^1_{p,q} = H_q(X_p) ⇒ H_{p+q}(|X|)
        
        This computes homology of geometric realization from
        homology of individual simplices.
        """
        pass
```

## The Stable Dold-Kan

```python
class StableDoldKan:
    r"""
    Dold-Kan in the stable setting - for bilinear module spectra.
    """
    
    @staticmethod
    def symmetric_spectra_dold_kan():
        r"""
        For symmetric spectra:
        
        Sp^Σ(BilR-Mod) ≃ Fun(Fin_*, BilR-Mod)
        
        where Fin_* is the category of finite pointed sets with 
        symmetric group actions.
        
        This is a generalization of Dold-Kan to the stable setting.
        """
        pass
    
    @staticmethod
    def infinity_dold_kan():
        r"""
        The ∞-categorical Dold-Kan:
        
        Fun(Δ^op, BilR-Mod^∞) ≃ Ch≥0(BilR-Mod^∞)
        
        This equivalence of ∞-categories preserves all homotopical 
        information, not just the homotopy category.
        """
        pass
```

This shows how Dold-Kan lets us use simplicial techniques to understand chain complexes of bilinear modules, giving us powerful tools for homotopy theory!