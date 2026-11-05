# The two orbit decompositions at the adopted runtime: what stands today (2026-11-05)

Read-only. Nothing under `/workspace/nucleus/work/home/sage-image/` was written.

This record serves `#689` (**B3**, whether `[1, 255, 272]` are the orbits of the stated
stabilizer) and `#688` (**B2**, whether `[1, 2, 120, 135, 270]` is the `G_Co`
decomposition). Both ask for one computation in the finite quadratic space
`A_{T_Co} = B/2B`; neither is obtained, and this file separates what stands today from
what does not rather than reporting a single verdict for both halves.

## What each question needs, named as an owner call

| issue | object | call | contract |
| --- | --- | --- | --- |
| #689 | `S = Stab_{Orth(q_{T_Co})}(½h̃_Co)`, named on the page as order `94 755 225 600` | `A.orthogonal_group()` then `stabilizer` of the class, then `orbits` on the 528 isotropic classes | returns the finite orthogonal group of the discriminant form and its orbit partition |
| #688 | `G_Co = ρ_{S_En}(Stab_{Orth(S_En)}(h))`, named on the page as order `696 729 600`, index `136` in `S` | `S_En.discriminant_representation()`, images of nine reflections, `A.orthogonal_group().subgroup(images)`, then `orbits` | same |

Every one of them starts with `orthogonal_group()` of a discriminant form, and that call
does not return at this runtime:

```
########## probe 2: the finite orthogonal group of a 4-class discriminant form
A_{U(2)} has 4 classes, 3 of them isotropic
about to ask for O(A_{U(2)})
#W Static module lib/oper1.g has CRC mismatch, ignoring
#W Static module lib/type1.g has CRC mismatch, ignoring
Unhandled SIGSEGV: A segmentation fault occurred.
```

That is `coble_owner_gap-blockers.sh` probe 2 on the four-class form `A_{U(2)}`, the
smallest case there is; the committed `coble_isotropic_orbits.py` — which did materialise
the full group's partition in 29.8 s on 2026-11-04 — now stops as well (probe 4 of the same
file). The cause, the probes that rule out a stale GAP workspace, a wrong GAP root and an
autoloaded package, and the second, independent API-level defect in `O_plus()` and
`spinor_norm()` are recorded in `coble_owner_gap-blockers-20261105.md`. Neither issue can
be settled on this runtime, and no orbit enumeration is implemented here in its place.

## What does stand today

The lattice-level half of both statements is re-verified on today's runtime by re-running
the committed `coble_528_isotropic_classes.py`, unchanged; the transcript is
`coble_528_isotropic_classes-rerun-20261105.txt`:

```
B = <1> + U + E8(-1): rank 11, determinant -1, signature (2, 9)
T_Co = B(2): rank 11, determinant -2048, signature (2, 9), even True
   Gram: <2> + U(2) + E8(-2)   AGREE with prop:tco-as-twist
   two_elementary_invariants: (11, 11, 1)
   type (r, a, delta) = (11, 11, 1)   AGREE with the Coble lattice table and open-problems
A_{T_Co}: 2048 classes, q-fibers {'0': 528, '1': 496, '1/2': 528, '3/2': 496}
   # {q = 0  } =  528   prop:coble-q-fibers says  528   AGREE
   # {q = 1  } =  496   prop:coble-q-fibers says  496   AGREE
   # {q = 1/2} =  528   prop:coble-q-fibers says  528   AGREE
   # {q = 3/2} =  496   prop:coble-q-fibers says  496   AGREE
isotropic classes (q = 0): 528, of which nonzero 527   AGREE
E8(-2): 256 classes, q-fibers {'0': 136, '1': 120}
U(2): 4 classes, q-fibers {'0': 3, '1': 1}
3*136 + 1*120 = 528   AGREE with the proposition's N_0 = 2^9 + 2^4 = 528
```

So the set both decompositions partition is verified: `528` isotropic classes, `527` of
them nonzero, and `1 + 255 + 272 = 528 = 1 + 2 + 120 + 135 + 270`. That is the *statement*
of both partitions and not the partition itself: it fixes the sizes to be accounted for and
says nothing about which class lies in which orbit.

## The checks a recomputation must satisfy

Both are already stated on the page that carries the two lists, and they are what a
recomputation would be tested against rather than against the lists themselves:

- the two lists refine the single orbit of `527` nonzero isotropic classes of
  `thm:coble-isotropic-class-orbits`, and they refine one another in exactly one way, since
  among the subset sums of `2, 120, 135, 270` the value `255` occurs only as `120 + 135`;
- the index `136 = 94 755 225 600 / 696 729 600` fixes the four stabilizer indices
  `136·2/272 = 1`, `136·270/272 = 135`, `136·120/255 = 64`, `136·135/255 = 72`, all
  integral and all at most `136`.

A recomputation that violates either would contradict one of the lists; a recomputation
that reproduces both would settle #689 and #688. Neither has been run at this runtime.

One part of #688 has a status of its own. The order `|G_Co| = |W(E_8)| = 696 729 600` that
`thm:coble-heegner-finite-orbits` (1) asserts was decided at the owner by
`coble_stabilizer_generators.py` at provider pin `c546077d`, which is before 2026-11-05 and
therefore history rather than evidence. It cannot be re-decided here: the run reaches the
nine reflections and then stops, at the same `orthogonal_group()` of probe 2 for the
subgroup order and at the membership test of probe 3 for the stabilizer, and its own
construction of `Gamma_Co` calls `O_plus()`, which is the API-level refusal of
`coble_owner_gap-blockers-20261105.md`. So #688's four orbit lengths are unproved *and* its
already-claimed order is currently unreproduced.

## Handoff

One operation would settle both: the orthogonal group of a finite quadratic module over
`F_2`, as an object whose subgroup, order and orbit partition on a given finite set are
computed from the module, available at order `2^11` and at order `2^10`. The route the
chapter records instead — stabilizing the four fibers of `Q` inside `GL(B/2B)` and then
taking orbits — is the subobject family of a 2048-element form, the route that did not
return in eight minutes in the A2 record, so a `block_preserving_subgroup`-style operation
computed from a declared orthogonal decomposition would serve it better than an enumeration.
