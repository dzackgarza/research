/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Core.Universes
import NormalizedCategoryGraph.Core.Ids
import NormalizedCategoryGraph.Core.Classifier
import NormalizedCategoryGraph.Core.CategoricalPullback
import NormalizedCategoryGraph.Core.AxiomOpfibration
import NormalizedCategoryGraph.Core.Expr
import NormalizedCategoryGraph.Core.Normalize
import NormalizedCategoryGraph.Core.StructuralMap
import NormalizedCategoryGraph.Model.Atomic
import NormalizedCategoryGraph.Model.Interpretation
import NormalizedCategoryGraph.Registry.Entry
import NormalizedCategoryGraph.Registry.Extension
import NormalizedCategoryGraph.Presentation.Nodes
import NormalizedCategoryGraph.Categories.Algebra.Magmas
import NormalizedCategoryGraph.Categories.Algebra.Rings
import NormalizedCategoryGraph.Names.Standard
import NormalizedCategoryGraph.Specimen.Viability
import NormalizedCategoryGraph.ForMathlib.CategoricalPullback

/-!
Standalone normalized graph root.

Mathlib and Sage realizations are **not** imported here — use
`NormalizedCategoryGraph.Realization.Mathlib.Atomic` and
`NormalizedCategoryGraph.Realization.Sage.Correspondence` as separate roots.

This root contains no serialized Sage observation or correspondence data.
-/
