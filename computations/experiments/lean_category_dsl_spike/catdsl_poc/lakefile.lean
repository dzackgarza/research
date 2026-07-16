import Lake
open Lake DSL

package «catdsl_poc» where
  version := v!"0.1.0"

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "v4.32.0"

@[default_target]
lean_lib CatDSL

/--
The worked example and its tests.

Kept out of `CatDSL` so the library stays free of `run_cmd` and `#via`
output, and so a failure here is visibly a failure of the example rather
than of the library.
-/
lean_lib CatDSLTest where
  roots := #[`CatDSL.Example.F2Semantic,
             `CatDSL.Example.RegistryTest,
             `CatDSL.Example.SurfaceTest]
