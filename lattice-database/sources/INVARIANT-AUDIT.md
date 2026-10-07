# Lattice invariant intake audit

This audit compares the source leads in [README.md](../README.md#sources-to-absorb) and [geometric intake](geometric/INTAKE.md) with the record schemas in [`model.py`](../src/latticedb/model.py), [`geometric.py`](../src/latticedb/geometric.py) and [`catalogues.py`](../src/latticedb/catalogues.py). It distinguishes available fields from source values that have not been imported. A source's group order is only meaningful after its group and action are identified.

The [group-data inventory](GROUP-DATA-INVENTORY.md) records the generator matrices, orders, indices, source locators and present coverage of the inspected Nebe–Sloane, LMFDB and Höhn–Mason material.

## `Shimada_86` source conflict

The [`Shimada_86` entry in the Nebe–Sloane union archive](https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/union.gz) prints a lower-triangular `GRAM` and a full `GRAM_MATRIX (in Maple)`. Exact arithmetic gives signature $(85,1)$ and determinant $-32571295334400$ for `GRAM`. The full matrix gives signature $(86,0)$ and determinant $196608=2^{16}3$, which agrees with the entry's `DET` field. The matrices first differ at $b(e_1,e_{11})$: `GRAM` prints $-8$, and `GRAM_MATRIX` prints $8$. The entry also states minimum $8$ and kissing number $109421928$; neither is an invariant of the indefinite form. The archive reader uses `GRAM_MATRIX` for this entry. Its lattice record and minimum and kissing-number checks remain to be added.

## Bulk catalogue source tables

These are source rows, including repeated presentations and twists. They are not a count of distinct isometry classes or of lattice records. The stored source files are read by `nipp.py`, `brandt_intrau.py`, `watson.py`, and `nebe_sloane.py`.
`latticedb bulk-index` writes the parsed Nipp, Brandt–Intrau–Schiemann, and Watson forms to `sources/normalized/`, with exact Gram determinants and source locators. It also indexes every named Nebe–Sloane union archive entry by ordinal and retains its source sections. These source rows still need identification with the corpus's lattice records.

| Published source | Source rows |
| --- | ---: |
| [Nipp quaternary forms](https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/nipp.html) | 74,075 |
| [Nipp quinary forms](https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/nipp5.html) | 45,560 |
| [Brandt–Intrau–Schiemann odd ternary forms](https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Brandt_1.html) | 5,453 |
| [Brandt–Intrau–Schiemann even ternary forms](https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Brandt_2.html) | 30,946 |
| [Watson single-class representatives](https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/Classi/watson) | 3,494 |
| [Nebe–Sloane union archive](https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/union.gz) | 823 |
| Total source rows | 160,351 |

The quinary table `tbl.256.html` prints a `D=113` block whose forms have Gram determinant $228$, while its stated discriminant convention gives $2D=226$. These forms repeat the following `D=114` block. The `D=113` genus-one header also gives a mass that does not equal the sum of reciprocal automorphism orders of the rows grouped under it. Keep the source rows and their locators; do not count the repeated presentation as a new lattice class.

## Orthogonal groups and their subgroups

The schema stores `definite.automorphism_group_order = |O(L)|` for a definite lattice and primitive-vector orbit counts for eight standard groups. `orthogonal-subgroups/` can name their generators, orders, indices, inclusions and stabilizers; source values still need intake. Its `O+` is the kernel of the **real spinor norm**; sources that use `O+` for a cone-preserving group need an explicit comparison. For an indefinite lattice, `O(L)` can be infinite. An index, finite image or stabilizer action can then be meaningful even when `|O(L)|` is not a finite number.

| Group or action | Stored result |
| --- | --- |
| `O(L)` for definite even `L` | Its finite order and generator morphisms when `integral.discriminant_sequence` has been certified. |
| `SO(L)`, `O+(L)`, `Otilde(L)` and their intersections | Primitive-vector orbit series; `orthogonal-subgroups/` holds named generators, order, index and parent when sourced. |
| Reflection subgroup `W(L)` | The `hyperbolic.reflective` Boolean and a distinct subgroup and chamber schema; source generators and indices remain to be entered. |
| Discriminant action `O(L) -> O(A_L,q_L)` for even `L` | The Gram matrix determines the map; `integral.discriminant_sequence` stores computed finite-group data for definite lattices. |
| A group fixing a vector, chamber, embedding or geometric polarization | `orthogonal-subgroups/` links generators to named self-isometries and identifies the stabilized object. |

The Gram matrix specifies the discriminant form and the canonical homomorphism $\rho_L:O(L)\to O(A_L,q_L)$: an isometry $g$ acts by $x+L\mapsto gx+L$. For a definite even lattice, PARI's `qfauto` supplies full generators of $O(L)$; [the Sage computation](../src/latticedb/sage_genus.py) stores them as self-isometry morphisms, stores their induced matrices in the discriminant basis, and enumerates the image and its pointed cosets. For an indefinite lattice, $O(L)$ may be infinite; the Miranda–Morrison local formula applies under its stated hypotheses without listing full generators. Hashimoto's [Table 10.2](https://arxiv.org/abs/1012.2682) states discriminant-form symbols, but the current [checker](../src/latticedb/hashimoto.py) compares their underlying abelian groups. For definite $L$, $|\widetilde O(L)|=|O(L)|/|\operatorname{im}\rho_L|$. The orders of $SO$, $O^+$ and their intersections depend on the joint determinant, spinor and discriminant action; multiplying separate indices is not generally valid.

For every nondegenerate even lattice, $MM(L)$ is the pointed coset set $O(A_L,q_L)/\operatorname{im}\rho_L$. Its distinguished point is the image subgroup; `mm_trivial` says this set has one point, equivalently that $\rho_L$ is surjective. Normality of the image is needed only to give the cosets a quotient-group law, and commutativity is needed to regard that group as a $\mathbb Z$-module. For an even indefinite lattice of rank greater than $3$, the [Miranda–Morrison exact sequence, as stated in Akyol–Degtyarev, Theorem 3.8](https://webdoc.sub.gwdg.de/ebook/serien/e/mpi_mathematik/2013/63.pdf), identifies this quotient with $\ker(E(L)\to\mathfrak g(L))$, an $\mathbb F_2$-vector space $(\mathbb Z/2\mathbb Z)^d$. Theorem 3.12 gives a local formula. The full group $E(L)$ equals $MM(L)$ only when $\mathfrak g(L)=1$.

| Intake source | Source claim | Current coverage and missing datum |
| --- | --- | --- |
| [Nebe–Sloane catalogue, `A14`](https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/A14.html); [Barnes–Wall `BW16`](https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/BW16.html) | `GROUP_ORDER`, `GROUP_NAME`, generator matrices; `BW16` also states `MODULAR = 2`. | `|O(L)|` has a definite-lattice field, and the Barnes–Wall record already holds its order. The [reader](../src/latticedb/nebe_sloane.py) transcribes none of these source group fields. The subgroup schema can hold structure and named generator morphisms; modularity requires `integral.modular_scale` and a checked dual-isometry morphism. The source values and witness remain to be entered. |
| [LMFDB lattice data](https://github.com/annahaensch/lattice_data) and its [level definition](https://www.lmfdb.org/knowledge/show/lattice.level) | Automorphism-group order, generators and structure; level; genus representatives; Hermite invariant and packing density. | The group schema, checked `integral.level` and `genera/` records provide the typed homes. Hermite and packing values are exact functions of rank, determinant and minimum. The LMFDB rows remain to be matched and imported. |
| [Höhn–Mason, §2 and Table 1](https://arxiv.org/pdf/1505.06420); [Hashimoto, Table 10.2](https://arxiv.org/abs/1012.2682) | Orders and generators of finite actions; orders of full pointwise stabilizers; indices of discriminant-action images; a normalizer quotient and its index in the fixed lattice's orthogonal group. | The [Höhn–Mason checker](../src/latticedb/hoehn_mason.py) already persists source generators and their induced action on the coinvariant record; it checks the generated order against Hashimoto. The source's discriminant-image indices and normalizer index are not transcribed in the inspected local entries. Höhn–Mason Lemma 2.2 identifies the **full pointwise stabilizer** of the fixed lattice with `Otilde` of the coinvariant lattice. |
| [Borcherds, Table −2](https://math.berkeley.edu/~reb/lattices/table2.html) and [Table −4](https://math.berkeley.edu/~reb/lattices/table4.html) | A stabilizer `G` of a vector in the Conway chamber, the root-reflection group `R`, and the group structure of `O(L)` in the stated cases. | The subgroup, vector-orbit and chamber schemas can identify these actions and their orders. Table −2 states that `O(L)` is a split extension of `R` by `G` for the even determinant-2 case. Table −4 states that `O(L)` has the form `2 × R.G` for its odd unimodular rank-25 lattice. The source values remain to be entered. |
| [Allcock rank-3 source header](https://github.com/MathieuDutSik/GeometryDatabase_Rank3_Lorentzian_lattices/blob/main/rk3.tex#L18-L33) | Gram forms, simple roots and enumeration fields `W` and `L`. | `chambers/` and `orthogonal-subgroups/` hold the mathematical data. `W` numbers a Weyl group in the source list; `L` numbers a lattice within that group. They are identifiers, **not** `|W|` or `[O(L):W(L)]`. The source identifiers remain to be matched. |

A source-defined subgroup $\Gamma\leq O(L)$ names its defining property or generators as lattice isometries, and its inclusion in $O(L)$. A vector, polarization, chamber or primitive embedding has its own stabilizer and names the object stabilized. A bare `#Gamma` field on a lattice would merge different groups that happen to have the same order.

## Other source claims

| Intake source | Schema and remaining intake |
| --- | --- |
| [Watson](https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/) and [Brandt–Intrau–Schiemann](https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/) | The class count is stored; `genera/` can hold cited representatives. The source rows remain to be matched. |
| [Jagy](https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/) | `definite.regular` and `definite.spinor_regular` hold the ternary predicates. Source claims remain to be entered. |
| [Kirschmer's tables](https://www.math.uni-bielefeld.de/~mkirschm/forms/) | Their lattices over rings of integers of number fields require a lattice kind over that base ring. They are not entries of the present integer-lattice kind without a named trace construction. |
| [King via Borcherds](https://math.berkeley.edu/~reb/lattices/) | The mass $\sum_{[M]\in\operatorname{Gen}(L)}1/|O(M)|$ belongs to a `genera/` record. |
| [Martinet's perfect lattices](http://jamartin.perso.math.cnrs.fr/Lattices/index.html) | `definite.minimal_vectors` and `definite.perfect` hold the configuration and its checked spanning predicate. |
| [Cohn's kissing bounds](https://cohn.mit.edu/kissing-numbers) | A bound is a claim about the kissing-number problem in a dimension. A lattice's kissing number already has a field. |
| [Delaunay polytopes of Niemeier lattices](https://github.com/MathieuDutSik/delaunaypolytopeniemeier.github.io) and [Sloane's packing files](https://neilsloane.com/packings/) | `lattice-polytopes/` can hold a Delaunay sphere tied to a metric lattice; `definite.minimal_vectors` holds a complete basis-aware minimal shell. |
| [Hyperkähler and surface sources](geometric/INTAKE.md#source-detail) | Hodge and characteristic numbers belong to geometric objects; cohomology actions, polarization orbits, moduli problems and local systems have separate typed records. Values remain to be sourced. |
| [Kreuzer–Skarke and ReflexivePolytopesDB](geometric/INTAKE.md#source-detail) | `lattice-polytopes/` stores vertex and polar data; `toric-varieties/` and geometric constructions link the associated varieties and families. |
| [Mainz and CYCluster](geometric/INTAKE.md#source-detail) | Operators, realizations, families and integral local systems have separate records; no operator has yet been imported. |

Scholl's and Schiemann's unavailable pages yield no further inspected claim in the present [source survey](../README.md#sources-to-absorb).

## SPLAG coverage

Conway–Sloane, *Sphere Packings, Lattices and Groups* (Zotero `T2WVLTDB`, with extraction) is not a stated source to absorb; the coverage below was audited record by record against Gram tensor, rank and determinant on 2026-10-05, not by name match.

| SPLAG family | Corpus status, verified |
| --- | --- |
| Root lattices $A_n$, $D_n$, $E_6,E_7,E_8$ | $A_1$–$A_{20}$, $D_4$–$D_{20}$, $E_6,E_7,E_8$ present with the correct determinants ($n+1$, $4$, $3,2,1$); duals $A_n^*,D_n^*,E_6^*,E_7^*$ present. $A_{21}^+$ and $D_{21}^+$ have no standalone record. |
| Laminated $\Lambda_n$ (Table 6.1) | $\Lambda_9$–$\Lambda_{20}$ and $\Lambda_{24}$ present with the table determinants (512, 768, 1024, 1024, 1024, 768, 512, 256, 256, 192, 128, 64, 1). $\Lambda_{21},\Lambda_{22}$ and SPLAG's $\Lambda_{23}$ are absent (`LAMBDA23d` is a different catalogue object: rank 23, determinant $2^{44}$, sparse card). $\Lambda_{25}$ and up absent. |
| The 24 Niemeier lattices | All 24 root systems present as rank-24 determinant-$1$ records, even where parity is stated. |
| $K_{12}$, $BW_{16}$, Leech family | $K_{12}$ present (rank 12, determinant $3^6$); $BW_{16}$ present (rank 16, determinant $2^8$) with its relatives; shorter Leech and Thompson–Smith (rank 248) present. Odd Leech absent. |
| Unimodular lattices | $E_8,D_{16}^+,D_{24}^+,E_8^2,E_8^3$ and $Z^n=I_{n,0}$ for $n=2$–$26$ present. Mordell–Weil lattices and $II_{25,1}$ have no record under any name searched. |
| Kappa lattices | Catalogue `KAPPA7/8/9` entries present as union-seeded cards. |

Seeded union cards duplicate full records with byte-identical Gram tensors: `N(A24)` twice (`029C`, `3HQ1`) and $A_1$ twice (`<2>`, `A1 (union:33)`). The other `N(...)`/`N(...) (union:...)` pairs follow the same seeding pattern and need the same Gram comparison. The corpus records a lattice once; a seeded card whose Gram equals a held record is not a second record.

## Remaining intake

1. Compute $MM(L)$ from the Gram matrix using the Miranda–Morrison local formula for nondegenerate even indefinite lattices of rank greater than $3$. Store its $\mathbb F_2$-dimension and `mm_trivial`. Keep $E(L)$ and the genus group distinct when the computation exposes them.
2. Import source generators, structures, orders and indices into named groups. Reuse isometry morphisms for lattice-action matrices.
3. Import reflection groups and chambers, genus masses and representative classes. Keep the distinct Borcherds formulas and Allcock identifiers as source-specific intake rules.
4. Import exact level, modularity with its dual isometry, and minimal-vector witnesses. Check source packing and Hermite decimals against exact formulas.

The schemas supply these mathematical owners. This audit does not import source numbers.
