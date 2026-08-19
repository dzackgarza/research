# Theory Spec: Monodromy of Hypersurface Families via foliation.lib

This file documents the intended verifications for `tests/test_foliation_backend.py`
and the `src/research/foliation_backend.py` implementation. Each test assertion must
trace to a directly citable source. Internal consistency checks are not acceptable as
primary evidence of correctness.

---

## Status of existing tests

### `test_legendre_family_picard_fuchs_data`

**Current state:** The PF operator coefficients (`operator.list()`) are asserted against
hardcoded values produced by the code itself. This is an internal consistency check, not
a literature-grounded assertion.

**What is needed:** A source that writes down the explicit PF ODE for the Legendre
family `y² = x(x-1)(x-u)` as computed by Griffiths-Dwork/Gauss-Manin reduction *in the
same normalisation as foliation.lib*. The coefficient list depends on the choice of
P_form generator and the Milnor basis — Movasati's book is the canonical reference for
what `PFequ` outputs.

**Reference needed:**
> Movasati, H. — *A Course in Hodge Theory: With Emphasis on Multiple Integrals*.
> World Scientific, 2021. (Also available as IMPA preprint.)
> Required section: explicit PF matrix for Weierstrass/Legendre family.

---

### `test_legendre_family_picard_fuchs_data` — indicial polynomial

**Current assertion:** `family.indicial_polynomial() == -4 * alpha**2`

**Problem:** This tests the exact polynomial, including leading coefficient, which
depends on the normalisation of ore_algebra's `indicial_polynomial` method (GCD-reduced,
lcm of denominators cleared). The roots — both equal to 0 — are the mathematically
meaningful content.

**What should be asserted instead:** The roots of the indicial polynomial are both 0
(a double root), i.e. the indicial exponents at t=0 are (0, 0).

**Reference needed (same as above):**
> Movasati, H. — *A Course in Hodge Theory*. For the statement that the Legendre family
> has a regular singular point at t=0 with both indicial exponents equal to 0.
>
> Griffiths, P. — "On the periods of certain rational integrals I, II".
> Ann. of Math. 90 (1969), 460–541.

---

### `test_legendre_family_monodromy_data`

**Current assertions:** log-monodromy JNF = `[[0,1],[0,0]]`, unipotent monodromy =
`[[1, 2πi], [0, 1]]`. These are in the *period-integral basis*, not the
integral-homology basis. The value `2πi` (rather than an integer) is a signature of
working in the period basis.

**What is needed:** A source that explicitly states the local monodromy around t=0 for
the Legendre family in the period basis (or the Gauss-Manin connection basis), ideally
the same basis that `foliation.lib` uses. The topological statement (monodromy =
`[[1,0],[-2,1]]` or `[[1,2],[0,1]]` in an integral cycle basis) is standard but does
NOT directly validate our output, since the basis differs.

**References needed:**
> Movasati, H. — *A Course in Hodge Theory*. For the monodromy in the Gauss-Manin
> connection basis matching what foliation.lib returns.
>
> Griffiths, P. — "On the periods of certain rational integrals I, II".
> Ann. of Math. 90 (1969), 460–541. For the topological statement (different basis).
>
> Deligne, P. et al. — *SGA 7, Groupes de monodromie en géométrie algébrique*,
> Exp. XV (Katz). For the integral-basis statement (Picard-Lefschetz formula).

---

## Planned new tests (blocked pending literature)

### A₂ Brieskorn-Pham family `y² = x³ - u`

**Family:** `f = y² - x³ - u` with weights `(x,y,u) = (2,3,6)` (weighted homogeneous),
so `TermOrder("wdegrevlex", (2,3,6))`.

**Intended assertions:**
1. `milnor_number == 2`
   > Milnor, J. — *Singular Points of Complex Hypersurfaces*.
   > Ann. of Math. Studies 61, Princeton, 1968. Lemma 8.6: μ = (p-1)(q-1) for
   > Brieskorn-Pham x^p + y^q.
   > **This source is available; add it.**

2. Indicial exponents at t=0: their values depend on the Gauss-Manin normalisation.
   In the literature (Brieskorn 1970), the spectrum of the A₂ singularity gives
   Hodge-theoretic weights, but translating these to indicial exponents of the PF ODE
   as output by `foliation.lib` requires knowing the precise basis.
   **Cannot assert specific values until Movasati's book is available.**
   > Brieskorn, E. — "Die Monodromie der isolierten Singularitäten von Hyperflächen".
   > Manuscripta Mathematica 2 (1970), 103–161.
   > **This source is needed; add it.**

3. Monodromy eigenvalues are primitive 6th roots of unity (roots of Φ₆ = x²-x+1),
   i.e. monodromy is semisimple with no unipotent part.
   > Brieskorn (1970), ibid. This is the main theorem for isolated singularities of
   > Brieskorn-Pham type.
   > **Cannot write the test until exact eigenvalue expressions (in our basis) are
   > confirmed from the source.**

---

## References to acquire

The following are needed before the blocked test assertions can be written. Please add
to Zotero and provide markdown extractions:

| # | Reference | Needed for |
|---|-----------|------------|
| 1 | Movasati, H. — *A Course in Hodge Theory*. World Scientific, 2021. | PF operator coefficients, indicial exponents, and monodromy in the foliation.lib basis for Legendre/Weierstrass families |
| 2 | Griffiths, P. — "On the periods of certain rational integrals I, II". Ann. of Math. 90 (1969) | Indicial exponents at t=0 for Legendre family; Gauss-Manin connection setup |
| 3 | Brieskorn, E. — "Die Monodromie der isolierten Singularitäten von Hyperflächen". Manuscripta Math. 2 (1970) | A₂ monodromy eigenvalues; spectrum of isolated singularities |
| 4 | Deligne et al. — *SGA 7*, Exp. XV (Katz) | Integral-basis monodromy (Picard-Lefschetz formula) for cross-check |
