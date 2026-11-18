-- #760, item 3: which of the notions the statement needs does the installed library carry?
--
-- The import is narrowed to the two Mathlib modules that carry the notions the statement does
-- use, because `import Mathlib` on this machine stalled on cold disk and never reached the
-- checker: the wide claim ("no semifan anywhere in the tree") is the tree search in
-- coble_760-lean-declaration-search-run.txt, which reads all 8311 Mathlib files and all 178
-- CSLib files; this file is the checker's verdict on the names themselves.
import Mathlib.GroupTheory.Coxeter.Basic
import Mathlib.LinearAlgebra.QuadraticForm.Basic
-- carried, at the level the statement needs
#check @CoxeterSystem
#check @CoxeterMatrix
#check @QuadraticForm
#check @LinearMap.BilinForm
-- not carried: the object the statement is about
#check @Semifan
