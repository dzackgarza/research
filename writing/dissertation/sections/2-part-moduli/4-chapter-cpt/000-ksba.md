## Compactifications {#sec:chapter-4}

### Comparing Compactifications

Given a smooth projective family of varieties $\mcx \rightarrow \Delta$ over the unit disk with $\mcx_0$ $\mcx_0$ a simple normal crossings (SNC) divisor, the Clemens–Schmid exact sequence provides a powerful tool to analyze the limit mixed Hodge structure on the cohomology of the general fiber. This sequence, however, depends on the presence of semistable (SNC) reduction, and in general, no analogous sequence or description is known when the total space $\mcx$ is itself singular or the $\mcx_0$ has worse singularities.
To systematically handle degenerating families of higher-dimensional varieties -- where semistable reduction is either inadequate or inapplicable -- @KS88 introduced the theory of stable slc pairs. A **stable pair** consists of a projective variety $X$ (possibly reducible and with mild singularities) together with a $\QQ$-divisor $D$ such that $K_X + D$ is ample and $\QQ$-Cartier, and the pair $(X, D)$ has semi log canonical (slc) singularities. This generalizes the definition of stable curves from the classical Deligne–Mumford compactification $\cpt{\mcm }_g$ to all dimensions, and stable slc pairs provide a modular, proper, algebraic compactification of moduli spaces of varieties and pairs.
For moduli of K3 surfaces, this leads to the **KSBA compactification**: for a moduli space $F_{2d}$ of degree $2d$ polarized K3 surfaces, and for a suitable **recognizable** divisor $R$ on a generic such surface, one studies the closure of the locus of pairs $(X, \eps R)$ (for sufficiently small $\eps > 0$) in the moduli space of all KSBA stable pairs, sometimes referred to as *slc pairs* in the relevant literature. For example, for a degree two polarized K3 surface $(X, L)$, the linear system $|L|$ gives a double cover $X \rightarrow \PP^2$ branched along a sextic, and $R$ can be chosen as the ramification divisor for the covering involution. When $R$ is recognizable, there exists a semifan $\semifan{F}_R$ so that the normalization of the KSBA compactification $\ksbacpt{F_{2d}}$ is isomorphic to the corresponding **semitoroidal compactification** $\semifancpt{F_{2d}}{\semifan{F}_R}$. The precise construction of such semifans is highly nontrivial and depends on the geometry of the polarization.

Drawing an analogy with the Deligne–Mumford compactification of $\mcm_g$, one obtains the following procedure for families of surfaces: after base change and birational modifications, any family $\mcx \to \Delta$ of surfaces can be replaced by a semistable model, that is, with $\mcx$ smooth and the $\mcx_0$ $\mcx_0$ a reduced snc divisor. One then contracts $(-1)$-curves in the fibers to obtain a relatively minimal model with smooth total space. To construct a stable model, one further contracts all $(-2)$-curves in the fibers; this produces a family whose total space is typically singular, but whose $\mcx_0$ is uniquely determined and has at worst nodal singularities. This uniqueness (up to isomorphism), together with the finiteness of the automorphism group and the ampleness of the dualizing sheaf, are the properties which extend to higher dimensional varieties.
Recall that a divisor $D$ on a normal variety $X$ has simple normal crossings (snc) if, in a Zariski neighborhood of every point, its support is defined by the vanishing of a product of coordinate functions. A log pair $(X,D)$ is said to be **divisorial log terminal** (dlt) if there exists an open subset $U \subseteq X$ such that $D|_U$ has snc support, and for any divisorial valuation $E$ centered in $X \setminus U$, the log discrepancy $a(E,X,D)>-1$.
A **KSBA-stable pair** is a pair $(X, D=\sum b_j D_j)$ where $X$ is a projective demi-normal variety (that is, $X$ satisfies Serre's condition $S_2$ and has normal crossing singularities in codimension $1$), the divisorial components $D_j$ are effective Weil divisors of $X$ not contained in the singular locus of $X$, and the coefficients $b_j$ are rational numbers with $0 < b_j < 1$, such that:

1. The divisor $K_X + D$ is ample and $\QQ$-Cartier.
2. The pair $(X, D)$ has semi log canonical (slc) singularities 
  
<!-- see [Kollár, *Singularities of the Minimal Model Program*, Cambridge, 2013, Definition 5.10]). -->

This notion generalizes the stability condition for curves: for $X$ a nodal curve and $D = \sum b_j p_j$ a divisor with $0 < b_j < 1$, the pair $(X, D)$ is KSBA stable if and only if $X$ is stable in the sense of Deligne–Mumford.
The KSBA compactification provides a canonical and proper compactification of the moduli space of varieties and pairs of log general type by allowing stable pairs $(X, D)$ with semi log canonical singularities and ample $K_X + D$. As a consequence, these moduli spaces are proper and projective, and their construction is compatible with the minimal model program. 

<!-- see [Kollár, *Moduli of varieties of general type*, in: *Handbook of Moduli*, vol. II (2013), 131–157, arXiv:1008.0621], [@Alexeev, *Comp. Math.* 112 (1998), 147–182], [Kollár–Shepherd-Barron, *J. Algebraic Geom.* 1 (1992), 429–479]. -->

<!-- see (Kollár–Shepherd-Barron–Alexeev) compactification, as constructed in [Kollár–Shepherd-Barron, *J. Algebraic Geom.* 1 (1992), 429–479], [@Alexeev, *Comp. Math.* 112 (1998), 147–182], and [Kollár, *Moduli of varieties of general type*, Handbook of Moduli, vol. II, 2013 (arXiv:1008.0621)],  -->

### Recognizable Divisors

Let $F_S$ be the moduli space of $S$-polarized K3 surfaces, and let $R$ be a canonical ample divisor on the generic surface in $F_S$. The divisor $R$ is called **recognizable** (for $F_S$) if for any $S$-quasipolarized Kulikov degeneration $\mcx \to \Delta$, there exists a divisor $R_0 \subset \mcx_0$ such that, for any other smoothing $\tilde{\mcx} \to \Delta$ with $\mcx_0$ $\tilde{\mcx}_0$, the divisor $R_0$ is, up to the connected component of the identity $\Aut^0(\tilde{\mcx}_0)$, the unique flat limit of the divisors $R_t \subset \mcx_t$ as $t \to 0$.This yields a form of uniqueness and "path-independence" for Kulikov models, namely that $R$ extends unambiguously to all boundary components of $F_S$.
For any choice of recognizable divisor, the normalization of the KSBA stable pair compactification $\ksbacpt{F}_R$ is a semitoroidal compactification of the period domain, with the semifan determined by $R$.
A canonical example of a recognizable divisor comes from @AE23, who compactify the moduli spaces $F_{2d}$ of polarized K3 surfaces $(X, L)$ of degree $2d$.
The **rational curve divisor** is the formal sum $R_\rcop$ of all smooth genus zero curves in the linear system $\abs{L}$:

\begin{align*}
R_\rcop \da  \sum_{i=1}^{n_d} R_i \in |n_d L|
.\end{align*}

where each $R_i$ is an irreducible rational curve and $n_d$ is given by the *Yau–Zaslow* formula, see e.g. [@AE23, Thm. 10.2].
In loc.cit., this divisor is shown to be recognizable for all $d$, and thus there are semifans such that $\semitorcpt{F_{2d}} \cong \ksbacpt{F_{2d}}$.
The proof uses the Kontsevich moduli space of stable maps, Gromov-Witten invariants, and properties of rational stable maps to surfaces with K-trivial degenerations.

This follows a similar line of work: for $F_2$, see [@AET23], and for degree 2 elliptic K3 surfaces $\fell$, see [@ABE22]. These are $S$-polarized K3 surfaces for $S$ a 2-elementary lattice that primitively embeds in $\lkt$, of which there are exactly 75 by @Nik79a, and [@AE22, Thm. 9.10] handles the remaining cases, including $\fttz$ corresponding to $S = U(2) = (2,2,0)_1$, using the fact that such surfaces carry a nonsymplectic involution $\iota$ whose ramification divisor $R_\iota$ is recognizable.
For $50$ of these cases, there is result similar to @thm:main-theorem: $\semitorcpt{F_S} \iso \ksbacpt{F_S}$ for a semifan associated to $R_\iota$ -- they are precisely the closures of irreducible components on which monodromy invariants $\lambda$ maintain a fixed *combinatorial type*, as defined in @AE23a.
By passing to Kulikov models with nonsymplectic involutions, they show that stable limits can be constructed using the fact that the central fibers $\mcx_0 = \union_i V_i$ of Type $\II$ Kulikov models $\mcx$ of K3 surfaces admit dual complexes $\Gamma(\mcx_0)$ homeomorphic to $S^2$, which can naturally be equipped with integral affine structures, yielding an $\iota$-symmetric $\IAS^2$, where $\iota$ typically acts on $S^2$ by $(x,y,z)\mapsto (x,y,-z)$ in the standard coordinates on $\RR^3$.
Thus one can reverse-engineer this procedure, starting with a model for a hemisphere of $S^2$ which is homeomorphic to $\DD^2$, and realizing $S^2 \cong \DD^2 \Disjoint_{\bd \DD^2} \DD^2$ as the pushout of two discs along their boundaries, naturally enforcing $\iota$-invariance. 
The process starts from a *monodromy invariant* $\lambda$ encoding a degeneration, then constructs an integral-affine polygon $P(\lambda)$ in $\RR^2$ with singularities, performing Symington surgeries on $P(\lambda)$ that encode the degeneration. Passing to a complete triangulation and taking the pushout

\begin{align*}
B(\lambda) \da  P(\lambda) \Disjoint_{\partial P(\lambda)} (-P(\lambda))
,\end{align*}

where $-P(\lambda)$ denotes reversing the orientation, yields an $\IAS^2$.

From this, one can construct a *$d$-semistable Kulikov surface* such that $B(\lambda) \cong \Gamma(\mcx_0(\lambda) )$, which by @Fri83a smooths to K3 surface $\mcx_t \da \mcx_t(\lambda)$ and thus specifies a family $\mcx \da \mcx(\lambda)$.
One extends the induced involution $\iota$ on $mcx_0$ to $\mcx$, passes to a carefully chosen divisorial component of the ramification divisor $R_\iota$ on $\mcx$ and performs modifications to obtain a pair $(X,\eps R) \da (X(\lambda), \eps R(\lambda))$.
One then shows that the limit of $R_\iota$ is big and nef and thus defines a contraction $\pi: (X, \eps R) \to (\bar X, \eps \bar R)$ to a KSBA stable pair
There is a decomposition $X = \union_i ( V_i, D_i)$ into irreducible components indexed by the lattice points in $B(\lambda)$, each of which forms an anticanonical pair, and so we can write $(X, \eps R) = \union_i ((V_i, D_i), \eps R_i)$, which contracts under $\pi$ to a decomposition $(\bar X, \eps \bar R) = \union_i ( (\bar V_i, \bar D_i ), \eps \bar R_i )$ of the stable model.
Tracing this construction backwards, we thus access the irreducible components of the stable model by understanding how the contraction $\pi$ combinatorially acts at the level of $B(\lambda) = \Gamma(\mcx_0)$, and in particular how the contraction acts on individual anticanonical pairs $(V_i, D_i)$.
By analogy, we seek a similar method of studying Enriques surfaces.