---
unit: method
status: partial
tags:
  - periods
  - monodromy
  - picard-fuchs
  - hodge-theory
  - method
notes: |-
  Provenance: the hypersurface-family monodromy computation note, migrated 2026-08-20 from the lattice-research corpus, together with the two extraction specifications and the method-comparison notes.
---

# Periods, Picard--Fuchs operators, and local monodromy of a one-parameter family


## Periods and the period map

::: {.definition #def:period-map title="Period matrix and period map" defines="period matrix; $\Pi(t)$; period map; $\mathcal P$; $\omega_i$; $P_X$; $\omega$; projective period map"}

Let $\pi\colon\mathcal X\to M$ be a smooth projective family of complex $m$-folds (or a smooth proper Kähler family) over a connected complex manifold $M$ or a connected complex quasi-projective base taken in the analytic topology. Fix a reference fibre $X=X_{t_0}$ and a basis $\Sigma_0,\ldots,\Sigma_{k-1}$ of $H_m(X,\ZZ)/\mathrm{tors}$. Parallel transport along a path from $t_0$ to $t$ gives cycles $\Sigma_i(t)$ on $X_t$. Integration identifies the de Rham class of a closed $m$-form $\Omega$ with the functional
$$
H_m(X_t,\ZZ)/\mathrm{tors}\longrightarrow\CC,\qquad
\Sigma\longmapsto\int_\Sigma\Omega.
$$
Indeed integration on cycles gives the de Rham comparison with singular cohomology, and evaluation on integral homology identifies $H^m(X_t,\CC)$ with this space of functionals. For a morphism $f\colon Y\to X_t$, the comparison respects pullback because $\int_\gamma f^*\Omega=\int_{f_*\gamma}\Omega$.

In a local holomorphic frame $\omega_1(t),\ldots,\omega_p(t)$ of $F^m_t=H^{m,0}(X_t)$, the **period matrix** is
$$
\Pi(t)_{ji}=\int_{\Sigma_i(t)}\omega_j(t).
$$
Its rows are the coordinates of these classes in the cohomology basis dual to the transported cycles. Replacing the frame by $\omega'_j=\sum_l C_{jl}\omega_l$ and the cycles by $\Sigma'_i=\sum_l\Sigma_l B_{li}$ gives $\Pi'=C\Pi B$. Left multiplication preserves the row space. Right multiplication expresses that same subspace in the new coordinates.

Transport on the universal cover $\widetilde M$ therefore gives a holomorphic map to $\Gr(p,H^m(X,\CC))$. For a polarized variation the full Hodge filtration gives the period map $\mathcal P\colon M\to\mathcal D/\Gamma$, where $\mathcal D$ classifies filtrations of the prescribed Hodge numbers satisfying the Hodge--Riemann relations and $\Gamma$ is the monodromy group (@def:transport-and-monodromy). The row space above records its top filtration piece.

When $p=1$, as for a K3 surface, choose a local generator $\Omega_t$ of the Hodge line and put $\omega_i(t)=\int_{\Sigma_i(t)}\Omega_t$. The **projective period map** in a flat marking is
$$
\omega\colon\widetilde M\to\PP(H^m(X,\CC)),\qquad
\tilde t\longmapsto P_{X_t,\tilde t}=[\omega_0(t):\cdots:\omega_{k-1}(t)].
$$
For a marked K3 surface with marking $\varphi\colon H^2(X_t,\ZZ)\isoto\lkt$, this point is the line $\varphi_{\CC}(H^{2,0}(X_t))\subset\lkt\otimes\CC$. Rescaling $\Omega_t$ fixes the point. A deck transformation acts on it by projective monodromy. Over $M$ the Hodge line defines a section of the projectivized cohomology bundle, and the marked period descends to the quotient by $\Gamma$. A global flat marking gives a map to the fixed projective space itself.
:::

## From the family equation to monodromy

::: {.question #qst:monodromy-from-family-equation title="Can one compute monodromy before classifying the singular fibre?"}

Given the equation of a family over a punctured disc, how can its monodromy be an output of the calculation? Which de Rham class supplies the period, how does the Gauss--Manin connection produce its differential equation, and when do the solutions detect the monodromy on the whole cohomology? A classification by singular fibres can check such a computation once it has been made.
:::

::: {.construction #cons:pf-from-jacobian title="The differential equation of a specified class" defines="Picard--Fuchs operator"}

Let $X_t$ be a smooth projective family over an open subset of the complex $t$-line. On its generic fibre take the finite-dimensional space $H=H^m_{\mathrm{dR}}(X_t/\CC(t))$ with Gauss--Manin connection $\nabla_t$. Specify a nonzero class $\omega\in H$. For a smooth projective hypersurface $f_t=0$, primitive classes can be presented as residues of rational forms with poles along $f_t=0$. For such a form $\eta$, the period of $\operatorname{Res}(\eta)$ over a middle-dimensional cycle $\gamma$ is $(2\pi i)^{-1}\int_{\operatorname{Tube}(\gamma)}\eta$, where the tube circles the hypersurface once in the positive normal direction. Reduction of differentiated forms modulo exact forms uses the Jacobian ideal $J=(\partial_{x_i}f_t)_i$ [@Mor92, §3, eq. (6)].

Let $r$ be the first index at which $\omega,\nabla_t\omega,\ldots,\nabla_t^r\omega$ become dependent. Write the first relation as $\sum_{i=0}^r a_i(t)\nabla_t^i\omega=0$, with $a_r=1$. For any flat cycle $\gamma(t)$, differentiation under the period pairing gives
$$
\mathcal L\int_{\gamma(t)}\omega=0,\qquad
\mathcal L=\sum_{i=0}^r a_i(t)D_t^i,\qquad D_t a=aD_t+\partial_t a .
$$
The monic minimal operator for this class is its *Picard--Fuchs operator*. Clearing denominators gives a polynomial-coefficient equation. Its rank is the dimension of the differential submodule generated by $\omega$. To recover the full local system when $r<\dim H$, compute the connection on a basis of $H$, including how it acts between the submodule and its quotient.

Continue a fundamental system of solutions around a positively oriented loop. At a regular singular point, Frobenius expansions do this locally by continuing $t^\alpha$ and $\log t$. The former acquires the factor $e^{2\pi i\alpha}$, and the latter acquires the summand $2\pi i$. Thus the indicial roots give the eigenvalues. The logarithmic terms determine additional entries of the continuation matrix. Identifying an integral lattice in the solution space requires comparison with periods of integral cycles [@Mor92, §1, pp. 3–5].
:::

::: {.construction #cons:integral-monodromy-by-periods title="Monodromy in an integral basis of cycles"}

In the family of @cons:pf-from-jacobian, choose a basis $\omega_1,\ldots,\omega_n$ of the full degree-$m$ de Rham cohomology over $\CC(t)$. Fix a base point $t_0$ and a loop $\ell$ along which these classes are a frame. Transport an integral basis $\gamma_1,\ldots,\gamma_n$ of $H_m(X_{t_0},\ZZ)/\mathrm{tors}$ along $\ell$. Write
$$
\nabla_t\omega_i=\sum_k A_{ik}\omega_k,\qquad
P_{ij}(t)=\int_{\gamma_j(t)}\omega_i(t).
$$
Differentiating gives $P'=AP$, with forms indexing rows and cycles indexing columns [@Mov21, §13.5, Prop. 13.2]. The de Rham comparison in @def:period-map makes $P(t_0)$ invertible. After continuation around $\ell$, the de Rham basis returns to its original value because it is single-valued. The $j$th column of the continued matrix $P^\ell(t_0)$ therefore consists of integrals over the transported cycle $T_\ell\gamma_j$. With the images of basis cycles written in columns, this gives
$$
P^\ell(t_0)=P(t_0)T_\ell,\qquad T_\ell=P(t_0)^{-1}P^\ell(t_0).
$$
This choice of periods determines the integral matrix. An arbitrary fundamental matrix of the same system determines its complex conjugacy class. A single class $\omega$ supplies a frame by successive derivatives precisely when the order of its minimal Picard--Fuchs operator equals $n$. If its order is smaller, its scalar equation describes the periods restricted to the differential submodule it generates.
:::

::: {.question #qst:symbolic-family-monodromy title="What does the period of a single elliptic differential determine?"}

Let $E_t$ be the smooth projective completion of $y^2=x^3-t$ for $t\ne0$. What is the minimal differential equation for the periods of $dx/y$? How can its solutions form a complex line when $H_1(E_t,\ZZ)$ has rank two? What determines the action of a positive loop about $0$ on integral cycles?
:::

::: {.example #ex:elliptic-monodromy-from-equation title="Integral monodromy of the family $y^2=x^3-t$"}

Put $\omega=dx/y$ and $\eta=x\,dx/y$. Differentiation at fixed $x$ gives $\partial_t(1/y)=1/(2y^3)$. Using $2y\,d_xy=3x^2\,dx$ on the fibre gives the exact differentials
$$
(6t\partial_t+1)\omega=-2\,d_x(x/y),\qquad
(6t\partial_t-1)\eta=-2\,d_x(x^2/y).
$$
The classes of $\omega$ and $\eta$ form a basis of $H^1_{\mathrm{dR}}(E_t)$. Indeed, $\omega$ is holomorphic and nowhere zero. The only pole of $\eta$ is a double pole at infinity. Its residue is zero by the residue theorem, so its periods descend to cycles on the complete curve. If $\eta-c\omega$ were exact, its meromorphic primitive would have a single simple pole. It would give a degree-one map $E_t\to\PP^1$, which is impossible. The nonzero holomorphic form $\omega$ itself has no meromorphic primitive, since such a primitive would be holomorphic on the projective curve. This proves independence in the two-dimensional cohomology.

Thus the connection matrix in @cons:integral-monodromy-by-periods is $\frac{1}{6t}\operatorname{diag}(-1,1)$ in this basis. The minimal operator for $\omega$ is $D_t+1/(6t)$. The periods of $\omega$ are constant multiples of $t^{-1/6}$, and those of $\eta$ are constant multiples of $t^{1/6}$. The substitution $t=u^6$, $x=u^2X$, $y=u^3Y$ gives the same exponents geometrically. The curve becomes $Y^2=X^3-1$, and the two forms become $u^{-1}dX/Y$ and $uX\,dX/Y$.[^elliptic-period-implementations]

Fix $t_0\ne0$ and write $\zeta=e^{2\pi i/6}$. Integration of $\omega$ identifies $H_1(E_{t_0},\ZZ)$ with its period lattice $\Lambda\subset\CC$ [@Sil09, VI, Prop. 5.2]. For a cycle with period $p$, continuation of $t^{-1/6}$ around a positive loop gives the period $\zeta^{-1}p$. Thus multiplication by $\zeta^{-1}$ acts on $\Lambda$ as the monodromy. The periods of two basis cycles are independent over $\RR$ even though their period functions are proportional over $\CC$.

Choose a shortest nonzero period $\lambda$. Then $\lambda,\zeta\lambda$ belong to $\Lambda$ and form a positively oriented basis over $\RR$ of $\CC$. They also generate $\Lambda$ over $\ZZ$. Indeed, express any period in this real basis and round each coefficient to the nearest integer. The remainder is a period of length at most $\sqrt{3}\,|\lambda|/2$, so it vanishes by minimality. Since $\zeta^{-1}=1-\zeta$, transport sends the cycle with period $\lambda$ to the cycle with period $\lambda-\zeta\lambda$, and the one with period $\zeta\lambda$ to the one with period $\lambda$. In that ordered integral basis,
$$
T=\begin{pmatrix}1&1\\-1&0\end{pmatrix}.
$$
Its eigenvalues $\zeta^{-1},\zeta$ agree with the continuation factors for the two rows of the period matrix.
:::

[^elliptic-period-implementations]: For the scalar equation, see Lairez's Magma package `periods` [@Lai15, §8] and Koutschan's `HolonomicFunctions`. An annihilating operator can have higher order than the minimal operator derived here. For the connection matrix, Movasati describes `gaussmaninmatrix` in the Singular library `foliation.lib` [@Mov21, §20.3]. Compare the result in the ordered basis $(\omega,\eta)$. Numerical continuation with `ore_algebra` starts from a supplied differential operator. Comparison with integral cycles is a further step.

::: {.corollary #cor:pf-unipotent-monodromy title="Unipotence and the logarithm of monodromy"}

Let $T$ act on the solution space of a regular singular equation at $0$ with indicial roots $\alpha_j$.

1. $T$ is unipotent if and only if every $\alpha_j$ is an integer.
2. If $T$ is unipotent, then $N=\log T=\sum_{k\ge1}(-1)^{k+1}(T-I)^k/k$ is a finite sum.
3. The Jordan type of $T$ and the nilpotency index of $N$, when defined, are invariant under change of basis. For a Kulikov degeneration the test in @def:kulikov-types applies to the action on the full $H^2$.
:::

::: {.proof}
The eigenvalues are $e^{2\pi i\alpha_j}$ by @cons:pf-from-jacobian. They all equal one precisely for integral exponents. Then $T-I$ is nilpotent. The logarithm is a polynomial in $T-I$, so conjugating $T$ conjugates $N$ by the same change of basis.
:::

The equations $y''=0$ and $t(1-t)y''+ty'-y=0$ have the same monic indicial polynomial $s(s-1)$ at zero. The first has solutions $1,t$. The second has solutions $t,1+t\log t$, as substitution shows. Continuation adds $2\pi i\,t$ to its second solution. The same indicial polynomial thus occurs with two different Jordan types.

## The Legendre family

::: {.example #ex:legendre-monodromy title="The logarithm in the periods of the Legendre family"}

Let $y^2=x(x-1)(x-t)$ and $\omega=dx/y$. Differentiating at fixed $x$ gives
$$
\left(t(1-t)D_t^2+(1-2t)D_t-\tfrac14\right)\omega
=\tfrac12\,d_x\!\left(\frac{x(x-1)}{(x-t)y}\right).
$$
Hence the operator on the left annihilates the periods. The classes of $\omega$ and $\nabla_t\omega$ span $H^1$. Indeed $\partial_t\omega=dx/(2(x-t)y)$ has a double pole at the ramification point over $x=t$ and is regular elsewhere. If $\partial_t\omega-c\omega$ were exact on a smooth fibre, a meromorphic primitive would have just one simple pole. It would define a degree-one map from that elliptic curve to $\PP^1$, which is impossible.

At zero the holomorphic solution $y_1$ with $y_1(0)=1$ has coefficients $(n+1)^2a_{n+1}=(n+\tfrac12)^2a_n$. Reduction of order gives a second solution
$$
y_2=y_1\int\frac{dt}{t(1-t)y_1^2}.
$$
The integrand has residue one. Thus $y_2=y_1\log t+h(t)$ for a holomorphic $h$. Continuation fixes $y_1$ and sends $y_2$ to $y_2+2\pi i\,y_1$. In the ordered solution basis $(y_1,y_2)$ its matrix is
$$
T=\begin{pmatrix}1&2\pi i\\0&1\end{pmatrix}.
$$
Here $N\ne0$ and $N^2=0$. The logarithm in the solution exhibits the nonzero entry.
:::

::: {.proposition #prop:legendre-monodromy-basis-not-integral title="The Legendre monodromy is not written in an integral basis"}

The basis (@def:based-module) in which @ex:legendre-monodromy writes $T$ is not a $\ZZ$-basis of $H_1(X_t,\ZZ)$ or of $H^1(X_t,\ZZ)$.
The Jordan type of the monodromy in any basis of $H^1(X_t,\CC)$ is one Jordan block of size $2$.
:::

::: {.proof}

The monodromy is induced by parallel transport (@cons:calculus-transport) along a loop (@def:based-loop) in the base, which is a homeomorphism of the fiber (@def:fiber-cofiber).
It therefore preserves $H_1(X_t,\ZZ)\cong\ZZ^2$ and $H^1(X_t,\ZZ)$, and its matrix in a $\ZZ$-basis of either lies in $\GL_2(\ZZ)$.
The matrix $T$ of @ex:legendre-monodromy has the entry $2\pi i\notin\ZZ$.
The second statement is @cor:pf-unipotent-monodromy(3) applied to the single Jordan block of $T$.
:::

## The topological construction

::: {.construction #cons:lefschetz-periods title="Periods from a Lefschetz pencil" defines="vanishing cycle; $\delta_i$; thimble; $\Delta_i$"}

For a smooth projective hypersurface $X$, an iterated Lefschetz pencil $X\dashrightarrow\PP^1$ has critical values the roots of the discriminant of the pencil.
At each critical value there is a vanishing cycle $\delta_i\in H_{n-1}(X_b)$ in the homology (@def:homology) of a nearby fiber (@def:fiber-cofiber), and a thimble $\Delta_i\in H_n(Y,Y_b)$ with $\partial\Delta_i = \delta_i$.
Integrating a basis (@def:based-module) of rational differential forms over the thimbles gives the period matrix (@def:period-map); a homology modification corrects $H_n(Y)$ to $H_n(X)$ across the blow-up.
The monodromy around a critical value is the Picard--Lefschetz twist (@def:form-twist) along the corresponding vanishing cycle, and continuing the periods numerically around each critical value returns the monodromy matrices on $H_{n-1}(X_b)$ in an explicit homology basis.
:::

Related: [Kulikov models and limiting mixed Hodge structures](#sec-kulikov-models), [Open problems and technical gaps](#sec-open-problems), [Toolchain and recipe for a hyperbolic 2-elementary lattice](#sec-computational-toolchain-and-recipe).
