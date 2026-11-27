# Hom/End/Aut Categories Hierarchy

```mermaid
graph TD
    Cat["Cat"]
    Cat --> HomCategory["C.HomCategory()<br/>Hom_C(A,B) objects, domain, codomain"]
    HomCategory --> EndCategory["C.EndCategory()<br/>End_C(A) = Hom_C(A,A), identity, is_endomorphism_set"]
    EndCategory --> AutCategory["C.AutCategory()<br/>Aut_C(A), is_invertible, is_isomorphism, inverse, order"]
    
    HomCategory --> SetHom["Sets().HomCategory()<br/>function hom objects, injectivity, image subobjects"]
    SetHom --> SetEnd["Sets().EndCategory()<br/>endofunction monoid"]
    SetEnd --> SetAut["Sets().AutCategory()<br/>permutation group"]
    
    HomCategory --> ModuleHom["Modules(R).HomCategory()<br/>R-linear morphisms, kernel, image, cokernel"]
    ModuleHom --> ModuleEnd["Modules(R).EndCategory()<br/>endomorphism algebra"]
    ModuleEnd --> ModuleAut["Modules(R).AutCategory()<br/>GL(R), general linear group"]
    
    HomCategory --> FormHom["FormedModules.HomCategory()<br/>form-preserving morphisms"]
    FormHom --> LatticeHom["Lattices.HomCategory()<br/>isometries"]
    LatticeHom --> LatticeAut["Lattices.AutCategory()<br/>O(L), orthogonal group"]
    
    HomCategory --> RingHom["Rings().HomCategory()<br/>ring homomorphisms"]
    HomCategory --> AlgHom["Algebras(R).HomCategory()<br/>algebra homomorphisms"]
```
