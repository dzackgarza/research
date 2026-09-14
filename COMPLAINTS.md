# Foundational Gaps and Papercuts

Record unresolved issues observed anywhere in research or contribution work.
The primary subject is general mathematical machinery that should be available
but is missing, incomplete, or bypassed in the owned language. Concrete workflow
papercuts also belong here. This is neither a retrospective work log nor a list
of hypothetical defects.

Use the [mathematical tracing method](CONTRIBUTING.md#mathematical-dependency-tracing)
and the capture/lifecycle rule
[`DEV-59`](CONTRIBUTING.md#dev-59-record-observed-foundational-gaps-and-papercuts).
State the mathematics before its implementation symptoms. Extend an existing
entry when another consumer exposes the same foundation. Link execution details
in [TODO.md](TODO.md); keep implementation ordering and active reservations there.
Remove resolved entries with evidence in the commit, retaining only unfinished
needs and any required terminal verification. Durable definitions and decisions
belong at their mathematical declarations or in CONTRIBUTING, not solely here.

## Foundational Mathematics

### Image sets are not one reusable owned construction across finite and infinite sources

- **Mathematics:** for a map \(f:S\to X\), the image \(f(S)\) is a set equipped with the canonical surjection from \(S\); when \(f\) is injective it carries the canonical bijection with \(S\).  Finiteness, enumeration/order, cardinality and positional access should be transported from the source when justified by that map, not reimplemented by each consumer.
- **Expected architecture:** one owned image construction retains the exact source set, map, injectivity/inverse data and resulting set.  Finite and infinite cases are realizations of that same construction.  Consumers such as the canonical generator image \(S\to U(\operatorname{Free}_R(S))\) reuse it directly.
- **Observed:** `Sets.image_set()` currently materializes a `finite_ordered_set(tuple(...))` for a finite source but returns Sage's `ImageSet` for the non-finite remainder.  The free-module layer separately grew `FreeModuleGeneratorSet`, another implementation of the image of its unit/basis map, with its own membership, cardinality, indexing and display logic.
- **Why this matters:** the finite/infinite split and the bespoke free-generator image are symptoms of a missing uniform owned construction.  They create parallel sources for order/cardinality/display and make a generic functorial image look like module-specific machinery.
- **Owner:** owned set image construction and the free/underlying-set adjunction.  Replace consumer-specific image-set classes with the common owned image object once that object carries the required transported structure.

### A framing is stored as labels plus a function and reconstructs its free source later

- **Mathematics:** a framing of an \(R\)-module \(M\) is the selected epimorphism \(\operatorname{Free}_R(S)\twoheadrightarrow M\).  The source free module and arrow are defining structure, not consequences to rediscover from a label set.
- **Expected architecture:** constructing a framed module constructs/retains \(S\), the actual `Free_R(S)` source and the framing morphism (or an equivalent first-class construction object).  `module_generating_set()`, `module_generator_morphism()`, `module_generators()` and `framing_morphism()` are views of that one datum.
- **Observed:** `FramedModules.ParentMethods.__init__` stores `_preamble_module_generating_set` and `_preamble_module_generator_function`; `framing_morphism()` later calls `FreeModuleOn(self.base_ring(), self.module_generating_set())` and constructs the framing arrow on demand.  The method is therefore acting as a second constructor.  The lattice defect that triggered this audit was a stronger instance of the same pattern: the real free module already existed but lattice accessors bypassed it.
- **Why this matters:** later reconstruction can silently substitute an isomorphic source for the selected one, encourages descendants to manufacture their own generator-family wrappers, and makes category membership stand in for actual chosen structure.
- **Owner:** `FramedModules` construction.  Make the selected free source/arrow first-class constructor data, while allowing subclasses whose framing is canonically derived to supply that actual construction through the same contract.

### Functor and adjunction displays do not have one endpoint-aware semantic owner

- **Mathematics:** a functor is not determined for interactive purposes by a noun such as “abelianization” or “free-group”; its domain and codomain are part of the datum.  An adjunction is a specified pair \(F:C\rightleftarrows D:U\) together with unit/counit.
- **Expected display:** default functor displays include at least the standard operation/symbol and `domain -> codomain`; adjunction displays expose both adjoints or the corresponding `C <-> D` relationship.  Subclasses may add meaningful parameters (ring map, acting group, fixed module) but should not each invent an unrelated prose label.
- **Observed:** the common `Functor` stores `domain()` and `codomain()` but has no common semantic display.  Subclasses return constants such as `Free-group functor`, `Abelianization functor`, `Fraction-field functor`, `Ring-of-integers functor`, and `Unit group functor`; several adjunctions similarly return only a compound name.  Other subclasses independently include partial endpoint/parameter information, so the public view is inconsistent.
- **Why this matters:** a type/name paraphrase can be correct yet tell the user nothing about the particular categorical arrow in hand, and duplicated display code drifts from actual endpoints.
- **Owner:** common `Functor`/`Adjunction` display protocol.  Standard names/symbols should be optional semantic labels layered on endpoint data owned by the base construction.

### Generic family displays still receive refinement- and implementation-flavoured names from callers

- **Mathematics:** an indexed family is the map \(I\to X\) (or the corresponding values with their index set).  A public operation such as `module_generators()` or morphism generator images is owned at its weakest semantic level; internal realization refinements do not change that result.
- **Expected display:** the family shows its actual finite indexed values, or its index set/defining rule for lazy cases.  An optional label names genuine extra mathematics, never the private realization that supplied the family.
- **Observed:** the common indexed-family display now exposes finite values and bounds large displays, but callers still pass labels including `Fractional-ideal generator family`, `Restricted-scalar generator family`, `Sparse free-algebra morphism generator-image family`, `Presented-algebra morphism generator-image family`, and `Ring-module generator family`.  Some labels may denote real stronger data (for example Smith framing or invariant factors); others merely expose the leaf implementation/refinement.
- **Why this matters:** fixing `Lattice-generator family` at one call site would leave the same abstraction leak throughout the tower.  The audit must distinguish genuinely refined mathematical families from generic operations wearing implementation-specific names.
- **Owner:** each semantic operation, reviewed against `OWN-18`, `OWN-21`, `STY-188` and `STY-189`.  Delete pure-renaming overrides/labels; retain specialized labels only where the returned object has genuinely stronger mathematical structure.

## Workflow Papercuts

Add concrete observed workflow friction here under a descriptive heading, with
the user action, expected behavior, actual result, owning boundary and example.
Use `DEV-59` for capture and resolution. Foundational mathematical gaps belong
above even when first noticed as an inconvenient method or notebook interaction.

### Required agent-memory search command is absent from the working environment

- **User action:** follow `AGENTS.md` before an architectural edit by running `agent-memory search --scope both ...`.
- **Expected:** the required `agent-memory` CLI is available in the repository working environment.
- **Observed:** the shell returned `command not found: agent-memory`; the vault itself remained readable at `/home/dzack/.agent-memory-vault`, so the required context had to be searched directly.
- **Owner:** contribution/tooling environment provisioning.
- **Example:** observed while selecting `analytic-families` on 2026-09-12.
