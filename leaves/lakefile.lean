import Lake
open Lake DSL

/-
Realization leaves hosted by `research` (`lean-cas-dsl/specs/architecture.md`: research owns no
ontology and may host realizations). Each module registers realizations of operations already formal
in `lean-categories`, through `lean-cas-dsl`'s leaf API, and nothing else.
-/
package «research-leaves» where
  version := v!"0.1.0"

require «cas-dsl» from git
  "https://github.com/dzackgarza/lean-cas-dsl" @ "2c2e31c029bb358fe0885f1e13d463f555787291"

lean_lib ResearchLeaves where
  globs := #[.andSubmodules `ResearchLeaves]
  leanOptions := #[
    ⟨`relaxedAutoImplicit, false⟩,
    ⟨`weak.linter.mathlibStandardSet, true⟩,
    ⟨`weak.linter.style.header, false⟩,
    ⟨`maxSynthPendingDepth, (3 : Nat)⟩]
