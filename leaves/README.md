# Research realization leaves

A Lake package of realization leaves hosted by `research`
([`lean-cas-dsl/specs/architecture.md`](https://github.com/dzackgarza/lean-cas-dsl/blob/main/specs/architecture.md)):
each module registers, through `lean-cas-dsl`'s leaf API (`register_leaf`), realizations of
operations already formal in `lean-categories`, and nothing else. No category, method, placement or
semantic row is written here, and none can be.

- `ResearchLeaves/FiniteSets/Forget.lean`: the forgetful functor of finite sets on finite sets
  presented by `n`.
- `ResearchLeaves/Acceptance.lean`: `lean-cas-dsl`'s permanent assertions, rerun unchanged with
  these realizations (`#acceptance_rerun`); the operation surfaces are unchanged and the gaps shrink.

Build with `lake build` (the toolchain and `lean-cas-dsl` are pinned in `lakefile.lean`).
