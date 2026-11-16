# Calculus on Schemes: source transfer audit

## Disposition

The transfer of sources A and B is complete across the calculus chapter and its companion. Independent comparisons found no substantive material from those sources missing and no undue loss of their mathematical voice. The destinations and comparison were committed as research `8afc9b1f77` before either source was trashed. Each original was then trashed and committed separately. The additional illustrated and native TeX archives are audited separately below.

The destinations are `writing/calculus-on-schemes.md` and `writing/symmetric-spaces-and-period-domains.md`. The source files are:

- `/home/dzack/notes/Class_Notes/2024/Dissertation/archive/unused_sections/140_HSD.md` (A).
- `/home/dzack/notes/diss/archive/unused_sections/140_HSD.md` (B).

Source ranges below refer to the files inspected on 2026-11-16. B omits introductory sentences and hypotheses from A and contains damaged TeX. Full-text, inline-math and display-math comparisons found no B-only mathematical assertion. Its final Kähler equivalence list corrects a repeated list number. The transfer uses A's fuller statements and checks B separately for additional material; the semantic correspondence below, not formatting similarity, supports the disposition.

Both files were tracked and clean in the notes repository at commit `9fb9a4b20506a06dada21a78f415e7b47e07f137`:

| Source | Git blob | SHA-256 |
| --- | --- | --- |
| A | `56c8aa5027fe609ce9d737399f205f6cd34484aa` | `f9fe2307c8530499bcf6e082bdee0b64b459819fc414fa25230c3220aa50b4fc` |
| B | `acd98dd0ac732fc9a6ad0f80f1403d648fd72873` | `9823efc8aac239b6799a5fd9cf2fbedb626c119408bc6b5a4e0148e9ef4a9156` |

These identifiers identify the inspected originals and allow their exact text to be recovered from notes history. They are not substitutes for the semantic comparison.

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

## Symmetric-space correspondence

| Source A | Source B | Destination and disposition |
| --- | --- | --- |
| 421–461 | 248–286 | `ex:hsd-classical-pairs`, `rmk:hsd-type-dictionary`, `def:hsd-tube-type`: all classical pairs, Hermitian types and tube types. Exceptional labels corrected to EIII/EVII. |
| 463–480 | 288–305 | `ex:hsd-compact-grassmannians`, `ex:hsd-hyperbolic-spaces`, `ex:hsd-upper-half-plane`: Euclidean, spherical, projective and hyperbolic models. The positive-matrix model of the hyperbolic plane imposes determinant one; the disc stabilizer is unitary. |
| 481–498 | 306–326 | `ex:hsd-compact-grassmannians`, `def:hsd-positive-grassmannians`, `rmk:hsd-positive-graphs`, `rmk:hsd-spinor-conventions`: real, complex and quaternionic Grassmannians, positive subspaces, orientations and connected components. |
| 500–505 | 327–335 | `ex:hsd-isotropic-models`, `rmk:hsd-structures-versus-subspaces`: real and complex Lagrangians, orthogonal complex structures, quaternionic-linear complex structures. The bare `LGr(H^n)` has no specified form and is replaced by the distinct specified spaces, not asserted as an additional equivalence. |
| 507–509 | 337–342 | `ex:hsd-split-isotropics`: split real, complex and quaternionic Hermitian maximal isotropics and the quaternionic skew-Hermitian model `U(2n)/Sp(n)`, with graph and stabilizer arguments. Compatible quaternionic structures appear in `rmk:hsd-structures-versus-subspaces`. |
| 511–520 | 344–353 | `sec-hsd-matrices`, `def:hsd-siegel`, `ex:hsd-isotropic-models`, `rmk:hsd-siegel-complex-structures`: cones, Siegel models and corrected isotropic quotients. The quotient with `U(k)` stabilizer parametrizes a symplectic subspace with a compatible complex structure. |
| 526–535 | 358–365 | `sec-hsd-groups`, `def:hsd-quaternionic-real-forms`, `rmk:hsd-quaternionic-orthogonal`: defining matrices, dimensions of symplectic representations, quaternionic determinant interpretation and the anti-involution. |
| 541–555 | 376–389 | `sec-hsd-matrices`, `def:hsd-siegel`, `ex:hsd-hyperbolic-spaces`, `def:hsd-positive-grassmannians`, `def:hsd-isotropic-grassmannians`: every named matrix and subspace locus. Siegel disc matrices are complex symmetric; the hyperbolic vector space is `k^(n+1)`. |
| 981–1019 | 681–710 | `rmk:hsd-type-dictionary`: Cartan/Helgason labels, bounded domains I–III, compact duals and root types. The maximal orthogonal compact dual is one component. |
| 1021–1024 | 711–714 | `rmk:hsd-siegel-complex-structures`, `rmk:hsd-ppav`: positive compatible complex structures, Riemann form and symplectically marked principally polarized abelian varieties. Positivity and polarization-preserving marking are explicit. |
| 1028–1041 | 718–730 | `rmk:hsd-type-dictionary`, `ex:hsd-classical-pairs`: type IV, its quadric dual, compact real group and root type; exceptional dimensions and references retain the original scope, which did not include exceptional matrix constructions. |
| 1045–1051 | 733–736 | Companion Sources: original Enriques PDF/page pointer retained. The empty definition block makes no mathematical assertion to transfer. |
| 1053–1064 | 737–752 | `sec-hsd-arithmetic-boundary`, `ex:hsd-k3-boundary`: arithmetic quotients, Baily–Borel line/plane strata, the correctly parented discriminant kernel and Type II/III period limits. Boundary strata do not classify central fibers. |
| 1066–1082 | 753–777 | `def:hsd-positive-grassmannians`, `rmk:hsd-hyperboloid`, `rmk:hsd-spinor-conventions`: maximal compact stabilizer, hyperboloid metric, dimension and projective isometry group; sheet character and both spinor conventions. |
| 1084–1092 | 779–785 | `def:hsd-period-domain`, `rmk:hsd-oriented-periods`, `cons:hsd-tube-coordinates`: projective quadric, oriented positive-plane map and explicit tube coordinates with inverse normalization. |

The original questions are resolved mathematically: the compact subgroup fixes `R^p⊕0`; the hyperboloid is dimension `n` with metric the negative of the restricted quadratic form; the real compact orthogonal group is obtained by imposing both orthogonality and unitarity; orientation is retained in the period correspondence; and the spinor convention is stated on reflections. The source's unspecified quaternionic notation is resolved into the defined structures in the table. The empty splitting remark at A:629 is supplied by `prop:calculus-eigensheaves`.

## Voice and exposition

The source's short definition, remark and example blocks, explicit maps, tensor identifications and concrete calculations remain the main form of both chapters. The calculus introduction now opens with the sheaf formulation and references, and the added proofs use continuous mathematical prose. The directional derivative, conjugate descent, paired adjoints, type formulas, quaternionic models and period-plane calculation are explicit. Parallel homogeneous-space lists become comparison tables; this reorganizes the examples without replacing their mathematical content.

Independent readers compared the chapters with the originals under the criterion of preserving mathematical voice while permitting reorganization, clarification and correction. They found no concrete undue change after this revision. Tentative questions with resolved answers now appear as justified claims; malformed formulas and false equivalences are corrected rather than reproduced. Exact sentence identity is not asserted.

## Verification and file disposition

The full-source comparison and the independent companion audit agree on semantic coverage. The companion audit also checked classical real forms, real versus complex isotropic Grassmannians, the quaternionic skew-Hermitian stabilizer, compatible complex structures, spinor signs and orthogonal tube coordinates. The convention for complex Hermitian forms is linear-first; the right-module negative-line model explicitly uses the other convention. The PPAV paragraph cites Huybrechts Corollary 5.3.5 for the Riemann-form criterion and Kondō Remark 5.7 for the moduli quotient.

| File | Semantic comparison | Voice comparison | Disposition |
| --- | --- | --- | --- |
| A | Full calculus and geometry correspondence above; questions and citations resolved or retained. | Definition/remark style and worked calculations retained with corrections. | Trashed; notes deletion commit `f4a2a7186`. |
| B | Full comparison against A found omissions and TeX damage, with no independent content left untransferred. | Its recoverable prose is represented by A's fuller text and the revised chapters. | Trashed; notes deletion commit `3e835a70b`. |

Neither file was an active include or a linked source in the notes tree. The chapters identify their former locations as provenance. Each deletion commit contains only its source file. The trash copies are `~/.local/share/Trash/files/140_HSD.md` (A) and `~/.local/share/Trash/files/140_HSD.md_1` (B); their SHA-256 values match the inspected originals above. The source text also remains recoverable from the recorded Git blobs.

Both chapter renders passed `just docs-lint`, including source citation and reference checks. Browser inspection found no MathJax errors or unresolved chapter cross-references; the rendered domain table was inspected for layout. These checks establish document rendering and links, separately from the mathematical and semantic comparisons.

## Additional archive sources

The subsequent transfer includes the complete text and embedded mathematical images of the illustrated notes, together with the native TeX archive. Its destination is `writing/symmetric-spaces-and-period-domains.md`. Retirement requires semantic and voice comparison of each source, including the image-only material, followed by document checks. The original LaTeX is recoverable as a Git blob as well as from the trash after retirement.

| Source | Path relative to `~/notes` | Git blob | SHA-256 |
| --- | --- | --- | --- |
| C | `diss/old-notes/Ch.1 Basics/Symmetric Spaces/Hermitian symmetric domains.md` | `95b1d4d684288e0e1960ba98c763d2c138bd4bf3` | `451c06fea7350801f4bac9c583dc28771854becb40b8d521e3e23d480de6345d` |
| D | `dissertation/Ch.1 Basics/Symmetric Spaces/Hermitian symmetric domains.md` | `95b1d4d684288e0e1960ba98c763d2c138bd4bf3` | `451c06fea7350801f4bac9c583dc28771854becb40b8d521e3e23d480de6345d` |
| E | `diss/GROUND_TRUTH/my_enriques_notes/140_HSD.tex` | `674a21e847fc9d297582b14b64d32bc682f969dc` | `300694e479c13a3ae0293382b6b2ec1b1e399ba1e8ac4ea2667e4a5458adfabe` |

C and D are byte-identical. Their attachment paths are resolved separately before retirement. Source E contains independent arithmetic and compactification material, so textual overlap with the earlier archives does not establish its transfer.

### Text correspondence

| Source content | Destination | Correction or clarification |
| --- | --- | --- |
| C/D: local/global Hermitian symmetry, types, bounded domains | `rmk:hsd-local-symmetry`, `rmk:hsd-types` | Geodesic symmetry uses `exp(-v)`; parallel curvature is a local criterion. Noncompact type excludes Euclidean factors. |
| C/D: period integrals, markings, arbitrary polarization type | `rmk:hsd-polarization-types`, `rmk:hsd-ppav` | Period matrix is `n × 2n`; cycles belong to homology. The polarization fixes the marking group and sign convention. |
| C/D: half-plane/disc, tori, projective line, homogeneous examples | `ex:hsd-upper-half-plane`, `sec-hsd-grassmannians`, `sec-hsd-matrices` | Stabilizers, effective isometry groups, and determinant-one condition corrected. The projective-line question is answered by the Fubini–Study model. |
| C/D: types I–IV, automorphic/Hodge bundles, tangent spaces | `rmk:hsd-type-dictionary`, `rmk:hsd-automorphic-tautological`, `rmk:hsd-hodge-line` | Type II uses `SO*`, not the split orthogonal group. The determinant Hodge line is an exterior power; canonical exponents are derived. |
| C/D: tube, conic, projective and oriented-plane models | `cons:hsd-tube-coordinates`, `ex:hsd-conic-half-plane`, `rmk:hsd-oriented-periods` | Explicit normalization and inverse; consistent conic equation and positivity. |
| E:7–96, symmetric spaces and orthogonal moduli | Earlier homogeneous-space sections; `rmk:hsd-discriminant-arrangements` | Compact dual distinguished from domain; root mirrors and period-image qualifications explicit. |
| E:99–120, arithmetic/parabolic definitions and classical modular types | `def:hsd-arithmetic-subgroup`, `def:hsd-parabolic-subgroup`, `sec-hsd-arithmetic-boundary` | Faithful representation specified; quaternionic skew-Hermitian real form corrected. |
| E:124–140, type IV toroidal compactification | `rmk:hsd-toroidal` | Admissible fans, unipotent lattice, torus charts and orbits, canonical curve-cusp charts, properness and map to Baily–Borel. |
| E:142–174, modular curves and automorphic forms | `ex:hsd-modular-curve` and its following Hodge-line paragraph | Full level includes Weil pairing; level zero means cyclic subgroup; both projective coordinates have weight 12. The source's line-bundle question is answered by the Hodge line and its complete linear system. |
| E:178–204, K3/Siegel boundaries and rational components | `ex:hsd-k3-boundary`, `rmk:hsd-siegel-boundary`, `rmk:hsd-boundary-components` | Stabilizer/rational-form conditions and component orbits explicit; boundary records periods, not isomorphism classes of central fibers. |
| E:207–236, explicit orthogonal models | `def:hsd-positive-grassmannians`, `rmk:hsd-hyperboloid`, `rmk:hsd-spinor-conventions`, `rmk:hsd-oriented-periods`, `cons:hsd-tube-coordinates` | Negative restricted metric, dimensions, orientation, and spinor normalization retained correctly. |

### Embedded image correspondence

All images were opened and read, including sections with no accompanying prose. The paths are relative to each note's `../../attachments/` directory. Both sets exist and the corresponding image bytes agree.

| Image filename | Mathematical content | Destination |
| --- | --- | --- |
| `2023-04-09-3.png` | Orthogonal moduli examples and signatures; quotient regularity | `rmk:hsd-discriminant-arrangements`, `sec-hsd-arithmetic-boundary` |
| `2024-04-13-5.png` | Hermitian symmetry | `def:hsd-symmetric-space`, `rmk:hsd-local-symmetry` |
| `2023-02-27hermsymdom.png` | Irreducibility and Euclidean/compact/noncompact types | `rmk:hsd-types` |
| `2023-02-27hermdomterm.png` | Harish-Chandra and Bergman realizations | `rmk:hsd-types` |
| `2023-02-27quotient.png` | Adjoint real group and homogeneous quotient | `sec-hsd-shimura-circle` |
| `2024-04-13-6.png` | Circle action at a pointed domain | `sec-hsd-shimura-circle` |
| `2024-04-13-7.png` | Real algebraic group and Shimura formulation | `sec-hsd-shimura-circle` |
| `2023-03-10tube.png` | Tube-domain definition | `def:hsd-tube-type` |
| `2023-03-14tube.png` | Formally real Jordan algebras and cones | `sec-hsd-jordan-tubes` |
| `2024-04-13-16.png` | Siegel action | `rmk:hsd-siegel-action` |
| `2024-04-13-17.png` | Polarized abelian moduli | `rmk:hsd-ppav`, `rmk:hsd-polarization-types` |
| `2023-03-14siegel.png` | Siegel homogeneous model | `def:hsd-siegel`, `rmk:hsd-siegel-action` |
| `2023-03-14-8.png` | Fractional linear action | `rmk:hsd-siegel-action` |
| `2023-03-14-9.png` | Unitary stabilizer and dimension | `rmk:hsd-siegel-action` |
| `2023-03-14-10.png` | Cayley transform and bounded realization | `def:hsd-siegel`, `rmk:hsd-siegel-action` |
| `2023-03-10.png` | Classical and exceptional classification; conjugate invariant complex structures | `rmk:hsd-type-dictionary`, `sec-hsd-marked-diagrams` |
| `2023-03-12proj.png` | Tube-to-quadric map and conic specialization | `cons:hsd-tube-coordinates`, `ex:hsd-conic-half-plane` |
| `2023-03-14riem.png` | Determinant-one positive symmetric matrices | `sec-hsd-matrices` |
| `2023-03-14herm-1.png` | Marked Dynkin classification | `sec-hsd-marked-diagrams` |
| `2023-03-14-13.png` | Special nodes and root systems | `sec-hsd-marked-diagrams` |
| `2023-03-14-14.png` | Exceptional diagrams | `sec-hsd-marked-diagrams` |
| `2023-04-06-4.png` | Parabolics and cusps | `def:hsd-parabolic-subgroup`, `ex:hsd-modular-curve` |
| `2023-04-06-5.png` | Modular forms and projective embedding | `ex:hsd-modular-curve` and its Hodge-line interpretation |
| `2023-05-16.png` | Siegel modular varieties; congruence subgroup property for genus at least two | `rmk:hsd-siegel-boundary` |
| `2023-05-16-1.png` | Siegel Baily–Borel and toroidal compactifications | `rmk:hsd-siegel-boundary`, `rmk:hsd-siegel-toroidal` |
| `2024-04-13-19.png` | Non-Hermitian complex special-linear example | `sec-hsd-arithmetic-boundary` |
| `2023-05-16-2.png` | Hilbert modular varieties and compactifications; congruence subgroup property for totally real fields of degree greater than one | `ex:hsd-hilbert-modular` |

### Independent comparison

The final comparison includes both full text sources and their image-only claims. It checked the period-matrix ordering and Riemann-form sign, cohomological Hodge positivity, canonical-bundle exponents, the two circle-action normalizations, Jordan cones, type IV tube coordinates, and all marked-root incidence data. Low-rank diagram shapes are interpreted through the explicit domain coincidences. The general modular-form map includes its basepoint-free hypothesis; the congruence assertions include the required rank and field-degree hypotheses and cite Bass–Milnor–Serre and Serre.

The source's definition, remark, and example form, explicit quotient models, period maps, and calculations remain. Reorganization groups related examples and replaces screenshot diagrams by named root systems, marked nodes, and explicit edge lists. The original reference pointers are retained in Sources. Independent comparison found no remaining unique mathematical claim or undue change of mathematical voice in C/D/E after these corrections. Rendering and retirement are recorded below separately.

### Document verification

`just docs-lint symmetric-spaces-and-period-domains.md` passed after the final corrections. Chromium inspection of the rendered chapter found no MathJax errors or unresolved cross-references; the Milne, Bass–Milnor–Serre, and Serre bibliography entries all resolved. The marked-root tables were inspected visually and the page fit its viewport. Every destination anchor in this additional-source correspondence exists. These checks are separate from the full-text and image-content comparisons above.

The generated bibliography entries are committed in pandoc-config `1757fd7`. Incoming archive links in the lattice notes, changelogs, TeX assembly, and archive index are redirected to the chapter. Their relative destinations resolve to the authored Markdown file.

### Additional-source retirement

The completed chapter and transfer comparison were committed as research `f132238278` before source retirement. Each source was then checked against its recorded SHA-256, trashed independently, and committed with its incoming-link corrections. The trash copies were checked against the same hashes after retirement.

| Source | Notes retirement commit | Recovery path |
| --- | --- | --- |
| C | `2364eb452` | `~/.local/share/Trash/files/Hermitian symmetric domains.md` |
| D | `14b185217` | `~/.local/share/Trash/files/Hermitian symmetric domains.md_1` |
| E | `e1070f76e` | `~/.local/share/Trash/files/140_HSD.tex` |

All source paths C/D/E are absent. Their Git blobs above remain a second recovery route. Attachment files remain in their original directories; the mathematical content of every embedded image is represented by the correspondence above.

## Arithmetic and modular-form source transfer

The following sources are relative to `research/docs/theory/`. The Git blobs
record their complete pre-transfer contents. The first five destinations are
under `writing/lattice-theory/arithmetic/`; the last is directly under
`writing/`.

| Source and destination basename | Source Git blob | Semantic comparison |
| --- | --- | --- |
| `integral-lattice-algorithms.md` | `581d6d6a11bce9006e3a226ad1ea05ac9724a0c5` | All four source versions; existence versus explicit isometry; specified orbit action; class counts versus mass; independent mathematical acceptance and formal ownership. |
| `integral-trace-lattices.md` | `1162918123e50c5619df7754c1183b40d7dcb32f` | Trace pairing, signed discriminant, cyclic classification including wild ramification, abelian conductor/parity criterion, real signature, maximal-order versus power-basis index, explicit unimodular map, and family restriction. |
| `indefinite-binary-class-numbers.md` | `53f34667cd1e1d1734a1556eac630672bc1cca03` | Proper classes, nonmaximal orders, average bound, Pell regulator formula, effective-constant and exhaustion distinctions, exact analytic errors, Gram sign, and narrow-class conventions. |
| `kneser-neighbors-and-orthogonal-modular-forms.md` | `467f0bb673118f508caf354d54d53f22f8c3b49c` | Cusps and positive-definite quotients, proper/oriented classes, historical genus API and enumeration cap, mass equality, singular-weight identity, character and H1 boundaries, multiplicities, independent cusp vector, and the undetected-error calculation. |
| `finite-automorphism-groups-and-polynomial-certificates.md` | `8d93a8b51b159a7c853f2a445ec3d1af7e173f3a` | Graph hypotheses, polynomial infeasibility, Nullstellensatz identity, solver/prover/verifier distinction, complexity, faithful lattice actions, kernel and lift obligations, infinite-group limitation, and formal acceptance ownership. |
| `modular-forms-and-hecke-operators.md` | `db08ce5684d062e7c7e43a9c9ac6f97b2dbeef00` | Every object and lead: congruence groups and Schreier generation, curves, cusp widths, modular and adelic forms, Hecke algebra, Euler factors, analytic continuation, point counts and zeta functions, modularity, Jacobians, isogenies, complex torsion, literature, and software entry points. |

An independent comparison checked the arithmetic pages against their full
source notes and the four cited preprint versions. The theorem hypotheses
agree with Zhang Theorem 1.1, Diao Theorem 1.1 and §1.1,
Müller–Scheithauer Theorem 5.4, and Drecun Theorem 4. These works were imported
through Zotero as `Zha26`, `Dia26`, `MS26`, and `Dre26`. The modular-form
comparison checked its expanded claims against the local Diamond–Shurman
and Silverman texts. The original modular note marked its claims unchecked;
the book supplies the missing hypotheses and sources, including cusp widths,
bad-prime conventions, Fricke eigenforms, and the field of definition of an
isogeny. The right-coset Schreier formula is stated explicitly as
`ts = h t'`.

The arithmetic prose remains close to its source wording. The former
`sage_extensions/categories/lattices.py` discussion is explicitly historical,
preserving its interface and observed bounds without claiming that the old
path is a current implementation. Programme ownership still points to
`INTENT.md`. No runtime computation is inferred from the archived API account.

The source gate passed with these pages registered in the book. All six
pages rendered successfully after their cross-reference targets were built.
Chromium found no MathJax errors or unresolved cross-references on those
renders; the modular chapter was also inspected visually. Source retirement
is recorded only after the book changes have been committed.
