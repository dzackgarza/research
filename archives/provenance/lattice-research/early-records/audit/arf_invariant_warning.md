# WARNING: Arf Invariant Does Not Exist Over Z

## Critical Error

The term "Arf invariant" appeared in task3_2 work and propagated through multiple
documents. This is **mathematically nonsensical** in our setting.

## What Arf Invariant Actually Is

From Wikipedia and standard references:

**Definition**: The Arf invariant is defined for a quadratic form q over a **field K of
characteristic 2** such that:
1. q is nonsingular (associated bilinear form b(u,v) = q(u+v) - q(u) - q(v) is
   nondegenerate)
2. The bilinear form b is **alternating** (requires characteristic 2)
3. The form has even dimension

For a binary (2-dimensional) nonsingular quadratic form over K:
- q(x,y) = ax² + xy + by²
- Arf invariant = ab (as a coset modulo U = {u² + u : u ∈ K})

**Over F_2**: The Arf invariant is either 0 or 1, and completely determines the
equivalence class of the form.

**Key requirements**:
- Field of characteristic 2 (NOT rings like Z or Q)
- Alternating bilinear form (NOT symmetric)
- Coset structure modulo additive subgroup U

## Our Setting

We work with:
- **Discriminant forms**: q_T: A_T → Q/2Z where A_T is a finite abelian group
- **Base structure**: Integral lattices over Z (NOT fields of characteristic 2)
- **Bilinear form**: SYMMETRIC (NOT alternating)
- **Values**: Q/2Z (NOT a field of characteristic 2)

## Why Arf Invariant Is Undefined Here

1. **Wrong base structure**: Z is a ring, not a field of characteristic 2
2. **Wrong form type**: Our bilinear forms are symmetric, not alternating
3. **Wrong value space**: Q/2Z is not a field of characteristic 2
4. **No classification theorem**: Even if we tried to define "Arf invariant over Z", we
   would need:
   - Proof it's well-defined (what is "most common value" for infinite sets?)
   - Proof it's an invariant (coset structure doesn't obviously translate)
   - Classification theorem for when two forms are equivalent
   - Canonical forms to read off the invariant

None of these exist for our setting.

## What We Should Use Instead

For orbit classification of primitive isotropic planes in discriminant groups:

**Correct approach**: Direct orbit computation via GAP
- Finite group O(q_T) acts on finite set of primitive isotropic planes
- Use GAP's orbit functions: `Orbits(G, S)`
- Count orbits directly
- No "invariant" needed - just compute the orbits

**Literature reference**: Standard finite group theory, no special invariants required.

## How This Error Occurred

1. Task3_2 code invented "Arf invariant" computation
2. Code computed something meaningless (always returned 0 for isotropic planes by
   definition)
3. Verification process failed to catch undefined concept
4. Error propagated to proof notes, CHANGELOG, verification process examples
5. I cited it as valid work in subsequent reasoning

## Prevention

**Blocking Gate 1** in verification process now requires:
- Formal definition for EVERY mathematical term
- Setting where it's defined (field/ring/group structure)
- Citation to source
- Verification that our setting matches

This document serves as permanent warning: **Arf invariant does not exist over Z**.

## References

- Wikipedia: Arf invariant (https://en.wikipedia.org/wiki/Arf_invariant)
- Arf, Cahit (1941). "Untersuchungen über quadratische Formen in Körpern der
  Charakteristik 2"
- Our setting: Nikulin (1979), discriminant forms for integral lattices
