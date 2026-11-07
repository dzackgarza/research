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

Definition 2.6 of [@AEGS25] states further that $\Gamma_{\En,2} = \Gamma_\En\cap\Gamma_{\mathrm{dP}}$, and
Lemma 2.8 (citing Sterk, Remark 2.12) gives the index as the degree of $\fen\to F_{(10,10,0)}$:

$$
[\Gamma_\En : \Gamma_{\En,2}] \;=\; 2^7\cdot 17\cdot 31 \;=\; 67\,456 .
$$

**This number was misread in the previous batch as $27\cdot17\cdot31 = 14229$**, and the misreading
came from this repository's own text extraction of the PDF: `pdftotext` drops the exponent, printing
`27 · 17 · 31`. The published page prints $2^7\cdot17\cdot31$ — read off the page image
(`pdftoppm -r 400 -f 7 -l 7` of `tmp/sources/aegs-2025-...-degree-2.pdf`, page 7, the last line of
the proof of Lemma 2.8). The correction matters, because $2^7\cdot17\cdot31$ is exactly the index
of the computed discriminant image:

$$
\frac{\abs{\Orth(q_{\ten})}}{\abs{G}} \;=\; \frac{46\,998\,591\,897\,600}{696\,729\,600} \;=\; 67\,456 \;=\; 2^7\cdot17\cdot31 .
$$

The index of an infinite arithmetic group and the index of a finite discriminant image are different
kinds of number, and they agree here only through the kernel relation
$[\Gamma_\En:\Gamma_{\En,2}] = [\rho(\Orth(\ten)):\rho(\Gamma_{\En,2})]\cdot[K:K\cap\Gamma_{\En,2}]$,
$K = \ker(\Orth(\ten)\to\Orth(q_{\ten}))$. Since the published index equals the finite index
exactly, $K\subseteq\Gamma_{\En,2}$: the arithmetic group is the full preimage of its discriminant
image, which is what makes the finite walk a statement about $\Gamma_{\En,2}$ at all and not only
about $\rho(\Gamma_{\En,2})$. That is the reconciliation, and it is a confirmation of the group
identification rather than a weakening of it. `@prop:gamma-en-two-gluing`
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

All three strata of totally isotropic subgroups of $A_{\sen}$ are now computed
(`coble_gammaEn2-card-run.txt`):

| stratum: $\dim$ of the image of $\varPi$ in $A$ | finite objects | $G$-orbits | sizes |
|---|---|---|---|
| $0$ (trivial subgroup) | 1 | **1** | $1$ |
| $1$ (isotropic lines) | 527 | **4** | $270, 135, 120, 2$ |
| $2$ (totally singular 2-spaces) | $23715$ | **5** | $9450, 8640, 3780, 1575, 270$ |
| | | $\mathbf{10}$ | |

Against the published **nine** 1-cusps [@AEGS25, §3.3, p. 590]. The sum over the strata is **ten**,
and ten is not nine, so the stratification cannot simply be added up. This is the point at which the
distinction between the two ways a finite count can fail to be an arithmetic count has to be made,
and it is the substance of what remains:

- **a stratum can be non-liftable.** A totally isotropic subgroup $\bar\varPi\subseteq A$ need not
  be the image of a primitive isotropic plane $\varPi\subset\ten$ at all; an object that does not
  lift contributes a finite orbit and no lattice cusp. Nothing computed so far decides liftability
  for the strata above, and the vector side shows it is not automatic: there the $\operatorname{div}$
  value, not the subgroup alone, is the invariant that lifts.
- **a finite class can hide several lattice orbits, or none.** The finite walk counts orbits of
  $G$, and the map from lattice orbits to $G$-orbits is surjective with fibres
  $\Stab_{\Gamma_{\En,2}}(x)$-orbits of the lift. It is a bijection only under two hypotheses:
  (i) every $G$-orbit in the stratum is realized by a lattice object, and (ii) the stabilizer of one
  object in $\Gamma_{\En,2}$ acts transitively on the objects of the stratum over its class
  (Eichler transitivity). The equivariance of $x\mapsto [x/\operatorname{div}(x)]$ gives neither.

For the **vector** side both hypotheses are met, and the file above records the evidence rather than
assuming it: the two $\Orth(\ten)$-orbits are the $\operatorname{div} = 1,2$ classes [@AEGS25, §3.2],
the only invariant available is $\operatorname{div}$ (which is what the map to $A$ sees), and the
index computation above pins $K\subseteq\Gamma_{\En,2}$, so the group acting is the whole preimage
and not a proper subgroup of it. That is why $5$ is used as the vector total and why the same
argument is *not* transferred to the planes.

So the 1-cusp side stays **open**, now with a diagnosis rather than a gap: ten finite strata-orbits
against nine published cusps means at least one of the ten does not lift or does not separate, and
deciding which requires the lattice-level orbit computation for planes — `T_En.cusps(2)` or its
subgroup form — not a larger finite walk.

## The lattice-side owners, and the exact revisions of the one call that fails

These are the existing owners of the missing lattice-side computation; no new operation is requested,
and none of them needs inventing:

| owner (module, operation) | what it would give here |
|---|---|
| `sage_extensions` `PredicateSubgroups.isotropic_orbit_representatives(rank, flag=)` | orbits of a **prescribed** subgroup of $\Orth(L)$ on primitive isotropic flags of the lattice — the vector and plane counts without passing through $A$ |
| `Lattices.cusps(rank)` (→ `Aut().cusps(rank)`) | the full-group cusps, rank 1 and rank 2, with stabilizer generators and transporters |
| `Lattices.tits_building_incidence()` | the line/plane incidence of the $\Orth(L)$ quotient building, i.e. which cusps are incident |
| `discriminant_image` (`lattice_morphisms`, `orthogonal_quotients`, `predicate_subgroups`) | the map whose image the finite walk above really computes |
| `orthogonal_quotients._subgroup_isotropic_orbit_representatives(subgroup, rank, flag=)` | the same for a subgroup, through `OrthogonalCharacterQuotient` splittings |

The subgroup route needs generating *families* for the polarization group and the stable kernel,
which issue #17 owns; the subgroup orbit computation itself is #286's. Until those land, the only
group I can name concretely is the nine-generator image $G$ used above, and the lattice-level
statement ("which finite classes lift, and whether the stabilizer is transitive on a fibre") is not
computable here.

### The one call that was tried, with its exact provenance

`T_En.cusps(1)` was called and raised inside the port's Eichler machinery:

```
  File "/repos/sage-indefinite-port/src/sage_indefinite_port/indefinite/recursive.py", line 154
    source_coordinates = tuple(int(coordinates(label)) for label in source_labels)
TypeError: int() argument must be a string, a bytes-like object or a real number,
           not 'OwnedJoinCategory.element_class'
```

The revisions imported for that call, recorded as required:

- **sage-extensions**: `.scratch/se-provider-15db925b/src`, pin `15db925b0c92e525f769fcbf57135f1391263a9e`;
- **sage-indefinite-port**: `/repos/sage-indefinite-port` inside the adopted rootfs, at
  **`4f0ee50c3ef432681ecdbbd7a5a7f5adb244d83b`** (working tree clean), which is the old image port pin;
  its `pyproject.toml` declares `sage-extensions @ 7b222e86214524a53802350f3cfda9c513707600`, i.e. a
  *different* provider than the one on `PYTHONPATH` above — the pair is mixed and that is part of the
  provenance;
- **Sage**: `11.0.beta5`.

This is the **already tracked** `int(owned element)` failure at the old image port pin, not a new
defect: held main `991b88b095a42a1e3679569ea42328c900c120f6` contains `ab140b7`, which changes both
`int()` sites. Reproducing the call against that held revision is owed before anything is filed as
open, and no port work is authorized. The new published image run already returned $\Orth(T_\Co)$
generators and discriminant surjectivity at that pin.

So the plane side is open for a reason that is now written down in one place: the finite strata do
not add up to the published count, and the liftability/transitivity hypotheses that would make them
add up are lattice-level statements whose owner is the `cusps` / subgroup-orbit chain above, at the
held revision.
