# Research specification for invariant \((4,4)\)-curves

## 1. The question

Let
\[
Y=\mathbf P^1_{\mathbf Q}\times\mathbf P^1_{\mathbf Q},
\qquad
L=\mathcal O_Y(4,4),
\]
and let
\[
\tau([x_0:x_1],[y_0:y_1])
=
([x_0:-x_1],[y_0:-y_1]).
\]
Choose the standard \(\tau\)-linearization of \(L\), and write
\[
V=H^0(Y,L)=V_+\oplus V_-
\]
for the eigenspace decomposition.

The central early research question is:

> Describe the parameter set of invariant curves
> \(C_s=Z(s)\), \([s]\in\mathbf P(V_+)\), having exactly one geometric
> singular point, with that singularity a geometric \(A_1\) singularity.

The desired description is not known in advance.  It may emerge as equations
and inequations, a locally closed subscheme, a constructible Boolean
expression, an incidence description, compatible chartwise conditions, or a
mathematical predicate with explicit intermediate objects.  The purpose of
the foundational language is to make all of these forms natural and
comparable.

The investigation is about the curves themselves.  Double covers, K3
surfaces, and Enriques quotients are later consumers.

## 2. Fixed mathematical data

### 2.1 The representation

A monomial
\[
x_0^{4-i}x_1^i y_0^{4-j}y_1^j
\]
has eigenvalue \((-1)^{i+j}\).  Consequently,
\[
\dim V_+
=
\#\{(i,j):0\leq i,j\leq4,\ i+j\text{ even}\}
=3\cdot3+2\cdot2
=13,
\]
and
\[
\dim V_-=12.
\]

The notebook should construct these spaces as eigenspaces of the induced
representation, not merely select a hard-coded monomial list.  The monomial
calculation then gives a readable basis and recovers the dimensions.

### 2.2 The fixed subscheme

The fixed subscheme
\[
F=Y^\tau
\]
is the equalizer of \(\tau\) and \(\operatorname{id}_Y\).  It consists of the
four reduced coordinate corners
\[
p_{00},\ p_{01},\ p_{10},\ p_{11}.
\]

The standard linearization has trivial fiber character at these four points.
It therefore gives evaluation maps
\[
\operatorname{ev}_p:V_+\to L|_p
\]
and hyperplanes
\[
H_p=\mathbf P(\ker\operatorname{ev}_p)
\subset P_+:=\mathbf P(V_+).
\]

The hyperplane \(H_p\) parameterizes invariant curves passing through \(p\).

### 2.3 The local invariant equation

Fix \(p\in F\).  There are regular parameters \(u,v\) at \(p\) for which
\[
\tau(u,v)=(-u,-v).
\]
If \(s\in V_+\), its local equation has the form
\[
f_s(u,v)
=
a_{00}
+a_{20}u^2+a_{11}uv+a_{02}v^2
+\text{terms of total degree at least \(4\)}.
\]

There are no terms of odd total degree.  Hence:

1. \(C_s\) passes through \(p\) exactly when \(a_{00}=0\);
2. if \(a_{00}=0\), then both first derivatives vanish at \(p\), so \(p\) is
   singular on \(C_s\);
3. in characteristic different from \(2\), the singularity is a geometric
   node exactly when the quadratic form
   \[
   q_p(s)=a_{20}u^2+a_{11}uv+a_{02}v^2
   \]
   is nondegenerate after base change to an algebraic closure.

Equivalently,
\[
\Delta_p(s):=a_{11}^2-4a_{20}a_{02}\neq0.
\]

Thus the local geometric-node condition defines the open subset
\[
A_p^{\mathrm{loc}}
=
H_p\setminus V(\Delta_p).
\]

This is a known local reduction.  It does not impose the global condition
that no other singular point occurs.

### 2.4 Why a unique singular point is fixed

After base change to \(\overline{\mathbf Q}\), the singular locus of an
invariant curve is \(\tau\)-invariant.  If a singular point \(q\) is not fixed,
then \(q\) and \(\tau(q)\) are distinct singular points.  Therefore an
invariant curve with exactly one geometric singular point has that point in
\(F_{\overline{\mathbf Q}}\).

Consequently, the total exactly-one-node parameter set is the union of four
pairwise disjoint set-theoretic loci, one for each fixed corner:
\[
U_{A_1}^{(1)}
=
\bigcup_{p\in F}U_p.
\]
Determining useful scheme or constructible structures on these loci and
their union remains part of the investigation.

## 3. The universal family

### 3.1 Universal invariant divisor

Let
\[
P_+=\mathbf P(V_+)
\]
in the line convention, so that \(P_+\) parameterizes one-dimensional
subspaces of \(V_+\).  On \(Y\times P_+\), with projections \(p_Y,p_P\), the
tautological inclusion
\[
\mathcal O_{P_+}(-1)\hookrightarrow V_+\otimes\mathcal O_{P_+}
\]
and evaluation give a tautological invariant equation, equivalently a section
of
\[
p_Y^*L\otimes p_P^*\mathcal O_{P_+}(1)
\]
whose zero scheme is the universal invariant divisor
\[
\mathcal C_+\subset Y\times P_+.
\]

The structure morphism
\[
\pi:\mathcal C_+\to P_+
\]
has fiber \(C_s\) over \([s]\).

### 3.2 Relative singular subscheme

The family is a family of hypersurface curves in the smooth relative surface
\(Y\times P_+\to P_+\).  Its relative singular closed subscheme is
\[
\Sigma_+
:=
\operatorname{Sing}(\mathcal C_+/P_+)
=
V\!\left(\operatorname{Fitt}_1
(\Omega_{\mathcal C_+/P_+})\right)
\subseteq\mathcal C_+.
\]

On a standard affine chart of \(Y\), if the universal equation is
\[
f(u,v;\mathbf a)=0,
\]
then \(\Sigma_+\) is cut out by
\[
f,\qquad
\frac{\partial f}{\partial u},\qquad
\frac{\partial f}{\partial v}.
\]

The relative singular subscheme and these chart equations describe the same
closed subscheme.  The notebook should display both and identify the
transition maps on overlaps.

Every residue field of \(P_+\) has characteristic \(0\), hence is perfect.
Consequently, on every fiber the underlying nonsmooth locus is also the
intrinsic nonregular locus.  This identification is a consequence of the
base field in this investigation, not part of the definition by Fitting
ideals.

Formation of \(\Sigma_+\) commutes with base change.  In particular,
\[
(\Sigma_+)_{[s]}
\cong
\operatorname{Sing}(C_s)
\]
with the Fitting scheme structure appropriate to this hypersurface family.

### 3.3 The discriminant and smooth locus

Because \(Y\) is projective, the projection
\[
\Sigma_+\to P_+
\]
is proper.  Its image is therefore a closed subset
\(\Delta\subseteq P_+\).  One may also take the scheme-theoretic image to
obtain a closed subscheme with that support.

The smooth invariant locus is the open subscheme
\[
P_+^{\mathrm{sm}}=P_+\setminus\Delta.
\]

Every smooth invariant curve avoids the fixed subscheme, since an invariant
curve through a fixed corner is automatically singular there.  Hence
\[
P_+^{\mathrm{sm}}
\subseteq
P_+\setminus\bigcup_{p\in F}H_p.
\]

The equality or strictness of related discriminant descriptions, their
degrees, components, and scheme structures are legitimate computational
questions.

## 4. The exactly-one-\(A_1\) loci

### 4.1 Geometric \(A_1\)-locus at a fixed corner

Fix \(p\in F\).  Restrict the universal curve and singular scheme to
\(A_p^{\mathrm{loc}}\):
\[
\mathcal C_p
=
\mathcal C_+\times_{P_+}A_p^{\mathrm{loc}},
\qquad
\Sigma_p
=
\Sigma_+\times_{P_+}A_p^{\mathrm{loc}}.
\]

The fixed point gives a section
\[
\sigma_p:A_p^{\mathrm{loc}}\to\Sigma_p,
\qquad
[s]\mapsto(p,[s]).
\]
Every fiber has a geometric \(A_1\) singularity along this section.

The definition of \(A_p^{\mathrm{loc}}\) has an intrinsic form.  Over
\(H_p\), let

\[
g:Y\times H_p\longrightarrow H_p,\qquad
\widetilde L
=
p_Y^*L\otimes p_H^*\mathcal O_{H_p}(1),
\]

let \(s_{\mathrm{univ}}\) be the universal section, and let
\(\bar\sigma_p:H_p\to Y\times H_p\) be the constant section at \(p\).
The restriction of \(\bar\sigma_p\) to \(A_p^{\mathrm{loc}}\) factors through
\(\Sigma_p\) as the section \(\sigma_p\) above.
Invariance at the fixed point implies

\[
\bar\sigma_p^*j^1(s_{\mathrm{univ}})=0.
\]

The restricted second jet therefore has the degree-two term

\[
q_p\in
H^0\!\left(
H_p,
\operatorname{Sym}^2(\bar\sigma_p^*\Omega_{g})
\otimes\bar\sigma_p^*\widetilde L
\right).
\]

Put \(E_p=\bar\sigma_p^*\Omega_g\) and
\(M_p=\bar\sigma_p^*\widetilde L\).  Since \(E_p\) has rank two, polarization
gives a symmetric map
\[
b_{q_p}:E_p^\vee\longrightarrow E_p\otimes M_p.
\]
Define the discriminant by
\[
\operatorname{disc}(q_p)=-\det(b_{q_p}).
\]
It is a section

\[
\operatorname{disc}(q_p)\in
H^0\!\left(
H_p,
(\det E_p)^{\otimes2}\otimes M_p^{\otimes2}
\right).
\]

Then

\[
A_p^{\mathrm{loc}}=D(\operatorname{disc}(q_p))\subseteq H_p.
\]

After trivializing \(E_p\) by \(u,v\), this discriminant is
\(a_{11}^2-4a_{20}a_{02}\).  Thus the chart calculation in Section 2.3 is a
trivialization of the intrinsic degree-two term, not the definition of the
locus.

### 4.2 Singular points away from the distinguished section

Remove the image of the distinguished section:
\[
\Sigma_p^\circ
=
\Sigma_p\setminus\sigma_p(A_p^{\mathrm{loc}}).
\]

Its geometric points are the additional singular points of the fibers.  Let
\[
b_p:\Sigma_p^\circ\to A_p^{\mathrm{loc}}
\]
be the restricted structure morphism.

By Chevalley's theorem,
\[
B_p=b_p\!\left(|\Sigma_p^\circ|\right)
\]
is constructible.  It is the set of parameters for which the curve has at
least one further geometric singular point.

The desired set-theoretic locus is therefore
\[
U_p
=
A_p^{\mathrm{loc}}\setminus B_p.
\]

This formula is a canonical starting description in standard
scheme-theoretic language.  It does not determine:

- a shortest or most informative Boolean decomposition of \(U_p\);
- whether \(U_p\) is locally closed;
- equations for its closure;
- the irreducible components or dimensions;
- the multiplicities or nilpotent structure of any chosen closure;
- the most useful coordinate charts;
- the best way to exhibit sample members and boundary degenerations.

Those are research questions for the notebook.

### 4.3 Why this image, although constructible, is not automatically closed

The morphism \(\Sigma_p\to A_p^{\mathrm{loc}}\) is proper, but
\(\Sigma_p^\circ\) is an open subscheme of \(\Sigma_p\).
The restricted morphism \(b_p\) need not be proper.  Its image is therefore
constructible by finite presentation, but closedness requires additional
mathematics.

This distinction is central.  Replacing \(B_p\) by an unspecified closed
"bad locus" would assume one of the properties the investigation should
determine.

### 4.4 Alternative presentations to investigate

The same set \(U_p\) may admit more useful descriptions.

1. **Equations and inequations.**  Eliminate the point variables from the
   incidence equations, retain the inequation
   \(\operatorname{disc}(q_p)\neq0\), and
   express the absence of further singular points on a finite affine cover
   of \(P_+\).
2. **Finite locally closed decomposition.**  Decompose \(B_p\) into locally
   closed images and take the Boolean complement.
3. **Saturation comparison.**  Compare saturation by the ideal of the
   section \(\sigma_p\) with the incidence morphism
   \(\Sigma_p^\circ\to A_p^{\mathrm{loc}}\), taking care that saturation and
   removal encode different scheme structures.
4. **Finiteness and fiber length.**  On an open subscheme \(W\) where
   \[
   b_W:\Sigma_p\times_{A_p^{\mathrm{loc}}}W\longrightarrow W
   \]
   is finite and finitely presented, put
   \[
   \mathcal M_W
   =
   (b_W)_*
   \mathcal O_{\Sigma_p\times_{A_p^{\mathrm{loc}}}W}.
   \]
   The locus on which this module is finite locally free of rank \(r\) is
   detected by
   \[
   \operatorname{Fitt}_{r-1}(\mathcal M_W)=0,\qquad
   \operatorname{Fitt}_{r}(\mathcal M_W)=\mathcal O_W.
   \]
   There the geometric fiber of the relative singular subscheme has scheme
   length \(r\).
   Counting geometric support points additionally requires reduced fibers;
   these are not the same condition.
5. **Chartwise predicate.**  On each standard chart of \(Y\), solve the
   singular equations and show that the resulting conditions agree on
   overlaps.
6. **Symmetry of the incidence data.**  If a symmetry group is used,
   specify its action on the union of the four \(U_p\) and distinguish the
   full centralizer from a stabilizer of one chosen corner.

The notebook may discover that one of these descriptions is inadequate and
replace it.  Section 7 names the mathematical category to which each such
change belongs.

## 5. What a useful notebook must expose

The notebook is a piece of mathematical exposition.  Its code and output
should let a mathematician follow the following chain:

\[
\text{invariant section}
\longmapsto
\text{curve}
\longmapsto
\text{relative singular subscheme}
\longmapsto
\text{geometric \(A_1\) condition at a fixed point}
\longmapsto
\text{open complement of the distinguished section}
\longmapsto
\text{parameter set}.
\]

At minimum, it should expose:

1. \(Y,L,\tau\), the chosen linearization, \(V_+\), and \(P_+\);
2. a basis of \(V_+\) and the computation \(\dim V_+=13\);
3. the fixed subscheme \(F\) and its four points;
4. the evaluation map and hyperplane \(H_p\) for each \(p\);
5. the first-jet vanishing along \(\sigma_p\), the degree-two term \(q_p\),
   the invertible module
   \((\det E_p)^{\otimes2}\otimes M_p^{\otimes2}\) containing its
   discriminant section, and the coordinate expression obtained after a
   local trivialization;
6. the universal curve \(\mathcal C_+\);
7. the ideal sheaf or compatible chart ideals defining \(\Sigma_+\);
8. the distinguished section \(\sigma_p\);
9. the open complement
   \(\Sigma_p\setminus\sigma_p(A_p^{\mathrm{loc}})\) and the exact image
   operation used;
10. the resulting description of \(U_p\) and its union over \(F\);
11. explicit members, nonmembers, and boundary examples whose classification
    can be read from the displayed intermediate objects.

A useful output can take any of the following forms:

- a closed, open, or locally closed subscheme with its defining maps;
- a constructible subset displayed as finite Boolean operations on named
  loci;
- equations and inequations on a stated affine cover;
- an incidence description with the projection and quantifier visible;
- a predicate whose domain is \(P_+\) and whose local and global conditions
  are separately inspectable;
- a semialgebraic description after a stated base change to an ordered field,
  if the real locus becomes mathematically relevant.

The following do not yet constitute a description:

- a printed object with no defining equations, maps, or operations;
- a sample list of curves;
- a Boolean answer on individual sections;
- a method named after the desired locus whose intermediate mathematics is
  hidden;
- a coordinate answer whose behavior under a change of chart is not shown.

## 6. Standard computations around the main question

The exactly-one-node investigation should sit among ordinary curve
computations rather than appear as an isolated specialized routine.

### 6.1 Smooth and fixed-point-avoiding curves

Construct the closed image of
\(\Sigma_+\to P_+\), display the image operation and any equations obtained
for it, and form its open complement \(P_+^{\mathrm{sm}}\) as a named open
subscheme.  Construct the four evaluation hyperplanes and the open complement
of their union.  Exhibit smooth invariant members in these opens and compare
their genus with adjunction:
\[
g=(4-1)(4-1)=9.
\]

### 6.2 Curves singular at several fixed points

For a subset \(S\subseteq F\), the linear condition
\[
\bigcap_{p\in S}H_p
\]
parameterizes curves through every point of \(S\), hence singular at every
point of \(S\).  Compare the independent evaluation conditions, and study
the open part on which each local quadratic form is nondegenerate.

### 6.3 Singular orbits away from the fixed scheme

Study the incidence over
\[
(Y\setminus F)\times P_+.
\]
Every geometric singular point occurs with its distinct \(\tau\)-translate.
The notebook should exhibit examples and record whether the corresponding
parameter image meets the closures of the fixed-point loci.

### 6.4 Reducible and nonreduced curves

Construct invariant reducible and nonreduced sections.  Display their
reductions, components, singular schemes, and positions in the discriminant.
This separates "has one point in the support of the singular scheme" from
"has one geometric \(A_1\) singularity".

### 6.5 Higher \(A\)-type behavior

At a fixed corner, invariant local equations contain even total degrees.
The normal forms
\[
u^2+v^{2m}
\]
have type \(A_{2m-1}\) over an algebraically closed field of characteristic
\(0\).  The notebook may investigate higher odd \(A\)-types through jet
conditions and exclusion of more degenerate terms.

The language must keep three layers separate:

- closed conditions forcing lower-order jets to vanish;
- open inequations selecting the exact type;
- the global exclusion of additional singular points.

No claim is made that these loci have a predetermined scheme structure or
component decomposition.

## 7. Where improvements belong

| Mathematical improvement | Owning category or parent |
| --- | --- |
| faster radical, saturation, or elimination | finitely presented commutative \(\mathbf Q\)-algebras |
| better equations for the relative singular subscheme of a family | flat locally finitely presented morphisms with equidimensional fibers and Fitting ideals; local Jacobian equations in the effective Cartier divisor case |
| improved local \(A_n\) recognition | isolated plane hypersurface germs with a chosen equation in the local ring of a smooth \(k\)-surface, using the relative Jacobian ideal |
| the geometric node condition over a nonclosed residue field | scalar extension of the plane hypersurface germ to an algebraic closure of its residue field |
| comparison of a local scheme and its formal completion | completion of Noetherian local schemes and affine formal spectra |
| establishing that a parameter image is closed | proper morphisms for closed topological images; finite morphisms when the stronger finite affine structure is established |
| better constructible decomposition | `ConstructibleSubsets(P_+)` and direct images along morphisms of finite presentation by Chevalley's theorem |
| equations for a scheme-theoretic image | projective morphisms together with a chosen closed immersion into projective space over the base, with elimination in the resulting homogeneous coordinate ring |
| treatment of nonreduced parameter structures | closed subschemes and reductions |
| comparison of the four fixed-point loci | the centralizer action on \(P_+\) and equivariant parameter loci |
| faster \((4,4)\) chart calculations | closed subschemes with a chosen embedding in a product of projective spaces and a multihomogeneous ideal |
| branch-cover consequences | cyclic-cover data after the curve locus has been constructed |

This table is the practical consequence of using categories with axioms,
replete full subcategories, and categories of chosen data.  A change to local
singularity recognition belongs to the local hypersurface category; a change
to the constructible presentation of a direct image belongs to
`ConstructibleSubsets(P_+)`.

## 8. Questions the notebook should answer or sharpen

The following are genuine research questions.

1. Is each \(U_p\) locally closed in \(P_+\), or is a nontrivial constructible
   decomposition necessary?
2. What is the closure \(\overline{U_p}\), and what equations define it?
3. What are the dimensions and irreducible components of \(U_p\),
   \(B_p\), and their closures?
4. Which components correspond to another fixed singularity, a nonfixed
   singular orbit, reducibility, or nonreducedness?
5. Does the centralizer of \(\tau\) act transitively on the four loci
   \(U_p\), and what is the stabilizer action on one locus?
6. Which boundary components record degeneration at the fixed point \(p\)
   to \(A_3,A_5,\ldots\), the \(A\)-types compatible there with the even
   local equation?  Which instead record an additional
   \(\tau\)-pair of singularities away from \(F\), where even and odd
   \(A\)-types, including \(A_2\), may occur?
7. Can the image of
   \(\Sigma_p\setminus\sigma_p(A_p^{\mathrm{loc}})\) be replaced by equations
   and inequations of manageable degree?
8. On which open subsets is the relative singular subscheme finite over the
   parameter space, and can its pushforward describe scheme lengths?  On
   which of those subsets are the geometric fibers reduced, so those lengths
   also count geometric support points?
9. How do the descriptions change after base extension from \(\mathbf Q\) to
   \(\overline{\mathbf Q}\), \(\mathbf C\), or \(\mathbf R\)?
10. Which description is most useful for the later double-cover and quotient
    constructions?

The plan constrains the language and the mathematical visibility of the
investigation.  It does not prejudge these answers.

## 9. Later cover questions

After the invariant curve family is understood, let
\[
M=\mathcal O_Y(2,2),
\qquad
L=M^{\otimes2}.
\]
An invariant section \(s\in H^0(Y,L)\), together with a compatible
linearization of \(M\), defines double-cover data and a cover
\[
\pi:X_s\to Y.
\]

The later questions include:

- smoothness or normality of \(X_s\) from the branch germ;
- the two lifts of \(\tau\);
- their fixed subschemes;
- the fixed-point-free condition;
- the K3 condition for a smooth branch;
- the Enriques quotient when a lift is fixed-point-free;
- the surface singularity over a nodal or higher-\(A\)-type branch point.

These questions use the outputs of the curve notebooks.  They do not replace
the work of describing \(U_p\).

## 10. Source anchors

- [Sage category framework](https://doc.sagemath.org/html/en/reference/categories/sage/categories/primer.html)
- [Sage categories with axioms](https://doc.sagemath.org/html/en/reference/categories/sage/categories/category_with_axiom.html)
- [Stacks, Smooth morphisms](https://stacks.math.columbia.edu/tag/01V4)
- [Stacks, Relative singular locus](https://stacks.math.columbia.edu/tag/0C3H)
- [Stacks, Scheme-theoretic image](https://stacks.math.columbia.edu/tag/01R5)
- [Stacks, Chevalley's theorem](https://stacks.math.columbia.edu/tag/054H)
- [Stacks, Nodal curves](https://stacks.math.columbia.edu/tag/0C46)
- [Stacks, Effective Cartier divisors](https://stacks.math.columbia.edu/tag/0CPG)
- [Stacks, Principal parts](https://stacks.math.columbia.edu/tag/09CQ)
- [Stacks, Fitting ideals and finite locally free rank](https://stacks.math.columbia.edu/tag/07ZD)

The category architecture supplies the remaining definitions and places each
operation used here in its general mathematical home.
