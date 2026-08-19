<!-- Absorbed from the Coxeter research corpus on 2026-08-20 under
     PLAN-coxeter-deletion-audit-registry (reader H). The body below is the
     source document, unchanged. -->

> **Origin.** `Coxeter/research/explorations/connections/homotopy_theory/suspension/suspension_functor.md`
>
> **Preamble status.** Absent. The orthogonal sum itself is owned (`direct_sum` on integral lattices, used throughout `catalogue.sage`), so the underlying operation exists; the functor, its prospective right adjoint, and prespectra do not.
>
> **Recorded error.** The document gives three inequivalent descriptions of one functor. The class docstring says the underlying module of the suspension is `R + M + R`; the method docstring says the suspension is `H + M + H`; the worked example reports rank 3 and Gram matrix `[[0,1,0],[1,0,0],[0,0,2]]` for a rank-1 input, which is `H + M`. Only the third is internally consistent with the printed Gram matrix. Separately, `desuspension_when_possible` presumes hyperbolic summands split off canonically; over ZZ the number of hyperbolic summands that split from a fixed lattice is not an invariant of an isomorphism class in general, so the stated inverse is not well defined without a hypothesis the document does not give.

---

# Interface: Suspension Functor for Bilinear Modules

The suspension functor that allows us to build the stable ∞-category of bilinear module spectra.

## Basic Suspension

```python
class BilinearModuleSuspension:
    r"""
    The suspension functor Σ: BilR-Mod → BilR-Mod.
    
    For a bilinear module (M, b), the suspension ΣM has:
    - Underlying module: R ⊕ M ⊕ R
    - Bilinear form: Hyperbolic extension of b
    
    This is the categorical suspension, not just the topological one.
    """
    
    @staticmethod
    def suspend(M):
        r"""
        Suspend a bilinear module by adding hyperbolic summands.
        
        The suspension ΣM = H ⊕ M ⊕ H where H is the hyperbolic plane.
        
        INPUT:
        - M: A bilinear module (M, b)
        
        OUTPUT:
        - ΣM: The suspended bilinear module
        
        EXAMPLES::
        
            sage: M = BilinearModule(matrix(ZZ, [[2]]))
            sage: SM = BilinearModuleSuspension.suspend(M)
            sage: SM.rank()
            3  # Original rank 1 + 2 from hyperbolic summands
            sage: SM.gram_matrix()
            [0 1 0]
            [1 0 0]
            [0 0 2]
            
            sage: # Suspension is functorial
            sage: f = M.hom(M, {M.0: 2*M.0})
            sage: Sf = BilinearModuleSuspension.suspend_morphism(f)
            sage: Sf.domain() == SM
            True
        """
        # Add hyperbolic plane at both ends
        H = BilinearModule.hyperbolic_plane()
        return H.orthogonal_sum(M).orthogonal_sum(H)
    
    @staticmethod
    def suspend_morphism(f):
        r"""
        Apply suspension to a morphism f: M → N.
        
        Returns Σf: ΣM → ΣN.
        """
        # Extend by identity on hyperbolic summands
        pass
    
    @staticmethod
    def desuspension_when_possible(M):
        r"""
        The desuspension Σ^{-1}M when M has hyperbolic summands.
        
        This is only defined on the subcategory of suspendable modules.
        """
        # Check for hyperbolic direct summands
        # Remove them if present
        pass
```

## Iterated Suspension and Spectrum Objects

```python
class BilinearModulePreSpectrum:
    r"""
    A prespectrum in BilR-Mod: a sequence of bilinear modules with structure maps.
    
    E = (E_n, ε_n) where:
    - E_n is a bilinear module for each n ≥ 0
    - ε_n: E_n → ΩE_{n+1} are structure maps (adjoint to ΣE_n → E_{n+1})
    
    Here Ω is the loop functor (right adjoint to suspension).
    """
    
    def __init__(self, modules, structure_maps):
        """
        INPUT:
        - modules: Dict n ↦ E_n (bilinear modules)
        - structure_maps: Dict n ↦ ε_n: E_n → ΩE_{n+1}
        """
        self.modules = modules
        self.structure_maps = structure_maps
        self._check_spectrum_axioms()
    
    def is_omega_spectrum(self):
        r"""
        Check if this is an Ω-spectrum (all structure maps are equivalences).
        
        In the stable ∞-category, every spectrum can be replaced by an Ω-spectrum.
        """
        return all(self.structure_maps[n].is_equivalence() 
                  for n in self.structure_maps)
    
    def suspension_spectrum(M):
        r"""
        The suspension spectrum Σ^∞M of a bilinear module M.
        
        This is the free spectrum on M:
        (Σ^∞M)_n = Σ^n M for n ≥ 0
        """
        modules = {}
        maps = {}
        current = M
        
        for n in range(10):  # Compute first 10 levels
            modules[n] = current
            current = BilinearModuleSuspension.suspend(current)
            # Structure map is adjoint to identity ΣE_n → E_{n+1}
            maps[n] = BilinearModuleSuspension.adjoint_structure_map(
                modules[n], modules[n+1]
            )
        
        return BilinearModulePreSpectrum(modules, maps)
```

## The Stable ∞-Category

```python
class StableBilinearModuleCategory:
    r"""
    The stable ∞-category Sp(BilR-Mod) of bilinear module spectra.
    
    This is the ∞-categorical colimit of:
    BilR-Mod --Σ--> BilR-Mod --Σ--> BilR-Mod --Σ--> ...
    
    Objects: Spectra of bilinear modules
    Morphisms: Derived from sequences of maps compatible with suspension
    
    Key properties:
    - Has all finite limits and colimits
    - Suspension is an equivalence
    - Distinguished triangles from mapping cones
    - Enriched over spectra
    """
    
    def hom_spectrum(self, E, F):
        r"""
        The mapping spectrum Hom(E, F) between two bilinear module spectra.
        
        This is itself a spectrum with:
        Hom(E, F)_n = holim_k Hom_{BilR-Mod}(E_k, F_{n+k})
        """
        pass
    
    def smash_product(self, E, F):
        r"""
        The smash product E ∧ F of bilinear module spectra.
        
        This is the tensor product in the stable ∞-category.
        (E ∧ F)_n = colim_{i+j=n} E_i ⊗_{BilR-Mod} F_j
        """
        pass
    
    def mapping_cone(self, f):
        r"""
        The mapping cone C(f) of a map f: E → F of spectra.
        
        Fits into a distinguished triangle:
        E --f--> F --> C(f) --> ΣE
        """
        pass
    
    def homotopy_groups(self, E):
        r"""
        The homotopy groups π_*(E) of a bilinear module spectrum.
        
        π_n(E) = colim_k Hom_{Ho(BilR-Mod)}(Σ^k M, E_{n+k})
        
        where M is the unit bilinear module.
        """
        pass
```

## Stabilization and Infinity Structure

```python
class BilinearModuleInfinityStructure:
    r"""
    The ∞-categorical structure on bilinear module spectra.
    
    This encodes:
    - Higher morphisms (homotopies between homotopies)
    - Coherence data for compositions
    - ∞-categorical limits and colimits
    """
    
    def stabilization_functor(self):
        r"""
        The stabilization functor BilR-Mod → Sp(BilR-Mod).
        
        This is the ∞-categorical colimit of the suspension diagram.
        It's the left adjoint to the 0th space functor.
        """
        pass
    
    def infinite_loop_space(self, E):
        r"""
        The infinite loop space structure Ω^∞E.
        
        For a bilinear module spectrum E, this recovers the underlying
        bilinear module with additional coherent group structure.
        """
        pass
    
    def postnikov_tower(self, E):
        r"""
        The Postnikov tower of a bilinear module spectrum.
        
        ... → P_2 E → P_1 E → P_0 E
        
        where P_n E has π_k = 0 for k > n.
        """
        pass
```

## Connection to Classical Homological Algebra

```python
def derived_category_via_spectra(R):
    r"""
    Realize D(BilR-Mod) as the homotopy category of HR-module spectra.
    
    The Eilenberg-MacLane spectrum HR gives:
    - HR-modules ≃ D(R-Mod)
    - Bilinear HR-modules ≃ D(BilR-Mod)
    
    This recovers Ext and Tor as homotopy groups of mapping spectra.
    """
    pass

def spectral_sequence_from_filtration(E, filtration):
    r"""
    Construct spectral sequences from filtered bilinear module spectra.
    
    A filtration ... ⊆ F_2 E ⊆ F_1 E ⊆ F_0 E = E gives rise to:
    - Associated graded spectrum gr(E)
    - Spectral sequence converging to π_*(E)
    
    This modernizes classical spectral sequences via stable homotopy theory.
    """
    pass
```