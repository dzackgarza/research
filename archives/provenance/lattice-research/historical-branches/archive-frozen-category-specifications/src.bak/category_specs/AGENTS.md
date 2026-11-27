# AGENTS.md - category_specs

This file is the mandatory entry point for agents working under `category_specs/`. Keep it small.
Canonical category-spec guidance lives in local skills under `.agents/skills/category-spec-*`.

## Research destination

`category_specs` exists to define the mathematically natural category/refinement language required by `GOAL.md`: typed objects, constructors, Hom/End/Aut vocabulary, modules with forms, lattices, lattice isometry groups, and implementations by Sage or other exact systems that later Coble/K3 work can use without raw-matrix folklore.
Its purpose is not to maintain method inventories, ledgers, or diagnostic classifications for their own sake, and it is not a catalog of every Sage method.

The spec phase is source-grounded, but Sage coverage does not decide mathematical admissibility.
Sage inventories decide realization, honest refinement targets, existing methods, and implementation gaps.
Category membership and witness data decide the public mathematical vocabulary.

The public vocabulary must let later research code construct `R^n` as a free `R`-module with the correct module, finite-rank, and basis/witness refinements; define homomorphisms by images of generators when the source object has the required generator or basis data; construct modules with bilinear or quadratic forms; and express Gram matrices, orthogonal complements, primitive sublattices, discriminant groups/forms, and base changes through the categories that make those methods meaningful.

Hom, End, and Aut are mathematical objects.
For a lattice `L`, `O(L)` is `Aut_Lattices(L)`, the group of lattice automorphisms.
It belongs in the spec as a canonical object of `Groups`. Identity, multiplication, inverse, equality or extensional comparison, and certified elements are group-level structure.
The method `gens()` appears only when the same object is also placed in `FinitelyGeneratedGroups`, a generated matrix-group category, `FinitelyPresentedGroups`, or an explicitly generated-subgroup category.

The downstream lattice/Coble computations should eventually read as constructions of objects and morphisms such as `Pic(S)`, `f^*Pic(S) <= H^2(X, \mathbb{Z})`, and `T_Co = (f^*Pic(S))^\perp <= \Lambda_{\mathrm{K3}}`, with discriminant forms, primitive embeddings, orthogonal complements, isotropic orbits, stabilizers, and involution eigenspaces computed through source-backed mathematical interfaces.

Every category-spec action must preserve or advance a mathematical owner, operation, hypothesis, representation split, Sage bridge point, category/refinement membership, required witness, or missing-category obligation.
A spec item is in scope when it is needed to express later lattice or Coble computations as typed mathematical constructions, or when Sage investigation shows that omitting it would force raw matrix, vector, or group manipulation at the research layer.
It is out of scope for this phase when it only improves general Sage ergonomics, covers unrelated algebraic structures, documents arbitrary concrete methods, or claims a stronger category refinement without the required witnesses or proof.
Later geometry vocabulary is recorded as deferred until the lattice substrate exists.

If an edit only makes a report cleaner, a row count smaller, or a diagnostic bucket tidier, it has not advanced the category-spec goal.
Terminology cleanup is also insufficient.
Replacing words such as "surface", "admission", "frontier", or "smoke" only matters when the rewritten passage states the mathematical object, operation, category, hypothesis, witness, source evidence, or implementation gap that the old wording hid.

Operational invariants:

- Type mathematical objects by their structure, not by their storage.
  A lattice is not merely a matrix; a Hom object is not merely a Python method search.
- Accept raw matrices only as realizations of maps, forms, embeddings, quotients, complements, or orbit problems.
- Place each operation at the highest mathematically valid owner.
- Let category membership determine method obligations.
  `Groups` gives group operations; `FinitelyGeneratedGroups` gives finite-generation structure.
- Treat Sage behavior as implementation evidence and compatibility data, not as the specification itself.
- Classify gaps by ownership: external Sage API stub, plugin inheritance edge, category-spec owner method, or wrong category graph.

## Directive alignment

Before acting, confirm the user's stated directive, the action you plan, and why the action matches that directive rather than a substituted goal.
A handoff leaf, mapping block, test repair, or plan cleanup is not automatically the directive.
If the user asks for entrypoint guidance, anti-laundering doctrine, or repo-wide framing, do not substitute the current source-mapping leaf unless that leaf is explicitly named.

## Mathematical checkpoints

When asked to touch base with high-level tasks, do not answer with feature names, plan names, stage names, or a "real work stack" before stating the mathematics.
A valid category-spec checkpoint names the active mathematical unit:

```text
For objects of category C satisfying hypotheses H,
Sage method or constructor m realizes operation O,
with codomain or return object Y,
and requires witness data W.
```

Then state the unresolved mathematical claims, the next claim to settle, the controlling source evidence, and the claim that becomes true when the task succeeds.
A list of routes, mappings, audits, tests, or implementation stages is allowed only after those claims are stated.

Do not describe a docs edit, handoff update, renamed plan, mapped row, or category test as progress unless it changed a definition, construction, theorem-shaped claim, category/refinement membership, proof obligation, implementation witness, or source-backed computation.
If it did not, say that it was paperwork, not mathematical progress, and continue from the current mathematical obligation.

## Sage constructor and method operation rows

Before category-spec Sage inventory or mapping work, open `[[SPEC-SAGE-CONSTRUCTOR-METHOD-FRONTIER]]`.

That spec is semantic-extraction first.
Read the Sage method body, docs, and examples deeply enough to state what behavior is implemented; then introduce the mathematical vocabulary required by that behavior, state the weakest structure and hypotheses, and only then assign the owner.
Sage exposure and an a priori category primer are both insufficient owner evidence.

A source-mapping row is a mathematical assertion with provenance:

```text
Sage behavior
  -> mathematical operation under hypotheses H
  -> weakest category owner or refinement C
  -> required witnesses and return object
  -> source evidence
```

Category-spec mathematical inventory or mapping progress exists only when a row states or corrects the mathematical operation, hypotheses, owner category or refinement, witness data, codomain/return object, and source evidence; or when it records that no such assertion exists because the Sage constructor, method, or class is nonmathematical residue or an unresolved mathematical question.
The map document is not the mathematical object of progress; the object is the source-backed mathematical claim in the row.

Compatibility, runtime, display, private, test-helper, package-export, and backend-plumbing methods are not a parallel progress object.
Discard them after a one-line residue classification unless they change the mathematical interface or block construction of a required spec object.

Do not report progress from row counts, file counts, review prose, current-state summaries, handoff edits, broad checkpoints, or mapping-doc edits that do not change a theorem-shaped operation claim.
Subtree `SAGE_INVENTORY.md`, `MAPPING.md`, spec rows, cards, decisions, and handoffs are evidence for definitions, implementations, and gaps; the map only records source-backed mathematical assertions.

## Always-active rules

- Obey the repo root `AGENTS.md`; load `research-state-machine` for plan-to-execution routing and acceptance, and load `research-proof-auditing` for proof, evidence, and audit-sufficiency questions.
- The category-spec project exists to specify a Sage-grounded mathematical interface inside Sage's category/object universe.
  Current Sage coverage is not the adequacy standard, but Sage interop remains a design constraint: refined Sage objects should remain usable by existing Sage code when mathematically appropriate.
  Inventory and mapping preserve existing Sage functionality, identify honest refinements, and expose where implementation is weaker than the mathematically natural spec.
- Category-obligation examples assert that representative Sage/project objects instantiate declared categories and satisfy the obligations of those categories.
  A failed assertion asks which mathematical claim failed: false, under-hypothesized, unrealized by the implementation, missing constructor or refinement witness, missing source evidence, or blocked by a backend/tooling gap.
  Route the answer to the spec, implementation, or backend task; do not treat test output as a separate epistemic layer or weaken a spec obligation without a grounded replacement weakest category.
- Refinement is declaration, not validation.
  It says that an implementation is to be regarded as an object of a project category and therefore carries that category's contract.
  It does not interrogate the object, prove satisfaction, reject because project methods remain abstract, or instantiate a missing implementation.
  Category obligation examples expose those implementation gaps.
- `ParentMethods` are mathematical object-method obligations, not provider implementations or runtime failure hooks.
  Use Python `abc.abstractmethod` to represent abstract spec obligations in the class system; do not replace them with generated bodies, `assert False`, `NotImplementedError`, name-specific logic, or refinement-time satisfaction checks.
- For ABCMeta/refinement work, use the project-owned category/refinement/constructor path, not raw Sage refinement, as the boundary under test.
  Do not add runtime acceptance checks, instantiate inside refinement, or perform MRO surgery when the intended relation can be expressed by local dynamic-metaclass composition that delegates ordinary behavior to Sage and ABCMeta.
  If a project abstract requirement has the same name as a concrete method already supplied by the Sage parent-class bases, keep Sage's MRO as the source of satisfaction; do not let the abstract spec method shadow that concrete implementation.
- Before advancing a category-spec task, phase, or plan, review the staged diff, the unstaged diff, and any commits created during the work for spec weakening.
  Deleted abstract methods, removed constructor obligations, narrowed category assertions, moved obligations without a source-grounded replacement weakest category, and Sage-gap-driven interface shrinkage fail review even if category-obligation output improves.
- Treat spec files, review files, theory notes, TODO files, and durable design artifacts as source material.
  Do not rewrite, shorten, modernize, or delete them unless the user explicitly asks for that exact edit.
- Use Nimbalyst tracker files for planning, follow-ups, blockers, decisions, deferred compliance findings, failed-assertion classification, and outstanding work.
  Do not create ad hoc planning, status, audit, or TODO markdown files when a tracked file is the right durable artifact.
- Use only standard registered tracker types.
  Classify category-spec work with tags and `.agents` paths, not custom `x-work` types.
- Never call `tracker_create` or `create_task` for markdown-backed tracker items.
- Never mark parent work `accepted`, native items `done`, sprint plans `closed`, or broader phase/feature acceptance without human approval.
  Do not translate that rule into `needs-human-input` for ordinary category-spec task cards whose routing is already determined by source grounding, repo policy, the DAG, or agent-executable review.
- If a category-spec rule is relevant but not in context, load the matching category-spec skill or memory before acting.
  Do not guess from memory.
- Before reviewing recent category-spec commits, suspicious engineering-shaped patches, cache/lookup/cast/hook/QC work, or prior agent output, retrieve the ordinary governing memories by topic: `mem:repo-purpose-mathematical-research-machine`, `mem:category-spec-rotten-core-indicators`, `mem:mathematical-sanity-check`, `mem:analysis-must-be-grounded`, `mem:paperwork-is-a-routing-layer-not-progress`, and `mem:corrections-update-the-model-not-the-artifact`. If the work touches refinement, provider ordering, constructor refinement, abstract methods, ABCMeta, or failed category assertions, also retrieve `mem:category-spec-repo-model-corrections`, `mem:category-spec-refinement-category-declaration`, `mem:category-spec-methods-are-abstract`, and `mem:what-category-specs-actually-is`. Use `agent-memory search content` with the relevant topic words if the exact memory key is not known.
- Before editing a spec, mapping, method, constructor, Hom/End/Aut rule, invariant, or predicate, perform the definition-grounding prerequisite from `category-spec-style`: locate the exact mathematical definition and hypotheses in canonical repo theory, Sage written docs/source, references, spec backups, or an approved decision card.
  Vague migrated cards and old TODO bullets are not enough.
  If the definition is unclear, create or update a decision/source-mining card and stop that leaf.
- Constructor mapping has no deferred state.
  Every source-grounded Sage constructor shape recorded in mapping docs maps to a named-parameter category-owned overload or spec-layer promotion path.
  Ungrounded or rejected constructor ideas are absent from constructor mappings, provenance, category-obligation examples, decisions, and tasks; do not preserve them as "not included in the definition", "deferred", blocked, or gap records.
- Refinement targets one category: the smallest mathematically correct category for the object.
  Do not pass several categories to `refine_category`; inherited membership must come from the category hierarchy, not from manually listing ancestors at the call site.
- Do not use `MorphismMethods` in category specs.
  Morphism behavior belongs on the relevant Hom-category element method class, e.g. `C.HomCategory().ElementMethods`, not on the object category itself or a nested `MorphismMethods` method-container.
- For domain-specific terms with multiple plausible meanings, keep the meanings separate unless a source-backed proof records exactly when they coincide.
  Do not write a category operation by normalizing to the most familiar interpretation of a word.

## Canonical skills

- Load `category-spec-style` before any task that touches category-spec content or compliance: specs, category definitions, methods, constructors, morphisms, Hom/End/Aut objects, Sage wrappers, type annotations, test files, category-obligation examples, implementations, Sage inventory, or mapping documents.
- For nontrivial edits, loading the skill stub is not enough: keep the canonical references named by the matching skills in context before editing.
  Any change to method ownership, inherited method classes, `@abstractmethod`/`@override`/`@final`, type aliases, construction categories, Hom/End/Aut categories, category-obligation examples, specs, or mapping rows is nontrivial.
  If the needed reference is not already in context, stop and read it before checkpointing or editing.
- Load `category-spec-subtrees` before editing a specific category subtree or deciding where a method, constructor, Hom/End/Aut rule, or subtree test belongs.
- Load `category-framework-design` and its relevant references before editing or reviewing Hom/End/Aut structure, autsets, construction categories, refinement order, or constructor interception.
  For Hom/End/Aut objects, `homsets-structural-core.md` is mandatory context.
- Load `lattice-redesign` and its relevant references before editing forms, formed modules, lattices, lattice morphisms, orthogonal groups, discriminant objects, or lattice-backed Hom/End/Aut objects.
  For these edits, `category-abc-spec.md` and `lattice-interface-style-guide.md` are mandatory context.
- Load `category-spec-workflow` before any task that touches execution mechanics: tracker item creation or migration, Nimbalyst plans, sprint metadata, tracked work metadata, delegation contracts, subagent instructions, branch/PR policy, failed-assertion classification, validation handoff, stale-document migration, or status changes.
- Load narrower category-spec skills when their descriptions match the task: audit, planning, retirement, Sage mapping, failed-assertion classification, and visuals.

## Removed local docs

`STYLE.md`, `WORKFLOW.md`, and lower nested `AGENTS.md` files have been migrated into skills and should not be recreated as parallel docs.
If an older prompt references one of those files, load the corresponding category-spec skill instead.
