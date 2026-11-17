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

A primitive isotropic plane $\varPi\subset\ten$ has an isotropic discriminant subgroup
$D(\varPi)$ of **dimension one or two, never zero**. This is proved by
@prop:ten-plane-classes(1)--(3), not conjectured from the finite orbit counts.
The two full-$\Orth(\ten)$ plane representatives are
$P_1=\generators{e,e'}$, with $D(P_1)=\generators{[e'/2]}$ of order $2$,
and $P_2=\generators{z,e'}$, with $D(P_2)$ of order $4$.
Equivalently, the mod-two pairing of $\ten=U\perp U(2)\perp E_8(2)$ is supported
on the rank-two symplectic space $U/2U$; a totally isotropic rank-two plane
cannot inject into that space, so at least one nonzero primitive parity class
has even pairing with all of $\ten$. The zero discriminant stratum is
therefore **not liftable**, accounting exactly for the difference between the
naive sum of ten finite orbits and the nine arithmetic plane orbits.

The finite calculation in `coble_gammaEn2-card-run.txt` gives:

| $\dim_{\F_2}D(\varPi)$ | Finite objects | $G$-orbits | Sizes | Integral liftability |
|---|---:|---:|---|---|
| $0$ | $1$ | $1$ | $1$ | **None** |
| $1$ | $527$ | $4$ | $270,135,120,2$ | All |
| $2$ | $23715$ | $5$ | $9450,8640,3780,1575,270$ | All |

The nonzero strata are fully realized: by @prop:ten-plane-classes,
$P_1$ and $P_2$ realize one subgroup of each respective dimension; the
full finite orthogonal group is transitive on each such stratum, and the
surjective discriminant representation of $\Orth(\ten)$ transports these
representatives to every subgroup. Crucially, realization does not by itself
prove one lattice orbit per finite $G$-orbit. The **integral fibre theorem**
@thm:enriques-integral-plane-stabilizers(2) proves exactly that for the
full discriminant preimage $\gent=\rho^{-1}(G)$: two primitive planes
are $\gent$-equivalent if and only if their discriminant subgroups are
$G$-equivalent. The complete arithmetic classification is therefore
$4+5=9$ plane orbits, as proved in @thm:enriques-degree-two-arithmetic(2)
and published in [@AEGS25, §3.3] and [@Ste91, §4.3]. This does **not**
assume kernel transitivity merely from finite equivariance; it uses the
proved integral parabolic stabilizer image and the two integral plane
classes.

The remaining acceptance obligation in research#748 and sage-extensions#294
is an **independent execution of the public lattice subgroup operation**
`Gamma_En,2.isotropic_orbit_representatives(2)` and comparison with the
`gamma-en-2` group card and lattice card `029J`. The mathematical
liftability and fibre hypotheses are already proved; a failed or slow public
operation is an implementation/verification gap, not an unresolved
mathematical ambiguity between ten and nine finite strata.

## Current public subgroup execution (17 November 2026)

The current public-library run uses Sage `11.0.beta5`, `sage-extensions` at
`b72a9161f6d7e9c189aa08f7e868268569e59715` and `sage-indefinite-port` at
`22ac412254c7c39468af3528d002f949385569f8` (the current checkout
revisions at the time of the run), rather than the historical mixed-provider
snapshot discussed below. It constructs the actual
`NamedLattices.TEn.Aut().discriminant_preimage(M)` through the public
predicate-subgroup API, with complete character data, where the nine
integral reflection images generate a group of order `696729600` and index
`67456` in the full discriminant orthogonal group. The **executed public
rank-one** operation returned **five** `Gamma_En,2` orbits in `298` seconds,
and the full orthogonal group returned **two**, exactly as proved in
@thm:enriques-degree-two-arithmetic(1).

The **rank-two** public operation entered the ambient `O(L)` plane-row and
`parabolic completeness decision` stages and had not returned a count when
this record was updated. A separate diagnostic invokes the existing
`_DividedClassPlaneOrbitDecomposition` with the **two proved complete
integral ambient representatives** $P_1=\generators{e,e'}$ and
$P_2=\generators{2e+2f+\alpha,e'}$ from @prop:ten-plane-classes(1).
It returned **nine** subgroup orbits in `212` seconds, but materializing
all nine integral representatives failed after the first: the provider's
`plane_of` transport passes integer letters from
`self._section.letters_of(element)` into `_transported`, whose loop expects
`(label, exponent)` pairs, raising `TypeError: cannot unpack non-iterable int
object`. This precise provider defect is recorded on sage-extensions#294.
The precise consumer-format correction was then independently executed as
an **uncommitted runtime-only diagnostic**, without modifying the provider:
`_transported` was given the signed-integer word format returned by
`_FiniteImageWordSection.letters_of` (a positive index selects its integral
generator, a negative index its inverse), while the existing `plane_of`
finite-class verification remained intact. The same exact subgroup orbit
computation returned **nine** orbits, and this time **all nine actual
integral plane representatives were materialized**, each passing the
public `is_primitive()` test. The complete executed transcript is committed as
`computations/reports/coble_gammaEn2-signed-word-probe-run.txt`; the isolated
runtime patch is `.tmp/coble_signed_word_probe.py` (git-ignored), and the
original diagnostic log is `/tmp/coble_signed_word_probe.log`. This confirms the
provider consumer-format defect and its correction, but the correction
is not yet integrated into the provider source or its tests.

The provider source has since been fixed and pushed as
`sage-extensions` commit `ee8ecdaa`. Reexecuting the same exact integral
subgroup decomposition with the **actual fixed provider**, without any
runtime override, returns nine plane orbits in 210 seconds and materializes
all nine primitive integral plane representatives. Its full transcript is
`computations/reports/coble_gammaEn2-subgroup-orbits-run.txt`. This discharges
the provider word-format defect and the independent integral representative
materialization diagnostic, not the separate top-level public rank-two call.

Neither this runtime-only successful diagnostic nor the earlier failed
transport is presented as completion of the separate top-level public
rank-two acceptance. The mathematical nine-orbit theorem and the
required executable public verification remain distinct obligations.

## Completed top-level public line and plane count comparisons

After integrating the integral signed-word transport correction
(`sage-extensions` `ee8ecdaa`) and the mathematically proved Sterk
ambient-plane representatives for the canonical named Enriques lattice
(`sage-extensions` `3ec1120b`), the **actual top-level public**
`Gamma_En,2.isotropic_orbit_representatives(2)` returned **nine** in 397
seconds and `O(T_En).isotropic_orbit_representatives(2)` returned **two**.
The complete executed transcript is
`computations/reports/coble_gammaEn2-public-rank2-run.txt`.
The public rank-one operations had already returned five and two,
respectively. Thus the full published **5/9** polarized and **2/2**
full-orthogonal-group line/plane count comparison is now executed through
public operations, not merely inferred from the finite discriminant action.
The exact card comparison is as follows. The current
`lattice-database/lattices/029J.md` card has
`integral.primitive_orbits.O.constant = 2`; both public full-$O(T_{\En})$
line and plane operations return **2**. The current arithmetic-group card
`lattice-database/arithmetic-groups/gamma-en-2.md` records
`parent_group: o-t-en` and `index_in_orthogonal_group: 67456`;
the public construction uses exactly `T.Aut().discriminant_preimage(M)`
with $|O(q_T)|=46\,998\,591\,897\,600$ and
$|M|=696\,729\,600$, giving the card's index **67456**.
The **five line and nine plane** counts are the cited published
AEGS/Sterk classification, and the current `029J` card does **not** store
separate `gamma-en-2` primitive-orbit values. The public outputs agree
with the published values; no nonexistent card row is claimed to have
been read or certified.

The earlier slow or failed runs below are retained as historical evidence.

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
defect. **Reproduced and cleared**: at the held main
`991b88b095a42a1e3679569ea42328c900c120f6` with the provider its `pyproject` declares,
`sage-extensions cdafca84065405cb810bba047f8a965299b03762`, the same call returns
`T_En.cusps(1) -> 2 records (326 s)` — the two $\Orth(\ten)$-orbits of primitive isotropic vectors,
matching [@AEGS25 §3.2]. The call, its imported revisions and its output are in
`coble_gammaEn2-cusps-lattice.md`; no port work was done. The plane call `T_En.cusps(2)` runs under
the same pair as job `jmw69fxhq`.

The historical finite-stratum mismatch is resolved by @prop:ten-plane-classes and @thm:enriques-integral-plane-stabilizers, as proved above: the zero stratum is not liftable, and the four one-dimensional and five two-dimensional finite orbits lift bijectively to the nine integral plane orbits. The **public subgroup-orbit execution** remains the outstanding independent verification. The old provider/port failure and its revision provenance are retained here as historical evidence, not presented as an unresolved mathematical problem.
