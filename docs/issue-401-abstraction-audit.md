# Mathematical ownership audit for research #401

This audit covers the [issue body and all comments](https://github.com/dzackgarza/research/issues/401), including the frozen API, affine shells, and affine-line points. It determines the mathematical constructions required before further implementation. It does not authorize implementation where the formal declaration or the contract remains unresolved.

The governing rules are [mathematical dependency tracing](../CONTRIBUTING.md#mathematical-dependency-tracing), `OWN-01`, `OWN-04`, `OWN-08`, and `OWN-14`. Mathematical authority belongs to `lean-categories`. A proposed mathematical owner below is not a new local declaration of that authority.

Source snapshot for the implementation findings: research `9e448424e5`; lean-categories `aca89befcd1ade794aa3b7a93f320de995c7a5bc`. Contract reconciliation uses research #401, updated `2026-10-08T17:38:15Z`, including its comments. Port implementation evidence uses the previously inspected `b3fd95d` source and the local `research-401-primitives` branch. The live [migration procedure in #396](https://github.com/dzackgarza/research/issues/396) instead pins `709f81a`, freezes names through port #33, and says to leave the port unchanged. That procedure governs subsequent work. The local port branch is not the migration authority.

## Conclusions

The issue does not call for a collection of independent lattice helpers. Its shared constructions are:

- module morphisms, images, kernels, inverse images, and fibres;
- scalar restriction, scalar extension, and chosen integral submodules;
- bilinear and quadratic forms, restriction of forms, orthogonal complements, and isotropic quotients;
- chosen orthogonal decompositions with inclusions, projections, and comparison isometries;
- group actions, generated submodules, orbit quotients, and torsors;
- sublevel sets of positive forms and their intersections with discrete lattices.

Named lattice operations specialize these constructions. Coordinate matrices, chosen bases, finite search bounds, and backend applicability belong to realizations. They do not determine the mathematical domain or result type.

Several frozen rows need a mathematical clarification through port #33: unconditional integral partners, arbitrary invariant overlattices, affine parameter kernels, lift torsors, and the distinction between a norm fibre and its orbit quotient. The recorded amendments already specify the similarity denominator factor and the signed shell/sphere contracts. The names are not silently replaced while the remaining questions are resolved.

## Formal dependency paths and evidence

The paths below give the shared foundation for the operation-by-operation audit. Paths into lean-categories are relative to this document.

| Key | Formal source inspected | What it supplies; coverage limit |
| --- | --- | --- |
| F0 | [Modules/Mathlib.lean](../../gitclones/lean-categories/LeanCategories/Modules/Mathlib.lean), `ModulesOf`, `modulesToSets`; [Foundation/Sets.lean](../../gitclones/lean-categories/LeanCategories/Foundation/Sets.lean) | Fixed-ring module categories and forgetful maps to types/sets; finite, countable, and enumerated sets remain distinct. Morphisms have endpoints and composition. An enumerable presentation is additional data. |
| F1 | [Modules/Total.lean](../../gitclones/lean-categories/LeanCategories/Modules/Total.lean), `ModulesOverRings`, `fibreInclusion`, `reindex`, `reindex_eq` | The category over rings and restriction of scalars. Same-ring kernels, images, sums, and inverse images live in a fibre. Scalar extension uses the imported change-of-rings theory. This does not by itself identify a particular integral submodule of a rational space. |
| F2 | [Modules/Bilinear/Valued/Fixed.lean](../../gitclones/lean-categories/LeanCategories/Modules/Bilinear/Valued/Fixed.lean), `bilinearForms`, `BilinModuleCat`, `form`, `underlyingMap`; [Isometry.lean](../../gitclones/lean-categories/LeanCategories/Modules/Bilinear/Valued/Isometry.lean) | A form is a map from a tensor square to a value module. Its category is built from that form functor. A form-preserving arrow retains the underlying map and pairing equation. Invertibility is extra structure. This separates formed modules from their finite/projective/free refinements. |
| F3 | [Lattices/Valued/Arithmetic.lean](../../gitclones/lean-categories/LeanCategories/Lattices/Valued/Arithmetic.lean); [Constructions.lean](../../gitclones/lean-categories/LeanCategories/Lattices/Valued/Constructions.lean), `IsIsotropic`, `divisibility`, `scaleLattice`, `gramMatrix` | Finite/projective/free hypotheses; the zero-self-pairing predicate; divisibility as the image ideal of a pairing functional; form scaling; coordinates in a selected basis. A predicate is not an algorithm selecting a witness. |
| F4 | [OrthogonalSplitting.lean](../../gitclones/lean-categories/LeanCategories/Lattices/Valued/OrthogonalSplitting.lean), `isCompl_span_anisotropicComplement`; [ReflectionGeneration.lean](../../gitclones/lean-categories/LeanCategories/Lattices/Valued/ReflectionGeneration.lean), `extendComplementEquiv_isometry`, `extendOrthogonal` | Splitting off a nonisotropic line over a field and extending a complement automorphism while fixing that line. The inspected extension theorem fixes one ambient space and vector. The two-endpoint extension and its integral descent need their own explicit comparison with this construction. |
| F5 | [Modules/Bilinear/Valued/Witt.lean](../../gitclones/lean-categories/LeanCategories/Modules/Bilinear/Valued/Witt.lean); [Lattices/Valued/Witt.lean](../../gitclones/lean-categories/LeanCategories/Lattices/Valued/Witt.lean), `HyperbolicSummand`, `WittDecomposition` | Orthogonal submodules, hyperbolic forms, and chosen decompositions with actual isometries. The inspected hyperbolic decomposition structures are over fields. They do not establish the integral divisibility-one splitting theorem or the full degenerate-hyperplane extension contract. |
| F6 | [Modules/Bilinear/Valued/ChangeValue.lean](../../gitclones/lean-categories/LeanCategories/Modules/Bilinear/Valued/ChangeValue.lean), `changeValue`, `changeValue_id`, `changeValue_comp` | Postcomposition of a form with a value-module map, including its functorial action. Form scaling is a specialization. A functor preserves isomorphisms; a Python return type that forgets the inverse does not express that fact. |
| F7 | [Lattices/Valued/Equivariant.lean](../../gitclones/lean-categories/LeanCategories/Lattices/Valued/Equivariant.lean), `EquivariantLatticeCat`, `carrierRepresentation`, `groupAlgebraModule`; [Gluing.lean](../../gitclones/lean-categories/LeanCategories/Lattices/Valued/Gluing.lean), `Overlattice`, `IsIntegralSubmodule` | Actions on formed objects, their underlying representations, and integral overlattices with inclusions. Fixed vectors and the smallest submodule generated by an orbit are different constructions. Integral-valuedness is additional to finite generation. |
| F8 | [Lattices/Valued/Signature.lean](../../gitclones/lean-categories/LeanCategories/Lattices/Valued/Signature.lean), `signature`, `signature_eq_of_iso`; [DefiniteIndefinite.lean](../../gitclones/lean-categories/LeanCategories/Lattices/Valued/DefiniteIndefinite.lean) | Inertia and definite/indefinite refinements. These sources do not alone provide the requested signed witness or affine-shell selection declaration. |
| F9 | [CategoryTheory/AffineCombinationMonad.lean](../../gitclones/lean-categories/LeanCategories/CategoryTheory/AffineCombinationMonad.lean); Mathlib [affine subspaces and inverse images](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/AffineSpace/AffineSubspace/Basic.html) | Affine combinations are present locally; Mathlib supplies affine spaces, directions, and inverse images. The declaration connecting the requested mixed-scalar integral fibre to this structure remains to be located or supplied upstream. An affine-combination monad is not already that construction. |
| F10 | [Lattices/Valued/IdealDual.lean](../../gitclones/lean-categories/LeanCategories/Lattices/Valued/IdealDual.lean), `idealDual`, `idealDualMap`, `idealDualInclusion`, `toRationalSpan_mem_idealDual_iff` | The ideal-valued metric dual is the kernel of the pairing map modulo the ideal. The membership theorem identifies its inverse image in the original lattice with vectors whose pairings lie in that ideal. This supplies the formal dependency for row 20. |

Each row below unfolds through these paths: a fibre uses a map and a pullback of sets; its translation action uses a kernel in the same module fibre; a formed subobject pulls back the form along its inclusion; a quotient requires the form to descend; an orbit quotient retains the action and its equivalence relation. Finite lists are realizations of these objects only when the relevant finiteness is established.

The formal availability boundary is explicit: the files above were inspected, and declaration/name searches covered `LeanCategories/Modules` and `LeanCategories/Lattices`, with a broader search for isotropic reductions, Eichler transvections, affine subspaces, content ideals, and Witt extensions. These searches locate partial foundations. They do not establish global absence from Mathlib or all imported theories. An unresolved declaration mapping below blocks implementation of that mathematical addition; it is not permission to define it in research.

## Complete operation audit

Throughout this audit, the issue's square convention is `q(x)=b(x,x)`. Characteristic-two quadratic refinements are not interchangeable with this convention. Choosing a witness, partner, basis, or base point is additional data, not a canonical invariant.

### 1. Isotropic witness — frozen `L.isotropic_vector()`

**Owner:** the nonzero zero fibre of a quadratic form, with a witness-selection operation on that represented locus. Integral lattices specialize this after scalar extension to their rational quadratic space.

**Contract:** retain the quadratic space, its form, the selected nonzero vector, and the integral inclusion when an integral vector is requested. Over a finite free integer lattice, denominator clearing followed by primitive normalization raises a rational witness. In a degenerate space a radical vector is a valid isotropic witness, but it is insufficient for splitting off a nondegenerate hyperbolic plane.

**Trace:** F0 → F1 → F2 → F3. The zero-fibre predicate is present; the exact formal witness operation and its failure contract need mapping. `qfsolve` is the private realization over rational coefficients. The local `isotropic_vector_witness()` changes both the frozen name and the anisotropic failure behavior and cannot stand as the agreed public entrypoint.

### 2. Vector content — frozen `v.content()`

**Owner:** the order ideal of an element of a module, obtained from evaluation `M* → R`, `f ↦ f(v)`. On a finite projective module this gives the intrinsic ideal represented by the coordinate ideal in a basis. The nonnegative integer generator is a specialization for free integer modules.

**Contract:** separate the ideal from a normalized generator and from division by that generator. The zero vector has content zero under the ideal convention; the literal maximum of positive divisors of zero does not exist. Primitive normalization of zero is undefined. A form plays no role.

**Trace:** F0/F1 → internal Hom/dual → evaluation → image ideal → normalized principal generator. The module/dual foundations are present; the order-ideal declaration and its comparison with the free-coordinate realization remain unresolved. The added `FramedFreeModules.ElementMethods.content()` is a coordinate realization, not evidence that framing is the semantic owner. Infinite free modules require a separate comparison using finite support, rather than an unqualified finite-projective argument.

### 3. Bezout partner — frozen `v.bezout_partner()`

**Owner:** lifting a generator of the image of a linear functional. For a formed module, compose its correlation map with evaluation at `v` to obtain `b(v,-): M → R`.

**Contract:** over a PID with a selected generator `d` of the image ideal, return an element of the fibre over `d`. The full fibre is a torsor under the kernel. Over `ZZ`, choose `d ≥ 0`. For `d=0`, zero is a permissible selected lift. Over a nonprincipal image ideal, a single generator and hence this scalar-returning contract need not exist.

**Trace:** F1/F2/F3 → image factorization → fibre and kernel. `divisibility` is already an image ideal in F3. Generic image lifting owns the computation; a lattice-local xgcd loop duplicates that responsibility. The added method and the rational Witt consumer must use the same general lift construction once its presentation is available.

### 4. Integral hyperbolic partner — frozen `v.hyperbolic_partner()`

**Owner:** the integral point locus cut out by `b(v,w)=d` and `q(w)=0`, where `d` generates the pairing ideal. This is a quadratic locus inside an affine linear fibre, not another linear solver.

**Contract:** retain that locus and distinguish an empty locus from an unavailable computation. Primitivity alone does not imply a point exists. In the even lattice with Gram `[[0,2],[2,2]]`, `v=e` is primitive and has divisibility two. Minimal pairing forces `w=a e+f`, with square `4a+2`, so no integral partner exists. For an even integer lattice and divisibility one, any Bezout partner `h` gives `w=h-q(h)v/2`.

**Trace:** row 3 → affine fibre → quadratic restriction → integral points; F2/F3/F5. The general integral-point construction and the integral splitting theorem need explicit upstream declarations. The added correction method handles a sufficient case; failure of that correction does not decide the whole locus. The unconditional frozen row requires clarification through #33.

### 5. Integral hyperbolic splitting — frozen `R.integral_hyperbolic_splitting()`

**Owner:** a chosen orthogonal summand, specialized to an even integer lattice with a specified primitive isotropic line generated by `e` of divisibility one.

**Contract:** the reduction retains `I → I-perp → L`, the quotient map `I-perp → I-perp/I`, and its descended form. A selected partner gives `L ≅ U ⊥ K`; the result must compare `K` with the given reduction and retain both summand inclusions/projections. The frozen arrow points from `L` to `U ⊕ K`. A rational decomposition or an isomorphic abstract complement without that comparison is insufficient.

**Trace:** row 4 → formed restriction and quotient → F5 chosen decomposition → direct-sum maps. Field-valued `HyperbolicSummand` is partial formal coverage. The integral theorem and reduction comparison are still required. The general owner is the chosen decomposition, with the reduction as the named entrypoint.

### 6. Recovering two hyperbolic planes

**Owner:** repeated chosen orthogonal decomposition, using row 5 at each stage. A two-plane or Eichler model contains this decomposition; it does not independently compute another lattice and attach splitting labels.

**Contract:** return a chosen isometry and its summand maps for `L ≅ U ⊥ U ⊥ K`. Finding a suitable divisibility-one isotropic vector is a separate integral existence/search problem. A rational witness with larger divisibility does not refute the existence of a splitting. A construction from a supplied complement is not recovery from an arbitrary Gram presentation.

**Trace:** rows 1, 4, 5, with the integral hypotheses retained at both stages. The local `two_hyperbolic_plane_splitting()` bypasses the requested reduction-owned splitting and does not supply the general existence search. Its `TwoUEichlerModel` source is a downstream specialization, not the owner of an orthogonal decomposition. The scrambled `2U + E8(-1)` specimen does not settle that abstraction.

### 7. Affine integral solution locus — frozen `family.integral_members()`

**Owner:** inverse image of a chosen integral submodule under an affine map, after restricting scalars. For `F: P → V`, `F(p)=c+A(p)`, and `j: M → Res(V)`, the object is the pullback of `F` and `j` on underlying affine sets.

**Contract:** when nonempty, retain a selected point, the homogeneous group `A^-1(M)`, its action, and the maps to parameters and integral values. It is a coset of a module, but that module need not be a finitely generated lattice. For `A(s,t)=s+t`, the homogeneous group is `ZZ*(1,0)+QQ*(1,-1)`. An injective rational parameter map into a finite-dimensional rational space gives the finite-lattice case. A solver must not drop the rational kernel.

**Trace:** F0/F1/F9 → scalar restriction → inverse image → affine fibre and kernel action. Existing single-preimage and finite-span operations are partial presentation capabilities. A general mixed-scalar affine fibre has not been identified in the inspected sources. Smith form/Hermite form and CRT are private realizations of the appropriate linear/integral pieces, not definitions of the object. A named affine-family wrapper with only a particular matrix is insufficient.

### 8. Equation `XA + A-transpose X-transpose = B`

**Owner:** a fibre of a linear map between modules of maps/forms. With explicit finite framings, the displayed map is `X ↦ XA+(XA)^t`; without framings, use duality and a correctly typed symmetrization into bilinear forms. An unframed map `V → W` does not canonically identify either space with its dual.

**Contract:** preserve the coefficient map, parameter module, target module, right-hand side, full affine fibre, and homogeneous kernel. Integral solutions are the intersection of that fibre with a chosen integral parameter module, not merely the integral homogeneous kernel. Commutativity suffices for matrix linearity; division by two is not allowed over arbitrary rings.

**Trace:** F1/F2 → Hom modules and duality → linear map → row 7. The added `symmetrized_right_multiplication()` exposes a based linear operator and is useful as a realization/composite. It is not the shared solution-space abstraction, and `preimage(B)` returns only one point. Matrix coordinates must remain a selected presentation of the general construction.

### 9. Invariant overlattice — frozen `G.invariant_overlattice(L)`

**Owner:** the submodule generated by the orbit of a submodule under a represented linear group action: `sum(g(L), g in G)`, equivalently the image of the group-algebra-generated module. The action `G → Aut(V)` and the inclusion `L → Res(V)` are required data.

**Contract:** the result has its inclusion, induced action, and least-stable-submodule property. Finite generation is not implied by commensuration: `diag(2,1/2)` on `U_Q` generates `ZZ[1/2]^2` from `ZZ^2`. A finite group or a supplied finite stable containing module gives a finite-generation route. Integral-valuedness of the restricted form remains a separate condition. The order-two isometry `e ↦ 2f, f ↦ e/2` gives the finite span `ZZ*(e/2)+ZZ*f`, whose cross-pairing is `1/2`; it has no integral-valued overlattice containing it.

**Trace:** F1 → group representation/group algebra (F7) → generated submodule → formed restriction (F2) → lattice/integrality refinements (F7). The inspected equivariant lattice owner supplies an action on an already integral object; that is not this closure construction. The frozen row needs existence and value-module hypotheses. Repeated spans until stabilization are not a definition or a termination proof.

### 10. Nonisotropic perpendicular extension — frozen `phi.extension_across(v,w)`

**Owner:** extension of an isometry between orthogonal summands, composed with chosen orthogonal decompositions. Over a field, a vector of nonzero square splits off its line. An isometry of the complementary spaces together with `v ↦ w` extends uniquely when their squares agree.

**Contract:** retain both perpendicular inclusions and both ambient spaces. The partial isometry need not have subobjects as literal Python endpoints if explicit embedding data is supplied. Scalar extension supplies the rational ambient extension; integral descent is row 12. Definiteness belongs only to an algorithm enumerating the complement isometry torsor.

**Trace:** F2/F4 → direct-sum isometry → composition with decomposition isometries → F1 descent. The local `extend_from_perpendicular()` uses the right formula but selects another name, requires endpoint `.inclusion()` methods, and lacks a retained general decomposition. The inspected formal automorphism extension does not alone discharge the two-endpoint generalization.

### 11. Codimension-one Witt extension — frozen `phi.witt_extension(source_inclusion,target_inclusion)`

**Owner:** extension of a partial isometry along specified formed embeddings. The isometries of the ambient objects with the required restriction form a fibre of the restriction operation; a selected extension is a point of this fibre.

**Contract:** distinguish a degenerate hyperplane in a nondegenerate ambient quadratic space from an ambient space with radical. Over a field of characteristic different from two, a hyperplane with one-dimensional radical inside a nondegenerate space admits the usual Witt extension. If the ambient form is degenerate, compatibility with the ambient radicals is necessary; the former theorem must not be applied unchanged. Preserve the square formed by the inclusions and extension.

**Trace:** F2 → restriction of isometries → orthogonal complement/radical → extension theorem. The inspected formal sources provide vector reflection transitivity, cancellation, and nonisotropic complement extension, not an identified declaration for this full contract. The port's norm correction requires a nonzero pairing with a complementary vector and therefore cannot establish the unrestricted degenerate-ambient claim. Resolve the ambient hypotheses and formal theorem before migration.

### 12. Integral descent — frozen `M.integral_isometry(phi)` and `phi.is_integral_on(L)`

**Owner:** factorization through specified integral subobject inclusions under scalar extension. For `j_L: L → V`, `j_M: M → W`, factor `phi*j_L` through `j_M`. This gives an integral map. Factor the inverse too to obtain an isomorphism.

**Contract:** retain `j_L`, `j_M`, and the commuting square. The source integral structure must be explicit or retained in the scalar-extension datum; a bare rational space does not determine it. Mapping `L` into `M` and mapping `L` onto `M` are different predicates. The frozen isometry constructor raises if equality fails. Integrality on a lattice needs a declared target integral structure.

**Trace:** F1 → subobject factorization → F2 structured map → core/isomorphism. The local `integral_restriction(source,target)` correctly considers both directions but is a lattice-specific coordinate implementation with another name and failure result. General module-map descent owns the arithmetic; form preservation is transported through the commuting square.

### 13. Clearing denominators of a rational isometry — frozen `phi.integral_similarity(L,E)` and `.scale()`

**Owner:** the denominator ideal of a rational module map relative to integral structures, followed by scalar multiplication of the map and transport of its form equation. Over `ZZ`, this ideal has a least positive generator `N` for finite-rank full lattices.

**Contract:** retain the map `sigma=N*phi`, its finite-index image, the denominator factor `N`, and its form multiplier `N^2`. Indeed `b_E(sigma x,sigma y)=N^2*b_L(x,y)`. These are different scalars. `sigma` is generally an embedding, not an isomorphism onto `E`. On `U`, `phi=diag(2,1/2)` has `N=2`; `sigma=diag(4,1)` has index four and form multiplier four.

**Trace:** F1 → Hom and integral subobjects → denominator ideal → F2/F6 form comparison. The current `L.similarity_mor(E,a)=L.twist(a).Isom(E)` supplies only surjective similarities and is insufficient for this request. The [frozen amendment](https://github.com/dzackgarza/research/issues/401#issuecomment-6065197711) specifies `.scale()` as the least denominator factor `N`; the form multiplier is `N^2`. The general denominator-ideal declaration and similarity-embedding presentation remain required.

### 14. Twist functor on isometries

**Owner:** change of value of a formed object, by multiplication on its value module. Restrict this functor to the relevant lattice category and its core of isomorphisms.

**Contract:** transport both a map and its inverse; preserve composition. Scaling twice has the comparison with scaling by the product. For the sign twist, the requested Python identity `L.twist(-1).twist(-1) is L` additionally requires constructor normalization of this action. Mathematical functoriality alone does not imply object identity in Python. Nonzero versus invertible scaling must be separated when claiming an equivalence over a general ring.

**Trace:** F2 → F6 `changeValue` and its identity/composition laws → core functor → chosen presentation normalization. `TwistFunctor._apply_morphism` currently calls `source.Mor(target)`, forgetting the isomorphism specialization. Repair belongs to value-change transport and its restriction, not a port-specific matrix retargeting method.

### 15. Lifts through isotropic reductions — frozen `R.rational_lifts(target,psi)`

**Owner:** a fibre of the map from isometries preserving marked isotropic data to isometries of the reductions. When nonempty this fibre is a torsor under the kernel of the restriction/reduction action.

**Contract:** specify the map on the isotropic line as well as on the reduction. For a marked isotropic vector in a nondegenerate rational space of dimension `n`, the relevant kernel is the additive unipotent group of dimension `n-2`. Preserving only the line leaves an additional scaling parameter. Higher-dimensional isotropic subspaces need their own kernel group and cannot inherit the rank-one dimension formula.

The parameter space can be affine while its evaluation in the space of matrices is nonlinear. For `U ⊥ <2>` with basis `e,f,a`, the standard transvection with parameter `t*a` sends `f` to `f+t*a-t^2*e`. The midpoint of the matrices at `t=1` and `t=-1` sends `f` to `f-e`, of square `-2`; it is not an isometry. Thus an affine-linear expression `T0+sum(lambda_i*Ti)` does not represent this lift torsor. The transvection formula and additive parameter law are given in [Gritsenko–Hulek–Sankaran, §3.1, equations (4)–(5)](https://archive.mpim-bonn.mpg.de/3203/1/preprint_2008_114.pdf). The midpoint calculation is a direct consequence.

**Trace:** F2/F5 → isotropic quotient and parabolic action → kernel group → torsor and evaluation → row 12 for integral members. A chosen `.base_point()` trivializes the torsor; it does not replace its action or parameters. Integral members, when nonempty, are a torsor under the subgroup of integral kernel elements. Identifying that subgroup with an additive lattice needs a theorem. The existing finite `Torsors` constructor in `group/g_sets.py` does not yet present this rational parameter torsor. A torsor with an empty list of directions has not supplied the requested object.

### 16. Signature-defined directions — frozen `L.positive_vector()`, `S.vector_of_sign(sign)`

**Owner:** witness selection in a signed locus of an ordered-field-valued quadratic form. For a subspace, first restrict the form along its retained inclusion.

**Contract:** a nonzero vector with the requested strict sign, or the declared absence result; return an element of the specified subspace with its ambient inclusion available. Ordering, or a chosen real place for a number field, is part of the input. Signature can decide existence in a finite-dimensional setting but does not itself choose a vector.

**Trace:** F1/F2 → restriction → ordered value predicate → F8 existence → witness. Rational diagonalization is a private realization. The local positive/negative methods expose lattice conveniences; the general signed-locus operation and the frozen subspace method still need their formal and presentation mapping.

### 17. Binary fixed-norm representations — frozen extension of `L.vectors_of_square(n)`

**Owner:** the norm fibre as a `G`-set, followed by its orbit quotient for an explicitly selected subgroup of the orthogonal group. Chosen representatives and transporters are data over that quotient.

**Contract:** distinguish all vectors in the fibre from one vector in each orbit. A definite shell currently returns vectors; replacing its meaning by orbit representatives only in the indefinite case is not a signature-based specialization of the same object. Distinguish `O`, `SO`, primitive vectors, and all vectors. A generator of the infinite cyclic part is not the whole automorphism group. At norm zero a split binary lattice has infinitely many content classes unless primitivity is imposed.

**Trace:** F0/F2 → norm fibre → represented action (F7) → orbit equivalence relation and quotient → representative section. Binary reduction cycles and PARI are realizations. The added nonsplit-only `binary_fixed_norm_representatives()` neither supplies the frozen API nor the retained action/quotient/automorph data. Resolve the frozen shell-versus-quotient type through #33; do not hide the difference in a finite-set return value.

The current issue body distinguishes the cases explicitly: `vectors_of_square(n)` returns all vectors for a split binary form and `n != 0`; `primitive_isotropic_vectors()` returns the primitive vectors on its isotropic lines; `reduction_cycle(bound,start)` returns the cycle automorph as an isometry and the bounded vectors met in one period, or `None`, for an anisotropic binary form. The older frozen table instead assigns orbit representatives to `vectors_of_square(n)`. Resolve this disagreement through #33. The cycle operation also retains its primitive positive starting vector and the action of the returned automorph; a norm-fibre quotient alone does not specify a reduction cycle.

### 18. Affine close-vector shells — frozen shell methods with a multiplier bound

**Owner:** intersection of an affine quadratic sublevel set with a discrete lattice, and an indexed family of such intersections. The least successful multiplier is a selection from the index set of nonempty fibres.

**Contract:** the [shell amendment](https://github.com/dzackgarza/research/issues/401#issuecomment-6065258075) specifies a definite form of either sign, with `B` of that sign. Retain `K`, its rational ambient space, target `t`, and the fibre `{x in K : min(0,m^2*B) <= q(x-m*t) <= max(0,m^2*B)}`. The sphere fibre has equality `q(x-m*t)=m^2*B`. `first_close_vector_shell(t,B,M)` and `first_close_vector_sphere(t,B,M)` return the least successful `1 <= m <= M` and that fibre, or `None`. Exhausting the bound decides only that bounded search. The fixed-m shell is `close_vectors(m*t,m^2*B)`. A denominator `D` with `D*t in K` supplies an unrestricted shell point at `m=D`; it supplies a sphere point by this argument only when `B=0`.

**Trace:** F0/F1/F2/F8 → signed sublevel or level locus → lattice intersection → indexed family → bounded minimum selection. The fixed-`m` shell is the shared operation. The local `first_close_vectors`/`affine_close_vectors` select other names and omit the frozen search bound. Supply both bounded selections through their respective fibres and the existing fixed-m shell entrypoint. The signed convention is settled by the amendment; the formal locus and selection mappings remain required.

### 19. Integral points on an affine line — frozen `L.affine_line_points(base,direction)`

**Owner:** row 7 specialized to the affine map `lambda ↦ base+lambda*direction`, followed by its image in the ambient rational space.

**Contract:** with nonzero rational direction, the integral point set is empty or an affine rank-one lattice; retain its inclusion and a chosen point and primitive integral step. For zero direction, the point set is empty or a singleton, while the parameter preimage is empty or all of `QQ`. Those are different objects. A pair of vectors is useful presentation data only when attached to the appropriate affine point set.

**Trace:** F1/F9 → row 7 → image and retained parameterization. This is not a separate coordinate congruence algorithm on lattices. The affine fibre must exist first.

### 20. Divisibility sublattice — requested `L.divisible_sublattice(d)`

**Owner:** inverse image of an ideal-valued metric dual along the integral inclusion into the rational span. For `j: L -> L_Q` and `I=(d)`, form the pullback of `idealDual(ZZ,L,I) -> L_Q` along `j`.

**Contract:** return the formed submodule `D` of `L` with its inclusion `i: D -> L`, its map `k` to the ideal dual, and the commuting equation `j*i = idealDualInclusion*k`. Its vectors satisfy `b(v,L) subset d*ZZ`, as requested in the issue body. The definition by inverse image also applies at `d=0`, where it selects the radical. The expression `L intersect d*L^#` needs `d != 0`; at zero it can lose a nonzero radical. The API's permitted values of `d` must be explicit.

**Trace:** F1 → F2 pairing and restriction → F10 ideal dual → inverse image. A concrete formal composite is `Submodule.comap (toRationalSpan ZZ L) (idealDual ZZ L (Ideal.span {d}))`. The theorem `toRationalSpan_mem_idealDual_iff` gives its required membership predicate; `idealDualMap` realizes the ideal dual as a kernel, and `idealDualInclusion` retains its ambient map. This identifies the formal constituents and the membership theorem. Acceptance of that composite as the public operation, its formed-subobject presentation, and the domain of `d` remain to be resolved. The adjacent metric-dual and rank-one-dual theories concern the general dual and rank-one modularity; they do not by themselves register this public operation.

## Private API accesses

The issue's instruction to supply public operations does not authorize exporting engine accessors. The required operation is determined by what a consumer asks the engine to compute.

| Private access | Correct abstraction and retained data | Disposition |
| --- | --- | --- |
| `_engine_polyhedron` | Convex polyhedron/cone in an owned affine/vector space; supporting functionals, face inclusions, intersections, and integral-point loci as requested | Use or extend `polyhedral_cones.py` and its mathematical owners. Keep the Sage polyhedron private. Audit each consumer operation rather than add `engine_polyhedron()`. |
| `_ExactCVPEngine` | Closest-point/closest-value problems and the shell family in row 18 | One private realization behind the mathematical metric/sublevel-set operations. |
| `_rational_positive_vector` | Signed locus of the restricted form, row 16 | Reuse the form restriction and witness selection; no public raw Gram-to-vector function. |
| `_engine_subgroup_from_generators` | Generated subgroup of a represented group, with inclusion and generating family | Generic group owner; `OwnedGroups.ParentMethods.subgroup` is an existing presentation route. This also meets the dependency on #396. |
| `_isometry_from_column_matrix` | A formed-module morphism, and inverse data for an isomorphism; construction in the correct Mor | A based coordinate realization of that arrow. Matrices supplied publicly must themselves be owned morphisms with retained framings. |
| `_row_action_matrix` | Coordinate realization of a linear map between selected frames, with variance/convention fixed | Generic based-module morphism operation. Row versus column conversion stays private to the adapter. |
| `_element_from_coordinates` | Application of a selected framing isomorphism to an element of the free coordinate module | Existing module framing/linear-combination construction; not a lattice-specific public engine converter. |

## Disposition of the code already added

No implementation is accepted merely because it computes a useful specimen. The following changes remain committed; this audit neither rewrites them nor treats them as the definition of the requested objects.

| Added surface | Required architectural disposition |
| --- | --- |
| `content`, `primitive_part` in `framed_free_modules.py` | Establish the intrinsic order-ideal owner and its coordinate comparison; retain the integer normalization as a specialization. |
| `bezout_partner` and the rational Witt edit | Route through the functional image fibre; avoid a separate lattice-owned elimination implementation. |
| `isotropic_vector_witness` and signed witnesses | Preserve the zero/signed loci, scalar-extension relation, and frozen witness contracts. Backend rank/ring limits remain realization limits. |
| `hyperbolic_partner` | Preserve the quadratic fibre and existence conditions; the correction of one Bezout lift is not a general solver. |
| `two_hyperbolic_plane_splitting` | Build through the reduction-owned one-plane split and general chosen orthogonal decomposition, not an Eichler-model-specific constructor. |
| `first_close_vectors`, `affine_close_vectors` | Use the common signed shell family and its sphere fibres; supply the amended names, multiplier bound, and `None` result. |
| Restricted-scalar `subobject_on` | Treat the fractional PID span as a realization of the same generated-submodule construction with inclusion; it is only the finite lattice part of an affine inverse image. |
| `extend_from_perpendicular`, `integral_restriction`, and definite-complement refactor | Use orthogonal decomposition and general integral factorization; reconcile frozen names, endpoints, and failure semantics. |
| `symmetrized_right_multiplication` | Keep the displayed based operator subordinate to general linear-map fibres and integral inverse images. It does not complete the solution-space item. |
| `binary_fixed_norm_representatives` | Supply the norm-fibre action and quotient/representative data; cover the stated binary regimes without changing the shell's meaning. |
| Local port branch `research-401-primitives` | Preserve its commits without further edits or integration. The live migration procedure says the port side already targets the frozen API; research must implement that contract. |

## Unresolved formal and contract work

The ownership decisions above cover every issue item. They do not claim that every needed formal declaration is already available. Before implementation resumes, the selected operation must have its exact declaration or approved formal composite, hypotheses, maps, and presentation identified. The remaining upstream mapping/request subjects are:

- order ideals and normalized content, and generic image-generator fibres;
- mixed-scalar affine inverse images, their rational kernels, and integral descent/denominator ideals;
- integral isotropic reduction and hyperbolic splitting, including its comparison maps;
- two-endpoint partial-isometry extension and the degenerate-hyperplane hypotheses;
- parabolic reduction maps, marked-line data, kernel torsors, evaluation, and integral subgroups;
- orbit-generated modules with finite-generation and integrality hypotheses;
- norm-fibre actions and quotient representations, signed witness selection, and affine shell families;
- similarity embeddings with separate denominator factor and form multiplier, and normalized form-change transport;
- the divisibility sublattice as the inverse-image composite in row 20, with its formed inclusion and the permitted domain of `d`;
- binary reduction cycles with their starting data, period automorph, and bounded vector family.

## Contract decisions required before implementation

The following are proposed resolutions for the frozen-API owner. They preserve the requested mathematical domains where a general construction exists. They require acceptance through [port #33](https://github.com/dzackgarza/sage-indefinite-port/issues/33).

| Contract | Proposed resolution | Remaining decision |
| --- | --- | --- |
| `hyperbolic_partner()` | Select a point of the integral quadratic locus in row 4; return `None` for a proved empty locus and report unavailable computation separately. Use the divisibility-one theorem under its evenness hypothesis. | Approve the absence result. The unconditional successful-return promise is contradicted by row 4. |
| `invariant_overlattice(L)` | Construct the orbit-generated module with its inclusion and action. Return it as a lattice when finitely generated and integral-valued; return `None` when no such lattice exists, and report unavailable computation separately. | Approve this partial existence contract on the original domain. Finite groups or a supplied finite stable containing module give finite-generation cases, with integral-valuedness checked separately. |
| Affine `integral_members()` | Return the full coset under the scalar-restricted inverse-image module, including its rational kernel. | Approve the module-valued result on the original parameter domain. |
| `rational_lifts(target,psi)` | For the rank-one contract, require marked generators `e` and `e'` and lifts sending `e` to `e'`. Return the kernel torsor with nonlinear evaluation and a chosen base point. Its integral members use the integral kernel subgroup. | Approve the marking and torsor result in place of an affine-linear matrix family. |
| Binary representations | Adopt the issue body's separate split norm fibre, primitive isotropic-vector set, and anisotropic reduction-cycle operations from row 17. | Reconcile the frozen orbit-quotient row with that body through #33. |
| `divisible_sublattice(d)` | Use the ideal-dual inverse image in row 20 for integer `d`, including the radical at zero. | Approve the domain and the restriction `d != 0` on the scaled-dual formula. |

The shell/sphere names, signed interval, multiplier bound and bounded-search failure result follow the shell amendment. The similarity `.scale()` follows the denominator-factor amendment. These settled conventions do not require a new choice; their formal mappings and implementations remain separate obligations.

For these subjects, the audit supplies the requested mathematical object and dependency path. Formal availability is unresolved where stated; the inspected declarations are partial capabilities, not a proof of a whole-repository absence. These questions belong to lean-categories and the frozen-API owner, not to new preamble helper classes. Research runtime and correctness acceptance are separate subsequent obligations; this audit performed neither.
