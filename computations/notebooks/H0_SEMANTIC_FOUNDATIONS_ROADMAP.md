# Semantic foundations for the \(H^0(\mathcal O(4,4))^\tau\) research program

## Purpose

The research begins with curves in
\[
H^0\!\left(\mathbf P^1\times\mathbf P^1,\mathcal O(4,4)\right)^\tau,
\]
their behavior at the fixed points of \(\tau\), and the loci on which the
corresponding curves acquire prescribed singular behavior.  The foundational
program must therefore make those curve calculations mathematically natural
before it attempts to package the later K3 and Enriques constructions.

The intended result is a Sage-native language in which a notebook can move
without translation among:

- commutative rings, ideals, quotients, and localizations;
- local rings, residue fields, cotangent spaces, and completions;
- sheaves of rings, ringed spaces, and locally ringed spaces;
- affine schemes, scheme points, local schemes, and morphisms;
- schemes obtained by gluing affine charts;
- quasi-coherent modules and algebras, relative spectrum and relative Proj;
- invertible modules, divisors, sections, principal parts, and jets;
- curves and surfaces with explicitly named hypotheses;
- representations, group actions, fixed-point functors and their representing
  schemes when representable, and linearized invertible modules;
- families, relative singular subschemes, and constructible parameter loci;
- blowups, strict transforms, conductors, and local intersection numbers;
- cyclic covers and lifted actions.

These are three complementary documents:

1. this roadmap orders the mathematical development by the notebooks that it
   should make possible;
2. [H0_MATHEMATICAL_CATEGORY_ARCHITECTURE.md](H0_MATHEMATICAL_CATEGORY_ARCHITECTURE.md)
   specifies the categories with axioms, replete full subcategories,
   functors, homsets, and method placement;
3. [H0_INVARIANT_CURVE_RESEARCH_SPECIFICATION.md](H0_INVARIANT_CURVE_RESEARCH_SPECIFICATION.md)
   states the invariant \((4,4)\)-curve problem, the reductions already known,
   and the forms in which a useful description of its parameter loci may
   appear.

The first notebook is not a universal K3 chart.  It is a local
commutative-algebra notebook in which smooth, nodal, reducible, and
nonreduced curve germs are compared through their actual rings and maps.  The
first return to K3 surfaces occurs only after the branch curves, their
families, and their singular loci can be studied directly.

## The organizing principle

### Mathematical properties determine method availability

A method belongs to the most general category on which its mathematical
definition is valid.  Stronger methods appear when a parent is placed in a
category with an additional axiom:

\[
\mathsf{Schemes}(k)
\supset
\mathsf{Schemes}(k).\mathsf{Reduced}
\supset
\mathsf{Schemes}(k).\mathsf{Normal},
\]

or when several categories imposing independent conditions are joined:

\[
\mathsf{Curves}(k)
=
\mathsf{Schemes}(k).\mathsf{FiniteType}
\cap
\mathsf{Schemes}(k).\mathsf{Separated}
\cap
\mathsf{Schemes}(k).\mathsf{PureDimension}(1).
\]

This has three consequences.

1. A construction places its output in every category with an axiom that
   follows from the construction.  If \(I\) is radical, \(R/I\) is returned
   as a reduced ring.  If \(\mathfrak p\) is prime,
   \(R_{\mathfrak p}\) is returned as a local ring with its maximal ideal,
   residue field, and localization map.
2. A stronger operation is not placed on a larger category merely because it
   is useful in one example.  Intersection theory for smooth proper surfaces
   does not become a method on arbitrary schemes.
3. A coordinate algorithm belongs to the most general mathematically defined
   category on which it is total.  For example, radical computation belongs
   initially to finitely presented \(\mathbf Q\)-algebras in this program.  A chosen
   generators-and-relations presentation is input to the computation, not a
   new full subcategory and not the home of reducedness.

Membership in a full subcategory is the mathematical declaration.  A result
enters a stricter full subcategory only in one of three ways:

1. a cited theorem applies to the construction and establishes the defining
   predicate;
2. the predicate is computed by an actual decision procedure on the
   mathematically specified input category;
3. the predicate follows from an established implication among category
   axioms or replete full subcategories.

Otherwise the result remains in the strongest supercategory whose predicates
are known, or in the category of the mathematical data actually constructed.
Quotient maps, ideals, sections, embeddings, actions, and chosen equations
are legitimate data.  Prose asserting that a predicate holds is not.

There are no proof, certificate, evidence, or trust objects.  No constructor
encodes a proof burden in additional software structure.  A citation belongs
in the mathematical documentation; a computation exposes the ideal, map,
invariant, or predicate value it computed; the result is then placed directly
in the corresponding category.  If neither theorem nor computation applies,
the result remains in the most specific category already established.

### Categories with axioms and categories of additional data are different

A Sage category with an axiom is a replete full subcategory: it has the same
morphisms between its objects as its supercategory.  `Reduced`, `Normal`,
`Noetherian`, and `Smooth` in the appropriate object or arrow category have
this form.

Additional data or a changed notion of morphism produces a category of the
stated objects and arrows instead:

- \(R\)-algebras form the coslice \((R\downarrow\mathsf{CRing})\);
- \(S\)-schemes form the slice
  \((\mathsf{Sch}\downarrow S)\);
- local rings with local homomorphisms are not a full subcategory of
  commutative rings;
- pointed schemes have point-preserving morphisms;
- embedded schemes are arrows with commutative-square morphisms;
- \(G\)-objects form the functor category \([BG,\mathcal C]\);
- polarized schemes, linearized invertible modules, and cyclic-cover building
  data retain additional structure.

Such a category has a projection or forgetful functor to the category
containing the underlying mathematical objects.  This functor need not be
faithful: a morphism of polarized schemes or cyclic-cover data includes a
chosen invertible-module isomorphism, and distinct choices may lie over the
same scheme morphism.  Sage method reuse follows only the mathematical data
actually forgotten; it must not turn the functor into a false
full-subcategory assertion.

### Not every mathematical collection is a category

For a fixed scheme \(X\):

- \(H^0(X,\mathcal F)\) is a module;
- \(\operatorname{Pic}(X)\) is a group of isomorphism classes;
- effective Cartier divisors form a commutative monoid;
- Cartier divisors form an abelian group;
- closed subschemes form a poset under inclusion;
- constructible subsets form a Boolean algebra;
- invertible modules and their isomorphisms form a groupoid.

The category architecture should retain these distinctions.  A new category
name is not introduced merely to provide a namespace.

## What the notebooks establish

The notebooks are the mathematician-facing audit surface.  A notebook
establishes a stage of the program when a mathematician can read it as a
piece of mathematics and can disagree with a displayed construction,
equation, morphism, invariant, or conclusion.

Each foundational notebook should contain:

- a mathematical question stated before the computation;
- the rings, schemes, sheaves, maps, and hypotheses entering the question;
- at least one nontrivial standard construction;
- intermediate objects that explain how the result was obtained;
- a familiar result recovered from those objects;
- contrasting examples on which category membership, and therefore available
  methods, changes;
- outputs whose mathematical type and meaning are visible.

For a parameter-locus investigation, the notebook need not know in advance
which representation will be most useful.  A reasonable output may be:

- a locally closed subscheme;
- a constructible subset written as finite Boolean operations on explicit
  closed and open loci;
- equations together with inequations on named affine charts;
- an incidence correspondence and an explicitly named image operation;
- compatible chartwise conditions;
- a mathematical predicate whose domain, quantifiers, and intermediate
  objects are displayed.

The result must be understandable and falsifiable in principle.  An opaque
object representation, a list of sampled sections, or a bare call such as
`show(X.sing())` does not describe a locus.

## Dependency graph

The program is a directed graph rather than a single linear hierarchy.

```text
categories, homsets, functors
    +--> commutative rings, ideals, modules
    |        +--> local rings and completions
    |        +--> graded and multigraded algebras
    |
    +--> topological spaces, presheaves, and sheaves
             +--> sheaves of rings and modules
             +--> ringed spaces
                     +--> locally ringed spaces

commutative rings + locally ringed spaces
    +--> affine schemes by Spec
             +--> schemes and scheme morphisms
                     +--> affine open covers and gluing
                     +--> local schemes

schemes + sheaves of modules and algebras
    +--> quasi-coherent modules and algebras
             +--> relative Spec and relative Proj
             +--> invertible modules, divisors, and section rings
             +--> principal parts and jets
             +--> blowups through Rees algebras

schemes + local algebra + quasi-coherent modules
    +--> curves, surfaces, and relative singular subschemes
    +--> actions, representations, fixed-point functors, and their representing schemes
    +--> families and constructible parameter loci

invertible modules + relative Spec + actions
    +--> cyclic covers and deck actions

curves + surfaces + invertible modules + actions + families + local singularities
    +--> invariant (4,4)-curve loci

invariant branch curves + cyclic covers
    +--> K3 covers, lifted involutions, and Enriques quotients
```

Some branches can advance in parallel.  Cyclic-cover algebra needs invertible
modules and relative spectrum, but it does not need a completed classification
of invariant curve singularities.  The geometric conclusions about a
particular cover do need the corresponding conditions on its branch divisor
and action.

## Mathematical stages and notebooks

### Stage 1: local algebra at points

**Mathematical language**

- `CommutativeRings()` and `CommutativeAlgebras(k)`;
- ideals, prime ideals, maximal ideals, and radical ideals;
- quotients and localizations with their canonical maps;
- reduced rings, domains, Noetherian rings, and regular rings;
- local rings with local homomorphisms;
- Noetherian, regular, Artinian, Cohen-Macaulay, Gorenstein, and complete
  local categories;
- Jacobson, G-rings, \(J\)-2, universally catenary, Nagata,
  quasi-excellent, and excellent rings, including the implications governing
  finite normalization;
- modules of differentials, Fitting ideals, cotangent spaces, associated
  graded rings, and completions.

**First notebook**

Compare the following pointed affine curves over \(\mathbf Q\):

\[
\begin{aligned}
C_{\mathrm{sm}}&=V(y-x^2),\\
C_{\mathrm{node}}&=V(xy),\\
C_{\mathrm{dbl}}&=V(y^2),
\end{aligned}
\qquad p=(0,0).
\]

For each example, the notebook constructs the quotient map, the prime or
maximal ideal defining \(p\), the localization
\(\mathcal O_{C,p}\), its maximal ideal and residue field, and the vector
space
\[
\mathfrak m_p/\mathfrak m_p^2.
\]
It compares Krull dimension with embedding dimension, displays the reduction
of the doubled line, computes the relevant module of differentials, and
relates the tangent cone to the associated graded ring.  The smooth point,
node, and doubled line must remain visibly different throughout the
calculation.

This notebook establishes mathematical usefulness immediately: it performs
ordinary local algebra that will later be reused at singular points of
invariant curves.

### Stage 2: sheaves, locally ringed spaces, affine schemes, and points

**Mathematical language**

- presheaves and sheaves of sets and rings on a topological space;
- restriction, sheafification, stalks, and maps on stalks;
- ringed spaces and morphisms
  \((f,f^\#):(X,\mathcal O_X)\to(Y,\mathcal O_Y)\);
- locally ringed spaces and the requirement that every induced stalk map be
  local;
- schemes as locally ringed spaces locally isomorphic to affine spectra;
- the contravariant spectrum functor;
- affine schemes over a base;
- closed immersions from quotients and open immersions from localizations;
- scheme points, \(T\)-valued points, and geometric points as distinct
  notions;
- pointed schemes and point-preserving morphisms;
- the local-scheme functor
  \((X,x)\mapsto\operatorname{Spec}\mathcal O_{X,x}\);
- induced local homomorphisms and residue-field maps;
- fiber products and base change.

**Notebook**

The rings from Stage 1 are transported through `Spec`.  On a standard open
cover, the notebook constructs the structure sheaf from localizations,
computes selected stalks, and displays the local homomorphism induced by a
scheme morphism.  It then displays the reversal of affine arrows, identifies
closed and principal-open subschemes, and forms the fiber product of
\[
\mathbf A^1_u\xrightarrow{\,t\mapsto u^2\,}\mathbf A^1_t
\quad\text{and}\quad
\mathbf A^1_v\xrightarrow{\,t\mapsto v^3\,}\mathbf A^1_t.
\]
It recovers
\(\operatorname{Spec}\mathbf Q[u,v]/(u^2-v^3)\) from the tensor product and
identifies the resulting cusp geometrically.  On \(\mathbf A^1_{\mathbf Q}\)
it also compares a rational point with the closed point defined by
\((x^2+1)\), its residue field \(\mathbf Q(i)\), and the corresponding point
morphisms.

The quotient, localization, residue, and induced local maps are ordinary
morphisms in named homsets and are composed there.  Coordinate substitutions
serve only as presentations of those morphisms.

### Stage 3: affine open covers, gluing, and products

**Mathematical language**

- open immersions and overlap isomorphisms;
- affine open covers with gluing isomorphisms and the scheme obtained by
  gluing;
- chosen covers with maps to two given covers;
- products and fiber products of schemes;
- separatedness through the diagonal;
- base change of chosen affine open covers and their gluing data.

**Notebook**

Construct \(\mathbf P^1\) from its two standard affine charts and their
\(\mathbf G_m\) overlap.  Construct
\(\mathbf P^1\times\mathbf P^1\) as the scheme product and recover its four
standard affine charts from the product cover.  Display the two
projections, the overlap maps, and one closed subscheme whose equations are
translated across charts.

Products of projective spaces enter here as an example of general products
and gluing.  They do not determine the scope of the foundational theory.

### Stage 4: quasi-coherent modules, divisors, and sections

**Mathematical language**

- `QCoh(X)` for every scheme \(X\), and `Coh(X)` for locally Noetherian
  \(X\);
- finitely presented and finite locally free replete full subcategories;
- invertible modules and the Picard groupoid;
- the Picard group;
- quasi-coherent \(\mathcal O_X\)-algebras and relative spectrum;
- graded quasi-coherent algebras and relative Proj;
- global sections and zero schemes;
- regular sections and effective Cartier divisors;
- Cartier and Weil divisors under their respective hypotheses;
- pullback of invertible modules and zero schemes along every morphism, and
  pullback of effective Cartier divisors along flat morphisms or, for a
  locally Noetherian source, morphisms for which no associated point of the
  source maps into the divisor;
- section rings and multigraded section rings.

**Notebook**

On \(Y=\mathbf P^1\times\mathbf P^1\), construct the projections and the
invertible modules
\[
\mathcal O_Y(a,b)
=
\operatorname{pr}_1^*\mathcal O_{\mathbf P^1}(a)
\otimes
\operatorname{pr}_2^*\mathcal O_{\mathbf P^1}(b).
\]
Recover
\[
\operatorname{Pic}(Y)\cong\mathbf Z^2,\qquad
h^0(Y,\mathcal O(a,b))=(a+1)(b+1)
\quad(a,b\geq 0),
\]
and the intersection formula
\[
(a,b)\cdot(c,d)=ad+bc.
\]
As relative affine and projective constructions, build
\[
\underline{\operatorname{Spec}}_{\mathbf P^1}
\operatorname{Sym}\bigl(\mathcal O_{\mathbf P^1}(1)\bigr),
\qquad
\underline{\operatorname{Proj}}_{\mathbf P^1}
\operatorname{Sym}\bigl(
\mathcal O_{\mathbf P^1}\oplus\mathcal O_{\mathbf P^1}(1)
\bigr),
\]
and recover their standard chart algebras and transition maps.
Construct zero schemes of sections, distinguish a regular section from a
section defining a non-Cartier zero scheme, and compare restriction of an
invertible module with pullback along a closed immersion.  On the integral
surface \(Y\), every nonzero section of an invertible module is regular, so
the contrasting example must not be fabricated there: return to
\[
X=V(xy)\subset\mathbf A^2
\]
and use the section \(x\in H^0(X,\mathcal O_X)\).  Since \(xy=0\), \(x\) is a
zero-divisor; its zero scheme is one component of \(X\) and is not an
effective Cartier divisor.

The notebook culminates in the adjunction calculation for a smooth divisor
of bidegree \((a,b)\):
\[
p_a=(a-1)(b-1).
\]
In particular, a smooth \((4,4)\)-curve has genus \(9\).

### Stage 5: basic curves and surfaces

**Mathematical language**

- curves as separated finite-type schemes of pure dimension \(1\);
- surfaces as separated finite-type schemes of pure dimension \(2\);
- reduced, integral, geometrically reduced, geometrically integral, normal,
  regular, smooth, proper, projective, Cohen-Macaulay, Gorenstein, and local
  complete-intersection replete full subcategories;
- normalization and irreducible components for reduced locally Noetherian
  curves, arithmetic genus for proper curves, dualizing modules for proper
  Cohen-Macaulay curves, and adjunction for effective Cartier curves on
  smooth surfaces;
- finite normalization of reduced Nagata curves, conductor ideals, branches,
  and local \(\delta\)-invariants;
- scheme germs \((X,x)\), local schemes
  \(\operatorname{Spec}\mathcal O_{X,x}\), and formal completions as distinct
  constructions;
- Rees algebras, blowups, exceptional divisors, total transforms, and strict
  transforms;
- local intersection multiplicity of effective Cartier curves meeting
  properly on a smooth surface;
- smooth locus as an open subscheme;
- the relative singular subscheme
  \(V(\operatorname{Fitt}_d(\Omega_{X/S}))\) for a flat, locally finitely
  presented family whose nonempty fibers are equidimensional of dimension
  \(d\); its underlying set is the nonsmooth locus, and on a fiber over a
  perfect field it is also the nonregular locus.

**Notebook**

Study several divisors on a smooth projective surface:

- a smooth \((4,4)\)-curve;
- a reduced reducible curve;
- a nonreduced divisor;
- a curve with a node;
- a curve with a singularity worse than a node.

For each curve, display its defining section, zero scheme, reduction,
irreducible components, singular closed subscheme, local rings at selected
points, and the invariants justified by its category.  Recover
adjunction for the smooth member and compare arithmetic genus with the
normalization of a singular integral member.

For a proper geometrically connected reduced curve over an algebraically
closed field, let \(C_1,\ldots,C_r\) be its irreducible components and let
\(C_i^\nu\) be their smooth normalizations.  The notebook constructs the
finite normalization and conductor, computes the local
\(\delta\)-invariants, and recovers
\[
p_a(C)=\sum_i g(C_i^\nu)+\sum_p\delta_p-r+1.
\]
On two curves meeting properly in a smooth surface it computes
\[
i_p(C,D)
=
\operatorname{length}\mathcal O_{X,p}/(f,g).
\]
Finally it blows up one named point, displays the exceptional divisor, and
compares total and strict transforms on affine charts.

This stage supplies basic curve fluency before parameter loci defined by
singularity conditions or double covers become central objects.

### Stage 6: actions, fixed subschemes, and invariant sections

**Mathematical language**

- actions of an abstract group as functors \(BG\to\mathcal C\);
- actions of group schemes over a base;
- \(\mathsf{Rep}_k(G)=[BG,\mathsf{Vect}_k]\), invariant subspaces, tensor
  products, duals, and intertwiners;
- the Reynolds operator for finite \(G\) when \(|G|\) is invertible in \(k\),
  and character eigenspaces over a splitting field;
- equivariant morphisms;
- the fixed subscheme of one automorphism as its equalizer with the identity,
  the scheme-theoretic intersection of these equalizers for a finite abstract
  group, and the fixed-point functor for a group-scheme action;
- the replete full subcategory of group-scheme actions whose fixed-point
  functor is represented by a scheme;
- equivariant quasi-coherent modules;
- linearized invertible modules;
- induced representations on global sections;
- invariant subspaces, and isotypic decompositions when the representation
  category is semisimple;
- affine quotients \(\operatorname{Spec}(A^G)\) for finite abstract-group
  actions, and scheme-representable fppf quotients for free actions of finite
  locally free group schemes on affine, quasi-affine, projective, or
  quasi-projective schemes.

**Notebook**

Let
\[
\tau([x_0:x_1],[y_0:y_1])
=
([x_0:-x_1],[y_0:-y_1]).
\]
Construct \(\tau\) as an automorphism of \(Y\), construct its fixed subscheme
as the equalizer of \(\tau\) and the identity, and obtain the four coordinate
corners from that scheme.  Choose the standard linearization of
\(\mathcal O(4,4)\) and compute
\[
H^0(Y,\mathcal O(4,4))=V_+\oplus V_-,
\qquad
\dim V_+=13,\quad \dim V_-=12.
\]
Display the restriction and evaluation maps at the fixed subscheme and
explain their kernels through the chosen linearization.

### Stage 7: families, jets, singular incidence, and parameter loci

**Mathematical language**

- `Schemes(B)` and replete full subcategories defined by properties of the
  structure morphism;
- separated flat finitely presented curve families of pure relative
  dimension \(1\);
- affine spaces of sections and projective linear systems;
- universal sections and universal effective Cartier divisors;
- base change and fibers;
- relative differentials and Fitting ideals;
- principal-parts sheaves \(\mathcal P^m_{X/B}(L)\), jets, and their
  truncation maps;
- the degree-two term of the restricted second jet of a section whose first
  jet vanishes along a section of a smooth relative surface, and the
  discriminant of the resulting quadratic form;
- loci on which
  \(\operatorname{Sing}(D/B)\to B\) is finite, and the Fitting-ideal
  criterion for its pushforward structure sheaf to be finite locally free of
  rank \(r\);
- closed, open, locally closed, and constructible subsets of a parameter
  scheme;
- the direct image of the underlying topological space, its constructibility
  under Chevalley's theorem, its closedness for proper morphisms, and the
  separate scheme-theoretic image.

**Notebook**

For a finite-dimensional subspace \(V\subseteq H^0(X,L)\), construct:

1. the universal section over the affine space \(\mathbf A(V)\);
2. the universal divisor over \(\mathbf P(V)\), using the tautological
   invertible module on \(\mathbf P(V)\);
3. the relative singular subscheme of the universal divisor, with its
   Fitting-ideal equations;
4. its fibers over named sections;
5. its projection to the parameter scheme;
6. on a smooth relative surface with a named section, the first and second
   jets of a universal equation and the nonvanishing locus of the quadratic
   discriminant;
7. on a locus where the singular scheme is finite, the open subsets on
   which its pushforward is finite locally free of rank \(r\), together with
   the corresponding geometric fiber lengths.

For a proper universal divisor \(D\to B\), compare the scheme-theoretic image
of \(\operatorname{Sing}(D/B)\to B\) with its underlying closed subset.  On
a nonproper example, display the direct image as a constructible subset for
which closedness is not automatic.  This notebook supplies the standard
language needed to discuss singular members through
the incidence scheme, its projection, and the precise image operation.

### Stage 8: the invariant \((4,4)\)-curve investigation

This is the first research stage whose principal answer is not known in
advance.  Let
\[
P_+=\mathbf P(V_+)
\]
and let \(\mathcal C_+\subset Y\times P_+\) be the universal invariant
\((4,4)\)-curve.  The notebook investigates:

- the smooth invariant locus;
- the locus of curves through each fixed point;
- the local geometric-\(A_1\) condition at a chosen fixed point;
- its intrinsic expression as the nonvanishing of the discriminant of the
  degree-two term after the first jet vanishes;
- the condition that no further geometric singular point occurs;
- the union over the four fixed points;
- higher singular behavior suggested by the invariant local equations.

The notebook's endpoint is a reasonable, understandable, and in-principle
falsifiable description of the exactly-one-\(A_1\) locus.  The plan does not
prescribe whether the best answer is a locally closed subscheme, a
constructible Boolean expression, equations and inequations, an incidence
description, or a readable predicate.  It does require the parameter scheme,
the maps used, the local and global conditions, and the resulting
mathematical object to be visible.

The exact research questions and the minimum semantic content of such a
description are stated in
[H0_INVARIANT_CURVE_RESEARCH_SPECIFICATION.md](H0_INVARIANT_CURVE_RESEARCH_SPECIFICATION.md).

### Stage 9: cyclic covers and lifted actions

**Mathematical language**

- cyclic-cover building data \((L,s)\) with
  \(s\in H^0(Y,L^{\otimes n})\);
- the finite locally free cover algebra
  \[
  \mathcal O_Y\oplus L^{-1}\oplus\cdots\oplus L^{-(n-1)};
  \]
- relative spectrum and the covering morphism;
- the \(\mu_n\)-action obtained from the grading;
- the zero scheme \(B=Z(s)\) of the defining section for every \(s\);
- when \(s\) is regular, the effective Cartier divisors
  \(B=Z(s)\) and \(R=Z(t)\), where \(t\) is the tautological root section,
  together with \(\pi^*B=nR\);
- when \(s\) is regular and \(n\) is invertible on \(Y\), the etale
  restriction over \(Y\setminus B\) and the ramification divisor
  \(V(\operatorname{Fitt}_0(\Omega_{X/Y}))=(n-1)R\);
- smooth covers when \(n\) is invertible on the base, \(Y\) is smooth over
  the base, and \(B\) is a smooth relative effective Cartier divisor;
- compatible linearizations and lifted group actions.

**Notebook**

Construct a double cover of
\(\mathbf P^1\times\mathbf P^1\) from
\[
L=\mathcal O(2,2),\qquad
s\in H^0(Y,L^{\otimes2}).
\]
Display the cover algebra, the covering morphism, deck involution,
ramification divisor, and canonical-module calculation.  Compare a smooth
branch divisor, a nodal branch divisor, and a branch divisor meeting the fixed
subscheme.  The notebook must make clear which conclusions follow from the
general cyclic-cover category and which require additional branch or action
conditions.

### Stage 10: K3 and Enriques consumers

Only now should the program treat the following as primary outputs:

- smooth K3 double covers branched in \((4,4)\)-curves;
- lifts of \(\tau\) and their fixed subschemes;
- fixed-point-free lifts and Enriques quotients;
- singular K3 models and resolutions;
- nodal del Pezzo quotients;
- fundamental-group calculations;
- period and lattice computations attached to these surfaces.

Each later notebook should consume the general language developed in Stages
1 through 9.  A surface-specific conclusion must not be used to define the
ring, scheme, divisor, action, or singularity operation on which it depends.

## Required category inventory

The following categories with axioms, replete full subcategories, joins, and
categories of additional data must exist before their names are used in a
research notebook.

### Sheaves and locally ringed spaces

- topological spaces, presheaves, sheaves of sets, and sheaves of
  commutative rings;
- sheafification, restriction, stalks, direct image, and inverse image;
- sheaves of modules over a fixed sheaf of rings, including tensor product
  and internal Hom;
- ringed spaces and locally ringed spaces, with local homomorphisms on stalks;
- schemes as the replete full subcategory of locally ringed spaces locally
  isomorphic to affine spectra.

### Commutative algebra

- `Noetherian`, `Artinian`, `Reduced`, `IntegralDomain`, `Normal`, `Regular`,
  `CohenMacaulay`, `Gorenstein`, `Jacobson`, `G-ring`, `J-2`,
  `UniversallyCatenary`, `Nagata`, `QuasiExcellent`, and `Excellent`;
- geometrically reduced and geometrically integral finite-type
  \(k\)-algebras;
- local, complete local, regular local, Artinian local,
  Cohen-Macaulay local, Gorenstein local, and discrete valuation rings;
- ideals over a fixed ring, with prime, maximal, radical, and primary ideals
  as distinguished subsets and with extension and contraction along ring
  morphisms;
- modules over a fixed ring, their finitely presented and finite locally free
  replete full subcategories, tensor, symmetric and exterior powers,
  differentials, and Fitting ideals;
- finitely generated and finitely presented \(R\)-algebras;
- graded and multigraded commutative algebras.

### Schemes and morphisms

- locally Noetherian, Noetherian, reduced, irreducible, connected, integral,
  normal, regular, Cohen-Macaulay, Gorenstein, Jacobson, universally
  catenary, Nagata, quasi-excellent, excellent, pure-dimensional, and
  equidimensional schemes;
- geometrically reduced, geometrically irreducible, geometrically integral,
  geometrically connected, and geometrically normal \(k\)-schemes;
- quasi-compact, quasi-separated, locally finite type, finite type, locally
  finite presentation, finite presentation, monomorphism, immersion, open
  immersion, closed immersion, regular immersion, separated, affine, finite,
  finite locally free of rank \(r\), flat, faithfully flat, quasi-finite,
  finite etale, smooth, unramified, etale, dominant, birational, proper,
  projective, and local complete-intersection morphisms;
- replete full subcategories over \(S\) obtained by applying these properties
  to the structure morphism;
- quasi-coherent algebras, relative spectrum, graded quasi-coherent algebras,
  relative Proj, Rees algebras, and blowups.

### Sheaves and divisors

- quasi-coherent modules on every scheme; coherent modules on locally
  Noetherian schemes; finitely presented, finite locally free of rank \(r\),
  and invertible quasi-coherent modules; torsion-free modules on integral
  schemes; and reflexive coherent modules on locally Noetherian schemes;
- regular sections, effective Cartier divisors, Cartier divisors, Weil
  divisors, divisor classes, the Picard groupoid, and the Picard group;
- section rings, multisection rings, and Cox sheaves and rings, with their
  dependence on the chosen invertible modules or divisor classes explicit;
- principal-parts sheaves, jets, first-jet vanishing along a section, and the
  degree-two term of the restricted second jet on a smooth relative surface.

### Geometry and equivariance

- curves and surfaces as joins of `FiniteType`, `Separated`, and
  `PureDimension(d)`;
- proper, projective, smooth, integral, normal, Cohen-Macaulay, Gorenstein,
  and local complete-intersection replete full subcategories of those joins;
- scheme germs with morphisms represented on neighborhoods, local schemes
  essentially of finite type, affine formal spectra of completed local rings,
  hypersurface germs embedded in smooth local schemes with chosen local
  equations, isolated hypersurface singularities, nodes, and plane curve
  germs geometrically of type \(A_n\);
- representations, actions, equivariant morphisms, fixed-point functors and
  their representing schemes when representable, linearized invertible
  modules, and invariant linear systems;
- flat finitely presented families, relative curves, universal divisors, and
  cyclic-cover building data.

### Parameter loci and quotients

- closed subschemes, open subschemes, locally closed subschemes, and
  constructible subsets as distinct mathematical outputs;
- inverse images, topological direct images under Chevalley hypotheses,
  proper closed images, and scheme-theoretic images, without identifying
  these operations;
- loci on which the relative singular subscheme is finite over the parameter
  scheme, finite locally free rank loci defined by Fitting ideals, and the
  distinction between fiber length and the number of geometric support
  points;
- fppf quotient sheaves, scheme-representable quotients, and the possibility
  that a general quotient is an algebraic space or quotient stack rather than
  a scheme.

The exact implication relations, stability under standard constructions, and
method namespaces are part of the architecture document.  A flat list of
names is not sufficient.

## Routing the existing notebook corpus

The current notebooks record both mathematical source material and abandoned
organizational attempts.  Their calculations should be routed by the
mathematical object they study, not copied wholesale into one new framework.

| Notebook | Mathematical role |
| --- | --- |
| `Commutative_Algebra_Foundations_v2.ipynb` | Prior work on arrows, \(R\)-algebras, quotients, localizations, and prime-local algebra; source material for Stages 1 and 2. |
| `H0_O_P1xP1_4_4.ipynb` | Main invariant-curve research narrative; target consumer of Stages 1 through 8. |
| `Projective_Scheme_Framework.ipynb` | Broad first prototype containing projective, local, sheaf, divisor, action, family, singularity, and cover constructions that must be separated by mathematical ownership. |
| `Projective_Scheme_Framework_v2.ipynb` | Categorical reset for arrows, diagrams, affine spectrum, covers, and gluing; source material for Stages 2 and 3. |
| `Refactor Fixtures/H0_O_P1xP1_5_5.ipynb` | Early section-basis and coordinate example. |
| `Refactor Fixtures/P1xP2_O44_all_monomials.ipynb` | Early monomial enumeration example for multigraded sections. |
| `curves/HandshakeCurves.ipynb` | Later curve algorithms; a consumer of the basic curve language. |
| `curves/curve-ideal-scratchpad.ipynb` | Minimal coordinate work on curve ideals; source material for early affine examples. |
| `archive/Curve Intersection Multiplicities.ipynb` | Prior calculations for local intersection theory. |
| `archive/Misc Toric Geometry.ipynb` | Prior toric calculations that may later supply examples with explicit coordinate presentations. |
| `periods/fermat_quartic_lefschetz_inputs_only.ipynb` | Later period and monodromy consumer. |
| `lattices/integral-lattice-import-failure.ipynb`, `spike-demos/spike_demo.ipynb`, and the lattice, cone, isometry, and Coxeter notebooks under `archive/` | Separate lattice-theoretic program and precedent for high-level mathematical notebooks; not a source of scheme foundations. |
| `preamble.ipynb` | Guide to the common notebook language once the category surface is stable. |
| `Local_Axiom_Probe.ipynb`, `Prime_Localization_Probe.ipynb` | Empty probes whose mathematical questions are absorbed by Stages 1 and 2. |
| `Projective_Framework_Validation.ipynb`, `Kernel_Interrupt_Helper.ipynb` | Operational notebooks with no authority over the mathematical dependency order. |
| `src/dzack_research/preamble/Untitled.ipynb` | Unsettled scratch work with no independent mathematical claim. |

The large first projective framework should be disassembled conceptually:

- ring, ideal, quotient, localization, and local-ring material routes to the
  commutative-algebra categories;
- affine charts and gluing route to affine open covers with gluing data;
- sheaf and invertible-module material routes to `QCoh(X)` and
  `InvertibleModules(X)`;
- divisor and section material routes to their fixed-\(X\) parents;
- curve and surface predicates route to joins and categories with the
  corresponding axioms;
- action and fixed-point material routes to equivariant geometry;
- singularity calculations route to local schemes and hypersurface germs
  embedded in smooth germs with chosen equations;
- cover calculations route to cyclic-cover building data.

No notebook becomes the mathematical home of the full theory merely because
it currently contains code for several of these subjects.

## Source anchors

The mathematical architecture uses the following standard sources:

- [Sage category framework primer](https://doc.sagemath.org/html/en/reference/categories/sage/categories/primer.html)
  for parents, elements, categories, and the generated method hierarchy;
- [Sage categories with axioms](https://doc.sagemath.org/html/en/reference/categories/sage/categories/category_with_axiom.html)
  for categories with axioms and joins;
- [Sage category construction](https://doc.sagemath.org/html/en/reference/categories/sage/categories/category.html)
  for `ParentMethods`, `ElementMethods`, and `MorphismMethods`;
- [Sage homsets](https://doc.sagemath.org/html/en/reference/categories/sage/categories/homsets.html)
  for homset parents and morphisms;
- [Sage invariant modules](https://doc.sagemath.org/html/en/reference/modules/sage/modules/with_basis/invariant.html)
  for invariant submodules under a group action;
- [Stacks, reduced schemes](https://stacks.math.columbia.edu/tag/01IZ);
- [Stacks, morphisms of ringed spaces](https://stacks.math.columbia.edu/tag/0094);
- [Stacks, locally ringed spaces](https://stacks.math.columbia.edu/tag/01HA);
- [Stacks, schemes](https://stacks.math.columbia.edu/tag/01II);
- [Stacks, germs of schemes](https://stacks.math.columbia.edu/tag/04QR);
- [Stacks, relative spectrum](https://stacks.math.columbia.edu/tag/01LQ);
- [Stacks, relative Proj](https://stacks.math.columbia.edu/tag/01O5);
- [Stacks, geometrically reduced schemes](https://stacks.math.columbia.edu/tag/035U);
- [Stacks, normalization](https://stacks.math.columbia.edu/tag/035E);
- [Stacks, Nagata rings](https://stacks.math.columbia.edu/tag/032E);
- [Stacks, excellent rings](https://stacks.math.columbia.edu/tag/07QS);
- [Stacks, smooth morphisms](https://stacks.math.columbia.edu/tag/01V4);
- [Stacks, relative singular locus](https://stacks.math.columbia.edu/tag/0C3H);
- [Stacks, scheme-theoretic image](https://stacks.math.columbia.edu/tag/01R5);
- [Stacks, Chevalley's theorem](https://stacks.math.columbia.edu/tag/054H);
- [Stacks, blowups](https://stacks.math.columbia.edu/tag/01OF);
- [Stacks, strict transforms](https://stacks.math.columbia.edu/tag/080C);
- [Stacks, effective Cartier divisors](https://stacks.math.columbia.edu/tag/0CPG);
- [Stacks, pullback of effective Cartier divisors](https://stacks.math.columbia.edu/tag/01WQ);
- [Stacks, regular sections](https://stacks.math.columbia.edu/tag/01WY);
- [Stacks, the divisor-section correspondence](https://stacks.math.columbia.edu/tag/0847);
- [Stacks, principal parts](https://stacks.math.columbia.edu/tag/09CQ);
- [Stacks, finite locally free rank from Fitting ideals](https://stacks.math.columbia.edu/tag/07ZD);
- [Stacks, normalization and delta invariants of curves](https://stacks.math.columbia.edu/tag/0C1R);
- [Stacks, conductor ideal](https://stacks.math.columbia.edu/tag/0C6L);
- [Stacks, local intersection multiplicity for a Cartier divisor](https://stacks.math.columbia.edu/tag/0B05);
- [Stacks, nodal curves](https://stacks.math.columbia.edu/tag/0C46).

The architecture document records exactly where these definitions enter.
