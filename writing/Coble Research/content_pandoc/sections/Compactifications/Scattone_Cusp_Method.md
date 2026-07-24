# Scattone's method for cusp enumeration

::: {.remark title="Orientation"}

The Cusp Correspondence section computes the specific cusp diagrams of the Coble and Enriques moduli spaces $F_\Co$ and $F_\En$.
Here we record the *general* arithmetic machinery underlying those computations, following Scattone [@Sca87]: the boundary components of a Baily--Borel compactification are enumerated by the orbits of primitive isotropic subspaces of a lattice under an arithmetic group, and those orbits are separated by two invariants --- **divisibility** and the image in the **discriminant group** --- via Eichler's criterion and its transvection refinement.
The concrete cusp counts of $F_\Co$, $F_\En$, and the degree-two K3 space $F_2$ are instances of this method; we cross-reference them below rather than recomputing them.
:::

## The cusp--isotropic-subspace correspondence

::: {.remark title="Boundary components of the Baily--Borel compactification"}

Let $F_{2d}$ be the moduli space of $2d$-polarized K3 surfaces, realized as a quotient $D_{L_{2d}}/\Gamma_{2d}$ of a type IV period domain by an arithmetic group $\Gamma_{2d}$ acting on a lattice $L_{2d}$ of signature $(2, 19)$.
Scattone [@Sca87] gives a concrete arithmetic approach to enumerating the $0$-cusps of the Baily--Borel compactification $\overline{F_{2d}}^{\mathrm{BB}}$.

The boundary of $\overline{F_{2d}}^{\mathrm{BB}}$ is stratified by $\Gamma_{2d}$-orbits of primitive isotropic subspaces of $L_{2d}$:

1. the **$0$-cusps** (Type III boundary points) correspond bijectively to $\Gamma_{2d}$-orbits of primitive isotropic *lines* $I\subseteq L_{2d}$;

2. the **$1$-cusps** (Type II boundary curves) correspond bijectively to $\Gamma_{2d}$-orbits of primitive isotropic *planes* (rank-$2$ isotropic sublattices) $J\subseteq L_{2d}$.

Each $0$-cusp records a degeneration of the underlying K3 surfaces, whose limiting Hodge structure is encoded by the lattice $I^{\perp}/I$; likewise each $1$-cusp carries the boundary lattice $J^{\perp}/J$.
Thus the enumeration of boundary components reduces to a purely lattice-theoretic orbit problem for primitive isotropic sublattices of $L_{2d}$.
:::

::: {.remark title="Scattone's 1987 memoir"}

Scattone's 1987 memoir [@Sca87] carries out this classification lattice-theoretically, with essentially no Hodge-theoretic machinery.
Its three technical ingredients are:

- **Discriminant-form analysis**: separating boundary components by their discriminant quadratic forms;

- **Isotropic-sublattice classification**: the bijective correspondence, above, between boundary components and $\Gamma_{2d}$-orbits of primitive isotropic sublattices of the period lattice $L_{2d}$ of signature $(2, 19)$, on which $\Gamma_{2d}$ acts;

- **Arithmetic group theory**: Eichler's criterion together with the properties of the group $\Orth^+(L_{2d})$.

For $d = 1$ the classification uses primitive embeddings into the $24$ Niemeier lattices to distinguish the four types of rank-$17$ boundary lattices; see \cref{rmk:niemeier-enumeration} and \cref{ex:scattone-f2-diagram}.
:::

## Divisibility and the discriminant group

The two invariants that separate isotropic orbits are the divisibility of a primitive vector and its image in the discriminant group.
Recall from the Lattice Theory section that the **divisibility** $\div_L(v)$ of $v\in L$ is the positive generator of the ideal $\beta_L(v, L)\subseteq\ZZ$, and that $v^* \da v/\div_L(v)$.

::: {.proposition ref="prop:divisibility-discriminant"}

Let $L$ be a nondegenerate lattice and $v\in L$ an arbitrary (not necessarily isotropic) vector.
Then $v^* \da v/\div_L(v)\in L\dual$ is primitive in the dual lattice, and its image in the discriminant group $A_L \da L\dual/L$ has order $\div_L(v)$.

In particular $\div_L(v)$ divides $\abs{A_L} = \abs{\disc(L)}$.
:::

::: {.remark}

Consequently the pair
$$
\bigl(\div_L(v),\ [v^*]\in A_L\bigr)
$$
is a well-defined isometry invariant attached to any primitive $v$, refining its length $v^2$.
Eichler's criterion asserts that, in the presence of two hyperbolic summands, these invariants are *complete*.
:::

## Eichler's criterion

::: {.theorem ref="thm:eichler-criterion" title="Eichler's criterion"}

Let $L \xrightarrow{\sim} U^{2}\oplus M$ be an even lattice containing two orthogonal copies of the hyperbolic plane $U$, and let $v, w\in L$ be primitive vectors.
Then $v$ and $w$ lie in the same $\Orth^*(L)$-orbit (where $\Orth^*(L)$ is the stable orthogonal group, acting trivially on $A_L$) if and only if
$$
v^2 = w^2
\qquad\text{and}\qquad
[v^*] = [w^*]\in A_L
.
$$
Equivalently, the $\Orth^*(L)$-orbit of a primitive vector is determined by its length together with the pair $\bigl(\div_L(v),\ v/\div_L(v)\bmod L\bigr)$ in the discriminant group [@Eic74; @Sca87].
:::

::: {.theorem ref="thm:eichler-transvection" title="Scattone's condition for Eichler transvection orbits"}

Let $L$ be an even lattice admitting a splitting $L \xrightarrow{\sim} U^{2}\oplus M$ with $M$ an arbitrary lattice, and fix $k\in\ZZ$.
Write $L[k] \da \ts{ x\in L \mid x^2 = k }$.
Then for $v, w\in L[k]$,
$$
v \sim_{E(L)} w
\iff
[v^*] = [w^*]\in A_L
,
$$
where $E(L)$ is the **Eichler transvection group** and $\sim_{E(L)}$ denotes $E(L)$-equivalence [@Sca87].
:::

::: {.remark}

\Cref{thm:eichler-transvection} is the engine that separates orbits of isotropic vectors: it reduces the orbit question to computing the image $[v^*]$ in the *finite* discriminant group $A_L$.
Since $E(L)\leq\Orth(L)$ is generated by Eichler transvections, the criterion also refines \cref{thm:eichler-criterion} by pinning the equivalence to the transvection subgroup on each fixed length level $L[k]$.
:::

## Orbit classification in $T = U\oplus\overline{T}_\eta$

Sterk's refinement extends the transvection method to isotropic vectors of arbitrary divisibility, and is the form directly applied to the Enriques and Coble transcendental lattices in the Cusp Correspondence section.

::: {.theorem ref="thm:sterk-orbit" title="Orbit classification (Sterk 1991)"}

Fix an even lattice $T$ with a splitting $T = U\oplus\overline{T}_\eta$, where $\overline{T}$ is negative-definite and even.
Let $\eta_1, \eta_2\in T$ be primitive isotropic vectors satisfying

1. $\eta_1^2 = \eta_2^2 = k$,

2. $\div_T(\eta_1) = \div_T(\eta_2) = p > 0$,

3. $\eta_1 \equiv \eta_2 \pmod{pT}$.

Then there exists an isometry $\phi\in\Orth^*(T)$ with $\phi(\eta_1) = \eta_2$ [@Ste91].
:::

::: {.remark}

\Cref{thm:sterk-orbit} generalizes the Eichler transvection method of \cref{thm:eichler-transvection} to classify primitive isotropic vectors by the triple (length, divisibility, residue mod $pT$). In particular it shows that all divisibility-one isotropic vectors of a given length in $T_{\En}$ lie in a single $\Orth^*(T_{\En})$-orbit; this is the statement used to collapse the divisibility-one cusps in the Cusp Correspondence computations.
:::

## Enumeration via Niemeier lattices

::: {.remark ref="rmk:niemeier-enumeration" title="Niemeier embeddings for $d = 1$"}

For the degree-two case $d = 1$, Scattone [@Sca87] realizes the boundary data through the $24$ **Niemeier lattices** --- the even, negative-definite, unimodular lattices of rank $24$ [@CS10]. The reduction expresses the enumeration of the relevant boundary components as a count of orbits of primitive embeddings into each Niemeier lattice, up to the orthogonal group of that lattice, with the orthogonal complement recording the boundary lattice $\overline{T}_J$.

Scattone realizes the Type II boundary data through the $24$ Niemeier lattices as follows: each Type II boundary lattice $\overline{T}_J = J^{\perp}/J$ is an even negative-definite lattice of rank $17$ (for $d = 1$), which by Nikulin's embedding theory [@Nik80] admits a primitive embedding into an even unimodular lattice of rank $24$; the boundary components are enumerated by classifying these embeddings up to the orthogonal group of the Niemeier lattice.
Scattone does *not* embed the hyperbolic plane $U$ into a Niemeier lattice --- impossible, since $U$ is indefinite --- and no even unimodular negative-definite lattice of rank $22$ occurs.
:::

## Example: the cusp diagram of $F_2$

::: {.example ref="ex:scattone-f2-diagram" title="Cusp diagram of $F_2$ (Scattone)"}

For $d = 1$, there is exactly one $\Gamma_2$-orbit of primitive isotropic lines in $T_2$, yielding a unique $0$-cusp (Type III) in $\overline{F_2}^{\mathrm{BB}}$ [@Sca87].

There are exactly four $\Gamma_2$-orbits of primitive isotropic planes in $T_2$, yielding four Type II boundary curves.
The corresponding boundary lattices $\overline{T}_J$ are rank-$17$ negative-definite lattices, distinguished by their root sublattices:
$$
A_1\oplus E_8^{\oplus 2},
\qquad
E_7\oplus D_{10},
\qquad
A_1\oplus D_{16},
\qquad
A_{17}
.
$$
All four Type II curves meet transversely at the unique Type III point.
:::

::: {.remark}

\Cref{ex:scattone-f2-diagram} is the cusp diagram of the *degree-two K3* moduli space $F_2$, and is distinct from the Coble and Enriques cusp diagrams computed in the Cusp Correspondence section: there the transcendental lattice $T_\Co = (11,11,1)_1$ produces a single $0$-cusp incident to a single $1$-cusp via the mirror-move algorithm, with divisibility data $(2,2)$.
We record the $F_2$ numbers here only as the illustrative instance of Scattone's general method and do not reuse them for the Coble computation.
:::

## Type III degenerations: the Friedman--Scattone analysis

::: {.remark title="Friedman--Scattone 1986"}

The geometric counterpart to the arithmetic Type III cusps is the Friedman--Scattone [@FS86] analysis of Type III degenerations of K3 surfaces, carried out through **mixed Hodge structure** theory.
Its ingredients are:

- **Limiting mixed Hodge structures** in the sense of Steenbrink--Schmid;

- **Monodromy weight filtrations** attached to a nilpotent monodromy operator $N$ with $N^3 = 0$ and $N^2\neq 0$ (the Type III condition);

- the **Clemens--Schmid exact sequence** and the **weight spectral sequence**, which for K3 surfaces degenerates integrally at $E_2$.

The resulting classification identifies Type III degenerations with triangulations of $S^2$ subject to combinatorial constraints; the dual complex of the degeneration then determines the lattice-theoretic invariants, giving a precise dictionary between the geometric degenerations and their monodromy representations.
This Hodge-theoretic picture matches, on the boundary of $\overline{F_{2d}}^{\mathrm{BB}}$, the $0$-cusps enumerated arithmetically by the isotropic-line correspondence above.
:::
