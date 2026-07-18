# Settled Mathematical Rulings

Rulings ratified through the [#251](https://github.com/dzackgarza/research/issues/251) record (2026-07-16/17), stated once in their final superseding form.
Where a ruling replaced an earlier one, the supersession is recorded — the record is a progression, and earlier phrasings on the issue are not authoritative.
Every ruling is **seated** under a definition in [Mathematical Definitions](Mathematical-Definitions.md): the definition states the object, the ruling states the settled choice about it.
Vocabulary follows the [Mathematical Language Style Guide](Mathematical-Language-Style-Guide.md).

## Master rulings {#sec-master-rulings}

[]{#master-rulings}

These govern all the object-level rulings below. The first two are peers: [A1](#a1) fixes *where* an object is declared, [A5](#a5) fixes *how* a property is defined once you are there.

[]{#a1}**A1 — Lowest generating level.** *Seat: [Categorical Foundations](Categorical-Foundations.md); [Categorical Presentation Principles](Categorical-Presentation-Principles.md).* Every object and every property is declared at the **lowest categorical level at which it is generated**, and nowhere else. The rule is "lowest generating level," not "highest generality": generality is correct for the deflationary errors but is itself the disease for the inflationary ones. Its five instances are one defect:

- *object-as-node* — a primitive node for what is an instance of a generic construction;
- *theorem-as-definition* — an implication baked into a definition instead of witnessed as an edge;
- *comparison-as-edge* — a $2$-cell (natural transformation) drawn as a $1$-cell;
- *induced-as-declared* — a derived/whiskered functor declared as primitive;
- *truncation-inflation* — a set-level or $1$-categorical object reached for at a higher level ($\pi_0$ promoted to a homotopy pullback; the genus is the sharp case).

[]{#a2}**A2 — No first-class instance of a generic.** *Seat: @sec-isometry.* Any first-class treatment — a node, a bespoke definition, special-cased notation — of an instance of a generic construction is a defect (the object-as-node instance of [A1](#a1), made explicit because it recurred most). $O(L) = \operatorname{Aut}(L)$, $GL(M) = \operatorname{Aut}_{\mathrm{Mod}}(M)$, Galois and unit groups, $\pi_1$: each is a value of a functor, interrogated through the functor, never declared.

[]{#a3}**A3 — Transport is legal only through the forgetful.** *Seat: @def-transport.* A property transports by pullback (@def-transport) exactly when it is a property of the underlying data the functor sees — i.e. it factors through the forgetful functor. Properties of the underlying set or module (finite, torsion-free) pull back freely; structure-relative ones do not and are declared per node. **Boundary counterexample:** finite generation. The same abelian group $\mathbb Q$ is finitely generated as a $\mathbb Q$-module (rank one) and *not* as a $\mathbb Z$-module (it needs $\{1/n\}$); generation depends on the available operations, so it does not factor through the underlying set (Sage records this as `FinitelyGeneratedAsMagma`, never a bare `FinitelyGenerated`) and is owned at each structured node.

[]{#a4}**A4 — Everything up to equivalence.** *Seat: @sec-pullback-cat.* All categorical statements are up to equivalence; strict equalities of categories are never asserted, and each canonical equivalence carries a named witness ($\mathbf{Ab} \simeq \mathrm{Mod}_{\mathbb Z}$, $\mathrm{Mod}_R \simeq \mathrm{Mod}_{R^{\mathrm{op}}}$). This premise is *why* the isofibration/pseudo-pullback correction (@sec-pullback-cat) is not optional: strict pullbacks are equivalence-invariant only along isofibrations, so "up to equivalence" forces the machinery.

[]{#a5}[]{#h1}**A5 — Homological presentation of properties.** *Seat: @sec-discriminant.* A property is defined by **naming the exact sequence (or diagram) it sits in and the homological invariants that sequence exposes** — not by a prose predicate or a formula about a single map. "The map is injective/iso" is demoted to "the named object ($\operatorname{rad}$, $\operatorname{coker}$, the obstruction class) has such-and-such position in the named sequence." Corollaries:

- []{#h2}*H2 — name the sequence, not the leg-condition.* Nondegeneracy is $\operatorname{rad} = 0$ in the radical sequence; perfectness is that sequence extended by $\to 0$; the implication perfect $\Rightarrow$ nondegenerate is read off one sequence, not asserted separately.
- []{#h3}*H3 — name the obstruction object/class.* $\operatorname{rad}(M)$, $A_L = \operatorname{coker}\tilde b = L^{\#}/L$, and the stable orthogonal group $\widetilde O(L) = \ker(O(L) \to O(A_L, q_{A_L}))$ get first-class status; the prose predicate is a dead end and the obstruction is the object of interest.
- []{#h4}*H4 — LES over SES; the connecting map is data.* Wherever a functor is applied to a short exact sequence (localization, $\operatorname{Hom}$, $\otimes$, completion), display the governing long exact sequence with its connecting maps named — that is where torsion, nondegeneracy-failure, and the discriminant obstruction appear ($T(M) = \operatorname{Tor}_1^R(M, K/R)$ is the localization LES's connecting object).
- []{#h5}*H5 — the discriminant lives in a comparison of two sequences.* $A_L$ is presented as $L^{\#}/L \cong \operatorname{coker}\tilde b$ inside the comparison (@def-metric-dual and @thm-double-complex), never as a bare cokernel formula; defining it by formula before the sequence that gives it meaning is a convention violation, not a nit.
- []{#h6}*H6 — functoriality is a named domain restriction.* When a construction is functorial only on a subcategory, name that subcategory ($\operatorname{Core}$ for the discriminant, the monomorphism subcategory for index, the free locus for basis-dependent constructions) rather than qualifying naturality in prose.
- []{#h7}*H7 — invariants land through the exact/homotopy structure.* Genus is $\pi_0$ of a fiber sequence; index is $\lvert G/H\rvert$ with $G/H$ the named coset object; cardinality is $\pi_0(\mathbf{Set}^{\simeq}) \to \mathbf{Card}$. This is [A5](#a5) one categorical level up: the "sequence" is the fiber sequence and the "obstruction" is the $\pi_1$-orbit data the invariant quotients away.

## Forms and lattices {#sec-forms-lattices}

[]{#forms-and-lattices}

**Nondegenerate is not unimodular.** *Seat: @sec-forms.* Nondegeneracy is injectivity of the polarization $\tilde b : L \to L^{\vee}$; unimodularity/perfectness is bijectivity (Mathlib anchors: `LinearMap.BilinForm.Nondegenerate`, `LinearMap.IsPerfPair`). They coincide only when the determinant is a unit.
Conflating them deletes $\operatorname{coker}(\tilde b) = L^{\vee}/L$ and with it the entire discriminant theory.
The lattice category declares the **nondegenerate** notion; unimodularity is a further property-defined replete full subcategory, entered by a real membership proof through the canonical inclusion.

**The defining datum is the W-valued form, not a map to a dual.** *Seat: @sec-forms.* An object is $(M,\, b : \operatorname{Sym}^2 M \to W)$ over a PID/Dedekind domain $R$ with fraction field $K$; the map-to-dual picture survives only as the derived **polarization** $\tilde b : M \to \operatorname{Hom}(M, W)$ (currying, no freeness needed).
The value module $W$ is a structural parameter, never a convention: $\operatorname{Hom}(A, R) = 0$ for finite $A$, so "$b$ as a map to $\operatorname{Hom}(-, R)$" is empty exactly where discriminant forms live.
Free restriction with $W = R$ recovers lattices; finite-torsion restriction with $W = K/R$ (for $\mathbb{Z}$: $\mathbb{Q}/\mathbb{Z}$, even refinement $\mathbb{Q}/2\mathbb{Z}$) recovers discriminant forms — special cases recovered, never defined independently.

**The total category and its variance.** *Seat: @sec-forms; convention fixed in @sec-el.* The bilinear category is the category of elements of the presheaf of $W$-valued bilinear forms on f.g. $R$-modules, in the standard sense (no $(-)^{\mathrm{op}}$), so a morphism $(M, b_M) \to (N, b_N)$ has underlying map $f : M \to N$ with $f^{*} b_N = b_M$ and the projection to $\mathrm{Mod}_R$ is covariant.
The variance is forced, not chosen: the datum is the $W$-valued form and a form morphism pulls the target form back to the source. The integral sign is the Grothendieck construction, not an end or coend.
*Supersession:* the root presheaf is the **full bilinear** one — symmetry, skew-symmetry, alternating, nondegeneracy, perfectness are property-defined replete full subcategories of it.
The earlier working presheaf that baked symmetry into the construction is superseded.

**Alternating vs skew-symmetric.** *Seat: @sec-forms.* $\mathrm{Alternating} \subseteq \mathrm{SkewSymmetric}$ holds unconditionally (polarize $b(x{+}x',\, x{+}x') = 0$); the converse holds exactly when multiplication by $2$ on $W$ is injective (injectivity suffices — invertibility was overkill).
Both predicates are owned at the bilinear category; the implication is a generated inclusion with the polarization identity as witness.
*Supersession:* the intermediate "correction" that nested the alternating definition inside the skew subcategory was rejected — it baked a theorem into a definition and diverged from the Mathlib anchor (`IsAlt` is defined on bilinear maps directly).

**Bilinear and quadratic are parallel hierarchies.** *Seat: @sec-polarization-functors.* $\operatorname{diag} : \mathrm{SymBil} \to \mathcal{Q}$ ($b \mapsto q(x) = b(x,x)$) and $\operatorname{polar} : \mathcal{Q} \to \mathrm{SymBil}$ satisfy $\operatorname{polar} \circ \operatorname{diag} = 2$ and $\operatorname{diag} \circ \operatorname{polar} = 2$; they are equivalences only when $2$ is invertible on $W$.
On the torsion side $W = \mathbb{Q}/\mathbb{Z}$ has $2$-torsion — exactly where even discriminant forms live — so the two hierarchies are genuinely parallel, related by the polarization functors, with equivalences only under hypotheses.
`QuadraticModuleCat` is the Mathlib anchor for the quadratic side, never the definition of lattice morphisms.
*Supersession:* earlier mapping rows identifying lattice hom-sets with `QuadraticMap.Isometry` are wrong identifications.
Even lattices / quadratic discriminant forms arise by **pullback along the bilinearization functor**, not as an "even cut" of bilinear objects — the same one mechanism used twice.

**Derived categories are expressions, never declared.** *Seat: @sec-derived.* In final form:

$$
\mathbf{Lat}_R = \mathcal{B}_{R,R}\big[\mathrm{Symmetric} \wedge \mathrm{Nondegenerate} \wedge \pi^{*}(\text{f.g.} \wedge \text{projective})\big]
$$

(projective of finite rank is the definition; over a PID this is finitely generated free); $\mathbf{Unimod}_R$ replaces Nondegenerate by Perfect (which implies it);

$$
\mathbf{DiscBil}_{\mathbb{Z}} = \mathcal{B}_{\mathbb{Z},\,\mathbb{Q}/\mathbb{Z}}\big[\mathrm{Symmetric} \wedge \mathrm{Nondegenerate} \wedge (U \circ \pi)^{*}(\mathrm{Finite})\big];
$$

$\mathbf{DiscQuad}_{\mathbb{Z}}$ is the pullback of $\mathbf{DiscBil}_{\mathbb{Z}}$ along bilinearization.
The AG negative-definite convention ($A_n$ negative-definite) is a normalization on objects, not a change of category.

## The discriminant construction and the exact-sequence package {#sec-discriminant-package}

[]{#the-discriminant-construction-and-the-exact-sequence-package}

*Seat: @sec-discriminant.*

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

## Automorphism groups {#sec-automorphism-groups}

[]{#automorphism-groups}

*Seat: @sec-isometry.*

**O is an instance, never a node.** $\operatorname{Aut} : \operatorname{Core}(\mathcal{C}) \to \mathbf{Grp}$ is one generic construction; $O(X) = \operatorname{Aut}(X)$ at an object of the forms category, and $\operatorname{Isom}(X, Y) = \operatorname{Hom}_{\operatorname{Core}(\mathcal{C})}(X, Y)$.
Nothing about $O$ is data.
Where bases exist (the free restriction), passing to a basis induces the faithful representation $O(L) \hookrightarrow \mathrm{GL}_n(R)$ — the precise sense in which $O(L)$ "is" a matrix group.

**The torsion side is a quotient of a matrix group, never a subgroup.** For $A = \mathbb{Z}^n / D\mathbb{Z}^n$ with mixed invariant factors, $A$ is free over no ring; entrywise reduction on the stabilizer of $D\mathbb{Z}^n$ surjects onto $\operatorname{End}(A)$ with a congruence kernel, and restricted to $\mathrm{GL}_n(\mathbb{Z})$ it is *not* onto $\operatorname{Aut}(A)$ (multiplication by $2$ on $\mathbb{Z}/5$ has no lift in $\mathrm{GL}_1(\mathbb{Z}) = \{\pm 1\}$). Hence $O(A_L)$ is canonically a quotient of a congruence-type matrix group, finitely presented by generators and relations; any realization *as* matrices is incorrect, not merely lossy (Hillar–Rhea 2007). The **homocyclic** exception ($d_1 = \cdots = d_n = d$): $A$ is free over $\mathbb{Z}/d$ and $O(q) \le \mathrm{GL}_n(\mathbb{Z}/d)$ genuinely — e.g. $A_2$'s discriminant group $\mathbb{Z}/3$.

**$\operatorname{Isom}(L, M)$, when nonempty, is an $(O(L), O(M))$-bitorsor** — free transitive actions on both sides, statable with standard action machinery.

## Invariants and their evaluation {#sec-invariants}

[]{#invariants-and-their-evaluation}

**Cardinality is total on Sets.** *Seat: @sec-constructors.* It is an invariant on isomorphism classes, $\pi_0(\mathbf{Set}^{\simeq}) \to \mathbf{Card}$ — $\mathbb{Z}$ has one.
Not a functor into a discrete category (morphisms exist between sets of unequal cardinality).
A finite presentation (a chosen $X \simeq \mathrm{Fin}\, n$) is the **evaluation witness** where computation happens; a presentation is never the home of the invariant it evaluates.
Every structured object reaches set-level invariants through its forgetful functor and never re-declares them.
*Supersession:* the original "cardinal-equipped finite sets" home is retracted (S5 at-source correction).

**Index.** *Seat: @sec-isometry.* The home is the subgroup/monomorphism; the value is the cardinality of the coset space $G/H$ — which for non-normal $H$ is a plain type, exactly as Mathlib defines `Subgroup.index := Nat.card (G ⧸ H)`. The identity "index $= \lvert\operatorname{coker}\rvert$" is a **theorem under the abelian hypothesis, not a definition**: categorical cokernels exist over groups but compute $\lvert H / \text{normal-closure}(\operatorname{im} f)\rvert$ — the wrong number for non-normal images.
*Supersession (twice over):* both the original "sited on morphisms" phrasing and the later "objects of the arrow category over a has-cokernels base" gate are falsified — the gate was neither necessary (the coset space needs no cokernels) nor sufficient (cokernels exist over groups and give the wrong answer).
The group-index row can be written, correctly, via the coset space.

**(Co)limits are sited at the category-theory level.** *Seat: @sec-constructors.* Limits, colimits, products, coproducts are defined once for arbitrary categories, with Type-level (and each concrete category's) limits as instances; siting them at an instance re-implements them at every other instance (the same failure one level up).
Universal-property witnesses (limit cones, biproducts) are the identification obligations, not constructors.

**Genus is set-level.** *Seat: @sec-genus-sec.* The genus of $L$ is the fiber of $\pi_0 \operatorname{Core}(\mathbf{Lat}_{\mathbb{Z}}) \to \pi_0 \prod_v \operatorname{Core}(\mathbf{Lat}_{R_v})$ over the class of the local profile of $L$ — a **set-level pullback**. *Supersession:* the homotopy-pullback formula "genus $= \pi_0(\text{homotopy pullback})$" is false — $\pi_0$ does not commute with homotopy pullbacks; the components of the homotopy fiber over $[L]$ form $O(L) \backslash \prod_v O(L_v)$, typically uncountable.
If the groupoid is wanted, it is the classical adelic double coset with restricted products doing real work.
The 1-truncation is the content; higher-categorical machinery deployed decoratively silently changes the object.

**Left and right modules are distinct categories.** *Seat: @sec-module-categories.* Right $R$-modules are modules over $R^{\mathrm{op}}$ — a different category, with the commutative-case identification carried by a canonical functor (a hypothesis-bearing equivalence with a natural-isomorphism witness), not an equality.
$\mathrm{Mod}_R$, $\mathrm{Mod}_{R^{\mathrm{op}}}$, and ${}_{R}\mathrm{BiMod}_S$ are distinct objects of the presentation; there is one parameterized module family, and "right modules" is not a separate primitive kind.

## Relation kinds are not fungible {#sec-relation-kinds}

[]{#relation-kinds-are-not-fungible}

*Seat: @sec-axioms and [Categorical Presentation Principles](Categorical-Presentation-Principles.md).*

Identity, definitional equality, equivalence, isomorphism, forgetful image, chosen presentation, property, ingredient, and example are distinct relation kinds, and every recorded claim names which one it makes.
Standing consequences:

- a bilinear form is an *ingredient* of a lattice, not the lattice or its category;

- a chosen basis is not the property of being finite free; a computational enumeration is not the property of finiteness or countability;

- an equivalence of categories does not erase the design choice between property-defined objects and objects carrying chosen data;

- a worked example (the standard rank-n lattice, $\mathbb{F}_2$) is an *instance*, never category-level vocabulary — define the general construction and instantiate (singleton reification is the recorded failure mode);

- a proof that a local declaration agrees with a standard one is evidence the local declaration is redundant or misplaced, not evidence it belongs where it is.

Absence of a single prepackaged upstream name is **not** absence of the mathematics: standard mathematics is frequently compositional (full subcategories cut by properties, categories of elements, transported functors), and a claimed gap is admissible only with search evidence — what was searched, the nearest notions found and distinguished (negative-finding bar; see the [Lean–Sage Integration Model](Lean-Sage-Integration-Model.md)).
