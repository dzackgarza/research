---
title: No stub re-declaration in subcategory specs
---
Subcategory `ParentMethods` must only contain operations that do NOT exist on any
supercategory in the chain.
Before adding a method, trace the full `super_categories()` linearization — if any
supercategory already defines the operation (even with a different signature), the
subcategory MUST NOT re-declare it as `@override @abstractmethod`. Delete the
re-declaration entirely.
Inherited operations are inherited for a reason.

When reviewing a subcategory spec file, if most methods are inherited re-declarations,
delete them structurally — do not adjust decorators, tweak signatures, or rename.
The correct diff is a net removal.

**Recognition heuristic — before making ANY edit to a subcategory spec:**

1. Read `super_categories()` and resolve the full ParentMethods chain.
2. For each method in the subcategory's ParentMethods, ask the MATHEMATICAL question
   first: what IS this operation?
   Does it belong to the object itself, or to a more general category in the chain?
   A real subset HAS a cardinality because every set does.
   A real subset IS connected because every topological space is.
   Union of real subsets IS union of sets — "interval normalization" is an
   implementation detail, not a new mathematical operation.
3. If the operation is mathematically guaranteed by a supercategory, the method is a
   re-declaration. The only correct action is deletion.
   Do not: remove `@override`, change the signature, add `@final`, rename, or adjust
   decorators. Any edit short of removal is turd-polishing.
4. If the operation is genuinely new to this subcategory — something no supercategory
   could define because it requires structure not present at higher levels — keep it.

Override errors are symptoms of a mathematical error, not a type-system one.
If you find yourself adjusting decorators to resolve a conflict, stop and ask the
mathematical question first.

When IS a narrowed override valid?
Only when there is a concrete implementation whose body genuinely depends on the
narrower type. `is_compact` on RealSet with a body that calls `self.inf()` and
`self.sup()` — valid, because the implementation needs RealSet-specific operations.
`union(self, X: RealSubset) -> RealSubset` with no body (just `...`) — re-declaration.
The narrower return type is speculative; there is no code that actually needs
`RealSubset` rather than `Subset`.

Distinguish spec concerns (WHAT operations exist) from implementation concerns (HOW they
are computed). "Interval-normalized union" is a HOW — the mathematical operation is
union, and normalization belongs in the implementation, not the spec.
If a method name describes an algorithm rather than a mathematical operation, it does
not belong in a category spec.

Beware invented agent word salad: phrases like "finite-interval-normalized" are not
standard mathematical vocabulary and should not be accepted as precise.
Translate to established mathematics: "express in terms of the standard basis of R." The
idea is usually simpler than the invented language makes it sound, and stripping the
noise often reveals that the "specialized" operation is just a standard one.

The mapping document produces category obligations, not code justifications.
If a Sage method has no spec home, the mapping declares where it must go.
No "rejected surfaces," no deferrals, no "abstract" in place of spec.
If the target spec file doesn't have the method yet, the mapping still names it — and
that gap is a task, not a document note.

A file where most methods match step 3 is not a spec file to be edited — it is a
deletion target. Approach it by asking "what stays?"
not "what changes?"

Do not confuse a set with a basis expression representing it.
A real subset X expressed as X = ∪ᵢ Xᵢ (finite union of intervals) is NOT the set {X₁,
…, Xₙ}. Iterating over the basis components is not the same as iterating over elements.
Methods that describe the representation (component count, interval access) belong on a
representation object, not on the set itself.

Do not use existing code declarations as mathematical authority.
The fact that `_SetObjectMethods` declares `__iter__` does not make `Sets()` iterable —
R is a set but uncountable.
Existing code can be wrong.
Judge methods by what the mathematical object IS, not by what some Python class
currently declares.
