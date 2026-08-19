---
title: Mathematical Sanity Check — Step Back and Ask if It Is Absurd
date: 2026-05-27
status: active
---
# Rule: Perform a Mathematically-Minded Review Before Committing

## The principle

Before committing any code that defines mathematical structure — category graphs, method
ownership, type signatures, or inheritance — step back and ask:

**"Is this absurd?"**

Agents are capable of mathematical reasoning.
The failure is not ignorance; it is laziness.
Agents checkbox their way through implementation without exercising the mathematical
judgment they already possess.

## The test

For any mathematical definition:

1. **Does it make sense to a mathematician?** Would someone who knows the subject matter
   immediately recognize it as coherent, or would they laugh?
2. **Is it minimal?** Does it list only what is necessary, or does it bundle redundant,
   derived, or consequence-level structure?
3. **Is the naming correct?** Does the name match the mathematical concept, or does it
   import historical misnomers?
4. **Is the hierarchy a chain or a grab-bag?** Are parents immediate and meaningful, or
   is every ancestor listed directly?

If any answer raises doubt, stop.
Do not commit. Fix the definition.

## The anti-pattern

- **Box-checking without thinking:** implementing a method because a stub or a ledger
  says it is missing, without asking whether it belongs there mathematically.
- **Incremental accumulation without review:** adding direct ancestors, consequence
  categories, or redundant parents to make something work locally, without stepping back
  to see whether the graph is still coherent.
- **Deferring mathematical judgment to tooling:** treating mypy errors, ledger counts,
  or plugin behavior as the arbiter of correctness rather than mathematical sense.

## Historical example: QQ

A previous agent wrote:

```python
_QQ.super_categories() returns [
    _Fields(),
    _QuotientFields(),
    _NumberFields(),
    _GlobalFields(),
    Rings().Characteristic(0),
]
```

No one asked the obvious question: **is this absurd?**

QQ is a number field.
Number fields are fields.
The graph should encode `QQ <= NumberFields <= GlobalFields <= Fields`. Instead, it
listed all of them as direct siblings.
This is like saying "a dog is a mammal, a dog is an animal, a dog is a vertebrate" as
independent facts rather than a chain.

Also, `_QuotientFields` is not a quotient; it is a fraction field / localization.
The name is wrong.

Also, `_Fields` lists consequence categories (`_CommutativeRings`, `_EuclideanDomains`,
etc.) as direct parents.
A field is not a Euclidean domain in the sense of inheritance; it satisfies the axioms.

None of these required deep expertise.
They required **one second of thinking**. An agent who knows what a number field is
should immediately see that `QQ` is not a sibling of `Fields`. The failure was not
ignorance; it was not asking.

## The rule

**No mathematical code may be committed without a written sanity check.**

Before any commit that touches category graph, method ownership, or mathematical naming,
record in the commit message or a brief note:
- Why this definition is mathematically correct.
- Why it is minimal.
- Why the naming is accurate.

If you cannot write this in one or two sentences, you have not thought about it enough.

## Operation ownership gate

Before changing signatures, parents, inheritance, method names, or category placement,
answer:

- What mathematical operation is this?
- What object owns the operation?
- Is `self` the object being studied, the ambient object, a subobject, an element, or a
  morphism?
- Is an argument being used because the operation is relative to an ambient object?
- Is a zero-argument method meaningful, or only meaningful when `self` carries
  ambient/subobject structure?
- Would the proposed fix erase a true mathematical fact?

If the code conflict is between two meanings of one name, do not solve it by weakening
the category graph. Separate the meanings.

## Engineering skepticism gate

Before doing detailed engineering, ask whether the engineering preserves, clarifies, or
distorts the mathematics.

Reject fixes that:

- weaken a true mathematical inheritance because typing is inconvenient;
- rename or move operations without identifying their mathematical owner;
- satisfy a checker by erasing semantics;
- introduce adapters, facades, or runtime gaps instead of correct abstract obligations;
- produce architecture that cannot be explained in ordinary mathematical language.

The mathematical abstraction is the authority. The code is inspected and corrected until
it expresses that abstraction.

The RealSet/topological-space incident: the correct response was not to remove topology
from real subsets, but to distinguish ambient-relative operations from subobject
self-predicates. The drift came from treating a mathematical design issue as
ledger/typing work and from proposing degradation before understanding the object
structure.

## Commit-history review gate

When reviewing recent category-spec commits, do not start from whether the author
claimed alignment or whether QC improved. The writing agent almost always believed the
patch was aligned.

Start from the shape of the patch. In the category-spec phase, most legitimate changes
should look mathematical: categories, methods, owners, constructors, morphisms,
abstract obligations, source-grounded definitions, or tests that expose those
relations. A commit whose dominant nouns are engineering nouns, such as cache, lookup,
plugin, stub, cast, hook, report, ledger, test order, or runtime state, is suspicious
until it names the mathematical deficiency it repaired.

This is not a ban on engineering code. It is a sanity test for placement. If spec code
knows about a runtime/tooling concern and the commit does not explain the
corresponding mathematical object-level defect, presume the patch is making the repo
look more correct rather than making the mathematics more correct.

Case study: cache priming before category refinement should have looked out of place
immediately. Caching is not a mathematical structure. The right question was not "does
this fix the failed category assertion?" but "why is category-spec refinement reasoning
about caches at all?" That question leads to the actual defect: concrete providers and
abstract obligations were being ordered/classified incorrectly during refinement.

## Mathematical delta gate

For category-spec work, a patch is not substantively aligned merely because it makes a
tool, category-obligation example, hook, report, or ledger look better. It must have a
visible mathematical delta: a category edge becomes correct, an operation owner is
fixed, an abstract obligation is represented faithfully, a concrete provider is allowed
to satisfy the right contract, a missing obligation is exposed instead of hidden, or a
recovery formula/representation split is made explicit.

If the only visible delta is engineering-shaped, stop before polishing. The review
question is: "What mathematical statement would be false without this patch, and where
is that statement visible in the diff or its tracked work item?" If that cannot be
answered, reconstruct the hidden defect from transcript/source/commit evidence or
queue that reconstruction explicitly. Do not add casts, decorators, caches, local
validators, reports, or hook exceptions as substitutes for the mathematical delta.
