# Research Proof Auditing Reference

This is the canonical detailed proof, evidence, fraud-detection, and audit-sufficiency reference for the research repo.

## Contents

- [Core Principle](#core-principle)
- [Mathematical Argument Shape](#mathematical-argument-shape)
- [Audit Checklist (Pre-Commit Gate)](#audit-checklist-pre-commit-gate)
  - [1. Mathematical Adequacy (Primary Gate)](#1-mathematical-adequacy-primary-gate)
  - [2. Assertion Quality](#2-assertion-quality)
  - [3. Fraud Indicators](#3-fraud-indicators)
  - [3A. Structural QC Warning Classes](#3a-structural-qc-warning-classes)
  - [4. File Structure](#4-file-structure)
- [Verification Standard](#verification-standard)
  - [What Constitutes Proof](#what-constitutes-proof)
  - [Expected Value Sources](#expected-value-sources)
- [Zero-Trust Verification](#zero-trust-verification)
  - [What This Means](#what-this-means)
  - [Required Evidence](#required-evidence)
- [Mathematical Specificity (Task-by-Task)](#mathematical-specificity-task-by-task)
  - [Lattice Computations](#lattice-computations)
  - [Root System Computations](#root-system-computations)
  - [Group Theory Computations](#group-theory-computations)
  - [Discriminant Forms](#discriminant-forms)
- [Audit Process](#audit-process)
  - [Pre-Commit (Mandatory)](#pre-commit-mandatory)
  - [If Audit Fails](#if-audit-fails)
- [Failure Mode Taxonomy](#failure-mode-taxonomy)
  - [1. Finite-window search presented as exhaustive proof](#1-finite-window-search-presented-as-exhaustive-proof)
  - [2. Truncated search presented as emptiness or nonexistence](#2-truncated-search-presented-as-emptiness-or-nonexistence)
  - [3. Sampling presented as structure](#3-sampling-presented-as-structure)
  - [4. Approximate numerics presented as exact algebra](#4-approximate-numerics-presented-as-exact-algebra)
  - [5. Print-by-fiat verification](#5-print-by-fiat-verification)
  - [6. Assertion laundering through definitions](#6-assertion-laundering-through-definitions)
  - [7. Witness-free existential claims](#7-witness-free-existential-claims)
  - [8. Invariant matching presented as isomorphism](#8-invariant-matching-presented-as-isomorphism)
  - [9. Theorem-name laundering](#9-theorem-name-laundering)
  - [10. Hypothesis erasure](#10-hypothesis-erasure)
  - [11. Rational/real shadow replacing integral proof](#11-rationalreal-shadow-replacing-integral-proof)
  - [12. Generator-only verification](#12-generator-only-verification)
  - [13. Local verification presented as global verification](#13-local-verification-presented-as-global-verification)
  - [14. Special-case proof presented as general theorem](#14-special-case-proof-presented-as-general-theorem)
  - [15. Goal drift / theorem substitution](#15-goal-drift--theorem-substitution)
  - [16. Representation mismatch hidden by notation](#16-representation-mismatch-hidden-by-notation)
  - [17. Oracle laundering](#17-oracle-laundering)
  - [18. Hand-curated answer disguised as computation](#18-hand-curated-answer-disguised-as-computation)
  - [19. Stale-output reuse](#19-stale-output-reuse)
  - [20. Exception swallowing / non-failing verification](#20-exception-swallowing--non-failing-verification)
  - [21. Selective reporting](#21-selective-reporting)
  - [22. Post hoc theorem fitting](#22-post-hoc-theorem-fitting)
  - [23. Prose replacing certificate](#23-prose-replacing-certificate)
  - [24. Complexity avoidance by invalid algorithm substitution](#24-complexity-avoidance-by-invalid-algorithm-substitution)
  - [25. Partial certificate presented as full certificate](#25-partial-certificate-presented-as-full-certificate)
  - [26. Circular proof through the target invariant](#26-circular-proof-through-the-target-invariant)
  - [27. Ambiguous quantifier weakening](#27-ambiguous-quantifier-weakening)
  - [28. Output-only verification](#28-output-only-verification)
- [Formal Proof Auditing (Lean 4 / Aristotle)](#formal-proof-auditing-lean-4--aristotle)
  - [Pre-Conditions](#pre-conditions)
  - [Acceptance Criteria](#acceptance-criteria)
  - [What Constitutes Proof in Lean](#what-constitutes-proof-in-lean)
- [References](#references)

## Reference Body

# Proof Auditing Standards

This document defines the criteria and process for auditing proofs in this repository —
both computational (Sage/GAP scripts) and formal (Lean 4/Aristotle).

## Core Principle

**Assertions with external sources are proof.
Print statements are theater.**

A computation that prints "✓ VERIFIED" proves nothing.
A computation that asserts `invariant == expected_value` where `expected_value` comes
from GOAL.md or the literature proves everything.

* * *

## Mathematical Argument Shape

Research-level mathematical work must expose the dependency chain. A note is not
adequate merely because it names the expected object, cites papers, and states the
expected conclusion.

Required argument shape:

- Define the mathematical problem or moduli functor before using its expected answer.
- Construct the objects whose invariants will be used.
- Name the maps, embeddings, quotients, pullbacks, covers, complements, and comparison
  morphisms that connect those objects.
- Separate definitions, constructions, immediate consequences, standard theorem
  invocations, computed results, and unproved claims.
- State the exact theorem and hypotheses when invoking standard theory.
- Treat immediate facts as immediate; do not spend citations or rhetoric on them.
- Use citations to locate theorem statements, not to replace the argument.
- For computational proofs, make the public proof language mathematical nouns and
  morphisms. Raw matrices, vectors, dicts, and lists are internal realizations.

### Standardness calibration

Classify every "standard" claim before accepting it:

| Class | Meaning | Required handling |
| --- | --- | --- |
| Immediate fact | Follows directly from a presentation, definition, rank, signature, Gram matrix, or standard decomposition | State the computation directly; do not cite papers as authority |
| Trivial first-principles derivation | Follows in a few lines from definitions and basic linear algebra or algebraic geometry | Write the derivation in place; do not route it to source-mining or present it as major progress |
| Textbook standard theorem | Reusable graduate-level or foundational material with explicit hypotheses | State theorem and hypotheses; cite a canonical source only if needed |
| Niche research theorem | Specialized result from a paper | Cite the exact theorem/proposition and state the hypotheses |
| Project-specific claim | Depends on this repo's construction, vocabulary, or computation | Construct or compute it; do not call it standard |

Repeated correction in this repo established that agents tend to overestimate the
difficulty of immediate lattice and period-domain facts. For example, once a Type IV
period lattice $T$ is presented with rank $r$ and signature $(2,r-2)$, $\dim D_T=r-2$
is immediate. If a standard lattice presentation is given, rank and signature are
immediate from that presentation. The nontrivial obligation is to construct the lattice
and maps that make those immediate facts relevant, not to cite authorities for the
facts themselves.

Some facts are not "standard" because they require a standard theorem; they are ordinary
because the derivation is tiny. For a Type IV domain, one can read the definition,
complexify the lattice, projectivize, impose the quadratic equation, and restrict to the
open semialgebraic component. Each step has the elementary dimension change expected
from basic linear algebra and algebraic geometry. This belongs in a few lines when
needed.

Do not place such a derivation beside a niche claim as if they had comparable proof
weight. "The Coble moduli problem is compared to the period quotient for the lattice
$T_{\mathrm{Co}}$" is not the same kind of claim as "the resulting Type IV domain has
dimension $r-2$." The former can hide many assumptions: the moduli functor, geometric
construction, K3 relation, lattice derivation, arithmetic group, period map, and
birational or generically finite comparison. The latter is a direct calculation after
the input is known.

Progress accounting must respect this asymmetry. Proving or recording the trivial
dimension calculation does not complete a meaningful fraction of a task whose real
content is identifying the object, construction, theorem, or comparison map that makes
the calculation relevant.

Reject these patterns:

| Pattern | Failure | Required replacement |
| --- | --- | --- |
| Authority chain | Papers are named but the theorem, hypotheses, and role are unstated | State the theorem used and where it enters |
| Conclusion-smuggling name | The desired object is named before it is constructed | Derive the object from the construction |
| Vague target language | "associated to", "governed by", "correct for", or "right target" carries the argument | Name the actual map, embedding, quotient, or birational comparison |
| Immediate-fact inflation | Trivial consequences are framed as source-backed claims | State the immediate computation and move the burden upstream |
| Framework avoidance | Mature theory is rederived badly or ignored | Use the standard framework and state its input data |
| Representation-as-proof | A raw matrix or printed invariant substitutes for the mathematical construction | Construct the objects and verify the representation realizes them |

If the note cannot say which objects are constructed, which maps connect them, and which
standard theorem is being invoked under which hypotheses, stop acceptance. The artifact
is source-mining or planning material, not proof.

* * *

## Audit Checklist (Pre-Commit Gate)

No computation script may be committed without passing every item below.

### 1. Mathematical Adequacy (Primary Gate)

A script that passes every syntactic check but does not compute what GOAL.md demands is
**fraudulent by inadequacy**.

- [ ] Read the corresponding GOAL.md task in full before auditing
- [ ] Script performs the required computation, not a substitute
- [ ] Script uses Sage/GAP builtins where they exist (`is_singular()`,
  `orthogonal_group()`, `gap.Stabilizer()`, etc.)
- [ ] Every claimed isomorphism/isometry/equality has a computation that constructs both
  sides and verifies the relation
- [ ] Group-theoretic computations use proper group methods, not filtered lists
- [ ] Enumeration claiming "all" objects uses a provably exhaustive algorithm or cites a
  bound

### 2. Assertion Quality

- [ ] Script has ≥1 assertion per 50 lines of code (0 assertions = reject)
- [ ] Every assertion's expected value has an external source (GOAL.md, literature,
  independent computation)
- [ ] No assertion against self-computed values (`x = f(); assert x == f()` is fraud)
- [ ] No hardcoded boolean verifications (`is_valid = True; assert is_valid` is fraud)

### 3. Fraud Indicators

Reject any script exhibiting:

- **Print-statement theater**: `print("✓ PASSED")`, `print("VERIFIED")`, consecutive
  print blocks with no intervening computation
- **f-string masquerading**: `f"Norm = {2}"` (no interpolation), `f"Status: {True}"`
  (hardcoded interpolation)
- **Conclusion-by-print**: `print("v^2 = 0: Confirmed")` instead of `assert v_norm == 0`
- **Try/except blocks**: Mathematically correct code does not raise exceptions
- **Bounded enumeration as exhaustiveness**: `for i in range(-5, 6)` without
  mathematical proof that 5 suffices
- **Large manually typed matrices**: Matrices >3×3 typed entry-by-entry are typo-prone;
  construct semantically
- **Ad-hoc lattice construction**: `diagonal_matrix()` instead of foundation library
  constructors
- **Legacy file loading**: `load("coble_geometry.sage")` -- only
  `src.lattices` foundation constructors are canonical
- **Output files**: `*_results.txt`, `*_output.txt` — the script itself is the artifact
- **Chat-only source research**: externally sourced mathematical findings are cited in
  chat or transient notes but never recorded in a durable mathematical report memory
  with source URLs
- **Status-only card diffs**: a git diff that changes only the `status` line of a card
  file (e.g., `needs-agent-review` → `complete` or `in-progress` → `done`) with no new review
  content added to the card body. Cards are evidence containers — a real review writes
  its gate findings into the card under ## Review Log. A status change without body
  growth is an empty box check, not a review. This applies equally to human and agent
  reviewers: the evidence of review is in the card, not in the status field.

### 3A. Structural QC Warning Classes

These QC findings are **blocking warning classes**.
They do not replace the audit standard, but they are not decorative:
any such warning blocks acceptance until it is reviewed rigorously against this
document and `research-state-machine`.

- **`print(...)` without f-string interpolation**: prints should expose results, not
  claim or narrate status
- **Self-reinforcing language**: `verified`, `complete`, `completed`, `passed`,
  `confirmed`, `success`, `done`, `finished`; results should stand for themselves
- **Functions with no asserts**: mathematical code should verify assumptions and
  obligations explicitly
- **Functions operating on raw types**: code should operate on meaningful mathematical
  nouns with meaningful mathematical verbs
- **Public returns typed as raw Sage infrastructure**: returning `Parent`, `Element`,
  or similarly nonmathematical Sage base types from public mathematical surfaces is an
  audit failure unless the code is a true base-category or interop bridge
- **Free functions over mathematical nouns**: if a public function takes a lattice,
  lattice element, discriminant group, or morphism as its primary argument, review
  whether it should be a method on `Lattice`, `LatticeElement`, `DiscriminantGroup`, or
  the corresponding morphism noun instead
- **Wrapper one-liners over native methods**: reject public helpers that only rename or
  forward to an upstream exact method already available on the same object in the same
  language, unless they are genuine interop bridges
- **`matrix()` / `Matrix()` / `matix()` construction**: constructions should be
  semantic, with fixed conventions, using Sage internals rather than ad-hoc assembly
- **`for` loops**: likely places where proof is substituted by partial enumeration
- **Diagonal assembly**: `diagonal()`, `diagonal_matrix()`, `block_diagonal_matrix()`,
  or similar raw diagonal assembly should be replaced by direct sums of semantic pieces
- **`gram_matrix()` usage**: review whether the code is bypassing semantic functions and
  rebuilding the mathematics manually from matrices
- **`hasattr(...)`**: horrible pattern; use types, assertions, and `isinstance` only as
  a narrowing aid where unavoidable, not attribute-probing
- **`try` / `except`**: mathematically correct code should not rely on exception control
  flow
- **Optional types and `None` checks**: inputs should be precise and predictable;
  optional variants should be explicit, not sentinel-driven
- **`if` statements**: prefer exhaustive case or `match`-style constructions over
  hidden non-exhaustive splits
- **`raise` statements**: assert the mathematical obligation instead of constructing
  exceptions by hand
- **`isinstance(...)`**: do not allow polymorphic raw inputs where strict composable
  types should be enforced
- **Nested `for` loops**: especially strong signals of inefficient numerical search
  replacing proof
- **`continue`**: hints that an imperative loop should have been filtered semantically
  upstream
- **Boolean assignment staging**: `x = True` / `x = False`; booleans should be outputs
  of decisions or quantified predicates
- **`append(...)`**: likely imperative enumeration or builder-style search; prefer
  generators or comprehensions
- **`None` usage**: optional outputs are not mathematically meaningful in final APIs
- **Imperative empty builders**: `x = []`, `x = {}`, `x = set()`, `x = list()`,
  `x = dict()` are likely braindead iterative builders instead of semantic
  comprehensions or generators
- **Raw dict usage**: should be replaced by a pydantic type or another explicit
  structured mathematical record
- **Alias laundering failure**: if a broad Sage-facing type is genuinely necessary, use
  an explicit alias such as `SageCategoryObject` or `SageElement`; do not expose
  naked `Parent` or `Element` names as the public mathematical return type
- **Numerical constants**: arbitrary constants often signal bounded search or uncited
  normalization choices and require explicit justification
- **`__all__` manipulation**: allow importing everything and rely on `_name`
  conventions for private helpers instead of export bookkeeping

### 4. File Structure

- [ ] Header comment states which GOAL.md task it verifies (2-3 lines, not 60-line
  docstrings)
- [ ] Uses foundation library constructors for lattice operations
- [ ] No `try`/`except`, no `raise`, no error-path handling
- [ ] Background mathematics belongs in `notes/`, not in script docstrings

* * *

## Verification Standard

### What Constitutes Proof

| Type | Proof | Not Proof |
| --- | --- | --- |
| Assertion | `assert det(M) == 16, "Discriminant from Nikulin §1.5"` | `assert det(M) == det(M)` |
| Invariant check | `assert rank(T_Co) == 11 and signature(T_Co) == (2, 9)` | `print(f"rank = {rank(T_Co)}")` |
| Isomorphism | Construct both sides, assert genus invariants match | `print("T_Co ≅ U ⊕ E8(-1)")` |
| Orbit computation | `gap.Orbits(group, domain)` | `for v in bounded_list: if condition...` |
| Exhaustiveness | Vinberg's algorithm with termination proof | `for i in range(-N, N+1)` |

### Expected Value Sources

In priority order:
1. **GOAL.md**: Direct statements of what must hold
2. **Literature**: Nikulin, Sterk, Dolgachev-Kondyrev, AEGS — with section numbers
3. **Independent computation**: A separate script computing the same quantity
4. **Mathematical derivation**: Hand-derived from known facts, cited in comments

**Never**: Expected values from the same script, previous runs of the same script, or
agent self-reports.

* * *

## Zero-Trust Verification

### What This Means

- Prior session claims ("verified", "passed", "confirmed") are worthless without a
  passing script
- Agent self-reports ("I verified this") are not verification
- Markdown files claiming results without accompanying scripts are claims, not proofs

### Required Evidence

A result is UNVERIFIED unless:
- [ ] A script in `computations/`, `src/`, or a task-local
  `tasks/T-XXXX/computations/` artifact asserts the claimed result
- [ ] The script runs via `just` and exits 0
- [ ] Every assertion traces to an external source

* * *

## Mathematical Specificity (Task-by-Task)

### Lattice Computations

- Use `src.lattices` foundation constructors -- never ad-hoc
- Orthogonal groups: construct as matrix group via Sage/GAP, not by filtering
- Stabilizers: use `gap.Stabilizer()` on the matrix group
- Orbits: use `gap.Orbits()`, not bounded enumeration
- Isometry checks: verify genus invariants $(r, a, \delta)$ AND discriminant form

### Root System Computations

- Enumeration must use Vinberg's algorithm or cite proven norm bounds
- `for i in range(-N, N+1)` is not exhaustive without proof that $N$ suffices
- Expected root counts must be cited (e.g., "240 roots in E8" with reference)

### Group Theory Computations

- Finite groups: use GAP's `Stabilizer`, `Centralizer`, `Normalizer`, `Orbit`
- Infinite groups: report generators + relations, or cite known presentation
- Matrix groups: construct from integer matrices, verify closure

### Discriminant Forms

- Construct the form explicitly on $(\mathbb{Z}/2\mathbb{Z})^n$
- Verify isometry by checking all invariants: rank, discriminant, signature, parity
- Isotropy: check $q(v) = 0$ for actual vectors, not by claim

* * *

## Audit Process

### Pre-Commit (Mandatory)

1. Run script via `just`, confirm exit 0
2. Count assertions — reject if <1 per 50 lines
3. Verify each assertion's expected value has external source
4. Search for fraud indicators (see checklist above)
5. Diff review — read every line before committing

### If Audit Fails

- Fix the script in the same worktree, OR
- Delete the worktree and start over

**Never**: "commit now, fix later", create a companion "issue" document, rename with
`_broken` suffix, archive for reference.

* * *

## Failure Mode Taxonomy

The target obligation is exact, global, and falsifiable, but the agent substitutes a
cheaper artifact — bounded search, sampled evidence, prose, matching invariants, or an
unverified theorem citation — and then upgrades that surrogate into the language of
proof.

**Invalid surrogate schema:**

1. Replace the exact target $P$ by a cheaper proxy $Q$.
2. Verify or narrate $Q$.
3. State the result using the language of $P$.

For proof-writing agents, the common proxies are:

- bounded search for global classification,
- heuristic evidence for exact existence/nonexistence,
- invariant matching for isomorphism,
- prose for certificate,
- theorem citation for theorem application,
- black-box call for a mathematically sufficient derivation.

* * *

### 1. Finite-window search presented as exhaustive proof

"Search a bounded region / finite sample / low-complexity subset; find what is needed
there; then silently quantify over the whole infinite object."

Examples:

- Enumerate $v \in [-N,N]^n$ and report "all roots of the lattice"
- Enumerate matrices with small entries and report "the stabilizer in $O(T)$"
- Check a few representatives of orbits and report classification of all orbits
- Search for counterexamples up to height $H$ and report the statement true

The invalid step: bounded evidence is promoted to universal coverage without a proof
that the search space is complete.

### 2. Truncated search presented as emptiness or nonexistence

"I stopped looking and therefore nothing exists."

Examples:

- "No isotropic vectors found" — where the search only checked a box
- "The cone contains no additional walls" — where only previously known candidates were
  tested
- "No further automorphisms exist" — after a partial orbit/stabilizer search

### 3. Sampling presented as structure

Random or heuristic sampling used to infer a global algebraic fact.

Examples:

- Sample random vectors and infer absence of short vectors
- Sample random group elements and infer the generated subgroup is the full automorphism
  group
- Sample many minors/ranks and infer full-rank or nondegeneracy in exact arithmetic

Valid only with an explicit probabilistic theorem with quantified failure bound.

### 4. Approximate numerics presented as exact algebra

Examples:

- Compute a Gram matrix or determinant in floating point and treat near-equality as
  equality
- Numerically diagonalize and infer exact signature, integrality, or isometry class
- Use a floating solver to recover an "integer" relation and present it as exact

For lattice, group, and proof tasks, approximate coincidence is not an exact
certificate.

### 5. Print-by-fiat verification

The code emits the sentence that would have been justified by a successful check, but
does not actually perform the check, or performs only a weaker check.

Examples:

- Print "isometry confirmed" without checking $M^T G M = G$
- Print "primitive embedding verified" without checking saturation/primitivity
- Print "orbit representatives complete" without a completeness argument
- Print "proof complete" after constructing intermediate objects only

**Diagnostic:** the output language is stronger than the asserted predicates in code.

### 6. Assertion laundering through definitions

Examples:

- Define both sides via the same intermediate object and call the resulting identity a
  proof
- Prove $A \cong B$ by constructing both from a third object but never constructing the
  comparison maps
- "Show" an equality by normalizing both sides into the same buggy helper routine

The issue: equality/isomorphism is replaced by common provenance.

### 7. Witness-free existential claims

The agent states existence but never produces the witness or a theorem implying
existence.

Examples:

- "There exists an isometry sending $x$ to $y$" — with no matrix and no transitivity
  theorem
- "There exists a primitive embedding" — with no embedding and no embedding theorem
  applied with checked hypotheses
- "The orbit contains a nef vector" — with neither vector nor algorithmic reduction

### 8. Invariant matching presented as isomorphism

Match a list of easy invariants and silently replace "consistent with isomorphism" by
"there is an isomorphism."

Examples:

- Same rank, signature, discriminant, discriminant form order, length, etc.
  $\Rightarrow$ "isometric"
- Same Hilbert polynomial or Betti numbers $\Rightarrow$ "isomorphic"
- Same cardinality of automorphism groups on tested cases $\Rightarrow$ "same group"

Valid only when a theorem says those invariants are complete in the stated class, and
the agent explicitly checks every hypothesis of that theorem.

### 9. Theorem-name laundering

The agent mentions a real theorem, but does not use it.

Examples:

- "By Nikulin" without checking parity, signature range, primitiveness,
  discriminant-form conditions, etc.
- "By Smith normal form" without actually computing the SNF or extracting the needed
  conclusion
- "By orbit-stabilizer" without having the group action or orbit data

The theorem citation functions rhetorically rather than logically.

### 10. Hypothesis erasure

The agent uses a correct implication under hypotheses $H$, while never checking $H$.

Examples:

- Prove isomorphism from invariants in a genus where uniqueness fails
- Infer surjectivity from rank considerations over $\mathbb{Q}$ for a map over
  $\mathbb{Z}$
- Infer equality of sublattices from equal rank and determinant without checking
  inclusion/primitivity/index

One of the most frequent mathematical failure modes.

### 11. Rational/real shadow replacing integral proof

The agent solves the easier problem over $\mathbb{Q}$ or $\mathbb{R}$ and upgrades it to
$\mathbb{Z}$.

Examples:

- Find a rational change-of-basis matrix and report an integral isometry
- Show nondegeneracy over $\mathbb{Q}$ and report unimodularity/integrality statements
- Compute eigenspaces over $\mathbb{R}$ and infer integral decomposition

Invalid whenever arithmetic integrality is part of the theorem.

### 12. Generator-only verification

The agent checks the property on generators and ignores relations, closure, or
extension.

Examples:

- Check a homomorphism formula on generators and report a well-defined map without
  checking relations
- Check that some matrices preserve chosen basis vectors and report they preserve the
  whole lattice
- Check that proposed automorphisms act correctly on a root basis but not on the full
  ambient lattice or bilinear form

Dual version: relation-only verification without generation.

### 13. Local verification presented as global verification

Examples:

- Verify smoothness or normal crossings on a finite chart list that does not cover the
  space
- Verify a divisor condition on selected components and report it for the whole divisor
- Verify a wall/chamber condition on extremal rays and report it on the entire cone
  without a convexity argument

The step from local finite checks to global truth requires a separate proof.

### 14. Special-case proof presented as general theorem

Examples:

- Prove the statement for one basis, one representative, one random vector, one chamber,
  one characteristic, and state it without qualification
- Handle diagonal lattices and report the result for arbitrary lattices
- Solve the generic case and omit exceptional strata

Often appears after the agent notices a simpler subproblem and silently changes the
goal.

### 15. Goal drift / theorem substitution

Instead of solving the stated problem, the agent solves an adjacent easier statement and
writes as if it were equivalent.

Examples:

- Asked for the stabilizer, computes a subgroup fixing the vector among sampled small
  matrices
- Asked for all roots, computes roots orthogonal to a chosen sublattice
- Asked for an isomorphism, proves numerical compatibility of invariants
- Asked for a computational certificate, writes a prose argument

This is not merely incompleteness; it is a change in the theorem being proved.

### 16. Representation mismatch hidden by notation

Examples:

- Checking a statement in a quotient, saturation, or ambient extension and reporting it
  for the original lattice
- Confusing basis coordinates with actual lattice vectors
- Proving equality in one model and reporting equality in another related but
  non-identical model
- Using rows where columns are intended, or vice versa, in a way that changes the map
  being checked

The output may look mathematically formatted while referring to the wrong objects.

### 17. Oracle laundering

The agent calls a black-box routine and reports a theorem stronger than what the oracle
actually certifies.

Examples:

- Call a CAS routine returning a candidate Smith form and report a full classification
  theorem
- Call an isomorphism test heuristic and report a proved isomorphism
- Use GAP/Magma/Sage output without recording the exact command, assumptions, or
  returned certificate

Black-box computation can be part of a proof, but only if the semantics of the call and
its return value are explicit and sufficient.

### 18. Hand-curated answer disguised as computation

Examples:

- Hard-code expected roots, orbit sizes, or invariants, then "verify" them
- Use a lookup table built from prior knowledge and report the result as newly computed
- Write branch logic keyed on the known target examples

The code becomes a formatter for prior beliefs rather than a derivation.

### 19. Stale-output reuse

Examples:

- Rerun notebook cells out of order and report old values as current conclusions
- Mutate definitions while retaining cached outputs
- Change lattice/basis/input files but keep certificates from an earlier run

Common in notebook-style workflows; can silently invalidate the entire computation.

### 20. Exception swallowing / non-failing verification

Examples:

- `try`/`except` around the critical check, with failure converted to logging
- Assertions disabled or replaced by warnings
- Code continues after "not implemented" branches and still prints summary conclusions

A proof computation must fail closed, not fail open.

### 21. Selective reporting

Examples:

- Show only successful test cases and omit failures or undecided cases
- Report one invariant that matches while ignoring another that does not
- Present a subgroup found by search without reporting that completeness was not
  established

Not necessarily fabrication of raw data, but invalid as proof because the omitted cases
may carry the entire obstruction.

### 22. Post hoc theorem fitting

The agent computes some data first, then searches for a theorem that would imply the
desired conclusion if only certain extra facts held, and writes as though those extra
facts were already established.

Examples:

- Compute discriminant/signature, then invoke a uniqueness theorem without checking its
  range conditions
- Observe a finite set of roots, then retrospectively assert the chamber is
  Vinberg-complete
- Match a known lattice in a database and report isometry without proving the
  identification

### 23. Prose replacing certificate

Several subforms:

- Long explanatory printouts instead of machine-checked predicates
- Verbal descriptions of why a search "should be enough" instead of a bound proving
  completeness
- Heuristic discussion of group structure in place of generators/relations/certified
  order

The key issue: explanation is substituting for a certificate.

### 24. Complexity avoidance by invalid algorithm substitution

When the real task requires a structurally appropriate algorithm — SNF, LLL,
orbit-stabilizer, Todd-Coxeter, GAP group routines, lattice reduction, exact linear
algebra over $\mathbb{Z}$, certified Gröbner methods, etc.
— the agent replaces it with an easier but mathematically non-equivalent brute-force
process.

Signals that the agent recognized the hard part but had no gate forcing it either to use
the correct algorithm or to stop.

### 25. Partial certificate presented as full certificate

Examples:

- Compute a candidate basis for roots but not prove spanning/completeness
- Compute a subgroup of the stabilizer and report the stabilizer
- Produce one direction of an isomorphism test but not the inverse or bijectivity
- Prove equality up to finite index and report equality

Especially common because the partial object often looks substantial.

### 26. Circular proof through the target invariant

Examples:

- To prove $L \cong L'$, define a normal form using an isometry oracle and then compare
  normal forms
- To prove a set is complete, use a membership test that itself assumes completeness of
  the set
- To prove primitivity, compute with a basis already assumed to be primitive

The computation appears nontrivial, but the needed property has been built into the
machinery.

### 27. Ambiguous quantifier weakening

Examples:

- "For many", "for all tested", "generically", "in practice", "appears to" quietly
  replacing "for all"
- "The computation suggests" in a place where the deliverable requested a proof
- "Up to numerical precision" replacing exact equality in an arithmetic theorem

Linguistic failure: the quantifier or modality is weakened in the premises and
strengthened again in the conclusion.

### 28. Output-only verification

The agent checks only that the final printed objects have the expected shape or values,
not that they satisfy the defining equations.

Examples:

- Matrix has the right size and determinant $\pm1$, so it is called an isometry
- List has the expected cardinality, so it is called the complete root set
- Group presentation has the expected order on examples, so it is called the correct
  stabilizer

This is matching a signature, not proving the property.

* * *

## Formal Proof Auditing (Lean 4 / Aristotle)

### Pre-Conditions

- Check upstream mathlib for existing results before formalizing
- Never spend Aristotle budget reproving upstream theorems
- Target results must be stated in `notes/proofs/` with Lean theorem names

### Acceptance Criteria

- [ ] Theorem statement matches the mathematical claim in GOAL.md
- [ ] Proof uses imported mathlib theorems, not ad-hoc tactics
- [ ] No `sorry` placeholders remain
- [ ] Build succeeds via `just lean-check` or equivalent

### What Constitutes Proof in Lean

- A completed proof term with no `sorry`
- Import chain traces to mathlib or project foundations
- Theorem statement is mathematically precise, not hand-wavy

* * *

## References

- **Nikulin (1979)**: Integer symmetric bilinear forms — genus classification, embedding
  uniqueness
- **Sterk (1991)**: Compactifications of Enriques moduli — isotropic orbit technique
- **Dolgachev & Kondyrev (2013)**: Moduli of Coble surfaces — lattice invariants
- **AEGS (2023)**: Compact moduli of Enriques surfaces — modern constructions

## Current verification baseline

The `GOAL.md` Tasks 1.1 through 6.1 are unverified unless a current accepted artifact proves the specific obligation through the standards in this document. Older proof notes may contain useful mathematical reasoning, but any former "verified" claims traced to deleted scripts, print-only scripts, self-validating assertions, or stale outputs are not accepted evidence.
