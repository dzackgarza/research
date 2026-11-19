# research#658 (A15): state of the item, for the orchestrator

At `main@10dc46868b`, and kept current as the reductions sharpen.  The issue's acceptance is: "Done when the question is settled in `writing/`
with a proof, a disproof, or a computation record, and every page that cites the open form is
updated."

## Item by item

| item | state | evidence |
|---|---|---|
| 1a stable-group lifting | MET | `thm:coble-strong-lifting`, `enriques-to-coble-cusp-correspondence.md:231-263` |
| 1b equivalence | MET | `prop:gamma-co-strong-lifting` |
| 1c sign half | MET | `lem:monodromy-is-spinor-positive` |
| 1d group hygiene | MET, narrowly | `conj:gamma-co-stable` open, `rmk:gamma-co-status` says neither inclusion is proved |
| 1e discriminant half | **NOT MET** | reduced to a divisor question, `rmk:gamma-co-nodal-pair-proposal` |
| 1f divisibility-2 image | **NOT MET** | class level proved, orbit count open, `prop:cusp-map-onto-criterion` |
| 2 pages updated | **NOT MET** | they are consistent, but nothing further to update to while 1e is open |

## The four reductions now on the page

0. **1e's gap 2 is sharpened and substantive.**  The members are Coble surfaces by the book's own
   definitions -- a one-node member is a singular Coble quotient (`def:singular-coble`) whose
   resolution is the resolved Coble surface of `def:resolved-coble` -- so what is missing is the
   *moduli* identification: whether the one-node members lie in the open subset of $\bD(N)/\Orth(N)$
   that [@DK13, Prop. 3.2, printed p. 513] gives for the classical ten-node construction.  That
   question is substantive: [@DZ01] states the classical construction gives "some (not all) Coble
   surfaces", so the class is strictly larger (recorded without a printed page, which the conversion
   does not pin).
1. **1e is a divisor question.**  The forward inclusion fails as soon as the parameter space of the
   Coble family meets a Heegner divisor of square $-4$ in $T_\Co$, since the monodromy around one is
   $s_\delta$, which lies in $\Orth^+$ and outside the discriminant kernel
   (`prop:gamma-co-reflective-set(3)`, `rmk:gamma-co-nodal-pair-proposal`).  The converse is not
   claimed: it would need the meridians to generate $\pi_1$ of the parameter space.
2. **1f is an orbit count.**  `prop:cusp-map-onto-criterion`: $\Phi$ is onto the divisibility-2 locus
   iff every nonzero isotropic class of $A_{\ten}$ carries exactly one $\Gamma_\En$-orbit of
   divisibility-2 primitive isotropic vectors.  Proof from `prop:cusp-map-injective`,
   `thm:coble-zero-cusp-count(2)` and `prop:cusp-map-surjective-on-classes`.
3. **The Eichler criterion is unavailable** for both lattices: `prop:tco-no-hyperbolic-plane` and
   `prop:ten-no-second-plane` — each lacks a second hyperbolic plane, so the transitivity tool that
   would give the count does not run.
4. **The classes are settled, the orbits are not**: `prop:cusp-map-surjective-on-classes`, corrected
   this session from an orbit-level to a class-level statement.

## Routes closed, with their records

* transitivity of $\Gamma_\En$ on the primitive isotropic vectors of $\ten$ — false, the lattice is
  2-elementary (`coble_658-ten-transitivity-probe-run.txt`);
* the fibre-singleton route transplanted from $T_\Co$ — does not transfer, $\ten = U + B_0(2)$ is not
  $B(2)$ (`coble_658-1f-blocked-input-2026-11-19.txt`, route b);
* the literature — [@Daw22] states algorithms, not a closed form, and the subgroup-orbit operation is
  unavailable (sage-extensions#286), route c;
* separation by $\det(v^\perp/\langle v\rangle)$ — class-determined, so vacuous, route d;
* a dimension count for the moduli identification — the parameter space is 11-dimensional against a
  9-dimensional moduli, so the period map has fibres and the count decides nothing, route e.

## Claims withdrawn this session, so that they are not re-derived as findings

* a lemma that $\Gamma_\En$ is transitive on primitive isotropic vectors (wrong lattice:
  $T_\En \ne U\oplus E_8(-1)$, that is the Enriques lattice);
* a lemma that a two-node collision in DK13's classical model has vanishing class $e_i\pm e_j\in M_X$
  (the $e_i$ are algebraic on every member, so they are not vanishing classes);
* a reduction of 1f to a class-level statement ($v+2w$ preserves the class but not isotropy);
* `thm:gamma-co-not-stable` itself, which was on main for one commit: the realisation of $s_e$ in
  $\Gamma_\Co$ is not proved, DK13's moduli is the classical ten-node construction, and the derivation
  the record cites is off main.

## Inputs that are missing, all checked

* a printed statement of the two-node Picard--Lefschetz product: absent from all 28 held PDFs, each
  converted and searched in full;
* the Picard--Lefschetz identification itself: `cons:lefschetz-periods` states it as a construction,
  `prop:monodromy-contains-root-reflections` assumes it;
* which Heegner divisors of $T_\Co$ the parameter space meets: neither [@DK13, Prop. 3.2, printed
  p. 513] nor [@DZ01] decides;
* the orbit count for $\ten$: needs machinery the provider lacks (sage-extensions#286).

## What would close the item

One of: the two printed statements in `tmp/sources`; an explicit two-node degeneration with a
$T_\Co$-component in its vanishing class, computed on main; or the orbit operation.  With any of them
the four reductions above say exactly what remains to be done.
