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

The arithmetic prose was committed in `7e3d003d94` and book integration in
`0f4b0a41db`. Each source was checked against its recorded blob, trashed
separately, and committed. The recovered trash bytes have the same Git blob
hashes. This is the retirement record at those revisions, not a live source
inventory.

| Source basename | Retirement commit |
| --- | --- |
| `integral-lattice-algorithms.md` | `eca18b0e14` |
| `integral-trace-lattices.md` | `fb1ced1575` |
| `indefinite-binary-class-numbers.md` | `dc3e332496` |
| `kneser-neighbors-and-orthogonal-modular-forms.md` | `7b33d26506` |
| `finite-automorphism-groups-and-polynomial-certificates.md` | `381c2bcbdc` |
| `modular-forms-and-hecke-operators.md` | `42dc97f893` |

Each trash recovery path is `~/.local/share/Trash/files/` followed by the
basename in the table. The original Git blobs provide independent recovery.

## Affine, hyperbolic, and compactification transfer

This correspondence records the source revisions used for the November 2026
migration. Native TeX paths below are relative to
`notes/diss/GROUND_TRUTH/my_enriques_notes/`; the mixed theory notes are
relative to `research/`. The historical dissertation remains a separate
authored work.

| Source | Original Git blob | Mathematical destination |
| --- | --- | --- |
| `100_BB.tex` | `8a8ea1f98da5ecdf59374f156b9ff3cadc9556e3` | `writing/symmetric-spaces-and-period-domains.md`; Coble toroidal and Kulikov chapters |
| `110_boundary.tex` | `2320b17efecc7a437bf72dd0476cc7d1d5ef60f3` | Coble toroidal, Kulikov, and KSBA chapters; symmetric spaces |
| `160_IAS.tex` | `176f3ed45f7f053c93e16591d943b2287453052d` | `writing/integral-affine-geometry.md`; shared native figure objects and sources |
| `170_KPP.tex` | `8c2b0879c0ccaa9b71928290476dd44fcdb52346` | Coble anticanonical-pair, Kulikov, toroidal, and KSBA chapters |
| `180_KSBA.tex` | `736d8ef7db63097a965a040691fbb4cd6c77457f` | Coble toroidal, anticanonical-pair, and KSBA chapters |
| `docs/theory/hyperbolic-index.md` | `5d53bb3e3c86473815335e5117a599b0c579945a` | The four chapters under `writing/lattice-theory/hyperbolic/`; software contracts remain in the source note |
| `docs/theory/integral-affine-manifolds-and-polyhedral-complexes.md` | `03cf4e87e4b03de1206194563c45c2175e0cee50` | `writing/integral-affine-geometry.md`; category graph and software contracts remain in the source note |

### Native-source correspondence and corrections

| Source ranges | Retained content and editorial decisions |
| --- | --- |
| `100_BB:5–64` | Boundary codimension and incidence; rational parabolics; affine-cone weight and character; degree-zero modular-form ring and Proj; descended ample automorphic line. Homogeneity is on the affine cone. |
| `100_BB:66–109,119–125` | Toroidal charts, cusp lattices, fan refinement and morphisms; log Calabi–Yau components; maximal dual complexes and the qualified sphere/SYZ statements; squarefree-degree cusp classification. The general cusp statement uses squarefree `d`; the explicit Coxeter example is degree two. |
| `110_boundary:5–79,236–344` | PPAV periods and exponential coordinates, nodal cubic, monodromy quadratic form, Voronoi/Delaunay duality, Mumford height projection and quotient, theta/Proj description, genus-two cell example, and wall/ray limits. The honeycomb graph and its dual triangulation are distinguished. Component counts belong to the specified cell type. |
| `110_boundary:81–234` | Full degree-two Coxeter diagram and symmetry; eighteen-sided polygon, surgeries, doubled sphere, weighted equator, triangulation and gluing; twenty-four dependent root pairings in a rank-nineteen lattice; stable eighteen-plane example and Type II labels; Enriques/Coble boundary questions. The last six parameters measure near/opposite distances for the same three singularities, not six independent surgeries. |
| `110_boundary:345–482` | K3 cusp torus coordinates, Fermat quartic degeneration and small resolutions, intersection/dual complexes, smoothing, recognizable divisors, and the AET/ABE fan comparisons. Uniqueness concerns the stable pair after contraction. The flat ramification limit need not equal the entire fixed locus on a nongeneric Kulikov fiber (AET23 Remark 6.22, Lemma 6.34, Theorem 6.35). |
| `160_IAS:4–174` | Affine groups, atlases and marked lattice points; Lagrangian torus fibrations and their cotangent-torus converse; local singularity models; pseudofans and corner blowup equivalence; charge and Type III gluing. Tangent lattices do not select affine lattice points. |
| `160_IAS:175–1043` | Boundary intersection rules; corner/internal blowups and charge; the tenfold moment triangle; every corner and internal blowup panel; nodal trades in order `p13,p23,p12`; nodal slides of sizes two and three. Conic and cubic self-intersections are corrected to four and nine. |
| `170_KPP:6–114` | Quotient exceptional curves of squares minus four, minus two, minus one; anticanonical pairs; the nine-blowup example and native drawing; Kulikov models, modifications, recognizable divisors and d-semistability. |
| `170_KPP:117–213` | Kulikov types and log monodromy, charge, existence and meaning of toric models, and charge as the number of interior blowups. Smooth rational double curves and nodal pseudofan conventions are distinguished. |
| `180_KSBA:5–72` | Stable curves and dualizing degrees; period-extension question with its conditional answer; sextic branch pairs; dlt/slc and stable pairs; small positive coefficient and avoidance of log canonical centers. |

The named raster figures from `110_boundary.tex` are retained byte-for-byte
in the shared figure library and displayed in the corresponding chapters.
The full Coxeter drawing is the canonical `vinberg-19-1-1` object, whose
source identifies its lattice and AET23 diagram; the nine-blowup drawing
retains `NontoricBlowups.tikz`. The literal word `image` at
`110_boundary:396,404,413,418` has no filename or attached drawing in the
source. Its surrounding mathematical descriptions are retained; these
unpopulated editorial markers supply no image data to recover.

The IAS archive contains nine figure environments and two inline pairs,
giving twenty-three drawn panels. Native source panels and captions live
under `pandoc-config/figures/sources/ias-surgeries/`, with canonical drawings
under `figures/objects/ias/p2-*.tikz`. The shared figure changes are committed
in `e85af92`, with their cut style in `cfa97af`. Blank image paragraphs and
Quarto grids are necessary here: the initial adjacent-image paragraphs
rendered only their first panels. The corrected HTML contains every panel;
Chromium inspection checked the figure grids, formula rendering, and image
loads separately from the semantic comparison.

The compactification and affine writers independently compared each other's
destinations with the native sources. A further fresh mathematical audit
identified the lattice-point marking and positive-surgery hypotheses; both
are explicit in the final prose. The source's definitions, worked examples,
questions, and diagrams remain, with the corrections above rather than
verbatim retention of erroneous claims.

### Mixed theory notes

The original hyperbolic note's lines 1–112 and 1608–1633 are represented in
the integral-index chapter; 113–791 in real/rational splitting; 792–1607 in
effective embedding bounds; and the later mathematical norm-fiber,
embedding-locus, undecidability, and three-ring examples in those chapters
and `norm-fibres-and-embedding-loci.md`. The explicit constants, completion
argument, all-versus-orbit bounds, split and nonsplit binary cases, scaled
definite shell, Borovoi congruence example, and constrained-search distinction
were retained. Calderón's equivalence locator is corrected to Theorem 5.1
and the Siegel-set locator to Proposition 6.6. Zotero imports supplied
`Cal23`, `Bor00a`, `Hen02`, `Tur37`, `LLL82`, and `Cas78`.

The affine design note's original lines 134–338 supply the general
mathematical exposition. Its category graph, constructors, map types,
reuse ledger, phases, and acceptance boundary remain in their existing
implementation owner. Its mathematical links now lead to the book.

An independent preservation audit found that initial condensation had
omitted implementation clauses. The retained notes restore the original
Cauchy-map evaluation, enclosure and relation-termination rules; unknown
predicate and scaling behavior; exact determinant and finite-bound
providers; public API examples and source links. The affine note restores
manifold category guards, torsor identities, rectangular affine maps,
singular-map requirements, PL links, cellular and collar gluing checks, and
the specified doubling and involution data. These are preserved design
contracts and historical implementation observations. This migration does
not assert that their runtime specimens were executed. The mixed notes are
therefore retained rather than trashed.

### Native archive retirement

The transferred prose and source corrections are committed in research
`593390c250`; historical implementation references are clarified in
`29240414df`. The full book completed both render passes. Its external-link
check exposed obsolete PDF addresses in the earlier period-domain chapter;
`53baecb203` preserves their titles and page references and updates the
author-hosted Borcherds link. The affected chapter was rendered again. The
source gate, external-link check, and a complete rendered-site check of local
files and fragment targets then passed. External requests that time out or
reject automated clients remain subject to the existing gate's limitations.

The archive index and TeX entrypoint were redirected to the book in notes
`d9f24326b`. Each native source was checked against its original blob above,
trashed individually, and committed only after the semantic comparisons and
render checks. Each recovery copy in `~/.local/share/Trash/files/` has the
same basename and Git blob hash as its source.

| Native source | Retirement commit in notes |
| --- | --- |
| `100_BB.tex` | `be902b63a` |
| `110_boundary.tex` | `bc1cf13bf` |
| `160_IAS.tex` | `9a07fdfb4` |
| `170_KPP.tex` | `7cca50097` |
| `180_KSBA.tex` | `31f18e549` |

This records verification and retirement at these revisions. The shared
figure sources and the mixed implementation notes retain their distinct
roles described above.

## Enriques, Coble, lattice, and toric archive absorption

This is a fixed-revision transfer record. The book state is research
`2bd4eb0abc`; the source checkpoint before retirement is notes
`44d01adb0`. Source blobs and individual retirement commits appear below.
The comparison included the differing passages of the successive manuscripts,
not just the latest draft or their shared text.

### Mathematical owners and semantic comparison

| Archived material | Book owner and preserved content |
| --- | --- |
| Coxeter notes, diagrams-to-surfaces, and appendix | `writing/coble/compactifications/` and `writing/coble/cusp-correspondence/`: chambers, Vinberg calculations, cusp incidence, modular curves, preliminary and completed diagrams, and the questions connecting diagrams to surfaces |
| Hyperbolic and lattice notes | `writing/lattice-theory/`, `writing/coble/lattices-and-moduli/`, and `writing/coble/appendix-reference/`: lattice definitions and proofs, discriminant calculations, Niemeier data, hyperbolic models, monodromy, and native illustrations |
| Mirror and nonsymplectic notes | `writing/coble/stable-limits/nonsymplectic-k3-models.md`, `writing/coble/stable-limits/ias.md`, and the Kulikov chapters: markings, root arrangements, admissible cusps, mirror lattices, Kulikov models, and open realization questions |
| V1–V4 and successive Enriques manuscripts | The Enriques results, stable-limits, compactification, and cusp chapters: equations, proofs, folded families, boundary counts, root coordinates, gluing constructions, and draft-specific examples |
| Dated Enriques meetings and compiled notes | Surface types, polarizations, moduli construction, nonsymplectic models, and main results: fixed-locus alternatives, period quotients, normalization, inverse-period questions, and the special and nonspecial models |
| Coble paper versions and moduli notes | Coble basics, covers, moduli, and research-program chapters: arguments, examples, diagrams, acknowledgements, and the distinction between established results and proposed compactifications |
| Enriques talk facts and surface-reading notes | Surface types, K3 periods, calculus on schemes, and adjunction: classification, linear systems, Hodge and Tate structures, torsors, positive-characteristic qualifications, automorphism groups, and surface examples |
| Toric notes and mathematical whiteboards | `writing/toric-geometry.md` and integral-affine chapters: fans, normal cones, support functions, polar polytopes, divisor sequences, blowups, nef partitions, and degeneration examples |
| Questions for Phil | `writing/coble/stable-limits/ias.md`: the fiber class, normalized integral-affine volume, and the nilpotent-orbit meaning of approximation |
| Outline, index, entrypoint, glossary, and bibliography wrapper | The book's topic organization, definitions, notation, and annotated bibliography |

The transfer keeps proofs and examples as mathematical exposition. Questions
remain questions where the sources do not establish a result. Repeated versions
were reconciled at their mathematical owners; incomplete or false assertions
were corrected rather than promoted to theorems.

### Corrections that affect the mathematical content

- The V3 root-coordinate tables have corrected signs and basis labels. The
  existing Sage computation verifies the square and triangle pairings and the
  folding sums. The corrected tables and label maps are in the reflection
  chapter (`dd4ce7306a`, with links corrected in `df64c20532`).
  The cusp-four parabolic is two copies of affine $D_4$; the cusp-five
  description includes its root reflections.
- The five draft IAS drawings retain their parameter labels. The conflict
  between the even highlighted vertices and the proposed odd negative
  eigenspace in cusp five remains an explicit realization question.
- The published ABCDE notation was checked against the actual
  `sty-en.sty` source of arXiv:2312.03638. Left minus signs, left primes,
  and left subscripts are distinct. Boundary counts and the published
  one-cusp diagrams are included.
- The cover square uses normalization where quotient singularities require
  it. Smooth branch hypotheses, ADE resolutions, invariant lattices,
  polarizations, pair coefficients, and volumes are stated separately.
  Period lattices are distinguished from polarization lattices.
- The surface material corrects the intersection sign for Coble boundary
  curves, the Type II/III distinction, primitive orthogonal splitting,
  Picard-rank bounds, symplectic automorphism bounds, and base-point-free
  hypotheses. Étale torsors are sheaves without an unsupported universal
  representability assertion.
- Toric support-function conventions, dual polytopes, Hilbert bases, divisor
  sequences, moment classes, and blowup formulas are explicit. The quadric
  degeneration from the whiteboards is included. A fiber alone does not
  provide the missing positive-square polarization in the Halphen program.
- The draft's unfinished proof slots are replaced by complete arguments
  where supplied by later sources; unresolved assertions retain their
  research-question status.

### Native figures and verification

Native TikZ and Excalidraw sources and the relevant raster captures are
preserved in the shared figure repository. Relevant preservation commits include
`85e7592`, `60a42ce`, `a5a9b90`, `99284d4`, `1b0f8b3`, and
`99393a8`. The IAS inputs were corrected in `cc79682` so that their
definitions are inside each TikZ picture. The book's Scattone drawing supplies
its local styles. These repairs address empty figure bodies that a successful
Quarto exit alone did not detect.

The full book gate completed both render passes and its citation,
cross-reference, anchor, and external-link checks. After the final source
changes, affected pages were rendered again. The final source check passed
against the registered chapters and staged bibliography. A whole-site scan
found no missing images, empty figures, unresolved references, broken local
files, or missing fragment targets. Every registered source was older than
its rendered page. Chromium loaded MathJax and completed typesetting on the
IAS, Scattone, ABCDE, and surface-types pages without math errors. The native
IAS and Scattone diagrams, toric polar diagram, and ABCDE table were visually
inspected. Grouping the period-domain subscript fixed the browser-only
double-subscript error.

### Retirement and retained source boundaries

Each source below matched its committed audited blob immediately before
retirement. Each was moved through `trash`, checked absent from its original
path, and recovered by its original absolute path in the Trash metadata.
The recovery file's Git blob hash matched the source hash before the individual
retirement commit was made. Git history and Trash retain the originals.

The mixed whiteboard note now contains its calculus-grading photograph.
The meeting index remains because its linked meeting PDFs were not found in
the inspected filesystem sources and their contents could not be verified.
Active Obsidian drawings remain with their consumers; byte-identical copies
are preserved in the shared figure repository. These retained items are not
claims of unverified absorption.

| Source path relative to notes | Source and recovery blob | Retirement commit |
| --- | --- | --- |
| `diss/GROUND_TRUTH/my_enriques_notes/000_INDEX.md` | `a60d59cfec728495c5c0113bf696a7914faf9940` | `463b6b2d6d` |
| `diss/GROUND_TRUTH/my_enriques_notes/120_coxeter_diagrams.tex` | `e523731e6e389c407425f72caee06be5baf7e787` | `e5dc6d8940` |
| `diss/GROUND_TRUTH/my_enriques_notes/130_diagrams_to_surfaces.tex` | `9c0d7ad8f12fc77696871ae88bd89b63054b2c37` | `ca621912bc` |
| `diss/GROUND_TRUTH/my_enriques_notes/150_hyperbolic.tex` | `1bd68e8680e1facd14620fa1d63a7565d5e4a59a` | `ad0953ffb1` |
| `diss/GROUND_TRUTH/my_enriques_notes/190_lattices.tex` | `8eaa6d08b039ac0f361eb6cc82cff96b3f9d03bb` | `78ba16f442` |
| `diss/GROUND_TRUTH/my_enriques_notes/200_valery.tex` | `f1628040cf0975951c27307f965804e26d297825` | `864a4f5f36` |
| `diss/GROUND_TRUTH/my_enriques_notes/210_Mirror_Symmetry.tex` | `de64e45593609cf63d9bbd231ae9e6dca22f2d6f` | `4e8ba78f22` |
| `diss/GROUND_TRUTH/my_enriques_notes/900_appendix.tex` | `8a67357f44accf14884e6c00f1fb04656cf0c0c5` | `f506d3782c` |
| `diss/GROUND_TRUTH/my_enriques_notes/V1.tex` | `972eee05db53ed56a922b2c25a792f556d83963d` | `f51f8328b5` |
| `diss/GROUND_TRUTH/my_enriques_notes/V2.tex` | `3463cb4c27e5f750afafd54bc218ee123d32d56c` | `5f162ab3a7` |
| `diss/GROUND_TRUTH/my_enriques_notes/V3.tex` | `11f99eb01baa1ed341c415af792dd390a559232b` | `56554ae485` |
| `diss/GROUND_TRUTH/my_enriques_notes/V4 Paper Outline.md` | `e40ae441d13c773ac10d1ab801bfe064af03ec8d` | `f7c5ceea39` |
| `diss/GROUND_TRUTH/my_enriques_notes/en-Dec6.tex` | `5792d804289856e10e6d0c8b608bc43a2b34c50e` | `46cfa37ac4` |
| `diss/GROUND_TRUTH/my_enriques_notes/en-compositio-Jan17-2024.tex` | `9ba971188c6fc9a3136eaa2f3a0b45699aec2ebb` | `b8cf1c269c` |
| `diss/GROUND_TRUTH/my_enriques_notes/en-dzg-Nov16.tex` | `87bde74bebe30b2ef581a3d403db0f26cbe7db5e` | `49c056957a` |
| `diss/GROUND_TRUTH/my_enriques_notes/en-dzg-Nov25c-just-proofreading-edits.tex` | `1516d2a3a76bc0839c564fa830ee2e10a1e6d353` | `28048690e1` |
| `diss/GROUND_TRUTH/my_enriques_notes/en-mathannalen.tex` | `fa819d3d3a6370689cefc07d81b4a9710ecce4fd` | `d721dd2ed2` |
| `diss/GROUND_TRUTH/my_enriques_notes/en-nagoya-nov30-2024.tex` | `f190982930225fdaa53318d846e0a056f28b1976` | `ff777285a0` |
| `diss/GROUND_TRUTH/my_enriques_notes/en-onarxiv-Dec27.tex` | `8d4eb2c398df983b729375fbbfec51915fbf0168` | `84d15fbfcc` |
| `diss/GROUND_TRUTH/my_enriques_notes/en-revised-Oct05.tex` | `15b64e3d7f12f286429654f723eb99813dfb2001` | `6fd10030eb` |
| `diss/GROUND_TRUTH/my_enriques_notes/en-revised-Oct12-Phil.tex` | `998d2e0cf898fbcb01ec1beee72c60889a17f032` | `8c8996e31f` |
| `diss/GROUND_TRUTH/my_enriques_notes/en-revised-Oct12b-Phil.tex` | `3586705a444ecad431b13374c52bf38e72d2dff3` | `be0baf2165` |
| `diss/GROUND_TRUTH/my_enriques_notes/en-revised-Oct15-Phil.tex` | `31e26d87316cbd09c506d578507dca179e25b019` | `b536140885` |
| `diss/GROUND_TRUTH/my_enriques_notes/en-valery-Dec17.tex` | `b1bfedd4204c050e4b6894843bc9dee803381488` | `2a23b5a4ef` |
| `diss/GROUND_TRUTH/my_enriques_notes/en-valery-Dec18b.tex` | `46ae9541d1082ee3630f5f1dd78770cfa0d6d5f2` | `10e1509c7b` |
| `diss/GROUND_TRUTH/my_enriques_notes/en-valery-Dec19b.tex` | `7ddc63f64446af155f6b847de0d9d27639f5ca23` | `8cc9883bf4` |
| `diss/GROUND_TRUTH/my_enriques_notes/en-valery-Dec19c.tex` | `290b2d09dad69848b6ce20f89a2a1993b00990a6` | `2e304b766e` |
| `diss/GROUND_TRUTH/my_enriques_notes/en-valery-Dec22.tex` | `5b6df17f751faa2395fef824c57bc3306321cde6` | `68e02166ad` |
| `diss/GROUND_TRUTH/my_enriques_notes/en-valery-Dec22b.tex` | `4276c4ebfd9813198486bf74e5c1a3ed7287ac03` | `3037e68836` |
| `diss/GROUND_TRUTH/my_enriques_notes/en-valery-Dec26.tex` | `97d6c8a32b460740bcbb3b7fa58a23c15003d9de` | `1e1dc6e4cc` |
| `diss/GROUND_TRUTH/my_enriques_notes/en-valery-Nov15.tex` | `d28a61bbc00f6eda7db1c961a4d9d44de81512a0` | `b740fe96c9` |
| `diss/GROUND_TRUTH/my_enriques_notes/main.tex` | `2298c654a7bb434a2357bd21e4f655bdf95f23f6` | `d83b8b57ec` |
| `diss/GROUND_TRUTH/my_enriques_notes/symbol_glossary.tex` | `65f1b27df68f7c89c1f063fd5ea925f24bede8f1` | `d0166898ae` |
| `diss/old-notes/000 Dissertation Outline.md` | `01cd3911f0a316e7996e2ca34dbe78ff42527a73` | `8bd0ffadff` |
| `diss/old-notes/2023-08-01 Old Notes.md` | `d6be125614c69a6787fae36977b13f5f6d321510` | `622f37bc13` |
| `diss/old-notes/Archive/000 Questions for Phil.md` | `9ad23f53d9690616db37d681bf566ebe70afdfc2` | `6a18c5d6dc` |
| `diss/old-notes/Ch.1 Basics/Toric Geometry/Misc Notes 2023-08-01.md` | `7eab9d07808b0b145e80488b1ec0ca66ae003821` | `a034d0ab8e` |
| `diss/old-notes/Ch.5 Enriques/000 Enriques Talk Facts 0.md` | `559aebadee33dbd9e90de90ef1c5cf322b554bf8` | `fc18f81588` |
| `diss/old-notes/Ch.5 Enriques/Complete Moduli of Enriques Surfaces.md` | `c35515aaa0cf93df76461a71ffb9fd2bcc8721f4` | `3ce52b3dc9` |
| `diss/old-notes/Ch.5 Enriques/Enriques surfaces.md` | `33bf4185cdee47cfdfe98436a2bb68c9c38ef238` | `8ab96886e6` |
| `diss/old-notes/Ch.5 Enriques/Horikawa's Model.md` | `0300654a7002da0181fd4fe1e31917eee07b6518` | `058d988dc7` |
| `diss/old-notes/Ch.5 Enriques/Moduli of Enriques.md` | `58676aef868ecfb8cd3a4d1f1f32d2cb837372f6` | `1d029b552c` |
| `diss/old-notes/Ch.6 Cobles/Coble Surfaces.md` | `5c8de01f2e5e4c36c4e0315d577795a0169c0b06` | `340b38443e` |
| `diss/old-notes/Ch.6 Cobles/moduli of Cobles.md` | `e1c6f591aa43789b89682a66b982c1eebc948bf6` | `90741d6f1e` |
| `diss/old-notes/Enriques/030_Moduli_of_Cobles.md` | `02b367aea0689c0752b6761a7c11b4209ba7c0f9` | `998b1fec11` |
| `diss/old-notes/Enriques/CoblePaper.md` | `10dae1c6c6ac83143e353cfb6c4faeadc1b7b0e9` | `63e53befc2` |
| `diss/old-notes/Enriques/CoblePaper_stripped.md` | `d13929c8654fad05de967dbc415de9e8645f7ff6` | `845fb5ec10` |
| `diss/old-notes/Enriques/Complex Algebraic Surfaces, 2nd ed_ - Arnaud Beauville.md` | `0e24e373ccaedbb302c8ef2f562cbe0730a0d047` | `0d92ac25e8` |
| `diss/old-notes/Enriques/Enriques-Kodaira Classification.md` | `2af97053f4215b87ed693ffb4c76b30ce83ff19c` | `cb1913f0e4` |
| `diss/old-notes/Enriques/LightningTalk_stripped.md` | `d6c7eb2322c3645df47c3af27c2f20c6420766c8` | `b8f2fd8dc3` |
| `diss/old-notes/Enriques/ResearchStatement.md` | `e2499fdd93e7cb2487a0971c0db070b555158a0b` | `78d6362e36` |
| `diss/old-notes/Enriques Notes/2023-08-20.md` | `feab75c2f1ca755c302cb2c9684762d2f97c7e6e` | `a6f17ee94c` |
| `diss/old-notes/Enriques Notes/2023-08-22.md` | `d3dff4619e5d1c402e0f427925e89bed41dabf96` | `d51f597c84` |
| `diss/old-notes/Enriques Notes/2023-08-23 Compiled Meeting Notes.pdf` | `30ab7c59a1df76762d00d71d4a44b3efeb10be60` | `d70d53e509` |
| `diss/old-notes/Enriques Notes/2023-08-24 Zack-Luca meeting.md` | `f1ba443ed6412de56c555d4eb8c2849ab427e511` | `cf440eeaca` |
| `diss/old-notes/Enriques Notes/attachments/2023-08-01 Old Notes 2023-08-25 11.00.30.excalidraw.md` | `8bf9ccbc0e615e0bcde56393ffc1a330e09a80db` | `f5b7e76f33` |
| `diss/old-notes/Enriques Notes/attachments/2023-08-01 Old Notes 2023-08-25 11.06.13.excalidraw.md` | `281523028aa059c89c98e5fda5673e7d1a9b5915` | `7d3669a483` |
| `diss/old-notes/Enriques Notes/attachments/2023-08-01 Old Notes 2023-08-25 11.31.06.excalidraw.md` | `299de8a5375a52e525439e2372d1af9de8001227` | `a14b08a663` |
| `diss/old-notes/Enriques Notes/attachments/2023-08-01 Old Notes 2023-08-25 11.35.49.excalidraw.md` | `be76367205cbcb9557859814116530adc550bba4` | `aa84d694c0` |
| `diss/old-notes/Enriques Notes/attachments/2023-08-01 Old Notes 2023-08-25 11.38.29.excalidraw.md` | `8913296f6f760dae3f25a3ddb77251c6bcb08e14` | `8f8ac4adaf` |
| `diss/old-notes/Enriques Notes/attachments/2023-08-01 Old Notes 2023-08-25 13.21.59.excalidraw.md` | `88700249582d84606e51c2c308e230d752ec2ec7` | `893dabb4e9` |
| `diss/old-notes/Enriques Notes/attachments/2023-08-01 Old Notes 2023-08-25 13.33.48.excalidraw.md` | `5bcbaf3b5e9364ddca63f47c920339efbd2cdf30` | `1d9b344f3a` |
| `diss/old-notes/Enriques Notes/attachments/2023-08-01 Old Notes 2023-08-25 16.12.11.excalidraw.md` | `183e6189071f0ef71b82926a00fb1268596dff1d` | `0deeddd30f` |
| `diss/old-notes/Enriques Notes/attachments/Pasted image 20230819153854.png` | `c4a4ef663b98c702b6e8b59cef82b2838f0bd933` | `ac75a1cba5` |
| `diss/old-notes/Enriques Notes/attachments/Pasted image 20230821194826.png` | `a3a37e40a3f6a944f45cfc45c85978709ab6cf8d` | `e61e66cddd` |
| `diss/old-notes/Enriques Notes/attachments/Pasted image 20230821194835.png` | `fdc841ccf03a5b9f4edb2b2f624794e37227083b` | `ce63c6af7f` |
| `diss/old-notes/Enriques Notes/attachments/Pasted image 20230824135448.png` | `c117a569cf8ad5bed0a426a4505b15e76e188024` | `c5c5dfc6ad` |
| `diss/old-notes/Enriques Notes/attachments/Pasted image 20230824143638.png` | `64532353917d6440b5d927403f11c21a2521685d` | `ad6f888b0b` |
| `diss/old-notes/Enriques Notes/attachments/Pasted image 20230824150237 1.png` | `678eda3077d7c64a4472486fbc8e195eec4e254c` | `b391ac6776` |
| `diss/old-notes/Enriques Notes/attachments/Pasted image 20230824150237.png` | `678eda3077d7c64a4472486fbc8e195eec4e254c` | `361c2709de` |
| `diss/old-notes/Enriques Notes/attachments/Pasted image 20230824150239.png` | `678eda3077d7c64a4472486fbc8e195eec4e254c` | `0c316a838d` |
| `diss/old-notes/Enriques Notes/attachments/Pasted image 20230825114600.png` | `fc22dbc23f974f1df7ff0caad352b519ea74fd60` | `f77f648b23` |
| `diss/old-notes/Enriques Notes/attachments/Pasted image 20230825115623.png` | `0df09cb13786d6a5309fdaf0d50953767d3259cf` | `0790a7315c` |
| `diss/old-notes/Enriques Notes/attachments/Pasted image 20230825115735.png` | `5511064a4855a9735ece80c6658458428481dc3e` | `e0cafc831d` |
| `diss/old-notes/Enriques Notes/attachments/Pasted image 20230825115934.png` | `2d8bfe019b72be35b14c0be4fb0b120704ab8227` | `ccd5777ac7` |
| `diss/old-notes/Enriques Notes/attachments/Pasted image 20230825115942.png` | `177ef7d496437238223841ebe80c92a8cfcaf842` | `65ed937b74` |
| `diss/old-notes/Enriques Notes/attachments/Pasted image 20230825152319.png` | `6e37336d8a9eab3c8c68b5e5ec84eb6cf5218853` | `ba30c19f8b` |
| `diss/old-notes/Enriques Notes/attachments/Pasted image 20230825152557.png` | `eaea2f515325d96b2f7fbcebf351f002eee2a76e` | `cd9eaeeceb` |
| `diss/old-notes/Enriques Notes/attachments/Pasted image 20230825152728.png` | `9c6600610cbab63c413c75ac722bde8212cf17c6` | `59fa55d482` |
| `diss/old-notes/Enriques Notes/attachments/Pasted image 20230825153453.png` | `30433ceb74b09e5dcf968da9d193393088a56acf` | `1ecabbb085` |
| `diss/old-notes/Enriques Notes/preamble.sty` | `ebcd1cf70a0595583426abb27ae0242eaad679f8` | `8dd08009d4` |
| `diss/old-notes/Flashcards/000 Enriques Talk Facts 1.md` | `d0fb71ea3359d1bdfcad862626f550f1c82272ac` | `40db6882c3` |
| `diss/old-notes/Learning/2023-08-19.md` | `09dac0bab2414607bd2ce0a50e70922e269f6430` | `5a9235a2d1` |
| `diss/old-notes/Sterk91.md` | `232654e45300225e8e17075d42fbad876162bd9e` | `cfed3848cf` |

