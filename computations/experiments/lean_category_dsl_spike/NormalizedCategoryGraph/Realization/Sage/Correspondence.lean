/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Core.Ids

/-!
# Sage realization — name ↔ stable-id correspondence

Generated from `sage_category_tree_stubs/design/sage_to_normalized_map/correspondence.json`.
Do not edit by hand; regenerate with `scripts/generate_sage_correspondence.py`.
-/

namespace NormalizedCategoryGraph.Realization.Sage

open NormalizedCategoryGraph

/-- Full Sage ↔ graph correspondence as deterministic JSON. -/
def correspondenceJson : String :=
  "{\"axiom_sage_to_graph\":{\"AdditiveAssociative\":\"Associative\",\"AdditiveCommutative\":\"Commutative\",\"AdditiveInverse\":\"Inverse\",\"AdditiveUnital\":\"Unital\"},\"graph_to_sage\":{\"cat.abelian_groups\":\"AbelianGroups\",\"cat.additive_abelian_groups\":\"CommutativeAdditiveGroups\",\"cat.additive_groups\":\"AdditiveGroups\",\"cat.additive_magmas\":\"AdditiveMagmas\",\"cat.additive_monoids\":\"AdditiveMonoids\",\"cat.additive_semigroups\":\"AdditiveSemigroups\",\"cat.algebras_over_field\":\"MagmaticAlgebras\",\"cat.algebras_r\":\"MagmaticAlgebras\",\"cat.algebras_r.graded\":\"GradedAlgebras\",\"cat.bialgebras_r\":\"Bialgebras\",\"cat.bimodules_r\":\"Bimodules\",\"cat.coalgebras_r\":\"Coalgebras\",\"cat.commutative_algebras\":\"CommutativeAlgebras\",\"cat.commutative_rings\":\"CommutativeRings\",\"cat.coxeter_groups\":\"CoxeterGroups\",\"cat.division_rings\":\"DivisionRings\",\"cat.domains\":\"Domains\",\"cat.euclidean_domains\":\"EuclideanDomains\",\"cat.fields\":\"Fields\",\"cat.finite_fields\":\"FiniteFields\",\"cat.gcd_domains\":\"GcdDomains\",\"cat.groups\":\"Groups\",\"cat.hopf_algebras_r\":\"HopfAlgebras\",\"cat.integral_domains\":\"IntegralDomains\",\"cat.left_modules_r\":\"LeftModules\",\"cat.lie_algebras_r\":\"LieAlgebras\",\"cat.magmas\":\"Magmas\",\"cat.modules_r\":\"Modules\",\"cat.modules_with_basis\":\"ModulesWithBasis\",\"cat.monoids\":\"Monoids\",\"cat.pids\":\"PrincipalIdealDomains\",\"cat.posets\":\"Posets\",\"cat.right_modules_r\":\"RightModules\",\"cat.rings\":\"Rings\",\"cat.rngs\":\"Rngs\",\"cat.schemes_s\":\"Schemes\",\"cat.semigroups\":\"Semigroups\",\"cat.semirings\":\"Semirings\",\"cat.sets\":\"Sets\",\"cat.ufds\":\"UniqueFactorizationDomains\",\"cat.unital_algebras\":\"Algebras\",\"cat.vector_spaces_k\":\"VectorSpaces\",\"cat.weyl_groups\":\"WeylGroups\"},\"sage_to_graph\":{\"AbelianGroups\":\"cat.abelian_groups\",\"AdditiveGroups\":\"cat.additive_groups\",\"AdditiveMagmas\":\"cat.additive_magmas\",\"AdditiveMonoids\":\"cat.additive_monoids\",\"AdditiveSemigroups\":\"cat.additive_semigroups\",\"Algebras\":\"cat.unital_algebras\",\"Bialgebras\":\"cat.bialgebras_r\",\"Bimodules\":\"cat.bimodules_r\",\"Coalgebras\":\"cat.coalgebras_r\",\"CommutativeAdditiveGroups\":\"cat.additive_abelian_groups\",\"CommutativeAdditiveMonoids\":\"cat.additive_monoids\",\"CommutativeAdditiveSemigroups\":\"cat.additive_semigroups\",\"CommutativeAlgebras\":\"cat.commutative_algebras\",\"CommutativeRings\":\"cat.commutative_rings\",\"CoxeterGroups\":\"cat.coxeter_groups\",\"DivisionRings\":\"cat.division_rings\",\"Domains\":\"cat.domains\",\"EuclideanDomains\":\"cat.euclidean_domains\",\"Fields\":\"cat.fields\",\"FiniteFields\":\"cat.finite_fields\",\"GcdDomains\":\"cat.gcd_domains\",\"GradedAlgebras\":\"cat.algebras_r.graded\",\"Groups\":\"cat.groups\",\"HopfAlgebras\":\"cat.hopf_algebras_r\",\"IntegralDomains\":\"cat.integral_domains\",\"LeftModules\":\"cat.left_modules_r\",\"LieAlgebras\":\"cat.lie_algebras_r\",\"Magmas\":\"cat.magmas\",\"MagmaticAlgebras\":\"cat.algebras_r\",\"Modules\":\"cat.modules_r\",\"ModulesWithBasis\":\"cat.modules_with_basis\",\"Monoids\":\"cat.monoids\",\"Posets\":\"cat.posets\",\"PrincipalIdealDomains\":\"cat.pids\",\"RightModules\":\"cat.right_modules_r\",\"Rings\":\"cat.rings\",\"Rngs\":\"cat.rngs\",\"Schemes\":\"cat.schemes_s\",\"Semigroups\":\"cat.semigroups\",\"Semirings\":\"cat.semirings\",\"Sets\":\"cat.sets\",\"UniqueFactorizationDomains\":\"cat.ufds\",\"VectorSpaces\":\"cat.vector_spaces_k\",\"WeylGroups\":\"cat.weyl_groups\"},\"schemaVersion\":\"0.1.0\"}"

theorem sage_magmas_id : CategoryId.magmas.raw = "cat.magmas" := rfl
theorem sage_sets_id : CategoryId.sets.raw = "cat.sets" := rfl
theorem sage_comm_rings_id : CategoryId.commutativeRings.raw = "cat.commutative_rings" := rfl

theorem correspondence_mentions_magmas :
    correspondenceJson.contains "cat.magmas" = true := by
  native_decide

end NormalizedCategoryGraph.Realization.Sage
