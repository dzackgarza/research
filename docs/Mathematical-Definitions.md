# Mathematical Definitions

The dependency tree of the program's mathematical objects, stated as definitions in standard language.
Every settled design ruling is **seated** under one of these definitions: the definition says what the object *is*; the [Settled Mathematical Rulings](Settled-Mathematical-Rulings.md) say which choices about it are closed, with their supersession trails.
The generation calculus (classify, factor, lift; property vs structure; transport as factorization) is owned by [Categorical Presentation Principles](Categorical-Presentation-Principles.md); vocabulary is governed by the [Mathematical Language Style Guide](Mathematical-Language-Style-Guide.md); Sage's actual category framework is enumerated in the [Sage Category Framework Inventory](Sage-Category-Framework-Inventory.md).
Provenance for everything here is the [#251](https://github.com/dzackgarza/research/issues/251) record.

Throughout, $R$ is a commutative ring — the arithmetic fibers take $R$ a PID or Dedekind domain with fraction field $K$ — and $W$ is an $R$-module, the **value module** of a form.
Notation carries claims: $\hookrightarrow$ asserts a replete full subcategory.

## 1. Module categories

**1.1 (One module family.)** For a ring $A$, $\mathrm{Mod}_A$ is the category of left $A$-modules.
Right $R$-modules are $\mathrm{Mod}_{R^{\mathrm{op}}}$ — the same parameterized family at a different ring, never a separate primitive kind.
Bimodules carry two forgetful functors

$$
\mathrm{Mod}_R \xleftarrow{\;U_L\;} {}_{R}\mathrm{BiMod}_S \xrightarrow{\;U_R\;} \mathrm{Mod}_{S^{\mathrm{op}}},
$$

and for commutative $R$ the identification $\mathrm{Mod}_R \simeq \mathrm{Mod}_{R^{\mathrm{op}}}$ is a hypothesis-bearing equivalence witnessed by a natural isomorphism, not an equality.

**1.2 (The tower.)** The algebraic tower is generated from magmas by four subcategory inclusions — associativity, commutativity, unitality, inverses — with monoids, groups, and abelian groups arising as intersections, never as new declarations.
The abelian landing is identified with the $\mathbb{Z}$-fiber of the module family, $\mathbf{Ab} \simeq \mathrm{Mod}_{\mathbb{Z}}$, and $\mathbb{Z}$ initial in rings gives base change $\mathrm{Mod}_{\mathbb{Z}} \to \mathrm{Mod}_R$ along the unique $\mathbb{Z} \to R$.

*Seated rulings:* [left/right modules are distinct categories](Settled-Mathematical-Rulings.md#invariants-and-their-evaluation).

## 2. Axioms as subcategories; transport

**2.1 (Axiom.)** An axiom on a category $\mathcal{C}$ is a **property-defined replete full subcategory**, declared once at the node that owns the property:

$$
\iota_A : \mathcal{C}.A \hookrightarrow \mathcal{C}.
$$

A proof that an object satisfies $A$ is a factorization through $\iota_A$.

**2.2 (Transport.)** For a functor $F : \mathcal{C} \to \mathcal{D}$ and a declared $\mathcal{D}.P \hookrightarrow \mathcal{D}$, the transported subcategory is the pullback

$$
\mathcal{C}.P \;=\; \mathcal{C} \times_{\mathcal{D}} \mathcal{D}.P .
$$

This single rule generates every transported axiom; a property is declared at the highest node where it is well defined and only pulled back below.

**2.3 (Derived expressions.)** Categories built from declared axioms by intersection, pullback, and the constructors of §9 are **expressions**; they are never re-declared as primitive nodes.

**2.4 (Theorem-witness inclusions.)** Inclusions such as $\mathrm{PID} \subset \mathrm{UFD} \subset \mathrm{Dom}$ are full subcategory inclusions whose witness is a theorem rather than a defining axiom; they are recorded as such.

**2.5 (Property vs structure.)** A *property* of a category is a lift of its classifying point through a full inclusion (being abelian, being a groupoid, having cokernels); a *structure* is a lift through a forgetful functor that is not full (a monoidal structure — one category may carry several: $\otimes$ and $\oplus$ on modules, orthogonal sum on forms).

*Seated rulings:* the calculus itself is in [Categorical Presentation Principles](Categorical-Presentation-Principles.md); [relation kinds are not fungible](Settled-Mathematical-Rulings.md#relation-kinds-are-not-fungible).

## 3. Bilinear and quadratic form categories

**3.1 (The presheaves.)** The two generating objects of the forms frame are the presheaves

$$
\operatorname{Bil}_{R,W},\ \operatorname{Quad}_{R,W} \;:\; \mathrm{Mod}_R^{\mathrm{op}} \longrightarrow \mathbf{Set},
$$

sending a module to its $W$-valued bilinear forms, respectively quadratic maps, acting by pullback along module maps.

**3.2 (Categories of elements.)** The total form categories are the Grothendieck constructions

$$
\mathcal{B}_{R,W} \;=\; \operatorname{El}\!\big(\operatorname{Bil}_{R,W}\big)^{\mathrm{op}},
\qquad
\mathcal{Q}_{R,W} \;=\; \operatorname{El}\!\big(\operatorname{Quad}_{R,W}\big)^{\mathrm{op}},
$$

with projections $\pi : \mathcal{B}_{R,W} \to \mathrm{Mod}_R$.
The variance is chosen so that a morphism $(M, b_M) \to (N, b_N)$ has underlying map $f : M \to N$ with $f^{*} b_N = b_M$.
The defining datum is always the $W$-valued form; the map-to-dual picture appears only as the derived polarization of 3.4.

**3.3 (Form axioms at the total.)** Owned at $\mathcal{B}_{R,W}$, each a property-defined replete full subcategory: symmetric, skew-symmetric, alternating ($b(x,x) = 0$), nondegenerate, perfect, and even ($b(x,x) \in 2W$). The implications

$$
\mathrm{Perfect} \Rightarrow \mathrm{Nondegenerate},
\qquad
\mathrm{Alternating} \Rightarrow \mathrm{SkewSymmetric}
$$

hold unconditionally, and skew-symmetric implies alternating exactly when multiplication by $2$ is injective on $W$.

**3.4 (Polarization of a form.)** For $(M, b)$, currying gives the polarization

$$
\tilde b : M \longrightarrow \operatorname{Hom}_R(M, W),
$$

requiring no freeness.
**Nondegenerate** means $\tilde b$ injective; **perfect** means $\tilde b$ an isomorphism.

*Seated rulings:* [the W-valued form is the defining datum](Settled-Mathematical-Rulings.md#forms-and-lattices) · [the total category and its variance](Settled-Mathematical-Rulings.md#forms-and-lattices) · [alternating vs skew-symmetric](Settled-Mathematical-Rulings.md#forms-and-lattices) · [nondegenerate is not unimodular](Settled-Mathematical-Rulings.md#forms-and-lattices).

## 4. The polarization functors

Between the symmetric-bilinear and quadratic hierarchies:

$$
\operatorname{diag} : \mathrm{SymBil}_{R,W} \to \mathcal{Q}_{R,W},
\quad b \mapsto \big(x \mapsto b(x,x)\big);
\qquad
\operatorname{polar} : \mathcal{Q}_{R,W} \to \mathrm{SymBil}_{R,W},
\quad q \mapsto \big((x,y) \mapsto q(x{+}y) - q(x) - q(y)\big),
$$

satisfying

$$
\operatorname{polar} \circ \operatorname{diag} \;=\; 2 \;=\; \operatorname{diag} \circ \operatorname{polar},
$$

hence mutually inverse equivalences exactly when $2$ is invertible on $W$.
The two hierarchies are genuinely parallel wherever $W$ has $2$-torsion.
On the discriminant fiber the **bilinearization**

$$
\beta \;=\; \big(\tfrac{1}{2}\big)_{*} \circ \operatorname{polar}
\;:\; \mathcal{Q}_{\mathbb{Z},\, \mathbb{Q}/2\mathbb{Z}} \longrightarrow \mathrm{SymBil}_{\mathbb{Z},\, \mathbb{Q}/\mathbb{Z}}
$$

composes the generic polarization with pushforward along $\mathbb{Q}/2\mathbb{Z} \xrightarrow{\;\sim\;} \mathbb{Q}/\mathbb{Z}$, $w \mapsto w/2$.

*Seated rulings:* [bilinear and quadratic are parallel hierarchies](Settled-Mathematical-Rulings.md#forms-and-lattices).

## 5. Derived arithmetic categories

All of the program's headline categories are expressions in the frame above (2.3); none is declared.

**5.1 (Lattices.)**

$$
\mathbf{Lat}_R \;=\; \mathcal{B}_{R,R}\big[\, \mathrm{Symmetric} \wedge \mathrm{Nondegenerate} \wedge \pi^{*}(\text{f.g.} \wedge \text{projective}) \,\big],
$$

the value module being $R$ itself; over a PID, finitely generated projective means finitely generated free.
The AG **negative-definite convention** ($A_n$ negative-definite) is a normalization on objects, not a change of category.

**5.2 (Unimodular lattices.)** $\mathbf{Unimod}_R$ replaces Nondegenerate by Perfect in 5.1 (which implies it).

**5.3 (Even lattices.)** $\mathbf{EvenLat}_{\mathbb{Z}} = \mathbf{Lat}_{\mathbb{Z}} \cap \mathcal{B}[\mathrm{Even}]$, the intersection taken inside $\mathcal{B}_{\mathbb{Z},\mathbb{Z}}$.

**5.4 (Discriminant bilinear forms.)**

$$
\mathbf{DiscBil}_{\mathbb{Z}} \;=\; \mathcal{B}_{\mathbb{Z},\, \mathbb{Q}/\mathbb{Z}}\big[\, \mathrm{Symmetric} \wedge \mathrm{Nondegenerate} \wedge (U \circ \pi)^{*}(\mathrm{Finite}) \,\big],
$$

the finiteness axiom pulled back from sets through the underlying-set functor (2.2). In general the torsion fiber takes $W = K/R$.

**5.5 (Discriminant quadratic forms.)** The quadratic discriminant category is the pullback of $\mathbf{DiscBil}_{\mathbb{Z}}$ along the bilinearization $\beta$ of §4 — quadratic objects whose bilinearization is a discriminant form, **not** an even cut of bilinear objects.

*Seated rulings:* [derived categories are expressions, never declared](Settled-Mathematical-Rulings.md#forms-and-lattices).

## 6. The discriminant construction and the exact-sequence package

**6.1 (Discriminant form of a lattice.)** For nondegenerate integral $L$,

$$
A_L \;=\; \operatorname{coker}\big(\tilde b : L \to \operatorname{Hom}(L, R)\big)
$$

carrying the induced $K/R$-valued form.
The discriminant construction is the functor "cokernel of polarization with induced form," from the free-nondegenerate restriction to the finite-torsion restriction, declared **on cores** (§7): it is functorial for isometries, not for arbitrary form-preserving maps.

**6.2 (The three sequences.)** Kernel-checked diagram lemmas, never re-encoded informally:

*Radical sequence.* $\operatorname{rad}(M) = \ker \tilde b$ and

$$
0 \to \operatorname{rad}(M) \to M \to \operatorname{Hom}(M, W)
$$

is exact; nondegeneracy is $\operatorname{rad} = 0$, and exactness continued by $\to 0$ is precisely perfectness.

*Base-change sequence.* With $T(M)$ the torsion submodule,

$$
0 \to T(M) \to M \to M \otimes_R K,
$$

and inside $L \otimes K$ the metric dual is

$$
L^{\#} \;=\; \{\, x \in L \otimes K \;:\; b_K(x, L) \subseteq R \,\}.
$$

*Comparison.* A map of the two sequences realizes $\operatorname{Hom}(L, R) \cong L^{\#} \subseteq L \otimes K$ over $L \hookrightarrow L^{\#}$, and

$$
A_L \;=\; L^{\#}/L \;\cong\; \operatorname{coker}(\tilde b).
$$

This comparison is the **once-only** sanctioned realization of the dual inside the rational span; everything downstream consumes the abstract objects and canonical maps.

*Seated rulings:* [the discriminant construction and the exact-sequence package](Settled-Mathematical-Rulings.md#the-discriminant-construction-and-the-exact-sequence-package).

## 7. Isometry groupoids and automorphism groups

**7.1 (Core; isometries.)** $\operatorname{Core}(\mathcal{C})$ is the maximal subgroupoid.
Isometries and orthogonal groups are instances of generic constructions, never nodes:

$$
\operatorname{Isom}(X, Y) \;=\; \operatorname{Hom}_{\operatorname{Core}(\mathcal{C})}(X, Y),
\qquad
O(X) \;=\; \operatorname{Aut}(X).
$$

When nonempty, $\operatorname{Isom}(L, M)$ is an $(O(L), O(M))$-bitorsor.

**7.2 (Discriminant representation.)** Applying $\operatorname{Aut}$ to the discriminant functor (6.1) yields

$$
O(L) \longrightarrow O(q_L),
$$

with kernel the stable isometry group and image the discriminant representation — generic group-homomorphism machinery.

**7.3 (Matrix realizations.)** On the free restriction a choice of basis induces the faithful representation $O(L) \hookrightarrow \mathrm{GL}_n(R)$ — the precise sense in which $O(L)$ "is" a matrix group.
On the torsion side, for $A = \mathbb{Z}^n / D\mathbb{Z}^n$ with mixed invariant factors, $O(A)$ is canonically a **quotient** of a congruence-type matrix group and not a subgroup of any $\mathrm{GL}_n$; the homocyclic case $A \cong (\mathbb{Z}/d)^n$ is the genuine exception, with $O(q) \le \mathrm{GL}_n(\mathbb{Z}/d)$.

**7.4 (Index.)** The home of index is the subgroup (a monomorphism); its value is the cardinality of the coset space $G/H$.
The identity of index with a cokernel cardinality is a theorem under the abelian hypothesis, not a definition.

*Seated rulings:* [O is an instance, never a node](Settled-Mathematical-Rulings.md#automorphism-groups) · [the torsion side is a quotient of a matrix group](Settled-Mathematical-Rulings.md#automorphism-groups) · [index](Settled-Mathematical-Rulings.md#invariants-and-their-evaluation).

## 8. Genus

For each place $v$ let $R_v$ be the corresponding completion.
The local profile of $L \in \mathbf{Lat}_{\mathbb{Z}}$ is its image under $\operatorname{Core}(\mathbf{Lat}_{\mathbb{Z}}) \to \prod_v \operatorname{Core}(\mathbf{Lat}_{R_v})$.
The genus of $L$ is the fiber

$$
\operatorname{gen}(L) \;=\; \text{fiber over } [\,\mathrm{profile}(L)\,] \text{ of }\;
\pi_0 \operatorname{Core}(\mathbf{Lat}_{\mathbb{Z}}) \longrightarrow \pi_0 \prod_v \operatorname{Core}(\mathbf{Lat}_{R_v}),
$$

a **set-level** pullback: two lattices are in one genus exactly when their local profiles agree up to isometry, equivalently when they become isometric adelically.
If the genus *groupoid* is wanted, it is the classical adelic double coset with restricted products doing real work; $\pi_0$ does not commute with homotopy pullbacks, and the 1-truncation is the content.

*Seated rulings:* [genus is set-level](Settled-Mathematical-Rulings.md#invariants-and-their-evaluation).

## 9. Constructors

The generation calculus uses a fixed small set of category-level constructors, each a standard construction applied — never a new notion:

- $\operatorname{El}$ — the category of elements (Grothendieck construction) of a presheaf, generating the form categories of §3;

- $\operatorname{Core}$ — the maximal subgroupoid, generating isometry groupoids (§7) and the domains of core-sited functors (§6, §8);

- $\pi_0$ — connected components, landing invariants at the set level (§8);

- pullback of a replete full subcategory along a functor — the transport rule (2.2);

- intersection of replete full subcategories — derived nodes (2.3).

(Co)limits, products, and coproducts are sited once at the category-theory level with concrete categories as instances; universal-property witnesses are identification obligations, not constructors.

*Seated rulings:* [(co)limits are sited at the category-theory level](Settled-Mathematical-Rulings.md#invariants-and-their-evaluation) · [cardinality is total on Sets](Settled-Mathematical-Rulings.md#invariants-and-their-evaluation).
