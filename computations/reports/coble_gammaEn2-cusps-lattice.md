# The lattice-side cusps of $T_\En$, at the held port revision

This record holds the public calls that replace the finite-form walk on the vector and plane sides,
with the exact revisions they imported, and the result of each.

## Provenance of the call

| component | revision | where |
|---|---|---|
| Sage | `11.0.beta5` | the adopted rootfs `/workspace/nucleus/work/home/sage-image/rootfs` |
| `sage-indefinite-port` | `991b88b095a42a1e3679569ea42328c900c120f6` ("test: pin the four resolved #15 defect rows with their reproducers") | scratch clone `.scratch/port-held`, imported from `/repo/.scratch/port-held/src` |
| `sage-extensions` | `cdafca84065405cb810bba047f8a965299b03762` — the pin the held port's `pyproject.toml` declares | snapshot `/workspace/nucleus/work/home/sage-extensions-cdafca84`, bound into the image as `/prov` |

The earlier attempt at this call, recorded in `coble_gammaEn2-known-family-obligation.md`, ran against
the **old image** pair (port `4f0ee50c…` in the rootfs with provider `15db925b…` on `PYTHONPATH` — a
mixed pair, since that port declares `7b222e86…`) and raised

```
File "/repos/sage-indefinite-port/src/sage_indefinite_port/indefinite/recursive.py", line 154
  source_coordinates = tuple(int(coordinates(label)) for label in source_labels)
TypeError: int() argument must be a string, a bytes-like object or a real number,
           not 'OwnedJoinCategory.element_class'
```

At the held revision, with the provider it declares, the same call succeeds:

```
imported sage_indefinite_port from: /repo/.scratch/port-held/src/sage_indefinite_port
imported sage_extensions     from: /prov/src/sage_extensions
T_En: rank 12, det 1024, signature (2, 10)
T_En.cusps(1) -> 2 records   (326 s)
  record: Cusp of rank 1 in Integral lattice of rank 12 and signature (2, 10)
  record: Cusp of rank 1 in Integral lattice of rank 12 and signature (2, 10)
```

So the failure was the tracked `int(owned element)` defect at the old image pin, not a defect of the
current port.

## What the two records are

`T_En.cusps(1)` returns the $\Orth(\ten)$-orbits of primitive isotropic rank-one subobjects, i.e. the
$0$-cusps of $F_{(10,10,0)} = \bD(\ten)/\Orth(\ten)$, each with its parabolic subgroup, its stabilizer
generators and transporters. The count is **two**, which is what [@AEGS25 §3.2] states — "two 0-cusps
distinguished by $\operatorname{div}(e) = 1$ or $2$" — and it is a lattice-level count: no
discriminant picture is involved.

This is the anchor the stage-1 batch lacked. It confirms, on the lattice, that the two divisibility
classes are two $\Orth(\ten)$-orbits, which is one of the two inputs of the surjectivity argument in
`@rmk:gamma-en-two-fibres`; the other, transitivity of $\Orth(A_\ten,q_\ten)$ on the $527$ nonzero
isotropic classes, is in `coble_gammaEn2-card-run.txt`.

## The plane side

`T_En.cusps(2)` — the $\Orth(\ten)$-orbits of primitive isotropic rank-two subobjects, i.e. the
$1$-cusps of $F_{(10,10,0)}$ — is the call that decides which finite strata of planes lift: every
liftable stratum of the finite picture is the image of one of these lattice orbits, so the number of
them bounds the number of nonempty strata from above. It is running as job `jmw69fxhq` under the same
pair, and its result is recorded here when it lands; the transcript is `.scratch/cusps2.out` and the
job log `.nucleus/jobs/jmw69fxhq.log` until it is folded in.

## What this record does not claim

Not the $9$ one-cusps of $\fen$: that needs $\gent$-orbits, not $\Orth(\ten)$-orbits, on the plane
side, and the group is not the full orthogonal group. Not the $5$: `@rmk:gamma-en-two-fibres` states
exactly what stands there — surjectivity of the divisibility map is proved, injectivity needs the
Eichler transitivity of $\Orth(\ten)$ on the fibre over a class, and that is not assumed.
