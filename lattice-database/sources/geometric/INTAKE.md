# Geometric source intake

Each geometric record cites a primary mathematical source through `geometric-bibliography.bib`. Citation keys below use that file.
An online catalogue can supply candidate values and source leads.
Record its locator, verify the value against the cited theorem or computation, and retain the source citation in the record.

## Entry-point audit

These are the exact entry points supplied for this workstream.
A status describes only the inspection completed by 2026-10-03. Keep an entry when its data or mathematical interpretation is still unresolved.

| Entry point | Inspection status | Next audit |
| --- | --- | --- |
| <https://hyperkaehler.info/hodge/> | Hodge symmetry and family formula references inspected; sample K3 and hyperkähler records entered. | Check each further invariant against its cited theorem. |
| <https://www.grassmannian.info/> | HTML title and periodic-table content reached; no entries imported. | Inspect individual variety pages and their references. |
| <https://www.grassmannian.info/horospherical> | HTML content reached; no entries imported. | Resolve each construction and parameter set. |
| <https://superficie.info/> | Surface-geography tools and invariants surveyed; no entries imported. | Identify cited surface families and numerical sources. |
| <https://fanography.info/> | Fano-threefold catalogue fields surveyed; no entries imported. | Identify families by their constructions and source references. |
| <https://ahuchala.com/hodge/> | Page reached, but the browser-rendered mathematical content was not inspected. | Inspect the interactive content and its references. |
| <https://www.researchgate.net/publication/231022806_All_the_Hodge_numbers_for_all_Calabi-Yau_complete_intersections> | Paper identified through its [publisher DOI](https://doi.org/10.1088/0264-9381/6/2/006); configuration rows not imported. | Extract configuration matrices and the corresponding Hodge series from the paper. |
| <https://benjaminjurke.com/academia-and-research/calabi-yau-explorer/> | Manual inspected; explorer deactivated. The named Davies source list remains available. | Check further archives or author releases for the former MySQL tables. |
| <https://www.nikhef.nl/~t58/Site/Hodge_Numbers.html> | Hodge-pair positions and physical spectrum fields identified; no geometric objects imported. | Match a pair to a cited algebraic construction before intake. |
| <https://hep.itp.tuwien.ac.at/~kreuzer/CY/CYhome.html> | Catalogue navigation inspected; the [CY/4d page](https://hep.itp.tuwien.ac.at/~kreuzer/CY/CYcy.html) identifies raw polytope and Hodge files. | Preserve source identifiers while testing a small polytope specimen. |
| <https://cydb.mathematik.uni-mainz.de/about.php> | Operator and geometric-realization definitions inspected; no operator imported. | Link a specific operator to a sourced family and period. |
| <https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/ReflexivePolytopesDB/html/index.html> | Package access method and entry format inspected; no entry imported. | Compare a returned vertex matrix with the Kreuzer–Skarke source. |
| <https://cycluster.mpim-bonn.mpg.de/aesz.html> | Search page and [documented API](https://cycluster.mpim-bonn.mpg.de/api.html) inspected; one API record examined, none imported. | Reconcile its operator ID, formula and references with Mainz and primary literature. |

## Source detail

| Source | Observed material | Intake unit |
| --- | --- | --- |
| [Hyperkaehler.info](https://hyperkaehler.info/) and its [Hodge page](https://hyperkaehler.info/hodge/) | Hodge diamonds, the additional hyperkähler reflection, (K3^{[n]}) and (mathrm{Kum}^{n}) formula references, BBF forms, Chern numbers, Betti numbers, local deformation dimensions, automorphism groups, monodromy, Riemann–Roch polynomials and polarization data | Cite the original results for each instance. Add characteristic numbers and group-valued invariants at their mathematical type before importing more values. |
| [Grassmannian.info](https://www.grassmannian.info/) | A periodic table of generalized Grassmannians with dimension, index, Euler characteristic, quantum cohomology and exceptional-collection data | Give each homogeneous variety a defining group and parabolic datum; cite the source of each numerical invariant. |
| [Grassmannian.info: horospherical varieties](https://www.grassmannian.info/horospherical) | Rank-one horospherical varieties with dimension, index and Euler characteristic | Retain the horospherical construction and its parameters with each object. |
| [Le superficie algebriche](https://superficie.info/) | Surface geography by (c_1^2), (c_2) and Kodaira dimension; Hodge, Betti, Euler and Chern data with references | Reconcile the named surface classes with geometric families and individual instances. |
| [Fanography](https://fanography.info/) | Fano threefold families with Picard rank, anticanonical degree, (h^{1,2}), index, descriptions, (mathrm{Aut}^0) and moduli data | Keep each construction and family identifier; complete the Hodge series from cited mathematics. |
| [Huchala's Hodge tool](https://ahuchala.com/hodge/) | Interactive Hodge resource | Inspect its dynamically rendered statements and sources before choosing data fields or imports. |
| [Green–Hübsch–Lütken, 1989](https://doi.org/10.1088/0264-9381/6/2/006) | Hodge numbers of Calabi–Yau complete intersections in products of projective spaces | Retain each configuration matrix and its Hodge series. The paper reports distinct diamonds, so a diamond alone does not identify a geometric object. |
| [Jurke's Calabi–Yau explorer](https://benjaminjurke.com/academia-and-research/calabi-yau-explorer/) and [Davies's source lists](https://www.rhysdavies.info/physics_page/resources.html) | The explorer is deactivated. Its manual identifies Davies's Hodge-pair list as its original data. Davies publishes [pairs with reference keys](https://www.rhysdavies.info/physics_page/hodge_nums/hodge_list_1), a second ordering and a companion reference list. | Read the source list and resolve its reference keys to the cited construction. A Hodge pair is an index into constructions, not an object identifier. The archive availability API returned no snapshot for `cyexplorer.bjurke.net`; the explorer's MySQL tables were not recovered. |
| [NIKHEF Hodge number tables](https://www.nikhef.nl/~t58/Site/Hodge_Numbers.html) | Gepner and free-fermion model spectra; the first two entries of each tuple are named $h^{1,1}$ and $h^{1,2}$. Its comparison section takes the 30,108 toric hypersurface Hodge pairs from Kreuzer–Skarke. | The listed physical spectrum is a source lead only. Attach a Hodge pair to a geometric record after identifying a smooth projective variety and a mathematical construction; do not treat multiplicities, singlets, vector bosons or world-sheet supersymmetry as geometric invariants. |
| [Kreuzer–Skarke CY/4d data](https://hep.itp.tuwien.ac.at/~kreuzer/CY/CYcy.html) | Complete four-dimensional reflexive-polytope list in vertex-count gzip files and Parquet; separate Hodge-pair files; a weight-system file with Hodge, lattice-point, vertex and K3-fibration data [@KreuzerSkarke2002Classification; @KreuzerSkarke2002Fibrations]. | Use the polytope and its ambient lattice as one record, with vertices and polar dual. Relate it to the toric variety and the family of anticanonical hypersurfaces. Keep the source's polytope identifier, weight system, Hodge pair and fibration datum with that relation. |
| [Macaulay2 ReflexivePolytopesDB](https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/ReflexivePolytopesDB/html/index.html) | `kreuzerSkarke(h11,h21)` returns Kreuzer–Skarke entries with descriptions and vertex matrices; a small subset ships for offline use. | Use the package as a reader and specimen source for the original polytope list. Check the returned vertex matrix and header against the source entry before linking its associated Hodge pair. |
| [Mainz Calabi–Yau operator database](https://cydb.mathematik.uni-mainz.de/about.php) | Fourth-order differential operators, Riemann symbols and descriptions of geometric realizations. Its B-incarnation is a one-parameter family whose Picard–Fuchs operator has the listed operator as a factor. | Record an operator and its coordinate/normalization separately from each realized family. A proposed geometric origin is a cited relation with its own evidence. |
| [CYCluster AESZ catalogue and API](https://cycluster.mpim-bonn.mpg.de/api.html) | A machine-readable `operators` table gives operator coefficients, singularities, exponents, characteristic numbers, descriptions and references. The documented query `nn=eq.4.3.1` returns one entry. | Cross-reference operator identifiers with Mainz and primary sources. Keep the operator, family, variation of Hodge structure and monodromy representation as distinct records or relations. |

## Mathematical lead audit

| Lead | Present record or outstanding owner |
| --- | --- |
| Hodge–Poincaré series, Hodge diamond, Betti numbers and Euler characteristic | Sparse series is stored on geometric objects; the other values are derived from it. |
| Diamond symmetry group | `V4` or `D4` is checked against the stored coefficients. Further claimed group actions require their own representation. |
| Geometric families and instances | Parameterized K3 Hilbert schemes and generalized Kummer varieties have family records and linked dimension-four instances. Homogeneous, horospherical, complete-intersection and toric constructions have typed fields for future intake. |
| Theoretical Hodge formulas | Göttsche and Göttsche–Soergel are cited for the two hyperkähler families. A general family-level series computation has not been authored. |
| Complex dimension and local deformation dimension | Both are object fields. A polarized or global moduli-space dimension needs its own moduli problem and source. |
| $H^2(X;\mathbb Z)$ and Beauville–Bogomolov–Fujiki form | Tagged lattice links name the degree, pairing and scale for entered examples. |
| Chern and other characteristic numbers | Top-degree Chern and Pontryagin products are stored and checked for degree; a stated top Chern number is checked against Euler characteristic. Riemann–Roch polynomials have exact rational coefficients. Other characteristic-class conventions need source-specific normalization. |
| $\operatorname{Aut}^0(X)$, homotopy groups and other group invariants | The geometric schema names the algebraic group and each homotopy degree; a cohomology action can link to a named lattice subgroup. No such values have been imported. |
| Reflexive lattice polytopes and polar duals | `lattice-polytopes/` names ambient rank, vertices, reflexivity and a polar record. Reflexivity belongs to that record, not to a Hodge diamond. |
| Toric varieties and Calabi–Yau hypersurfaces | `toric-varieties/` and typed geometric constructions link a polytope, toric ambient variety and anticanonical hypersurface. A shared Hodge pair does not identify any of them. |
| Fibrations, Picard–Fuchs operators and monodromy groups | `geometric-maps/` names the map, `picard-fuchs-operators/` names coordinate and period realizations, and `integral-local-systems/` names the monodromy matrices. Source links remain to be authored. |
| Source tools and visualizations | Hodge plots and interactive source pages are retained as discovery and presentation leads. Their numerical claims require the same cited identification as a table row. |

The Hodge series determines Betti numbers and the topological Euler characteristic.
A BBF form or another bilinear form requires its own named pairing and lattice link.
A Chern number requires a top-degree monomial in the tangent bundle's Chern classes.
A local deformation dimension is distinct from the dimension of a polarized moduli space.
An automorphism group, monodromy group or homotopy group needs a group-valued record rather than an untyped label.

## Polytope and family boundary

A lattice polytope is a bounded convex hull of finitely many points in a lattice $M$.
A full-dimensional lattice polytope with the origin in its interior is reflexive when its polar is a lattice polytope in $M^\vee$.
The vertex matrix, ambient lattice and polar relation are its defining data.
Dimension, lattice-point counts and reflexivity belong to the polytope.
A toric variety and a smooth Calabi–Yau hypersurface obtained from it are other objects, with their own construction and Hodge data.
Kreuzer and Skarke classified 473,800,776 four-dimensional reflexive polytopes; this is a count of polytope classes, not of pairwise distinct Calabi–Yau threefolds [@KreuzerSkarke2002Classification].

A fibration is a map from a total space to a base, with a stated generic fiber and singular locus.
Its monodromy acts on a specified local system over the smooth base.
A Picard–Fuchs operator is attached to a period of a variation of Hodge structure, with a coordinate and normalization.
Different families can realize the same operator; a Riemann symbol gives local exponents and does not by itself specify the global monodromy representation.
The source relation must identify the family, map, local system and operator before a monodromy group can be attached to a geometric record.

`lattice-polytopes/` stores polytope vertices and polar links separately from `toric-varieties/` and geometric objects. `geometric-maps/` stores fibrations, while `picard-fuchs-operators/` links an operator to each cited family realization. `integral-local-systems/` stores monodromy on a specified cohomology group. Source entries still need intake and verification.
