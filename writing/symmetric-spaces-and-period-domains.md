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

Surjectivity follows from the positive square root; the displayed compact groups are the stabilizers of $I_n$. Here positivity includes symmetry or Hermitian symmetry.

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

For $q=1$, $I_{p,1}$ is the unit ball in $\mathbb C^p$. For type IV, the real graph domain in @rmk:hsd-positive-graphs is a real-analytic model of a component. Its real matrix entries are not the holomorphic Harish-Chandra coordinates $z$ in the table.
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

## Arithmetic quotients and boundary components {#sec-hsd-arithmetic-boundary}

Let $\operatorname O(L)^+$ be the subgroup preserving $\Omega_L^+$. For an arithmetic subgroup $\Gamma\subset\operatorname O(L_{\mathbb Q})\cap\operatorname O^+(L_{\mathbb R})$, put

\begin{align*}
F_L(\Gamma)&=\Gamma\backslash\Omega_L^+.
\end{align*}

This is a locally symmetric arithmetic quotient. Baily–Borel theory makes it a quasiprojective variety with a canonical projective compactification [@BB66]. Its rational boundary components are associated with nonzero totally isotropic rational subspaces. Since the real signature is $(2,n)$, these have dimension at most two:

| Rational isotropic subspace | Boundary component before arithmetic quotient | Stratum in the compactification |
| --- | --- | --- |
| Line $I$ | A point | A $0$-cusp |
| Plane $J$ | An upper half-plane | A modular curve, a $1$-cusp |

Strata are indexed by $\Gamma$-orbits of these subspaces. The incidence $I\subset J$ gives a point in the closure of the corresponding curve. Their stabilizers give the rational boundary parabolics; in the usual type IV range $n\geq3$ these are maximal parabolics. This is the boundary correspondence used in @thm:baily-borel-isotropic-boundary.

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

## Sources

The homogeneous-space lists, Grassmannians, matrix models, and period-domain calculations come from the archived *Hermitian Symmetric Domains* notes formerly at `~/notes/Class_Notes/2024/Dissertation/archive/unused_sections/140_HSD.md` and `~/notes/diss/archive/unused_sections/140_HSD.md`. Their differential-geometric sections are in @sec-calculus-on-schemes.

- [@Hel01, Chapters IV, VIII and X]: symmetric spaces, classical real forms, and classification.
- [@Viv14, §§2–3 and Corollary 4.45]: Hermitian symmetric domains, compact duals, and tube types.
- [@BB66; @GHS13, §2; @AE23, §§2–3]: arithmetic quotients, K3 periods, and degenerations.
- The archive also records [EnriquesOne.pdf, page 556](https://dept.math.lsa.umich.edu/~idolga/EnriquesOne.pdf#page=556), a reference pointer to Cossec–Dolgachev's *Enriques Surfaces I*. The current edition is [@CDL25]; the archived PDF page number is version-specific.
