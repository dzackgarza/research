---
title: Mathematical Narrative Test
status: active
---
# Real implementation work should read as a mathematical narrative

Before doing detailed engineering, ask whether the result will let future code say
something mathematically meaningful.

## Good target shape

```python
L = NamedLattice(...)
M = NamedLattice(...)
f = L.hom(M, images_of_generators)
f.is_primitive()
f.cokernel()
L.discriminant_group()
v * w
```

The exact API may differ, but the standard is fixed: the code should expose named
mathematical objects, maps, invariants, and verifiable claims.

## Bad target shape

- raw matrices with no named mathematical interpretation;
- hand-rolled algorithms already available in Sage/GAP;
- computations that "prove" correctness only by producing an answer;
- huge construction scripts that cannot be translated into a written mathematical
  argument;
- wrappers whose only purpose is satisfying process artifacts.

If an implementation task cannot explain how it improves this mathematical narrative, it
is likely engineering drift.

## Already aligned rules

`research-math-boundary` already says the trusted shared code is a semantic mathematical
base of explicit nouns and methods.
`research-software-wiring` already says missing wrapper does not mean missing algorithm
and agents should prefer mature exact backends.
