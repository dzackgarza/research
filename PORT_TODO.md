# Archive Port Outstanding Work

Unresolved semantic-migration work from `archives/preamble/` into
`src/dzack_research/preamble/`. Completed work and standing guidance are omitted.

Execution order is breadth-first: restore broadly useful categorical/module and
scheme/geometry foundations before returning to specialized lattice, orbit, and
Coxeter/Vinberg algorithms. Original section numbers are retained for provenance.

## 8. Remaining module-level algorithms

### 8.2 Presented modules over more general bases

- [ ] Extend Smith/Hermite/presentation operations beyond `ZZ`/fields only where theorem/backend support exists.
- [ ] Extend the now-live rank distinction beyond represented finite modules: `rank_at(p)=dim_{kappa(p)}(M tensor_R kappa(p))`, finite-projective local rank, and generic/Matsumura rank over domains are separate APIs and must remain so. Add rank-function objects/stratifications on `Spec(R)` and locally constant rank for finite projectives; support infinite-cardinal generic rank only when the module/cardinal infrastructure genuinely represents it.
- [ ] Extend the now-live module-localization functor `S^{-1}(-)`, prime localizations `M_p`, localization units, localized morphisms, and fibers `M(p)=M_p tensor_{R_p} kappa(p)` beyond the currently materialized framed/free/finitely-presented scalar-extension regimes. Connect `mu(M_p)=dim_{kappa(p)}M(p)` to an actual minimal-generator/Nakayama API over local rings rather than only returning the fiber dimension numerically.
- [ ] Extend the now-live Fitting ideals/support/rank-threshold loci beyond chosen finite presentations: verify presentation independence through the generic algebra, add `Ann(M)` and the supported equality `Supp(M)=V(Ann(M))=V(Fitt_0(M))`, and use Fitting strata for local-freeness/projective-rank tests and rank-jump loci.
- [ ] Generalize torsion/torsion-free predicates without guessed booleans.
- [ ] Generalize cardinality using the cardinal of the base and actual decomposition.
- [ ] Generalize exponent/annihilator vocabulary only where meaningful; a nonzero free abelian group does not have exponent `1`.

### 8.3 Module automorphism groups/action homsets

- [ ] Audit archived `ModuleAutomorphism`, `ModuleAutomorphismGroup`, `AutomorphismSubgroup`, `SubFramingMorphism` against live generic machinery.
- [ ] Port only missing mathematical operations: actual automorphism groups, subgroup inclusions, sections/retractions/one-sided inverses, and action homsets.

### 8.4 Commutative-algebra foundation required by scheme theory

- [ ] Backend routing policy: keep mathematical objects, inclusions, structure maps, universal properties, and functorial laws in the preamble, but delegate algorithmic engine work to established CAS backends wherever available. Backend-specific matrices/ideals/handles/process protocols remain private and every public result must be crossed back into live owned objects/morphisms/subobjects.
- [ ] Use Sage's native commutative-algebra interfaces, and hence Singular where Sage routes there, for Groebner bases, syzygies, elimination, ideal membership/reduction, saturation/colon computations, dimensions/Hilbert data, polynomial quotient calculations, resolutions, and primary-decomposition/associated-prime computations in the regimes those backends actually support. Do not reimplement these algorithms in Python.
- [ ] Audit Sage's Singular bridge before adding any owned algorithmic code for polynomial/local singularity computations; use direct Singular only when Sage does not expose the needed exact operation cleanly, and keep the direct interface behind one private adapter.
- [ ] Use `libgap`/Sage's GAP-backed parents for finite/combinatorial group calculations, automorphism groups, stabilizers, orbit calculations, and group homomorphism algorithms rather than duplicating GAP algorithms in the preamble.
- [ ] Restore `sage-julia-bridge` as the canonical persistent Julia/OSCAR/Hecke boundary. Instantiate/provision the bridge's Julia project so its declared `JSON` dependency is available, initialize `using Oscar` through the bridge, and make bridge availability a normal backend capability rather than bypassing it.
- [ ] Replace the current raw `julia` subprocess + temporary-matrix-file + stdout-parsing code in `categories/lattice_engines.py` with `sage-julia-bridge` calls/handles and structured Sage<->Julia conversions; preserve the owned row/column/tensor convention checks at the private crossing only.
- [ ] Reuse the bridge's structured integer/rational/vector/matrix codec and opaque `JuliaHandle` support; add conversion registrations to `sage-julia-bridge` when a reusable mathematical Sage<->OSCAR conversion is missing instead of building one-off text protocols in the preamble.
- [ ] Prefer OSCAR/Hecke through `sage-julia-bridge` for lattice/quadratic-form, number-field/order, normalization, and exact algebra computations when it is materially stronger than Sage's native backend; verify returned data at the owned mathematical boundary rather than duplicating the engine algorithm.
- [ ] Treat Macaulay2 as an optional advanced commutative-algebra backend: Sage's M2 interface is present but no `M2`/`Macaulay2` executable is currently provisioned. Once available, use it where it materially improves free resolutions, Betti data, local/cohomological algebra, or primary decomposition instead of recreating those algorithms.
- [ ] Use Maxima only for symbolic-calculus operations it actually owns; do not route exact algebraic ideal/module computations through Maxima merely because the executable is present.
- [ ] Maintain a small backend-capability layer selecting among Sage/Singular, `libgap`, OSCAR via `sage-julia-bridge`, optional Macaulay2, Maxima, and specialized wrappers such as `py_polyhedral`; mathematical code should ask for an operation/capability rather than shelling out to a particular executable itself.
- [ ] Ring/algebra homsets with composition, kernels, images, quotient factorization, and universal properties for quotient/localization maps; use these as the source of contravariant affine scheme morphisms.
- [ ] General owned ideals beyond the current `ZZ`/number-order module adapter: finitely generated ideals in polynomial, quotient, localization, power-series, and local rings, with inclusions and quotient modules/rings.
- [ ] Ideal arithmetic: sum, product, intersection, powers, extension/contraction along ring maps, colon/saturation where supported, radicals, nilradical/Jacobson radical, and exact prime/maximal predicates.
- [ ] Noetherian ideal theory: associated primes, primary decomposition, minimal primes, irreducible components, support, and annihilators/Fitting ideals of finitely generated modules.
- [ ] Prime spectrum as an actual set/poset of prime ideals where representable, with specialization order and Zariski closed sets `V(I)`, distinguished opens `D(f)`, radical-ideal/closed-set correspondence, generic points in supported Noetherian cases, and maximal spectrum where useful.
- [ ] Extend localization beyond the now-live submonoids `S <= (R, ·)`, represented ring localizations, module localization functor, localization units, and localized morphisms: universal factorization for arbitrary represented `S`, extension/contraction of ideals, localization of quotient rings, arbitrary-module materialization, and exact-sequence preservation/exactness laws. Principal localization uses `<f>` and prime localization uses `R \ p` as actual submonoids.
- [ ] Local homomorphisms and local-ring structure beyond the initial principal examples: maximal ideal/residue field compatibility, localization at arbitrary represented primes, units/nonunits, and Artinian local quotient examples.
- [ ] Nakayama's lemma and its standard computational consequences for finite modules over local rings: minimal generators, surjectivity/isomorphism tests modulo the maximal ideal, and cotangent-space calculations.
- [ ] Extend the now-live residue maps `R -> R_p -> kappa(p)` and module fibers beyond the current domain/prime-localization regime to arbitrary represented commutative rings and primes; test localization/base-change squares and reuse the same residue-field object for scheme stalks, cotangent spaces, and module fibers.
- [ ] Noetherian modules and exact finite-presentation machinery over polynomial/quotient/local rings using Sage/Singular/Groebner backends; do not force PID Smith-form semantics outside their valid range.
- [ ] Flat and faithfully flat modules/algebras, exactness of localization, finite projective/locally free criteria, and the local criterion for flatness in the exact regimes needed by base change and fibers.
- [ ] Finite/integral ring extensions, integral dependence, finite algebras/modules, lying-over/going-up/incomparability where applicable, integral closure/normalization, and conductor ideals; connect normalization to curves/schemes later.
- [ ] Krull dimension, chains/heights of primes, principal ideal theorem and basic dimension formulas in supported Noetherian finite-type regimes; codimension should use height when ambient-dimension subtraction is not justified.
- [ ] Zero-dimensional/Artinian structure and Chinese-remainder decompositions, local Artinian factors, nilpotence of the Jacobson radical, and length of finite modules where exact.
- [ ] Adic topology beyond the initial completion objects: powers `I^n`, inverse systems `R/I^n` and `M/I^nM`, separatedness/completeness, Krull intersection, Artin--Rees, completion of finite modules, exactness/flatness statements under Noetherian hypotheses, and compatibility with quotients.
- [ ] Treat finite-precision `p`-adic/power-series backends explicitly as computational realizations of abstract completions rather than identifying precision with the mathematical completion object.
- [ ] DVR/valuation-ring basics needed for local geometry: uniformizers, valuations, residue fields, completions, discrete valuation criteria, and order-of-vanishing computations in the supported PID/Dedekind/function-field examples.
- [ ] Extend the now-live finite-presentation commutative-algebra coproducts `A tensor_R B` and pushouts `B tensor_A C` to broader represented algebras; add categorical pullbacks of commutative rings/algebras where needed and complete the expected base-change/associativity laws.
- [ ] Extend module base change/localization beyond the current framed/free/finitely-presented materializations, prove/test localization exactness and compatibility with kernels/cokernels in supported Noetherian regimes, and add enough `Tor`/`Ext` for local intersection multiplicity and basic deformation/cotangent examples; the scalar-extension/restriction adjunction and first-class localization specialization are already live.
- [ ] Kähler differentials over general commutative algebras integrated with quotients/localization/base change; exact conormal sequence, derivations, `m/m^2`, Zariski cotangent/tangent spaces, and Jacobian matrices in finite-type presentations.
- [ ] Graded commutative algebra needed for `Proj`: homogeneous ideals, irrelevant ideal, graded localization and degree-zero parts, homogeneous quotient rings/modules, and standard affine charts.
- [ ] `A^n_R = Spec(R[x_1,...,x_n])` derived through affine `Spec`, with functor-of-points `A^n_R(S)=S^n`; similarly derive affine closed subschemes from quotient algebras.
- [ ] `Proj` sufficient to derive `P^n_R = Proj(R[x_0,...,x_n])`, its standard affine cover, and its functor-of-points interpretation rather than only adopting Sage's ambient projective-space object.
- [ ] Presheaves/sheaves on a basis sufficient for affine schemes: restriction maps, sheaf condition on represented finite distinguished-open covers, sheafification where needed, and direct-limit stalks.
- [ ] Structure sheaf on `Spec(R)` from `D(f) |-> R_f`; stalk `O_{Spec R,p}=R_p`; principal/basic opens from localization; affine quasi-coherent sheaves from modules with `M~(D(f))=M_f` and exact localization/restriction laws.
- [ ] Only after the preceding affine/local algebra is live, use stalks/localizations for regularity, regular local rings, smoothness/Jacobian criteria, local intersection multiplicity, and singularity computations.

## 9. Scheme and algebraic-geometry foundation

### 9.1 Ringed spaces and schemes

- [ ] Extend the now-live affine stalks `O_{Spec R,p}=R_p` beyond the current domain/prime-localization regime and integrate them with general ringed-space/local-intersection constructions.
- [ ] Populate exact generic membership/refinement for quasi-affine, quasi-projective, integral, separated, finite-type, normal, and smooth scheme properties beyond the currently placed base/affine/projective spaces.

### 9.2 Subschemes

- [ ] Integrate closed-subsheme inclusions with the generic `SubobjectCategory`; native equation-defined closed embeddings already land as live scheme morphisms.
- [ ] Open subschemes as actual open immersions/subobjects.
- [ ] Principal/basic opens.
- [ ] Scheme-theoretic intersections.
- [ ] Intersection multiplicity from correct local/stalk/Tor definitions with hypotheses visible.

### 9.3 Varieties, curves, surfaces

- [ ] `Varieties(S)` with finite-type/separated/integral hypotheses explicit.
- [ ] `Curves(S)` and `Surfaces(S)` as dimension subcategories.
- [ ] Toric varieties through the toric-scheme layer.
- [ ] Arithmetic and geometric genus as distinct invariants.
- [ ] Curve normalization data and relation to delta invariants.

## 10. Categorical scheme operations and products

- [ ] Products of schemes as categorical products over the stated base.
- [ ] Extend the now-live products of projective spaces and finitely presented affine schemes to the remaining general affine/projective cases while preserving actual categorical projections.
- [ ] Mixed affine/projective/base-change products without backend strings as API.
- [ ] Extend the now-live affine fiber products/pullback squares `Spec(B tensor_A C)` to non-affine/mixed cases and verify gluing/base-change compatibility.
- [ ] Inverse images of closed subschemes.
- [ ] Diagonals as morphisms/subobjects.
- [ ] Graph morphisms/subschemes.
- [ ] Equalizers and fixed subschemes.
- [ ] Scheme-theoretic image.
- [ ] Base change of schemes with identity/composition laws.
- [ ] Parameter spaces/relative Spec where needed by section and cyclic-cover families.

## 11. Picard groups, line bundles, intersections, cohomology, and sections

### 11.1 Picard and divisor groups

- [ ] Attach live `PicardGroup`, `ClassGroup`, `CartierDivisorGroup`, `WeilDivisorGroup` functorially to schemes where defined.
- [ ] Natural Cartier/Picard to Weil/class comparisons under correct hypotheses.
- [ ] Distinguished `O(1)` on projective space.
- [ ] Field cases `Pic(A^n)=0`, `Cl(A^n)=0`, `Pic(P^n)=Z`, `Cl(P^n)=Z` through the general objects.
- [ ] General-base projective-space Picard group including the base contribution; do not hard-code field formulas.
- [ ] `Pic(P^1 x P^1) ~= Z^2` and standard generators.
- [ ] Picard lattice/intersection pairing on surfaces such as `P^1 x P^1`.

### 11.2 Line bundles/intersections

- [ ] `O(d_1,...,d_r)` on products of projective spaces.
- [ ] Tensor product/addition, dual/inverse, powers.
- [ ] Pullback and base change.
- [ ] Canonical and anticanonical bundles.
- [ ] Ampleness predicates where exact.
- [ ] Intersection pairings and top self-intersections.
- [ ] Complete-intersection adjunction through the actual canonical bundle.

### 11.3 Cohomology/sections

- [ ] `H^i(X,L)` as actual modules/vector spaces.
- [ ] Exact cohomology dimensions on supported projective spaces/products.
- [ ] Pullback/restriction maps on global sections as actual linear morphisms with kernels/cokernels.
- [ ] Sections <-> homogeneous polynomials.
- [ ] Section rings as graded algebras.
- [ ] Cox rings with Picard/multigrading.
- [ ] Homogeneous-degree lookup in the Cox ring.

### 11.4 Linear systems

- [ ] Complete linear systems `|L|`.
- [ ] Associated projective morphism.
- [ ] Base loci and basepoint-freeness.
- [ ] Restriction/evaluation maps to closed subschemes.
- [ ] Jets and imposed-singularity conditions.
- [ ] Parameter spaces of sections.
- [ ] Bertini-family interfaces only with correct genericity statements.

## 12. Singularities of curves and schemes

- [ ] Local regularity/singularity testing.
- [ ] Zariski tangent spaces.
- [ ] Jacobian criterion in supported finite-type settings.
- [ ] Milnor algebras/numbers for isolated hypersurface singularities.
- [ ] Tjurina algebras/numbers.
- [ ] ADE normal-form/type recognition with explicit scope/hypotheses.
- [ ] Archived `A_n` and `D_n` plane-curve families.
- [ ] Delta invariants and relation to normalization/geometric genus.

## 16. Toric schemes and varieties

- [ ] `ToricSchemes(S)` as schemes with torus/fan structure, not hard-coded fan recognition.
- [ ] Construction from rational fans.
- [ ] Construction from lattice polytopes via normal fans.
- [ ] Preserve polarizing-polytope relation.
- [ ] Native Sage toric varieties only as backend realizations.
- [ ] Toric closed subschemes as ordinary closed subschemes; general hypersurfaces are not toric automatically.
- [ ] Standard identifications (`P^n`, `P^1 x P^1`, weighted projective spaces, Hirzebruch surfaces, etc.) only as proven isomorphisms or exact derived display metadata.

## 13. Cyclic covers, involutions, fixed loci, and quotients

- [ ] Cyclic-cover data `(L,s,n)` with branch section in `H^0(X,L^n)`.
- [ ] Cover algebra `oplus_{i=0}^{n-1} L^{-i}` with multiplication from the branch section.
- [ ] Finite cover morphism as an actual scheme morphism.
- [ ] Branch and ramification subschemes.
- [ ] Canonical-bundle formula under correct hypotheses.
- [ ] Smoothness criteria in supported cases.
- [ ] Deck transformations as automorphisms.
- [ ] Lifts of base automorphisms preserving/scaling the branch section; two lifts for double covers when they exist.
- [ ] Fixed subschemes as equalizers.
- [ ] Fixed-point evaluation and equivariant section-space actions.
- [ ] Action on holomorphic top forms when cohomology is present.
- [ ] Fixed-locus/representation/Lefschetz compatibility.
- [ ] Quotient schemes/families for supported finite actions.
- [ ] Local invariant rings connected to global quotient data.
- [ ] `(4,4)` K3 double-cover family and two lifts of the diagonal sign involution.
- [ ] Enriques quotient only after fixed-point-free and compatibility conditions are actual predicates/morphisms.

## 14. Complete intersections, del Pezzo geometry, and blowups

- [ ] Complete-intersection detection and defining degrees.
- [ ] Mathematical complete-intersection datum/object rather than generic certificate records.
- [ ] Normality and Gorenstein predicates where exactly decidable.
- [ ] Canonical/anticanonical bundles by adjunction.
- [ ] Del Pezzo degree and predicate via ampleness of `-K`.
- [ ] Blowups of the projective plane and supported smooth surfaces.
- [ ] Exceptional divisors and Picard/intersection changes.
- [ ] Strict transforms of curves/divisors.
- [ ] Archived del Pezzo blowup benchmarks.

## 7. Representation theory of `R[G]`-modules and group lattices

- [ ] Restricted automorphism actions on invariant/isotypic pieces.
- [ ] `(4,4)` involution example with `13+12` section-space decomposition after geometry lands.

## 3. Integral Lattices, Elements, Reductions, and Arithmetic Groups (Semantic API Contracts)

### 3.1 Lattices (`L`)

- [ ] `B = L.gram_tensor()`: actual symmetric $(0,2)$-tensor.
- [ ] `M = L.gram_matrix(basis=None)`: coordinate presentation of $B$.
- [ ] `L.b(v, w)`: bilinear pairing $b_L(v,w)$.
- [ ] `L.q(v)`: quadratic evaluation $b_L(v,v)$ without $1/2$ factor.
- [ ] `L.metric_map()`: canonical map $L \to L.\operatorname{linear\_dual}()$.
- [ ] `L.linear_dual()`: exact module dual $\operatorname{Hom}_{\mathbb{Z}}(L, \mathbb{Z})$.
- [ ] `L.dual_lattice()`: dual lattice $L^\vee$ inside $L \otimes \mathbb{Q}$.
- [ ] `L.discriminant_module()`: finite formed module $A_L = L^\vee/L$ with quadratic form $q(x + L) \in \mathbb{Q}/2\mathbb{Z}$ (even) or bilinear form (odd).
- [ ] Invariant predicates: `L.signature()`, `L.radical()`, `L.is_even()`, `L.is_nondegenerate()`.
- [ ] `L.sublattice_from(vectors, saturate=False)`: returns a subobject pair $(S, \iota: S \hookrightarrow L)$ with inclusion morphism, never an unattached Gram matrix.
- [ ] `L.primitive_sublattice_from(vectors)`: saturated subobject via Smith normal form of the quotient.
- [ ] `L.orthogonal_complement(I)` / `L.perp(I)`: orthogonal subobject pair $(I^\perp, \iota: I^\perp \hookrightarrow L)$.
- [ ] `L.O()`: full finitely generated arithmetic group $O(L)$.
- [ ] `L.O_plus()`: stable orthogonal group $\widetilde{O}(L) = \ker(O(L) \to O(A_L))$.
- [ ] `L.O_component()`: positive cone component group $O^\Omega(L)$, when a component is specified.
- [ ] `L.isometry_to(M)`: returns an actual `LatticeIsometry` morphism $f: L \to M$ or `None`.
- [ ] `L.is_isometric_to(M)`: verified boolean predicate.
- [ ] Locus objects: `L.vector_locus(norm=m, primitive=False)`, `L.isotropic_sublattice_locus(rank=k)`, `L.isotropic_flag_locus(ranks=(d1, ..., dr))`.

### 3.2 Lattice Elements (`v`)

- [ ] `v.parent()`: lattice $L$.
- [ ] `v.to_vector(basis=None)`: coordinate row vector.
- [ ] `v.to_covector()`: dual evaluation $\beta_L(v) \in L.\operatorname{linear\_dual}()$.
- [ ] `v.is_primitive()`: primitivity test in $L$.
- [ ] `v.divisor()`: positive generator of the ideal $b(v, L) \subset \mathbb{Z}$.
- [ ] `v.discriminant_class()`: associated class $[v / \operatorname{div}(v)] \in A_L$ for primitive $v$.
- [ ] `v.is_isotropic()`: test $L.q(v) == 0$.
- [ ] `v.sublattice()`: rank-1 subobject $\mathbb{Z}v \hookrightarrow L$ with inclusion morphism.
- [ ] `v.orthogonal_complement()` / `v.perp()`: orthogonal complement $(v^\perp, \iota: v^\perp \hookrightarrow L)$.
- [ ] `v.isotropic_reduction()`: rank-1 isotropic reduction object.

### 3.3 Sublattices and Isotropic Reductions (`I`, `R`)

- [ ] `I.ambient_lattice()`: derived codomain of inclusion morphism $\iota.\operatorname{codomain}()$.
- [ ] `I.inclusion()`: embedding morphism $\iota: I \hookrightarrow L$.
- [ ] `I.basis()`: basis elements of $I$.
- [ ] `I.rank()`: rank of $I$.
- [ ] `I.saturation()`: saturated closure $I_{\text{sat}} \hookrightarrow L$.
- [ ] `I.is_primitive()`: saturation test via Smith invariants of $L/I$.
- [ ] `I.is_totally_isotropic()`: test $b(x,y) = 0$ for all $x,y \in I$.
- [ ] `I.perp()`: orthogonal complement $(I^\perp, I^\perp \hookrightarrow L)$.
- [ ] `R = I.isotropic_reduction()`: structured reduction object for $K_I := I^\perp / I$ (torsion-free, non-degenerate of signature $(p-k, q-k)$ for $\operatorname{rk}(I)=k$ and $\operatorname{sig}(L)=(p,q)$):
  - `R.isotropic_sublattice()`: original subobject $I$.
  - `R.orthogonal_complement()`: $I^\perp$.
  - `R.quotient_lattice()`: non-degenerate formed quotient lattice $K_I = I^\perp / I$.
  - `R.inclusion()`: inclusion morphism $I \hookrightarrow I^\perp$.
  - `R.projection()`: canonical projection morphism $I^\perp \twoheadrightarrow K_I$.
  - `R.levi_action()`.
  - `R.unipotent_kernel()`.
  - `R.lift_isometry(...)`.

### 3.4 Orthogonal and Arithmetic Groups (`G = L.O()`) and Subgroup Constructors

- [ ] `G.ambient_lattice()`: underlying lattice $L$.
- [ ] `G.gens()`, `G.one()`, `G.element(matrix)`, `G.contains(g)`.
- [ ] `G.discriminant_representation()`: reduction homomorphism $\rho_A: G \to O(A_L)$.
- [ ] `G.component_character()`: character $\chi_\Omega$, when defined.
- [ ] `G.kernel(phi)`: kernel subgroup for homomorphisms $\phi$.
- [ ] `G.preimage(phi, H)`: preimage subgroup.
- [ ] `G.stable_subgroup()`: kernel of $\rho_A$ on discriminant form.
- [ ] `G.component_subgroup()`.
- [ ] `G.centralizer(f)`: centralizer $Z_G(f)$.
- [ ] `G.stabilizer(v)`: point stabilizer of vector $v$.
- [ ] `G.stabilizer(I, action="setwise")` and `G.stabilizer(I, action="pointwise")`: setwise and pointwise stabilizers of sublattice $I$.
- [ ] `G.intersection(H1, ..., Hr)`: intersection of subgroups.
- [ ] `G.transporter(x, y)`: element $g \in G$ mapping $x \mapsto y$.
- [ ] `G.orbit_decomposition(X)`: orbit representatives, stabilizers, and transporters on locus $X$.
- [ ] Structured subgroup parents retaining construction provenance:
  - `GeneratedSubgroup(generators)`
  - `KernelSubgroup(phi)`
  - `PreimageSubgroup(phi, H)`
  - `StabilizerSubgroup(G, object, action)`
  - `CentralizerSubgroup(G, f)`
  - `IntersectionSubgroup(G1, ..., Gr)`
- [ ] Finite-quotient double coset splitting for $\Gamma = \rho^{-1}(H) \leq O(L)$: $P_x \backslash G / \Gamma \cong \rho(P_x) \backslash \rho(G) / H$ computed via libGAP.

### 3.5 Rational Matrix Groups and Integral Lattice Stabilizers

- [ ] `integral_stabilizer(G_Q, L)`: computes $G \cap \operatorname{GL}(L) = \rho^{-1}(\operatorname{Stab}_{\rho(G)}(S_L))$ for rational matrix group $G = \langle g_1, \dots, g_r \rangle \leq \operatorname{GL}(V_{\mathbb{Q}})$ and commensurable lattice $dM \subseteq L \subseteq M$.
- [ ] `integral_transporter(G_Q, L1, L2)`: computes rational element making $g L_1 = L_2$ integral.
- [ ] `integral_right_cosets(G_Q, L)`: computes right-coset transversals of $G_L$ in $G$.
- [ ] `integral_double_cosets(V_Q, G_Q, L)`: computes $V \backslash G / G_L$ on finite quotient module $F_M = M/dM$ via libGAP.

### 3.6 Centralizers $O(L,f)$ and Equivariant Lattices

- [ ] Involution centralizer algorithm for $f^2 = 1$: eigenspaces $V_\pm = \ker(f \mp 1)$, sublattices $L_\pm = L \cap V_\pm$, gluing subgroup $H_L = L/(L_+ \oplus L_-) \subset A_{L_+} \oplus A_{L_-}$, and $O(L,f) \cong \{(g_+, g_-) \in O(L_+) \times O(L_-) : (g_+, g_-)(H_L) = H_L\}$.
- [ ] Cyclotomic decomposition for finite-order $f$: $\bigoplus_{d \mid \operatorname{ord}(f)} V_{\Phi_d}$, sublattices $L_d = L \cap V_{\Phi_d}$, and equivariant gluing stabilizer.
- [ ] Semantic decorated lattice types: `Lf = L.with_isometry(f)`, `Lf.centralizer_group()`, `Lf.equivariant_sublattice(...)`, `Lf.equivariant_isometry_to(Mg)`.
- [ ] Equivariant orbit enumeration on decorated objects $(L,f)$ preserving $b_L$ and $f$ at every stage.

### 3.7 Finite Configuration, Graph Labeling, and Polyhedral Primitives

- [ ] **Pairing configuration graphs**: Encoding vector/facet pairings into colored graphs with vertex/edge invariants.
- [ ] **Graph canonization interface**: Interface to Sage's Bliss/Nauty backend for canonical graph labeling and automorphism groups.
- [ ] **Permutation lifting**: Lifting graph automorphism permutations to integral lattice isometries via `libgap`.
- [ ] **Exact rational polyhedral cones**: Facet enumeration, extreme rays, incidence, and face stabilizers delegating to Normaliz, cddlib, or PPL.

### 3.8 Reduction Complex, Transporters, and Lorentzian Base Case

- [ ] **Reduction cell and transporter interfaces**: Structured `ReductionCell` and `AdjacentCell` records.
- [ ] **Lorentzian perfect-domain engine**: Signature $(1,n)$ component group $O^\Omega(L)$ and full group $O(L) = O^\Omega(L) \times \langle -I \rangle$.
- [ ] **Marked-vector cell extension**: Traversal of perfect domains carrying marked nonzero-norm vector sets for general Lorentzian vector orbits.

## 5. Indefinite Recursion, Parabolic Induction, and Milestones

### 5.1 Higher-Witt-Index $2U$-Eichler Approximate Models and Recursion

- [ ] **$2U$-Eichler model**: For $L = U \oplus U \oplus K$, generate $A(L) = \langle SL_2(\mathbb{Z})_{\text{left}}, SL_2(\mathbb{Z})_{\text{right}}, E_{f,x}, \operatorname{Aut}_K(A_L) \rangle$ where $E_{f,x}(y) = y + b(y,x)f - \frac{q(x)}{2}b(y,f)f - b(y,f)x$.
- [ ] **Covering representatives**: Compute finite covering list $C(L, \beta)$ from discriminant classes $[v/\operatorname{div}(v)] \in A_L$ and square divisors.
- [ ] **Full orthogonal group generation**: Compute $O(L) = \langle A(L), P_v, t_1, \dots, t_s \rangle$ from approximate subgroup $A(L)$, recursive stabilizer $P_v = \operatorname{Stab}_{O(L)}(v)$, and transporters $t_i$.
- [ ] **Recursive lattice equivalence**: Splitting vector selection, covering list enumeration, and recursive vector transporters.

### 5.2 Primitive Isotropic Vectors & Cusp Orbits

- [ ] Priority API: `L.primitive_isotropic_vectors()` returning the domain/enumeration of primitive isotropic vectors $v \in L$ ($b_L(v,v)=0$, $\operatorname{div}(v)=1$ in $\mathbb{Z}v$).
- [ ] Priority API: `O.orbit_decomposition(X)` for primitive isotropic vectors returning exact cusp orbit representatives, stabilizers $\Gamma_v$, and transporter isometries.
- [ ] Exact cusp invariants: divisibility $\operatorname{div}(v) = \gcd(b_L(v, L))$ and associated discriminant class $[v/\operatorname{div}(v)] \in A_L = L^\vee/L$.

### 5.3 Primitive Isotropic Sublattices & Flags via Exact Gluing Parabolics

- [ ] Priority API: `L.primitive_isotropic_sublattices(rank=k)` returning saturated isotropic submodules $(I, \iota: I \hookrightarrow L)$ satisfying $I^\perp \cap I = I$ (primitivity certified by Smith invariants of $L/I$, never raw basis matrices).
- [ ] Semantic separation: Vector $v$ vs. rank-1 sublattice $\mathbb{Z}v$ vs. rational $k$-plane $W \subset L \otimes \mathbb{Q}$ vs. integral saturated sublattice $L \cap W$.
- [ ] Exact gluing-based parabolic stabilizer replacing the "helping lattice" heuristic: rational Witt decomposition $L_{\mathbb{Q}} \cong I_{\mathbb{Q}} \oplus K_{\mathbb{Q}} \oplus I'_{\mathbb{Q}}$ with exact SES $1 \to U_I(\mathbb{Z}) \to P_I \to M_I \to 1$ where $M_I \leq \operatorname{GL}(I) \times O(K_I)$ preserves the gluing subgroup $H_L = L/(I \oplus K \oplus I')$.
- [ ] Inductive orbit step via double cosets $Q_u \backslash O(K_I) / H_I$ where $Q_u = \operatorname{Stab}_{O(K_I)}(u)$ and $H_I = \pi_I(P_I) \leq O(K_I)$.

### 5.4 Mathematical Verification Milestones

- [ ] Milestone 1 ($h=1$): $L = U \oplus E_8(-1)$ — full Lorentzian $O(L)$, $O^\Omega(L)$, primitive isotropic vector orbit, cusp stabilizer $\twoheadrightarrow O(E_8)$, unipotent radical, and transporters.
- [ ] Milestone 2 ($h=2$): $N = U \oplus U(2) \oplus E_8(-2)$ — full $O(N)$, stable $O^+(N)$, line and plane orbits, stabilizers, Tits-building incidence, and $\Gamma$-orbit splitting for finite-index $\Gamma = \rho_A^{-1}(H)$.
- [ ] Milestone 3 (Equivariant): K3 lattice $\Lambda_{K3} = 3U \oplus 2E_8(-1)$ with Enriques involution $\iota$ — invariant/anti-invariant decomposition $S_{\text{En}} \oplus T_{\text{En}}$, $O(\Lambda_{K3}, \iota)$ via gluing stabilizer, intersection with polarization stabilizer, and anti-invariant isotropic orbits.

## 6. Coxeter diagrams, reflection groups, and Vinberg theory

### 6.1 Coxeter diagrams

- [ ] Preserve root realizations/root-to-diagram morphisms, not only graphs.
- [ ] Associated Coxeter/finitely-presented Coxeter groups.
- [ ] Elliptic and parabolic subdiagram orbit posets.
- [ ] Maximal elliptic and parabolic subdiagram posets.
- [ ] Root-intersection graphs.
- [ ] Restore mathematically valid finite/affine/noncrystallographic literature regressions from `coxeter_tdd_specs`.

### 6.2 Vinberg invariant matrices and weighted graphs

- [ ] Exact reflection-cosine values.
- [ ] Vinberg invariant matrix from Gram/root data.
- [ ] Combinatorial Vinberg invariant matrices.
- [ ] Projective weighted graphs/digraphs and symmetric variants as mathematical objects.
- [ ] Conversion to/from Coxeter matrices where valid.
- [ ] Exact edge/vertex weights and projectivization.
- [ ] Crystallographic, simply-laced, compact-hyperbolic, and paracompact-hyperbolic predicates with exact hypotheses.
- [ ] Schlaeflian/determinant invariants and literature examples.

### 6.3 Hyperbolic reflection algorithms

- [ ] Dominant cone/fundamental chamber.
- [ ] Vinberg's algorithm over integral hyperbolic lattices.
- [ ] Number-field-root-row backend where mathematically valid.
- [ ] Root-length bounds and local-obstruction cases from archived tests.
- [ ] Reflectivity testing when the algorithm actually proves the result.
- [ ] Cocompactness from chamber/diagram data.
- [ ] Weyl/reflection groups as actual subgroups of `O(L)`.
- [ ] Isotropic vectors below a Vinberg height bound.
- [ ] Chamber-complex data.
- [ ] Lorentz/Allcock edge-walk fundamental-domain backend.
- [ ] Bogachev--Kolpakov exact regression examples.

## 17. ADE and toric log-pair geometry

- [ ] `LogPairs` as equipped `(X,Delta)` objects.
- [ ] Toric log pairs `(V,Delta_toric)`.
- [ ] ADE log pairs.
- [ ] Exact ADE type/variant range, including affine families where intended.
- [ ] Integral ADE polygons `Q` and distinguished point `p*`.
- [ ] Side decorations as exact combinatorial classification data.
- [ ] Toric base `Y=V_Q`.
- [ ] Boundary/blue divisor `C` and complementary divisor `C'`.
- [ ] Branch polynomial/section with Newton polygon `Q` and branch divisor `B`.
- [ ] Pyramidal 3-polytope `P` and toric threefold `V_P`.
- [ ] Double cover `X=V(z^2+f(x,y))->Y` through the general cyclic-cover construction.
- [ ] Del Pezzo involution as deck involution.
- [ ] Boundary divisor `D=pi^*C`.
- [ ] ADE base/cover surfaces as equipped geometric objects, not duplicate records.
- [ ] Polarizing-polytope invariants from the general polytope layer.
- [ ] Dynkin/ADE diagrams through the Coxeter/root-system layer.
- [ ] Alexeev--Thompson regression examples.

## 20. Archived framework specifications without complete source implementations

- [ ] Relative-Spec primitive and affine parameter spaces of sections.
- [ ] Jets and imposed-singularity linear systems.
- [ ] Bertini-family machinery.
- [ ] Linearizations of line bundles/group actions.
- [ ] Equivariant evaluation at fixed points.
- [ ] Holomorphic Lefschetz examples.
- [ ] Invariant divisors versus eigensections.
- [ ] Singular orbits and parity-forced odd `A_n` cases.
- [ ] General complete-intersection families.
- [ ] Local-global singularity compatibility cycles.
- [ ] Quotient compatibility cycles.
- [ ] Gluing-independence cycles.
- [ ] External database adapters/examples (LMFDB, curve/field databases, OEIS, GRDB) only if useful to live research API.
- [ ] Kreuzer--Skarke reflexive-polytope probes after lattice-polytopes land.
- [ ] Fanography/classified Fano-family probes after the toric layer lands.
- [ ] Late backend cleanup: wire a leaner adaptation of the required `polyhedral_common` binaries through the `py_polyhedral` bridge, preserving the wrapper boundary and PATH-based executable resolution.

## 19. Visualization and display helpers (non-blocking)

- [ ] 2D polygon SVG generation if still useful.
- [ ] 3D polytope HTML/Three.js generation if still useful.
- [ ] Coxeter/ADE TikZ only after diagram objects exist live.
- [ ] Custom rich representations only as views of live mathematical objects.
- [ ] Reassess implicit display-hook installation separately from mathematical ports.

## 24. Port-completion audit

- [ ] Compare public mathematical nouns/operations in every archived `categories/**/*.sage`/`.py` file against live API.
- [ ] Re-run every mathematically valid archived `test_known_mathematics.sage` assertion through live public constructions.
- [ ] Re-run valid `coxeter_tdd_specs` literature examples through live Coxeter/Vinberg surface.
- [ ] Rebuild valid framework scenarios against live scheme/geometry surface.
- [ ] Confirm every intentionally unported archived construction is recorded above as superseded, rejected, or spec-only.
