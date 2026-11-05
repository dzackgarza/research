# Owning-library group operations at the adopted runtime: two defects and a run (2026-11-05)

Read-only. The rootfs was mounted and the repository bound into it; nothing under
`/workspace/nucleus/work/home/sage-image/` was written, and `/sage` was not touched.

## Runtime, as adopted

- rootfs `/workspace/nucleus/work/home/sage-image/rootfs`, entered with
  `.scratch/udocker_dir/bin/proot-x86_64 -R <rootfs> -b /proc -b /dev -b /sys -b <repo>:/repo -w /repo`
  — the recipe of `smw0_maintained-gamma_container.sh`, which is the corpus's own;
- `SageMath version 11.0.beta5`;
- the provider is the image's own checkout `/repos/sage-extensions` at
  `7b222e86214524a53802350f3cfda9c513707600`, which is what `import sage_extensions`
  resolves to inside the rootfs;
- GAP is the image's `libgap.so.11` under `/sage/.venv/lib`.

## Defect 1: `libgap` stops the interpreter on any evaluation

`bash computations/reports/coble_owner_gap-blockers.sh` (output in
`coble_owner_gap-blockers-run.txt`) runs four probes, one process each, because a
segfault ends the interpreter. All four stop:

```
########## probe 1: libgap itself, no owning library involved
about to evaluate 1+1 in libgap
#W Static module lib/oper1.g has CRC mismatch, ignoring
#W Static module lib/type1.g has CRC mismatch, ignoring
Unhandled SIGSEGV: A segmentation fault occurred.
```

```
########## probe 2: the finite orthogonal group of a 4-class discriminant form
A_{U(2)} has 4 classes, 3 of them isotropic
about to ask for O(A_{U(2)})
#W Static module lib/oper1.g has CRC mismatch, ignoring
#W Static module lib/type1.g has CRC mismatch, ignoring
Unhandled SIGSEGV: A segmentation fault occurred.
```

```
########## probe 3: membership in ker(rho_T), the matrix #646 turns on
reflection built; asking whether it lies in ker(rho_T)
#W Static module lib/oper1.g has CRC mismatch, ignoring
#W Static module lib/type1.g has CRC mismatch, ignoring
Unhandled SIGSEGV: A segmentation fault occurred.
```

```
########## probe 4: the committed record coble_isotropic_orbits.py, green on 2026-11-04
#W Static module lib/oper1.g has CRC mismatch, ignoring
#W Static module lib/type1.g has CRC mismatch, ignoring
Unhandled SIGSEGV: A segmentation fault occurred.
```

Probe 4 is the decisive one for provenance: it is a committed, previously green record,
and it now stops before printing a line. Probe 1 involves no owning-library code at all.

What was ruled out, so that the report names the cause and not a guess:

| hypothesis | check | outcome |
| --- | --- | --- |
| a stale GAP workspace cached under `~/.sage/gap` | `DOT_SAGE=/repo/.scratch/a3/dotsage`, empty directory | same crash; a fresh workspace does not help |
| a wrong GAP root on the search path | `GAP_ROOT_PATH=/sage/.venv/share/gap` and `=/usr/share/gap` | same crash under both |
| a broken user package autoloaded from `/root/.gap/pkg` | bound an empty directory over `/root` | same crash |
| the provider pin | probe 1 does not import the provider | crash is independent of the provider |

The named modules are the ones GAP's own kernel has compiled in:
`strings /sage/.venv/lib/libgap.so.11` contains `GAPROOT/lib/oper1.g` with its compiled
functions, so the message is the kernel refusing a library module whose checksum does not
match what it was built against. `lib/oper1.g` and `lib/type1.g` in
`/sage/.venv/share/gap/lib` carry the same mtime as `libgap.so.11` itself
(2026-11-04 16:25:57), so the skew is inside the image and is not something a caller can
repair. Repair belongs to the image, not to this repository.

## Defect 2: `O_plus()` and `spinor_norm()` refuse every lattice over `ZZ`

Independent of GAP, and reproducible on the provider's own minimal example:

```
Lattices(ZZ)("U").O_plus()
  AssertionError: O^+(Integral lattice of rank 2 and signature (1, 1)) is the kernel of
  the real spinor norm at the real place of Frac(R); QQ has exactly one, but
  Frac(R) = Fraction Field of Integer Ring: pass a real embedding of it to spinor_kernel
Lattices(ZZ)("U").spinor_norm()
  AssertionError: the spinor norm of ... is computed here over represented absolute
  number fields, but Frac(R) = Fraction Field of Integer Ring
```

Both hold with the provider's `ZZ` as well as with Sage's, and both hold for `T_Co`. The
provider's own suite asserts the opposite — `tests/lattices/test_definite.sage:321`
(`o_plus = lattice.O_plus()`), `tests/lattices/test_definite.sage:315`
(`lattice.spinor_norm(QQ.Mor(RR)(...))`) and
`tests/lattices/test_orthogonal_reduction_sequences.sage:130-134` — so these are
regressions at this pin and not contracts research is being held to.

## What this leaves available, and what it does not

Available, and used by `coble_gamma_co_reflective_set.py`: building a lattice from its
Gram data; `signature_pair`, `determinant`, `is_even`, `two_elementary_invariants`;
`possible_root_lengths`; `reflective_root_locus` as an object and as a membership test;
`Aut()`, `O_plus`, `stable_orthogonal_group` and their `intersection` **as objects**;
`reflection` and the action of an isometry on a vector; `determinant` of an isometry.

Not available: the real spinor norm and hence `O^+(T_Co)` as a membership test; the
discriminant action of an isometry and hence `ker(rho_{T_Co})` as a membership test;
`roots`, `roots_of_square`, `root_sublattice` for an indefinite lattice (definite-only by
contract); the orthogonal group of any discriminant form, finite or not; orbit partitions;
and any operation returning generators of, or a finite-index certificate for, a subgroup
of `O(L)` of an indefinite `Z`-lattice.

Consequently the three units that need those operations cannot be settled on this
runtime, and this repository does not substitute a locally implemented group algorithm,
orbit enumeration or subobject enumeration for them:

- #646 needs the discriminant action of an isometry (to decide `s in Gamma_Co`) and,
  for the generation half, generators or a finite-index certificate for
  `O^+(T_Co) cap ker(rho_{T_Co})`;
- #689 and #688 need the orbit partition of the 528 isotropic classes under a prescribed
  finite subgroup of `O(A, q)`, which is `orthogonal_group().subgroup(...).orbits(...)`
  and is refused at the first step, `orthogonal_group()` (probe 2).

The two semantic handoffs of `coble_stabilizer_generators.py` are unaffected in substance
and are restated with the evidence: an operation returning generators, or a finite-index
certificate, for the intersection of predicate subgroups of `O(L)` of a `Z`-lattice; and
one returning the subgroup of `O(A)` preserving a given orthogonal decomposition of a
finite torsion form, computed from the decomposition rather than from the subobject
family.
