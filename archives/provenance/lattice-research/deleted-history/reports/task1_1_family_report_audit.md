# Audit Report: Literature Families for 10-Nodal Rational Sextics

## 1. Scope and Audit Standard

This audit re-evaluates all prior claims about construction families for explicit
rational plane sextics with ten nodes.

Each claim is classified as:

- **Verified**: Primary source directly inspected and supports the claim
- **Secondary supported**: Secondary source supports the claim (citation of primary)
- **Unsupported**: No source found to support the claim
- **Retracted**: Prior claim was incorrect and is withdrawn

The standard requires direct source evidence — indirect citations, plausibility
arguments, MathOverflow summaries, or tertiary citations do NOT qualify as primary
verification.

* * *

## 2. Claim-by-Claim Verdict Table

| Claim | Verdict | Source Quality | Exact Support | Safe Repo Phrasing |
| --- | --- | --- | --- | --- |
| Coble (1919) gave explicit sextic equations | **Retracted** | None | No evidence found — Coble's papers study configuration geometry, not explicit equations | "Coble studied the configuration geometry of 10-nodal sextics" |
| Desargues configuration + Thas gives unique sextic | **Secondary supported for uniqueness; primary for weaker existence** | Primary for weaker existence claim; archived secondary source for uniqueness | C. Thas (1994) directly supports existence/construction of a rational sextic with ten nodes from a Desargues configuration, while an archived 2016 Dolgachev abstract directly attributes the stronger uniqueness claim to `J. Thas`; the underlying primary `J. Thas` source is still unresolved | Cite C. Thas (1994) for existence/construction; if mentioning uniqueness, attribute it to Dolgachev's archived abstract and keep the underlying `J. Thas` source unresolved |
| Halphen index-2 guarantees rational 10-nodal sextic | **Retracted** | None | Halphen framework exists but no theorem found guaranteeing rational member | "Halphen pencils provide a framework — rationality condition is subtle" |
| Coolidge Theorem 28 gives existence | **Unsupported as stated** | Primary for a nearby weaker claim | Direct inspection of Coolidge pp. 390-392 confirms a classical discussion of nine and ten double points on rational sextics, but the exact MathOverflow paraphrase of "Theorem 28" was not yet isolated verbatim from the primary text | Cite Coolidge for configuration constraints on nine/ten double points, not yet for the stronger MO theorem wording |
| K3/period moduli give explicit equations | **Retracted** | None | Moduli sources are existence statements only | "Moduli theory proves existence, not constructibility" |
| Steiner sextics produce 10-nodal curves | **Retracted** | None | Steiner constructions produce different node counts | "Steiner constructions are not relevant to 10-node case" |
| Generic parametrization approach is classical | **Unsupported** | None | No classical source found for this specific approach | Do not claim classical status for generic parametrization |
| Any 10 points yield unique sextic | **Retracted** | None | Points must satisfy geometric conditions | "10 points must satisfy no-three-collinear, no-six-on-conic, etc." |

* * *

## 3. Verified Families with Exact Support Level

### 3.1 COOLIDGE THEOREM 28 — STATUS: PRIMARY INSPECTED; CLAIM AS STATED STILL UNSUPPORTED

**Reported Source**: Julian Lowell Coolidge, "A Treatise on Algebraic Plane Curves"
(1928), Theorem 28, p. 392

**What I Actually Verified**:
- I directly inspected the machine-readable OCR text of the 1931 Oxford scan available
  via Internet Archive item `dli.ernet.524477`, aligned with printed p. 392 using the
  archive page-number JSON.
- Coolidge explicitly discusses the sextic threshold where nine assigned double points
  are no longer arbitrary because a nondegenerate sextic must form a superabundant base.
- Coolidge also explicitly writes: "Suppose, now, that our sextic is rational, and so
  has ten double points.
  How must they lie?"
- This confirms that pp.
  390-392 genuinely contain the classical nine-/ten-node rational-sextic discussion that
  later summaries point to.
- I also inspected the MathOverflow answer (Francesco Polizzi, Dec.
  2020), which reconstructs a theorem from Coolidge's surrounding propositions.
- However, I did **not** isolate a clean verbatim primary-text theorem statement
  matching the exact MathOverflow paraphrase of "Theorem 28, p. 392".

**Exact Statement** (from MathOverflow summary): Let $S = \{P_1, \ldots, P_{10}\}
\subset \mathbb{P}^2$ such that for any $i$, there is an irreducible sextic curve
singular along $S \setminus P_i$; then there is an irreducible sextic curve singular
along all of $S$.

**Support Level**:

- **Verified for the weaker claim** that Coolidge directly studies the geometric
  constraints on nine and ten double points of rational sextics at the cited location.
- **Unsupported as stated** for the stronger MathOverflow paraphrase until the exact
  theorem wording is isolated directly from a better primary-text extraction or page
  image.

* * *

### 3.2 THAS/DESARGUES CONFIGURATION — STATUS: PRIMARY VERIFIED FOR THE WEAKER CLAIM; ARCHIVED SECONDARY SUPPORT FOR THE STRONGER UNIQUENESS WORDING

**Reported Source**: J. Thas, theorem cited in:
- Igor Dolgachev, "Coble surfaces and Desargues configurations" (MPI lecture abstract
  2016\) — current URL 404, but an archived copy is directly inspectable via Wayback

**Directly inspected primary source**:

- C. Thas, "A rational sextic associated with a Desargues configuration," *Geometriae
  Dedicata* 51 (1994), 163–180. DOI: `10.1007/BF01265327`.

**What I Actually Verified**:
- The live MPI abstract URL returns 404, but an archived Wayback copy is directly
  inspectable and states: "A beautiful theorem of J. Thas asserts that the ten points of
  a Desargues configuration ... can serve as the ten nodes of a unique rational plane
  curve of degree 6."
- The Springer landing page for C. Thas (1994) gives a directly inspected abstract
  stating: "We construct a rational curve of order 6 which has a node at each of the ten
  points" of a Desargues configuration and "find a rational parametric representation of
  it."
- This directly supports a weaker claim: a Desargues configuration can be used to
  produce a rational sextic with ten nodes.
- The archived Dolgachev abstract directly supports the stronger uniqueness wording as a
  secondary attribution.
- No directly inspected primary source yet verifies that stronger uniqueness statement,
  and the archived abstract does not resolve whether Dolgachev's cited "J. Thas" is a
  typo, different author, or a separate source trail.

**Exact Statement**:

- From the directly inspected C. Thas abstract: a Desargues configuration is used to
  construct a rational plane sextic with a node at each of its ten points, together with
  a rational parametrization.
- From the cached MPI search snippet only: the ten points of a Desargues configuration
  can serve as the ten nodes of a **unique** rational plane curve of degree 6.

**Support Level**:

- **Verified for the weaker existence/construction claim** via the directly inspected
  abstract of C. Thas (1994).
- **Secondary supported for the stronger uniqueness wording** via the directly inspected
  archived Dolgachev abstract.
- **Still unresolved at the primary-source level** because no directly inspected
  `J. Thas` publication has yet been tied to that exact wording.

* * *

## 4. Retracted or Unsupported Claims from Prior Report

### 4.1 Claims Now Retracted

1. **"Coble gave explicit sextic equations"** — No evidence supports this.
   - Coble's work is configuration-theoretic, not computational.

2. **"Halphen index-2 guarantees a rational 10-nodal sextic member"** — No theorem
   found.
   - The literature does NOT contain a theorem guaranteeing this.

3. **"Steiner sextics produce 10-nodal curves"** — No relevance found.
   - Steiner constructions produce different node configurations.

4. **"K3/period moduli give explicit construction"** — No constructibility found.
   - These are existence theorems in moduli theory.

5. **"Generic parametrization approach is classical"** — No source identified.
   - This computational approach has no identified classical source.

6. **"Any 10 points yield unique sextic"** — False as stated.
   - Points must satisfy geometric genericity conditions.

### 4.2 Audit Defects in the Current Evidence Chain

The following defects were identified in the prior audit:

1. **Coolidge theorem-overreach**: I previously treated the MathOverflow paraphrase as
   if it were already a directly verified theorem statement from Coolidge.
   I have now inspected the primary source and confirmed the surrounding classical
   nine-/ten-node discussion, but I still have not isolated a verbatim theorem statement
   matching the exact MathOverflow wording.
   The corrected classification is therefore: **primary inspected for a nearby weaker
   claim; unsupported as stated for the stronger paraphrase**.

2. **Thas/Desargues source-chain collapse**: I previously treated the MPI layer as if it
   were either unavailable noise or enough to support the full claim.
   The better split is now: C. Thas (1994) directly supports existence/construction of a
   rational 10-nodal sextic from a Desargues configuration; Dolgachev's archived 2016
   abstract directly supports the stronger uniqueness wording as a secondary
   attribution; the exact "J. Thas" primary source remains unresolved until directly
   tied to an inspected source.

3. **Wikipedia citation**: I cited Wikipedia as a source in section 3.2. Wikipedia is
   NOT an acceptable source class for mathematical claims in this audit.
   This citation has been removed.

4. **MathOverflow as evidence**: The MathOverflow discussion is tertiary evidence
   (someone summarizing/reconstructing a theorem).
   It is not acceptable to cite this as "Primary" or even "Secondary" support.

* * *

## 5. Best Next Literature-Backed Example Routes

Based on audited evidence, ranked by what could theoretically be verified:

### 5.1 First Priority: Direct Source Verification

**Route**: Actually inspect the primary sources that were only cited indirectly.

- Obtain Thas publication on Desargues configurations and sextics
- Verify whether these theorems actually say what prior reports claimed

**Risk**: Even if these sources exist, they may not contain constructible algorithms.

* * *

### 5.2 Second Priority: Computational Construction Without Classical Precedent

**Route**: Given that no explicit construction is found in literature, accept that
repo's generic parametrization approach may be novel, and focus on rigorous verification
of those examples.

- Keep the three existing generic parametrization examples
- Verify they satisfy the conditions for a Coble curve (10 nodes, rationality)
- Do NOT claim these are "classical" — treat them as repo-native constructions

**Risk**: May be computationally valid but historically novel.

* * *

### 5.3 Third Priority: Search for Any Explicit Equations

**Route**: Broader literature search for any paper giving explicit polynomial equations
of a 10-nodal rational sextic.

- Search arXiv, MathSciNet for "explicit equation" + "10 nodes" + "sextic"
- Check if any classical treatise (Coble, Coolidge, etc.)
  contains examples

**Risk**: May yield no results.

* * *

## 6. Open Gaps Requiring Manual/Source-Level Follow-Up

1. **Resolve the exact Coolidge theorem wording**: the primary text has now been
   inspected and it does support the surrounding nine-/ten-node rational-sextic
   discussion, but the exact stronger theorem wording quoted in MathOverflow still needs
   a cleaner direct extraction or page-image confirmation before it can be cited as
   such.

2. **Resolve the Thas attribution / uniqueness layer**: Determine whether Dolgachev's
   archived MPI abstract intended the 1994 C. Thas paper or some separate J. Thas
   source, and whether any directly inspected primary source actually states uniqueness.

3. **Determine if any explicit equations exist**: Search systematically for any source
   that provides an explicit polynomial equation of a 10-nodal rational sextic.

4. **Verify repo examples against any standard**: Check whether the three existing
   generic parametrization examples correspond to any known construction or are novel.

5. **Re-assess Halphen sources**: Obtain Halphen's original paper (1882) on sextics and
   verify whether it contains the claimed theorem.

* * *

## Summary

- **Unsupported as stated**: the stronger MathOverflow paraphrase of Coolidge Theorem 28
  and all remaining claimed families that still lack direct support
- **Direct primary support for a weaker claim**: C. Thas (1994) constructs a rational
  sextic with ten nodes from a Desargues configuration and gives a rational
  parametrization, based on the directly inspected journal abstract
- **Direct secondary support for a stronger claim**: Dolgachev's archived 2016 MPI
  abstract attributes to `J. Thas` the stronger uniqueness statement for the
  Desargues-configuration sextic, but the underlying primary source remains unresolved
- **Direct primary support for a nearby classical discussion**: Coolidge directly treats
  the nine-/ten-node rational-sextic configuration problem on the cited pages, even
  though the exact stronger theorem wording still needs cleaner extraction before use
- **Retracted**: All claims that prior report made about Coble equations, Halphen
  guarantees, Steiner relevance, K3 explicitness, generic parametrization as classical
- **Core gap**: No directly inspected full-text explicit sextic equations have been
  verified in-repo; the surviving literature support is still configuration-theoretic,
  except for the weaker constructive Desargues route recorded from C. Thas (1994)
- **Audit defect**: Prior report incorrectly classified source quality levels due to not
  actually inspecting primary sources
