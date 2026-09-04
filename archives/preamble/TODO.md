# Outstanding archive-derived mathematical work

## Presented modules over general bases

- [ ] Generalize `is_torsion_free` beyond `ZZ` without guessed booleans; the archived implementation returns `True` unconditionally off `ZZ`.
- [ ] Generalize module cardinality using the cardinality of the base and the actual module decomposition; the archived implementation returns `aleph_0` for every non-torsion module.
- [ ] Generalize exponent/annihilator vocabulary only where meaningful; the archived implementation reports exponent `1` for nonzero free modules.

## Scheme invariants

- [ ] Separate arithmetic genus from geometric genus for singular curves instead of routing both through one engine `genus()` value.
- [ ] Rebuild `Pic(A^n)`, `Cl(A^n)`, `Pic(P^n)`, and `Cl(P^n)` through the actual scheme/divisor-group layer with hypotheses and base contributions visible; in particular do not hard-code `Pic(P^n_S) = Z` over arbitrary `S`.

## Lattice and finite-form gaps

- [ ] Resolve or explicitly retain the `Isom(L,M)` gap for indefinite binary lattices and for genera splitting into several improper spinor genera when the available backend cannot place a given lattice in a spinor genus.
- [ ] Extend embedding existence/enumeration beyond the current exact regimes: enumeration for indefinite codomains and existence for indefinite codomains that are not even unimodular.
- [ ] Add the bilinear analogue of `is_anti_isometric`; the quadratic torsion-form surface has the operation but the bilinear surface does not.
