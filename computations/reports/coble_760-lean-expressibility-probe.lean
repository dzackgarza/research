-- #760, item 3: what a declaration of the semifan statement would have to be built on.
--
-- The theorem of item 1 is a statement about a cosening of a fan of convex cones by the mirrors
-- of a set of "irrelevant" simple roots.  This file asks Lean which of those primitives the
-- installed library supplies, and states the one definition that the concept needs and that no
-- library here has.  Imports are narrowed to the modules that could carry them.
import Mathlib.LinearAlgebra.QuadraticForm.Basic
import Mathlib.Analysis.Convex.Cone.Basic
import Mathlib.LinearAlgebra.Ray

-- the cone primitives, which do exist
#check @ConvexCone
#check @PointedCone
#check @Module.Ray

-- the objects the statement is about, which do not
#check @Semifan
#check @Fan
#check @Chamber
#check @Irrelevant

-- what the statement needs and cannot be written from the above: a coarsening of a fan along the
-- mirrors of a distinguished set of roots, and the relative interior of its cones.  `ConvexCone`
-- is a cone, not a fan, and Mathlib has no face lattice of a fan to coarsen.
def CoarsenedAlong (mirrors : Set (Set M)) (cone : Set M) : Set M := cone
