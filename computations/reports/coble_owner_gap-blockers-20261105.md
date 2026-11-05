# The owning library's decision layer at the adopted runtime (2026-11-05)

Read-only. Nothing under `/workspace/nucleus/work/home/sage-image/` was written and `/sage`
was not touched.

This file has been corrected once, and the correction is the first thing in it because it
changes what may be filed where.

## Withdrawal: the `O_plus()` / `spinor_norm()` refusal was mine, not the provider's

An earlier version of this file reported that `Lattices(ZZ)("U").O_plus()` and
`.spinor_norm()` refuse at the adopted runtime, and called that a provider regression at the
image's pin `7b222e86`. **That report was wrong, and it is withdrawn.** The two calls refuse
only when the *image's own* checkout `/repos/sage-extensions` (pin
`7b222e86214524a53802350f3cfda9c513707600`) is the provider on `PYTHONPATH`. At the snapshot
the corpus's computations actually run at — `sage-extensions`
`6ad7a5ea396da6e758ee28f3dea10a35baee0266`, and likewise at `c546077d` — both calls return
objects on this same runtime, in this same interpreter, under `env -i`:

```
### provider source: /repo/.scratch/se-provider-6ad7a5ea/src
  O_plus()       -> OwnedJoinCategory.parent_class
  spinor_norm()  -> OwnedGroupMor_with_category_with_category.ArrowType
### provider source: /repo/.scratch/se-provider-c546/src
  O_plus()       -> OwnedJoinCategory.parent_class
  spinor_norm()  -> OwnedGroupMor_with_category_with_category.ArrowType
```

and for `T_Co` itself:

```
T_Co: (2, 9) -2048
  T.O_plus()                     -> PreimageSubgroups.parent_class
  T.spinor_norm()                -> OwnedGroupMor_with_category_with_category.ArrowType
  T.stable_orthogonal_group()    -> PreimageSubgroups.parent_class
```

So `Gamma_Co`'s two halves are both constructible at the declared pin, and the sentence
"this is why `Gamma_Co` cannot be built as an owned object" is false. The mistake is mine
and it has a source: `computations/reports/deployed-runtime-readiness-20261104.md` states
that the provider the research runs is the `6ad7a5ea` snapshot and *not* the rootfs's own
`/repos/sage-extensions` at `7b222e8`, and my probes imported the image checkout instead.
`coble_gamma_co_reflective_set.py` now sets the snapshot on `PYTHONPATH` and its transcript
prints it as provenance.

The image's `7b222e86` checkout refuses those two calls because it treats `Frac(Z)` as
"not a represented absolute number field"; that is a fact about that stale checkout and is
not filed as a regression here.

## The two failure modes that remain, at the declared pin

`bash computations/reports/coble_owner_gap-blockers.sh` with
`PYTHONPATH=/repo/.scratch/se-provider-6ad7a5ea/src`, transcript
`coble_owner_gap-blockers-run.txt`, four probes, one process each:

**GAP stops the interpreter (probes 1, 2, 4).**

```
provenance
  PYTHONPATH=/repo/.scratch/se-provider-6ad7a5ea/src
  rootfs .../sage-image/rootfs, /sage/.venv/bin/sage, Sage 11.0.beta5

########## probe 1: libgap itself, no owning library involved
about to evaluate 1+1 in libgap
#W Static module lib/oper1.g has CRC mismatch, ignoring
#W Static module lib/type1.g has CRC mismatch, ignoring
Unhandled SIGSEGV: A segmentation fault occurred.

########## probe 2: the finite orthogonal group of a 4-class discriminant form
A_{U(2)} has 4 classes, 3 of them isotropic
about to ask for O(A_{U(2)})
[... the same two warnings, then] Unhandled SIGSEGV

########## probe 4: the committed record coble_isotropic_orbits.py, green on 2026-11-04
[... the same two warnings, then] Unhandled SIGSEGV
```

**The provider raises before GAP is reached (probe 3).**

```
########## probe 3: membership in ker(rho_T), the matrix #646 turns on
reflection built; asking whether it lies in ker(rho_T)
[...]
  File ".../categories/modules/framed/formed/torsion_form_modules.py", line 315, in _torsion_form_isometry
    return category.Iso(source, target)(formed_forward, formed_inverse, check=check)
  File ".../categories/abstract_categories/mor_foundation.py", line 61, in __call__
    return self._element_constructor_(*args, **kwargs)
TypeError: TorsionFormOrthogonalGroup._element_constructor_() got an unexpected keyword argument 'check'
```

That `TypeError` is a precise, fileable defect at the declared pin: an internal caller passes
`check=` to a constructor that does not accept it, so deciding membership in
`ker(rho_{T_Co})` for a named isometry — the decision #646's generation half turns on, and
the one the corpus's own `coble_stabilizer_generators.py` made at pin `c546` — fails before
it can be made. What is needed is either the constructor accepting `check` or the caller
dropping it; both are inside the library.

## Where the GAP fault sits, and when it arrived

- GAP initializes and reaches `READ_GAP_ROOT`, so it finds a root and reads library text; it
  is not failing to locate GAP.
- The root that a `kernel_info()` check names, `/sage/.venv/lib/gap/`, contains `pkg` and
  `sysinfo.gap` and **no `lib/` tree**, so `lib/oper1.g` cannot come from there.
- The tree it does read is `/sage/.venv/share/gap/lib`, and `sysinfo.gap` declares
  `GAP_VERSION="4.16.1"`, `GAP_BUILD_VERSION="4.16.1"`,
  `GAParch=x86_64-pc-linux-gnu-default64-kv11`, matching the `11` in `libgap.so.11`.
- `lib/oper1.g` is 41070 bytes and `lib/type1.g` 27322 there, against 39545 and 26872 in the
  rootfs's distro GAP at `/usr/share/gap`, a third and different tree.
- All 515 files of `share/gap/lib` carry one mtime, `2026-11-04 16:25:57`, the same mtime as
  `libgap.so.11` itself, so the pair came out of one extraction.
- `proot` is excluded: `md5sum` of both files is identical inside the proot view and on the
  host, so the bytes GAP reads are the bytes on disk.
- The shell environment is excluded: the same stop happens under `env -i HOME=/root`, and
  `env | grep -iE 'GAP|SAGE'` is empty in this shell; the repository's `.envrc` defaults
  `SAGE_BIN` to `$HOME/.local/bin/sage`, which does not exist, so it selects nothing.

**Dated.** Every green GAP-dependent record in this repository predates that mtime — the
commits touching them are `2026-11-01 09:32` (`coble_isotropic_orbits-run.txt`),
`2026-11-01 18:52` (`coble_stabilizer_generators-run.txt`) and `2026-11-03 20:28`
(`smw0_maintained-gamma_compute-container-run.txt`) — and every attempt after it stops. So
the rootfs's GAP library tree was rewritten on 2026-11-04 at 16:25:57, after the last green
run, and the kernel's compiled checksums no longer match it. What I can state is the
measurement and that date; whether the right repair is to restore a matching `lib/` tree,
to place one at `/sage/.venv/lib/gap/lib`, or to run this rootfs the way the other
workspaces run it, is for the runtime owner.

## Ruled out, each by a run

| hypothesis | check | outcome |
| --- | --- | --- |
| a stale GAP workspace under `~/.sage/gap` | empty `DOT_SAGE` | same stop |
| a wrong GAP root on the search path | `GAP_ROOT_PATH` at the venv and at the distro tree | same stop under both |
| a user package autoloaded from `/root/.gap/pkg` | an empty directory bound over `/root` | same stop |
| this shell's environment | `env -i HOME=/root` | same stop |
| the repository `.envrc` | its `SAGE_BIN` default does not exist; no `SAGE_*`/`GAP_*` set | nothing selected |
| the provider snapshot | probes 1, 2, 4 run with `6ad7a5ea` on `PYTHONPATH` | same stop |
| `proot` corrupting the file reads | `md5sum` inside and outside | identical |
| a third Sage or GAP installation on this VM | `find / -xdev -name 'libgap.so*'` outside the rootfs | only `/opt/math`'s two files, and that Sage cannot even import `libgap` (`ImportError: cannot import name GAPError`) |

## What is available, and what is not

Available at the declared pin, and used by `coble_gamma_co_reflective_set.py`: building a
lattice from its Gram data; `signature_pair`, `determinant`, `is_even`,
`two_elementary_invariants`; `possible_root_lengths`; `reflective_root_locus` as an object
and as a membership test; `Aut()`, `O_plus`, `spinor_norm`, `stable_orthogonal_group` and
their `intersection` **as objects**; `reflection`, the action of an isometry on a vector, and
`determinant`; and the discriminant quadratic form with its class count and q-fibres, as
re-run in `coble_528_isotropic_classes-rerun-20261105.txt`.

Not available — every one of them a *decision* about a named isometry or a finite group:

- membership in `O^+(T_Co)`, in `ker(rho_{T_Co})`, or in their intersection: it stops in GAP
  (probe 3's route) or raises the `TypeError` above;
- the discriminant action of a named isometry;
- `roots`, `roots_of_square`, `root_sublattice` for an indefinite lattice (definite-only by
  contract — a different limitation, and not evidence about the `(-2)`-vectors of `T_Co`);
- the orthogonal group of any discriminant form, finite or not (probe 2);
- orbit partitions and orbit representatives (probe 4);
- any operation returning generators of, or a finite-index certificate for, a subgroup of
  `O(L)` of an indefinite `Z`-lattice.

So #646's generation half, #689 and #688 cannot be settled with what decides here, and this
repository does not substitute a locally implemented group algorithm, orbit enumeration or
subobject enumeration for them. The handoffs, restated: (a) membership decisions in
predicate subgroups of `O(L)` for a `Z`-lattice, which is the `TypeError` above and not a new
capability; (b) an operation returning generators, or a finite-index certificate, for an
intersection of predicate subgroups of `O(L)` of a `Z`-lattice; (c) a
`block_preserving_subgroup`-style operation for a finite torsion form, computed from the
declared decomposition rather than from the subobject family; and (d) a working GAP in the
rootfs, which (a)–(c) all sit on top of.
