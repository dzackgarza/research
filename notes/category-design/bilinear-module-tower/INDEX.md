# The bilinear-module tower — design corpus

Design records for the category tower

$$R\text{-Mod} \;\to\; \mathrm{Bil}_R\text{-Mod} \;\to\; \mathrm{SymBil}_R\text{-Mod} \;\to\; \text{integral lattices},$$

together with its subcategory scheme by signature (definite, indefinite,
hyperbolic, degenerate, parabolic), its 2-elementary and Coxeter-lattice
branches, and its morphism hierarchy. Landed 2026-08-20 from
`~/gitclones/Coxeter` and `~/gitclones/Coxeter-v2`.

Three generations of the same design are held side by side:

| Directory | Source tree |
|---|---|
| `api-planning/` | `Coxeter/tmp_restore/docs/api-planning/` |
| `implementation-planning/` | `Coxeter/implementation/planning/` |
| `sage-planning-modules-bak/` | `Coxeter-v2/archive/cold_storage_pre_integration/background-research/sage-planning/modules_bak/` |

The built surface these are read against is
`src/dzack_research/preamble/categories/` — chiefly `forms/forms.sage`,
`modules/framed/formed/form_modules.sage`, and the
`modules/framed/formed/integrallattice/` subtree.

---

## 1. Documents

### 1.1 `api-planning/` — the interface specifications

| Document | Mathematical content |
|---|---|
| `BILINEAR_FORMS_MATHEMATICAL_NOTES.md` | Terminology; left and right orthogonality for a non-symmetric form; which methods are defined under which symmetry hypothesis (no orthogonal complement, norm, or reflection on the general bilinear branch); the full symmetry hierarchy including skew-symmetric and alternating. |
| `bilinear_module_morphisms.md`, `categories/bilinear_forms/bilinear_module_morphisms.md` | The morphism hierarchy $\mathrm{PrimEmb} \subseteq \mathrm{Emb} \subseteq \mathrm{Hom} \subseteq \mathrm{Hom}_R$ as first-class homsets; kernels, cokernels, images carrying restricted forms; the adjoint $f^{*}$; the discriminant multiplier of a morphism; $O(L)$. |
| `categories/bilinear_forms/bilinear_form_operations.md` | Operations on a form itself: decomposition into symmetric and skew parts, pullback along a morphism, the two-sided fibre product $b(\varphi_L \times \varphi_R)$, tensor of forms, hom-spaces of forms, symmetric monoidal structure on forms. |
| `categories/bilinear_Rmod/bilinear_RMod.md`, `bilinear_Rmod_elements.md` | The free bilinear-module interface: left and right dual modules and radicals, the nondegenerate quotient, discriminant, Witt index and Witt decomposition, isotropic submodules, symmetric monoidal structure; element-level form evaluation. |
| `categories/bilinear_Rmod/symmetric_Rmod/symmetric_Rmod.md`, `symmetric_Rmod_elements.md` | Symmetric bilinear $R$-modules: the signature $(p,q,r)$ under the hypothesis that $R$ embeds in $\mathbb{R}$, definiteness predicates, Witt index, radical identities; element operations (reflection, polarization identity, radical projection, orthogonal hyperplane). |
| `.../nondegenerate_lattices/nondegenerate_lattices.md`, `nondegenerate_lattice_elements.md` | The base lattice interface: `is_hyperbolic`, isometry, the stable orthogonal group $O^{*}(L)$, the metric dual, the discriminant group and form, sublattice posets, base change; element divisibility, dual element, discriminant image, primitive representative. |
| `.../definite_lattices/definite_lattices.md`, `definite_lattice_elements.md` | Definite lattices: shortest vectors, minimum, theta series, covering and packing radius, successive minima, Voronoi cell, enumeration, reduction; minimal-vector predicate and reduced coset representative. |
| `.../negative_definite_lattices/*.md` | Negative definite = elliptic. Algebraic-geometry reading: the intersection form on exceptional divisors, $K^2$, the dual graph of a resolution; element-level reflection length, alcove walks, intersection multiplicity, canonical height, weight decomposition, characters. |
| `.../positive_definite_lattices/*.md` | Sphere packing: density, centre density, the Hermite constant, contact polytope, inradius and circumradius, SVP and CVP, LLL/BKZ/HKZ; element angle, distance, reduced representative, kissing neighbours. |
| `.../indefinite_lattices/indefinite_lattices.md`, `indefinite_lattice_elements.md` | Cone structure in the base-changed parent $L \otimes \mathbb{R}$ (positive, negative, light, future and past cones), primitive isotropic vectors, Witt decomposition, reflection vectors of bounded norm; causal class of a vector, cone projections, Lorentz boosts. |
| `.../hyperbolic_lattices/hyperbolic_lattices.md`, `hyperbolic_lattice_elements.md` | Hyperbolic lattices: the hyperboloid, Klein and Poincaré models, the Vinberg algorithm, reflectivity, Coxeter polytopes, volume, cusps, the Lannér condition; hyperbolic distance and angle, future/past pointing, reflection hyperplane, chamber location, Vinberg distance. |
| `.../degenerate_lattices/degenerate_lattices.md`, `degenerate_lattice_elements.md` | The degenerate subcategory: rank of the radical, a radical complement, the split-degeneracy test, the stabiliser of the radical in $O(L)$, classification of the parabolic case; element decomposition into radical and non-radical components, the quotient projection, the in-radical predicate, and the caveat that reflections are not defined. |
| `.../parabolic_lattices/parabolic_lattices.md`, `parabolic_lattice_elements.md` | Parabolic (affine) lattices: the null vector, the level, the affine root system, height grading, the affine Weyl group, string functions; element level and height, real and imaginary root predicates, null-root coefficient, cusp projection, affine Weyl orbit. |
| `.../two_elementary_lattices/*.md` | 2-elementary lattices: the invariant $a$, the mod-2 quotient with its induced form, the spinor norm, the theta characteristic, the correspondence with binary codes; element order in the discriminant group, mod-2 class, companion vector, mod-2 orthogonality. |
| `categories/coxeter_lattices/coxeter_systems.md` | The category of Coxeter systems: an object is a pair $(\Phi, \iota)$ with $\iota$ a primitive embedding of the root span into a lattice; a morphism is a commuting pair (root map, lattice map); derived Weyl group, hyperplane arrangement, and chamber data. |
| `categories/coxeter_lattices/coxeter_lattices.md`, `coxeter_lattice_elements.md` | The combined category of pairs $(L, C)$: the embedding index $[L : \langle \Phi\rangle]$, Weyl group orders, maximal parabolic subdiagrams, weight and coroot lattices, Levi decomposition, Weyl characters; element root membership and height, coroots, $\alpha$-strings, Weyl orbits and stabilisers, the dominant chamber, alcove and level, long and short roots. |
| `categories.md` | The lattice category tree as a whole: free bilinear modules $\to$ symmetric $\to$ lattices and degenerate lattices, the torsion quadratic hierarchy, the discriminant functor, the Nikulin invariants $(r,a,\delta)$, and Coxeter systems versus Coxeter lattices. |
| `factory.md` | Construction policy: signature-driven automatic classification of an input Gram matrix, $\mathbb{Z}$-first defaults, automatic sign normalisation of a definite input to the negative-definite convention, Coxeter-lattice constructors. |

### 1.2 `implementation-planning/` — the same tower as an implementation plan

| Document | Mathematical content |
|---|---|
| `RMod/RMod_category.md` | $R$-modules as a category with an abelian supercategory, operator sugar for the Grothendieck ring, the homset tensor, and an optional *parameterised* symmetric-monoidal axiom carrying the product and unit as data. |
| `RMod/RMod_objects.md`, `RMod_elements.md` | Parent mechanics for a module with a chosen basis: element constructor, coordinate module, generating set, `an_element`/`some_elements`. |
| `RMod/RMod_homs.md` | $\mathrm{Hom}_R(M,N)$ as an $R$-module with a basis of elementary morphisms; morphism construction from images, dictionaries, or matrices; evaluation morphisms; the pairing. |
| `RMod/RMod_constructions.md` | Constructors: generators and relations, presentation matrices, exterior and symmetric powers, the dual module, graded, filtered and differential modules. |
| `RMod/RMod_subcategories.md` | The axiom scheme Free / FinitelyGenerated / WithBasis together with Torsion, TorsionFree, Projective, Injective, Flat; basis-extension predicates; annihilators; invariant factors. |
| `RMod/RMod_subobjects.md` | Submodules and quotients: the coset element class, the correspondence and isomorphism theorems, the colon submodule, the socle, the Jacobson radical, a short-exact-sequence object. |
| `RMod/structures/symmetric_monoidal_direct_sum.md` | The direct sum as a symmetric monoidal structure: biproduct data, unit $0$, coherence isomorphisms, the rank homomorphism on $K_0$. |
| `RMod/structures/symmetric_monoidal_tensor.md` | The tensor product as a symmetric monoidal structure: pentagon, triangle and hexagon coherence, bifunctoriality, the closed structure with evaluation and coevaluation. |
| `BilRMod/BilRMod_category.md` | `BilinearModules(R)`: the form interface, degenerate and nondegenerate predicates, Gram-matrix methods under a chosen basis. |
| `BilRMod/BilRMod_objects.md` | A concrete bilinear-module parent: Gram storage, evaluation $v^{T} G w$, signature by eigenvalues, test-suite hooks. |
| `BilRMod/BilRMod_elements.md` | Element operations: form evaluation, the quadratic form, orthogonal projection onto a vector, Gram–Schmidt complement inside a span. |
| `BilRMod/BilRMod_homs.md` | A form-preserving homset with checked construction; orthogonal, symplectic and isomorphism classes of transformation; kernel, image and cokernel carrying forms. |
| `BilRMod/BilRMod_subcategories.md` | The axiom lattice for forms: Symmetric, SkewSymmetric, Alternating (with the characteristic-2 distinction), Nondegenerate, and the definiteness classes; the symplectic complement. |
| `BilRMod/BilRMod_subobjects.md` | Restricted forms on submodules, quotient bilinear modules, orthogonal decomposition by connectivity of the Gram matrix, the radical of a submodule. |
| `BilRMod/BilRMod_constructions.md` | Standard-form constructors: the hyperbolic plane, Euclidean and Minkowski spaces, the symplectic form, diagonal forms; root and weight lattice constructors. |
| `BilRMod/structures/tensor_product_structure.md` | Tensor of formed modules: the Kronecker Gram matrix, multiplicativity of signature and discriminant, monoidal coherence, the symmetriser and alternator. |
| `SymmetricBilRMod/SymmetricBilRMod_category.md` | The symmetric branch: the quadratic form and polarization, diagonalisation, Sylvester's law of inertia, Witt index and decomposition, $O(p,q)$, local invariants. |
| `SymmetricBilRMod/SymmetricBilRMod_objects.md` | Eigen-diagonalisation, Gram–Schmidt orthogonal and orthonormal bases, the Sylvester canonical form, a maximal isotropic subspace. |
| `SymmetricBilRMod/SymmetricBilRMod_elements.md` | Angles and distances in the positive definite case, Householder reflections, causal sign, conjugation and real/imaginary parts over $\mathbb{C}$. |
| `SymmetricBilRMod/SymmetricBilRMod_homs.md` | Orthogonal transformations: rotations (Rodrigues), reflections, similarities, the Cartan–Dieudonné decomposition, stabilisers. |
| `SymmetricBilRMod/SymmetricBilRMod_subobjects.md` | Orthogonal complements and projections, the algorithm extending an isotropic submodule to a maximal one, $\mathrm{rad}(W) = W \cap W^{\perp}$, Hermite normal form, additivity of the signature. |
| `SymmetricBilRMod/SymmetricBilRMod_subcategories.md` | The axiom scheme by signature, isotropy and integrality: definite, indefinite, anisotropic, isotropic, Integral, EvenIntegral, Unimodular; the Lorentzian causal types. |
| `IntegralLattices/IntegralLattices_category.md` | Even, unimodular, level, minimum, theta series, kissing number, genus, root-system detection, adjacency graphs. |
| `IntegralLattices/IntegralLattices_objects.md` | Algorithms: LLL/BKZ/HKZ, shortest vectors, Babai's CVP, successive minima, covering radius, the Minkowski–Siegel mass, spinor genera, Kneser $p$-neighbours, representation numbers. |
| `IntegralLattices/IntegralLattices_elements.md` | Norm, primitivity, divisibility, primitive part, height and $L^1$ enumeration, characteristic vectors, closure of a Weyl orbit. |
| `IntegralLattices/IntegralLattices_subcategories.md` | The Even, Unimodular, RootLattice and PositiveDefinite axioms: the shadow, characteristic vectors, Type II codes, Kneser neighbours, the Coxeter number, the exponents. |
| `IntegralLattices/IntegralLattices_constructions.md` | Explicit ADE Gram matrices, the Leech, Niemeier and Barnes–Wall lattices, Construction A from a binary code, Nikulin gluing, unimodular completion, Hermite normal form. |
| `categories.md` | The same lattice category tree as `api-planning/categories.md`, with an added block of mathematical test assertions. |
| `MIGRATION_CHECKLIST.md` | The index of the `modules_bak` scheme: `RMod`/`BilRMod`/`SymmetricBilRMod` with the symmetric, skew, alternating and degenerate branches and the signature subcategories. |
| `FEATURE_001_SAGEMATH_CATEGORY_REFACTORING.md` | The `RModules` refactor: the Category/Parent/Element split, the observation that only free modules have bases, and the resulting Free / WithBasis axiom plan. |

### 1.3 `sage-planning-modules-bak/` — the third pass

The same notions reorganised under `RMod/BilRMod/SymBilRMod`. What this
generation adds over the other two:

| Document | What is distinctive here |
|---|---|
| `RMod/BilRMod/BilRMod_category.md` | The fullest statement of non-symmetric form theory: left versus right radical, left and right dual modules, the adjoint $f^{*}$ characterised by $b(v, f^{*}w) = b(fv, w)$, Witt index and decomposition, the monoidal structure on formed modules, the orthogonal group. |
| `RMod/RBilForms/RBilForms_objects.md` | Forms *as objects* of their own category: symmetric and skew parts, the fibre product $b(\varphi_L \times \varphi_R)$, tensor of forms, the internal hom and the tensor–hom adjunction, the $\langle v,w\rangle$ notation proposal. |
| `RMod/RBilForms/RBilForms_homs.md` | The homset hierarchy $\mathrm{PrimEmb} \le \mathrm{Emb} \le \mathrm{Hom} \le \mathrm{Hom}_R$ as first-class parents; the adjoint morphism; the coimage and canonical factorization; the discriminant multiplier. |
| `RMod/RMod_refactored.md` | The refactor rationale: `RModules` inheriting from abelian and symmetric monoidal categories, and the no-duplication inheritance discipline. |
| `RMod/RMod_constructions.md` | The signature-dispatching lattice factory, $\mathbb{Z}$-first defaults, and automatic normalisation of a definite input to the negative-definite convention. |
| `RMod/RMod_subcategories.md` | The Free / FinitelyGenerated / WithBasis axiom scheme with its implication lattice, and the distinction *a basis is structure, freeness is a property*. |
| `RMod/RMod_subobjects.md` | Submodule poset comparison ($\le$, $<$), the context-dependence of $+$ (inner submodule sum versus external direct sum), the intersection algorithm. |
| `RMod/BilRMod/CoxeterLattice/coxeter_lattices.md`, `coxeter_systems.md` | The pair category $(L, \Phi, \iota)$ with morphisms as commuting squares; the embedding index; parabolic sublattices; weight and coroot lattices; the Levi decomposition. |
| `RMod/BilRMod/SymBilRMod/**` | The signature-branch tree (degenerate, parabolic, definite, negative and positive definite, indefinite, hyperbolic, nondegenerate, two-elementary) restated at this generation. |

**Byte-identical across generations.** Ten element-level documents in
`sage-planning-modules-bak` are identical to their `api-planning`
counterparts and were landed only once, under `api-planning/`:
`coxeter_lattice_elements`, `degenerate_lattice_elements`,
`parabolic_lattice_elements`, `definite_lattice_elements`,
`negative_definite_lattice_elements`, `positive_definite_lattice_elements`,
`hyperbolic_lattice_elements`, `indefinite_lattice_elements`,
`nondegenerate_lattice_elements`, `two_elementary_lattice_elements`.

**Empty placeholders, not landed.** Fifteen files in `modules_bak` were
created and never written: `BilRMod_factory`, `BilRMod_homs`,
`BilRMod_objects`, `BilRMod_subcategories`, `BilRMod_subobjects`,
`RBilForms_category`, `RBilForms_constructions`, `RBilForms_elements`,
`RBilForms_structures`, `RBilForms_subcategories`, `RBilForms_subobjects`,
`RMod_elements`, `RMod_homs`, `RMod_objects`, `RMod_structures`.

---

## 2. Divergences between the design and the built preamble

These are **recorded findings**. The preamble took a different route in each
case, and the design is kept because the difference is only legible against
it.

### 2.1 Coxeter data: a pair category versus a diagram holding an arrow

The design (`api-planning/categories/coxeter_lattices/`,
`sage-planning-modules-bak/RMod/BilRMod/CoxeterLattice/`) makes the object a
**pair** $(L, C)$ with $C = (\Phi, \iota)$ and $\iota$ a primitive embedding,
and a morphism a commuting square of a lattice map with a root map.

The preamble instead makes the **diagram** the object.
`coxeter_diagrams.sage:194` defines `FiniteCoxeterDiagram`, which carries an
optional `root_morphism: FormMorphism` (`:226`); the root lattice is the
domain of that arrow (`root_lattice()` at `:572`, the accessor for the
morphism itself at `:544`), and `CoxeterDiagramHomset` (`:909`) with
`CoxeterDiagramMorphism` (`:950`) is a homset of diagram morphisms, not of
commuting squares. So the lattice enters as the codomain of one
morphism a diagram may hold, rather than as half of the object.

Unbuilt in either form: the embedding index $[L : \langle\Phi\rangle]$, the
weight and coroot lattices, the parabolic sublattices, the Levi
decomposition.

### 2.2 A chosen basis versus a framing

The design's `WithBasis` axiom (`RMod_subcategories.md` at two generations)
already contains the right insight — a basis is *structure*, freeness is a
*property*. The preamble carries that insight further: the structure it
declares is a **framing**, a chosen generating epimorphism from a free
object, owned by `framed_modules.sage` and `framed_free_modules.sage` (the
notion is §13.5 of the `lean-categories` FOUNDATIONS document). `WithBasis`
as an axiom name does not exist in the preamble.

### 2.3 Degenerate and parabolic lattices are not categories in the preamble

The design gives both a first-class subcategory with their own methods
(radical rank, radical complement, split-degeneracy, stabiliser of the
radical; and for the parabolic case the null root, the level, the height
grading, the affine Weyl group).

The preamble owns the *ingredients* — `radical` and `radical_quotient` on
form modules, `is_negative_semidefinite` at `integral_lattices.sage:975`,
`is_parabolic` on Coxeter diagrams — but has no such category. A degenerate
lattice routes **out** of `IntegralLattices`:
`refine_one_lattice` (`integral_lattices.sage:2061`) refines a lattice whose
correlation morphism has nonzero kernel only into
`Lattices(ℤ).FinitelyGenerated()` and `Lattices(ℤ).Integral()` and returns.
Nothing downstream of that point is available on an affine root lattice.

### 2.4 Classification by determinant sign versus by the radical

The design classifies by the sign of $\det G$ in several places. The
preamble deliberately rejects that route: `refine_one_lattice` states in
comment that it routes by the predicate the axiom gate re-asks — the radical
as the kernel module of the correlation morphism — and *not* by a
determinant proxy. The determinant criterion is rank-dependent, so the two
routes disagree; the audit recorded specific instances (§3 below).

### 2.5 Witt theory is absent, and the design states it wrongly

Witt index, Witt decomposition, the anisotropic kernel and the maximal
isotropic submodule recur through five documents and exist nowhere in the
preamble. They should be built on symmetric bilinear form modules over a
field. The design's statement of the notion is wrong (§3), so what is to be
built is the corrected notion, not the one written here.

### 2.6 Subobjects: order-theoretic operators versus a carried inclusion

The design treats a submodule as an element of a poset with $\le$, $<$, and a
context-dependent $+$. The preamble treats a subobject as the pair
$(S, f\colon S \hookrightarrow B)$ — the inclusion morphism is the data —
and sites sum, intersection, index, saturation and `is_primitive` on that
morphism (`subobjects.sage:124`, `:142`). The poset operators and the
homological bookkeeping objects (short exact sequence, socle, Jacobson
radical) remain design-only.

### 2.7 Construction by dispatch versus explicit construction

`factory.md` and `RMod_constructions.md` design a constructor that inspects
the signature of an input Gram matrix, auto-classifies it, and silently
normalises a definite input to the negative-definite convention. The preamble
constructs explicitly and then *refines* by asking predicates; the sign
convention is a stated convention (§`../conventions/`), not an automatic
rewrite of caller input.

### 2.8 What the design has that the preamble owns

For contrast, so that the corpus is not read as a backlog: the form-module
tower itself, the Gram matrix, the radical and radical quotient, the
correlation morphism and nondegeneracy, the dual module, element-level form
evaluation, reflections, the isometry and embedding homsets with primitivity
via a torsion-free cokernel, the genus and discriminant form, gluing and
overlattices, the Vinberg algorithm and reflectivity, and the elliptic /
parabolic / hyperbolic classification of diagrams are all built. See the
`[owned]` rows of readers P1 and P2 in the audit registry for the owner of
each.

---

## 3. Errors recorded in these documents

Recorded so that a later reader cannot re-derive them from the source. The
document itself is unmodified; the correction lives here.

| Document | Claim as written | Correction |
|---|---|---|
| `implementation-planning/BilRMod/BilRMod_constructions.md` | `RootLattice(cartan_type)` is `IntegerLattice(cartan_matrix)`. | For $B$, $C$, $F_4$, $G_2$ the Cartan matrix is not symmetric and so is not a Gram matrix. The Gram matrix is the symmetrization $d_i a_{ij}$. |
| `implementation-planning/BilRMod/BilRMod_objects.md` | `is_alternating()` $\iff$ every diagonal Gram entry is zero. | Zero diagonal gives alternating only together with skew-symmetry. The symmetric form with Gram matrix $[[0,1],[1,0]]$ has zero diagonal and $b(e+f,e+f) = 2 \neq 0$. |
| `implementation-planning/BilRMod/BilRMod_subobjects.md` | $M/N$ inherits a bilinear form iff $N$ is isotropic ($N \le N^{\perp}$). | $\bar b([v],[w]) = b(v,w)$ is well defined on $M/N$ only when $b(v,n) = 0$ for **all** $v \in M$, i.e. $N \subseteq \mathrm{rad}(M)$. For a merely isotropic $N$ the induced form lives on $N^{\perp}/N$. The document states the correct condition in prose and then implements the weaker one. |
| `implementation-planning/IntegralLattices/IntegralLattices_category.md` | $\mathrm{diag}(2,3)$ and $\mathrm{diag}(1,6)$ lie in the same genus because both have discriminant $6$. | Equal discriminant is not sufficient. The 2-adic Jordan symbols differ (unit blocks $\langle 1\rangle$ versus $\langle 3\rangle$, and $3$ is a 2-adic non-square), so these lie in different genera. |
| `implementation-planning/SymmetricBilRMod/SymmetricBilRMod_category.md` (also `_objects.md`, `_subcategories.md`) | Witt index $= \min(p,q)$ of the signature; definite $\iff$ anisotropic. | True only over a real-closed field. Over $\mathbb{Q}$, $x^2 + y^2 - 3z^2$ is indefinite yet anisotropic, so the Witt index over the base field can be strictly smaller than $\min(p,q)$. |
| `implementation-planning/SymmetricBilRMod/SymmetricBilRMod_homs.md` | For an orthogonal transformation, $A^{-1} = A^{T}$. | Only for the identity Gram matrix. An isometry of a form with Gram matrix $G$ satisfies $A^{-1} = G^{-1}A^{T}G$. |
| `implementation-planning/RMod/RMod_homs.md` | $0 \to A \to B \to C \to 0$ is exact iff $0 \to \mathrm{Hom}(M,A) \to \mathrm{Hom}(M,B) \to \mathrm{Hom}(M,C) \to 0$ is exact for all $M$. | $\mathrm{Hom}(M,-)$ is left exact only. Exactness of the Hom sequence for all $M$ is equivalent to the sequence being **split**, not merely exact. |
| `implementation-planning/RMod/RMod_subcategories.md` | $M$ torsion-free $\iff$ $M$ embeds in a free module; a short exact sequence splits $\iff$ $C$ projective $\iff$ $A$ injective. | Embedding in a free module needs finite generation over a domain; a general torsion-free module embeds only in a vector space over $\mathrm{Frac}(R)$. And $C$ projective is sufficient for splitting, not necessary — a particular sequence can split without it. |
| `api-planning/.../nondegenerate_lattices/nondegenerate_lattice_elements.md` | In the hyperbolic plane $U$ with $b(e,f) = 1$, $(2e+3f)\cdot(e-f) = -5$. | $e$ and $f$ are isotropic, so bilinearity gives $-2b(e,f) + 3b(f,e) = -2 + 3 = 1$. |
| `api-planning/.../two_elementary_lattices/two_elementary_lattice_elements.md` | For every $v$ there is a companion $v'$ with $\langle v, v'\rangle$ odd, "due to the 2-elementary property". | For $v \in 2L$ every pairing $\langle v,w\rangle = 2\langle u,w\rangle$ is even, so no such companion exists. 2-elementarity of $L^{*}/L$ does not grant this. |
| `api-planning/categories/bilinear_forms/bilinear_form_operations.md` | The tensor of $\mathrm{diag}(1,-1)$ with $[2]$ has signature $(2,2,0)$ — "signatures multiply". | The tensor is $\mathrm{diag}(2,-2)$, of signature $(1,1,0)$. Signature composition is $(p_1p_2 + q_1q_2,\; p_1q_2 + q_1p_2)$. |
| `api-planning/categories/bilinear_forms/bilinear_module_morphisms.md` | The projection $a \mapsto x$, $b \mapsto y$, $c \mapsto 0$ from the Gram matrix $[[2,1,0],[1,3,1],[0,1,2]]$ is form-preserving; and an image of a nondegenerate $L_1$ under a form-preserving map is automatically isotropic. | $b(b,c) = 1$ while the images pair to $b(y,0) = 0$, so the map is not an isometry. A form-preserving image of a nondegenerate module carries a **nondegenerate** form, not an isotropic one. The document's cokernel example also conflates the quotient form with the $\mathbb{Q}/\mathbb{Z}$-valued discriminant form. |
| `api-planning/categories/coxeter_lattices/coxeter_lattices.md` | $D_4$ has one maximal parabolic of type $A_3$ and three of type $A_1^{3}$; affine types have no maximal parabolics under the remove-one-node definition. | The counts are inverted: removing any of the three outer nodes gives $A_3$ (three of them) and removing the centre gives $A_1^{3}$ (one). The affine claim contradicts the document's own definition and conflates parabolic *subgroups* with parabolic-*type* subdiagrams. |
| `api-planning/categories/coxeter_lattices/coxeter_systems.md` | `is_hyperbolic` tests whether the fundamental domain has infinite volume. | Hyperbolic type is the Lorentzian signature condition $(1, n-1, 0)$. Hyperbolic Coxeter groups of finite covolume exist, including the compact (Lannér) ones. Infinite covolume is a separate condition on the maximal parabolic subdiagrams. |
| `sage-planning-modules-bak/.../two_elementary_lattices/two_elementary_lattices.md` | $A_3$ is 2-elementary because its discriminant is $4 = 2^2$. | $A_n$ has cyclic discriminant group $\mathbb{Z}/(n+1)$, so $A_3$ gives $\mathbb{Z}/4$, not $(\mathbb{Z}/2)^2$. A power-of-2 determinant does not imply an elementary abelian 2-group. |
| `sage-planning-modules-bak/.../positive_definite_lattices/positive_definite_lattices.md` | $\det(G) < 0$ is "our convention: negative determinant for positive definite forms" (Property 4, the $D_4$ example). | $D_4$ has Gram determinant $+4$, and any even-rank definite form has positive determinant under either sign convention. The asserted doctest output is false. |
