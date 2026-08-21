# Broader TODO

Arrive at the correct preamble architecture, under which all strictly mathematical tests pass. Type-checking is a non-concern for this phase.

Here, the correct architecture means that each category is unified with its implementation classes. The preamble constructs every required object through the owned category hierarchy instead of refining Sage objects into that hierarchy. A leaf category constructs only its immediate declared supercategory object through cooperative `super()` calls. Construction data passes down this chain, while inherited mathematical operations pass back up it. Refinement remains only for constructor-computed membership in subcategories that add properties or axioms without new construction data.

Correct. The plans supply the architectural model, not a progress ledger.

The broad design requires:

- Each category owns its parent, element, homset, and morphism implementations.
- Construction data passes through immediate supercategories.
- Each level provides enough data for lower-level mathematical operations.
- An enriched object remains one object. It does not wrap a duplicate underlying object.
- Morphisms are elements of homsets in the arrow category.
- Standalone functors forget structure.
- `refine()` adds properties or axioms only.

## Illustrative vertical consequences

These are examples of what the architecture should make true. They are not independent goals.

- For a finite field \(\mathbb F_q\), the free module \(\mathbb F_q^n\) is constructed as a module whose underlying set is an \(n\)-fold product. The set construction therefore gives \(\lvert\mathbb F_q^n\rvert=q^n\).
- A finite free \(R\)-algebra of rank \(n\), with finite base ring \(R\), receives cardinality \(\lvert R\rvert^n\) from its underlying free module. The final cardinality is owned by its underlying set, not by an algebra-specific method.
- The tensor algebra \(T_R(M)=\bigoplus_{d\geq 0}M^{\otimes d}\) receives set-theoretic facts through its graded module construction. In particular, \(T_R(0)\cong R\), and countability of the latter is inherited through construction.
- A finite-rank integral lattice is constructed through its formed free \(\mathbb Z\)-module and then through its underlying set. Its bilinear form adds structure without creating a second owner for set operations or cardinality.
- A group module is constructed through its module and set levels, with the action added at the group-module level. A standalone functor forgets the action; the object does not store a second module.
- A lattice isometry is an element of a homset. Its underlying function comes from the set level, linearity comes from the module level, and form preservation comes from the lattice level. Identity and composition belong to the corresponding homset and arrow-category structures.

The current implementation largely matches the first, fourth, and fifth points. Category-owned classes, cooperative construction, homsets, and standalone functors exist.

The current mathematical failure exposes the main remaining gap:

\[
\mathrm{Lattices.Zero}
\to \mathrm{BilinearForm}
\to \operatorname{TensorSquare}(0)
\to T_{\mathbb Z}(0)
\to \operatorname{UnderlyingSet}.
\]

Mathematically,

\[
T_{\mathbb Z}(0)\cong \mathbb Z.
\]

Therefore, this tensor algebra is countable. Its category does not preserve that fact. The valid assertion in [underlying_sets.py](/home/dzack/research/src/dzack_research/preamble/categories/sets/underlying_sets.py:119) rejects the incomplete construction.

No selected mathematical test body ran. Preamble construction failed during `tests/conftest.py`.

The next architectural repair is therefore precise:

1. Preserve countability and cardinality through the free-algebra and tensor-algebra construction.
2. Keep the assertion unchanged.
3. Run the existing mathematical specimens again.
4. Use the next mathematical failure to locate the next missing construction datum.
5. Inspect remaining `refine()` calls against the architectural boundary. Owned constructors build objects through cooperative `super()` calls. Each leaf category constructs only its immediate declared supercategory object. Refinement is limited to constructor-computed membership in subcategories that add properties or axioms. It never adopts Sage objects into the owned hierarchy or supplies construction data after instantiation.

This follows the goals recorded in the [threading architecture](/home/dzack/.agent-memory-vault/projects/github.com__dzackgarza__research/plans/features/FEATURE-category-foundations/plans/PLAN-coxeter-gitclones-absorption/plans/PLAN-threading-set-behaviour/PLAN-threading-set-behaviour.md:42) and [category construction model](/home/dzack/.agent-memory-vault/projects/github.com__dzackgarza__research/plans/features/FEATURE-category-foundations/plans/PLAN-coxeter-gitclones-absorption/plans/PLAN-threading-set-behaviour/plans/PLAN-cat-model-migration/PLAN-cat-model-migration.md:88).
