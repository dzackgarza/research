<!--
Origin: gitclones/Coxeter/research/archive/sage_integration/bilinear_chain_complex_extension.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences and recorded errors are listed in the INDEX.md of this
corpus.
-->

# Extending SageMath's Chain Complexes for Bilinear Modules

## Current SageMath Capabilities

SageMath already has:
1. **ChainComplex** class with tensor products and Hom functors
2. **Free resolutions** for polynomial ideals  
3. **QuadraticForm** class (but limited bilinear form support)
4. **Group cohomology** that uses bar resolutions internally

## Proposed Extension: BilinearChainComplex

```python
from sage.homology.chain_complex import ChainComplex
from sage.matrix.constructor import matrix

class BilinearChainComplex:
    """
    A chain complex of bilinear modules.
    
    This extends SageMath's ChainComplex by tracking bilinear forms
    at each degree and ensuring differentials preserve these forms.
    """
    
    def __init__(self, base_ring, differentials, forms, degree=-1):
        """
        INPUT:
        - base_ring: The ring R
        - differentials: Dict {i: matrix} for d_i: C_i → C_{i+degree}
        - forms: Dict {i: matrix} for bilinear form on C_i
        - degree: The degree of differentials (usually -1)
        
        EXAMPLES::
        
            sage: # Create the bar resolution of Z/2Z with forms
            sage: R = ZZ
            sage: H = matrix(ZZ, [[0, 1], [1, 0]])  # Hyperbolic form
            sage: 
            sage: # C_0 = Z/2Z with form [1]
            sage: # C_1 = H ⊗ Z/2Z with induced form
            sage: # d_1: C_1 → C_0 is the counit
            sage: 
            sage: forms = {0: matrix([[1]]), 1: H}
            sage: diffs = {1: counit_matrix}
            sage: BC = BilinearChainComplex(ZZ, diffs, forms)
        """
        self.chain = ChainComplex(differentials, base_ring=base_ring, degree=degree)
        self.forms = forms
        self.base_ring = base_ring
        self._check_form_preservation()
    
    def _check_form_preservation(self):
        """
        Verify that differentials preserve bilinear forms.
        
        For d: (C, b_C) → (D, b_D), we need:
        b_D(d(x), d(y)) = b_C(x, y) for all x, y
        """
        for i, d in self.chain.differential().items():
            if i in self.forms and i + self.chain.degree() in self.forms:
                b_source = self.forms[i]
                b_target = self.forms[i + self.chain.degree()]
                # Check: d^T * b_target * d = b_source
                if d.ncols() > 0 and d.nrows() > 0:
                    preserved = d.transpose() * b_target * d
                    if preserved != b_source:
                        raise ValueError(f"Differential at degree {i} does not preserve forms")
    
    def tensor(self, other):
        """
        Tensor product of bilinear chain complexes.
        
        Uses SageMath's tensor product for underlying chains,
        then computes tensor product of forms.
        """
        # Get tensor product of underlying chain complexes
        tensor_chain = self.chain.tensor(other.chain)
        
        # Compute tensor product of forms at each degree
        tensor_forms = {}
        for i in self.forms:
            for j in other.forms:
                # Tensor product of forms uses Kronecker product
                form_ij = self.forms[i].tensor_product(other.forms[j])
                # Place in appropriate degree (i+j for homological grading)
                tensor_forms[i + j] = form_ij
        
        # Build new BilinearChainComplex
        # Extract differentials from tensor_chain
        tensor_diffs = tensor_chain.differential()
        
        return BilinearChainComplex(self.base_ring, tensor_diffs, tensor_forms)
    
    def hom_complex(self, other):
        """
        Internal Hom complex of bilinear chain complexes.
        
        Hom(C, D)_n = ∏_i Hom_{BilR-Mod}(C_i, D_{i+n})
        """
        # This is more complex - need to track form-preserving maps
        pass
```

## Bar Resolution Implementation

```python
class BarResolution(BilinearChainComplex):
    """
    Bar resolution of a bilinear module using hyperbolic planes.
    """
    
    @staticmethod
    def hyperbolic_plane(R):
        """Return the hyperbolic plane over R."""
        return matrix(R, [[0, 1], [1, 0]])
    
    @classmethod
    def create(cls, bilinear_module, length=5):
        """
        Create bar resolution of a bilinear module.
        
        ... → H⊗H⊗M → H⊗M → M → 0
        
        where H is the hyperbolic plane.
        
        EXAMPLES::
        
            sage: # Resolution of Z/nZ with form
            sage: M = BilinearModule(matrix(ZZ, [[2]]), quotient_by=[(3,)])
            sage: bar = BarResolution.create(M, length=3)
            sage: bar.chain.homology()
            {0: Z/3Z, 1: 0, 2: Z/3Z, 3: 0}  # 2-periodic
        """
        R = bilinear_module.base_ring()
        H = cls.hyperbolic_plane(R)
        M_form = bilinear_module.gram_matrix()
        M_module = bilinear_module.ambient_module()
        
        differentials = {}
        forms = {0: M_form}
        
        # Build the bar complex
        for i in range(1, length + 1):
            # C_i = H^⊗i ⊗ M
            # Form is tensor product of i copies of H and M's form
            
            # Compute form by Kronecker products
            form_i = M_form
            for j in range(i):
                form_i = H.tensor_product(form_i)
            forms[i] = form_i
            
            # Differential d_i is alternating sum of face maps
            # For simplicity, just sketch the structure
            if i == 1:
                # d_1: H ⊗ M → M is counit (partial)
                # This needs proper implementation
                d_i = matrix(R, M_module.dimension(), 
                           H.nrows() * M_module.dimension())
            else:
                # Higher differentials from simplicial structure
                d_i = matrix(R, forms[i-1].nrows(), forms[i].nrows())
            
            differentials[i] = d_i
        
        return cls(R, differentials, forms)
```

## Computing Derived Functors

```python
def compute_ext_bilinear(M, N, n):
    """
    Compute Ext^n(M, N) in category of bilinear modules.
    
    Algorithm:
    1. Take bar resolution of M
    2. Apply Hom_{BilR-Mod}(-, N) 
    3. Compute cohomology
    
    EXAMPLES::
    
        sage: M = BilinearModule(matrix(ZZ, [[2]]))
        sage: N = BilinearModule(matrix(ZZ, [[3]]))
        sage: ext1 = compute_ext_bilinear(M, N, 1)
        sage: ext1
        BilinearModule with form [6] over Z/gcd(2,3)
    """
    # Get bar resolution
    bar = BarResolution.create(M, length=n+2)
    
    # Apply Hom functor
    # This computes form-preserving maps at each degree
    cochain = apply_hom_functor(bar, N)
    
    # Compute cohomology
    return cochain.cohomology(n)

def compute_tor_bilinear(M, N, n):
    """
    Compute Tor_n(M, N) in category of bilinear modules.
    
    Uses bar resolution and tensor product.
    """
    # Get bar resolution
    bar = BarResolution.create(M, length=n+2)
    
    # Tensor with N
    tensor_complex = bar.tensor(N)
    
    # Compute homology
    return tensor_complex.homology(n)
```

## Integration Points

1. **Reuse SageMath's ChainComplex** for the module structure
2. **Extend with bilinear forms** at each degree
3. **Use existing tensor/Hom** infrastructure where possible
4. **Add form-preservation checks** to ensure morphisms are valid
5. **Leverage existing homology computation** algorithms

## Next Steps

1. Implement the basic BilinearChainComplex class
2. Get bar resolutions working with explicit differentials
3. Implement form-preserving Hom functor
4. Add methods for computing Ext and Tor
5. Optimize using periodicity for cyclic modules