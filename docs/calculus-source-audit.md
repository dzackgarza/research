# Calculus on Schemes: source transfer audit

## Disposition

Both archived sources must be retained. The chapter gives corrected counterparts to the calculus passages listed below, but does not transfer their full mathematical contents. Neither source meets the condition for trashing.

The destination is `writing/calculus-on-schemes.md`. The source files are:

- `/home/dzack/notes/Class_Notes/2024/Dissertation/archive/unused_sections/140_HSD.md` (A).
- `/home/dzack/notes/diss/archive/unused_sections/140_HSD.md` (B).

Source ranges below refer to the files inspected on 2026-11-16. B is substantially reflowed and contains damaged TeX. Comparison of the calculus passages found the same mathematical claims in both versions; byte equality is not asserted. The final Kähler equivalence list has corrected numbering in B. Neither formatting similarity nor this comparison certifies the untransferred sections.

## Calculus correspondence

Destination names below are stable anchors in the chapter. A row records semantic correspondence, not preservation of every sentence.

| Source A | Content | Destination | Disposition |
| --- | --- | --- | --- |
| 3–11 | Tensor–Hom and duality identities | `rmk:calculus-duality`, `rmk:calculus-pairing-adjoints` | Retained with finite locally free hypotheses. |
| 14–99 | Relative scalars, stalks and fibers, derivations, differentials, vector fields, valued forms | `sec-calculus-differentials` | Universal property and fiber notation made precise. |
| 101–143 | Connections, horizontal sections, covariant derivatives, tangent connections | `sec-calculus-connections`, `def:calculus-torsion` | Leibniz and base-linearity retained; being non-linear is not imposed as a separate axiom. |
| 144–166 | Coordinate computation of directional derivatives | `rmk:calculus-directional-derivative` | Restored the computation; corrected evaluation of a derivation at a point. |
| 168–250 | Exterior covariant derivative, curvature, flatness, bracket, torsion | `sec-calculus-curvature`, `def:calculus-torsion`, `thm:calculus-flat-local-system`, `cor:calculus-monodromy` | Tensoriality proved; topological transport statements confined to manifolds. |
| 252–311 | Pairing adjoints, real-point positivity and semidefiniteness, metrics, metric connections | `rmk:calculus-pairing-adjoints`, `def:calculus-real-positivity`, `def:calculus-perfect-metric`, `def:calculus-metric-connection` | Real positivity distinguished from perfectness; the induced connection acts on the bilinear dual tensor. |
| 313–419 | Affine connections, Riemannian metrics, Levi-Civita, transport, geodesics, sectional curvature, space forms | `def:calculus-torsion` through `thm:calculus-space-forms` | Smooth function sheaves use locally ringed spaces. Curvature sign made consistent; complete connected manifolds and scale are required for the model-space conclusion. |
| 557–641 | Scalar conventions, complex modules, real structures, base change, descent and conjugate-pair descent | `sec-calculus-complex-modules`, `rmk:calculus-conjugate-descent` | Scalar complexification on a fixed space separated from scheme base change. The descent cocycle is corrected. Fixed points do not replace descent. The unrestricted claim of effective descent of arbitrary schemes is not retained as a theorem. |
| 643–746 | Conjugation, eigensheaves, tangent and cotangent types, integrability, holomorphic maps and functions | `def:calculus-conjugate` through `sec-calculus-integrability`, `rmk:calculus-polyvector-types` | Conjugation is semilinear. Smooth type sheaves and holomorphic sheaves distinguished. Integrability is required for the full Dolbeault splitting. |
| 747–791 | Holomorphic bundles, sections, compatible and holomorphic connections, flat connections | `sec-calculus-holomorphic-connections` | Leibniz operators are scalar-linear, not structure-sheaf-linear. The real connection must preserve the complex structure. |
| 793–815 | General sesquilinear pairings and parallel pairings with type formulas | `def:calculus-sesquilinear` | Restored independently of positivity or nondegeneracy. |
| 819–908 | Hermitian metrics, paired-adjoint symmetry, Hermitian and Chern connections | `sec-calculus-hermitian`, `rmk:calculus-hermitian-adjoints` | Conjugate dual identification made explicit. Positivity is on fibers, not on a section that can vanish. |
| 910–944 | Almost Hermitian structures, real/complex/alternating metric dictionary, normalization and averaging | `cons:calculus-fundamental-form`, `rmk:calculus-hermitian-reconstruction`, `rmk:calculus-hermitian-normalization`, `prop:calculus-compatible-metric` | Restored converse dictionary for general bundles. Closedness is additional; the eigensheaf factor is distinguished from the formula on the original real bundle. |
| 946–979 | Parallel complex structures, almost Kähler and Kähler structures | `def:calculus-almost-kahler`, `def:calculus-kahler`, `thm:calculus-kahler-equivalences`, `rmk:calculus-parallel-J` | The induced derivative is the commutator with the connection; a general parallel bundle endomorphism is not itself a Kähler structure. |
| 1094–1101 | Endomorphisms compatible with metrics | `def:calculus-isometric-endomorphism` | Restored sheaf identity. Fiber identities alone need not detect nilpotent errors. |

The opening bibliography and specific archived attributions are retained in the chapter's Sources section. The old keys correspond to `Kat70`, `Ram04`, `HK24`, `NR69`, and `Hel01` in the current bibliography. Their attribution in the archive is distinguished from the references actually used to justify the corrected chapter.

Two formulations require an explicit distinction. The conjugate scheme in A:643–650 is transferred to `def:calculus-conjugate-scheme` as base change along complex conjugation, rather than a presumed involution on an arbitrary complex scheme. The names “almost Hermitian scheme” and “Kähler scheme” in A:912–978 refer to a mixture of smooth function sheaves and algebraic schemes. Their intended tensor data, positivity, integrability, closedness and parallelness conditions are retained in the chapter's definitions and comparison section. The chapter does not assert that this mixture is a general algebraic definition: positivity is specified on real fibers, while recovery of holomorphic charts is an analytic theorem. This is a correction of the setting, not a claim that the original generality was established.

## Material still held by the originals

| Source A | Source B | Material requiring a destination before deletion |
| --- | --- | --- |
| 421–480 | 248–305 | Compact/noncompact symmetric-space pairs; Hermitian and tube-type classification; Euclidean, spherical, projective and hyperbolic homogeneous models. |
| 481–510 | 306–343 | Real, complex, quaternionic, indefinite, oriented, Lagrangian and isotropic Grassmannians; compatible complex and quaternionic structures. |
| 511–555 | 344–390 | Matrix realizations, real forms of classical groups, positive cones, Siegel domains, and defining forms. |
| 981–1051 | 681–736 | Cartan/Helgason type dictionary; domains I–IV and compact duals; root types; marked principally polarized abelian varieties; exceptional-type pointers; Dolgachev reference pointer. |
| 1053–1064 | 737–752 | Orthogonal arithmetic quotients, component groups, Baily–Borel boundary strata, polarized K3 groups, and Type II/III degenerations. |
| 1066–1092 | 753–785 | Hyperboloid and orthogonal period-domain constructions, isometry groups, oriented positive planes, tube realization, and spinor-norm questions. |

These passages contain assertions that require correction, not just relocation. Examples include mismatched matrix dimensions, compact versus noncompact stabilizers, the sign of the induced hyperboloid metric, orientation in the period-domain correspondence, and spinor-norm conventions. Their questions and citation pointers are part of the material to preserve. This table identifies the outstanding scope; it is not a correctness certificate for those claims.

## Voice and exposition

The sources use short definition and remark blocks, explicit maps and tensor identifications, and concrete calculations introduced by phrases such as “Concretely” and “Note that.” The chapter retains the sheaf-first order of ideas and explicit maps, but the first synthesis is a substantial rewrite. Its long explanatory introduction, numbered proof blocks, and repeated “Assume/Prove” headings are additions, not the source's voice.

The restored calculus passages use short definitions and remarks and recover the directional-derivative calculation, conjugate descent map, pairing adjoints, and type formulas. This restores material that the abstract treatment had compressed away. It does not establish sentence-level style fidelity for the whole chapter. The originals remain the evidence for a further comparison of exposition and voice.

Deletion requires a separate decision for each file, based on a complete comparison with its destinations. Render success, matching headings, shared subject matter, and preservation of a backup are not evidence of full semantic transfer.
