# The known-family card for $F_{\En,2}$: lattice, group, fibres, and what is missing

This record states the comparison that the stage-1 batch is owed, after the group identification in
`coble_TEn-gammaEn2-orbits.py` was found to be false. The computation is
`coble_gammaEn2-card.py` with transcript `coble_gammaEn2-card-run.txt`; everything below that is not
a quotation is printed there.

## The lattices, kept apart

| lattice | what it is | rank | signature | $|A|$ |
|---|---|---|---|---|---|
| $\lkt = U^3\oplus E_8^2$ | the K3 lattice | 22 | $(3,19)$ | 1 |
| $\sen = U(2)\oplus E_8(2)$ | invariant lattice of the Enriques involution $I_\En$; carries the polarization $h = u_0+w_0$, $h^2 = 4$ | 10 | $(1,9)$ | $2^{10}$ |
| $\ten = U\oplus U(2)\oplus E_8(2)$ | coinvariant, i.e. the **period** lattice: the period domain is $\bD(\ten)$ | 12 | $(2,10)$ | $2^{10}$ |
| $T_{\mathrm{dP}} = U\oplus\Delta^-(U)\oplus E_8^2$ | invariant lattice of the degree-2 K3 involution $I_{\mathrm{dP}}$ | 20 | $(2,18)$ | $2^2$ |

The ranks add up as they must: $10 + 12 = 22$, $\sen$ of signature $(1,9)$ and $\ten$ of signature
$(2,10)$ giving $(3,19)$. (The rank-18 lattices of [@AEGS25, §3.1] are the quotients $e^{\perp}/e$,
not $T_{\mathrm{dP}}$ itself: $T_{\mathrm{dP}}$ has rank 20 and signature $(2,18)$.)
$\lkt$ is the overlattice of $\sen\oplus\ten$ glued along the anti-isometry
$\gamma\colon A_{\sen}\iso A_{\ten}$ with $q_{\ten}\circ\gamma = -q_{\sen}$, of index
$[\lkt:\sen\oplus\ten] = \abs{A_{\sen}} = 2^{10}$ ([@AEGS25, Def. 2.3]; `@cons:embedding-gluing-data`,
`@prop:gamma-en-two-gluing`). The three lattices are **not** interchangeable: $\sen$ is where $h$ and
its stabilizer live, $\ten$ is where the periods and the cusps live, and $T_{\mathrm{dP}}$ enters only
through $\Gamma_{\mathrm{dP}} = \Orth(T_{\mathrm{dP}})$ in the intersection below.

## The group, as the sources define it

$$
\Gamma_{\En,2} \;=\; \im\Bigl(\theset{g\in\Orth(\lkt)\mid g\circ I_\En = I_\En\circ g,\; g(h) = h}\;\too\;\Orth(\ten)\Bigr),
\qquad
\Gamma_\En = \Orth(\ten),\quad \Gamma_{\mathrm{dP}} = \Orth(T_{\mathrm{dP}}),
$$

Definition 2.6 of [@AEGS25] states further that $\Gamma_{\En,2} = \Gamma_\En\cap\Gamma_{\mathrm{dP}}$, with
$[\Gamma_\En : \Gamma_{\En,2}] = 27\cdot 17\cdot 31 = 14229$ by Lemma 2.8 (citing Sterk,
Remark 2.12), that index being the degree of $\fen\to F_{(10,10,0)}$. `@prop:gamma-en-two-gluing`
gives the discriminant description:

$$
\gent = \theset{g_T\in\Orth(\ten)\mid \exists\, g_S\in\Orth(\sen):\ g_S(h) = h \text{ and } \bar g_T\circ\gamma = \gamma\circ\bar g_S},
$$

so the image of $\Gamma_{\En,2}$ in $\Orth(q_{\ten})$ is the $\gamma$-transport of the image of
$\Stab_{\Orth(\sen)}(h)$, and by `@prop:polarization-stabilizer-enriques` that stabilizer is
$\theset{\pm1}\times W(E_8)$ of order $2\cdot 696\,729\,600$ while its discriminant image $G$ has
order $\abs{W(E_8)} = 696\,729\,600$ (`@thm:coble-heegner-finite-orbits`).

### The false identification, withdrawn

The earlier batch took $\Gamma_{\En,2} = \Stab_{\Orth(\ten)}(h)$ and counted the orbits of
$\rho(\Stab(h)) = \Stab_{\Orth(q_{\ten})}([h/2])$. That is wrong twice over:

- $\Stab_{\Orth(\ten)}(h)$ has **infinite** index in $\Orth(\ten)$, since the orbit of $h$ is the
  infinite set of $(-4)$-vectors of divisibility $2$; it cannot be a subgroup of index $14229$;
- the group actually used has order $94\,755\,225\,600 = 136\cdot 696\,729\,600$, i.e. $136$ times
  the correct discriminant image.

The number $2$ that batch obtained is therefore not a $\Gamma_{\En,2}$ count. It is the divisibility
split $\operatorname{div} = 1$ against $\operatorname{div} = 2$, which is the **two** 0-cusps of
$F_{(10,10,0)} = \bD(\ten)/\Gamma_\En$ [@AEGS25, §3.2] — a correct count of a different quotient. The
transcripts are unchanged and carry a correction block; no page in the writing asserted the false
identification (`lattices.md`, the owning page, states the correct one at line 213).

## The fibres, computed for the correct group

A primitive isotropic $v\in\ten$ has $\operatorname{div}(v)\in\{1,2\}$, and those two values are
exactly the two $\Orth(\ten)$-orbits [@AEGS25, §3.2]. The class $[v/\operatorname{div}(v)]\in A_{\ten}$
is isotropic, zero for $\operatorname{div} = 1$ and nonzero for $\operatorname{div} = 2$, and it is
$\Gamma_{\En,2}$-equivariant. So the $\Gamma_{\En,2}$-orbits are the orbits on that finite set,
transported along $\gamma$ to $A_{\sen}$, where $G$ acts:

```
  isotropic classes of A_{S_En}: 528
    G-orbits on them: 5, sizes [270, 135, 120, 2, 1]
    the zero class is its own orbit: True; the nonzero classes give 4 orbits, sizes [270, 135, 120, 2]
```

$$
\#\{\text{0-cusps of } \fen\} \;=\; \underbrace{1}_{\operatorname{div}=1,\ \text{class } 0} \;+\; \underbrace{4}_{\operatorname{div}=2,\ \text{sizes } 2,120,135,270} \;=\; 5,
$$

which is [@AEGS25, §3.3, p. 590]'s five 0-cusps and Sterk's five vectors of Prop. 4.2.3 (p. 16),
now in the fibres of the two $\Gamma_\En$-orbits: **one** over the unimodular one and **four** over
the divisibility-2 one. That split is the answer to what the earlier batch called the missing fibre
data.

## The 1-cusps: computed on one stratum, not closed

A primitive isotropic plane $\varPi\subset\ten$ carries the same kind of datum: the image of
$\varPi$ in $A_{\ten}$ is a totally isotropic subgroup of dimension $0$, $1$ or $2$ according to
$\varPi^{*}/\varPi$. Only the $2$-dimensional stratum is a finite-form datum, and there the count is:

```
  totally singular 2-spaces of A_{S_En}: 23715
    G-orbits on them: 5, sizes [9450, 8640, 3780, 1575, 270]
```

against the published **nine** 1-cusps [@AEGS25, §3.3, p. 590]. The count is therefore **not**
reproduced, and the reason is precise rather than numerical: the strata of dimension $0$ and $1$ are
not orbits on $A$, so no finite-form walk can supply them. This is the part of the obligation that
stays open, and it is open for want of the operations below, not for want of a decision.

## The public operations this needs, stated for filing

1. **`orthogonal_group_intersection(L, M)`** — for a primitive sublattice $M\subset L$ (here
   $\ten\subset T_{\mathrm{dP}}$, resp. the two eigenspaces of $I_\En$ inside $\lkt$), generators of
   $\Orth(M)\cap\Orth(L)$, equivalently of the isometries of $M$ preserving the gluing subgroup
   $(L\cap M^{*})/M\subseteq A_M$. Certificate: each returned generator is an isometry of $M$, its
   induced map on $A_M$ preserves that subgroup, and $\abs{\langle\text{generators}\rangle}$ equals a
   supplied index (here $14229$). Today the image can only be *constructed* because
   `@prop:gamma-en-two-gluing` names it as a $\gamma$-transport; it is not computed as an intersection.
2. **`isotropic_flag_orbits(L, generators, rank, div)`** — orbits of a *prescribed* subgroup of
   $\Orth(L)$ on the primitive isotropic rank-$k$ flags of the lattice $L$, stratified by
   $\operatorname{div}$. The existing orbit operations act on the finite discriminant module, and
   `A.orbits(group=)` additionally builds the full permutation representation of the group on all
   $\abs{A}$ classes, which is what made the previous run hang. Certificate: orbit representatives with
   their $\operatorname{div}$ and the lattice $\varPi^{\perp}/\varPi$ (or $v^{\perp}/\ZZ v$), plus
   transversality $|\Orth(L)| = \sum|\text{orbit}|\cdot|\text{stabilizer}|$ restricted to a stated
   finite quotient.
3. **`isotropic_subobjects_by_image(A, rank)`** — for a finite torsion quadratic module, the
   form-bearing subobjects of rank $k$ grouped by the dimension of their image in $A$ (the strata
   $\dim = 0,1,2$ above), with one representative of each orbit of the acting group and, for each,
   the lattice-level lift. This is what turns the 5 computed here into the 9.

Without (1) the group is only inferable from a proposition; without (2) and (3) the 1-cusp side cannot
be decided, and no count of the Coble side should be accepted before it is.
