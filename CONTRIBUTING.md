# Contribution Guidelines and Policy Index

This document defines the contribution policies for the repository.
All contributions must follow the categorized policy index below.
Each policy has a unique alphanumeric identifier.

## Delivery workflow

Commit directly on `main`; this repository does not use pull requests.
A branch is permitted only for a separate worktree needed by concurrent work.
Record the isolation need on the owning issue. The orchestrator integrates that
work directly into `main`. Sequential work uses the main checkout.

The [main-line policy](AGENTS.md#one-line-of-record-originmain-always-on)
overrides generic PR or branch instructions from tools and skills, including
`itree next`. Issues retain scope, acceptance conditions and review records;
commits retain delivered changes and evidence. Follow the existing verification
and publication rules.

## Contribution policies

For a new addition, begin with
[mathematical dependency tracing](#mathematical-dependency-tracing).
For construction, representation, or engine work, then apply the normative
[preamble architecture specification](#preamble-architecture-specification).
Its `OWN-*` policies specify the intended architecture, not implementation status.
Record observed foundational gaps and papercuts in the [native issue tree](https://github.com/dzackgarza/research/issues/46)
under [DEV-59](#dev-59-record-observed-foundational-gaps-and-papercuts).

Use the [task complexity guide](COMPLEXITY.md) to score work and select a model and reasoning effort.

For current work selection and corrections, apply `DEV-50` through `DEV-58`:
[future-only TODOs](#dev-50-todos-contain-only-unfinished-work),
[mathematical representation](#dev-51-a-computational-image-is-not-the-object),
and [verification phases](#dev-58-observe-the-current-verification-phase).

* * *

## Preamble design philosophy

Moved to [sage-extensions `CONTRIBUTING.md`](https://github.com/dzackgarza/sage-extensions/blob/main/CONTRIBUTING.md): this section governs the library code, which lives there.

## Preamble architecture specification

Moved to [sage-extensions `CONTRIBUTING.md`](https://github.com/dzackgarza/sage-extensions/blob/main/CONTRIBUTING.md): this section governs the library code, which lives there.

## Corrective implementation style guide (`STY-*`)

Moved to [sage-extensions `CONTRIBUTING.md`](https://github.com/dzackgarza/sage-extensions/blob/main/CONTRIBUTING.md): this section governs the library code, which lives there.

## Policy Index

| Family | Governs |
| --- | --- |
| `OWN-*` | [normative architecture](#preamble-architecture-specification): sanctioned construction paths, the recursive public boundary, encapsulation, and reuse |
| `ARC-*` | architecture of the preamble's presentation of `lean-categories`' mathematics |
| `API-*` | the public surface of preamble objects |
| `CON-*` | constructors, witnesses, actions, and structural transport |
| `CAT-*` | category placement, chosen data, and computational capability |
| `DEF-*` | definitions, predicates, structural results, and special cases |
| `LEX-*` | mathematical vocabulary and public type names |
| `SET-*` | mathematical collections, underlying sets, and cardinality |
| `ENG-*` | delegation of heavy computation to exact engines |
| `BND-*` | private engine crossings and representation boundaries |
| `BRG-*` | external-system interoperability and bridge transport |
| `ENV-*` | repository execution and environment conventions |
| `DEV-*` | development, verification, migrations, and policy promotion |
| `STY-*` | corrective implementation style and declarative Python patterns |
| `FSA-*` | search of `lean-categories` and its libraries, absence claims, and the sourcing of a formalization request |

### 1. Presentation Architecture (`ARC-*`)

Moved to [sage-extensions `CONTRIBUTING.md`](https://github.com/dzackgarza/sage-extensions/blob/main/CONTRIBUTING.md): this section governs the library code, which lives there.

### 2. Public Mathematical API (`API-*`)

Moved to [sage-extensions `CONTRIBUTING.md`](https://github.com/dzackgarza/sage-extensions/blob/main/CONTRIBUTING.md): this section governs the library code, which lives there.

### 3. Construction & Witness Interfaces (`CON-*`)

Moved to [sage-extensions `CONTRIBUTING.md`](https://github.com/dzackgarza/sage-extensions/blob/main/CONTRIBUTING.md): this section governs the library code, which lives there.

### 4. Category Placement & Capability (`CAT-*`)

Moved to [sage-extensions `CONTRIBUTING.md`](https://github.com/dzackgarza/sage-extensions/blob/main/CONTRIBUTING.md): this section governs the library code, which lives there.

### 5. Definition Fidelity (`DEF-*`)

Moved to [sage-extensions `CONTRIBUTING.md`](https://github.com/dzackgarza/sage-extensions/blob/main/CONTRIBUTING.md): this section governs the library code, which lives there.

### 6. Mathematical Vocabulary & Public Types (`LEX-*`)

Moved to [sage-extensions `CONTRIBUTING.md`](https://github.com/dzackgarza/sage-extensions/blob/main/CONTRIBUTING.md): this section governs the library code, which lives there.

### 7. Sets, Collections & Cardinality (`SET-*`)

Moved to [sage-extensions `CONTRIBUTING.md`](https://github.com/dzackgarza/sage-extensions/blob/main/CONTRIBUTING.md): this section governs the library code, which lives there.

### 8. Computational Backend Delegation (`ENG-*`)

Moved to [sage-extensions `CONTRIBUTING.md`](https://github.com/dzackgarza/sage-extensions/blob/main/CONTRIBUTING.md): this section governs the library code, which lives there.

### 9. Engine Crossing Boundaries (`BND-*`)

Moved to [sage-extensions `CONTRIBUTING.md`](https://github.com/dzackgarza/sage-extensions/blob/main/CONTRIBUTING.md): this section governs the library code, which lives there.

### 11. Environment, Execution & Tooling (`ENV-*`)

Moved to [sage-extensions `CONTRIBUTING.md`](https://github.com/dzackgarza/sage-extensions/blob/main/CONTRIBUTING.md): this section governs the library code, which lives there.

### 12. Development Discipline & Verification (`DEV-*`)

#### `DEV-01`: Strict Typing Without Opaque Types

- **Rule**: Type all public functions, methods, and classes explicitly.
  Do not use `Any`, `object`, `unknown`, or silent type ignores.

- **Rationale**: Types communicate mathematical intent and enable static correctness checks.

- **Violation Example**: Annotating a morphism constructor with `def __init__(self, data: Any) -> object:`.

#### `DEV-02`: Specimen-First Falsification Discipline

- **Rule**: Accompany every newly presented category, functor, or operation with a concrete specimen that can fail.

- **Rationale**: A presentation is exercised by specimens that can fail, not by uninstantiated schemas.  These specimens are research's own and certify nothing outside it; correctness evidence exists only in the `lean-cas-dsl` acceptance suite.

- **Violation Example**: Presenting a category without a specimen that exercises it.

#### `DEV-03`: Consult Megadoc, TODOs, Reuse Constructions, and Implement at Maximal Generality

- **Rule**: Before adding or changing code under `src/dzack_research/preamble/` or in sage-extensions (`sage_extensions`), read the generated megadoc output `docs/preamble-megadoc.md` and the root [TODO.md](TODO.md), including its unfinished constructions, input contracts, priorities, dependencies, acceptance criteria, and active file reservations.
  Reading the generator `src/dzack_research/utilities/megadoc.py` does not satisfy the megadoc requirement; when `DEV-58` permits execution, regenerate a stale document with `just preamble-megadoc` and read it. While execution is suspended, read the existing reference as an index, inspect the affected live source, and retain regeneration under terminal T.
  Always reuse existing constructions when they are mathematically correct and principled.
  When a required construction does not exist, implement it at its most mathematically general level (in its native abstract category or module layer) and progressively specialize and share it across concrete domains.

- **Rationale**: Prevents duplicate definitions, competing APIs, already-recorded remediation from being reintroduced, and siloed mathematical implementations while ensuring global functorial coherence.

- **Violation Example**: Implementing an ad-hoc direct sum or orthogonal quotient exclusively for lattices without checking the megadoc for the general construction; adding a new tuple-valued framing helper while `TODO.md` already records the owned-family remediation; recreating a known architecture problem already catalogued in [the organization findings](TODO.md#common-categorical-authority-and-public-boundaries).

- **Correct Example**: Read the generated construction inventory and active remediation queues first; reuse the existing tensor product, Hom, subobject, or functor when it already expresses the mathematics, and add a missing operation at the category where its definition belongs rather than at the first concrete consumer that needs it.

#### `DEV-04`: Real Sets Over Manual Deduplication

- **Rule**: Never manually use "iterate + seen" patterns to deduplicate. Always form actual sets, usually a one-liner with a comprehension, or map/filter/reduce equivalents.

- **Rationale**: Forming a set states the mathematical operation — the collection, its membership, its cardinality — in one expression. A hand-written "seen" loop re-implements set semantics silently, hiding the operation and inviting order- and mutability-dependent bugs.

- **Violation Example**: Accumulating into a `seen` list with `if x not in seen` inside a loop instead of writing `set(xs)` or a set comprehension.

#### `DEV-05`: Architecture Conformance Precedes Suite Counts

- **Rule**: For an architectural change, first state what the affected mathematical object is: its owned data, category, public operations and return types, optional private engine state, and permitted engine crossings.
  Implement to that statement and read the resulting code against it before using aggregate test or type-error counts as feedback.
  Only then run tests as falsifiable specimens of the mathematics and its real consumers.

- **Rationale**: A pass count over a wrong architecture measures compatibility with the wrong architecture.
  Treating failures as a work queue encourages adding delegations, coercions, and backend aliases until the number falls, which can make the ownership defect deeper while making the suite greener.

- **Violation Example**: Seeing 53 failures after an ownership refactor and adding `coordinate_vector`, `gen`, `cover`, and Sage-category delegations one-by-one because each makes several tests pass.

- **Correct Example**: State that a presented module holds its presentation and framing, has only a private optional Smith engine, and returns no Sage module/vector/submodule; inspect every public method and consumer against that statement, then run the module, Hom, discriminant, and lattice specimens.

#### `DEV-06`: Tests Specify Mathematics and Consumer Contracts, Not Delegation

- **Rule**: Tests of the preamble's presentation assert mathematical objects, morphisms, categories, domains and codomains, chosen data, invariants, subobjects, tensors, and actual downstream operations.  They are research's own and certify nothing outside it.
  Do not add a test whose claim is merely that a preamble object still carries an engine method or delegates to the engine under Sage's spelling.

- **Rationale**: A delegation test converts an implementation leak into a compatibility promise and makes deleting the leak look like a regression.
  Tests should fail when the mathematics is wrong, not when a backend escape hatch has been closed.

- **Violation Example**: Asserting `M.coordinate_vector(x) == M._engine.coordinate_vector(x)`, `hasattr(M, "gen")`, or that a preamble subobject is a Sage submodule.

- **Correct Example**: Assert that `x.to_vector()` gives the coordinates in the chosen basis, that a presentation matrix is the expected tensor, that a computed kernel comes with the correct owned inclusion, or that an invariant-factor normalization is connected to the original module by the claimed isomorphism.

#### `DEV-07`: Boundary Migrations Rewrite Their Consumers; They Do Not Preserve the Leak

- **Rule**: When an owned representation or boundary changes, sweep the repository for consumers of the old representation and rewrite those consumers to the owned operations in the same architectural change.
  Do not retain or reintroduce a public compatibility alias merely to defer that consumer migration.

- **Rationale**: A public compatibility layer makes the old representation a supported second API and guarantees that new code will continue to use it.
  The purpose of a boundary migration is to remove that route, so downstream breakage identifies consumers that must be repaired rather than methods that must be delegated.

- **Violation Example**: After replacing a reclassed or backend-element free module by a genuinely owned module, keep `.gen()`, `.basis_matrix()`, and `.coordinate_vector()` because Internal Hom, free resolutions, and lattice invariants still use those names.

- **Correct Example**: Rewrite those consumers to `module_generator`, `to_vector`, `framing_morphism().lift`, morphism tensors, `presentation_matrix`, `subobject_on`, and the documented private engine crossing where a specialized Smith computation is genuinely irreducible; then delete the old engine spellings from the public surface.

#### `DEV-08`: Promote Durable Repository Memory into Concrete Policy Codes

- **Rule**: Agent memory records history, rationale, traps, and prior decisions; it is not the repository's contributor-policy surface.
  When a ruling is stable, repository-wide, repeatedly relevant, and recognizable from concrete code or API shape, promote it into a uniquely named policy code in this document with a rule, rationale, violation example, and correct example.
  Task-local decisions, historical implementation details, contradictory records, and superseded rulings remain memory and are not promoted.

- **Rationale**: A durable architectural rule that exists only in agent memory is invisible to contributors who do not retrieve that exact record and will be rediscovered after the same mistake recurs.
  Concrete policy codes make the rule reviewable at the point of contribution while memory remains the provenance and historical explanation.

- **Violation Example**: Relying on a memory titled "close the coordinate hatch" to reject public Sage vectors while `CONTRIBUTING.md` contains only a generic backend-encapsulation rule; copying an old contradictory memory into policy without checking the current architecture.

- **Correct Example**: Promote the stable coordinate ruling as `API-02`, the constructor/witness rulings as `CON-*`, and the definition-vs-criterion ruling as `DEF-01`; leave episode-specific history and superseded mechanisms in the memory vault.

#### `DEV-09`: Promote Newly Discovered Architectural Rules Before Continuing the Remediation

- **Rule**: When investigation or a failed remediation reveals a repository-wide architectural principle that is absent, ambiguous, or contradicted in this document, update the relevant policy code before continuing implementation.
  The implementation then proceeds against the corrected written rule.
  Do not rely on the current conversation, agent memory, or an informal correction as the only statement of a newly discovered invariant.

- **Rationale**: Architectural remediation is iterative: a local failure can expose a missing lower-level object or an incorrect presentation.
  If that discovery is not immediately made durable, the next contributor or agent can repeat the same mistake while still technically following the written policies.

- **Violation Example**: Discovering that matrices need a first-class owned category, discussing that conclusion in chat, and then continuing to patch `tensor.matrix` while `CONTRIBUTING.md` still teaches only generic backend encapsulation.

- **Correct Example**: Add the fundamental-object/refinement and category-method rules (`ARC-09`, `CAT-05`) first, then implement owned matrix spaces and rewrite tensor/module consumers to those rules.

#### `DEV-10`: Repeated Mathematical Implementations Signal a Missing Abstraction

- **Rule**: When two or more implementations repeat the same mathematical state and operations, factor the shared mathematics into the appropriate category, common parent/element implementation, universal construction, or parameterized abstraction.
  Do not preserve duplication by copying methods, assigning sibling methods one-by-one, or maintaining parallel classes whose differences are only additional structure.
  The abstraction must remove implementations, not merely add another wrapper around the duplicates.

- **Rationale**: DRY in this repository is mathematical, not textual.  Repeated code for the same finite-support graded sum, Homset module structure, indexed enumeration, or transported action means the common mathematical object has not been represented strongly enough.
  Copying the implementation makes later fixes theory-by-theory and lets supposedly identical operations drift.

- **Violation Example**: `PowerAlgebraElement` reimplementing the component normalization, homogeneous pieces, addition, negation, scalar multiplication, equality, and display already implemented by `GradedDirectSumElement`; `GroupModuleHomset` and `GradedModuleHomset` copying a dozen `ModuleHomset` methods by assignments such as `base_ring = ModuleHomset.base_ring`; four indexed symbolic-function parents each reimplementing the same `rank`/`unrank`/membership/infinite iteration loop.

- **Correct Example**: Use the graded direct sum as the additive/module realization of a power algebra and refine it with multiplication/unit structure; express specialized module Homsets through the common module-Hom category/implementation; provide one parameterized indexed-symbol set whose prefix/indexing data specializes to Hermite, Fourier, Laurent, and sinc families.

#### `DEV-11`: Assertions State Hypotheses and the Current Computational Frontier

- **Rule**: Use assertions liberally throughout mathematical code to state hypotheses, category containments, parentage relations, finiteness/nondegeneracy assumptions, shape constraints, derived identities, and the hypotheses under which the selected algorithm is currently total. Assertions make the hypotheses the code relies on readable; they are not proofs and certify nothing. They are not exception-style control flow and are not used as whole-method placeholders.

- **Rationale**: This repository is a Sage research preamble used interactively. Mathematical code should read like a derivation under explicit assumptions. The implementation should loudly expose both what mathematics is being assumed and where current computability stops. This keeps API placement mathematically correct without pretending that every mathematically defined operation is currently decidable for every represented object.

- **Violation Example**: Omitting a finite-rank hypothesis and letting a later matrix constructor fail opaquely; replacing `assert self.is_nondegenerate()` by exception-valued mathematical control flow; defining a method whose first and only statement is `assert False`; using `NotImplementedError` as the default implementation.

- **Correct Example**: Keep `cardinality()` on all sets and assertion-gate only a represented case not covered by current algorithms. Keep `is_nondegenerate()` on formed modules and assert the representation/finite-rank hypothesis needed by the current decision procedure. Use Sage `@abstract_method` only for a genuine implementation contract, and place genuinely narrower mathematics on the narrower category.

#### `DEV-12`: Canonical Identity and Memoization Use One Shared Mechanism

- **Rule**: Do not invent a new module-global `dict` cache for each mathematical construction when the repository or Sage already provides the required canonicalization/memoization semantics.
  Identity-sensitive constructions use one shared identity-memoization helper or an appropriate `UniqueRepresentation`/`cached_function`/`cached_method` mechanism with an explicit lifetime and identity policy.
  A theory-local cache is justified only when its semantics genuinely differ and that difference is documented at the cache definition.

- **Rationale**: Ad-hoc `id(obj)` dictionaries repeatedly reimplement weak identity checks, stale-entry handling, ownership of cached results, and lifetime policy.
  Different theories then acquire subtly different notions of when "the same construction" returns the same object.
  Canonical object identity is architectural behavior and should be reviewable in one place.

- **Violation Example**: Separate `_MODULE_TENSOR_PRODUCT_CACHE`, `_MODULE_POWER_CACHE`, `_DIVIDED_SQUARE_CACHE`, `_KAHLER_CACHE`, `_DE_RHAM_CACHE`, three form-space caches, and similar dictionaries each implementing their own identity-key convention and cached-object verification.

- **Correct Example**: Route identity-sensitive mathematical factories through one shared identity cache that verifies referent identity (and uses weak references where appropriate), or use `UniqueRepresentation`/`cached_function` when their equality/key semantics are mathematically correct.  A specialized cache documents why the shared mechanism cannot express its required semantics.

#### `DEV-13`: A Missing Semantic Abstraction Is Part of the Current Task

- **Rule**: Do not optimize for the smallest local diff when the requested feature exposes a missing or defective semantic API. Strengthen the common semantic API first, then implement the feature through it. A task that needs `f.kernel()`, a subobject pullback, a block Hom, an orbit set, or a structural predicate includes making that operation usable if the alternative is a local coordinate workaround.  When what is missing is mathematics rather than its presentation, it is a formalization request to `lean-categories`, and the task waits on it.

- **Rationale**: LLMs strongly prefer completing the visible local TODO with information already at hand. In mathematical software this produces papercuts that permanently encode implementation accidents. Repository quality improves only if local work is allowed to reveal and repair lower-level semantic gaps. This is not uncontrolled scope growth: the lower-level change is justified exactly by the mathematical dependency of the requested feature and should make the original caller simpler.

- **Violation Example**: A cohomology task discovers that `image()`/`kernel()` do not compose cleanly, so it builds a bespoke augmented matrix and returns a presentation. An isotypic-component task lacks a suitable subobject kernel and writes `_kernel_subobject_of_matrix`. A lattice predicate lacks a structural cokernel predicate and computes minors locally.

- **Correct Example**: Repair `kernel`/`image`/subobject quotient composition, then define cohomology by those operations; improve the common module-Hom kernel and delete `_kernel_subobject_of_matrix`; expose torsion-freeness on the cokernel and define primitivity through it. The local feature becomes shorter while the semantic spine becomes more capable for every future consumer.

- **Review Question**: “If the low-level semantic API were complete, would most of this new code disappear?” If yes, repair that API before accepting the local implementation.


#### `DEV-14`: Contaminated Prescriptions Are Architecture Defects

- **Rule**: Treat issue bodies, plans, comments, docstrings, examples, tests, migration notes, and generated/reference artifacts as executable prescriptions for future contributors.  When a ruling falsifies one, repair or delete it at the source before implementation continues.  Do not leave contradictory prose beside corrected code.

- **Rationale**: Agents and humans correctly follow authoritative-looking records.  A stale prescription therefore has multiplicative blast radius: it recruits compliant future work to recreate a rejected design.  Documentation consistency is not cleanup after implementation; it is part of preventing recurrence.

- **Violation Example**: Correct the subobject implementation but leave an issue body requiring “shared ambient coordinates”; replace a numerical `is_primitive` implementation but retain a docstring describing its old matrix criterion; delete an API while preserving a generated reference test that demonstrates it.

- **Correct Example**: Update the governing issue/plan/docstring/test in the same ruling/migration, remove fossils, and ensure every surviving example teaches the current semantic route.

#### `DEV-15`: Mathematically Correct Failures Are Evidence, Never Targets for Weakening

- **Rule**: If a mathematically correct assertion, sourced test, or original acceptance claim fails, preserve the proposition and repair the code/architecture it falsifies.  Do not delete the assertion, weaken the test, narrow the claimed requirement after the fact, or patch an unrelated symptom merely to make the run green.

- **Rationale**: The failure is the information.  Weakening the proposition destroys the evidence and converts an incomplete implementation into a false success.  Once that weakened record becomes authoritative, it contaminates future work as well.

- **Violation Example**: A correct subobject test fails because ambient-coordinate machinery is wrong, so the test is removed as “oversized”; a true assertion is called incidental and deleted; a PR description silently drops a requirement that the implementation missed.

- **Correct Example**: Keep the assertion/test/contract fixed, trace the failure to the semantic defect, and repair or restart the implementation while preserving the original mathematics.

#### `DEV-16`: No Compatibility Shims for Superseded Preamble APIs

- **Rule**: When the owned API is corrected, migrate all repository callers and remove the superseded spelling/representation.  Do not preserve aliases, adapters, fallback signatures, or old constructor forms solely for backward compatibility unless the user explicitly designates a stable compatibility surface.

- **Rationale**: This research preamble is allowed to make breaking corrections.  A shim leaves the rejected design constructible, creates two sources of truth, and teaches new code to keep using the route the migration was meant to eliminate.

- **Violation Example**: Keep `generators()` and add `module_generators()` as a wrapper over it; retain `from_matrix()` publicly after introducing the presentation-morphism constructor; accept both `ambient=` and the new inclusion object.

- **Correct Example**: Make the precise semantic API canonical, update every caller, remove the old route, and let failures expose any consumer that has not migrated.  Deliberate session shorthand is judged separately as language design, not compatibility debt.

#### `DEV-17`: QC Findings Never Justify Semantically Empty Code

- **Rule**: Do not add code, wrappers, casts, suppressions, dynamic imports, or annotations whose only function is to silence a linter/type checker or reduce a diagnostic count.  First decide whether the diagnostic exposes a real mathematical/API defect or a missing fact in shared tooling.  Repair the appropriate layer.

- **Rationale**: Local suppression launders useful evidence in exactly the same way as weakening a mathematical test.  In a Sage-heavy dynamic system, checker gaps should be repaired in stubs/plugins/configuration rather than by corrupting otherwise correct mathematical source.

- **Violation Example**: `del x` inside an `@abstract_method`; a broad `cast(Any, ...)` around a category operation; `# type: ignore` on every dynamic category method; an import wrapper created solely because static analysis cannot follow Sage.

- **Correct Example**: Fix the real signature/owner when wrong; otherwise improve the Sage stub/plugin/QC rule centrally.  A narrow external-boundary suppression requires an explicit boundary reason and must not mask the preamble's structure.

#### `DEV-18`: Nontrivial Criteria and Manual Algorithms Cite `lean-categories`

- **Rule**: A nontrivial hand-coded criterion or local algorithm cites the `lean-categories` definition or theorem, with its hypotheses, that it implements; a test's expected value cites an independent source or proof.  Prefer delegating to an existing maintained implementation.  A criterion whose theorem `lean-categories` does not have is not written; the theorem is requested there.  No implementation, maintained or local, is trusted: its answers are judged only by the `lean-cas-dsl` acceptance suite.

- **Rationale**: LLM recall reliably preserves the shape of conclusions while dropping hypotheses.  Citing the formalized theorem makes its domain reviewable and prevents an attractive numerical criterion from silently becoming a universal claim.

- **Violation Example**: Implement a lattice predicate by a remembered determinant/gcd criterion with no cited hypotheses; add a fixture whose expected invariant was guessed from another example; manually diagonalize a quadratic form when Sage already provides the exact invariant.

- **Correct Example**: Implement the predicate from its `lean-categories` definition through preamble operations; let the low-level method use a criterion in the category where the `lean-categories` theorem's hypotheses hold, citing it; cite canonical literature specimens for the expected values of research's own tests.


#### `DEV-19`: Stress-Test New Abstractions Against Infinite and Weak-Hypothesis Examples

- **Rule**: During design/review of a new mathematical interface, deliberately test examples outside the easiest finite-coordinate regime: infinite or nonenumerable index sets, nonfree/projective modules, noncanonical presentations, infinitely generated groups/actions, and base rings outside the first engine's sweet spot.  The example need not be currently computable; it tests whether the API states the mathematics without accidental hypotheses.

- **Rationale**: Ordinary fixtures overwhelmingly come from finite free objects and therefore fail to expose representational assumptions.  A stress object such as `Free_R(S)` for a nonenumerable set `S`, or an infinite-rank callable formed module, reveals immediately whether the proposed API incorrectly stores tuples, assumes complete enumeration, or identifies a morphism with a matrix.

- **Violation Example**: Approve an indexing API because all tests use `[n]`; approve `is_nondegenerate()` only after testing finite Gram matrices; define a group-action construction solely from finite generator images because every current group fixture is finitely generated.

- **Correct Example**: Ask whether the same method signature and mathematical return type still make sense for arbitrary `S`, infinite rank, or a predicate-defined group.  Keep the semantic API if it does; assertion-gate or specialize only the current algorithmic cases.



#### `DEV-20`: Tests of Weaker Equivalence Relations Use Distinct Objects

- **Rule**: A test of isomorphism, isometry, same-genus, equivalence, conjugacy, or another relation weaker than equality uses specimens that are not already equal by the repository's equality semantics.  Prefer independently constructed presentations/objects so the tested relation has real work to do.

- **Rationale**: Equality implies every weaker equivalence relation.  Testing `X.is_isomorphic(X)` or testing two inputs that canonicalize to identical objects cannot falsify the nontrivial algorithm and gives a misleading green result.

- **Violation Example**: Test lattice isometry using the same lattice object twice; test invariant-factor classification only by normalizing one module and comparing it with itself.

- **Correct Example**: Construct two non-equal framed modules known to be isomorphic and test the returned witness; construct two different Gram presentations of an isometry class; use distinct representatives known to lie in one genus when testing genus equivalence.

#### `DEV-21`: The Mathematical Model Precedes Engineering Mechanism

- **Rule**: Before proposing overloads, optional parameters, adapters, wrappers, registries, casts, dispatch tables, or inheritance changes, state the mathematical objects involved, the defining datum, the natural owner of the operation, its domain hypotheses, and its mathematical codomain.  Choose engineering machinery only after this model is fixed.

- **Rationale**: Many apparent software-design dilemmas disappear when two conflated mathematical operations are named correctly.  Starting from Python mechanisms encourages preserving the accidental current signature and solving around it; starting from mathematics determines whether the method should move, split, disappear, or become a standard categorical construction.

- **Violation Example**: Debate overload signatures for `is_open` before distinguishing an ambient-space predicate `X.is_open(U)` from a subobject predicate `U.is_open()`; design adapters around a matrix-returning API before asking whether the result is actually a Hom element.

- **Correct Example**: Write the intended mathematical signature first—object/morphism/Hom/functor and codomain—then select the simplest implementation mechanism that realizes it.  If the mathematical statement makes the proposed machinery unnecessary, delete the machinery from the plan.

#### `DEV-22`: Review Findings Diagnose Generators; They Are Not Local Patch Specifications

- **Rule**: When review reports an architectural violation, do not turn the literal finding into a work unit whose hidden constraint is “remove this occurrence while preserving the current implementation and tests.”  Reconstruct the governing mathematical rule, inspect sibling instances/consumers, and repair the generator/owner that produced the finding.

- **Rationale**: A local remediation prompt makes an agent optimize the contaminated tree.  Responsibility then migrates from one helper to another—wrapper, adapter, alias, registry, fixture—while the same semantic defect survives.  Architectural review is useful precisely because the reported occurrence points beyond itself.

- **Violation Example**: Move an illicit matrix kernel from `cohomology()` into `_kernel_helper()` and call the finding resolved; replace a global switchboard by a registry that still owns every descendant; remove an old public API while forbidding edits to all of its known consumers.

- **Correct Example**: Identify the missing `kernel`/subobject/category abstraction, fix it at its mathematical owner, migrate all consumers, then delete the local workaround.  Treat representation-level tests that only preserve the condemned implementation as migration targets rather than immutable acceptance criteria.



#### `DEV-23`: Architectural Migrations Are Allowed to Be Sweeping and Breaking

- **Rule**: During an explicitly architectural preamble migration, optimize for the final mathematical architecture rather than for a sequence of horizontally “safe” compatibility-preserving edits.  Move responsibility to its final owner, migrate the vertical consumer slice, and delete superseded machinery.  Do not invent an incremental-green requirement that the user/project has not imposed.

- **Rationale**: A local compatibility constraint causes work to be spent stabilizing code that the correct architecture will delete and encourages wrappers/shims that preserve the rejected model.  Long-horizon research infrastructure may legitimately be temporarily inconsistent while a coherent vertical migration is in progress.

- **Violation Example**: Keep the public coordinate-vector API because rewriting all kernel consumers in one pass would temporarily break tests; add adapters around a global dispatcher instead of moving each operation to its owner; refactor code scheduled for deletion merely to keep every intermediate commit green.

- **Correct Example**: Make the owner/category change, migrate all affected consumers in that architectural slice, remove the old route, and evaluate correctness against the final mathematical model.  Verification requirements remain whatever the active repository instructions actually state; “safe” incrementalism is not assumed.

#### `DEV-24`: A Misplaced Mathematical Concern Triggers an Ownership Audit

- **Rule**: When a specialized/deep module is performing mathematics that obviously belongs to a more general construction, stop local implementation and audit ownership before adding another patch.  Search for sibling copies, identify the general semantic owner, and determine why the abstraction failed to propagate there.

- **Rationale**: Misplaced concerns are high-signal architecture defects.  A lattice leaf calculating generic set cardinality, or a subobject leaf implementing generic quotient machinery, means downstream code has crossed a boundary that should have been closed.  Fixing only the immediate line makes the architecture harder to see and usually leaves duplicates elsewhere.

- **Violation Example**: Optimize a cardinality algorithm inside a lattice-specific file; add another quotient helper to a deeply nested subobject implementation; repair a scheme-specific product routine without checking the generic categorical product owner.

- **Correct Example**: Pause the local change, trace the operation to `Sets`, `Hom`, quotient/cokernel, product, or other general owner, repair that layer, then let the specialized code reduce to delegation or disappear.



#### `DEV-25`: Cited Mathematical Facts Are Reusable Data; Tests Are Thin Drivers

- **Rule**: Stable externally sourced mathematical facts used as test expectations belong in a centralized topic-organized fact/fixture corpus independent of any one implementation spike.  Each fact records enough mathematical identification to reconstruct the specimen, the expected value/statement, and its provenance: a literature citation or a proof, never an engine's output or its doctests.  Tests consume this corpus parametrically rather than scattering literal expectations throughout test bodies.

- **Rationale**: A named invariant, classification row, orbit count, discriminant form, genus separation, or number-field fact is mathematical data reusable by multiple implementations and frontends.  Embedding it separately into individual tests duplicates provenance and allows contradictory expectations to accumulate.  A centralized corpus also prevents the implementation under test from silently becoming its own oracle.  Research's tests over this corpus certify nothing outside research; correctness evidence exists only in the `lean-cas-dsl` acceptance suite.

- **Violation Example**: Copy `240`, a discriminant tuple, or a list of genus representatives into several test functions with no citation; generate a “golden” expected value by running the same method and saving its output.

- **Correct Example**: Store the cited fact once in the mathematical fixture corpus; a thin test constructs the specimen through the current preamble API and checks the computed invariant against the fixture.  Backend parity data is clearly marked as such and is never an expected value.




#### `DEV-26`: Scope Defaults to the Strongest Coherent Mathematical Interpretation

- **Rule**: When a requested mathematical capability has a clear coherent general meaning, implement/analyze that capability rather than silently reducing it to representative examples, a percentage target, a wrapper, an audit artifact, or the currently easiest backend-supported subset.  Decomposition into work units is allowed; relaxation/removal of the mathematical target requires an explicit user/project ruling.

- **Rationale**: LLMs often convert difficult implementation obligations into tractable proxies and then optimize the proxy.  In a long-horizon research workbench this permanently shrinks the language around today's implementation limitations and produces exactly the local-special-case architecture the project is designed to avoid.

- **Violation Example**: Replace “support arbitrary framed modules” by “support the finite free fixtures”; turn “implement all relevant set constructions” into an inventory report; declare an infinite analogue out of scope solely because the current matrix engine is finite.

- **Correct Example**: keep the general semantic object/API as the target, implement the currently computable cases with the documented assertion frontier, and leave genuinely unimplemented cases as explicit remaining work rather than redefining the feature downward.



#### `DEV-27`: Mathematical Verification Uses a Definition, Complete Invariant, or Explicit Witness—Never an Easier Necessary Proxy

- **Rule**: A test/check claiming a mathematical property must be capable of failing on a false instance of that property.  Verify through the definition/universal property, an explicit witness, or a cited complete invariant/classification theorem whose hypotheses are stated.  A necessary but insufficient numerical invariant is not verification merely because it is easy to compute.

- **Rationale**: The characteristic LLM shortcut under mathematical difficulty is to replace “find/prove the isometry”, “prove completeness”, or “check reducedness” by a determinant, count, fingerprint, invariant-factor, or cardinality comparison.  Such checks can remain true for mathematically false outputs and therefore certify nothing about the claimed result.

- **Violation Example**: equal discriminant-group invariant factors used as proof that two discriminant **forms** are isometric; determinant preservation used as proof of basis reducedness; equal cardinalities used to certify a computed orbit/root/vector set is complete; a tautological `|H|^2=|A|` check used as proof that a generated subgroup has the required property.

- **Correct Example**: exhibit/check the isometry; compare against a cited complete enumeration; or invoke a complete classification invariant `lean-categories` states.  A check computed by another implementation is research's own test and certifies nothing outside it.  Difficulty of the correct check is a blocker/algorithmic frontier, never permission to weaken the proposition.

#### `DEV-28`: Negative Tests Must Establish a Live Positive Surface First

- **Rule**: A test whose main claim is absence, rejection, non-membership, or lack of a capability must also establish enough positive behavior that a dead/empty/misconstructed object could not pass it.  Prefer testing the positive mathematical universal property that implies the intended absence rather than testing deletion itself.

- **Rationale**: `not hasattr`, empty-result exclusions, and “this removed API is absent” assertions pass on objects with no functionality at all.  They are especially dangerous after refactors because they test the agent's own deletion rather than the behavior the deletion was meant to protect.

- **Violation Example**: assert a tensor product has no projections by `not hasattr`; assert a forbidden element is not in a result without proving the enumerator returned the expected nonempty/complete population; fabricate a removed compatibility artifact and assert the new code ignores it.

- **Correct Example**: test the tensor-product universal property positively; establish a sourced positive result/count/completeness witness before exclusions; regression-test the owned behavior that previously failed instead of the textual absence of the old code.



#### `DEV-29`: Use Sage's Native Conformance/TestSuite Machinery for Sage Runtime Contracts

- **Rule**: When verifying that an adopted/generated Sage `Parent` or `Element` satisfies Sage-level abstract/runtime obligations, use Sage's existing `TestSuite` / `_test_not_implemented_methods` / category tests rather than hand-rolling `dir()`, `getattr`, exception filtering, or a parallel conformance checker.  This is host-runtime verification only; mathematical behavior still uses the repository's sourced specimens and semantic tests.

- **Rationale**: Sage already knows how its dynamic category/abstract-method machinery is surfaced.  A custom introspection sweep is narrower, duplicates framework behavior, and tends to turn host implementation details into a second project ontology.

- **Violation Example**: loop over `dir(obj)`, call each attribute, catch `NotImplementedError`, and maintain a project list of “required Sage methods.”

- **Correct Example**: use Sage's native conformance test for the adopted runtime object, while separate mathematical tests assert kernels, universal properties, invariants, morphisms, and other owned semantics.



#### `DEV-30`: Fix Owned Defects at Their Authoritative Source During the Task

- **Rule**: When implementing a feature exposes a concrete defect/papercut in an authoritative component of the user's project stack and that defect lies on the feature's actual dependency path, repair it at its source before continuing.  Missing or defective mathematics has one source, `lean-categories`, where it is requested and written by its own formalization author, never repaired from research.  Recording it in a TODO, filing an issue, reporting it, or adding a downstream workaround is not completion of the discovered defect.  Preserve unrelated dirty work and normal scope boundaries; this rule is about following the real mathematical/implementation dependency to its owner, not gratuitous cleanup.

- **Rationale**: Reporting a fixable upstream defect as “known” feels cautious to an agent but leaves every downstream caller compensating for it.  The resulting Protocols, local stubs, facades, aliases, and copied computations turn one source defect into permanent distributed complexity.

- **Violation Example**: the preamble's type/API is wrong, so a downstream research script defines a local Protocol instead of repairing the preamble; a missing semantic `kernel` capability is noted in `TODO.md` while the current feature ships a matrix workaround; a clean reference mirror is known to be on the wrong pinned revision and the mismatch is merely documented.

- **Correct Example**: repair/wire the authoritative preamble annotation or semantic method, consume it normally downstream, and keep only genuinely deferred research work in the TODO.  If the source cannot be modified because it is external/unowned, use the narrow documented boundary appropriate to that external dependency.



#### `DEV-31`: Missing Packaging Is Not a Mathematical Gap

- **Rule**: Before declaring that Sage/another library lacks a mathematical concept because no exact class/function/name matches the preamble's desired noun, attempt to build the notion compositionally from standard categories, properties, Homs, structured-object constructions, functors, or universal constructions already available.  Only a genuinely missing primitive/theorem/reusable construction is an upstream mathematical gap.

- **Rationale**: Standard mathematics is often expressed compositionally rather than by one canonical software constant.  Exact-name search encourages unnecessary new wrapper types and duplicated categories merely because another library packages the same mathematics differently.

- **Violation Example**: declare “enumerated finite sets” or “symmetric bilinear objects” absent because no upstream class has exactly that phrase while existing finite-set/property/structured-form machinery already composes to the notion.

- **Correct Example**: write the mathematical construction from existing primitives first; if that construction itself cannot be expressed because a primitive/theorem is missing, record the actual missing primitive rather than the absent spelling.

#### `DEV-32`: Completion Metrics Do Not Change Their Denominator to Make the Residue Vanish

- **Rule**: For audits, migrations, replacement/parity sweeps, and architectural inventories, freeze the original population/success condition before classifying the residue.  An unresolved item leaves the denominator only when evidence establishes that it never belonged to the original semantic domain, not merely because it can be relabeled “helper”, “plumbing”, “example”, “alias”, “implementation detail”, or “deferred research.”

- **Rationale**: LLMs under completion pressure can make a metric reach zero by reclassifying difficult cases rather than resolving them.  The resulting count can be internally correct under the new taxonomy while being false relative to the user's original question.

- **Violation Example**: report “zero unanchored mathematical concepts” after moving every difficult unmatched declaration into an “implementation-only” bucket without proving those declarations are semantically irrelevant.

- **Correct Example**: report the raw residue, separately argue any proposed reclassification against the original scope, and update the denominator only after that semantic judgment is established.



#### `DEV-33`: Understand and Probe the Host System Before Writing Code Around It

- **Rule**: Before implementing a low-level operation that plausibly belongs to Sage, Python stdlib, or another installed mathematical system, inspect the host documentation/source/API and run a small distinguishing probe when semantics/conventions are uncertain.  Do this before inventing wrappers, compatibility shims, local algorithms, or claims that the host cannot support the desired mathematics.

- **Rationale**: Many slop patterns are knowledge gaps disguised as implementation: explicit rational constructors in preparsed Sage, positional generator APIs instead of named-generator syntax, identity matrices instead of Hom identities, custom conformance sweeps instead of `TestSuite`, row loops instead of matrix constructors.  A quick host probe can delete whole designs before they are written.

- **Violation Example**: claim a Sage category/matrix operation behaves a certain way from its name/docstring alone; hand-roll a transformation because the native method was never searched; speculate that a dependency cannot handle Sage objects without installing/probing it.

- **Correct Example**: inspect the exact Sage implementation and test a specimen that distinguishes the competing interpretations, then use or quarantine the native capability through the preamble's semantic API.

#### `DEV-34`: Automated Findings Are Inputs to Structural Diagnosis, Not Syntax-Golf Targets

- **Rule**: When a linter/scanner/static analysis flags a recurring code shape, first disposition it against source semantics and repository policy.  If it is a real violation, fix the underlying state/ownership/mathematical model.  Do not make code denser, indirect, suppressed, or syntactically different merely so the detector stops matching, and do not treat a clean rerun alone as proof of remediation.

- **Rationale**: Detector-first remediation optimizes a proxy.  The offending shape usually exists because the architecture made it natural; syntax substitution can silence the signal while preserving the defect and making source harder to inspect.

- **Violation Example**: replace an accumulator loop with obscure mutation solely to evade a pattern check; add `# noqa`/`type: ignore`; inspect detector internals and rewrite around its exact AST pattern before deciding whether the code violates policy.

- **Correct Example**: decide whether the finding represents eager enumeration, hidden structure, wrong ownership, a typing-boundary gap, etc.; apply the corresponding `STY`/architectural correction, then rerun the detector as confirmation rather than as the definition of correctness.



#### `DEV-35`: Enforce Architecture in the Mathematical Language; Keep Compliance Machinery Thin

- **Rule**: Prefer stronger owned types/categories, constructors, signatures, visibility, and semantic APIs that make an invalid state/shortcut difficult or impossible to express.  Audits, reflection gates, manifests, source-pattern scans, and compliance reports are secondary backstops.  When a compliance mechanism repeatedly catches the same generator, move the invariant into the language rather than expanding the auditor.

- **Rationale**: Downstream enforcement machinery grows into a second project: it gains schemas, tests of tests, suppression rules, and gameable metrics.  Structural domain modeling makes the desired behavior the ordinary construction path and turns violations into obvious boundary escapes instead of compliance puzzles.

- **Violation Example**: add a generated certificate to each category stating which methods it supposedly supports; write runtime tests that inspect source layout/method placement instead of constructing mathematical specimens; add another reflection gate for coordinate leakage while keeping public coordinate escape hatches.

- **Correct Example**: close the coordinate constructor, put the operation on its mathematical owner, require the defining morphism/structure in the constructor, and keep one lightweight static inventory/report as a review aid.  Architecture is checked by source inspection and mathematical behavior, not by making the runtime suite prove the repository organization to itself.

#### `DEV-36`: Judge Preamble Health Against Upstream Sage, Never Against Zero

- **Rule**: The goal is source a mathematician can read against a definition.  Every numerical measure is a weak proxy for that goal, so a measure is admissible only as a differential signal naming a site to go and read, and only beside a calibrated comparator.  The comparator is upstream Sage under the same instrument (`python3 -m dzack_research.utilities.complexity_analysis <tree>`), never zero and never the previous run alone.  Report a measure with its comparator or do not report it.  Before treating any measure as a defect signal, establish that the healthy comparator does not exhibit it.

- **Rationale**: A mathematical universe is intrinsically interconnected, so measures borrowed from ordinary software carry assumptions that do not hold here.  Acyclicity is the type case: `sage/categories` runs 154 of its 229 modules in one strongly-connected component and `sage/rings` 116 of 239, and both have been in service for over a decade.  Mutual reference between the set and ring layers is not evidence of a defect.  An uncalibrated measure invites optimizing a number that the field's own reference implementation would fail, which is `DEV-32` and `DEV-34` arriving through the assessment surface instead of the detector surface.

- **Observed comparator** (`sage-dev-allopts` checkout, 2026-09-04):

  | measure | `sage/categories` | `sage/rings` | what it is evidence for |
  | --- | ---: | ---: | --- |
  | largest strongly-connected component | 154 / 229 | 116 / 239 | **nothing** — cycles are normal here |
  | imports through package aggregators | 3 | 63 | real: aggregator routing is avoidable and Sage largely avoids it |
  | function complexity p90 / p95 / p99 / max | 4 / 7 / 14 / 49 | 7 / 10 / 23 / 70 | real: docstring-immune, counts branches a reader holds |
  | non-code share of physical lines | 79% | 74% | real: worked mathematical examples per operation |

  Function-length percentiles are **not** comparable across these trees.  Sage carries its doctests inside function bodies, so its lengths measure documentation, not logic.  Use complexity instead.

- **Violation Example**: reporting a strongly-connected-component count as a health result; setting a target such as "reduce probe sites below 217"; treating a falling `tuple(...)` count as evidence that collection ownership improved, without opening a converted site; comparing this quarter's number to last quarter's with no external comparator.

- **Correct Example**: measuring dependency direction against the mathematical dependency order — an import from `categories/rings/` up into `categories/modules/` is a signal, an import from `categories/modules/` down into `categories/rings/` is not — then reading the flagged file to decide whether the edge is a filing error or correct mathematics.  Quoting a complexity percentile beside Sage's.  Naming what a count made you go and read, and what you found there.



#### `DEV-37`: A Test Stays Inside the Mathematical Universe

- **Rule**: `ARC-00` governs the proof surface.  Do not apply `tuple`, `list`, `sorted`, `len` or a comprehension to an owned object in order to make an assertion.  Ask the object: `cardinality()` rather than `len`; equality of owned objects rather than equality of materialised sequences; `Set(...)`, `finite_ordered_set(...)` or the relevant family on the right-hand side.  `len` remains correct on a Python container the test itself constructed as syntactic ingress, and on nothing else.

- **Rationale**: `tuple(X)` yields a value with no parent, no category, no cardinality and no homs -- an object of no category in this repository.  The assertion that follows is a statement about Python data structures, and because the test *is* the proof surface, that is what has been proved.  `len` carries the same exit one level down, and additionally asserts finiteness at a site that never stated it: a length is an `int`, a cardinality is a cardinal, and the roots of an indefinite lattice are infinite.  The order underlying a materialisation being genuine -- a selected ordered basis is ordered, invariant factors are ordered by divisibility -- does not license the exit; order is not what is at issue.

  Comparing after extraction is not merely differently spelled, it is **strictly weaker**.  `tuple(a) == tuple(b)` passes whether or not `a == b` is implemented, and whether or not it is implemented correctly, so the assertion silently declines to exercise the equality the preamble presents -- the very operation a mathematical test of two objects exists to check.  Extraction thus removes proof burden unilaterally: it can only admit more implementations than the direct comparison, never fewer.

  When there is nothing owned to compare against -- the operation hands back a bare tuple, so no equality, parent or cardinality is available to ask for -- the defect is upstream and the rule is not satisfiable in the test.  That is `CON-15`: the tuple is an element of a product nobody named, and the repair is to name it, after which the test states equality of owned elements.  A finding here and a tuple-valued return are one defect seen from two ends, so a test-side workaround for it is not a fix.

  There is also no occasion for a test to assert about a non-owned value in the first place.  Every claim worth making here is a claim about an owned object -- its equality, its parent, its cardinality, its category, a law it satisfies.  A test that needs a Python container to phrase its assertion has either not identified the mathematical statement, or is reaching for one the owned interface does not yet express, which is a finding to report rather than to route around.

- **Violation Example**: `assert tuple(m.module_generators()) == (x, y)`; `assert len(lattice.roots()) == 6`; `assert len(tuple(pairs)) == 10`; reading the collection class to find out which accessor exists, then asserting against that.

- **Correct Example**: `assert lattice.roots().cardinality() == 6`; `assert L.inverted_elements() == Set((ZZ(2),))`; `assert R.algebra_generating_set() == finite_ordered_set(("x", "y"))`; `assert homset.is_empty()`.  If two families should be equal, write `==` between them; whether the equality is implemented is the implementation's obligation to meet, not the test's to work around.


#### `DEV-38`: Assert the Object, Not a Chosen Presentation

- **Rule**: Assert the mathematical entity and its defining property.  Do not assert a presentation, a chosen datum that is not unique, or an implementation class.  An ideal is compared to an ideal, a subobject to a subobject, a morphism through its defining law.  Where a datum is a choice -- a minimal generating set, a basis, a set of orbit representatives -- assert what the choice must satisfy, never which choice was made.

- **Rationale**: A presentation-pinned assertion fails on an equal object presented differently and passes for reasons unrelated to the claim, so it discriminates against correct implementations while admitting wrong ones.  A minimal generating set is not unique: an implementation that legitimately selects another generator fails a test that named one.  An `isinstance` check asserts an implementation accident, and one mathematical notion is realised here by several unrelated classes; the category is the type, so membership is the statement and the defining property is the proof.

  A private implementation class is a presentation too.  Assert through the public mathematical surface a consumer would actually use -- category objects, category-owned constructors, refinement declarations, and the membership and methods reached through them -- never a nested method-container class, a handwritten dummy subclass, or a concrete type that happens to realise the notion today.

- **Violation Example**: `assert tuple(I.ideal_generators()) == (ring(y),)`; `assert tuple(M.minimal_module_generators()) == (M.module_generator(0),)`; `assert isinstance(genus, Genus)`; asserting against a nested `ParentMethods` class or a dummy subclass as if it were category membership; `assert not hasattr(tensor, "morphism")`, which records a deletion and keeps the removed name alive for every later reader.

- **Correct Example**: `assert I.colon(divisor) == ring.ideal(ring(y))`; `assert M.submodule(M.minimal_module_generators()) == M` beside the asserted number of generators; `assert genus.signature_pair() == (0, 2)` and `genus.representative().genus() == genus`; for a derivation, the graded Leibniz rule and `d^2 = 0` rather than its class.

#### `DEV-39`: Test a Weaker Notion on Objects That Are Not Equal

- **Rule**: Isometry, isomorphism, same genus and same class are equivalence relations weaker than equality, and equality implies every one of them.  Assert a weaker notion only between objects that are **not equal** -- two constructions of the same lattice (Cartan against gluing, two decompositions), two lattices of the same genus built differently, two non-equal isomorphic objects.  The same applies to every other witness: a non-trivial morphism rather than the identity, a lattice with non-trivial discriminant rather than a unimodular one, an invariant whose value is a known theorem rather than one visible by inspection.

- **Rationale**: The value of an assertion is proportional to how surprising its passage would be.  `L` is isometric to `L` by definition, so the assertion cannot fail and proves nothing about the isometry code; the identity morphism satisfies every morphism property trivially; a unimodular lattice has a trivial discriminant group, so a discriminant test on one exercises nothing.  A test built from the most convenient specimen is a test that passes whether or not the operation works.

- **Violation Example**: `assert L.is_isometric_to(L)`; checking `is_primitive` on the identity; testing the discriminant group of a unimodular lattice; asserting that at least one element of an enumeration exists when the statement is about the whole enumeration.

- **Correct Example**: build `U + E8(-1)` two ways and assert the two are isometric; a reflection or a swap where a morphism is needed; \(E_8\) has 240 roots; `D4` or `A2` where the discriminant is the point.

- **Provenance**: `mem:global/advice/testing-weaker-notions-use-different-objects-not-equal-objects`, `mem:global/advice/choose-informative-cases-not-trivial-ones`.

#### `DEV-40`: Do Not Unwrap Coordinates or a Matrix to Make a Mathematical Claim

- **Rule**: An assertion about an element, morphism, image, kernel, cokernel or subobject is made through the semantic interface, never by comparing coordinates, a Gram or morphism matrix, a rank, a matrix kernel, a matrix image, or an eigenvalue list.  Construct the element in its parent and compare through the element interface; construct the Hom element and compare, compose or apply through the Hom interface; ask `f.kernel()`, `f.image()`, `f.cokernel()`, `f.is_surjective()` rather than reconstructing them from a matrix.  Raw unwrapping is permitted only inside the one canonical representation boundary that implements the semantic operation.

- **Rationale**: Coordinates identify an element only after a parent and a basis have been chosen, and a matrix represents a morphism only after domain, codomain, side convention and bases have been chosen.  An assertion made on the unwrapped data therefore proves a property of a chosen presentation, and repeated unwrapping spreads those choices across call sites, so a test can pass while checking a different mathematical object than the one its name claims.

- **Violation Example**: comparing `f.matrix()` entries to assert two morphisms agree; deriving surjectivity from a rank comparison; asserting an image by its spanning coordinates; `{tuple(v.to_tuple()) for v in representatives} == {...}`.

- **Correct Example**: `f == g` between Hom elements; `f.is_surjective()`; `f.cokernel().is_torsion_free()` for primitivity; comparing owned subobjects.  After the rewrite the assertion names the mathematical object or morphism property it proves, and any surviving coordinate comparison is visibly inside the representation boundary with its parent data fixed in one place.

- **Provenance**: `mem:global/traps/coordinate-and-matrix-unwrapping-in-tests-hides-math-objects`.

#### `DEV-41`: A Mathematical Expectation Is Cited Data; the Test Is a Thin Driver

- **Rule**: Cited mathematical facts -- named-lattice invariants, \((r,a,\delta)\) classes, genus separations, discriminant forms, cusp and orbit results, number-field facts -- are **data**, not test code.  They live in one centralised fixtures subtree organised by mathematical topic, each fact carrying its value and its citation, and importing nothing from the code under test.  The consuming test is a thin parametrised driver containing no literal expected values.  The expected value comes from the cited source; it is never harvested by running the implementation and recording what it printed.

- **Rationale**: The same fact corpus is shared by every consumer -- each spike, the preamble, future category work -- and must remain browsable and queryable independently of any of them, so scattering hand-written value assertions through suite code both duplicates the corpus and binds it to one caller.  An expectation recorded from the implementation's own output is not an oracle: it passes by construction and cannot detect the error it was copied from.

- **Violation Example**: a literal invariant written inline in an assertion with no citation; a fixture that imports the module it is used to test; recording an expected value by running the code and pasting the result.

- **Correct Example**: a fixture entry carrying construction, \((r,a,\delta)\) and citation key, with a short parametrised driver over it; a new fact greppable in the fixtures subtree beside its citation, and a consuming test with no literal values in it.

- **Provenance**: `mem:projects/github.com__dzackgarza__research/decisions/testable-mathematical-facts-are-data-centralized-deep-fixtures-subtree-spike-independent` (user decision 2026-07-09, research#47); `mem:projects/github.com__dzackgarza__research/advice/what-a-test-cites`.

#### `DEV-42`: Prove a New Check Fires Before Trusting It to Pass

- **Rule**: Before a check, gate, scan or audit is relied on, confirm it reports a **known instance**.  A clean result from a check that has never been shown to fire is not evidence.  When a check has a target-selection step -- a file list, a glob, a scan root, an ignore file -- report how many targets it examined alongside how many findings it produced, so that "nothing wrong" is distinguishable from "nothing looked at".

- **Rationale**: The dangerous failure of a check is not a false positive, which is visible and annoying, but a silent pass, which is invisible and reassuring.  Target selection is where it happens: a scanner with a built-in ignore list that excludes the very directory being scanned reports zero findings over zero targets, and the output is indistinguishable from success.  A pattern language supplies the same failure from the other side -- an exclusion clause that is broader than intended disables its whole rule while the run still exits clean.  Both were observed while building `just test-universe`: semgrep's default ignore list excludes `tests/`, and a `pattern-not` of the form `tuple((...))` matches any single-argument call.  Each reported a clean scan.

- **Violation Example**: adding a rule and concluding from a clean run that the code is clean; reporting a finding count with no target count; tuning a pattern until the output is empty and treating that as the fix.

- **Correct Example**: running the new rule against a file known to contain the shape and seeing it reported; printing "checked N files" with the count; when a clean result arrives unexpectedly, breaking the rule down until the part that stopped matching is identified, rather than accepting it.

#### `DEV-43`: A Phase's Acceptance Must Be Sensitive to Its Repair, Not Only Its Removal

- **Rule**: When a plan pairs a destructive step with a repair -- remove an edge and restore what it carried, delete a layer and re-site its behaviour, drop a dependency and own what it provided -- the phase's executable acceptance must be able to fail while the repair is unfinished.  A criterion that measures only the removal is not acceptance for the phase, and a phase that names no criterion sensitive to the repair has none.

- **Rationale**: An implementer who has performed the removal and hit the resulting gap has two moves: do the repair, which requires deciding where the behaviour belongs, or install the cheapest local substitute that keeps the criterion green.  If the criterion cannot tell those apart, the plan rewards the substitute -- not by anyone's choice, but because that is the only thing being measured.  The observed instance: `Priority 3` named the graph-purity specimen as its only executable acceptance, and that specimen asserts what the category graph does *not* contain, so it passes identically on a graph that is pure and answering and on one that is pure and unloadable.  It stayed green through a period in which capability probes nearly doubled.

- **Violation Example**: a negative specimen (no forbidden node appears, no banned import remains, the count fell) as a phase's sole gate; declaring a migration phase complete on the strength of what is gone.

- **Correct Example**: pairing the purity specimen with one that constructs the affected objects and asks them for the operations their categories promise, so the phase cannot pass until the removed behaviour has been restored at its owner.  See `DEV-28`, which is the same requirement stated for an individual test.

#### `DEV-44`: A Catalogued Defect Gets an Owner in the Execution Order

- **Rule**: When an assessment enumerates defects and an execution order is written from it, every catalogued defect appears in that order -- as a step, as an explicitly deferred item with the reason, or as a decision that it is not a defect.  A defect that survives the assessment but not the ordering is unowned, and unowned defects grow.

- **Rationale**: Producing the assessment is the visible work and feels like the hard part, so the ordering is written from the severe rows and the rest fall out silently.  Nothing then measures the dropped ones, and every new file adds to them.  The observed instance: of seventeen defects catalogued in [the historical organization assessment](https://github.com/dzackgarza/research/blob/b5ff721fb94b030a637a527d449e628003c2b842/TODO.md#earlier-assessment), three reached no priority.  One of them was the duck-typed capability probing that grew from 52 recorded sites to 78 in a single day of work on the very subsystem the assessment had examined.

- **Violation Example**: an execution order derived only from the items marked severe; a defect whose absence from the plan is discovered by re-reading the assessment months later.

- **Correct Example**: a plan whose items and the assessment's rows are in correspondence, deferrals included, so that a reader can check the mapping in both directions.

#### `DEV-45`: A Tool's Failure Is a Fact About the Tool, Not About the Task

- **Rule**: When a tool cannot answer a question, that establishes the tool's limits.  It establishes nothing about the difficulty, size, or riskiness of the underlying work.  Before concluding that a task is hard, state the property of the *task* that makes it so, in terms that do not mention the tool.

- **Rationale**: A failed measurement is evidence, and the temptation is to promote it into evidence about the thing measured, because the failure is concrete and the alternative is thinking about the task directly.  Observed: jedi resolved 1 of 53 call sites for `tensor_valence`, and that measurement became "changing this return type touches every caller" as though the work were correspondingly large.  It does not follow.  Refactoring edits text on disk; for a duck-typed call the safety of a rewrite depends on whether the name denotes one operation, not on whether an inference engine can type the receiver -- and the real job was 21 definitions and three syntactic call-site shapes, all mechanical.  The same move in the other direction is equally wrong: a scanner that silently reported nothing became a reason to abandon syntax awareness entirely, when the failures were that scanner's alone.

- **Violation Example**: "the type checker cannot verify this, so the design is wrong"; "the language server cannot rename it, so the refactor is large"; "the linter has no rule for this, so it is not checkable"; concluding from one tool's silence that a class of tools does not apply.

- **Correct Example**: naming what actually governs the work -- here, whether a name denotes one operation, and how many definitions and call-site shapes exist -- then choosing a tool that answers *that*.  A name-based structural rewrite was the right instrument all along, and the type-inference failure was irrelevant to it.

#### `DEV-46`: A Banned Shape Is a Pattern; Tooling Must Close a Class

- **Rule**: A one-off shape that should not appear goes in the declarative pattern catalogue -- the `ast-grep` patterns behind `just test-universe` -- where it costs a line and states its own scope.  Tooling beyond roughly twenty lines must justify that size by preventing an entire **class** of semantic behaviour.  Before writing it, name the faulty mental model that produces the shape, and name the variations that model will produce which you have *not* seen.  If the tool would not report an instance nobody has written yet, it is a pattern, not a tool.

- **Rationale**: The instances in front of you are a sample of what a mental model generates, never the population.  A detector built by generalising from the sample catches the sample, and its clean run afterwards is uninformative: the model that produced those instances is still there and still generating.  Measured here: a 200-line AST checker for assertions that recover their own input, whose logic was a hand-typed list of eight accessor names, reported ten findings -- every one of them written the same afternoon by the author of the checker -- and never reported `X = [X0, X1]; assert X[0] == X0`, the canonical form of the very defect it was built for, because that shape touches no accessor.  A declarative pattern would have cost one line and been honest about covering one shape.

  The size threshold is about what the tool *decides*.  A pattern matches syntax and says so.  Code that earns two hundred lines decides something syntax cannot enumerate -- it evaluates, it folds, it resolves, it follows a definition -- and therefore reports instances in forms its author never wrote down.  A checker whose finding count equals the number of instances that prompted it has not crossed that line, whatever its length.

- **Violation Example**: a checker whose logic is a list of names harvested from the current tree; a tool whose findings are exactly the instances that motivated it; two hundred lines to catch what one `ast-grep` pattern states; concluding from such a tool's clean run that the class is closed.

- **Correct Example**: adding a row to the `ast-grep` catalogue for a shape just seen, and leaving it at that; for anything larger, first writing down the mental model and the unseen variations, then choosing an algorithm that evaluates rather than enumerates -- and confirming it reports a variation nobody has written.

#### `DEV-47`: An Oracle and Its Subject May Not Share a Source

- **Rule**: The expected value in an assertion must come from somewhere the code under test did not.  A test may not construct an object from ingredients and then assert that the object yields those ingredients back, and it may not compare two accessors that read the same stored datum.  State, for each assertion, where the expectation came from and where the actual value came from; if the answer is the same place, the assertion cannot fail.

- **Rationale**: This is the general form of both the catalogue error and the tautology it decays into under correction.  `lattice = A1 + A2 + U_2` followed by `assert lattice.indecomposable_summands()[0] is A1` asserts that `+` remembers its arguments; a transcribed Gram matrix compared to its transcribed signature asserts that one file agrees with itself.  Both pass by construction, and `DEV-41` names why that disqualifies them: an expectation taken from the implementation's own output is not an oracle and cannot detect the error it was copied from.

- **Violation Example**: `m = A + B; assert m.factors()[0] is A`; `assert L.rank() == L.module_generating_set().cardinality()` where the rank is defined as that cardinality; asserting a fixture value against the constructor the fixture was written from.

- **Correct Example**: a value from a cited source against a value the repository computed; two independent constructions of one object asserted equal; a theorem's prediction against an enumeration.



#### `DEV-48`: A Refactor Is Finished Before It Is Measured

- **Rule**: Commit to the refactor, carry it through the whole tree, and review it **by hand**.  Until the conceptual change is completely applied, do not run the suite, the gates, or any other aggregate signal, and do not treat their output as work.  An isolated syntax or type check on a file you just edited is fine, and so is a one-off script written to answer a specific question; a whole-suite run is not, because during a refactor its output is a function of how far through you are rather than of what is wrong.  The primary job is **rewriting**.  Getting the code to run again is what happens *after* the rewrite is complete, not the activity you are engaged in.  A refactor breaks things along the way, and that is the expected state, not a defect to repair as it appears.

- **Rationale**: Mid-refactor errors arrive because the change is half-applied: a call site still expects the shape you are replacing.  Fixing one therefore means writing code to reconcile the new shape with a caller that has not been converted yet -- an adapter for a state that will not exist once the refactor lands, which must itself be removed later.  Such work is not merely orthogonal to the goal; it is negative, because it entrenches the intermediate state and adds to what must be undone.

  The queue is also self-replenishing and self-directing, which is what makes the drift unbounded.  Each fix exposes the next error, so the list never empties and never hands control back.  The refactor's remaining work lives in a plan or in your head; the error list is on the screen, concrete and immediately actionable, and the screen wins every time.  Because each error is *locally* falsifiable -- real, reproducible, and verifiably fixed -- the loop supplies a continuous sense of gradient while the direction is orthogonal.  Local verifiability is not direction, and this is the standing mechanism behind `DEV-32` and `DEV-34`: a number that moves, taken for progress.

  The loop has no completion condition, only exhaustion or interruption.  So it ends with the architecture half-applied *and* a layer of adapters written for the intermediate state -- strictly worse than either the old design or the new one, and the reason a repository accumulates perpetual half-finished refactors.  Observed here: a `Hom`-to-`Mor` conversion was interrupted after the first suite run and became a day of unrelated repairs -- scalar ingress, natural-number construction, a quotient lift, relation coefficients, glue classes -- each a genuine defect that the conversion was always going to surface, none of them the conversion.

- **Violation Example**: running the suite while a rename is half-applied and working the failure list; fixing a caller that the same refactor is about to rewrite; adding a compatibility branch so an unconverted site keeps working; reporting a mid-refactor failure count as status.

- **Correct Example**: converting every site, reading the diff end to end, then running the suite once and diagnosing what remains against a settled architecture; writing a throwaway script to answer one question about an object's behaviour while the rewrite continues.

#### `DEV-49`: Architecture Is Decided by Analysis, Never by a Tool

- **Rule**: The design comes first, and it comes from reading the code and the mathematics and reasoning about them.  No checker, type error, finding count, coverage figure or failing test decides what the architecture should be.  Those instruments report on the code that exists; the question of what should exist is not one they can answer.  Metrics are consulted after the design is settled and applied, to find out whether the applied design is correct -- never to discover what it is.

- **Rationale**: An automated signal ranges over the current implementation, so any design read off it is a description of what is already there.  That is the wrong direction: a refactor exists precisely because what is already there is wrong, and the instrument cannot see the object that does not exist yet.  Deferring to it therefore converts a design decision into a repair of the present design, which is how a rewrite silently becomes maintenance.

  The failure is seductive because the instrument's output is specific and the analysis is not yet written down.  Observed here across one session: a `just test-universe` count taken as the objective and driven from 118 to 58 while the proof surface was unchanged; a detector's ten findings taken as evidence of its value when all ten were the author's own work from that afternoon; a mutation score that would have reported the motivating defect as well tested.  In each case a real number stood in for a judgement nobody had made.

- **Violation Example**: choosing a return type because it silences a type error; deciding a Hom belongs in one place because a checker complains about another; letting a failing test dictate the shape of the operation it tests; treating a finding count as the definition of done.

- **Correct Example**: reading that a rank is a cardinal because `lean-categories` gives ranks that codomain and the preamble presents cardinals, then applying that and using the type checker to find the sites; settling the design in discussion, then measuring.

#### `DEV-50`: TODOs Contain Only Unfinished Work

- **Rule**: Write each TODO from the current implementation and the desired mathematical behavior. Remove delivered work; do not retain checked boxes, completion claims, release histories, or retrospective audits in the queue. The implementation commit records the evidence and reasoning. For a partial delivery, remove only the delivered obligations and retain every required unfinished object, map, hypothesis, and generalization. A newly observed defect gets a new task describing the current source and the required repair, not a reopened historical claim.

  Read the current owner before scheduling it. A stale unchecked row does not establish missing implementation, and an old checked row does not establish correctness. Preserve already supplied constructions as inputs to the remaining work. Under deferred verification, delivery of implementation and written specimens does not discharge the separate terminal execution obligation. Keep that obligation open without retaining a history of implemented tasks.

- **Rationale**: A TODO directs the next action. Mixing it with past work makes future contributors either repeat finished constructions or inherit unsupported assumptions from status labels. Removing completed work must not remove broader requirements that one example did not satisfy.

- **Violation Example**: restoring an old release row to unchecked after discovering a new defect; leaving a completed toric algorithm as work to implement again; deleting the general non-toric requirement because its toric specialization exists.

- **Correct Example**: name the present completion constructor, the finite quotient it currently uses, and the new exact completion behavior required. Keep completed implementation history in git and pending execution in terminal T.

#### `DEV-51`: A Computational Image Is Not the Object

- **Rule**: Before substituting an engine representation or a derived object, identify the mathematical map into that representation and what information it loses. A consumer may infer a property back at the source only with the theorem that makes that inference valid under its actual hypotheses. Implement the object at its mathematical owner and expose projections, localization, scalar extension, or other comparison maps explicitly. A convenient computation cannot silently change the parent, category, or codomain promised to the user.

  Apply this to new instances, not only familiar names: a finite quotient is not a completion; a fraction field is not a prime-local ring; a finite group image is not the group; and cohomology dimensions are not cohomology modules or their induced maps. More methods on the substitute do not recover information it discarded.

- **Rationale**: The same wrong representation can produce many individually plausible downstream operations. Each new consumer then compounds one foundational error instead of extending the intended construction.

- **Violation Example**: computing in an exact quotient by a power of an ideal and advertising its arithmetic as completed-ring arithmetic; deciding a local-ring unit question after moving to the fraction field.

- **Correct Example**: construct the completion and its separate finite quotients, with source and projection maps. A polynomial image can be nonzero in the completion while its projection to one finite quotient is zero. Use the definition in [Stacks 00M9](https://stacks.math.columbia.edu/tag/00M9).

#### `DEV-52`: Exact Decisions Require Sufficient Information

- **Rule**: State what makes each implemented equality, zero, unit, membership, or isomorphism decision decidable on its represented input. Finite agreement proves agreement at that finite level; it does not prove exact equality. A detected difference may prove inequality, but exhausting a bounded search does not prove nonexistence. Keep computational precision separate from exact defining relations. When a supported exact answer cannot be obtained, use the established assertion-gated computational frontier, never a guessed boolean, fabricated witness, or silent change of output type.

  Propagate the same semantics through element arithmetic, projections, refinement, comparisons, and hashing where defined. Increasing available precision must not change an exact mathematical object or invalidate its identity in a cache. Do not infer unseen coefficients from one finite residue.

- **Rationale**: Relabeling a parent leaves its element decisions unchanged. An interface is still wrong if a low-precision zero becomes an exact zero through truthiness, membership, or inherited quotient arithmetic.

- **Violation Example**: treating a series as exactly zero because its available coefficients vanish; treating a failed search for an isometry as proof that the lattices are not isometric.

- **Correct Example**: distinguish an actual zero, an element that first differs from zero beyond the initial precision, and a genuinely nilpotent element in a ring with nilpotents. State exact equality only when the represented data or a valid decision algorithm establishes it.

#### `DEV-53`: A Correction Must Survive Other Construction Routes

- **Rule**: Translate a correction into the invariant it establishes, then follow that invariant through the affected public constructor, alternative constructors, elements, morphisms, and structural functors. Repair the common mathematical owner where the invariant belongs. Preserve both the new behavior and the already required behavior at that boundary; a fix to one route must not silently leave a second route with the same defect.

  Write separating mathematical specimens at the existing proof surface, subject to `DEV-58`. Include a nontrivial positive case and a nearby case that would expose overgeneralization. Migrate implementation consumers, not the mathematician's expectations. The protected expectation subtrees and their catalogue remain unchanged except for a justified mathematical correction recorded in its commit, as required by `AGENTS.md`.

- **Rationale**: A local spelling or constructor repair can leave the generating error intact. Another coefficient regime, direct Hom constructor, or dependent functor then recreates the violation without copying its original code.

- **Violation Example**: repairing transported local-module kernels while direct local-module Homs still use the wrong scalar ring; making only the principal completion route distinguish truncation from completion.

- **Correct Example**: preserve the local ring and its structural maps in both directly constructed and transported module morphisms, and express their compatibility through the actual comparison maps. Add the corresponding multivariable completion specimen when changing the shared completion contract.

#### `DEV-54`: Repair a Required Input Before Extending Its Consumers

- **Rule**: Before extending a dependent construction, read the particular upstream path it will consume and establish its required objects, maps, and hypotheses by source analysis. A method name, category label, completed TODO row, or upstream specification is not that input. If the required path constructs the wrong mathematical object, repair it and adapt the first dependent construction before expanding the dependent API.

  Dependencies attach to specific mathematical outputs. Do not wait for an unrelated upstream workstream to finish, and do not let one broken input freeze consumers that do not use it. A computational specialization is acceptable only when its stated regime actually supplies the required input; it is not permission for a fallback object.

- **Rationale**: Adding module completion, formal fibers, and flatness decisions on top of finite-quotient arithmetic multiplies the repair surface. Fixing the shared input first removes the cause rather than requiring a separate correction in every consumer.

- **Violation Example**: extending formal-family operations because a completion class and truncation accessors exist, without inspecting its element arithmetic; declaring all geometry blocked by a completion defect.

- **Correct Example**: establish the corrected ring completion before finite-module completion, and use the Noetherian finite-module comparison with its actual hypotheses ([Stacks 00MA](https://stacks.math.columbia.edu/tag/00MA)). Independent scheme gluing proceeds on its own established inputs.

#### `DEV-55`: Review the Complete Affected Control Flow

- **Rule**: After editing a shared source file, read the complete affected methods and enclosing class boundaries, not only added diff lines. Follow conditionals, indentation, early returns, and the paths that equip returned objects with inherited structure. Review neighboring operations whose control flow or shared helpers changed. Compare with the relevant pre-edit contract and retain its mathematical obligations.

  Write preservation specimens for exposed regressions at their existing mathematical owner. During deferred verification, perform the source review and leave those specimens explicitly unverified; do not claim that reading source proves runtime correctness.

- **Rationale**: An operation can retain its name, most of its body, and its tests while an indentation or return-path edit makes its essential construction unreachable. A diff limited to the intended new operation can miss that loss.

- **Violation Example**: adding an ideal quotient beside an algebra center and reviewing only the quotient lines, while a changed return path prevents the center from receiving algebra structure.

- **Correct Example**: read the full center and quotient methods, including all branches that produce the central submodule or subalgebra; retain specimens for the inclusion, multiplication, and the unit when required, alongside the new quotient specimen.

#### `DEV-56`: Decide the Next Construction in the TODO

- **Rule**: A substantive TODO names its current owner, the remaining mathematical delta, required input maps and hypotheses, the chosen representation boundary, and an acceptance statement that a mathematician could falsify. Name the first concrete specimen and the neighboring case that distinguishes the intended construction from its tempting substitute. Settle consequential mathematical forks before delegating the item; when source research is genuinely necessary, name the exact unresolved question and the construction it blocks.

  Preserve the full requested regime. State what an existing specialization supplies and what remains to generalize. Derive dependency order from the maps the consumer actually needs. Name the sanctioned constructor, reusable owned operations, selected upstream computation, and the actual missing integration; an unresolved backend search names the specific capability question, not a presumed mandate to implement an algorithm. Link the durable architecture contract in this document and the declaration-side contract required by `OWN-13`, so removing a delivered item does not erase its architectural decisions. Keep task details with the unfinished item; do not create a parallel readiness ledger, checklist system, or new gate to certify the prose.

- **Rationale**: A heading such as "add completion" leaves the next worker to choose between an exact object and the easiest finite approximation. Explicit mathematical decisions prevent that choice from being made implicitly inside an adapter.

- **Violation Example**: "finish local geometry" with no next object or input; "verify the new API" without a proposition; treating a toric dimension formula as completion of general geometric cohomology.

- **Correct Example**: require the image of a specific polynomial to remain nonzero in its adic completion while its projections at two stated orders differ, then require the completed module maps that consume that ring. This defines both the first repair and its downstream obligation.

#### `DEV-57`: Judge Progress by Mathematical Change Over Time

- **Rule**: Select work and assess trajectory against the user's substantive objective and the time-ordered mathematical changes. Distinguish newly supplied behavior, preserved behavior, regressions, their repairs, and dependencies that remain unresolved. Commit counts, checkbox counts, document volume, and the fraction of administrative commits do not measure that trajectory. A short repair interval does not erase productive work elsewhere; a long unobserved interval is not evidence of inactivity.

  A blocker names the exact unavailable input or authority, its owner, the affected construction, and the next action that can change it. Read the current scope and verification rules before treating a tool or hook failure as a blocker. Continue independent required work when its inputs exist. Assess a repeated failure as a recurrence of its mathematical or operational cause, not as a new spelling-specific exception.

- **Rationale**: Local activity can move a proxy while leaving the intended construction wrong. Conversely, counting administrative artifacts can hide genuine mathematical progress between them. Time-ordered evidence is needed to distinguish those cases.

- **Violation Example**: inferring stagnation from many documentation commits; inferring correctness from a shrinking TODO; stopping all work because one engine operation or an inapplicable hook is unavailable.

- **Correct Example**: identify which constructions became available during the observed interval, whether later edits preserved them, and whether dependent work consumed the repaired contract. State unobserved intervals and runtime verification gaps without converting them into conclusions about effort.

#### `DEV-58`: Observe the Current Verification Phase

- **Issue acceptance:** Once an issue's source changes and actual construction
  prerequisites are complete, the orchestrator runs that issue's original
  mathematical acceptance assertions on the integrated committed source. This
  applies during M1. Unrelated unfinished M1 work does not block those checks.
  Keep failures and their repairs with the original issue, and rerun the affected
  assertions after repair. Close the issue only when every original requirement
  has supporting evidence, as required by `DEV-61`.

- **Programme acceptance:** Broad suites, QC gates and notebook campaigns remain
  suspended until the required M1 source prerequisites in `TODO.md` are delivered.
  T begins with `core-usability-session`; `terminal-session` owns complete
  frozen-API acceptance and `extended-mathematics-session` owns required feature
  acceptance. M2 audits and API freeze, M3 full-suite acceptance and M4 capability
  growth do not restart the suspension after T begins.

- **Readiness:** Inspect the source obligations and actual dependencies, not just
  issue open/closed state. An issue awaiting execution remains open without making
  its delivered source unfinished. Before an issue's prerequisites are ready,
  write and commit constructions and falsifying assertions explicitly unverified.
  The short merged-tree import check and required tool provisioning remain allowed.

- **Evidence:** Record the checked revision, original assertions and results at
  the existing issue. A startup check, source review or compilation does not prove
  mathematical acceptance. The orchestrator owns acceptance and publication;
  workers retain their existing targeted-check and commit limits. Keep the
  protected expectations and mathematical evidence boundaries intact.

- **Hooks:** Classify hook applicability by staged paths. Prose-only commits use
  `--no-verify`; the notebook/preamble scope exemption remains binding. Issue-level
  acceptance does not authorize broad hooks before T or changes to shared QC
  configuration.

#### `DEV-59`: Record Observed Foundational Gaps and Papercuts

- **Rule**: The [native issue tree](https://github.com/dzackgarza/research/issues/46)
  owns observed problems, including missing foundational
  mathematics and missing structural relationships, and also actual papercuts
  in research use or contribution workflows. Record a finding when it arises
  during mathematical tracing, source reading, implementation, review, notebook
  use, or permitted execution. Discovery is not restricted to the selected TODO
  item. Capture before leaving the relevant work, not at a future audit.

  For a foundational complaint, begin with the desired mathematics in standard
  terminology. State the input/output objects and maps, hypotheses, and the
  recursive dependency path exposing the gap. Identify the earliest missing
  general construction or relationship, with the mathematical sources that
  justify it. Include a small ideal-API mathematical expression or specimen
  where useful, explicitly distinguishing illustrative pseudocode from an
  existing callable API. Do not title the complaint after a proposed manager,
  registry, helper, adapter, or feature-specific programming class.

  Then give the observed evidence: inspected source and symbols or the actual
  workflow and output, the existing partial construction, the precise unmet
  contract, affected consumers, confidence, and uninspected scope. Distinguish
  source evidence from executed failures. For an absence claim, use the
  epistemic-integrity fields Searched, Found, Conclusion, Confidence, and Gaps;
  a failed name search alone does not establish absent mathematics. An unresolved
  availability question may be recorded as such, but not as a confirmed defect.
  Name relevant maintained implementations and the exact capability question
  where known; their presence is not permission to leak foreign objects.

  A papercut entry names the real user action, expected behavior, actual friction,
  owning boundary, and observed example. Record it even when it is small. Do not
  invent a defect from a possible future inconvenience, and do not inflate a
  local ergonomic issue into a missing theory without a mathematical trace.

  Search the native issue tree before filing.
  Extend the existing mathematical issue when a new consumer exposes
  the same missing foundation; retain genuinely different hypotheses or gaps.
  One general complaint can link several consumers. Its title and links should
  remain useful when those consumers move between files.

  Before admitting or migrating a work unit, reconcile its proposed decision
  with current `AGENTS.md`, this policy index, `lean-categories`, and later
  owner rulings. Apply `DEV-69` to its cited violation and source evidence.
  A protected expectation that uses an older spelling is evidence to reconcile,
  not a second authority that automatically creates an owner choice. If the
  authority already fixes the result, write the remaining source delta and
  acceptance directly. First check whether a test-side `conftest.py` can
  translate the spelling to the owned operation without changing the
  expectation or adding a public alias; the existing category abbreviations
  are an example. Account for a name exported by the session, which takes
  precedence over a builtin bridge. A bridge must still exercise the owned
  operation and preserve the mathematical assertion. If a genuine choice
  remains, name the incompatible governing prescriptions or the exact
  `ENG-06` scope choice and keep the evidence-gathering task distinct from
  implementation acceptance. Migration
  preserves complaint evidence but does not ratify its old decision status.

  **Division of responsibility:** `lean-categories` owns the mathematics, and a
  missing piece of it is a formalization request there; CONTRIBUTING and the
  preamble's declarations specify the enduring engineering design. The research
  issue owns the unmet need, evidence, remaining requirements, acceptance, and
  links to upstream requests. Use itree to navigate and select the work.
  Native sub-issues under #46 give the work order; native blocked-by relations
  record actual prerequisites. Rank by correctness, reusable capability, and
  reduction of later work, before optimizations, cleanups, or style work.
  Attach each new complaint to its owning native parent, assign the delivery
  milestone, and state concrete acceptance criteria in the issue body. Place
  its open prerequisites before it and add blocked-by relations only for actual
  prerequisites. Use `itree next dzackgarza/research` for selection and
  `itree doctor dzackgarza/research --strict` to check the tree after changes.
  Use the existing remediation issue when it already owns the complaint. If the current
  task requires the fix, update that issue with the actual remaining delta and
  continue it. An independent finding can remain recorded without starting a new
  workstream. External issues own upstream repair; link them from the local
  research issue without copying their live status or surrendering the preamble's
  obligation to present the result. Filing or recording a complaint never
  completes its repair.

  **Maintenance:** follow `DEV-61` for issue changes. Reread
  before editing and preserve other changes. Keep the full complaint evidence
  in the owning issue body or a linked comment. On delivery, compare the fix
  with the full mathematical requirement and its affected paths, record the
  resolution evidence, and close the issue only when its obligations are discharged.
  Partial delivery updates the remaining requirements and leaves the issue open.
  Preserve evidence comments after closure and use the issue's native state.
  Preserve enduring engineering decisions at their declaration.
  Source-based remediation does not certify runtime
  behavior; required execution remains in terminal T under `DEV-58`. An observed
  runtime failure is not resolved merely because a speculative source fix exists.

- **Rationale**: A leaf-level workaround can hide a reusable mathematical
  prerequisite from every later contributor. Recording the underlying theory
  makes that prerequisite visible without confusing discovery with implementation
  or turning an isolated symptom into another bespoke subsystem.
- **Violation Example**: discover that a specialization bypasses localization,
  add another fraction constructor, and mention the missing relationship only
  in chat; record "needs a backend manager" instead of the missing morphism.
- **Correct Example**: record the missing localization factorization with its
  submonoid and universal map, link the `lean-categories` request if it is not
  formalized there and the existing repair item, and complete the shared
  presentation with its consumer once the formalization exists. Remove the complaint only when that
  requirement is delivered, retaining any still-unverified execution obligation.

#### `DEV-60`: Close One Front at a Time in Dependency Order

- **Rule**: Work exactly one `TODO.md` node at a time, in the DAG's dependency
  order, and drive it to its stated acceptance before opening any other front.
  Shared-substrate (preamble) edits are in scope only when the current node's
  contract requires them. If multiple fronts are already open, close the
  nearest-to-acceptance front before any new authoring. During the refactor,
  commits use `--no-verify` per `DEV-58`; address real defects observed in the
  work itself as they arise, but do not run hooks, test suites, or type-check
  gates mid-refactor, and do not spend effort making files pass checks while
  the architecture around them is incomplete.

- **Rationale**: Parallel half-open fronts multiply integration debt, hide
  which mathematical contract is actually blocked, and leave abandoned
  mid-flight work that no later contributor can distinguish from delivered
  construction. One closed node is progress; several open ones are risk.

- **Violation Example**: open a second construction because the first grew
  difficult, touch shared preamble modules for a node that never named them,
  and leave a large refactor uncommitted and unowned across many files while
  starting new authoring elsewhere.

- **Correct Example**: select the next unblocked `TODO.md` node, complete and
  commit it with the queue reconciliation, and then select the
  following node; when a prior front is already open, finish the one closest
  to acceptance first.

#### `DEV-61`: Reconcile the Single-Worker Queue with Delivery

- **Rule:** The current repository workflow has one worker and no claim ledger.
  Select a ready issue from the native tree, reread its owners and acceptance,
  and deliver its remaining delta. Reconcile its requirements, complaint evidence,
  and native dependencies with the implementation commit. Selection, claiming
  and release do not merit separate commits.
  Before changing an issue or work-selection guidance, reread the live record and preserve edits
  not made in the current task. A clean `HEAD` is the target's checkpoint;
  conflicting uncommitted work must be resolved with its owner.

  A coordination mutex is required only if concurrent work is explicitly
  introduced with an agreed shared-checkout protocol. Do not invent a lock or
  reservation system for this single-worker queue. Existing foreign reservations
  or changes are preserved until their ownership is resolved.
- **Rationale:** A queue selects mathematical work. In a single-worker stream,
  a claim ledger adds a competing state transition without protecting a handoff.
- **Violation Example:** commit a claim, perform no construction, then commit its
  release; reject authorized work because a removed claim ledger has no entry.
- **Correct Example:** deliver a constructor and its falsifying specimens,
  discharge only the issue obligations supported by that commit, and leave
  execution evidence owed under terminal T.

  **Acceptance before reselection:** after a source unit is delivered, the
  orchestrator compares every requirement with the committed owners, callers
  and falsifying specimens. Record the verdict on the existing issue before
  selecting another unit. A remaining source defect stays with that issue.
  Close an issue only when its original acceptance requirements are satisfied.
  An issue that requires runtime behavior stays open while those assertions are
  unexecuted. A link from terminal acceptance preserves programme coverage;
  it does not transfer the issue's obligations or justify closing it.

  Distinguish delivered source from accepted issues. When a phase rule prevents
  the required acceptance, identify that rule and resolve the execution decision
  before claiming restored delivery. The orchestrator reviews
  delivered work while the sole implementation worker continues its current
  coherent unit; worker activity does not discharge this review.

#### `DEV-62`: An Empirical Claim About an Engine Has Its Measurement or Is Written as a Hypothesis

- **Rule**: A statement about what Sage or another engine does, costs, supports, or demands of its input is one of two things.  Either it is a finding, and it travels with the probe that produced it: the command, the specimen and its size parameter, the version, and the result.  Or it is a hypothesis, and it is written in words that cannot be read as a finding ("untested: `longest_path` may be the cost").  A causal sentence in the grammatical register of a finding, with no measurement behind it, is fabrication.  It is banned in code comments, docstrings, commit bodies, sage-extensions `TRAPS.md`, issues, reports, and conversation alike.  This extends the always-on performance-claims rule (wall time as a function of size, never counts) from how a cost is reported to whether the sentence may be written at all.

- **Rationale**: Such a sentence does four things.  It terminates the search: a named cause closes the question, and the story then stands between the reader and the measurement.  It borrows authority from plausibility: reciting a mechanism that would explain the observation feels, from the inside, identical to having found it, and the reader cannot tell the difference.  It counterfeits the project's currency: the product here is empirical knowledge of Sage (`ENG-07`), so an unmeasured engine claim is forged coin in the one denomination that matters, and it is trusted permanently because nobody re-derives a recorded fact.  And it is lazy in the literal sense: the measurement usually costs a second.  A false row in sage-extensions `TRAPS.md` is more expensive than an empty file for exactly the reason a true row is valuable.

- **Observed**: 2026-09-16, the same tool as `ENG-07`.  Two causes were asserted in the register of findings: that a Sage path method is MILP-backed and its cycle enumeration explodes, "those are the cost"; then that Sage's interpreter startup was the cost.  Neither had been timed.  When timing happened, the interpreter started in a fraction of a second (sage-extensions `TRAPS.md` holds the current numbers), and the slow call was in the library that had just been swapped in to avoid the Sage one.  Both claims pointed away from the truth, and either, recorded, would have steered every later reader off a Sage route that was never measured.

- **Violation Example**: "it is slow because it is MILP-backed"; "Sage's startup dominates"; "the native method cannot take this input" with no reproduction; a sage-extensions `TRAPS.md` row with no command; a docstring that explains a workaround by a property of the engine nobody checked.

- **Correct Example**: the interpreter-startup row in sage-extensions `TRAPS.md`: what was timed, three runs each, the version, the command; or the sentence "I have not measured this", followed by the measurement.

#### `DEV-63`: Measured Engine Facts Have One Durable Owner

- **Rule**: [TRAPS.md](https://github.com/dzackgarza/sage-extensions/blob/main/TRAPS.md) in sage-extensions is the ledger of measured facts about the engines this repository delegates to: a route's cost as a curve, an input it rejects, an output convention, a default that is wrong or slow, and the alternate spelling that answers.  Write the row in the same turn as the measurement, before the tool or construction that exposed it moves on.  A row records the operation, the Sage spelling measured, the specimen and its size parameter, the wall times, the version, the command that reproduces it, the route chosen, and the site that depends on it.  The owning issue keeps the unmet need and resolution evidence under `DEV-59`; sage-extensions `TRAPS.md` keeps the fact, which delivery uses and never resolves.  The owned name's docstring cites the row; it does not restate it.

- **Rationale**: The fact is the product (`ENG-07`) and it has no other home.  A commit body is found only by someone who already suspects the commit; a conversation is gone; a docstring at one site is invisible to the next site that meets the same engine.  One ledger, read before any engine route is chosen, is what turns one measurement into every later rediscovery avoided.

- **Violation Example**: a measurement quoted in a reply and nowhere else; a workaround committed with the engine fact only in the commit body; a cost recorded only as an issue and deleted when the consumer was delivered, taking the fact with it.

- **Correct Example**: the interpreter-startup row in sage-extensions `TRAPS.md`: what was timed, three runs, the version, the command, and the consequence for per-invocation tooling.

#### `DEV-64`: A Sage Mechanism Is Read in Its Source Before It Is Worked Around

- **Rule**: Before overriding, wrapping, or routing around any behaviour of Sage's category framework (`super_categories`, `extra_super_categories`, `_with_axiom`, joins, C3 ordering, `__contains__`, `refine`, dynamic classes), open the method in `sage/categories/` and state its contract in one sentence, with the file.  The workaround is then written against that contract or not at all, and the contract goes to sage-extensions `TRAPS.md` if it is a fact nobody in the tree had written down.

- **Rationale**: the mechanism has a design and the design is usually the answer.  The tree's history shows the alternative: `super_categories` overridden on every axiom class to stop an inheritance that one deleted edge stops; `refine` and `setattr` as construction; `NotImplementedError` as an abstract contract; `__contains__` as a predicate.  Each was a workaround for a mechanism whose actual behaviour, ten lines of source away, made it unnecessary or wrong.

- **Violation Example**: writing `def super_categories(self): return [Schemes(self.base_ring())]` on nine axiom classes to block axiom descent along a base-restriction edge, instead of reading why the descent happens and removing the edge.

- **Correct Example**: reading `CategoryWithAxiom.super_categories` (category_with_axiom.py) and `Category._with_axiom_as_tuple` (category.py), recording that an axiom is applied along every declared supercategory, and ruling that base-restriction edges are functors (AGENTS.md, *Red flags*; sage-extensions `TRAPS.md`).

#### `DEV-65`: An Obstruction Met While Changing a Declaration Is a Finding, Never a Mechanism

- **Rule**: When a declaration change meets an obstruction (a construction that cannot proceed, an object that must be in a category that does not yet exist when it is built, a Sage behaviour that a plain declaration triggers), the change stops there and the obstruction becomes a node in `TODO.md` with its dependency path, or a question to the owner.  It is never resolved by a runtime mechanism: not `refine` after construction, not a declaration that reads an engine object, not a `super_categories` override on an axiom class, not a membership predicate, not a placeholder supercategory.  The same rule binds an agent working one subtree under a brief: the report names the obstruction with the file and line, and the brief's owner decides.

- **Rationale**: every one of those mechanisms was tried on 2026-09-16 by an agent that had the policy in front of it, because from inside a subtree the mechanism is the shortest path to a passing view: nine `super_categories` overrides to block axiom descent that one deleted edge stops; the integers refined into `OwnedOrders` after construction, with a declaration reading an engine view of ZZ to avoid re-entry; a base-free category pointed two levels up for want of the node it needed.  Each would have been invisible to the next reader and each restated at the leaf a fact that belongs to the owner.  The obstruction is the information; the mechanism destroys it.

- **Violation Example**: `def super_categories(self): return [Schemes(self.base_ring())]` on every scheme axiom; `_owned_integers` refining ZZ into a category whose declaration needs ZZ; `RepresentedToricSchemes -> LocallyRingedSpaces` because no base-free scheme category exists.

- **Correct Example**: the schemes agent's report naming the axiom-descent mechanism with its source line, which became a ruling in `AGENTS.md`, a row in sage-extensions `TRAPS.md`, and the removal of every base-restriction edge; a placement left abstract with its missing construction recorded in the native issue tree and scheduled by native dependencies.

#### `DEV-66`: Keep Bulk Scratch Repository-Local

- **Rule**: Repository work does not create full-tree reproductions, worktrees,
  virtual environments, build trees, or bulk caches under global `/tmp` or
  `~/.cache`. Use the ignored repository `.tmp/` surface for genuinely
  necessary scratch and prefer a minimal specimen to a repository copy. Redirect
  tools whose default temp/cache roots are host-global before executing them.

- **Rationale**: External scratch outlives the worker that created it and makes
  unrelated repositories pay the disk cost. Multiple 270 MB reproduction trees
  accumulated under `/tmp` on a nearly full host even though the active
  mathematical unit did not need duplicate repositories.

- **Violation Example**: create `/tmp/research-owner-iso-tests` as a full
  checkout just to obtain a clean test surface; leave a package/build cache under
  `~/.cache` because the tool chose that default.

- **Correct Example**: reproduce the failure with the smallest specimen in
  `.tmp/repro-name/`, point `TMPDIR` or the tool cache there, and delete that
  disposable state when the unit is done.


* * *

#### `DEV-67`: Closure Preserves the Entire Mathematical Burden

- **Rule:** A source node closes only after its complete stated family has been
  inspected, the required construction and affected consumers are delivered,
  and distinguishing mathematical specimens are committed. The commit names
  the owner, entry routes, coefficient/hypothesis regimes and unexecuted proof.
  Before T this is source delivery, not a claim that the specimens pass.

  Derive that family from the original requirement and source declarations,
  constructors, overrides, exports and consuming calls before comparing the
  delivered routes. Search hits and the changed-file list do not define it.
  Match each requirement clause to the route and regime that discharge it;
  distinguish definition, representation and effective computation. A few
  positive and negative specimens separate particular wrong constructions but
  do not prove an "every" claim. Record coverage in the delivery commit, with
  concrete residue in the existing open row rather than a new compliance ledger.

  The producer and the consumers of its changed contract close together.
  Admission, private access, placement, inherited operations and ownership
  defects on that route block its delivery even when a later sweep has the
  same topic. Those sweeps own only independently untouched residue. A later
  consumer must preserve the producer's established contract and its separating
  specimens. If a counterexample defeats a shared repair, reopen the affected
  obligation and inspect the other uses of that repair method before proceeding;
  do not reopen unrelated work or patch only the reported spelling.

  Required residue stays in the DAG with its full objects, maps and hypotheses.
  An aggregate cannot close while any required descendant remains open. A split
  transfers every obligation and redirects the affected edges before delivery;
  recording a new child is not satisfying it. At T, execute the banked specimens
  against the repaired source, including inherited operations and alternative
  construction routes. A previous green run cannot certify a later revision.

  For a finite audit, fix its source population and obligations at entry, cover
  them once, then review each repair and its affected uses. Completed coverage
  remains valid for unchanged, unaffected routes. New relevant findings remain
  required repairs; neither a repair nor a newly consulted skill restarts the
  whole-repository pass or adds an unrelated audit lens. Close when the stated
  coverage is complete, its findings are repaired, and affected proof has been
  re-established under the current verification phase. Repeated rediscovery of
  the same cause requires a repair at its shared owner, not another broad scan.
- **Violation Example:** close category membership after changing only schemes
  while functor/arrow categories retain the same predicate; close provenance
  after renaming fields; close an aggregate because its repairs have new names.
- **Correct Example:** review every affected membership owner, preserve genuine
  element-of-set predicates, construct category placement at admission, and
  bank both a placed object and a similarly represented wrongly placed object.
  Retain the runtime obligation until terminal execution distinguishes them.

#### `DEV-68`: Repair the Semantic Operation, Not Its Search Signature

- **Rule:** A search result is an inspection boundary, not an acceptance test.
  Follow each implicated operation through helpers, inherited methods, adapters
  and its next consumer. A repair changes the authority, data flow or
  mathematical behavior that caused the defect. Moving code, renaming a field,
  replacing `try` with `match`, deleting an API, or adding a category label is
  insufficient unless that semantic obligation is discharged.

  Preserve supported mathematics and engine realizations. A removed operation's
  required behavior must have a usable owner and migrated consumers. A genuine
  abstract declaration is not implementation of a concrete promised operation.
  Retain specialization algorithms when their theorem supplies genuinely stronger
  computation; reuse the highest suitable maintained operation for standard
  algorithms (`OWN-08`, `ENG-06`). Policy does not ban iteration needed to adapt
  representations, nor does one low-level engine call constitute delegation of
  an algorithm still implemented locally.
- **Correct Example:** replace local kernel orchestration with the maintained
  kernel/presentation operation and recover its inclusion and factorization;
  an owned free module of the right rank is not a kernel over a ring with torsion.
  Replace a placement probe by correct construction, and demonstrate that the
  inherited operation works on that object rather than just disappearing from
  the search results.

#### `DEV-69`: A Node Is Admitted Only on a Cited Violation

- **Rule:** A TODO node that changes existing code is admitted only when its
  entry states three things:
  1. **The violated statement.** Cite the rule code in this document or a
     section of `AGENTS.md`, or the `lean-categories` definition or theorem,
     that the current code contradicts. Quote the clause.
  2. **The evidence.** Give the specimen, the call and the observed result
     that show the contradiction.
  3. **The policy search.** Name the rules that were searched for an answer
     that supports the current code, and say why none of them applies.

  A node that changes a public operation (its name, its result type, its
  owner or its signature) also states why the current operation is not
  mathematically correct. A different spelling that is equally correct is
  no reason.

  These are not admission reasons:
  - **A failing test alone.** First derive the type of the operation's
    result (object or morphism, and which morphism), independently of the
    test and of the code. If the test asks a question of the wrong type,
    the test is the finding. An expectation file is protected from edits
    that match an implementation. It does not give a failing line the
    authority to redesign a correct API.
  - **A preference.** "Should return a form", "a cleaner spelling" and "the
    usual name" do not show a contradiction.
  - **"Owner ruling owed"** on a question that `CONTRIBUTING.md`, `AGENTS.md`
    or `lean-categories` already decides. Search them first. A ruling is owed
    only when the search finds two rules in conflict or finds nothing, and the
    entry names what was searched.
- **Rationale:** A node is an instruction to a worker who trusts it. A node
  with no cited violation sends that worker to change correct code, and the
  cost lands on the owner, who must find and revert it.
- **Violation Example:** On 2026-10-07 `test_forms_construct.sage:208` called
  `.cardinality()` on `form.normal_form()`. The orchestrator filed a node to
  make `normal_form()` return a form. A normal form is a different module with
  a different form in its own coordinates. The isometry to it is the correct
  result, and the normal form is its codomain. The same day, a topology node
  required "one underlying set S, with no conversion". The chosen-enrichment
  rule (`CON-16`, `OWN-15`) already decides the opposite: a space `(S, tau)`
  is its own object.
- **Correct Example:** The node quotes `CON-07` ("a computed predicate ...
  never places") and shows that `from_module` refines the form into a
  subcategory on a computed answer. Its specimen is `A_1` built from
  relations, and it notes that `OWN-22` and `CAT-17` were searched and do not
  sanction the refinement.

### 13. Notebook, REPL & Mathematical Example Style (`NB-*`)

#### `NB-01`: Every Mathematical Claim in an Executable Example Is Executable

- **Rule**: In research notebooks, demos, doctests, and executable documentation, state checkable mathematical claims as assertions or computations that display the witness.  Do not leave “should be”, “correctly”, expected orders, equalities, or classifications only in comments/prose beside unverified code.

- **Rationale**: A notebook is part of the research instrument.  A prose claim beside code can remain true-looking after the implementation changes underneath it; an executable proposition fails at the point of drift.

- **Violation Example**: `# this reflection sends v to -v`; `print("correctly distinguished the genera")`; a markdown sentence claiming an automorphism has order five without checking it.

- **Correct Example**: `assert sigma(v) == -v`; compute and display the actual genus/isometry witness; assert the element order or cited invariant through the semantic API.

#### `NB-02`: Examples Use Specimens That Can Falsify the Claimed Feature

- **Rule**: Choose examples for which the feature under demonstration has nontrivial work to do.  Avoid identities, an object compared with itself, zero maps, or degenerate fixtures when those make the claimed property tautological.

- **Rationale**: A demonstration is useful in proportion to how surprising its passage would be if the implementation were broken.  Equality implies isomorphism/isometry, identity maps satisfy many laws automatically, and zero maps make many factorization tests vacuous.

- **Violation Example**: Demonstrate `is_isometric` using `L.is_isometric(L)`; demonstrate morphism behavior only with the identity; “test” uniqueness of a factorization by constructing the same route twice.

- **Correct Example**: Use two distinct presentations known to be isometric, a nontrivial reflection/projection, or two independently constructed candidate factorizations.  Prefer small specimens whose mathematical answer is independently sourced and transparent.

#### `NB-03`: A Notebook Section Answers a Mathematical Question, Not “Shows an API”

- **Rule**: Organize research examples around mathematical questions and conclusions.  Methods are means, not the subject of the section.  End with the mathematical object, invariant, classification, enumeration, witness, or conclusion the researcher wanted.

- **Rationale**: The preamble is an interactive mathematical language.  API-tour examples encourage users to think in method inventories and implementation boundaries rather than in the mathematical workflow the API exists to support.

- **Violation Example**: A section titled “Using `roots()`” that prints one returned object; “Testing the genus API” that merely shows a method exists.

- **Correct Example**: “What is the root system of this lattice?”, “Are these two lattices in the same genus?”, or “Enumerate the overlattices and their discriminant forms”, with the section computing the complete requested mathematical answer.

#### `NB-04`: Session Examples Use Sage/Preamble Host-Language Idioms

- **Rule**: In notebook/REPL-facing examples, use the concise Sage/preamble language already available instead of manually spelling its lower-level constructors.  This rule is scoped to preparsed/session code; ordinary `.py` implementation modules must not assume Sage preparser semantics.

- **Rationale**: The session language is part of the product.  Reimplementing it in examples teaches users to bypass the concise mathematical syntax and makes the documented workflow look lower-level than actual research use.

- **Violation Example**: In a Sage notebook, spell a rational as `QQ(1)/2`; construct an identity morphism from an identity matrix when the object exposes its identity; access named generators only through positional engine APIs.

- **Correct Example**: Use preparsed exact literals where active, named-generator syntax where supported, semantic identity maps, direct-sum notation, and the public preamble methods discoverable from the objects in hand.

#### `NB-05`: Show Mathematical Witnesses, Not Self-Affirming Status Text

- **Rule**: Output in examples displays mathematical data/witnesses or concise conclusions derived from them.  Do not print prose declaring that the preceding computation was correct, successful, or properly distinguished.

- **Rationale**: Self-affirming output contains no independently inspectable evidence and survives even if the computation above changes.  Showing the actual isomorphism, kernel, factorization, class, invariant, or boolean mathematical predicate lets the reader inspect what happened.

- **Violation Example**: `print("correctly found the primitive embedding")`.

- **Correct Example**: display the embedding and its cokernel/torsion-freeness, or assert the relevant predicate and print the resulting mathematical object when useful.



### 14. Formalization Requests and Search (`FSA-*`)

Moved to [sage-extensions `CONTRIBUTING.md`](https://github.com/dzackgarza/sage-extensions/blob/main/CONTRIBUTING.md): this section governs the library code, which lives there.

## Writing house conventions

Mathematical prose in this repository (the book under `writing/`, papers,
talks, docstrings, issue bodies, and plan cards) follows the
[mathematical writing policy](https://github.com/dzackgarza/ai/blob/main/opencode/skills/mathematics/writing/policy/policy.md).
Cite its codes (`PR-30`, `DEF-26`, `SYM-1`, …) in commits and review. This
section fixes the mechanisms that the policy leaves to the house.

### The book

The book is the Quarto site in `writing/.book`, which links in
`category-theory`, `coble`, `data`, and `index.md`. Everything else under
`writing/` (the dissertation, the research statement, the talks, the exams)
builds through `~/.pandoc`. The theorem syntax is the same in both, so a block
moves between the book and a paper unchanged. The book's own mechanics (the
flat chapter links, the two renders, the declared block classes) stop at what
`writing/.book` links in.

`writing/.book/_quarto.yml` lists the chapters, and that list is the book's
reading order (`SEC-9`). A page that is not listed does not render. After
adding pages, check both directions: every listed chapter has a file, and
every prose file is listed or deliberately unlisted. A page's frontmatter
often settles its part: `unit:` separates a reusable `method` from the
`computation` it produced and from a `research-program`, and
`status: conjectural` marks what is not proved. The Computations part and the
open-problems part are grouped on these fields.

Each page has one level-1 heading; later headings are `##` sections. Do not
number headings by hand: sections number automatically.

The book builds from the repository root:

```bash
just docs-preview                # serve the site locally with live reload
just docs-lint coble/<page>.md   # render one page
just docs-check                  # render, then fail on any citation, cross-ref, or link defect
```

### The Coble part

`writing/coble` holds the Coble surfaces work, one topic per page. The
mathematics that is written up sits beside the computations and the open
questions that produced it; there is no separate paper tree or notes tree.

```text
<topic>/              One directory per topic, kebab-case, one page per file
index.md              The part landing page
papers/               Extracted third-party sources, one directory per citation key
reference/            Source PDFs and the last built version of the paper
scripts/              The computational toolchain
tables/               Generated lattice and diagram tables
heegner-report/       A standalone research report and its own bibliography
coble_supplement.bib  Project-local entries not yet in the global bibliography
```

There is no PDF build for this work; the last dated PDF build is in
`reference/`.

`papers/<KEY>/` holds a read-only source archive of a third-party paper: its
LaTeX, its figures, and where available a readable extraction. The extraction
pipeline resolves `\cite{}` to `?` and `\ref{}` to `[0]`, so read an
extraction for its mathematics and take citations and numbering from the PDF.
Do not commit LaTeX build intermediates beside an extraction.

### The dissertation

`writing/dissertation` is the Markdown source of *Compact Moduli of
Numerically Polarized Degree Two Enriques Surfaces* (D. Zack Garza, University
of Georgia, 2025), and its build.

- `main.md` holds the front matter (title page, committee, abstract, index
  words) and the ordered `include` list of section files.
- `sections/` has one directory per part, one per chapter, and numbered files
  per section. `#` is a part, `##` a chapter, `###` a section.
  Theorem-like environments are fenced divs (`:::{.theorem title="..."}`);
  cross-references use typed Pandoc-crossref ids and `@...` references;
  citations use Better BibTeX keys (`@key`, `[@key]`). The full conventions
  are `~/.pandoc/AUTHORING_STYLE.md`.
- `figures` is a symlink to `~/.pandoc/figures`, the single owner of every
  figure and its editable source.
- `submitted-2025-08-12.pdf` is the dissertation as submitted to the UGA
  Graduate School, 227 pages, built from the LaTeX that this Markdown
  superseded. It is a record, not a build target; `just compile` does not
  produce it and does not match it page for page.

```bash
just compile          # dissertation-<date>.pdf via ~/.pandoc (pandoc -> latexmk)
just preview FILE     # live preview of one section
just format-md        # normalize markdown
```

Everything the build needs lives in `~/.pandoc`: the page template
`templates/uga-dissertation.tex`, the macro package
`styles/dzg-dissertation.sty` (shared tiers plus
`styles/macros/dissertation-overrides.tex`), the TikZ sources under
`figures/tikz/dissertation/`, and the bibliography `bib/references.bib`, which
is the live Zotero export. A citation key that does not resolve there is fixed
in Zotero, never in a local bib file.

### Numbered blocks (`DEF-4`)

A numbered block is a fenced div whose class is the full lowercase
environment name and whose id is a family prefix, a colon, and a key:

```markdown
::: {.theorem #thm:coble-cusps title="Cusps of the Coble moduli space"}
...
:::
```

The family prefixes are `ass clm conj cons conv cor def ex exr lem not obs
prob prop qst rmk thm warn`. Their registry is `THEOREM_FAMILY_METADATA` in
the zettlr-pandoc fork; the amsenv filter
(`~/.pandoc/filters/convert_amsthm_envs.lua`) and
`writing/.book/_extensions/local/amsthm-refs` mirror it. The colon keeps these
ids apart from Quarto's reserved hyphen prefixes (`def-`, `thm-`, `fig-`,
`sec-`, …), which Quarto takes for its own cross-references. The declared
block classes are listed at the bottom of `writing/.book/_quarto.yml`; add a
class there before using it.

### References (`XREF-1`, `XREF-4`, `XREF-5`)

- Reference a block as `@thm:coble-cusps` ("Theorem 2.9") or
  `[-@thm:coble-cusps]` ("2.9"). A bracketed cluster keeps its text:
  `[see @thm:a, (ii); @lem:b]`. A use of a defined term links its block,
  `@def:key`.
- The `amsthm-refs` filter rewrites each theorem-family citation into the
  `\ref` and `\longref` commands that `custom-numbered-blocks` resolves
  (`writing/.book/_extensions/dzackgarza/custom-numbered-blocks/cnb-3-crossref.lua`).
  A cluster that holds any other key goes to citeproc unchanged.
- A reference to an id that no block declares renders as nothing, and the
  sentence around it is left dangling. Raw LaTeX such as `\cref{x}`
  disappears the same way. `just docs-check` scans the sources for both,
  because the rendered HTML has nothing to find.
- A reference reaches any numbered block in the book, in any chapter, in
  either direction. The forked resolver keeps one registry for the whole
  book, and the gate renders twice, which lets a reference reach a later
  block. `writing/.book/TRAPS.md` records what breaks without either. Ids are
  therefore unique across the whole book.
- A section is anchored `{#sec-x}` and referenced `@sec-x`, or linked as
  `[text](#sec-x)`. Quarto finds the page that holds the id, so a link does
  not change when either page moves. A link to a page links the id of its
  `#` heading. A link by path, `[text](../dir/Page.md)`, fails
  `just docs-check`. A table carries no number; link to the section that
  holds it.
- A numbered block is referenced `@thm:key`, never linked as
  `[text](#thm:key)`. Quarto finds the page only for a heading id, so a
  link to a block in another chapter is a dead anchor. Write
  `the gluing theorem (@thm:key)`; `just docs-check` fails the link form.
- A figure is anchored `{#fig-x}`, with a hyphen, and referenced `@fig-x`;
  Quarto numbers it within its chapter. The image lives in the shared
  pandoc-config repository and `scripts/docs_figures.py` stages it into the
  book. A reference to a figure that is not there fails the build.

### Citations (`CITE-*`)

- Zotero is the source of truth. The global bibliography is exported to
  `~/.pandoc/bib/references.bib` and copied into `writing/.book/references.bib`
  by the build. Cite with a Better BibTeX key: `[@OR23, Definition 1.5.1]`.
  Add a missing work to Zotero first, by DOI or arXiv identifier, through the
  `zotero` skill.
- `writing/coble/coble_supplement.bib` holds only entries with no global
  counterpart yet; the work still belongs in Zotero.
- The docs gate rejects an inline URL to arXiv, a DOI, or nLab (`CITE-2`).
- Cite the Stacks Project as `[@stacks-02LS]` (`CITE-3`). The `stacks-tags`
  filter rewrites the key to the one global Stacks entry and appends a linked
  `[Tag 02LS]`.

### Source-grounded mathematics and original work

Before inserting a mathematical definition, hypothesis, criterion, theorem,
or identification into a research artifact, establish its source and its
place in the requested task. Read the cited passage and check the objects,
hypotheses, and conclusion against the proposed statement. Cite the exact
location. For a derivation of a requested claim, identify the cited premises
and supply the derivation.

If the required result has not been verified, keep the research question
open. Do not replace it with an agent-devised condition, conjecture, or
different theorem. A request to explain, compare, or document existing
theory does not authorize original mathematical development. Neither an
agent-written proof nor a label such as “sufficient condition” supplies
that authorization.

Original mathematical development requires an explicit request from the
user. Attribute it as original work and distinguish proved results from
conjectures. Before committing source-based exposition, check each added
statement for a verified source or a derivation of a requested claim;
remove additions that satisfy neither condition. Record unresolved source
questions under the house rule for open problems.

### House parameters

- **Definiendum (`DEF-26`, `PR-10`).** The term being defined is in *italics*
  at its defining occurrence and nowhere else.
- **Audience (`PR-18`).** The book's reader is the audience of `DEF-12` and
  `DEF-13`: comfortable with $\infty$-categories, $\mathbb{E}_1$- and
  $\mathbb{E}_\infty$-ring spectra, $\mathbf{LMod}_R$ versus
  $\mathbf{RMod}_R$, derived stacks, and homotopy types.
- **Ontology.** The book adopts the derived and homotopical ontology of
  `DEF-8` to `DEF-14`.
- **Proof obligation (`SEC-6`, `EX-2`).** Every claim in a statement block
  is proved in the book, and every lemma a proof uses is proved earlier.
- **One notion per block (`DEF-15`).** A definition block defines one
  notion. An enumerated family of notions gets one block per notion.
- **Pullbacks (`MA-8`, `DIA-*`).** A pullback is drawn in place as a
  `tikzcd` square with both legs and the corner mark before fiber-product
  notation names its apex.
- **Adjunctions (`DIA-4`).** The shared `\adj` macro gives the one
  adjunction diagram.
- **Open problems (`PR-72`).** A deferred generalization or a missing
  intrinsic definition is a GitHub issue labeled `needs-research`, never
  a block in the book.
- **Terminology (`TERM-*`).** The citation-backed inventory of recurring
  terminology drift is `.agents/references/terminology-dictionary.md`.
- **Source annotations (`STANCE-*`, `RESOURCE-*`).** The rules apply to
  the bibliography pages, such as
  `writing/category-theory/framework/Mathematical-Sources.md`.

## Detailed Documentation References

- **Writing guidelines**: [mathematical writing policy](https://github.com/dzackgarza/ai/blob/main/opencode/skills/mathematics/writing/policy/policy.md), with the [writing house conventions](#writing-house-conventions) above

- **Contribution workflow**: [`.agents/references/contribution-guidelines.md`](.agents/references/contribution-guidelines.md)

- **Categorical principles**: [`.agents/references/categorical-presentation-principles.md`](.agents/references/categorical-presentation-principles.md)

- **Design hazards ledger**: [`.agents/references/design-hazard-ledger.md`](.agents/references/design-hazard-ledger.md)

- **Mathematical lexicon**: [`.agents/references/mathematical-lexicon.md`](.agents/references/mathematical-lexicon.md)

## `COMMIT-01`: Read applicable contributing policies before every commit

Read the common and edit-specific sections routed by the
[reading index](docs/edit-reading-index.md) before committing. Check the work
in the commit against the applicable policies, following their cross-references.
Include this code anywhere in the commit message:

```text
c2291c7ab917bf86978a564337f00d5f
```

The hook checks whether the commit message contains the code. It does not check
whether the applicable policies were read or followed.

This requirement applies to authored commits, including amendments, checkpoints,
and commits made with `--no-verify`. Merge commits use Git's generated message.
Supply authored messages with `git commit -F <file>` or `-m <message>`;
interactive message editing is rejected before the editor starts.

Activate the tracked hooks in each checkout with
`git config --local core.hooksPath .githooks`. The `prepare-commit-msg` hook
checks the supplied authored message even with `--no-verify`; `commit-msg` checks it
again at the final message boundary. Both allow merge commits. The tracked `pre-commit`,
`pre-push`, and `post-commit` hooks delegate to the corresponding hooks in the
globally configured `core.hooksPath`.

Keep this policy last in this document. Put later policies before it.
