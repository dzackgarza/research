# #647, the θ half: the requirement, and why it is withdrawn

**Superseded.** The index this file was written to obtain is now proved on the page, so the
operation it asked the owner for is no longer needed. What follows is kept because the
reasoning that made the operation look necessary is the interesting part, and because a
withdrawn request should be recorded as withdrawn rather than deleted.

## What is now proved

`prop:theta-co-gluing`, `lem:coble-stabilizer-discriminant-nontrivial` and
`prop:theta-co-index` in
`writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md` give

$$
[\Gamma^\theta_\Co : \Gamma_\Co] = \abs{\rho_{S_\Co}(\Stab_{\Orth(S_\Co)}(\tilde h_\Co))}
= \abs{W(E_8)} = 696\,729\,600
,$$

by hand: $C = \langle K\rangle\oplus U\oplus E_8$ and $h = F_1+F_2$ give
$h^{\perp C} = \langle K\rangle\oplus\langle v\rangle\oplus E_8$ with $v = F_1-F_2$; the
restriction $\Stab_{\Orth(C)}(h)\to\Orth(h^{\perp C})$ is an isomorphism because
$A_{h^{\perp C}}\cong\ZZ/2$ has trivial automorphism group; the root system of $h^{\perp C}$ is
$\{\pm v\}\cup\Phi(E_8)$, which pins the factors; and the mod-2 kernel is
$\{\pm1\}_K\times\{\pm\id_{E_8}\}$, of order $4$.

## What the withdrawn request was, and why it was wrong to need it

The request was `centralizer_generators(ambient, involutions, fixed)` — a generating set of
$Z_{\Orth(\Lambda)}(\theta_\Co)\cap\Stab_{\Orth(\Lambda)}(\tilde h_\Co)$ as integral
isometries of $\Lambda$, certified per generator by isometry, commutation and fixity, and in
completeness by an order identity.

It was asked for on the assumption that the θ half needed the analogue of the sentence of
`prop:gamma-en-two-gluing` that identifies the image of `gent` in `Orth(q_{T_En})` with the
γ-transport of an integral stabilizer's image — an identification that on the Heegner side is
a clause of a proposition. It is not needed on the Coble side, and the reason is a single
fact: `ρ_{T_Co}` is **surjective** (`thm:two-elementary-surjectivity`, `T_Co` even, indefinite
and 2-elementary). A class of `Orth(q_{T_Co})` transported from the $S_\Co$ side is therefore
always realised by an integral isometry of $T_\Co$, the pair glues by
`thm:automorphism-lifting-criterion`, and the component condition is fixed by composing with
the extension of $(\id, s_\zeta)$. That is `prop:theta-co-gluing`, and it needs no new owner
operation.

With that in hand the index was a question about one small lattice rather than about a
generating set, and it is answered above.

## The probe that survives this file

```
|A_T| = 2048 |A_S| = 1024
  A_S.is_isometric_to(A_T(-1))     RAISED TypeError: bad operand type for unary -: ...
  A_S.isometry_to(A_T(-1))         RAISED TypeError: bad operand type for unary -: ...
  A_S.is_isometric_to(A_T)         -> False
```

`A_T(-1)` has no expression on a torsion form at this pin, so an anti-isometry has to be
built against a form carrying the negated value module; and `A_{S_En} → A_{T_Co}` is the wrong
pair in any case, since the two sides of the Coble gluing are `A_{S_Co}` and `A_{T_Co}`, both
of order 2048, while `A_{S_En}` has order 1024.
