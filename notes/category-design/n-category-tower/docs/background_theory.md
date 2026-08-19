<!--
Origin: gitclones/integral_lattice/cat/docs/background_theory.md
Copied 2026-08-20 by the integral_lattice enrichment migration
(PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences and recorded errors are listed in the INDEX.md of
this corpus.
-->

$$
% Semantic macros for commonly used symbols
\newcommand{\Cat}{\mathbf{Cat}}
\newcommand{\Catw}{\mathbf{Cat}_\omega}
\newcommand{\Mor}{\mathrm{Mor}}
\newcommand{\Nat}{\mathrm{Nat}}
\newcommand{\Elt}{\mathrm{Elt}}
\newcommand{\Cof}{\mathrm{Cof}}
\newcommand{\Fib}{\mathrm{Fib}}
\newcommand{\colim}{\mathrm{colim}}
\newcommand{\Fun}{\mathrm{Fun}}
\newcommand{\Hom}{\mathrm{Hom}}
\newcommand{\push}[0]{+}
\newcommand{\pull}[0]{\times}
\newcommand{\pt}{\ast}
\newcommand{\ZZ}{\mathbb{Z}}
\newcommand{\NN}{\mathbb{N}}
\newcommand{\limproj}{\varprojlim}
\newcommand{\liminj}{\varinjlim}
\newcommand{\from}{\leftarrow}
\newcommand{\terminal}{\pt}
\newcommand{\initial}{\emptyset}
\newcommand{\id}{\mathrm{id}}
\newcommand{\Cone}{\mathrm{Cone}}
\newcommand{\Cocone}{\mathrm{Cocone}}
\newcommand{\Cyl}{\mathrm{Cyl}}
\newcommand{\Cocyl}{\mathrm{Cocyl}}
\newcommand{\mca}{\mathcal{A}}
\newcommand{\Spaces}{\mathcal{S}}
\newcommand{\Maps}{\mathrm{Maps}}
\newcommand{\mcl}{\mathcal{L}}
\newcommand{\ev}{\mathrm{ev}}
\newcommand{\Eq}{\mathrm{Eq}}
$$

# A toy model for a category $\Catw$ of $(\infty, n)$ categories

Recall that an $n$-category $C\in \Cat_n$ has collections:

- $\Mor^0 C$: 0-morphism: objects.
- $\Mor^1 C$: 1-morphisms: morphisms between objects
- $\Mor^2 C$: 2-morphisms: morphisms between 1-morphisms,
- …
- $\Mor^n C$: $n$-morphisms are morphisms between $(n-1)$-morphisms
- $\Mor^{n+k}C = \emptyset$ for $k\geq 1$.

We regard this as a sequence $[\Mor^0 C, \Mor^1 C, \cdots, \Mor^n C]$ with “gluing data”.

It can be regarded as a category which is weakly enriched over $(n-1)$-categories. There is an inclusion $i_{n, n+1}: \Cat_n \hookrightarrow \Cat_{n+1}$ gotten by setting

$$
\Mor^{n+1}({\iota_{n, n+1}C}) := \displaystyle \int^{f\in \Mor^n C} [f, f]_{\Mor^n C} \cong \displaystyle\sum_{f\in \Mor^n C} \{\id_f\} \cong_{\mathrm{Set}} \Mor^n C
$$

i.e. by regarding all $n+1$ morphisms between $n-$morphisms as identities. We regard the image similarly as a sequence of length $n+1$.

Then define $\Catw := \lim(\Cat_0 \hookrightarrow \Cat_1 \hookrightarrow\cdots)$; thus an element $C\in \Catw$ has nonempty collections $\Mor^n C$ for every $n$ and is regarded as a sequence $[\Mor^0 C, \Mor^1 C, \cdots]$. We identify $\Cat_n$ with its image in $\Catw$, so that elements $C\in \Cat_n$ have (potentially nontrivial) collections $\Mor^k C$ for $k\leq n$, but every $(n+k)$-morphism is the identity for $k\geq 1$.

We thus have “brutal” adjoint extension and truncation functors $i_n \dashv t_n$:
$$
\begin{align*}
i_n: \Cat_n &\to \Catw  \\
C = [\Mor^0 C, \cdots, \Mor^n C] &\mapsto [\Mor^0 C, \cdots, \Mor^n C, \Mor^n C, \Mor^n C, \cdots] 
\\ \\
t_n: \Catw &\to \Cat_n \\
C = [\Mor^0 C, \cdots ] &\mapsto [\Mor^0 C, \cdots, \Mor^n C]
\\ \\

\end{align*}
$$
We define various notions of equivalence: there is a homotopy type of equivalences between objects $A, B$, $X := \mathrm{Equiv}(A,B)$. Then define

- $A\simeq B \iff \mathrm{Equiv}(A, B) \neq \emptyset$
- $A \cong B \iff \

An $(n, m)$-category is an $n$-category $C$ such that every $(m+k)$-morphism is _invertible_ for $k\geq 1$: for every such morphism $f: C\to D$, there is a morphism $g: D\to C$ and $(m+k+1)$-morphisms $\eta_0: fg \to \id$ and $\eta_1: gf \to \id$, where the $\eta_i$ are invertible in the same sense. Note that if $(m+k+1) > n$, this requires that $fg = \id$ and $gf = \id$. We can similarly define $(\infty, n)$-categories and $\Cat_{\infty, n}$. Note that $\Cat_{\infty, 0} = \Spaces$, and $\Cat_{\infty, n}$ is weakly enriched over $\Cat_{\infty, n-1}$, and we define homotopy categories by $\mathrm{ho}(C)(x, y) := \pi_0C(x, y)$. We want $\Cat_{\infty, 1}$ to include all usual categories.

A space $X\in \Spaces$ is an $n$-type if $\pi_{n+k} X = 1$ for all $k\geq 1$.

Goal: describe a category $\mca$ capturing a model of the category $\Catw$ of $\infty$-categories that closely follows the homotopy theory of CW complexes and relies on the category $\Spaces$ of homotopy types. We only need this so that we can explicitly define the strict $2$-category $\Cat$, whose objects (0-morphisms) are categories $C$, 1-morphisms are functors $F:C\to D$, 2-morphisms are natural transformations $\eta: F\to G$, and all higher morphisms are identities.

## Axioms and Definitions

- All limits and colimits in $\mca$ are inherently homotopy colimits.
- We assume $\mca$ is bicomplete, cartesian closed, and enriched over $\Spaces$.
- There is an a-posteriori notion of equality that we only use in the meta-theory. Within $\mca$, there is only isomorphism $\cong$ and equivalence $\simeq$, neither of which imply equality $=$. We say $A = B$ if $A, B$ are unique up to unique isomorphism.
- $A\simeq B$ iff there exists an equivalence $f: A\to B$.
- $f: A\to B$ is an equivalence if there exists a morphism $g: B\to A$ such that $f\simeq g$ in $\Mor(\mca) \in \Catw$.
- $A$ is contractible iff $t_A: A\to \pt$ is an equivalence.

### Standard constructions

- $\terminal$ is terminal if $\Hom(C, \terminal) \simeq \pt\in \Spaces$, so $C\to \pt$ is essentially unique.
  - A “section” $x: \pt \to C$ is a **point**.
- $\initial$ is an initial object if $\Hom(\initial, C) \simeq \pt \in \Spaces$, so $\initial \to C$ is essentially unique.
  - A “section” $x^\vee: C\to \emptyset$ is a **co-point**.
- There is an essentially unique map $z: \initial \to \terminal$
- $[-, -]$ is the internal hom in $\mca$, and $\Maps(-, -)$ is the internal hom in $\Spaces$.
  - $B^A := [A, B]$.
- Pullbacks are written $A \pull_C B := \lim(A \to C\from B)$.
  - Products are $A \times B := A\pull B :=  A \pull_\terminal B$.
- Pushouts are written $A\push^C B := \colim(A \from C \to B)$.
  - Coproducts are $A\amalg B = A + B = A \push^\initial B$.
- Wedge products depend on points, and are written $X \vee_{x, y} Y := \colim(X \xleftarrow{x} \pt \xrightarrow{y} Y) = X +^\pt Y$.
- Diagonal maps are written $\Delta_X: X \to X^2$ and codiagonal/fold maps are $\nabla_X: X\push X \to X$
- Path/Cocylinder objects $X^I$ are factorizations of $\Delta_X$ into $X \to X^I\to X^2$, and $X^I\simeq \pt$
- Cylinder objects $X\times I$ are factorizations of $\nabla_X$ into $X +X \to X\times I \to X$, and $X\times I \simeq X$.
  - Interval objects $I$ are factorizations of $\nabla_\pt: \pt\push\pt\to \pt$ into $\pt\push\pt \to I \to \pt$, and thus cylinders on $\pt$.

- Maps $f_i: X_i \to Y$ assemble vertically to coproduct maps $\left[ f_1 \atop f_2\right]: X_1 \push X_2 \to Y$, and maps $f_i: X\to Y_i$ assemble horizontally to product maps $[f_1, f_2]: X\to Y_1\pull Y_2$.
  - Thus a map from a coproduct into a product, say $F: X_1 + X_2 \to Y_1 + Y_2$, is specified by maps $f_{i_j}: X_i\to Y_j$ and assemble into a matrix $F = \left[ f_{11},\,\, f_{12} \atop f_{21},\,\, f_{22}\right]$.


### Homotopy-theoretic constructions:

$$
\begin{align*}
\Sigma_{f: X\to Y} 
&:= \colim(Y\xleftarrow{f} X \xrightarrow{f}  Y) \\
&= Y +_X Y \\[0.5em]
\Sigma C 
:= \Sigma_{C\to \Cone(C)}
&:= \colim(\Cone(C) \from C\to \Cone(C) \\
&= \Cone(C) \push^C \Cone(C) \\
&\simeq \colim(\pt \from C\to \pt), \\
&\simeq \terminal \push^C \terminal \\
&\simeq \Sigma_{C\to \pt} 
\\[1em]
\Omega_{f: X\to Y} 
&:= \lim(X\xrightarrow{f} Y \xleftarrow{f} X) \\
&= X \pull_Y X  \\
\Omega_x C 
:= \Omega_{\tilde x: \Cocone_X(C) \to C} 
&:= \lim(\Cocone_x(C) \xrightarrow{\tilde x} C \xleftarrow{\tilde x} \Cocone_x(C)) \\
&= \Cocone_x(C) \pull_C \Cocone_x(C) \\
&\simeq \lim(\pt \xrightarrow{x} C \xleftarrow{x} \pt) \\
&\simeq \terminal \pull_C \terminal \\
&\simeq \Omega_{x: \pt\to C}
\end{align*}
$$



Spheres, discs, and intervals
$$
\begin{align*}
[S^{-1}, S^0, S^1, \cdots] 
&:= [\emptyset,\Sigma \emptyset =\pt\push \pt, \Sigma^2 \emptyset =  \pt\push^{\pt\push\pt}\pt, \cdots] \\
[D^0, D^1, D^2, \cdots] 
&:= [\pt, [1] := \{0 < 1\}, [2] := \{0<1<2\}, \cdots] \\
I &= [1]
\end{align*}
$$

Fibers and cofibers
$$
\begin{align*}
\Fib_y(f: X\to Y) 
&:= \mcl_{(f, y):\, X\times \pt \to Y^2} \\
&= \lim(X\pull \pt \xrightarrow{(f, y)} Y^2 \xleftarrow{(\ev_0, \ev_1)} Y^I) \\
&= (X\pull \pt)\pull_{Y^2} Y^I \\
&\simeq \lim(X\xrightarrow{f} Y \xleftarrow{y} \pt)\\
&= X \pull_Y \pt  
\\[1em]
\Cof(f: X\to Y) 
&:= \colim(\Cone(X) \from X \xrightarrow{f} Y) \\
&= \Cone(X) \push^X Y \\
&\simeq \colim(\pt \from X \xrightarrow{f} Y) \\
&\simeq \pt \push^X Y
\end{align*}
$$

Paths and loops
$$
\begin{align*}
\mathcal{P}_{f: X\to Y} 
&:= \lim(X \xrightarrow{f} Y \xleftarrow{\ev_0} Y^I) \\
&= X \pull_{Y} Y^I \\
&\simeq X \pull_Y Y \simeq X \\
\mathcal{P}_x X
:= \mathcal{P}_{x:\pt \to X}
&:= \lim(\pt \xrightarrow{x} X \xleftarrow{\ev_0} X^I) \\
&= \Fib_x(\ev_0: X^I\to X) \\ 
&= \pt \pull_X X^I \\
&\simeq \pt \pull_X X \simeq \pt
\\[1em]
\mcl_{f: X\to Y^2} 
&:= \lim(X \xrightarrow{f} Y \xleftarrow{(\ev_0, \ev_1)} Y^I )\\
&= X\pull_{Y^2} Y^I \\
&\simeq X \pull_{Y^2} Y\\
\mcl X := \mcl_{\Delta: X \to X^2} 
&= \lim(X \xrightarrow{\Delta} X^2 \xleftarrow{(\ev_0, \ev_1)} X^I)\\
&= X \pull_{X^2} X^I \\
&\simeq X \pull_{X^2} X \\
&= \Omega_{\Delta: X\to X^2}
\\[1em]
\Omega_x X 
&= \lim(\pt \xrightarrow{x} X \from \mcl X) \\
&= \Fib_x(\mcl X \to X) \\
&= \pt\pull_X \mcl X
\end{align*}
$$

Write $\iota_0: \pt_0 \to S^0, \iota_1: \pt_1 \to S^0$ where $S^0 = \pt_0 + \pt_1$, for the two coprojections. Then any maps $f_0: \pt \to X$ and $f_1: \pt \to X$, these assemble into $f_{01} := \left[ f_0 \atop f_1 \right]: S^0\to X$.

An interval object $I$ is characterized as a factoring of $S^0\to \pt$ as $S^0 \xrightarrow{\iota_{01}} I\to \pt$, which yields two points $I_0, I_1: \pt \to I$ where $I_0 = \iota_{01}\circ \iota_0$ and $I_1 = \iota_{01}\circ \iota_1$.

One can define evaluation maps: write $\Gamma(C) := C^\pt := [\pt, C] \in \Spaces$. Then adjunction $[B^A, B^A] = [B^A\times A, B]$ sends $\id_{B^A}$ to

$$
\ev: B^A\times A \to B, \qquad \ev(f, a) \approx f(a)
$$

If $a: \pt\to A$ is a point, then define

$$
\ev_a: B^A \xrightarrow{\id_{B^A} \times !_{B^A}} B^A \times \pt \xrightarrow{\id_{B^A} \times a} B^A\times A \xrightarrow{\ev} B, \qquad\leadsto \ev_a: B^A\to B,\\ \ev_a(f) \approx \ev(f, a) \approx f(a)
$$

If $b: \pt \to B$ is a point, then define

$$
B^A_{a, b} := [A, B]_{a, b} := \lim(B^A \xrightarrow{\ev_a} B \xleftarrow{b} \pt) = B^A \pull_B \pt = \Fib_b(\ev_a)
$$

Applying global sections allows obtaining points:

$$
\begin{align*}
\Gamma\ev: \Gamma(B^A) \times \Gamma(A) &\to \Gamma(B), \\
\Gamma\ev(f: \pt\to B^A, a: \pt\to A) &=  \pt \xrightarrow{f \times a} B^A\times A \xrightarrow{\ev} B \\ \\
\Gamma \ev_a: \Gamma(B^A) &\to \Gamma(B), \\
\Gamma \ev_a(f:\pt \to B^A) &= \ev(f, a) \\ \\
\Gamma B_{a, b}^A &= \lim(\Gamma(B^A) \xrightarrow{\Gamma \ev_a} \Gamma(B) \xleftarrow{b'} \pt) \\
&= \Fib_{b'}(\Gamma \ev_a)
\end{align*}
$$

These naturally induce a mixed “evaluation” morphism:

$$
\begin{align*}
\ev: B^A \times \Gamma(A) &\to \Gamma(B) \\
(f: A\to B, a: \pt \to A) &\mapsto (f\circ a): \pt \to A\to B \\ \\
\ev_a: B^A &\to \Gamma(B) \\
(f: A\to B) &\mapsto \ev(f, a) \\ \\
[A, B]_{a, b} &:= \Fib_b(\ev_a) = B^A \pull_{\Gamma(B)} \pt
\end{align*}
$$

and

$$
\ev_f: \Gamma(A) \to \Gamma(B), \qquad (a: \pt \to A) \mapsto \ev_a(f)
$$

We define $C^I := [I, C]$ as the free path space, and for $x: \pt\to C$, the based path space as follows: use $I_0: \pt \to I$ to define $\mathrm{ev}_{I_0}: C^I \to C$, and define

$$
\mathcal{P}_xC := [I, C]_x := \lim(C^I \xrightarrow{\mathrm{ev}_{I_0}} C \xleftarrow{x} \pt) = C^I \pull_C \pt = \Fib_x(\mathrm{ev}_{I_0})
$$

The usual fiber sequences:

$$
\cdots \to \Omega_x B \to \Fib_x(f) \to A \xrightarrow{f} B\hspace{10em}  \\
\hspace{11em}
A \xrightarrow{f} B \to \Cof(f) \to \Sigma A \to \cdots
$$

### Cylinders and Cones

$$
\begin{align*}
\mathrm{Paths}_{a_0, a_1} A
&:= \lim(\pt \xrightarrow{a_0, a_1} A\pull A \xleftarrow{\ev_0, \ev_1} A^I) \\
&= A^I \pull_{A\pull A} \pt
\\
\Cyl(f: A\to B)
&:= \colim(\Cyl(A) \xleftarrow{\iota_0} A \xrightarrow{f} B) \\
&= \Cyl(A) \push_A B \\
&=  I\pull A \push_A B
\\[4pt]
\Cyl(A) := \Cyl(\id_A)
&:= I\pull A \push_A A \\
&= I\pull A
\\[4pt] \hline
\Cone(f: A\to B)
&:= \colim(\Cyl(f) \xleftarrow{\iota_0} A \to \pt) \\
&= \Cyl(f)\push_A \pt \\
&= I\pull A \push_A B \push_A \pt
\\[4pt]
\Cone(A) := \Cone(\id_A)
&:= \Cyl(\id_A) \push_A \pt \\
&= \Cyl(A) \push_A \pt \\
&= I\pull A \push_A \pt
\\[4pt] \hline
\Cocyl(f: A\to B)
&:= \lim(A \xrightarrow{f} B \xleftarrow{\mathrm{ev}_{I_0}} \Cocyl(B)) \\
&= A \pull_B \Cocyl(B) \\
&= A \pull_B B^I
\\[4pt]
\Cocyl(B) := \Cocyl(\id_B)
&= B \pull_B B^I \\
&= B^I
\\
\\[4pt] \hline
\Cocone_x(f: A\to B)
&= \lim(\Cocyl(f) \xrightarrow{\mathrm{ev}_{I_1}} B \xleftarrow{x} \pt) \\
&= \Cocyl(f) \pull_B \pt \\
&= A\pull_B B^I \pull_B \pt
\\[4pt]
\Cocone_x(B)
&:= \lim(B^I \xrightarrow{\mathrm{ev}_{I_1}} B \xleftarrow{x} \pt) \\
&= B^I \pull_{B} \pt
\\[4pt]
\end{align*}
$$

Note the two points $I_0, I_1: \pt \to I$ induce two morphisms $\iota_0, \iota_1: A\to I\times A$ given by $[I_k, \id_A]$, the inclusion of $A$ as the “bottom” and “top” of the cylinder. Thus there are two maps $\iota_k: A\to \Cyl(A)$. Similarly, there is a canonical map $\Cyl(A) \to \Cyl(f)$ from the definition of a pushout, and thus there are two composites $\iota_k: A\to \Cyl(A) \to \Cyl(f)$.

Some basic calculations:

- $A \pull_C C := \lim(A \to C \xleftarrow{\id_C} C) = A$.
- $A \push^C C = \lim(A \from C \xrightarrow{\id_C} C) = A$.
- $\Sigma^k \initial = S^{k-1}$ and $\Omega_x^k \initial$ does not exist for any $k$.
- $\Sigma \terminal = \terminal \implies \Sigma^k \terminal = \terminal$ and $\Omega_{\id_\pt} \pt = \pt \implies \Omega_{\id_\pt}^k = \pt$ for all $k$.
- $\Sigma S^n = S^{n+1}$ and $\Omega_x S^n$ depends on $x: \pt\to S^n$ and is nontrivial.

$$
\begin{align*}
\Cone(\initial \to A) &:= \\
\Cone(A\to \terminal) &:= \\
\Cocone(\initial \to A) &:= \\
\Cocone(A\to \terminal) &:= \\
\Cyl(\initial \to A) &:= \\
\Cyl(A\to \terminal) &:= \\
\Cocyl(\initial \to A) &:= \\
\Cocyl(A\to \terminal) &:= \\
\end{align*}
$$

## Categorical and Geometric Homotopy Groups

If $(-)^{(-)}: \mca \times \Spaces \to \Spaces$ is a powering, one can produce families $\pi_n(X) \to X$ for every $n$ such that $\pi_n(X, x) := \Fib_x(\pi_n(X) \to X)$ recovers usual homotopy groups on spaces. Use the canonical point $i_n: \pt \to S^n$ and apply $X^{(-)}$ to obtain $X^{i^n}: X^{S^n} \to X^*$, regarded as an object in $\mca_{/X^*}$. Then define $\pi_n(X) := \tau_{\leq_0} X^{i_n} \in \mca_{/X^*}$. Now note that any point $x: \pt \to X$ yields a point $\Gamma(x): \pt \to X^*$, and thus a pullback $\pi_n(X, x) := \Fib_{\Gamma(x)}(\pi_n(X))$.



## Equality

### Equalness objects and equality data

Fix an $(\infty,1)$-category $\mathsf{Cat}_w$ of weak categories and a *walking equivalence* $\mathcal{E}$ with two objects $0,1$ and a chosen adjoint equivalence between them. Consider
$$
\mathrm{ev}_{0,1} : \Fun(\mathcal{E},\mathsf{Cat}_w) \to
\mathsf{Cat}_w^2,
\qquad F \mapsto (F(0),F(1)).
$$


For a point $x: \pt \to \Catw$ corresponding to a pair $(A, B)$, the *category of equivalences* $\Eq(A, B)$ is the homotopy fiber
$$
\Eq(A, B) := \operatorname{hofib}_{x}(\mathrm{ev}_{0,1}).
$$
Objects of $\Eq(A, B)$ are functors $\mathcal{E} \to \mathsf{Cat}_w$ picking out equivalence data $A \rightleftarrows B$ (with all higher cells). For each $A$, there is a canonical basepoint $\mathbf{1}_A \in \Eq(A, A)$ given by the identity equivalence pair $A \rightleftarrows A$. There are natural maps
$$
s : \Eq(A, B) \to \Eq(A, A),
\qquad
t : \Eq(A, B) \to \Eq(B, B),
$$
sending a chosen equivalence $A \rightleftarrows B$ to its induced self-equivalence pairs on $A$ and $B$. The *equality category* between $A$ and $B$ is the homotopy fiber

$$
\Eq^0(A,B) := \operatorname{hofib}_{(\mathbf{1}_A,\mathbf{1}_B)}(s,t)
\hookrightarrow \Eq(A, B).
$$
A point of $\Eq^0(A,B)$ is an equivalence pair $(f,g):A \rightleftarrows B$ together with specified higher homotopies
$$
g f \simeq \mathrm{id}_A \in \Eq(A, A),\qquad f g \simeq \mathrm{id}_B \in \Eq(B,B)
$$
connecting the induced self-equivalences to the chosen identity data.

The internal equality on objects of $\mathsf{Cat}_w$ is
$$
A = B \iff \Eq^0(A,B)\neq \emptyset.
$$

There is a natural action
$$
\Aut(A)\times\Aut(B) \curvearrowright \Eq(A,B)
$$
by pre- and post-composition on the chosen equivalence data. On connected
components, this action typically makes $\pi_0\Eq(A,B)$ into an
$\Aut(A)\times\Aut(B)$-torsor whenever $A$ and $B$ are equivalent: all
ways of identifying $A$ with $B$ differ by composing with autoequivalences. This action descends to $\Eq^0(A, B)$. 

Some basic facts:

- $A = A$ for all $A\in \mca$, induced by the point $\id_A: \pt\to\Eq^0(A, A)$.
- By exchanging elements in an pair, $A=B \iff B = A$
- Composition induces $A=B,\, B = C \implies A = C$.
- $A=B\implies A\simeq B$ but not conversely, making this strictly stronger than equivalence in $\mca$.
  The essential reason: the image of an equivalence pair $(f, g)$ under $(s, t)$ may not lie in the same path component of $(\id_A, \id_B)$.
- Since isomorphisms $A\cong B$ are truncated equivalences $A\simeq B$, we have $A=B\implies A\cong B$ but again not conversely.
- If $A$ is unique up to unique isomorphism, then for any other object $B$ satisfying the same universal property, $\Eq^0(A, B) \simeq \pt$

## Results to Recover

Some known results and definitions that should be generalized and recovered:

- There are categorical homotopy groups $\pi_n^{\mca} C$ and geometric homotopy groups $\pi_n C$ for all $n$ and all $C\in \mca$.

- There are truncation functors $\tau_{\leq n}$ and $\tau_{\geq n}$ for all $n$, with $\pi_{n+k} \tau_{\leq n} C = \pt$ for all $C$.

  - Define $\tau_n := \tau_{\leq n} \tau_{\geq n}$.

- Relations to the subcategory $\Spaces$ of spaces:
  - There is a functor $\iota_\Spaces: \Spaces \to \mca$ that regards an $\infty$-groupoid as an $(\infty, 1)$-category.
  - There is a functor $\mathrm{core}: \mca \to \Spaces$ which discards all 1-morphisms which are not isomorphisms.
  - There is a functor $\Gamma: \mca \to \Spaces$ given by $\Gamma(-) = [\pt, -]$.
  - There is a functor $\Pi_\infty: \mca \to \Spaces$ where $\Pi_\infty C$ is likely obtained by freely inverting all 1-morphisms in $C$.
  - These are probably related by $\Pi_\infty \dashv \iota_\Spaces \dashv \Gamma \dashv \mathrm{core}$.

- There are mapping spaces $\Maps_{\mca}(C, D) := \Pi_\infty [C, D]$.

- There are cell functors $(-)^n: \mca \to \mca$ where probably $C^n := [I^n, C]$.

- Spheres, intervals, and discs:
  - $I^n \in \Spaces \leq \mca$ is contractible for every $n\geq 0$.
  - $I \simeq \pt$ is contractible and $S^k\not\simeq \pt$ is not contractible for any $k\geq -1$.
  - $S^{n+1} = \Sigma S^n$ and $I^{n+1} = \Sigma I^n$
  - $S^1 \cong B \ZZ$ for an appropriate notion of $S^1$ and $B$, possibly after truncation.
  - Free loops can be recovered as $\mcl C \equiv [S^1, C]$ and based loops as $\Omega_x C = [(S^1, 1), (C, x)]$ in $\mca_\pt$.
  - $\Sigma C = S^1 \otimes C$ for some tensoring
  - There is a functor $\partial: \mca \to \mca$ recovering $\partial I^n = S^{n-1}$.

- There is a functor $B: \mca\to \mca$ which recovers “higher” classifying groupoids.
  - Likely $BC = \{1 \xrightarrow{x} 2 \mid x\in C\}$ is the correct construction, which is equivalent to $\{ 0 \circlearrowleft_{g} \mid g\in G\}$.
  - $BG = K(G, 1) = \Cof(G\to \pt) = \pt/G$
  - $K(G, n) = \Cof(K(G, n-1) \to \pt) = \pt/K(G, n-1)$ in a reasonable way.

- Some reasonable functor $F:\mca \to \mca$ which sends $C$ to $\{1 \xrightarrow{C} 2\}$ which can be realized as $F(C) = BF \otimes C$ for some object $BF$ and some tensoring.

- Sequences:
  - $\Omega_x D \to \Fib_x(f) \to C\to D$
  - $C\to D\to \Cof(f) \to \Sigma C$
  - $\Omega_x C \to \mcl C \to C$
  - $G\to EG\to BG$
  - $\cdots \to C^I \to C \to \cdots$
  - $\cdots \to \mathcal{P}_x C \to C\to \cdots$

- Hope: $f \in [A, B]$ is an equivalence $\iff \Cof(f) \simeq \pt \iff \Fib_b(f) \simeq \pt$.

- A $\ZZ$ grading on $\mca$ with $\Cat_n := \mca_n$ and $\mca_0 = \mathbf{Set}$.

  - Try a fibration $n: \mca \to B\ZZ$ and unstraighten
  - Maybe $\mca_n := \Fun(I^n, A)$
  - $\pt$ is terminal in $\mca_n$ for every $n$.

- $\mca_n$ is enriched over $\mca_{n-1}$ for all $n\geq 0$.

- Functors $\Mor^n: \mca\to \mca_0$ and $\mathrm{Ob} := \Mor^0$

  - These should satisfy $\Mor^n = \Mor^1 \circ \Mor^{n-1}$, yielding a tower
    $$
    \cdots \to \mathcal{A}_n \xrightarrow{\mathrm{Mor}^1} \mathcal{A}_{n-1} \xrightarrow{\mathrm{Mor}^1} \mathcal{A}_{n-2} \xrightarrow{\mathrm{Mor}^1} \cdots \to\mathcal{A}_0
    $$

  - These should be “inverse” to the $BC$ construction, since $\mathrm{Ob}(BC) := \{1,2\}$ and $\Mor^n(BC) \supseteq \Mor^{n-1}(C)$ for all $n$. The subtlety: $BC$ has a tower of identity morphisms above $1$ and $2$. Also, $B \Mor^1 C$

- A functor $\Hom: \mca\to \mca$ where $\Hom_C$ has objects the categories $\Hom_C(x,y)$ for $x,y\in C$  and morphisms are functors.

  - $\Mor^1(C)$ should be something like $\int^{\Hom_C} \id$, the category of elements of $\Hom_C$.
  - Since $C\in \mca_n \implies \Hom_C(x, y)\in \mca_{n-1}$, we have $\Hom_C \in \mca_n$.

- A functor $\mathrm{Elt}: \mca \to \mca_0$ which sends $C$ to $\int^{\mathrm{Ob}(C)} \id$, the (discrete) category of elements of $C$.

  - Interpreting objects of $C\in \mca$ as categories, an *element* is any object in $\mathrm{Ob}(C)$, so it is an object of an object of a category.

- Possibly after stabilization, i.e. replacing $C$ with $\Sigma^\infty C := \lim(C \xrightarrow{\Sigma} C \xrightarrow{\Sigma} \cdots) \in \mca$, there should be a $\Sigma/\Omega$ calculus, so e.g.
  $$
  \pi_n(C) = [S^n, C] = [S^{n-1}\otimes S^1, C ] = [S^{n-1}, C^{S^1}] = \pi_{n-1}(\Omega C)
  $$

- There is a functor $(-)_\omega: \mathbf{Set} \to \mca$ where $X_\omega$ has cells of all orders, and is not just discrete.

- There are concrete constructions of $C\in \mca_n$ as length $n$ sequences of sets $(\Mor^k(C))_{0\leq k\leq n}$.

  - There is a concrete description of $\iota_n: \mca_n \to \mca_{n+1}$ and $\iota_{n, \omega}: \mca_n \to \mca$ in terms of these sequences.

- There is a notion of $C^n$, the set of $n$-cells, and $C^{(n)} := \bigcup_{0\leq k\leq n} C^k$, the $n$-skeleton.



Finally, we want to recover the following:

- $\Cat \in \mca_2$:

  - $\Elt(\Cat) \in \mca_0$: ordinary objects $X$, e.g. $X = \{1,2,3\}$.
  - $\mathrm{Ob}(\Cat) \in \mca_1$: ordinary categories $C$, e.g. $C = \mathbf{Set}$
  - $\Mor^1(\Cat) \in \mca_1$: functor categories $\Fun(C, D)$
  - $\Mor^2(\Cat)\in \mca_0$: natural transformations $\eta: F\to G$ 
  - $\Mor^{\geq 3}(\Cat) = \id$

- $C\in \mca_1$, e.g. $C = \mathbf{Set}$:

  - $\Elt(C) \in \mca_{-1}$: ordinary elements $x\in X$
  - $\mathrm{Ob}(C) \in \mca_0$: ordinary objects $X$.
  - $\Mor^1(C) \in \mca_0$: ordinary morphisms $f: X\to Y$
  - $\Mor^{\geq 2}(C) = \id$

- $X \in \mca_0$:

  - $\Elt(X) \in \mca_{-2} = \pt$, since elements have no further “elements”.
  - $\mathrm{Ob}(X) \in \mca_{-1}$: elements $x\in X$.
  - $\Mor^{\geq 1}(X) = \id$.

- $\Hom_C \in \mca_2$:

  - $\Elt(\Hom_C) \in \mca_0$: morphisms $f: X\to Y$ in $C$.
  - $\mathrm{Ob}(\Hom_C) \in \mca_1$: hom categories $\Hom_C(X, Y)$
  - $\Mor^1(\Hom_C)\in \mca_1$: functors $F: \Hom_C(X_1, Y_1) \to \Hom_C(X_2, Y_2)$
  - $\Mor^2(\Hom_C)\in \mca_0$: natural transformations $\eta: F \Rightarrow G$
  - $\Mor^{\geq 3}(\Hom_C) = \id$

- $\Hom_C(X, Y)\in \mca_0$ for $C\in \mca_1$

  - $\Elt(\Hom_C(X, Y)) \in \mca_{-2} = \pt$, since morphisms have no “elements”
  - $\mathrm{Ob}(\Hom_C(X, Y)) \in \mca_{-1}$: morphisms $f: X\to Y$
  - $\Mor^{\geq 1}(\Hom_C(X, Y)) = \id$

- $\Fun := \Hom_\mca \in \mca_2$:

  - $\Elt(\Fun) \in \mca_0$: functors $F\in \Fun(C, D)$ for $C,D\in \mca_1$.
  - $\mathrm{Ob}(\Fun) \in \mca_1$: functor categories $\Fun(C, D)$ for $C,D\in \mca_1$
  - $\Mor^1(\Fun) \in \mca_1$: functor categories $\Fun( \Fun(C_1, D_1), \Fun(C_2, D_2))$ for $C_i, D_i\in \mca_1$
  - $\Mor^2(\Fun) \in \mca_0$: natural transformations
  - $\Mor^{\geq 3}(\Fun) = \id$

- $[C, D] := \Fun(C, D) := \Hom_\mca(C, D) \in \mca_1$:

  - $\Elt(\Fun(C, D)) \in \mca_{-1}$: $\pt$
  - $\mathrm{Ob}(\Fun(C, D)) \in \mca_0$: functors $F:C\to D$
  - $\Mor^1(\Fun(C, D)) \in \mca_0$: natural transformations $\eta: F\Rightarrow G$
  - $\Mor^{\geq 2}(\Fun(C, D)) = \id$

  