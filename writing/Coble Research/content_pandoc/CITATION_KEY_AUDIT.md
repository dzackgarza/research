# Citation key audit — monograph consolidation

Every citation-key change made while consolidating "Coble Paper Draft" and "Coble Research" into `content_pandoc/`, with its evidence class.
The build bibliography is `~/zotero_global.bib` (symlinked as `global.bib`), supplemented by `../coble_supplement.bib`.

Evidence classes:

- **A — collision or exact-work match.** The project's own inline bibliography (`content_latex/main.tex`, `\begin{thebibliography}`) or `CoblePaper.bib` pins the key to a specific work (author+title+venue); the global bib holds that exact work under a different key, and in the collision cases holds a *different* work under the original key.
  Not remapping would cite the wrong paper.

- **B — twin restoration.** The pandoc port's automated key migration replaced a citation with an unrelated key; the LaTeX twin of the identical sentence preserves the original citation.
  The change restores the author's original.

- **C — version/edition drift.** The work is certain, but the global bib holds a later version/edition than the one the locators were written against.
  **Cited section/lemma/page numbers need verification against the published versions.**

- **D — judgment call.** The two serializations disagree or a key was overloaded; resolution chosen by content, flagged for author review.

| old key | new key | class | evidence |
| --- | --- | --- | --- |
| `Nik79` (this project) | `Nik80` | A | Project bibitem = *Integer symmetric bilinear forms…* (Izv. 43, 1979). Global `Nik80` = that work; global `Nik79` = *Finite groups of automorphisms of Kählerian K3 surfaces* (different paper). |
| `nikulin1979integer-symmetric` | `Nik80` | A | Same work, BBT-style key. |
| `Hor78` (this project), `Hor78b` | `Hor77` | A | Project bibitem = *On the periods of Enriques surfaces. II*, Math. Ann. **235** (1978). Global `Hor77` = Periods II; global `Hor78` = Periods I. |
| `Sha81` (this project) | `Sha81a` | A | Project bibitem = Shah, *Projective degenerations of Enriques' surfaces*, Math. Ann. **256**. Global `Sha81` = *Degenerations of K3 surfaces of degree 4* (different paper). |
| `Kol23` (this project) | `Kol23a` | A | Project bibitem = Kollár, *Families of varieties of general type*, Cambridge Tracts 231. Global `Kol23` = Kollár's Coble obituary. |
| `AD19` | `AD18` | A | Project bibitem = Allcock–Dolgachev, *The tetrahedron and automorphisms of Enriques and Coble surfaces of Hessian type*, arXiv:1809.07819 (2018). Global `AD18` exact. |
| `AE22nonsympinv` | `AE22` | A | CoblePaper.bib entry = Alexeev–Engel nonsymplectic-involution paper; global `AE22` exact. |
| `alexeev2023compact` | `AE23` | A | Project bibitem [AE23] = *Compact moduli of K3 surfaces*, Ann. of Math. 198 (2023); global `AE23` exact. |
| `alexeev2021nonsymplectic` | `AEH24` | A | Project bibitem [AEH21] = Alexeev–Engel–Han; global `AEH24` = the same authors' nonsymplectic-automorphism paper (published retitle *Complete*→*Compact*). No locators cited. |
| `alexeevCompactificationsModuliElliptic2023`, `alexeev2022compactifications-moduli` | `ABE22` | A | Alexeev–Brunyate–Engel, *…elliptic K3…: stable pair and toroidal*, Geom. Topol. 26 (2022); global `ABE22` exact. |
| `kiernan1972satake-compactification` | `KK72` | A | Kiernan–Kobayashi, Invent. Math. 16 (1972); exact. |
| `PSS71` | `PS71` | A | Piatetski-Shapiro–Shafarevich Torelli for K3 (1971); exact. |
| `kollar1988threefolds-and-deformations` | `KS88` | A | Kollár–Shepherd-Barron 1988; exact title in key and entry. |
| `deligne1969the-irreducibility-of-the-space` | `DM69` | A | Deligne–Mumford 1969; exact. |
| `knudsen1976the-projectivity-of-the-moduli` | `KM76` | A | Knudsen–Mumford, Projectivity I; exact. |
| `knudsen1983the-projectivity-of-the-moduli23` | `Knu83` | A | Knudsen, Projectivity II,III; global `Knu83` covers II,III (`Knu83a` = III alone). |
| `namikawa1976a-new-compactification-of-the-siegel1` | `Nam76` | A | Namikawa, new compactification of Siegel space I (1976); exact. |
| `alexeev1999on-mumfords-construction` | `AN99` | A | Alexeev–Nakamura 1999; exact. |
| `looijenga1985semi-toric` | `Loo85` | A | Looijenga, *Semi-toric partial compactifications I* (1985); exact. |
| `scattone1987on-the-compactification-of-moduli` | `Sca87` | A | Scattone 1987; exact. |
| `vinberg1985hyperbolic-groups` | `Vin85` | A | Vinberg, *Hyperbolic groups of reflections* (1985); exact. |
| `dolgachev2013the-rationality` | `DK13` | A | Dolgachev–Kondō rationality of Coble/nodal-Enriques moduli; exact. |
| `DM19` | `DM20` | A | Project bibitem = Dolgachev–Markushevich, *Lagrangian tens of planes…* arXiv:1906.01445; global `DM20` exact. (Where the *text* instead meant the unpublished Dolgachev lecture note, the URL footnote from the LaTeX source is used instead of any key.) |
| `AB21` (this project) | `ABE22` | A | **Collision found late.** knowledge/papers/AB21.md pins this project's `AB21` = Alexeev–Brunyate–Engel, *Compactifications of moduli of elliptic K3 surfaces* (2022); global `AB21` = Ascher–Bejleri (different paper). The first build cited the wrong work; fixed. |
| `AEGS23` | `AEGS25` | C | Same work (Alexeev–Engel–Garza–Schaffler), arXiv:2312.03638 → published *Compact Moduli of Enriques Surfaces of Degree 2* (2025). **Verify locators: Lem. 2.4, Rmk. 4.12, cusp-correspondence §§.** |
| `EnriquesOne`, `CDL24` | `CDL25` | C | Cossec–Dolgachev–Liedtke, *Enriques Surfaces I*, 2024 draft → published. **Verify locators: Def. 5.4.3, Eqn. 5.3.1, Table 5.1 (p. 553), Cor. 5.9.10, Prop. 5.46, Thm. 5.8.2, Rem. 5.9.12, p. 561, Ch. 5 §6.** |
| `EnriquesTwo`, `DK24` | `DK25` | C | Dolgachev–Kondō, *Enriques Surfaces II*, 2024 draft → published. **Verify locators: Prop. 9.1.1, 9.1.4, 9.1.5, 9.1.8, Ex. 9.1.7, Prop. 9.13, §3 (via Nue16 sentence), Table 5.1 uses.** |
| `AMRT75` | `AMRT10` | C | Ash–Mumford–Rapoport–Tai, 1975 → 2010 second edition. Cited without locators. |
| `Nue16` | `Nue15` | C | Nuer, *Unirationality…*; single global entry. **Verify locators: §3, p. 8.** |
| Halphen blowdown `Prop. 3.1` | `CDL25` | `CD12` | **VERIFIED**: CD12 extraction, Proposition 3.1 is the blowdown statement verbatim (index-2 Halphen; proper transform of the fiber; unique singular point). Not `CDL25`, not `DZ99`. |

## Whole-work substitutions, per instance

Every site where the *cited work* changed relative to the pandoc corpus, with its evidence.
The two serializations of this project disagree at several sites; the standing rule after review: **where content is decisive, the decisive reading wins; where it is not, the later (pandoc) serialization wins and the disagreement is recorded here** — earlier unilateral overrides in the non-decisive class have been reverted.

| file, site | pandoc had | now | evidence, status |
| --- | --- | --- | --- |
| Morrison_Flowerpot ×3, Coble_Moduli_Basics ×1 (flowerpot claims) | `Ols04` | `Mor81` | Decisive: section titled "Morrison's degenerations"; Lem 7.1/7.2, Cor 6.2 type (i.b), and the flowerpot terminology are Morrison 1981; LaTeX twin cites `Mor81`; knowledge stub Mor81.md exists. (Ols04.md also exists — Olsson is a real project reference, just not for flowerpots.) |
| Coble_Surface_Basics ×2 ("first studied in") | `Oda85` | `Cob29` | Decisive: LaTeX twin cites Cob29; no Oda85 stub exists; Coble surfaces were first studied by Coble (1919/1929). |
| Coble_Surface_Basics ×2 (Cremona special, §1.4 + "In [X] it is proved") | `CDL24` | `CD12` | Decisive: "Cremona special" is Cantat–Dolgachev's coinage and the unnodal-Halphen-or-Coble theorem is that paper's main result; both keys existed in the corpus vocabulary (stubs for each), so this is a content call, but a strong one. |
| Coble_Surface_Basics fn. + Rational_Sextic (genus formula "§3.1") | `CDL24` | `CD12` | **VERIFIED**: CD12's extraction has "3.1. From Coble to Halphen surfaces" opening with the p_a(C) computation. |
| Rational_Sextic (Hurwitz formula, Lem. 2.2) | `AS15` | `AD18` | **VERIFIED**: AD18's Lemma 2.2 proof contains the display 0 = 2K_X = 2(f*(K_S)+E) = f*(2K_S+C) verbatim; AS15 has no own Lemma 2.2 (only a citation to its ref [21]). The LaTeX (`AD19`) was right; the pandoc key and its knowledge stub were wrong. |
| Geometric ("§5.1" degeneration remark) | `Dol12` | `Dol17` | **VERIFIED**: Dol17 §5 = "Hyperbolic automorphisms of Coble surfaces", §5.1 = "Coble rational surfaces", containing the degenerating-involution passage verbatim. LaTeX right, pandoc + stub wrong. |
| IAS citation list | `AEGS23; AE22; AEGS23; AET23; Ols12` | `AEGS25; AE22; AE23; AET23; ABE22` | The literal duplication of AEGS23 marks the pandoc list as corrupted; LaTeX list (AEGS23, AE22, AE23, AET23, AB21) adopted with AB21 = ABE22 per the collision row above and AEGS23 = AEGS25 (class C). `Ols12` appears in no serialization's bibliography. |

Works with no global-bib entry — added to `../coble_supplement.bib` (should migrate to Zotero): `CD89` (Cossec–Dolgachev, Enriques Surfaces I, 1989 ed.), `Nik79b` (Nikulin, quotient-groups/2-reflections), `Mum65` (GIT), `Ale96` (M_{g,n}(W) for surfaces), `Ale02` (complete moduli, semiabelian action).

**`BHO+11` → `BHO+12`, RESOLVED** (class C, year drift). The work is
Blekherman–Hauenstein–Ottem–Ranestad–Sturmfels, *Algebraic boundaries of
Hilbert's SOS cones*, arXiv:1107.1846 (July **2011**) → Compositio Math. 148
(**2012**), doi 10.1112/S0010437X12000437; live Zotero `GJZ44LJI`, BBT key
`BHO+12`.
The alphabetic key encodes the arXiv year, the Zotero key the published year —
the same drift as the AEGS/CDL/DK rows, which is why a key-string search
missed it.
Its Theorem 2 is exactly the cited claim: the Severi variety of rational plane
sextics, whose general member has exactly 10 nodes (and those 10 nodes
uniquely determine the curve — directly relevant to the Coble construction).
Note the paper writes this variety $\mathcal{S}_{6,0}$; the monograph's
$V_{6,10}$ is our own $(d,\delta)$ notation.

**Provenance corrections after first full build**: `Ale96` and `Ale02` already exist in the global bib (the earlier absence check was defeated by brace-laden titles); the supplement copies were removed as duplicates.
Note the global `Ale96` is Alexeev, *Log canonical singularities and complete moduli of stable pairs* (alg-geom/9608013) — a sibling 1996 Alexeev paper to the *Moduli spaces $M_{g,n}(W)$ for surfaces* (Trento) paper the draft's key named.
Both are standard KSBA citations; if the Trento paper is specifically intended, add it to Zotero and re-point.

**Uncited works from the LaTeX inline bibliography** (curated but never cited in the text; not carried into the monograph's reference list): EF21, Eng18, Kul77, Ste91, Sym02 (`sterk1991…`, `symington2003…`), AT21 (`alexeev17ade-surfaces`), YZZ25. All except AT21 and YZZ25 exist in the global bib under those keys and can be cited directly when the Stable Limits sections are written.

## Verified against full-text extractions (live Zotero, 2026-07-23)

All disputes above and the class-C locators were checked against the markdown
extractions attached to the live Zotero items (the authoritative texts).

- **Confirmed verbatim sources**: AD18 Lem. 2.2 (Hurwitz display), Dol17 §5.1,
  CD12 §1.4 ("Cremona special point sets") and §3.1 ("From Coble to Halphen
  surfaces", including Prop. 3.1 = the blowdown lemma), DM20 §5.1 (the Coble
  definition, under "Degree 10 polarizations"), Cob19 §2 ("The Discriminant
  Conditions"), Mor81 (flower pot, Cor. 6.2 types, Lem. 7.1), Sha81a appendix
  (the flower/stalk/pot paragraph verbatim), KK72 Thm. 2 (extension to
  compactifications), Nue15 (ODP-degeneration passage), Nik80 (1.5.2/3.6.x),
  AE22 (Thm. 5.10, Prop. 5.5, Lem. 5.9, Prop. 5.13), AEGS25 (Lem. 2.4 unique
  embedding chain; Rmk. 4.12 Morrison comparison).
- **Renumbered in published versions (corrected in text)**: draft `DK24
  Prop. 9.13` -> published `DK25 Prop. 9.1.3` (terminal Coble of K3 type is
  basic rational, verbatim); draft `CDL24 Rem. 5.9.12` -> published `CDL25
  Thm. 5.9.8` (boundary of the Enriques Baily-Borel = Coble divisor + the two
  modular curves X_0(2), X). `CDL25 Cor. 5.9.10`, `Thm. 5.8.2`, `Prop. 5.46`,
  `Def. 5.4.3`, `Eqn. 5.3.1`, `Table 5.1`, and `DK25 9.1.1/9.1.4/9.1.5/
  9.1.7/9.1.8` all present in the published books.
- **Method correction**: the knowledge/papers stubs record the pandoc port's
  *intended* key per site, not ground truth — at two sites (AS15, Dol12) the
  stub-backed key was wrong and the LaTeX right; at others (Hor78 = Periods II,
  Nik79 = ISBF, AB21 = ABE) the stubs correctly witness collisions. Only the
  extraction texts decide.
- **BHO+11**: full-text search of the entire library (Severi variety, V_{6,10},
  nodal sextics) finds no B/H/O 2011 candidate; the work is not in Zotero.
  Still unresolved, still deliberately un-built.
