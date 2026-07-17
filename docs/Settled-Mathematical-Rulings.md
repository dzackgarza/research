# Settled Mathematical Rulings

Rulings ratified through the [#251](https://github.com/dzackgarza/research/issues/251) record (2026-07-16/17), stated once in their final superseding form.
Where a ruling replaced an earlier one, the supersession is recorded — the record is a progression, and earlier phrasings on the issue are not authoritative.
Every ruling is **seated** under a definition in [Mathematical Definitions](Mathematical-Definitions.md): the definition states the object, the ruling states the settled choice about it.
Vocabulary follows the [Mathematical Language Style Guide](Mathematical-Language-Style-Guide.md).

## Forms and lattices

**Nondegenerate is not unimodular.** *Seat: [Definitions §3](Mathematical-Definitions.md#3-bilinear-and-quadratic-form-categories).* Nondegeneracy is injectivity of the polarization $\tilde b : L \to L^{\vee}$; unimodularity/perfectness is bijectivity (Mathlib anchors: `LinearMap.BilinForm.Nondegenerate`, `LinearMap.IsPerfPair`). They coincide only when the determinant is a unit.
Conflating them deletes $\operatorname{coker}(\tilde b) = L^{\vee}/L$ and with it the entire discriminant theory.
The lattice category declares the **nondegenerate** notion; unimodularity is a further property-defined replete full subcategory, entered by a real membership proof through the canonical inclusion.

**The defining datum is the W-valued form, not a map to a dual.** *Seat: [Definitions §3](Mathematical-Definitions.md#3-bilinear-and-quadratic-form-categories).* An object is $(M,\, b : \operatorname{Sym}^2 M \to W)$ over a PID/Dedekind domain $R$ with fraction field $K$; the map-to-dual picture survives only as the derived **polarization** $\tilde b : M \to \operatorname{Hom}(M, W)$ (currying, no freeness needed).
The value module $W$ is a structural parameter, never a convention: $\operatorname{Hom}(A, R) = 0$ for finite $A$, so "$b$ as a map to $\operatorname{Hom}(-, R)$" is empty exactly where discriminant forms live.
Free restriction with $W = R$ recovers lattices; finite-torsion restriction with $W = K/R$ (for $\mathbb{Z}$: $\mathbb{Q}/\mathbb{Z}$, even refinement $\mathbb{Q}/2\mathbb{Z}$) recovers discriminant forms — special cases recovered, never defined independently.

**The total category and its variance.** *Seat: [Definitions §3](Mathematical-Definitions.md#3-bilinear-and-quadratic-form-categories); convention fixed in [Categorical Foundations §F.4](Categorical-Foundations.md#f.4-the-composite-convention-operatornameel-adopted).* The bilinear category is the category of elements of the presheaf of $W$-valued bilinear forms on f.g. $R$-modules, in the standard sense (no $(-)^{\mathrm{op}}$), so a morphism $(M, b_M) \to (N, b_N)$ has underlying map $f : M \to N$ with $f^{*} b_N = b_M$ and the projection to $\mathrm{Mod}_R$ is covariant.
The variance is forced, not chosen: the datum is the $W$-valued form and a form morphism pulls the target form back to the source. The integral sign is the Grothendieck construction, not an end or coend.
*Supersession:* the root presheaf is the **full bilinear** one — symmetry, skew-symmetry, alternating, nondegeneracy, perfectness are property-defined replete full subcategories of it.
The earlier working presheaf that baked symmetry into the construction is superseded.

**Alternating vs skew-symmetric.** *Seat: [Definitions §3](Mathematical-Definitions.md#3-bilinear-and-quadratic-form-categories).* $\mathrm{Alternating} \subseteq \mathrm{SkewSymmetric}$ holds unconditionally (polarize $b(x{+}x',\, x{+}x') = 0$); the converse holds exactly when multiplication by $2$ on $W$ is injective (injectivity suffices — invertibility was overkill).
Both predicates are owned at the bilinear category; the implication is a generated inclusion with the polarization identity as witness.
*Supersession:* the intermediate "correction" that nested the alternating definition inside the skew subcategory was rejected — it baked a theorem into a definition and diverged from the Mathlib anchor (`IsAlt` is defined on bilinear maps directly).

**Bilinear and quadratic are parallel hierarchies.** *Seat: [Definitions §4](Mathematical-Definitions.md#4-the-polarization-functors).* $\operatorname{diag} : \mathrm{SymBil} \to \mathcal{Q}$ ($b \mapsto q(x) = b(x,x)$) and $\operatorname{polar} : \mathcal{Q} \to \mathrm{SymBil}$ satisfy $\operatorname{polar} \circ \operatorname{diag} = 2$ and $\operatorname{diag} \circ \operatorname{polar} = 2$; they are equivalences only when $2$ is invertible on $W$.
On the torsion side $W = \mathbb{Q}/\mathbb{Z}$ has $2$-torsion — exactly where even discriminant forms live — so the two hierarchies are genuinely parallel, related by the polarization functors, with equivalences only under hypotheses.
`QuadraticModuleCat` is the Mathlib anchor for the quadratic side, never the definition of lattice morphisms.
*Supersession:* earlier mapping rows identifying lattice hom-sets with `QuadraticMap.Isometry` are wrong identifications.
Even lattices / quadratic discriminant forms arise by **pullback along the bilinearization functor**, not as an "even cut" of bilinear objects — the same one mechanism used twice.

**Derived categories are expressions, never declared.** *Seat: [Definitions §5](Mathematical-Definitions.md#5-derived-arithmetic-categories).* In final form:

$$
\mathbf{Lat}_R = \mathcal{B}_{R,R}\big[\mathrm{Symmetric} \wedge \mathrm{Nondegenerate} \wedge \pi^{*}(\text{f.g.} \wedge \text{projective})\big]
$$

(projective of finite rank is the definition; over a PID this is finitely generated free); $\mathbf{Unimod}_R$ replaces Nondegenerate by Perfect (which implies it);

$$
\mathbf{DiscBil}_{\mathbb{Z}} = \mathcal{B}_{\mathbb{Z},\,\mathbb{Q}/\mathbb{Z}}\big[\mathrm{Symmetric} \wedge \mathrm{Nondegenerate} \wedge (U \circ \pi)^{*}(\mathrm{Finite})\big];
$$

$\mathbf{DiscQuad}_{\mathbb{Z}}$ is the pullback of $\mathbf{DiscBil}_{\mathbb{Z}}$ along bilinearization.
The AG negative-definite convention ($A_n$ negative-definite) is a normalization on objects, not a change of category.

## The discriminant construction and the exact-sequence package

*Seat: [Definitions §6](Mathematical-Definitions.md#6-the-discriminant-construction-and-the-exact-sequence-package).*

For nondegenerate integral $L$, **$\operatorname{coker}(\tilde b)$ carrying the induced $K/R$-valued form is the discriminant form**: the discriminant construction is the functor "cokernel of polarization with induced form," from the free-nondegenerate restriction to the finite-torsion restriction.
It is declared **on cores** — functorial for isometries, not for arbitrary form-preserving embeddings.
Applying $\operatorname{Aut}$ to it generates $O(L) \to O(q_L)$; its kernel is the stable isometry group, its image the discriminant representation — all generic group-homomorphism machinery, none of it bespoke.

**Regularity is the vanishing of a carried witness, not a predicate.** The polarization $\tilde b : L \to L^*$ carries two functorial objects: $\operatorname{rad}(L) = \ker \tilde b$ and $A_L = \operatorname{coker} \tilde b$.
Nondegeneracy *is* $\operatorname{rad}(L) = 0$ (the radical is the obstruction, and nondegeneracy its vanishing — never "$b$ is degenerate" named as the obstruction); unimodularity/perfectness *is* $\tilde b$ an isomorphism, i.e. $\operatorname{rad}(L) = 0$ and $A_L = 0$.
Passing to $K$, the obstruction to the rational polarization $\tilde b_K : L_K \to (L_K)^*$ — equivalently to the comparison $\beta = \tilde b_K|_{L^{\#}} : L^{\#} \to L^*$ between the metric dual and the monoidal dual — is the object $\operatorname{rad}(L_K) = \operatorname{rad}(L) \otimes K$, whose vanishing is nondegeneracy. The discriminant $A_L$ is a *cokernel* witness, not an obstruction to this comparison: for a nondegenerate lattice $\beta$ is an isomorphism regardless of how large $A_L$ is.

Three kernel-checked diagram lemmas (formalization obligations, never re-encoded informally at the DSL level — the highest-drift-risk material in the program):

1. **Radical/discriminant sequence.** $0 \to \operatorname{rad}(L) \to L \xrightarrow{\tilde b} L^* \to A_L \to 0$ (with $W = R$; in general $L^* = \operatorname{Hom}(L, W)$), naming both witnesses at once.

2. **Localization LES.** From $L \otimes_R (0 \to R \to K \to K/R \to 0)$ with $K$ flat: $0 \to \operatorname{Tor}_1^R(L, K/R) \to L \to L \otimes_R K \to L \otimes_R (K/R) \to 0$, where $\operatorname{Tor}_1^R(L, K/R) \cong T(L)$; the metric dual $L^{\#} = \{x \in L_K : b_K(x, L) \subseteq R\} = \tilde b_K^{-1}(L^*)$ is always an honest submodule of $L_K$ containing $L$.

3. **The double complex.** For nondegenerate $L$ the polarization is a morphism of the localization LES to its $\operatorname{Hom}(L, -)$-dual with middle vertical $\tilde b_K$ an isomorphism; the snake lemma gives $A_L = \operatorname{coker} \tilde b \cong \ker \bar b$ and the dual presentation $0 \to A_L \to L \otimes (K/R) \xrightarrow{\bar b} \operatorname{Hom}(L, K/R) \to 0$, with $A_L = L^{\#}/L \cong L^*/\tilde b(L)$.
   The comparison $L^* \cong L^{\#}$ is the **once-only** sanctioned realization of the dual inside the rational span; everything downstream consumes the abstract objects and canonical maps.

## Automorphism groups

*Seat: [Definitions §7](Mathematical-Definitions.md#7-isometry-groupoids-and-automorphism-groups).*

**O is an instance, never a node.** $\operatorname{Aut} : \operatorname{Core}(\mathcal{C}) \to \mathbf{Grp}$ is one generic construction; $O(X) = \operatorname{Aut}(X)$ at an object of the forms category, and $\operatorname{Isom}(X, Y) = \operatorname{Hom}_{\operatorname{Core}(\mathcal{C})}(X, Y)$.
Nothing about $O$ is data.
Where bases exist (the free restriction), passing to a basis induces the faithful representation $O(L) \hookrightarrow \mathrm{GL}_n(R)$ — the precise sense in which $O(L)$ "is" a matrix group.

**The torsion side is a quotient of a matrix group, never a subgroup.** For $A = \mathbb{Z}^n / D\mathbb{Z}^n$ with mixed invariant factors, $A$ is free over no ring; entrywise reduction on the stabilizer of $D\mathbb{Z}^n$ surjects onto $\operatorname{End}(A)$ with a congruence kernel, and restricted to $\mathrm{GL}_n(\mathbb{Z})$ it is *not* onto $\operatorname{Aut}(A)$ (multiplication by $2$ on $\mathbb{Z}/5$ has no lift in $\mathrm{GL}_1(\mathbb{Z}) = \{\pm 1\}$). Hence $O(A_L)$ is canonically a quotient of a congruence-type matrix group, finitely presented by generators and relations; any realization *as* matrices is incorrect, not merely lossy (Hillar–Rhea 2007). The **homocyclic** exception ($d_1 = \cdots = d_n = d$): $A$ is free over $\mathbb{Z}/d$ and $O(q) \le \mathrm{GL}_n(\mathbb{Z}/d)$ genuinely — e.g. $A_2$'s discriminant group $\mathbb{Z}/3$.

**$\operatorname{Isom}(L, M)$, when nonempty, is an $(O(L), O(M))$-bitorsor** — free transitive actions on both sides, statable with standard action machinery.

## Invariants and their evaluation

**Cardinality is total on Sets.** *Seat: [Definitions §9](Mathematical-Definitions.md#9-constructors).* It is an invariant on isomorphism classes, $\pi_0(\mathbf{Set}^{\simeq}) \to \mathbf{Card}$ — $\mathbb{Z}$ has one.
Not a functor into a discrete category (morphisms exist between sets of unequal cardinality).
A finite presentation (a chosen $X \simeq \mathrm{Fin}\, n$) is the **evaluation witness** where computation happens; a presentation is never the home of the invariant it evaluates.
Every structured object reaches set-level invariants through its forgetful functor and never re-declares them.
*Supersession:* the original "cardinal-equipped finite sets" home is retracted (S5 at-source correction).

**Index.** *Seat: [Definitions §7](Mathematical-Definitions.md#7-isometry-groupoids-and-automorphism-groups).* The home is the subgroup/monomorphism; the value is the cardinality of the coset space $G/H$ — which for non-normal $H$ is a plain type, exactly as Mathlib defines `Subgroup.index := Nat.card (G ⧸ H)`. The identity "index $= \lvert\operatorname{coker}\rvert$" is a **theorem under the abelian hypothesis, not a definition**: categorical cokernels exist over groups but compute $\lvert H / \text{normal-closure}(\operatorname{im} f)\rvert$ — the wrong number for non-normal images.
*Supersession (twice over):* both the original "sited on morphisms" phrasing and the later "objects of the arrow category over a has-cokernels base" gate are falsified — the gate was neither necessary (the coset space needs no cokernels) nor sufficient (cokernels exist over groups and give the wrong answer).
The group-index row can be written, correctly, via the coset space.

**(Co)limits are sited at the category-theory level.** *Seat: [Definitions §9](Mathematical-Definitions.md#9-constructors).* Limits, colimits, products, coproducts are defined once for arbitrary categories, with Type-level (and each concrete category's) limits as instances; siting them at an instance re-implements them at every other instance (the same failure one level up).
Universal-property witnesses (limit cones, biproducts) are the identification obligations, not constructors.

**Genus is set-level.** *Seat: [Definitions §8](Mathematical-Definitions.md#8-genus).* The genus of $L$ is the fiber of $\pi_0 \operatorname{Core}(\mathbf{Lat}_{\mathbb{Z}}) \to \pi_0 \prod_v \operatorname{Core}(\mathbf{Lat}_{R_v})$ over the class of the local profile of $L$ — a **set-level pullback**. *Supersession:* the homotopy-pullback formula "genus $= \pi_0(\text{homotopy pullback})$" is false — $\pi_0$ does not commute with homotopy pullbacks; the components of the homotopy fiber over $[L]$ form $O(L) \backslash \prod_v O(L_v)$, typically uncountable.
If the groupoid is wanted, it is the classical adelic double coset with restricted products doing real work.
The 1-truncation is the content; higher-categorical machinery deployed decoratively silently changes the object.

**Left and right modules are distinct categories.** *Seat: [Definitions §1](Mathematical-Definitions.md#1-module-categories).* Right $R$-modules are modules over $R^{\mathrm{op}}$ — a different category, with the commutative-case identification carried by a canonical functor (a hypothesis-bearing equivalence with a natural-isomorphism witness), not an equality.
$\mathrm{Mod}_R$, $\mathrm{Mod}_{R^{\mathrm{op}}}$, and ${}_{R}\mathrm{BiMod}_S$ are distinct objects of the presentation; there is one parameterized module family, and "right modules" is not a separate primitive kind.

## Relation kinds are not fungible

*Seat: [Definitions §2](Mathematical-Definitions.md#2-axioms-as-subcategories-transport) and [Categorical Presentation Principles](Categorical-Presentation-Principles.md).*

Identity, definitional equality, equivalence, isomorphism, forgetful image, chosen presentation, property, ingredient, and example are distinct relation kinds, and every recorded claim names which one it makes.
Standing consequences:

- a bilinear form is an *ingredient* of a lattice, not the lattice or its category;

- a chosen basis is not the property of being finite free; a computational enumeration is not the property of finiteness or countability;

- an equivalence of categories does not erase the design choice between property-defined objects and objects carrying chosen data;

- a worked example (the standard rank-n lattice, $\mathbb{F}_2$) is an *instance*, never category-level vocabulary — define the general construction and instantiate (singleton reification is the recorded failure mode);

- a proof that a local declaration agrees with a standard one is evidence the local declaration is redundant or misplaced, not evidence it belongs where it is.

Absence of a single prepackaged upstream name is **not** absence of the mathematics: standard mathematics is frequently compositional (full subcategories cut by properties, categories of elements, transported functors), and a claimed gap is admissible only with search evidence — what was searched, the nearest notions found and distinguished (negative-finding bar; see the [Lean–Sage Integration Model](Lean-Sage-Integration-Model.md)).
