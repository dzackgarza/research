# Lattice Research — Roadmap

Durable narrative for the lattice-category project.
Live execution state is the GitHub issue tree under [root ledger #46](https://github.com/dzackgarza/research/issues/46); this page is the readable projection and the "why."

## The two buckets

The work is split into two top-level buckets, reflecting a ratified boundary: the base spike is a **Sage-parity** drop-in replacement; genuinely new mathematics **forks** into a separate extension track.

### 🟦 Sage parity — base spike ([#71](https://github.com/dzackgarza/research/issues/71))

A drop-in Sage replacement built by **parity sweeps, one per category** the project will own.
Each sweep organizes and uniformizes what Sage already provides for that category — **mathematical parity**, never new-feature drift.
Every sweep follows the same workflow the lattice sweep established.

**Only [Lattice parity #73](https://github.com/dzackgarza/research/issues/73) blocks the fork track** — it is the extension blocker and the release-gating milestone (tag + release when reached).
The other category branches do not block the fork track.
Their inventories may inform implementation, but their verification issues close only after the corresponding fork-track owner work and native dependencies are complete.

| Parity verification | Implementation owners |
| --- | --- |
| **[Lattice parity #73](https://github.com/dzackgarza/research/issues/73)** — blocker, release-gating: core API ([#21](https://github.com/dzackgarza/research/issues/21), #5 sign, #25 identity), morphism/isometry ([#22](https://github.com/dzackgarza/research/issues/22), #7, #70), module substrate ([#67](https://github.com/dzackgarza/research/issues/67)), parity verification/free-module/FGP ([#26](https://github.com/dzackgarza/research/issues/26)/[#27](https://github.com/dzackgarza/research/issues/27)/[#28](https://github.com/dzackgarza/research/issues/28)), odd genera ([#57](https://github.com/dzackgarza/research/issues/57)), invariants ([#61](https://github.com/dzackgarza/research/issues/61)), notebooks ([#69](https://github.com/dzackgarza/research/issues/69)) | lattice extensions [#68](https://github.com/dzackgarza/research/issues/68) → [#42](https://github.com/dzackgarza/research/issues/42) → [#66](https://github.com/dzackgarza/research/issues/66) |
| [Sets parity #74](https://github.com/dzackgarza/research/issues/74) | [#30](https://github.com/dzackgarza/research/issues/30) own the Set category |
| [Rings parity #75](https://github.com/dzackgarza/research/issues/75) | [#31](https://github.com/dzackgarza/research/issues/31) own Rings & ideals |
| [Groups parity #76](https://github.com/dzackgarza/research/issues/76) | [#34](https://github.com/dzackgarza/research/issues/34) own the Groups category |
| [Algebras parity #77](https://github.com/dzackgarza/research/issues/77) | [#40](https://github.com/dzackgarza/research/issues/40) algebras (graded/dg) |
| [Schemes/varieties parity #78](https://github.com/dzackgarza/research/issues/78) | [#38](https://github.com/dzackgarza/research/issues/38) R-schemes / varieties |

### 🟩 Fork / extension — new mathematics beyond Sage ([#72](https://github.com/dzackgarza/research/issues/72))

A separate track that **imports** the base spike and begins only after the base is frozen, tested in live research, and at parity.
Each engine graduates through an interactive, cited, user-reviewed session.
The GitHub issue tree and milestones are the roadmap surface; the implementation record lives in the private vault plan `PLAN-lattice-feature-spike`. Native GitHub dependencies, rather than this narrative projection, define blocker direction.

| Fork scope | Plan / ownership |
| --- | --- |
| [#68](https://github.com/dzackgarza/research/issues/68) bilinear/quadratic FGP R-modules (beyond ℤ; [#33](https://github.com/dzackgarza/research/issues/33)/[#41](https://github.com/dzackgarza/research/issues/41)) | form-generalization item |
| [#42](https://github.com/dzackgarza/research/issues/42) base-change / ZZ_p / Dedekind functors ([#29](https://github.com/dzackgarza/research/issues/29)/[#32](https://github.com/dzackgarza/research/issues/32)) | `feature-base-ring-generalization-padic-dedekind` |
| [#66](https://github.com/dzackgarza/research/issues/66) Nikulin embeddings / complements / invariant sublattices | `feature-nikulin-primitive-embeddings` |
| [#58](https://github.com/dzackgarza/research/issues/58) external catalogue fixtures and named-lattice proof data, after #66 | public issue grouping; native dependency on #66 |
| [#60](https://github.com/dzackgarza/research/issues/60) lattices from varieties/schemes, [#63](https://github.com/dzackgarza/research/issues/63) AEGS23 | geometry payload → GOAL.md |
| [#45](https://github.com/dzackgarza/research/issues/45) category ownership (Sets/Rings/Groups/schemes/algebras), [#62](https://github.com/dzackgarza/research/issues/62) viz | post-parity trajectory |

## Guiding philosophy

- **Define the general theory, recover special cases.** Objects are stated at the general level (R-lattices; bilinear/quadratic FGP R-modules with free=lattice, torsion=discriminant form) and special cases (ℤ, ZZ_p, O_K, free, torsion) recovered by axiom-gated specialization — never scoped to a specific instance or acceptance-criteria checklist.

- **Correct foundations first.** Sign convention, equality, morphism/hom semantics, and the module/form poset are pinned early because threading them through established code later is expensive.
  This investment buys cheap uniformity, not more refactors.

- **Own thin nodes early.** Owning attachment points (Sets/Modules) so new methods hang at the right poset level is separate from the later refactor that lifts existing methods up.

## User-story proof

The maintained proof that the researcher-facing foundation does not drift is a suite of **notebooks reproducing published results** (Nikulin, Sterk, Dolgachev–Kondō, AEGS23) using only the public generator-first DSL, wired into CI ([#69](https://github.com/dzackgarza/research/issues/69)). Every foundational change must keep these end-to-end arguments green; each new lattice-theory milestone adds at least one reproduced argument.
The downstream research target is the Coble/Enriques moduli program in `projects/lattice-research/GOAL.md`.
