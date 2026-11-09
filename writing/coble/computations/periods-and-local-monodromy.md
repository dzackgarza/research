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

::: {.definition #def:period-map title="Period matrix and period map"}

Let $\pi \colon \mathcal{X} \to M$ be a smooth projective (or compact Kähler) family of complex $m$-dimensional varieties over a connected complex quasi-projective variety (or complex manifold) $M$.
Fix a reference fiber $X = X_{t_0} = \inverseof{\pi}(t_0)$, and let $\{\Sigma_0, \dots, \Sigma_{k-1}\} \subset H_m(X, \ZZ)/\mathrm{tors}$ be an integral basis of the middle homology modulo torsion, where $k = b_m(X)$ is the middle Betti number.
For each $t \in M$, let $\{\omega_1(t), \dots, \omega_p(t)\}$ be a basis of a holomorphic subbundle of the relative de Rham cohomology, such as $H^{m,0}(X_t) \subset H^m_{\dR}(X_t)$ where $p = h^{m,0}(X)$, varying holomorphically with $t$.

1. **The general period matrix and period map:** The *period matrix* of the fiber $X_t$ with respect to the chosen bases is the $p \times k$ matrix of period integrals
   $$
   \Pi(t) \;\coloneqq\; \begin{pmatrix}
   \ds\int_{\Sigma_0(t)} \omega_1(t) & \cdots & \ds\int_{\Sigma_{k-1}(t)} \omega_1(t) \\
   \vdots & \ddots & \vdots \\
   \ds\int_{\Sigma_0(t)} \omega_p(t) & \cdots & \ds\int_{\Sigma_{k-1}(t)} \omega_p(t)
   \end{pmatrix}
   \;\in\; \Mat_{p \times k}(\CC).
   $$
   Because the basis of holomorphic forms is determined only up to an invertible change of basis in $\GL_p(\CC)$, the $p$-dimensional subspace spanned by the rows of $\Pi(t)$ defines a point in the Grassmannian $\Gr(p, H^m(X, \CC))$, or more precisely in the Griffiths period domain $\mathcal{D} \subset \Gr(p, k)$ cut out by the Riemann–Hodge bilinear relations.
   Modulo the global monodromy group $\Gamma \le \Aut(H_m(X, \ZZ), Q)$, this association defines the *period map* of the family
   $$
   \mathcal{P} \colon M \too \mathcal{D}/\Gamma.
   $$

2. **Specialization to the one-form case ($p = 1$, Calabi–Yau varieties):** When $X$ is a smooth $m$-dimensional Calabi–Yau variety (such as an elliptic curve with $m=1$, a K3 surface with $m=2$, or a Calabi–Yau threefold with $m=3$), the space of holomorphic top forms is one-dimensional: $h^{m,0}(X) = 1$.
   There is therefore a unique (up to scaling) non-vanishing holomorphic $m$-form $\Omega \in H^{m,0}(X)$.
   In this setting, there is exactly one form to integrate ($p = 1$), and the general period matrix specializes to a single row vector of $k = b_m$ period integrals $\omega_0, \dots, \omega_{k-1}$, given by
   $$
   \omega_i \;=\; \int_{\Sigma_i} \Omega \qquad (i = 0, \dots, k-1).
   $$
   Since $\Omega$ is determined up to an arbitrary non-zero constant $\lambda \in \unitsof{\CC}$, the period integrals are determined up to scalar multiplication, and their totality defines a well-defined point $P_X$ in projective space $\PP^{k-1}(\CC)$:
   $$
   P_X \;=\; [\omega_0 : \dots : \omega_{k-1}] \;\in\; \PP^{k-1}.
   $$
   When $X = X_t = \inverseof{\pi}(t)$ varies in a family $\pi \colon \mathcal{X} \to M$, with $\pi$ determining a locally topologically trivial fibration over a complex quasi-projective variety $M$ and $t \in M$, the association $t \mapsto P_{X_t}$ extends to a holomorphic map
   $$
   \omega \colon M \too \PP^{k-1}, \qquad t \longmapsto P_{X_t} = [\omega_0(t) : \dots : \omega_{k-1}(t)],
   $$
   called the *projective period map* of the family.
:::

## The algebraic construction

::: {.construction #cons:pf-from-jacobian title="From the defining polynomial to the local monodromy"}

Let $k$ have characteristic $0$ and let $f\in k[x_0,\dots,x_{n-1},t]$ present a family of affine hypersurfaces over a one-dimensional base with parameter $t$.

1. Form the Jacobian ideal $J = \left(\partial f/\partial x_0,\dots,\partial f/\partial x_{n-1}\right)$ in $k(t)[x_0,\dots,x_{n-1}]$ and a monomial basis $B$ of the Milnor algebra $k(t)[x]/J$.
   Then $\mu = \lvert B\rvert$ is the Milnor number of the generic fiber, the base field being $k(t)$.

2. On the Brieskorn module of $f$, take the Gauss--Manin connection, and apply it to the form
   $$
   P \;=\; (-1)^{n-1}\,\frac{\partial_t f}{t}\Bigl(\Sum_{b\in B} b\Bigr)
   $$
   with cycle vector $e = [1]$.

3. The result is the Picard--Fuchs operator
   $$
   \mathcal L \;=\; \Sum_{i=0}^{\mu} c_i(t)\, D_t^{\,i}
   \;\in\; k[t]\langle D_t\rangle ,
   $$
   of order $\mu$, with each $c_i$ a polynomial in $t$ alone.

4. Compute the indicial polynomial of $\mathcal L$ at $t = 0$.
   Its roots are the exponents $\alpha_1,\dots,\alpha_\mu$.
   Its degree equals $\mu$ exactly when $t = 0$ is a regular singular point, so checking that degree is checking the hypothesis under which the remaining steps are valid.

5. Let $R$ be the Jordan form over $\overline{\QQ}$ of the companion matrix of the monic indicial polynomial, and let $R = R_s + R_n$ be its Jordan decomposition into commuting semisimple and nilpotent parts.

6. The local monodromy at $t = 0$ is
   $$
   T \;=\; \exp(2\pi i R) \;=\; \exp(2\pi i R_s)\,\exp(2\pi i R_n),
   \qquad
   \exp(2\pi i R_s) = \diag\!\left(e^{2\pi i\alpha_j}\right),
   $$
   the second factor a finite sum since $R_n$ is nilpotent.
   This is the multiplicative Jordan decomposition of $T$: the first factor is its semisimple part, the second its unipotent part.
:::

::: {.corollary #cor:pf-unipotent-monodromy title="Unipotency and the log monodromy"}

Let $T$, $R = R_s + R_n$ and $\alpha_1,\dots,\alpha_\mu$ be as in @cons:pf-from-jacobian.

1. $T$ is unipotent if and only if every exponent $\alpha_j$ is an integer.

2. In that case
   $$
   N \;=\; \log T \;=\; 2\pi i\, R_n ,
   $$
   so the nilpotency index of $N$ is the nilpotency index of $R_n$, and the Jordan block sizes of $T$ are those of $R$.

3. The Jordan type of $T$, and hence the nilpotency index of $N$ and the type of @def:kulikov-types, is the same in every basis of the fiber cohomology.
:::

::: {.proof}

For (1), step 6 of @cons:pf-from-jacobian gives $\exp(2\pi i R_s) = \diag(e^{2\pi i\alpha_j})$ as the semisimple part of $T$.
By uniqueness of the multiplicative Jordan decomposition, $T$ is unipotent exactly when its semisimple part is the identity, that is, when $e^{2\pi i\alpha_j} = 1$ for every $j$.

For (2), integral exponents give $\exp(2\pi i R_s) = I$, so $T = \exp(2\pi i R_n)$.
The series $\exp$ and $\log$ are inverse bijections between nilpotent and unipotent matrices, so $\log T = 2\pi i R_n$.
A nonzero scalar multiple of $R_n$ has the nilpotency index and Jordan type of $R_n$.
The matrix $R$ is in Jordan form, so on each Jordan block of $R$ the part $R_s$ is the scalar $\alpha_j$ and $R_n$ is a single nilpotent Jordan block of the same size.
On that block $T - I = 2\pi i R_n\, u$ with $u = \Sum_{k\geq0} (2\pi i R_n)^k/(k+1)!$ invertible and commuting with $R_n$, so $\ker (T-I)^k = \ker R_n^k$ for every $k$, and $T$ has the Jordan block sizes of $R_n$.

For (3), a change of basis conjugates $T$ by an invertible matrix, and conjugates $N = \log T$ by the same matrix.
The Jordan type and the nilpotency index are invariant under conjugation.
:::

## The Legendre specimen

::: {.example #ex:legendre-monodromy title="The Legendre family"}

For $y^2 = x(x-1)(x-t)$, presented in $k[x,y,t]$ with weights $(2,3,1)$ and the weighted degree-reverse-lexicographic order, @cons:pf-from-jacobian returns
$$
\mu = 2,
$$
a Picard--Fuchs operator of order $2$ whose coefficient list begins
$$
-3t+3,\qquad 12t^2+8t-4,\qquad 12t^3-8t^2-4t,
$$
indicial polynomial $-4\alpha^2$ at $t = 0$, hence a double exponent $\alpha = 0$; nilpotent part with Jordan form $\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}$; and
$$
T \;=\; \begin{pmatrix} 1 & 2\pi i \\ 0 & 1\end{pmatrix},
$$
a single Jordan block, so $T$ is unipotent with $N\neq 0$ and $N^2 = 0$.
:::

::: {.proposition #prop:legendre-monodromy-basis-not-integral title="The Legendre monodromy is not written in an integral basis"}

The basis in which @ex:legendre-monodromy writes $T$ is not a $\ZZ$-basis of $H_1(X_t,\ZZ)$ or of $H^1(X_t,\ZZ)$.
The Jordan type of the monodromy in any basis of $H^1(X_t,\CC)$ is one Jordan block of size $2$.
:::

::: {.proof}

The monodromy is induced by parallel transport along a loop in the base, which is a homeomorphism of the fiber.
It therefore preserves $H_1(X_t,\ZZ)\cong\ZZ^2$ and $H^1(X_t,\ZZ)$, and its matrix in a $\ZZ$-basis of either lies in $\GL_2(\ZZ)$.
The matrix $T$ of @ex:legendre-monodromy has the entry $2\pi i\notin\ZZ$.
The second statement is @cor:pf-unipotent-monodromy(3) applied to the single Jordan block of $T$.
:::

## The topological construction

::: {.construction #cons:lefschetz-periods title="Periods from a Lefschetz pencil"}

For a smooth projective hypersurface $X$, an iterated Lefschetz pencil $X\dashrightarrow\PP^1$ has critical values the roots of the discriminant of the pencil.
At each critical value there is a vanishing cycle $\delta_i\in H_{n-1}(X_b)$ in the homology of a nearby fiber, and a thimble $\Delta_i\in H_n(Y,Y_b)$ with $\partial\Delta_i = \delta_i$.
Integrating a basis of rational differential forms over the thimbles gives the period matrix; a homology modification corrects $H_n(Y)$ to $H_n(X)$ across the blow-up.
The monodromy around a critical value is the Picard--Lefschetz twist along the corresponding vanishing cycle, and continuing the periods numerically around each critical value returns the monodromy matrices on $H_{n-1}(X_b)$ in an explicit homology basis.
:::

Related: [Kulikov models and limiting mixed Hodge structures](#sec-kulikov-models), [Open problems and technical gaps](#sec-open-problems), [Toolchain and recipe for a hyperbolic 2-elementary lattice](#sec-computational-toolchain-and-recipe).
