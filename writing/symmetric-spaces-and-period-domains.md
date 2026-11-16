# Symmetric Spaces and Period Domains {#sec-symmetric-spaces-period-domains}

We collect the homogeneous-space descriptions associated with the metrics and complex structures of @sec-calculus-on-schemes. The classical groups and their symmetric spaces are as in [@Hel01, Chapters VIII and X]; the bounded domains and their compact duals are as in [@Viv14, §§2–3]. Complex Hermitian pairings are linear in the first argument, as in that chapter. For right quaternionic vector spaces, we explicitly use conjugate-linearity in the first argument.

## Classical groups {#sec-hsd-groups}

Write $A^*=\overline A^{\mathsf t}$, and set

\begin{align*}
I_{p,q}&=\begin{pmatrix}I_p&0\\0&-I_q\end{pmatrix},&
J_n&=\begin{pmatrix}0&I_n\\-I_n&0\end{pmatrix},&
D_n&=\begin{pmatrix}0&I_n\\I_n&0\end{pmatrix}.
\end{align*}

The subscript in $\operatorname{Sp}(2n,k)$ is the dimension of its defining vector space. We use $\operatorname{Sp}(n)$ for the compact quaternionic unitary group. Thus

\begin{align*}
\operatorname O(p,q)&=\{g\in\operatorname{GL}(p+q,\mathbb R):g^{\mathsf t}I_{p,q}g=I_{p,q}\},\\
\operatorname{SO}(p,q)&=\operatorname O(p,q)\cap\operatorname{SL}(p+q,\mathbb R),\\
\operatorname U(p,q)&=\{g\in\operatorname{GL}(p+q,\mathbb C):g^*I_{p,q}g=I_{p,q}\},\\
\operatorname{SU}(p,q)&=\operatorname U(p,q)\cap\operatorname{SL}(p+q,\mathbb C),\\
\operatorname{Sp}(2n,k)&=\{g\in\operatorname{GL}(2n,k):g^{\mathsf t}J_ng=J_n\},\qquad k=\mathbb R,\mathbb C,\\
\operatorname{Sp}(n)&=\{g\in\operatorname{GL}(n,\mathbb H):g^*g=I_n\}
\cong\operatorname{Sp}(2n,\mathbb C)\cap\operatorname U(2n),\\
\operatorname{Sp}(p,q)&=\{g\in\operatorname{GL}(p+q,\mathbb H):g^*I_{p,q}g=I_{p,q}\}.
\end{align*}

Here $*$ on quaternionic matrices is quaternionic conjugate transpose. Under the complex representation of $\mathbb H^{p+q}$, the last group is

\begin{align*}
\operatorname{Sp}(2(p+q),\mathbb C)\cap\operatorname U(2p,2q),
\end{align*}

with the Hermitian form represented by $\operatorname{diag}(I_{p,q},I_{p,q})$ in the corresponding basis. The compact group $\operatorname{Sp}(n)$ is also denoted $\operatorname{USp}(2n)$; the archived notation $\operatorname{USp}_n$ counts quaternionic dimension.

:::{.definition #def:hsd-quaternionic-real-forms title="Quaternionic real forms"}
Let $\jmath(z)=J_n\bar z$ on $\mathbb C^{2n}$. Set

\begin{align*}
\operatorname{SU}^*(2n)&=\{g\in\operatorname{SL}(2n,\mathbb C):g\jmath=\jmath g\},\\
\operatorname{SO}^*(2n)&=\{g\in\operatorname{SL}(2n,\mathbb C):g^{\mathsf t}g=I_{2n},\ g^*J_ng=J_n\}.
\end{align*}

The first group is $\operatorname{SL}(n,\mathbb H)$, with determinant understood via its complex representation. The second preserves a complex symmetric form and a skew-Hermitian form [@Hel01, Chapter X, §2].
:::

:::{.remark #rmk:hsd-quaternionic-orthogonal title="Quaternionic orthogonal notation"}
For the quaternions $i,j,k$, the map
$\tau(a+bi+cj+dk)=a+bi-cj+dk$ is an anti-involution. It satisfies $\tau(q)=j^{-1}\bar qj$. Hence

\begin{align*}
\tau(g)^{\mathsf t}g=I_n
\quad\Longleftrightarrow\quad
g^*(jI_n)g=jI_n.
\end{align*}

This is the quaternionic skew-Hermitian description of $\operatorname{SO}^*(2n)$, sometimes written $\operatorname{SO}(n,\mathbb H)$. It is distinct from $\operatorname{Sp}(n)$, which preserves a quaternionic Hermitian form.
:::

Write $G^0$ for the identity component of a real Lie group. For block diagonal groups, $S(G_1\times G_2)$ means the subgroup with product of determinants equal to one.

## Homogeneous spaces and Grassmannians {#sec-hsd-grassmannians}

:::{.definition #def:hsd-symmetric-space title="Symmetric spaces"}
A connected Riemannian manifold is *symmetric* if every point $x$ admits an isometry $s_x$ with $s_x(x)=x$ and $(ds_x)_x=-1$. It is *Hermitian symmetric* if it is Hermitian and each $s_x$ can be chosen holomorphic [@Hel01, Chapter IV, §3; @Viv14, Definition 2.4].
:::

:::{.remark #rmk:hsd-local-symmetry title="Local and global symmetries"}
In normal coordinates the geodesic symmetry at $x$ is $s_x(\exp_xv)=\exp_x(-v)$. For the Levi-Civita connection it is a local isometry at every point precisely when $\nabla R=0$ [@Hel01, Chapter IV, §1, Theorems 1.1 and 1.3]. If also $\nabla J=0$, the local symmetries preserve $J$: they preserve the connection, and their differentials commute with $J$ at $x$ and hence throughout a normal neighborhood by parallel transport. The latter equation is the Kähler criterion of @thm:calculus-kahler-equivalences. A global symmetry is a holomorphic isometry defined on all of $M$; the local condition alone does not give one on a quotient of $M$.

An involutive holomorphic isometry fixing $x$ with $x$ isolated in its fixed locus has $(ds_x)_x=-1$. Indeed, the differential of an involution has eigenvalues $\pm1$, and the $+1$ eigenspace is tangent to its local fixed locus. This is the isolated-fixed-point formulation in [@Viv14, Definition 2.4 and Remark 2.5].
:::

:::{.remark #rmk:hsd-types title="Euclidean, compact, and noncompact types"}
A Hermitian symmetric manifold of *Euclidean type* is $\mathbb C^m/\Lambda$ with its flat metric, for a discrete additive subgroup $\Lambda\subset\mathbb C^m$. A non-Euclidean one is *irreducible* if it has no nontrivial product decomposition. Every Hermitian symmetric manifold has a unique product decomposition into a Euclidean factor, a product of compact irreducible factors, and a product of noncompact irreducible factors [@Viv14, Definition 2.7 and Theorem 2.9]. The last factors are *Hermitian symmetric domains*. Their Borel embeddings are open embeddings into the corresponding compact duals [@Viv14, §2.4].

A *bounded symmetric domain* is a connected bounded open set $D\subset\mathbb C^N$ with an involutive biholomorphism fixing each chosen point in isolation. Its Bergman metric makes it a Hermitian symmetric manifold of noncompact type; conversely, the Harish-Chandra embedding realizes each manifold of noncompact type as such a domain [@Viv14, Theorems 2.25 and 2.27].
:::

The quotients below are diffeomorphisms of homogeneous manifolds. Their invariant metrics have a choice of scale. For a transitive action, the map $G/G_x\to Gx$, $gG_x\mapsto gx$, gives the identification.

:::{.example #ex:hsd-compact-grassmannians title="Ordinary Grassmannians"}
Let $\operatorname{Gr}_p(k^{p+q})$ denote the space of $p$-dimensional $k$-subspaces. Orthonormal bases give

\begin{align*}
\operatorname{Gr}_p(\mathbb R^{p+q})
&\cong\frac{\operatorname O(p+q)}{\operatorname O(p)\times\operatorname O(q)}
\cong\frac{\operatorname{SO}(p+q)}{S(\operatorname O(p)\times\operatorname O(q))},\\
\operatorname{Gr}^{\mathrm{or}}_p(\mathbb R^{p+q})
&\cong\frac{\operatorname{SO}(p+q)}{\operatorname{SO}(p)\times\operatorname{SO}(q)},\\
\operatorname{Gr}_p(\mathbb C^{p+q})
&\cong\frac{\operatorname U(p+q)}{\operatorname U(p)\times\operatorname U(q)}
\cong\frac{\operatorname{SU}(p+q)}{S(\operatorname U(p)\times\operatorname U(q))},\\
\operatorname{Gr}_p(\mathbb H^{p+q})
&\cong\frac{\operatorname{Sp}(p+q)}{\operatorname{Sp}(p)\times\operatorname{Sp}(q)}.
\end{align*}

The oriented formula is for $p,q>0$. In particular,

\begin{align*}
S^n&\cong\operatorname{SO}(n+1)/\operatorname{SO}(n)
\cong\operatorname{Gr}^{\mathrm{or}}_1(\mathbb R^{n+1}),\\
\mathbb P^n(\mathbb R)&\cong\operatorname{SO}(n+1)/S(\operatorname O(n)\times\operatorname O(1)),\\
\mathbb P^n(\mathbb C)&\cong\operatorname{SU}(n+1)/S(\operatorname U(n)\times\operatorname U(1)),\\
\mathbb P^n(\mathbb H)&\cong\operatorname{Sp}(n+1)/(\operatorname{Sp}(n)\times\operatorname{Sp}(1)).
\end{align*}

The sphere has isometry group $\operatorname O(n+1)$; its antipodal quotient has isometry group $\operatorname{PO}(n+1)$. Euclidean space has the homogeneous description $\mathbb R^n\cong(\mathbb R^n\rtimes\operatorname O(n))/\operatorname O(n)$.
:::

:::{.definition #def:hsd-positive-grassmannians title="Positive Grassmannians"}
On $\mathbb R^{p,q}$ use the form with matrix $I_{p,q}$. Set

\begin{align*}
\operatorname{Gr}_k^+(\mathbb R^{p,q})
&=\{V\subset\mathbb R^{p,q}:\dim V=k,\ (\ ,\ )|_V>0\}.
\end{align*}

Adding an orientation gives $\operatorname{Gr}_k^{+,\mathrm{or}}$. For $0\leq k\leq p$, extension of orthonormal bases gives

\begin{align*}
\operatorname{Gr}_k^+(\mathbb R^{p,q})
&\cong\frac{\operatorname O(p,q)}{\operatorname O(k)\times\operatorname O(p-k,q)},\\
\operatorname{Gr}_k^{+,\mathrm{or}}(\mathbb R^{p,q})
&\cong\frac{\operatorname O(p,q)}{\operatorname{SO}(k)\times\operatorname O(p-k,q)}.
\end{align*}

In particular, the stabilizer of the standard maximal positive subspace $\mathbb R^p\oplus0$ is $\operatorname O(p)\times\operatorname O(q)$. For $p,q>0$, the oriented maximal positive Grassmannian has two components, each isomorphic to

\begin{align*}
\frac{\operatorname{SO}^0(p,q)}{\operatorname{SO}(p)\times\operatorname{SO}(q)}.
\end{align*}

Over $\mathbb C$, the corresponding positive Grassmannian is
$\operatorname{Gr}_p^+(\mathbb C^{p,q})\cong\operatorname U(p,q)/(\operatorname U(p)\times\operatorname U(q))\cong\operatorname{SU}(p,q)/S(\operatorname U(p)\times\operatorname U(q))$.
:::

:::{.remark #rmk:hsd-positive-graphs title="Graph coordinates"}
Every maximal positive subspace of $\mathbb R^p\oplus\mathbb R^q$ is the graph of a unique map $A:\mathbb R^p\to\mathbb R^q$. Its restricted form is $I_p-A^{\mathsf t}A$, so

\begin{align*}
\operatorname{Gr}_p^+(\mathbb R^{p,q})
&\cong\{A\in\operatorname{Mat}_{q\times p}(\mathbb R):I_p-A^{\mathsf t}A>0\}.
\end{align*}

An orientation on the graph is specified by an orientation of its projection onto $\mathbb R^p$. This explains both components in the oriented case. For $p=2$, transposing $A$ gives the model $\{B\in\operatorname{Mat}_{2\times q}(\mathbb R):I_2-BB^{\mathsf t}>0\}$ for either component.
:::

### Isotropic Grassmannians and complex structures

:::{.definition #def:hsd-isotropic-grassmannians title="Isotropic Grassmannians"}
For a nondegenerate symmetric form $b$ on $V$, write $\operatorname{OGr}_k(V,b)=\{W\in\operatorname{Gr}_k(V):b|_{W\times W}=0\}$. For an alternating form $\omega$, use $\operatorname{SGr}_k(V,\omega)$ for the same condition. In symplectic dimension $2n$, $\operatorname{LGr}(V,\omega)=\operatorname{SGr}_n(V,\omega)$ is the *Lagrangian Grassmannian*.
:::

:::{.example #ex:hsd-isotropic-models title="Compact models for isotropic Grassmannians"}
Choose a positive compatible complex structure on $(\mathbb R^{2n},\omega)$. A real isotropic $k$-frame is unitary after orthonormalization, and its stabilizer gives

\begin{align*}
\operatorname{SGr}_k(\mathbb R^{2n},\omega)
&\cong\frac{\operatorname U(n)}{\operatorname O(k)\times\operatorname U(n-k)},&
\operatorname{LGr}(\mathbb R^{2n},\omega)&\cong\operatorname U(n)/\operatorname O(n),\\
\operatorname{LGr}(\mathbb C^{2n},\omega)
&\cong\operatorname{Sp}(n)/\operatorname U(n).
\end{align*}

In the complex case, extend an orthonormal basis of a Lagrangian using the standard quaternionic structure to obtain a symplectic unitary basis; its stabilizer is $\operatorname U(n)$.

For real signature $(p,q)$ and $k\leq\min(p,q)$, an isotropic plane is the graph of an isometry between $k$-planes in the positive and negative factors. Consequently

\begin{align*}
\operatorname{OGr}_k(\mathbb R^{p,q})
&\cong\frac{\operatorname O(p)\times\operatorname O(q)}
{\Delta\operatorname O(k)\times\operatorname O(p-k)\times\operatorname O(q-k)}.
\end{align*}

For the complexification of a positive real quadratic space,

\begin{align*}
\operatorname{OGr}_k(\mathbb C^N,\textstyle\sum z_i^2)
&\cong\frac{\operatorname O(N)}{\operatorname U(k)\times\operatorname O(N-2k)}.
\end{align*}

Indeed, a complex isotropic $k$-plane determines an orthogonal complex structure on its underlying real $2k$-plane, and conversely its $i$-eigenspace recovers the isotropic plane. For $N=2n$, this gives $\operatorname O(2n)/\operatorname U(n)$, with two components $\operatorname{SO}(2n)/\operatorname U(n)$. Changing the complex quadratic form to the split matrix $D_n$ gives an isomorphic variety.
:::

:::{.remark #rmk:hsd-structures-versus-subspaces title="Spaces of compatible structures"}
These descriptions give several different spaces:

- Orthogonal complex structures on $\mathbb R^{2n}$ form $\operatorname O(2n)/\operatorname U(n)$.
- Quaternionic-linear orthogonal complex structures on $\mathbb H^n$ form $\operatorname{Sp}(n)/\operatorname U(n)$: conjugate left multiplication by $i$, whose centralizer is $\operatorname U(n)$.
- Conjugate-linear isometric involutions on $\mathbb C^n$ form $\operatorname U(n)/\operatorname O(n)$. Their fixed real subspaces are Lagrangian for the imaginary part of the Hermitian form.
- Conjugate-linear isometries $Q$ on $\mathbb C^{2n}$ with $Q^2=-1$ form $\operatorname U(2n)/\operatorname{Sp}(n)$; these are compatible quaternionic structures.
- Positive $\omega$-compatible complex structures on $\mathbb R^{2n}$ form $\operatorname{Sp}(2n,\mathbb R)/\operatorname U(n)$, as in @sec-hsd-siegel.

Each quotient follows by taking an orthonormal basis adapted to the structure and computing its stabilizer. In particular, a quaternionic Hermitian vector space needs a specified additional form before an isotropic Grassmannian is defined.
:::

:::{.example #ex:hsd-split-isotropics title="Split Hermitian and skew-Hermitian forms"}
For $k=\mathbb R,\mathbb C,\mathbb H$, put $U_k(n)=\operatorname O(n),\operatorname U(n),\operatorname{Sp}(n)$ respectively. The maximal isotropic subspaces for the split Hermitian form with matrix $D_n$ on $k^{2n}$ form

\begin{align*}
\frac{U_k(n)\times U_k(n)}{\Delta U_k(n)}\cong U_k(n).
\end{align*}

After diagonalizing the form to $I_{n,n}$, every such subspace is the graph of an isometry $k^n\to k^n$.

The maximal quaternionic isotropic $n$-planes for the skew-Hermitian form $b(x,y)=x^*J_ny$ on $\mathbb H^{2n}$ form $\operatorname U(2n)/\operatorname{Sp}(n)$. To see the stabilizer, regard $J_n$ as an orthogonal quaternionic-linear complex structure. An isotropic plane $W$ has $J_nW=W^\perp$. Orthonormal bases of $W$ and $J_nW$ identify any two such decompositions; transformations commuting with $J_n$ form $\operatorname U(2n)$, and those fixing $W$ form $\operatorname{Sp}(n)$.
:::

## Matrix spaces and symmetric pairs {#sec-hsd-matrices}

Let $\operatorname{Sym}_n(\mathbb R)=\{A:A^{\mathsf t}=A\}$ and $\operatorname{Herm}_n(\mathbb C)=\{A:A^*=A\}$. A superscript $+$ denotes the positive-definite cone, and a subscript $1$ imposes determinant one. These cones parametrize positive inner products in a chosen basis. The maps $g\mapsto gg^{\mathsf t}$ and $g\mapsto gg^*$ give

\begin{align*}
\operatorname{Sym}_n^+(\mathbb R)&\cong\operatorname{GL}(n,\mathbb R)/\operatorname O(n),&
\operatorname{Sym}_{n,1}^+(\mathbb R)&\cong\operatorname{SL}(n,\mathbb R)/\operatorname{SO}(n),\\
\operatorname{Herm}_n^+(\mathbb C)&\cong\operatorname{GL}(n,\mathbb C)/\operatorname U(n),&
\operatorname{Herm}_{n,1}^+(\mathbb C)&\cong\operatorname{SL}(n,\mathbb C)/\operatorname{SU}(n).
\end{align*}

Surjectivity follows from the positive square root; the displayed compact groups are the stabilizers of $I_n$. Here positivity includes symmetry or Hermitian symmetry. The real dimension of $\operatorname{Sym}_{n,1}^+(\mathbb R)$ is $n(n+1)/2-1$: symmetric matrices have $n(n+1)/2$ independent entries, and the derivative of determinant at $I_n$ is the nonzero trace functional.

:::{.example #ex:hsd-classical-pairs title="Classical symmetric pairs"}
The classical compact/noncompact pairs are [@Hel01, Chapter X, §6]:

| Type | Noncompact space | Compact dual |
| --- | --- | --- |
| AI | $\operatorname{SL}(n,\mathbb R)/\operatorname{SO}(n)$ | $\operatorname{SU}(n)/\operatorname{SO}(n)$ |
| AII | $\operatorname{SU}^*(2n)/\operatorname{Sp}(n)$ | $\operatorname{SU}(2n)/\operatorname{Sp}(n)$ |
| AIII | $\operatorname{SU}(p,q)/S(\operatorname U(p)\times\operatorname U(q))$ | $\operatorname{SU}(p+q)/S(\operatorname U(p)\times\operatorname U(q))$ |
| BDI | $\operatorname{SO}^0(p,q)/(\operatorname{SO}(p)\times\operatorname{SO}(q))$ | $\operatorname{SO}(p+q)/(\operatorname{SO}(p)\times\operatorname{SO}(q))$ |
| DIII | $\operatorname{SO}^*(2n)/\operatorname U(n)$ | $\operatorname{SO}(2n)/\operatorname U(n)$ |
| CI | $\operatorname{Sp}(2n,\mathbb R)/\operatorname U(n)$ | $\operatorname{Sp}(n)/\operatorname U(n)$ |
| CII | $\operatorname{Sp}(p,q)/(\operatorname{Sp}(p)\times\operatorname{Sp}(q))$ | $\operatorname{Sp}(p+q)/(\operatorname{Sp}(p)\times\operatorname{Sp}(q))$ |

The Hermitian families are AIII, DIII, CI, and BDI when one signature index is two, together with EIII and EVII. The exceptional EIII space has complex dimension $16$ and group locally $E_{6(-14)}$ with maximal compact locally $\operatorname{Spin}(10)\times\operatorname U(1)$; EVII has complex dimension $27$ and group locally $E_{7(-25)}$ with maximal compact locally $E_6\times\operatorname U(1)$. Their compact duals use the compact real forms of $E_6$ and $E_7$ [@Viv14, §§3.5–3.6].
:::

## Hyperbolic models {#sec-hsd-hyperbolic}

:::{.example #ex:hsd-hyperbolic-spaces title="Negative lines"}
For $k=\mathbb R,\mathbb C,\mathbb H$, regard $k^{n+1}$ as a right $k$-vector space. In this model we use the form $h$ linear in the second variable:

\begin{align*}
h(x,y)&=\sum_{j=1}^n\overline{x_j}y_j-\overline{x_{n+1}}y_{n+1},&
\mathbb H_k^n&=\{\ell\in\mathbb P(k^{n+1}):h|_\ell<0\}.
\end{align*}

The positive orthogonal complement identifies negative lines with maximal positive $n$-planes. Their homogeneous descriptions are

\begin{align*}
\mathbb H_{\mathbb R}^n&\cong\operatorname{SO}^0(n,1)/\operatorname{SO}(n),\\
\mathbb H_{\mathbb C}^n&\cong\operatorname{SU}(n,1)/S(\operatorname U(n)\times\operatorname U(1)),\\
\mathbb H_{\mathbb H}^n&\cong\operatorname{Sp}(n,1)/(\operatorname{Sp}(n)\times\operatorname{Sp}(1)).
\end{align*}

The real model also identifies with either component of $\operatorname{Gr}^{+,\mathrm{or}}_n(\mathbb R^{n,1})$. The group action is transitive by an orthonormal basis calculation, with the displayed stabilizers.
:::

:::{.remark #rmk:hsd-hyperboloid title="The hyperboloid"}
Start instead with $\mathbb R^{1,n}$ and $q(x)=x_0^2-\sum_{j=1}^nx_j^2$. The locus $q(x)=1$ is $H^+\sqcup H^-$, where $H^+$ is the sheet $x_0>0$. At $x\in H^+$, $T_xH^+=x^\perp$ is negative definite, so the hyperbolic metric is $-q|_{T_xH^+}$. Sending $x$ to its positive line identifies $H^+$ with $\mathbb H_{\mathbb R}^n$ after reversing the sign of the form.

The full isometry group is the sheet-preserving subgroup $\operatorname O^{\mathrm{sheet}}(1,n)$, isomorphic to $\operatorname{PO}(1,n)$: in each pair $\{g,-g\}$ exactly one preserves $H^+$. Thus the hyperboloid has dimension $n$.

![The two sheets of the hyperboloid $q=-1$ in the opposite-sign convention of $\mathbb R^{2,1}$.](/rendered/fig_hyperbolic_quadric.png){#fig-hyperbolic-two-sheets}

![A positive cone and one normalized sheet in $\mathbb R^{1,2}$.](/rendered/fig_hyperboloid_sheet.png){#fig-hyperboloid-cone-sheet}

Stereographic projection from $(-1,0,\ldots,0)$ gives the Poincaré ball
model. With $x=(x_0,x_1,\ldots,x_n)\in H^+$, its map and inverse are
\[
\phi(x)=\frac{(x_1,\ldots,x_n)}{1+x_0}\in B^n,
\qquad
\phi^{-1}(u)=\frac{(1+\lVert u\rVert^2,\,2u)}{1-\lVert u\rVert^2}.
\]
The hyperboloid equation gives $\lVert\phi(x)\rVert<1$ and verifies the
inverse formula. In this model geodesics are diameters or circular arcs
orthogonal to $\partial B^n$. Central projection $x\mapsto(x_1,\ldots,x_n)/x_0$
instead gives the projective (Klein) ball model; it is not the Poincaré
projection.
:::

:::{.example #ex:hsd-upper-half-plane title="The hyperbolic plane"}
The following models are diffeomorphic, with invariant metrics matched by a scale choice:

\begin{align*}
\mathbb H_{\mathbb R}^2
&\cong\{z\in\mathbb C:\operatorname{Im}z>0\}
\cong\operatorname{SL}(2,\mathbb R)/\operatorname{SO}(2)\\
&\cong\operatorname{Sym}_{2,1}^+(\mathbb R)
\cong\operatorname{SO}^0(2,1)/\operatorname{SO}(2)
\cong\operatorname{Sp}(2,\mathbb R)/\operatorname U(1).
\end{align*}

The Cayley transform $z\mapsto(z-i)/(z+i)$ gives the unit disc, also $\mathbb H_{\mathbb C}^1\cong\operatorname{SU}(1,1)/S(\operatorname U(1)\times\operatorname U(1))$.
Among the spaces $\operatorname{SL}(n,\mathbb R)/\operatorname{SO}(n)$ with $n\geq2$, only $n=2$ is Hermitian symmetric: the irreducible Hermitian families in @rmk:hsd-type-dictionary contain the rank-one coincidence $AI_2\cong CI_1$, but no higher-rank $AI_n$ [@Hel01, Chapter X, §6].
:::

:::{.example #ex:hsd-one-dimensional title="The disc, projective line, and flat quotients"}
On $\mathfrak H_1=\{x+iy:y>0\}$, the metric $y^{-2}(dx^2+dy^2)$ has curvature $-1$. The holomorphic isometry $z\mapsto-1/z$ fixes $i$ in isolation; conjugating it by the transitive $\operatorname{PSL}(2,\mathbb R)$ action gives a symmetry at every point. Under the Cayley transform the symmetry at $0\in\mathbb D$ is $z\mapsto-z$. Explicitly,

\begin{align*}
\operatorname{SU}(1,1)&=\left\{\begin{pmatrix}a&b\\\bar b&\bar a\end{pmatrix}:|a|^2-|b|^2=1\right\},&
\begin{pmatrix}a&b\\\bar b&\bar a\end{pmatrix}\cdot z&=\frac{az+b}{\bar bz+\bar a}.
\end{align*}

The complex projective line, with a Fubini–Study metric scaled to make $\mathbb P^1(\mathbb C)\cong S^2$ the unit round sphere, is the compact counterpart. Its holomorphic isometry $[z_0:z_1]\mapsto[z_0:-z_1]$ fixes $[1:0]$ in isolation; $\operatorname{PSU}(2)\cong\operatorname{SO}(3)$ moves this symmetry to every point. Finally, $\mathbb C^m/\Lambda$ is of Euclidean type: translations are transitive and $[z]\mapsto[2a-z]$ is the symmetry at $[a]$ [@Viv14, Example 2.6].
:::

## Hermitian symmetric domains {#sec-hsd-domains}

:::{.remark #rmk:hsd-type-dictionary title="Cartan's domains and compact duals"}
The classical bounded domains, their transitive groups, and compact duals are [@Viv14, §§3.1–3.4]:

| Domain | Bounded realization | Noncompact quotient | Compact dual | Root type |
| --- | --- | --- | --- | --- |
| $I_{p,q}$ | $Z\in\operatorname{Mat}_{p\times q}(\mathbb C),\ I_q-Z^*Z>0$ | $\operatorname{SU}(p,q)/S(\operatorname U(p)\times\operatorname U(q))$ | $\operatorname{Gr}_q(\mathbb C^{p+q})$ | $A_{p+q-1}$ |
| $II_n$ | $Z^{\mathsf t}=-Z,\ I_n-Z^*Z>0$ | $\operatorname{SO}^*(2n)/\operatorname U(n)$ | One component of $\operatorname{OGr}_n(\mathbb C^{2n},D_n)$ | $D_n$ |
| $III_n$ | $Z^{\mathsf t}=Z,\ I_n-Z^*Z>0$ | $\operatorname{Sp}(2n,\mathbb R)/\operatorname U(n)$ | $\operatorname{LGr}(\mathbb C^{2n},J_n)$ | $C_n$ |
| $IV_n$ | $z\in\mathbb C^n,\ 2z^*z<1+|z^{\mathsf t}z|^2,\ z^*z<1$ | $\operatorname{SO}^0(2,n)/(\operatorname{SO}(2)\times\operatorname{SO}(n))$ | $Q^n\subset\mathbb P^{n+1}_{\mathbb C}$ | $D_{n/2+1}$ for even $n$; $B_{(n+1)/2}$ for odd $n$ |

Here $Q^n=\{[z]:\sum_{j=0}^{n+1}z_j^2=0\}$. The correspondence $[x+iy]\mapsto\langle x,y\rangle$ with its ordered orientation gives $Q^n\cong\operatorname{Gr}^{\mathrm{or}}_2(\mathbb R^{n+2})$. Its compact group is $\operatorname{SO}(n+2)$: indeed $g^{\mathsf t}g=g^*g=1$ implies $g=\bar g$.

The Helgason labels are respectively AIII, DIII, CI, and BDI with a signature index two. The exceptional domains $V$ and $VI$ have labels EIII and EVII. Their explicit models use complexified octonionic constructions [@Viv14, §§3.5–3.6]. Low-rank coincidences are listed in [@Viv14, Table 7]; in particular $IV_2$ is a product of discs rather than an irreducible domain.

On each irreducible non-Euclidean symmetric factor, the invariant complex structure compatible with its symmetric metric has two choices, $J$ and $-J$. The corresponding Hermitian metrics have the same Riemannian part and conjugate complex structures. In a product, the sign can be chosen independently on each factor. This is the choice implicit in the classification of Hermitian symmetric manifolds [@Viv14, Theorem 2.16 and Definition 2.15; @Hel01, Chapter VIII, §4].

For $q=1$, $I_{p,1}$ is the unit ball in $\mathbb C^p$. For type IV, the real graph domain in @rmk:hsd-positive-graphs is a real-analytic model of a component. Its real matrix entries are not the holomorphic Harish-Chandra coordinates $z$ in the table.
:::

:::{.remark #rmk:hsd-automorphic-tautological title="Tautological and automorphic bundles"}
For type $I_{p,q}$, write $D\subset\operatorname{Gr}_p(V)$ for the positive $p$-planes in a Hermitian space $V$ of signature $(p,q)$, and let $S\subset V\otimes\mathcal O_D$ and $Q$ be the tautological subbundle and quotient. The graph chart at $F\in D$ gives

\begin{align*}
T_D&\cong\mathcal H om(S,Q)=S^\vee\otimes Q,\\
K_D&\cong(\det S)^{p+q}\otimes(\det V)^{-p}.
\end{align*}

Indeed, a first-order graph is a map $F\to V/F$, and $\det Q\otimes\det S\cong\det V$. Graph coordinates for positive $p$-planes are $q\times p$ matrices; transposition gives the $p\times q$ realization in the table. The line $\det S$ is the tautological automorphic line for this realization. After fixing a volume form on $V$, the canonical bundle is its $(p+q)$th power; for the ball $I_{1,q}$ the exponent is $q+1$, not the dimension $q$. The bounded graph realization and Grassmannian compact dual are those of [@Viv14, §3.1].

The split real orthogonal group $\operatorname O(g,g)$ does not give type $II_g$ by selecting positive maximal complex isotropics: if $z=x+iy$ is complex isotropic and $\beta(z,\bar z)>0$, then $x,y$ span a positive real two-plane, and a positive complex $g$-plane would require a positive real $2g$-plane in signature $(g,g)$. Type $II_g$ has real form $\operatorname{SO}^*(2g)$, as in the table [@Viv14, §3.2].
:::

:::{.definition #def:hsd-tube-type title="Tube domains"}
A *tube domain* is $V+iC\subset V_{\mathbb C}$, where $V$ is a real vector space and $C\subset V$ is an open cone. A bounded symmetric domain is *of tube type* if it is biholomorphic to such a domain.
:::

The irreducible tube types are $I_{n,n}$, $II_{2n}$, $III_n$, $IV_n$ for $n\ne2$, and $VI$ [@Viv14, Corollary 4.45]. The product $IV_2$ is also of tube type. In BDI this is the Hermitian case, where one signature index is two.

## Siegel space and polarized tori {#sec-hsd-siegel}

:::{.definition #def:hsd-siegel title="Siegel upper half-space and disc"}
Set

\begin{align*}
\mathfrak H_n&=\{Z=A+iB:A,B\in\operatorname{Sym}_n(\mathbb R),\ B>0\},\\
\mathfrak D_n&=\{W\in\operatorname{Sym}_n(\mathbb C):I_n-W^*W>0\}
=\{W\in\operatorname{Sym}_n(\mathbb C):\|W\|_{\mathrm{op}}<1\}.
\end{align*}

The Cayley transform $Z\mapsto(Z-iI_n)(Z+iI_n)^{-1}$ identifies them. Both have homogeneous model $\operatorname{Sp}(2n,\mathbb R)/\operatorname U(n)$ [@Viv14, §3.3].
:::

:::{.remark #rmk:hsd-siegel-action title="Symplectic action and the unitary stabilizer"}
For $g=\begin{pmatrix}A&B\\C&D\end{pmatrix}\in\operatorname{Sp}(2n,\mathbb R)$, the action in Siegel coordinates is

\begin{align*}
g\cdot Z&=(AZ+B)(CZ+D)^{-1},&
\operatorname{Im}(g\cdot Z)&=(CZ+D)^{-*}(\operatorname{Im}Z)(CZ+D)^{-1}.
\end{align*}

The second formula shows that the action preserves $\mathfrak H_n$; the symplectic equations show that $g\cdot Z$ is symmetric. The stabilizer of $iI_n$ consists of

\begin{align*}
\left\{\begin{pmatrix}A&B\\-B&A\end{pmatrix}:A+iB\in\operatorname U(n)\right\}\cong\operatorname U(n).
\end{align*}

This also gives $\dim_{\mathbb C}\mathfrak H_n=n(n+1)/2$. The Cayley transform in @def:hsd-siegel is the bounded realization by complex symmetric matrices of operator norm less than one [@BL04, §8.1; @Viv14, §3.3].
:::

:::{.remark #rmk:hsd-siegel-complex-structures title="Compatible complex structures"}
Fix a symplectic space $(V,\omega)$ of real dimension $2n$. Siegel space parametrizes endomorphisms $J$ with

\begin{align*}
J^2&=-1,&\omega(Ju,Jv)&=\omega(u,v),&g_J(u,v)&=\omega(u,Jv)>0\quad(u=v\ne0).
\end{align*}

The symplectic group acts transitively by conjugation: a $g_J$-orthonormal complex basis is a symplectic basis. The stabilizer preserves both $\omega$ and $J$, hence is $\operatorname U(n)$. This gives the quotient above and the positive Hermitian form $h_J=g_J-i\omega$, linear in the first argument: $h_J(Ju,v)=ih_J(u,v)$.

The space $\operatorname{Sp}(2n,\mathbb R)/(\operatorname U(k)\times\operatorname{Sp}(2n-2k,\mathbb R))$ has a related interpretation: a symplectic $2k$-subspace together with a positive compatible complex structure on it. This additional structure accounts for the unitary stabilizer.
:::

:::{.remark #rmk:hsd-ppav title="Marked principally polarized abelian varieties"}
Let $(\Lambda,\omega)$ be an integral unimodular symplectic lattice. A positive compatible complex structure $J$ on $\Lambda_{\mathbb R}$ gives

\begin{align*}
X_J&=(\Lambda_{\mathbb R},J)/\Lambda.
\end{align*}

The integral alternating form $\omega$, with $\omega(Ju,Jv)=\omega(u,v)$ and $\omega(u,Ju)>0$, is a Riemann form, so $X_J$ is projective [@Huy05, Corollary 5.3.5]. It defines a principal polarization: unimodularity makes the induced homomorphism $\Lambda\to\Lambda^\vee$ an isomorphism. Conversely, the marking $\Lambda\xrightarrow{\sim}H_1(X,\mathbb Z)$ of a principally polarized abelian variety is required to preserve its polarization pairing; pulling back its complex structure recovers $J$. These constructions are inverse, so $\mathfrak H_n$ parametrizes the marked isomorphism classes. The form $g_J$ is the associated positive symmetric form; the integral Riemann form is $\omega$. Forgetting the symplectic marking gives $\operatorname{Sp}(2n,\mathbb Z)\backslash\mathfrak H_n$ [@Kon20, Remark 5.7].
:::

:::{.remark #rmk:hsd-polarization-types title="Period matrices for general polarization type"}
For an ample line bundle $L$ on a complex torus $X=\mathbb C^n/\Lambda$, use Hermitian forms linear in the first argument, as in @rmk:hsd-siegel-complex-structures, and set $E_L=-\operatorname{Im}H_L$. Then $E_L(u,Ju)>0$. It has a basis $\lambda_1,\ldots,\lambda_n,\mu_1,\ldots,\mu_n$ in which its matrix is

\begin{align*}
J_D&=\begin{pmatrix}0&D\\-D&0\end{pmatrix},&
D&=\operatorname{diag}(d_1,\ldots,d_n),\qquad 0<d_1\mid\cdots\mid d_n.
\end{align*}

The tuple $(d_1,\ldots,d_n)$ is the polarization type. A basis $\omega_1,\ldots,\omega_n$ of $H^0(X,\Omega_X^1)$ gives the $n\times2n$ period matrix $\Pi_{ij}=\int_{\gamma_j}\omega_i$, where $\gamma_j$ are the homology cycles corresponding to the chosen basis of $\Lambda$. Normalizing the basis of forms gives

\begin{align*}
\Pi&=(D,Z),&Z^{\mathsf t}&=Z,&\operatorname{Im}Z&>0.
\end{align*}

Conversely $Z\in\mathfrak H_n$ gives $X_Z=\mathbb C^n/(D,Z)\mathbb Z^{2n}$ and the positive Hermitian form $H_Z(v,w)=v^{\mathsf t}(\operatorname{Im}Z)^{-1}\bar w$, whose negative imaginary part has matrix $J_D$ on the displayed lattice. Thus $\mathfrak H_n$ parametrizes polarized complex tori of type $D$ with symplectic basis. The integral change-of-basis group is $\Gamma_D=\{M\in\operatorname{GL}(2n,\mathbb Z):M^{\mathsf t}J_DM=J_D\}$; forgetting the basis gives $\Gamma_D\backslash\mathfrak H_n$ with its induced action. For $D=I_n$ this is the principal case of @rmk:hsd-ppav. Birkenhake–Lange use $E_L=\operatorname{Im}H_L$ and order the basis so the period matrix is $(Z,D)$; exchanging the two blocks and using $-\operatorname{Im}H_L$ gives the convention here [@BL04, §4.2 and §8.1, Propositions 8.1.1–8.1.3].
:::

:::{.remark #rmk:hsd-hodge-line title="The Hodge line and the tangent bundle"}
Use the cohomological realization $W=H^1(X,\mathbb R)$ of a marked polarized torus, with its alternating polarization form $Q$. A point of $\mathfrak H_n$ is a weight-one Hodge decomposition

\begin{align*}
W_{\mathbb C}&=F\oplus\bar F,&F&=H^{1,0}(X),&Q_{\mathbb C}(F,F)&=0,&iQ_{\mathbb C}(v,\bar v)&>0\quad(v\in F\setminus0).
\end{align*}

Let $\mathcal F$ be the tautological rank-$n$ Hodge bundle and $\lambda=\det\mathcal F$ [@Huy05, §3.C, Definition 3.C.5 and Proposition 3.C.10]. The polarization identifies $W_{\mathbb C}/F\cong F^\vee$. A tangent vector to the Lagrangian Grassmannian is a map $F\to W_{\mathbb C}/F$ whose induced bilinear form is symmetric. Consequently

\begin{align*}
T_{\mathfrak H_n}&\cong\operatorname{Sym}^2\mathcal F^\vee,&
K_{\mathfrak H_n}&\cong(\det\mathcal F)^{n+1}=\lambda^{n+1}.
\end{align*}

The determinant identity follows by diagonalizing a transition matrix of $\mathcal F$: its eigenvalues $t_i$ act on $\operatorname{Sym}^2\mathcal F$ with product $\prod_{i\leq j}t_it_j=(\prod_i t_i)^{n+1}$. These are equivariant line-bundle identities and descend to a torsion-free arithmetic quotient. The Borel embedding into the complex Lagrangian Grassmannian is described in [@Viv14, §3.3]; the period and Hodge interpretation is [@BL04, §8.1].
:::

## Orthogonal period domains {#sec-hsd-period-domains}

:::{.definition #def:hsd-period-domain title="The type IV period domain"}
Let $L$ be a nondegenerate integral lattice of signature $(2,n)$, with $n\geq1$. Extend its pairing complex-bilinearly and set

\begin{align*}
\Omega_L&=\{[z]\in\mathbb P(L_{\mathbb C}):(z,z)=0,\ (z,\bar z)>0\}
=\Omega_L^+\sqcup\Omega_L^-.
\end{align*}

The superscripts name the two connected components. Choose one, $\Omega_L^+$.
:::

:::{.remark #rmk:hsd-oriented-periods title="Oriented positive planes"}
Write $z=x+iy$. The period conditions say

\begin{align*}
x^2&=y^2>0,&(x,y)&=0.
\end{align*}

Thus $(x,y)$ is an oriented orthogonal basis of a positive plane. Multiplication by $a+ib\ne0$ changes this basis by a matrix of determinant $a^2+b^2>0$. Conversely, an oriented positive plane admits an oriented orthogonal basis of equal length, unique up to rotation and positive rescaling. We obtain

\begin{align*}
\Omega_L&\xrightarrow{\sim}\operatorname{Gr}^{+,\mathrm{or}}_2(L_{\mathbb R}),&
[x+iy]&\longmapsto\langle x,y\rangle,\\
\Omega_L^+&\cong\operatorname{SO}^0(2,n)/(\operatorname{SO}(2)\times\operatorname{SO}(n)).
\end{align*}

Complex conjugation reverses the orientation and exchanges the components. The connected stabilizer contains $\operatorname{SO}(2)\cong\operatorname U(1)$, which supplies the invariant complex structure.
:::

:::{.remark #rmk:hsd-spinor-conventions title="Components and the real spinor norm"}
Use the real spinor norm $\theta(r_v)=\operatorname{sign}(v^2)$ for the reflection
$r_v(x)=x-2(x,v)v/(v,v)$. For signature $(p,q)$, let $\varepsilon_+(g)$ be the character describing whether $g$ preserves the orientation component of maximal positive planes. Then

\begin{align*}
\varepsilon_+(g)&=\det(g)\theta(g).
\end{align*}

Indeed, reflection in a positive vector has $(\det,\theta,\varepsilon_+)=(-1,+1,-1)$, while reflection in a negative vector has $(-1,-1,+1)$. The Cartan–Dieudonné theorem extends the identity to every isometry. Hence

\begin{align*}
\operatorname O^+(p,q)&=\ker(\det\cdot\theta),&
\operatorname{SO}^0(p,q)&=\ker(\det)\cap\ker(\theta)\qquad(p,q>0),\\
\Omega_L^+&\cong\operatorname O^+(2,n)/(\operatorname{SO}(2)\times\operatorname O(n)).
\end{align*}

Some references normalize the spinor norm by $\theta'(r_v)=-\operatorname{sign}(v^2)$; then $\theta'=\det\cdot\theta$, and $\operatorname O^+$ is its kernel. With the first convention, the sheet-preserving group in signature $(1,n)$ satisfies $\theta(g)=\det(g)$. These formulas fix the convention in each description.
:::

:::{.construction #cons:hsd-tube-coordinates title="Tube coordinates for the orthogonal domain"}
Choose real isotropic vectors $e,f$ with $(e,f)=1$, and put $V=\langle e,f\rangle^\perp$, of signature $(1,n-1)$. For $z\in V_{\mathbb C}$ set

\begin{align*}
w(z)&=f+z-\tfrac12(z,z)e.
\end{align*}

Then $(w,w)=0$, $(w,e)=1$, and $(w,\bar w)=2(\operatorname{Im}z,\operatorname{Im}z)$. Every period has nonzero pairing with $e$: otherwise its positive real plane would lie in $e^\perp$, whose quotient by $\mathbb Re$ has only one positive direction. Normalize $(w,e)=1$ and solve the isotropy equation to recover the displayed formula. Thus

\begin{align*}
\Omega_L^+&\cong V+iC^+,\qquad
C^+\text{ a component of }\{y\in V:(y,y)>0\}.
\end{align*}

For $n=1$, this is the ordinary upper half-plane. Rational choices of $e,f$ are available when the rational quadratic space contains a hyperbolic plane.
:::

:::{.example #ex:hsd-conic-half-plane title="The conic and the upper half-plane"}
Take coordinates $(a,b,c)$ with quadratic form $a^2+2bc$, of signature $(2,1)$. The preceding construction becomes

\begin{align*}
\mathbb H&\longrightarrow\{[a:b:c]\in\mathbb P^2_{\mathbb C}:a^2+2bc=0\},&
z&\longmapsto[z:-z^2/2:1].
\end{align*}

The Hermitian square of this representative is $|z|^2-\operatorname{Re}(z^2)=2(\operatorname{Im}z)^2$. Positivity therefore selects the upper and lower half-planes; choose the component $\operatorname{Im}z>0$. Projection from the isotropic point $[0:1:0]$ gives the inverse $[a:b:c]\mapsto a/c$. The denominator cannot vanish at a positive period: the conic equation would then force $a=0$, leaving that isotropic point, whose Hermitian square is zero. Thus the conic, tube, and oriented-plane models agree explicitly.
:::

:::{.remark #rmk:hsd-discriminant-arrangements title="Discriminant arrangements"}
For a lattice $L$ of signature $(2,n)$, put

\begin{align*}
R_{-2}(L)&=\{\delta\in L:(\delta,\delta)=-2\},&
\mathcal H_L&=\bigcup_{\delta\in R_{-2}(L)}\bigl(\delta^\perp\cap\Omega_L^+\bigr).
\end{align*}

This is the root hyperplane arrangement, or *discriminant arrangement*. For polarized K3 surfaces the ample periods form its complement in the appropriate domain; the quasi-polarized periods permit these hyperplanes [@GHS13, §2]. In other period problems the excluded arrangement depends on the moduli problem and its Torelli theorem.

The signatures that occur in the archived examples are as follows [@GHS13, Proposition 3.2 and §5.1]:

| Period problem | Signature of the orthogonal period lattice |
| --- | --- |
| Polarized K3 surfaces | $(2,19)$ |
| K3 surfaces polarized by a lattice of signature $(1,r-1)$ | $(2,20-r)$ |
| Polarized abelian surfaces and their Kummer surfaces | $(2,3)$ |
| Enriques surfaces | $(2,10)$ |
| Polarized generalized Kummer varieties | $(2,4)$ |
| Polarized O'Grady sixfolds | $(2,5)$ |
| Polarized manifolds of K3$^{[m]}$ type, $m\geq2$ | $(2,20)$ |
| Polarized O'Grady tenfolds | $(2,21)$ |

For lattice-polarized K3 surfaces the period lattice is the orthogonal complement of the prescribed polarization lattice in $\Lambda_{\mathrm{K3}}$. For the irreducible symplectic examples, it is the orthogonal complement of a positive polarization class in the Beauville lattice. Removing a positive direction explains the signatures in the table. These domains supply arithmetic period quotients; the actual moduli image and arithmetic group still depend on the marking and polarization data. In particular, the abelian and Kummer moduli problems need not have the same arithmetic quotient [@GHS13, §3.2].
:::

## Arithmetic quotients and boundary components {#sec-hsd-arithmetic-boundary}

:::{.definition #def:hsd-arithmetic-subgroup title="Arithmetic subgroups"}
Let $G$ be a linear algebraic group over $\mathbb Q$ with a fixed faithful rational representation $G\hookrightarrow\operatorname{GL}_m$. Put $G(\mathbb Z)=G(\mathbb Q)\cap\operatorname{GL}_m(\mathbb Z)$. A subgroup $\Gamma\subset G(\mathbb Q)$ is *arithmetic* if it is commensurable with $G(\mathbb Z)$. This condition is independent of the chosen faithful rational representation [@BB66, §1].
:::

:::{.definition #def:hsd-parabolic-subgroup title="Parabolic subgroups"}
For a connected reductive algebraic group $G$ over $\mathbb Q$, a subgroup $P\subset G$ is *parabolic* if $G/P$ is projective. A rational parabolic is one defined over $\mathbb Q$. In $\operatorname{SL}_2$, the stabilizer of a line is parabolic; for the upper-triangular subgroup $B$, the map $gB\mapsto g\langle e_1\rangle$ identifies $\operatorname{SL}_2(\mathbb Q)/B(\mathbb Q)$ with $\mathbb P^1(\mathbb Q)$ [@DS05, §1.5].
:::

Let $\operatorname O(L)^+$ be the subgroup preserving $\Omega_L^+$. For an arithmetic subgroup $\Gamma\subset\operatorname O(L_{\mathbb Q})\cap\operatorname O^+(L_{\mathbb R})$, put

\begin{align*}
F_L(\Gamma)&=\Gamma\backslash\Omega_L^+.
\end{align*}

This is a locally symmetric arithmetic quotient. Baily–Borel theory makes it a quasiprojective variety with a canonical projective compactification [@BB66]. If $\Gamma$ is torsion-free, its properly discontinuous action makes $F_L(\Gamma)$ a complex manifold. In general, finite stabilizers give local analytic models that are finite quotients of a complex ball [@GHS13, §5.1].

::: {.definition #def:hsd-orthogonal-modular-form title="Orthogonal modular form"}
Suppose $n\geq3$, and let $\widetilde\Omega_L^+\subset L\otimes\mathbb C$
be the inverse image of $\Omega_L^+$ under projectivization, with the zero
vector removed. A *modular form of weight $k$ and character $\chi$* for a
finite-index subgroup $\Gamma\subset\operatorname O^+(L)$ is a holomorphic
function $f:\widetilde\Omega_L^+\to\mathbb C$ satisfying
\[
f(tz)=t^{-k}f(z),\qquad f(\gamma z)=\chi(\gamma)f(z)
\quad(t\in\mathbb C^*,\ \gamma\in\Gamma).
\]
Write $M_k(\Gamma,\chi)$ for this vector space. The homogeneity condition is
on the affine cone, not on its projectivization [@GHS13, Definition 6.4].
:::

For $n\geq3$, Koecher's principle supplies holomorphy at the rational
boundary. In lower dimensions that condition must be imposed separately
[@GHS13, §6.1]. With trivial character, multiplication of forms gives the
graded ring
\[
M_\bullet(\Gamma)=\bigoplus_{k\geq0}M_k(\Gamma,1),\qquad
F_L(\Gamma)^{\mathrm{BB}}=\operatorname{Proj}M_\bullet(\Gamma).
\]
The degree-zero term contains the constants. A sufficiently divisible power
of the automorphic line descends to an ample line bundle $\mathcal L$ on the
compactification; passing to the corresponding Veronese subring gives the
same Proj. Its degree-$m$ piece is $H^0(F_L(\Gamma)^{\mathrm{BB}},\mathcal
L^{\otimes m})$. This is the section-ring interpretation of the
Baily–Borel construction [@BB66, §10].

Its rational boundary components are associated with nonzero totally isotropic rational subspaces. Since the real signature is $(2,n)$, these have dimension at most two:

| Rational isotropic subspace | Boundary component before arithmetic quotient | Stratum in the compactification |
| --- | --- | --- |
| Line $I$ | A point | A $0$-cusp |
| Plane $J$ | An upper half-plane | A modular curve, a $1$-cusp |

Strata are indexed by $\Gamma$-orbits of these subspaces. The incidence $I\subset J$ gives a point in the closure of the corresponding curve. Their stabilizers give the rational boundary parabolics; in the usual type IV range $n\geq3$ these are maximal parabolics. This is the boundary correspondence used in @thm:baily-borel-isotropic-boundary.

:::{.remark #rmk:hsd-boundary-components title="Boundary components and rationality"}
In the Harish-Chandra realization $D\subset\mathbb C^N$, a boundary component is an equivalence class in $\overline D$ under chains of holomorphic discs. Its normalizer $N_G(F)$ is a parabolic subgroup of the connected automorphism group $G$, and $F$ is rational relative to a specified $\mathbb Q$-form of $G$ when this normalizer is defined over $\mathbb Q$ [@Viv14, §4.1, Theorem 4.5; @BB66, §3]. The arithmetic group permutes rational boundary components. The Baily–Borel topology on the union of $D$ with these components gives the compactification after taking the $\Gamma$-quotient. The compact dual from the Borel embedding is a different compactification of $D$; its full projective boundary is not the Baily–Borel boundary of $\Gamma\backslash D$.
:::

The other classical Hermitian arithmetic quotients include Siegel modular varieties of type $III_n$ from $\operatorname{Sp}(2n,\mathbb R)$, Hermitian modular varieties of type $I_{n,n}$ from $\operatorname{SU}(n,n)$, and type $II_{2n}$ quotients from $\operatorname{SO}^*(4n)$. The compact duals are respectively $\operatorname{LGr}(\mathbb C^{2n})$, $\operatorname{Gr}_n(\mathbb C^{2n})$, and one component of $\operatorname{OGr}_{2n}(\mathbb C^{4n})$ [@Viv14, §§3.1–3.3]. An arithmetic quotient requires a specified rational form and arithmetic subgroup of its real group. In particular, the type $II_{2n}$ group is the quaternionic skew-Hermitian orthogonal group of @rmk:hsd-quaternionic-orthogonal, not the quaternionic Hermitian group $\operatorname{Sp}(p,q)$.

The Riemannian symmetric space $\operatorname{SL}(n,\mathbb C)/\operatorname{SU}(n)$ of determinant-one positive Hermitian forms is not Hermitian symmetric for $n\geq2$: the center of $\operatorname{SU}(n)$ is finite, whereas the maximal compact subgroup of a noncompact Hermitian symmetric space has a one-dimensional center [@Hel01, Chapter VIII, §4; @Viv14, Theorem 2.12]. Its arithmetic quotients therefore do not acquire the holomorphic boundary-component description just given for bounded symmetric domains.

:::{.example #ex:hsd-k3-boundary title="Polarized K3 surfaces"}
Write $\Lambda_{\mathrm{K3}}=U^3\oplus E_8(-1)^2$, choose a primitive vector $h$ with $h^2=2d>0$, and put

\begin{align*}
L_{2d}&=h^\perp\subset\Lambda_{\mathrm{K3}},&
A_{L_{2d}}&=L_{2d}^\vee/L_{2d},\\
\widetilde{\operatorname O}^+(L_{2d})
&=\ker\bigl(\operatorname O(L_{2d})^+\longrightarrow\operatorname O(A_{L_{2d}})\bigr).
\end{align*}

The lattice $L_{2d}$ has signature $(2,19)$. The polarized K3 period quotient uses this discriminant kernel. For ample polarizations the period domain excludes the hyperplanes $\delta^\perp$ with $\delta\in L_{2d}$ and $\delta^2=-2$; the full quotient also permits the quasi-polarized periods [@GHS13, §2].

For a Kulikov–Persson–Pinkham degeneration, after finite base change to unipotent monodromy, let $N$ be the logarithm of monodromy. Type II has $N\ne0$ and $N^2=0$ and determines an isotropic plane, hence a $1$-cusp. Its elliptic double curve supplies the limiting point of that modular curve. Type III has $N^2\ne0$ and $N^3=0$ and determines an isotropic line, hence a $0$-cusp. Type II central fibers have a chain of components with elliptic double curves; Type III fibers have rational components with dual complex a sphere [@AE23, §§2–3]. The Baily–Borel boundary records limiting periods; it does not classify central fibers up to isomorphism.
:::

:::{.remark #rmk:hsd-toroidal title="Toroidal compactification at a type IV cusp"}
For each $\Gamma$-orbit of rational isotropic lines $I\subset L_{\mathbb Q}$, put $P_I=\operatorname{Stab}(I)$ and let $U(I)$ be its unipotent radical. The quadratic pairing identifies its rational vector group with $(I^\perp/I)\otimes I$. The quotient $I^\perp/I$ has signature $(1,n-1)$, and a choice of component of its positive cone determines a cusp cone $C_I$. A toroidal compactification uses a $\Gamma$-admissible rational polyhedral fan $\Sigma_I$ in the rational closure of $C_I$, with finitely many cone orbits under the cusp stabilizer and compatible choices for equivalent cusps [@Eng23, §2.4, Definition 2.13; @AE23, §5].

Write $U(I)_{\mathbb Z}=\Gamma\cap U(I)(\mathbb Q)$. The tube realization gives an open immersion $D/U(I)_{\mathbb Z}\hookrightarrow U(I)_{\mathbb C}/U(I)_{\mathbb Z}$, and $\Sigma_I$ supplies a torus embedding at this cusp. The cusp charts glue to a compactification $\overline{F_L(\Gamma)}^{\Sigma}$ with a morphism to the Baily–Borel compactification [@Eng23, §2.4, Theorem 2.12 and Definition 2.13; @AE23, §5]. An isotropic boundary ray in $I^\perp/I$ is associated with an isotropic plane containing $I$ and hence with a $1$-cusp; its chart must agree with that curve's boundary chart [@Eng23, §2.4, Remark 2.14].

Each cone $\sigma\in\Sigma_I$ gives a torus orbit in the partial compactification. Orbits for cones meeting the interior of $C_I$ lie over the $0$-cusp of $I$; rational isotropic boundary rays lie over the incident $1$-cusps. The partial charts at $1$-cusps are canonical and need no independent fan. Their gluing is a proper algebraic space over $\mathbb C$ [@Eng23, §2.4; @AMRT10, Chapter III, Theorem 5.2].
:::

:::{.example #ex:hsd-modular-curve title="The modular curve and its cusps"}
For a finite-index subgroup $\Gamma\subset\operatorname{SL}_2(\mathbb Z)$, set $Y(\Gamma)=\Gamma\backslash\mathfrak H_1$. Its rational cusps are the $\Gamma$-orbits of $\mathbb P^1(\mathbb Q)$; adjoining them gives the compact modular curve $X(\Gamma)$ [@DS05, §§1.5, 2.4]. The line stabilizers are the rational parabolic subgroups from @def:hsd-parabolic-subgroup.

For $N\geq1$, let $\Gamma(N)$ be the kernel of reduction $\operatorname{SL}_2(\mathbb Z)\to\operatorname{SL}_2(\mathbb Z/N\mathbb Z)$; let $\Gamma_0(N)$ and $\Gamma_1(N)$ be the inverse images of the upper-triangular and upper-unitriangular subgroups, respectively. Their quotients $Y(N)$, $Y_0(N)$, and $Y_1(N)$ parametrize, over $\mathbb C$, elliptic curves with a symplectic basis $(P,Q)$ of $E[N]$ satisfying $e_N(P,Q)=e^{2\pi i/N}$, a cyclic subgroup of order $N$, and a point of exact order $N$, respectively [@DS05, §1.5, Theorem 1.5.1].

For the full modular group, the graded ring of holomorphic modular forms is $\bigoplus_k M_k(\operatorname{SL}_2(\mathbb Z))=\mathbb C[E_4,E_6]$, with weights $4$ and $6$ [@DS05, Theorem 3.5.2]. The cusp form $\Delta=(E_4^3-E_6^2)/1728$ has weight $12$. The two weight-$12$ sections give $[E_4^3:\Delta]$ on $X(1)$, and $j=E_4^3/\Delta$ is its affine coordinate. Thus $X(1)$ is the coarse projective line obtained from this graded ring; the modular curve carries orbifold stabilizers at elliptic points [@DS05, §§1.1, 2.4, 3.5].

The line-bundle form of this map uses the Hodge line $\lambda_E=H^0(E,\Omega_E^1)$ on the moduli stack of elliptic curves, extended across the cusp by invariant differentials on the generalized elliptic curve. A weight-$k$ modular form is a section of $\lambda^{\otimes k}$: under $\tau\mapsto(a\tau+b)/(c\tau+d)$, the standard differential transforms by $dz\mapsto dz/(c\tau+d)$ while the form transforms by $(c\tau+d)^k$ [@DS05, §§1.1, 1.5]. The bundle $\lambda^{\otimes12}$ descends to the coarse curve $X(1)$, and its complete linear system has basis $E_4^3,\Delta$ by @ex:hsd-modular-curve and [@DS05, Theorem 3.5.2]. Its map $[E_4^3:\Delta]$ identifies $X(1)$ with $\mathbb P^1$.

More generally, suppose a power of the automorphic line descends to a line bundle $\mathcal L$ on the compactified quotient. A basepoint-free space of sections with basis $f_0,\ldots,f_N$ defines

\begin{align*}
\phi_{\mathcal L}:x&\longmapsto[f_0(x):\cdots:f_N(x)].
\end{align*}

A change of local trivialization multiplies all coordinates by the same nonzero scalar, so the projective point is well-defined; basepoint-freeness ensures that the coordinates do not vanish simultaneously. A very ample complete linear system gives a closed embedding. Baily–Borel theory supplies such embeddings from sufficiently high powers of its ample automorphic line [@BB66, §10]. This is the general construction realized by the weight-$12$ pair above.
:::

:::{.remark #rmk:hsd-siegel-boundary title="The Siegel boundary"}
For a unimodular symplectic lattice $\Lambda$ of rank $2g$, the Satake–Baily–Borel compactification of $\mathcal A_g=\operatorname{Sp}(\Lambda)\backslash\mathfrak H_g$ has the set-theoretic stratification

\begin{align*}
\mathcal A_g^*&=\bigsqcup_{r=0}^{g}\mathcal A_{g-r},&
\partial\mathcal A_g^*&=\bigsqcup_{k=0}^{g-1}\mathcal A_k,
\end{align*}

where $\mathcal A_0$ is one point [@Mum64, §2]. Rational boundary components correspond to totally isotropic rational subspaces $I\subset\Lambda_{\mathbb Q}$; for the full symplectic group their orbits are indexed by $r=\dim I$, and the component for $r$ has Siegel degree $g-r$. This places the modular curve $X(1)=\mathcal A_1^*$ at the first nontrivial level of the same boundary pattern.

For $g\geq2$, every finite-index subgroup of $\operatorname{Sp}(\Lambda)$ contains the kernel of reduction modulo some positive integer $N$. Thus every such subgroup is a congruence subgroup [@BMS67, Theorem 14.1].

The domain also has a Lagrangian model. In a symplectic basis with form matrix $J_g$, the point $Z\in\mathfrak H_g$ corresponds to the plane spanned by the columns of $\binom{Z}{I_g}$. It is isotropic, and $-i\omega(w,\bar w)>0$ for every nonzero $w$ in that plane [@Viv14, §3.3]. A maximal isotropic rational $I$ has $r=g$, so its rational boundary component is a point.
:::

:::{.remark #rmk:hsd-siegel-toroidal title="Toroidal compactifications of Siegel modular varieties"}
For an arithmetic subgroup $\Gamma\subset\operatorname{Sp}(\Lambda)$ and each rational isotropic subspace $I\subset\Lambda_{\mathbb Q}$, the center $U(I)$ of the unipotent radical of $\operatorname{Stab}(I)$ is the vector group $\operatorname{Sym}^2 I$. Its cone consists of positive semidefinite tensors whose kernel is rational. A $\Gamma$-admissible system of rational polyhedral fans $\Sigma_I$ subdivides these cones and is compatible under the arithmetic group and inclusions of boundary components [@FC91, Chapter IV; @AMRT10, Chapter III, §§5–7].

The fan gives a torus embedding for $U(I)_{\mathbb C}/U(I)_{\mathbb Z}$, where $U(I)_{\mathbb Z}=\Gamma\cap U(I)(\mathbb Q)$, and a partial compactification of the cusp chart $\mathfrak H_g/U(I)_{\mathbb Z}$. The stabilizer $\Gamma_I=\Gamma\cap\operatorname{Stab}(I)$ acts on this chart through $\Gamma_I/U(I)_{\mathbb Z}$. Gluing the resulting quotients gives a compact Moishezon space with a morphism to $\mathcal A_g^*$. A suitable projective fan yields a projective compactification [@FC91, Chapter IV; @AMRT10, Chapter IV, §2].
:::

:::{.example #ex:hsd-hilbert-modular title="Hilbert modular varieties"}
Let $F$ be a totally real field of degree $d>1$. Its real embeddings give an action of $\operatorname{SL}_2(F)$ on $\mathfrak H_1^d$. For a finite-index subgroup $\Gamma\subset\operatorname{SL}_2(\mathcal O_F)$, the quotient $Y_F(\Gamma)=\Gamma\backslash\mathfrak H_1^d$ is a Hilbert modular variety. Its Baily–Borel compactification adds finitely many point cusps indexed by $\Gamma\backslash\mathbb P^1(F)$ [@BB66, §10; @AMRT10, Chapter I, §5].

Every such $\Gamma$ contains the kernel of reduction $\operatorname{SL}_2(\mathcal O_F)\to\operatorname{SL}_2(\mathcal O_F/\mathfrak a)$ for some nonzero ideal $\mathfrak a\subset\mathcal O_F$. Hence it is a congruence subgroup [@Ser70, §1.2 and Theorem 2].

At each cusp, the additive unipotent group has real vector space $F\otimes_{\mathbb Q}\mathbb R\cong\mathbb R^d$. A $\Gamma$-admissible fan in the cone of totally positive elements determines a toroidal cusp chart. The charts glue to a toroidal compactification with a map to the Baily–Borel compactification; its boundary is a divisor over the finite cusp set [@AMRT10, Chapters I and III].
:::

## The circle action and Shimura data {#sec-hsd-shimura-circle}

For an irreducible Hermitian symmetric domain $D$ and a point $o\in D$, let $H$ be its associated adjoint real algebraic group, so that $H(\mathbb R)^+=\operatorname{Hol}(D)^+$. The symmetry at $o$ belongs to the compact stabilizer $K_o$. More precisely, there is a homomorphism

\begin{align*}
u_o:U(1)&\longrightarrow H(\mathbb R),&u_o(z)(o)&=o,&(du_o(z))_o&=z\,\operatorname{id}_{T_oD}.
\end{align*}

The stabilizer $K_o$ is the centralizer of $u_o(U(1))$ in $H(\mathbb R)^+$, and $D\cong H(\mathbb R)^+/K_o$. The pair $(H,u_o)$ describes the pointed domain. Conjugating $u_o$ by $H(\mathbb R)^+$ moves the base point. This is the group-theoretic passage from a symmetric-space quotient to its complex structure [@Mil05, Theorem 1.9].

To pass from this real pair to a Shimura datum, one requires a reductive group over $\mathbb Q$ and a conjugacy class of homomorphisms from the Deligne torus $\mathbb S=\operatorname{Res}_{\mathbb C/\mathbb R}\mathbb G_m$ satisfying the Shimura axioms. The circle $U(1)$ is a real subgroup of $\mathbb S(\mathbb R)=\mathbb C^\times$. In Milne's normalization the restriction of the Shimura homomorphism acts on $T_oD$ by $z^2$, whereas $u_o(z)$ above acts by $z$. The rational group and the remaining axioms are additional arithmetic data [@Mil05, §§1.5–1.7 and 5].

## Symmetric cones and tube domains {#sec-hsd-jordan-tubes}

The tube-domain description in @def:hsd-tube-type has a more precise algebraic form. A finite-dimensional real *Jordan algebra* is a commutative algebra $(J,\circ)$ satisfying $x^2\circ(x\circ y)=x\circ(x^2\circ y)$. It is *Euclidean* if its trace pairing $\operatorname{tr}(L_{x\circ y})$, where $L_x(y)=x\circ y$, is positive definite. For a unital Euclidean Jordan algebra, the cone

\begin{align*}
C_J&=\{x^2:x\in J\text{ invertible}\}\subset J,
\end{align*}

which is the component of the invertible elements containing the unit, is a homogeneous self-dual cone. Conversely, a symmetric cone together with a base point determines a Euclidean Jordan product. The correspondence respects products and irreducibility [@Viv14, Definition 4.20 and Theorem 4.26]. The associated tube is $J+iC_J\subset J_{\mathbb C}$. This realizes exactly the irreducible Hermitian symmetric domains of tube type [@Viv14, §4.3 and Corollary 4.45].

| Euclidean Jordan algebra $J$ | Cone $C_J$ | Tube-domain family |
| --- | --- | --- |
| $\operatorname{Sym}_n(\mathbb R)$ | Positive definite real symmetric matrices | $III_n$, the Siegel upper half-space |
| $\operatorname{Herm}_n(\mathbb C)$ | Positive definite complex Hermitian matrices | $I_{n,n}$ |
| $\operatorname{Herm}_n(\mathbb H)$ | Positive definite quaternionic Hermitian matrices | $II_{2n}$ |
| $\mathbb R\oplus\mathbb R^{n-1}$, the spin factor | A component of the Lorentz cone | $IV_n$ |
| $\operatorname{Herm}_3(\mathbb O)$, the Albert algebra | Positive elements in the Albert algebra | $VI$, the $E_7$ domain |

In the Siegel case this recovers $\operatorname{Sym}_n(\mathbb R)+i\operatorname{Sym}_n^{>0}(\mathbb R)$ from @def:hsd-siegel. Low-rank isomorphisms can identify rows; the classification is by simple Jordan algebras and their cones [@Viv14, Theorems 4.24 and 4.28].

## Marked Dynkin diagrams {#sec-hsd-marked-diagrams}

A simple root is *cominuscule* if it occurs with coefficient one in the expansion of the highest positive root. Its maximal parabolic has abelian unipotent radical. Marking this root on a Dynkin diagram determines the compact dual as a cominuscule homogeneous variety. Its noncompact dual is the corresponding Hermitian symmetric domain [@Viv14, Definition 2.33, Remark 2.34, and Table 5]. The marked roots are:

| Domain | Complex root diagram | Marked simple root | Compact dual |
| --- | --- | --- | --- |
| $I_{p,q}$ | $A_{p+q-1}$ | $\alpha_p$ (or $\alpha_q$ after reversing the chain) | $\operatorname{Gr}_p(\mathbb C^{p+q})$ |
| $II_n$, $n\geq4$ | $D_n$ | Either fork endpoint, $\alpha_{n-1}$ or $\alpha_n$ | One component of the maximal orthogonal Grassmannian |
| $III_n$, $n\geq2$ | $C_n$ | The long-root endpoint $\alpha_n$ | Lagrangian Grassmannian |
| $IV_{2m-1}$, $m\geq2$ | $B_m$ | The long-root endpoint $\alpha_1$ | Smooth quadric |
| $IV_{2m-2}$, $m\geq4$ | $D_m$ | The endpoint opposite the fork, $\alpha_1$ | Smooth quadric |
| $V$ | $E_6$ | Either of the two exchanged outer nodes, $\alpha_1$ or $\alpha_6$ | The $E_6$ cominuscule variety |
| $VI$ | $E_7$ | Its unique cominuscule node, $\alpha_7$ | The $E_7$ cominuscule variety |

Here the indices use Bourbaki's standard numbering. The diagrams and their marked-node incidence can be read from the following edge lists, with $m\geq2$ for $B_m,C_m$ and $m\geq4$ for $D_m$. A dash joins adjacent nodes; the double bonds have their arrows directed toward the short root.

| Diagram | Numbered edges | Cominuscule nodes |
| --- | --- | --- |
| $A_m$ | $1-2-\cdots-m$ | Every node $1,\ldots,m$ |
| $B_m$ | $1-2-\cdots-(m-1)\Rightarrow m$ | $1$ |
| $C_m$ | $1-2-\cdots-(m-1)\Leftarrow m$ | $m$ |
| $D_m$ | $1-2-\cdots-(m-2)$ with $(m-2)-(m-1)$ and $(m-2)-m$ | $1,m-1,m$ |
| $E_6$ | $1-3-4-5-6$ with $2-4$ | $1,6$ |
| $E_7$ | $1-3-4-5-6-7$ with $2-4$ | $7$ |

The two choices in types $A$ and $E_6$ are exchanged by diagram automorphisms; the two spinor marks in $D_n$ likewise give isomorphic compact duals. The low-rank cases are read through

\begin{align*}
I_{1,1}&\cong II_2\cong III_1\cong IV_1,&
I_{3,1}&\cong II_3,\\
III_2&\cong IV_3,&I_{2,2}&\cong IV_4,&II_4&\cong IV_6.
\end{align*}

These are the coincidences of [@Viv14, Table 7]. The disc uses the single-node diagram $A_1$, and $IV_2$ is a product of two discs.

## Sources

The homogeneous-space lists, Grassmannians, matrix models, and period-domain calculations come from the archived *Hermitian Symmetric Domains* notes formerly at `~/notes/Class_Notes/2024/Dissertation/archive/unused_sections/140_HSD.md` and `~/notes/diss/archive/unused_sections/140_HSD.md`. Their differential-geometric sections are in @sec-calculus-on-schemes. The illustrated notes at `~/notes/diss/old-notes/Ch.1 Basics/Symmetric Spaces/Hermitian symmetric domains.md`, their identical copy under `~/notes/dissertation/`, and `~/notes/diss/GROUND_TRUTH/my_enriques_notes/140_HSD.tex` supply the further period, bundle, arithmetic, and compactification constructions.

- [@Hel01, Chapters IV, VIII and X]: symmetric spaces, classical real forms, and classification.
- [@Viv14, §§2–3 and Corollary 4.45]: Hermitian symmetric domains, compact duals, and tube types.
- [@BB66; @GHS13, §2; @AE23, §§2–3]: arithmetic quotients, K3 periods, and degenerations.
- [@Mil05, §§1 and 5]: the circle action on a pointed Hermitian symmetric domain and the rational Shimura datum. The [revised notes](https://www.jmilne.org/math/xnotes/svi.pdf) retain the section numbering of the published version.
- The illustrated notes point to Tobias Strubel's *Basics on Hermitian Symmetric Spaces* (ETH Zürich diploma thesis, 2006/2007), pages 1 and 27. Their PDF address, `www.aimath.org/WWN/surfacegroups/strubel.pdf`, is no longer available. They also point to [Looijenga's Kyoto lectures](https://webspace.science.uu.nl/~looij101/kyoto2013.pdf), [Laza's Vancouver lectures](https://www.math.stonybrook.edu/~rlaza/vancouver_lect_final.pdf), and [Charlotte Chan's Borcherds notes, page 3](https://web.math.princeton.edu/~charchan/learning/borcherds2.pdf#page=3&zoom=170,67,500).
- The archive also records `EnriquesOne.pdf`, page 556, formerly at `dept.math.lsa.umich.edu/~idolga/EnriquesOne.pdf`, a reference pointer to Cossec–Dolgachev's *Enriques Surfaces I*. The current edition is [@CDL25]; the archived PDF page number is version-specific.
