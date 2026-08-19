# Origin: gitclones/Coxeter/implementation/planning/examples/working_f_inverse_example.py
# Copied 2026-08-20 by the Coxeter-corpora enrichment migration
# (PLAN-coxeter-deletion-audit-registry). Content below is unmodified.
# Design prototype, not maintained preamble code.

#!/usr/bin/env sage

"""
Working example of f^(-1)(y) syntax in SageMath.

This demonstrates that we CAN override the ^ operator for morphisms
without touching the preprocessor!
"""

from sage.all import *
from sage.modules.vector_space_morphism import VectorSpaceMorphism

# Save the original __pow__ method
original_pow = VectorSpaceMorphism.__pow__

class PreimageOperator:
    """
    Represents the preimage operation f^(-1): im(f) → domain(f).
    """
    def __init__(self, morphism):
        self.morphism = morphism
        
    def __call__(self, y):
        """Find a preimage of y under the morphism."""
        try:
            return self.morphism.lift(y)
        except Exception as e:
            raise ValueError(f"Element {y} is not in the image of the morphism: {e}")
    
    def __repr__(self):
        return f"Preimage operator of {self.morphism}"
    
    def domain(self):
        """Domain is the image of the original morphism."""
        return self.morphism.image()
    
    def codomain(self):
        """Codomain is the domain of the original morphism."""  
        return self.morphism.domain()

def enhanced_pow(self, n):
    """
    Enhanced power method that handles f^(-1) intelligently.
    
    - For invertible endomorphisms: f^(-1) returns the inverse morphism
    - For non-invertible morphisms: f^(-1) returns a PreimageOperator
    """
    if n == -1:
        # Check if this is an invertible endomorphism
        if (self.domain() == self.codomain() and 
            hasattr(self, 'is_invertible') and self.is_invertible()):
            # Use original behavior for invertible morphisms
            return original_pow(self, n)
        else:
            # Return preimage operator for non-invertible cases
            return PreimageOperator(self)
    else:
        # All other powers use original behavior
        return original_pow(self, n)

# Monkey-patch the enhanced method
VectorSpaceMorphism.__pow__ = enhanced_pow

def demo():
    """Demonstrate the enhanced f^(-1) syntax."""
    print("=== Enhanced f^(-1) Syntax Demo ===\n")
    
    # Example 1: Non-square morphism (most common case)
    print("Example 1: Non-square morphism")
    V = QQ**3  # Use ** instead of ^ in Python mode
    W = QQ**2
    f = V.hom([[1, 2], [3, 4], [5, 6]], W)
    
    print(f"f = {f}")
    print(f"f^(-1) = {f^(-1)}")
    
    # Test with an element in the image
    y = W([7, 8])
    print(f"y = {y}")
    x = (f^(-1))(y)  # This is the new syntax!
    print(f"x = f^(-1)(y) = {x}")
    print(f"Verification: f(x) = {f(x)}")
    print(f"f(x) == y: {f(x) == y}")
    print()
    
    # Example 2: Invertible endomorphism (should work as before)
    print("Example 2: Invertible endomorphism")
    g = V.hom([[2, 0, 0], [0, 3, 0], [0, 0, 1]], V)
    print(f"g = {g}")
    g_inv = g^(-1)
    print(f"g^(-1) = {g_inv}")
    print(f"Type: {type(g_inv)}")
    print(f"Is inverse correct: {(g_inv * g).is_identity()}")
    print()
    
    # Example 3: Non-invertible endomorphism  
    print("Example 3: Non-invertible endomorphism")
    h = V.hom([[1, 0, 0], [0, 1, 0], [0, 0, 0]], V)  # Projects to xy-plane
    print(f"h = {h}")
    h_preimage = h^(-1)
    print(f"h^(-1) = {h_preimage}")
    
    # Test lifting
    z = V([2, 3, 0])  # In the xy-plane (image of h)
    w = (h^(-1))(z)
    print(f"z = {z}")
    print(f"w = h^(-1)(z) = {w}")
    print(f"h(w) = {h(w)}")
    print(f"h(w) == z: {h(w) == z}")
    print()
    
    # Example 4: Error handling
    print("Example 4: Error handling")
    try:
        bad_y = W([1, 0])  # Try an element that might not be in image
        bad_x = (f^(-1))(bad_y)
        print(f"Unexpected success: {bad_x}")
    except ValueError as e:
        print(f"Expected error: {e}")

if __name__ == "__main__":
    demo()