/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
module

public import CasAcceptance
public import CasAcceptance.Surface.Realized
public import ResearchLeaves.FiniteSets.Forget
public meta import CasAcceptance
public meta import CasCatalogue.ResolveSyntax
public meta import CasCatalogue.AcceptanceSyntax

@[expose] public section

/-!
# `lean-cas-dsl`'s permanent assertions, with this package's realizations

The admitted assertions of `lean-cas-dsl` are rerun here, unchanged, with the realizations of this
package added (workflow step 8). The two assertions `lean-cas-dsl` records as gaps for want of an
action of the forgetful functor on presented finite sets now hold:

* `card.finite_sets.three`: `|Fin 3| = 3` on finite sets;
* `limit.finite_sets.pullback.card`: the pullback of finite sets returned along the lift has 3
  elements.

Adding the package changed only computability: the operation surfaces of sets, finite sets,
groups and bilinear modules are those `lean-cas-dsl` computes without it
(`CasCatalogue.Surface.realizedSurfaces`), and the implementation gaps differ.
-/

#acceptance_rerun expecting "card.finite_sets.three" "limit.finite_sets.pullback.card"

namespace ResearchLeaves.Acceptance

def surfaces : List String :=
  [closure_report% "cat.sets", closure_report% "cat.finite_sets", closure_report% "cat.groups",
   closure_report% "cat.bilin_module"]

def gaps : List String :=
  [gaps_report% "cat.sets", gaps_report% "cat.finite_sets", gaps_report% "cat.groups",
   gaps_report% "cat.bilin_module"]

#guard surfaces == CasCatalogue.Surface.realizedSurfaces
#guard gaps != CasCatalogue.Surface.realizedGaps

end ResearchLeaves.Acceptance
