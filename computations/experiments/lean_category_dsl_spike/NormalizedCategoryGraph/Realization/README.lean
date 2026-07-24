/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Realization.Mathlib.Atomic
import NormalizedCategoryGraph.Realization.Sage.Correspondence

/-!
# Realization layer

Concrete consumers of Spec:

* `Realization.Mathlib` — full `AtomicModel` (Sets, Finite, Graded, Magmas, algebra,
  modules, exceptional hosts)
* `Realization.Sage` — typed correspondence interface; versioned Sage data remains
  outside Lean source
-/

namespace NormalizedCategoryGraph.Realization

end NormalizedCategoryGraph.Realization
