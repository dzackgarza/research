/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Core.Ids

/-!
# Presentation overlay

Semantic registry must not know Graphviz layout. This layer records visibility,
clusters, and preferred parents for the hand DOT.
-/

namespace NormalizedCategoryGraph

structure PresentationEntry where
  target : CategoryId
  visible : Bool
  cluster : Option ClusterId
  preferredParent : Option CategoryId
  showClassifierLeg : Bool
  labelOverride : Option String
  deriving Repr

end NormalizedCategoryGraph
