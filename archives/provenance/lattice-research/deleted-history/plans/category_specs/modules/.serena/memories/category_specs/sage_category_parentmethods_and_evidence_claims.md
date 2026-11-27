# Sage Category ParentMethods And Method-Provider Mixins

## When This Applies

This applies when working in `plans/category_specs`, especially module/ring category specs that refine existing Sage objects with `_refine_category_`.

## Rule From Transcript Evidence

A prior Codex transcript records the user correcting direct calls such as `SageRings.ParentMethods.foo(self, ...)` / `Sets.ParentMethods.cartesian_product(self, ...)` as the wrong pattern for these specs.

Evidence source: parsed Codex transcript `~/.codex/sessions/2026/04/21/rollout-2026-04-21T14-08-20-019db05e-de7b-7612-a32b-c1da9f786724.jsonl`, section around the discussion beginning with “Honest question: is calling the parentmethods the theoretically most correct solution...”. The key correction was: the spec subcategories must define the relevant upstream Sage categories as supercategories properly. If the Sage categories are in the supercategory graph, Sage's dynamic MRO can see their `ParentMethods` implementations. Compatibility forwarding to `ParentMethods` is a symptom of malformed category joins, not the desired implementation strategy.

## Correct Protocol

- Treat `ParentMethods`, `ElementMethods`, `MorphismMethods`, homset nested classes, and related Sage category nested classes as method-provider/spec surfaces, not public implementation APIs.
- Constructor collectors like `NamedModules` / `NamedRings` are the implementation bridge: call existing Sage constructors, then refine the concrete result into the new category hierarchy.
- For every spec subcategory, define `super_categories()` so the relevant upstream Sage category/subcategory is actually in the category graph. The goal is for Sage's dynamic parent/element/morphism MRO to see upstream implementations naturally.
- If a method is implemented by the concrete Sage class returned by a named constructor, leave the spec method abstract and rely on the concrete class in the refined object's MRO.
- If a method is implemented by an upstream Sage category, include that upstream category as a supercategory rather than adding a forwarding shim.
- If an abstract spec method shadows an upstream Sage implementation after refinement, inspect the refined object's final MRO and category supercategories, then fix category composition.
- Implement method bodies in the spec category only for genuinely new behavior forced by the new mathematical subcategory, not to recover upstream Sage behavior.

## What Not To Do

- Do not implement behavior by calling `SomeCategory.ParentMethods.method(self, ...)`, `SomeCategory.ElementMethods.method(self, ...)`, `.f`, or similar direct method-provider internals.
- Do not use direct `ParentMethods` forwarding as a compatibility bridge for shadowed methods.
- Do not treat cooperative `super()` as an automatic fix; it only works when the desired implementation is actually present in the final refined object's MRO.
- Do not patch individual shadowed methods one by one when the real problem is that the Sage supercategory graph is malformed.
- Do not create fake named-category or fake axiom registrations to force method availability. Use real Sage supercategories and the proper `_base_category_class_and_axiom` mechanism only for literal chained subcategory registration.
- Do not redeclare an upstream Sage category method as a higher-priority abstract spec method unless the upstream category that implements it remains visible in the refined MRO.

## Why

Sage builds dynamic parent, element, morphism, and homset classes from the concrete object's class plus the joined category graph. If the new spec subcategory omits the upstream Sage category that supplies a method, an abstract method in the spec layer can mask the real implementation. Calling `ParentMethods` directly bypasses category composability and breaks future subcategories whose objects did not come from the named Sage constructor path. The correct fix is categorical composition, not method-level forwarding.


## Verification

- Searching the changed spec files should not show direct implementation calls to `.ParentMethods.` except citations/comments explicitly documenting upstream APIs.
- Runtime failures from abstract methods shadowing Sage implementations should be addressed by inspecting the refined object's MRO and category supercategories.
- Runtime verification should inspect the refined object's MRO and category supercategories, not validate direct `ParentMethods` forwarding.

## Category-Spec Design Philosophy

This applies to both `plans/category_specs/rings` and `plans/category_specs/modules`.

The new category hierarchy is an ABC/spec hierarchy. Its job is to record the mathematically correct method surface at the correct categorical level of generality, not to weaken itself until all current Sage concrete objects instantiate cleanly.

Constructor collectors such as `Rings().NamedRings()` and `Modules(R).NamedModules()` are convenience method collectors and implementation bridges. They are not axioms and not categories. Their methods call existing Sage constructors and then refine the resulting concrete object into the new spec hierarchy.

Named implementation categories for constructor outputs may describe the method surface of known Sage-backed objects, but they should not become ad hoc composite axioms. If a real chained subcategory is needed, use Sage's `_base_category_class_and_axiom` mechanism only for literal chained category registration, with empty intermediate classes as needed.

## ABC Failures Are Not Automatically Bugs

An abstract-method failure after refinement has to be classified before editing:

- If Sage already implements the method through a concrete class or upstream Sage category and the new spec shadows it, the category graph or MRO composition is wrong. Fix `super_categories()` / category registration so the implementation is visible.
- If the method is mathematically required at that categorical level but Sage has no implementation for some concrete object, the failure is a surfaced implementation gap. Do not remove or move the abstract method merely to make a smoke test pass.
- If the method is not mathematically required at that level, then the spec placement is wrong and should be moved to the correct subcategory.

In particular, methods such as `intersection` and `saturation` can belong in an integral-domain free-module spec even if Sage currently implements them only for narrower classes such as PID-backed free modules. Existing non-uniformity is part of what this spec work is intended to expose.

## Modules-Specific Vocabulary

The local module hierarchy should use the new vocabulary such as `WithGeneratingSet` / `WithOrderedGeneratingSet` rather than exposing Sage's `WithBasis` as the public design concept. Sage categories such as `ModulesWithBasis(R)` can still be included as upstream implementation supercategories when needed for Sage's existing method providers, but that is an implementation-composition detail, not the new public vocabulary.

## Runtime Verification Protocol

Do not use "all refined objects can access every declared method without an abstract-method failure" as the success criterion. That test confuses spec correctness with current implementation coverage.

Use these checks instead:

- For methods implemented on concrete Sage classes, confirm the concrete class remains before the spec category in the refined object's MRO.
- For methods implemented by upstream Sage categories, confirm the relevant Sage category is in `super_categories()` and appears in the final dynamic MRO before any local abstract declaration that would shadow it.
- For methods intentionally abstract because Sage lacks a general implementation, record the observed failure as an implementation gap, not as a reason to weaken the spec.
- Keep direct `.ParentMethods.` calls out of implementation code.

## Current Module Task Recovery Protocol

Before continuing module-spec implementation, treat the current staged module work as suspect and audit it against this memory.

Required first recovery checks:

- Restore any spec weakening done only because a refined Sage object raised an abstract-method error. Known example: `_FreeModulesOverIntegralDomains` must keep `intersection` and `saturation` if those are the intended integral-domain free-module ABC surface.
- Re-evaluate `_RModObjects.quotient` and any other fallback methods added to make existing Sage calls pass. Keep them only if they are genuine new categorical behavior, not compatibility patches that hide missing implementations or malformed category composition.
- Separate verification output into three categories: concrete implementation satisfied, upstream Sage category implementation satisfied through MRO, and intentional implementation gap surfaced by the ABC.
- When user corrections imply prior discussion exists, read the transcript or memory first. Do not reconstruct the design philosophy from a short reminder.
