# Lattice database

A catalogue of lattices.
A *lattice* here is a free module $L$ of finite rank over $\mathbb{Z}$ with a symmetric bilinear form $b \colon L \times L \to \mathbb{Q}$.
The form can be definite, indefinite or degenerate, and its values need not be integers.

Each lattice has one Markdown file, `lattices/<TAG>.md`. The YAML front matter of the file is the record of the lattice; the body is prose about it.
The build validates every record, writes one page for each lattice, and writes one table, with one row per record, that the database page filters, sorts and exports.

The site is served locally at <http://lattice-database.localhost/>, and published at <https://dzackgarza.github.io/research/lattice-database/> by `.github/workflows/docs.yml`, which deploys it beside the docs book.

## Layout

| Path | Contents |
| --- | --- |
| `lattices/<TAG>.md` | One record and its prose for each lattice |
| `geometric-objects/<slug>.md` | One geometric object, its Hodge–Poincaré series, optional cohomology lattice links and cited prose |
| `geometric-families/<slug>.md` | One parameterized geometric family and its cited prose |
| `orthogonal-subgroups/`, `vector-orbits/`, `chambers/` | Named lattice group actions, primitive-vector orbits and hyperbolic chambers |
| `genera/` | Genus records with representative isometry classes and mass |
| `lattice-polytopes/`, `toric-varieties/` | Based lattice polytopes, polar duals and normal-fan toric varieties |
| `geometric-maps/`, `moduli-problems/` | Geometric maps, fibrations and specified moduli problems |
| `integral-local-systems/`, `picard-fuchs-operators/` | Integral monodromy and period operators with geometric realizations |
| `morphisms/dual/` | Isometries $L\to L^*(k)$ in the basis dual to the lattice record |
| `geometric-bibliography.bib` | BibTeX entries cited by geometric object and family prose |
| `families.yaml` | Every family that a record may name, with one line of its meaning |
| `retired-tags.yaml` | Every tag whose record the corpus no longer admits, with the lattice that was there and the twist of a record that it is |
| `morphisms/<S>-<T>.md` | Morphisms from the lattice `S` to the lattice `T`, as matrices, and prose |
| `pages/<slug>.md` | One collection page: conditions on the database rows, and prose |
| `theory/<slug>.md` | One theory page: the definitions and conventions that the other pages link to |
| `src/latticedb/model.py` | The schema of a record and of a morphism file, and their validators |
| `src/latticedb/geometric.py` | The schema of geometric families, objects and their Hodge–Poincaré series |
| `src/latticedb/catalogues.py` | Schemas of group actions, genera, polytopes, toric varieties, maps, local systems and operators |
| `src/latticedb/arithmetic.py` | Exact arithmetic on the Gram tensor that the validators use |
| `src/latticedb/root_systems.py` | The types of the irreducible root systems, their Cartan data and the lattices that they generate |
| `src/latticedb/roots.py` | $\Phi(L)$ of a definite lattice as its irreducible components; roots that generate $\mathbb{Z}\Phi(L)$ for the others |
| `src/latticedb/records.py` | Computes the fields of a record that the Gram tensor determines, and writes a record as a file |
| `src/latticedb/nebe_sloane.py` | Reads an entry of the Catalogue of Lattices (G. Nebe, N. J. A. Sloane) and writes it as the declared fields of a record |
| `src/latticedb/hashimoto.py` | Reads Tables 10.2 and 10.3 of Hashimoto, the finite symplectic groups of the K3 lattice, checks every equation they state against the records, and checks that the morphism files embed each $\Lambda^G$ and its $\Lambda_G$ in the K3 lattice as orthogonal primitive sublattices |
| `src/latticedb/hoehn_mason.py` | Reads the coinvariant lattices of the Leech lattice of Höhn and Mason, computes their inclusions in the Leech lattice and the actions of their stabilizers, and checks them against the records, Table 10.2 of Hashimoto and the morphism files |
| `src/latticedb/genus.py`, `sage_genus.py` | Computes the genus symbol, the class number of the genus and the order of $O(L)$ with SageMath, and stores them in the records |
| `src/latticedb/corpus.py` | Reads all records and checks the statements that concern more than one record |
| `src/latticedb/site.py` | Builds the site |
| `src/latticedb/templates/`, `assets/` | Page templates, styles and the database script |
| `sources/nebe_sloane/union.gz`, `<ENTRY>.json` | The catalogue's standard-format union archive and stored entries read from it or from individual pages |
| `sources/hashimoto/table_10_2.json`, `table_10_3.json` | Tables 10.2 and 10.3 of K. Hashimoto, arXiv:1012.2682, as printed, each row linked to the records of $\Lambda_G$ and $\Lambda^G$ by a twist and a change of basis |
| `sources/hoehn_mason/leech.json`, `lattices_<i>_<j>.json` | The Leech lattice and the 40 entries `lattices[i,j]` of the Magma file of G. Höhn and G. Mason, arXiv:1505.06420, whose coinvariant lattice is $\Lambda_G(-1)$ for a row of Table 10.2 of Hashimoto: the bases and the stabilizer generators as printed, each linked to its record by a twist and a change of basis |
| `tests/` | Tests of the validators, of the record commands and of the built site |

## Geometric objects

Each file in `geometric-objects/` describes a smooth connected projective complex variety or a class whose stated invariants are constant.
Its file name is its permanent slug.
`hodge_poincare` stores the nonzero terms of $H_X(u,v)=\sum_{p,q}h^{p,q}u^pv^q$, where $h^{p,q}=\dim_{\mathbb C}H^q(X,\Omega_X^p)$.
Each term has `p`, `q` and a positive `coefficient`; omitted terms have coefficient zero.
The record checks unique terms, exponents at most `dimension`, $h^{0,0}=1$, Hodge symmetry and Serre duality.
It derives Betti numbers and the Euler characteristic from the series.
The optional `symmetry_group` declares the full square symmetry group of the Hodge diamond: `V4` or `D4`. The record checks this declaration against the coefficients.

`geometric-families/` holds parameterized families.
An instance names its `family` slug and integer `family_parameter`; the corpus checks that the family exists and that the parameter meets its minimum.
Each instance retains its own Hodge series.
`local_deformation_dimension` records the dimension of an unobstructed local complex deformation space.
`chern_numbers` stores top-degree products of tangent-bundle Chern classes as ordered `indices` and an integral `value`; the record checks their degree and checks a stated top Chern number against the Euler characteristic.

An optional `cohomology_lattices` entry identifies $H^k(X;\mathbb Z)$ modulo torsion with a tagged lattice, under the named pairing and integer scale.
The build checks that the tag exists and that its rank is $b_k = \sum_{p+q=k} h^{p,q}$.
The pairing names the form: the Hodge numbers alone do not determine it.
The geometric object page links to the lattice page, and the lattice page links back.

```yaml
slug: k3-surface
name: Complex projective K3 surface
dimension: 2
hodge_poincare:
- {p: 0, q: 0, coefficient: 1}
- {p: 0, q: 2, coefficient: 1}
- {p: 1, q: 1, coefficient: 20}
- {p: 2, q: 0, coefficient: 1}
- {p: 2, q: 2, coefficient: 1}
symmetry_group: D4
local_deformation_dimension: 20
chern_numbers:
- {indices: [2], value: 24}
cohomology_lattices:
- degree: 2
  pairing: the cup-product intersection form
  tag: 027E
  scale: 1
```

The body of each geometric file is Pandoc Markdown.
Cite BibTeX keys from `geometric-bibliography.bib` with Pandoc citation syntax such as `[@Huybrechts2016K3]`. The site lists families and objects at `geometric-objects.html` and serves their pages under `geometric-families/` and `geometric-objects/`.

## Related mathematical records

Each additional catalogue uses one Markdown file per permanent slug. Its front matter is validated by `latticedb check`; its body states the source and mathematical identification. These records remain distinct from the lattice, geometric object and geometric family records they link.

| Catalogue | Defining data and links |
| --- | --- |
| `orthogonal-subgroups/` | A lattice tag, a defining property or named self-isometry generators, optional relators, abstract structure, order, index and parent subgroup. A stabilizer names its vector orbit, chamber or geometric object. `O+` means the kernel of the real spinor norm. |
| `vector-orbits/` | A primitive vector in the record basis, its square and optional divisibility, the acting subgroup, and optional geometric polarization link. The Gram tensor checks the square and divisibility. |
| `chambers/` | A hyperbolic lattice, interior vector and oriented wall normals, with an optional reflection subgroup. |
| `genera/` | Signature, determinant, parity, genus symbol, representative lattice tags, class number, completeness and rational mass. A complete list with known group orders checks $\sum 1/|O(L_i)|$. |
| `lattice-polytopes/` | Vertices in a based free abelian group, ambient rank, source identifier, reflexivity, polar dual, and optional Delaunay sphere tied to a quadratic lattice. A toric ambient lattice is not the quadratic lattice of a lattice record. |
| `toric-varieties/` | A polytope and its normal fan, with optional subdivision rays. |
| `geometric-maps/` | Source and target geometric records; a fibration also names its generic fiber and can state its singular locus. |
| `moduli-problems/` | A family, moduli dimension, optional polarization orbit and arithmetic subgroup. |
| `integral-local-systems/` | A fibration over a smooth base, its source family, cohomological degree and rank; optional integral fiber lattice and matrices of monodromy around named loops. |
| `picard-fuchs-operators/` | Exact rational polynomial coefficients of $\sum_i a_i(x)(x\,d/dx)^i$, coordinate, normalization, singularities and exponents; each realization names a family, period and relation to the operator. |

`morphisms/dual/<slug>.md` records a matrix $M$ for $L\to L^*(k)$ in the dual basis. Its validator checks $M\in GL_n(\mathbb Z)$ and $M^{\mathsf T}(kG^{-1})M=G$. The lattice's `integral.modular_scale` names the same $k$ and requires such a morphism. `integral.level` is the least $k$ for which $k b(x,x)$ is even on $L^*$; the validator computes it from $G^{-1}$. They are different invariants.

`definite.minimal_vectors` is a complete shell in the record basis and must match the minimum and kissing number. `definite.perfect` is checked by the span of their rank-one tensors. `definite.regular` and `definite.spinor_regular` apply to integral ternary lattices. The Hermite invariant and packing density are exact functions of rank, determinant and minimum; source decimals are checked against those formulas rather than stored as exact values.

Geometric objects can also store Pontryagin numbers, a Beauville–Bogomolov Riemann–Roch polynomial, $\operatorname{Aut}^0$, homotopy groups, Fano and surface data, and a homogeneous, horospherical, Calabi–Yau complete-intersection or toric anticanonical construction. A complete-intersection configuration stores its projective factors and equation multidegrees; the schema checks the Calabi–Yau degree and dimension equations.

## A record

```yaml
---
tag: '0016'
name: U
latex: U
aliases: ['II_{1,1}']
rank: 2
gram_tensor:
- [0, 1]
- [1, 0]
signature: [1, 1]
determinant: -1
definiteness: indefinite
integral:
  parity: even
  discriminant_group: []
  overlattice_count: 1
  genus_symbol: II_{1,1}
indefinite:
  isotropic: true
families: [even-unimodular]
---

$U$ is the lattice with basis $e, f$ and $b(e, e) = b(f, f) = 0$, $b(e, f) = 1$.
```

`gram_tensor` is the defining datum: the components $b(e_i, e_j)$ of the Gram tensor $b$, a symmetric $(0,2)$-tensor, in a basis $e_1, \dots, e_n$ of $L$.
A component is an integer or a string `p/q`. Floats are refused.

The corpus records a lattice once, up to twist and sign.
For an integer $n$, the twist $L(n)$ is the module of $L$ with the form $nb$.
A Gram tensor that is $n$ times a Gram tensor with integer components for some $n \geq 2$, or that is zero, is refused: the lattice is $M(n)$ for the lattice $M$ with Gram tensor $b/n$, and the corpus records $M$.
So $\langle 1 \rangle$ is a record and $A_1 = \langle 1 \rangle(2)$ is not; $E_8$ is a record and $E_8(2)$ is not.
The one exception is the 13 rows $a = r$ of Table 1 of Nikulin (J. Soviet Math.
22 (1983)), the family `nikulin-two-elementary`: each row is a twist $M(2)$ of a unimodular record $M$, and each is a record, because the classification names the twist and not $M$.
`latticedb new` admits a twist by 2 in that family and no other twist.
Of $L$ and $L(-1)$ the corpus records one: the one with $b(x, x) \geq 0$ for all $x$ when $b$ is definite or semidefinite, and the one with signature $(n_+, n_-)$, $n_+ \leq n_-$, when $b$ is indefinite.
So $E_8$ is a record and $E_8(-1)$ is not, and $U \oplus E_8(-1)$, of signature $(1, 9)$, is a record.
A twist that a construction names is written as a summand with its scale, in the name and in `root_span.summands`: the root sublattice of $U$ is $\langle 1 \rangle(2) \oplus \langle 1 \rangle(-2)$, named `<2> + <-2>`.

The fields of a record are of two kinds.
The Gram tensor determines `rank`, `signature`, `determinant`, `definiteness`, `integral.parity`, `integral.discriminant_group`, `integral.overlattice_count`, `integral.delta`, `integral.bad_reduction_primes`, `integral.quadratic_character`, `definite.minimum`, `definite.kissing_number`, `definite.theta_series`, `definite.root_system`, `definite.roots`, `indefinite.isotropic`, `root_span.norms` and `root_sublattice`. `latticedb new` and `latticedb nebe-sloane` compute them once, with exact arithmetic, when they write the record.
`latticedb new` refuses a Gram tensor that is not symmetric or is a twist, a declared value that is false, and a definite lattice isometric to a record of the corpus.
The build reads the stored values and computes nothing again.
A person writes `name`, `latex`, `aliases`, `families`, `related`, `references` and the prose.
`latticedb certify` computes `integral.genus_symbol`, `integral.genus_class_count` and `integral.hyperbolic_index` with `Genus` of SageMath, `integral.spinor_genus_count` and `integral.spinor_genera` of a lattice of rank at least 3 with `Genus` and the neighbour method of SageMath (`theory/overlattices.md`), `definite.automorphism_group_order` with `qfauto` of PARI/GP, and `integral.primitive_orbits` through $z^4$ and $w^4$, of a definite lattice with `qfauto` and `qfminim` and of an even lattice of hyperbolic index at least 2 from its discriminant form (`theory/orbits.md`), under SageMath. For a definite even lattice it also computes `integral.discriminant_sequence`: PARI `qfauto` supplies generators of $O(L)$, SageMath supplies generators of $O(A_L,q_L)$, and the induced matrices determine the image, kernel order, and pointed coset quotient. The lattice generators are stored as self-isometries in `morphisms/<tag>-<tag>.md`. It writes each value that a record does not hold, and refuses a stored value that differs from the computed one; a series of orbits merges coefficient by coefficient with the stored one, and a person states the coefficients of any other indefinite lattice with a `reference` that proves them; a value that SageMath does not compute within the time limit is not written.
`hyperbolic.reflective` and a `root_span` block that `latticedb new` could not decide are declared: the prose states the source of each one, and the page of the lattice marks `hyperbolic.reflective` *declared*.

An invariant that exists only under a hypothesis lives in a block named for the hypothesis.
A block on a lattice that does not satisfy the hypothesis is a validation error, and so is a field whose own hypothesis fails.

| Block | Hypothesis on the lattice | Fields |
| --- | --- | --- |
| `integral` | every $b(e_i, e_j)$ is an integer | `parity`, `level`, `modular_scale`, `discriminant_group`, `discriminant_sequence`, `overlattice_count`, `delta`, `bad_reduction_primes`, `quadratic_character`, `genus_symbol`, `genus_class_count`, `spinor_genus_count`, `spinor_genera`, `hyperbolic_index`, `primitive_orbits` |
| `definite` | $b$ is positive or negative definite | `minimum`, `kissing_number`, `minimal_vectors`, `perfect`, `regular`, `spinor_regular`, `automorphism_group_order`, `theta_series`, `root_system`, `roots` |
| `root_span` | $b$ is not definite | `roots`, `norms`, `summands`, `embedding` |
| `root_sublattice` | $b$ is definite, or the record has `root_span` | `invariant_factors`, `norms` |
| `indefinite` | $b(x, x)$ takes both signs | `isotropic` |
| `hyperbolic` | $b$ is nondegenerate with signature $(1, n)$ or $(n, 1)$, rank at least 2 | `reflective` |

The `integral`, `definite`, `indefinite` and `root_sublattice` blocks are required when their hypotheses hold; `root_span` and `hyperbolic` are optional.
`definite.theta_series` and `definite.root_system` are required exactly when the lattice is integral, and `definite.automorphism_group_order`, `integral.discriminant_sequence`, `integral.genus_symbol`, `integral.genus_class_count`, `integral.spinor_genus_count`, `integral.spinor_genera`, `integral.hyperbolic_index` and `integral.primitive_orbits` are optional. `integral.discriminant_sequence` records a pointed coset set for every definite even lattice on which it is computed. It records a quotient multiplication table only when the image of the discriminant action is normal.
`integral.primitive_orbits` maps each of `O`, `SO`, `O+`, `SO+`, `Otilde`, `SOtilde`, `Otilde+` and `SOtilde+` to the coefficients `constant`, `z` and `w` of the series $F_{L,\Gamma}(z, w)$ of the numbers of $\Gamma$-orbits of primitive vectors of each norm, null where a coefficient is not known (`theory/orbits.md`).

`integral.overlattice_count` is the number of integral lattices $M$ with $L \subseteq M \subseteq L^*$, with $M = L$ counted.
A lattice $M \supseteq L$ of finite index is integral exactly when $H = M/L$ is a subgroup of the discriminant group $A_L = L^*/L$ on which the form $b_{A_L}(x + L, y + L) = b(x, y) + \mathbb{Z}$ vanishes, so the field is the number of those subgroups.
It counts subgroups, not their orbits under the isometries of $L$, and it counts every integral $M$: for an even $L$ some $M$ can be odd.
For $U(2)$ the count is 4, and 3 of the 4 lattices are even.
The record commands enumerate the subgroups of $A_L$, so the field is stated exactly when the determinant is not zero and $A_L$ has at most 100000 subgroups.
A record without it is not decided, and its page says so: $(\mathbb{Z}/2)^8$ has 417199 subgroups.

`integral.delta` is Nikulin's invariant $\delta$ of an even lattice with $2 A_L = 0$, and it is required for exactly those lattices, $A_L = 0$ included: 0 when $b(x, x)$ is an integer for every $x$ in $L^*$, and 1 otherwise.
With the rank $r$ and $A_L \cong (\mathbb{Z}/2)^a$ it gives Nikulin's $(r, a, \delta)$.
Because $2 L^* \subseteq L$, every $2 b(x, y)$ with $x, y \in L^*$ is an integer, so $\delta = 0$ exactly when every diagonal entry of $G^{-1}$ is an integer.

`integral.bad_reduction_primes` is the set $\Sigma_L$ of primes that divide $2 \det L$, required exactly when the determinant is not zero.
`integral.quadratic_character` is, for rank $2m$ and a nonzero determinant, the discriminant of $\mathbb{Q}(\sqrt{D})$ with $D = (-1)^m \det L$, and 1 when $D$ is a square.
With the rank and the determinant they give the zeta functions of the quadrics $Q(x) = n$ outside $\Sigma_L$ and the primes that divide $n$ (`theory/zeta.md`).

`fields.html` is generated from `model.py`.

The fields that a person writes follow these conventions:

| Field | Convention | Examples |
| --- | --- | --- |
| `name` | Plain text, as the lattice is written on a blackboard: `+` for the orthogonal sum, `^n` for a power, `*` for the dual lattice, `(k)` for the form scaled by $k$, `<a>` for the rank-one lattice with $b(e, e) = a$ | `E8`, `A3*`, `U + E8(-1)`, `E8^2 + A1`, `<2> + <-2>`, `I_{1,3}`, `I_{11,0}`, `affine D5`, `Lambda10` |
| `latex` | The same name as TeX, without `$` | `E_{8}`, `A_{3}^{*}`, `U \oplus E_{8}(-1)`, `\langle 2 \rangle`, `\mathrm{I}_{1,3}`, `\mathrm{I}_{11,0}`, `\widetilde{D}_{5}`, `\Lambda_{10}` |
| `aliases` | Other names in the literature and the names of the same lattice in other conventions, each as plain text; the name of the entry when the source is a catalogue | `II_{4,4}`; `LAMBDA16`, `BW16`, `Barnes-Wall lattice`; `(r, a, delta) = (15, 7, 1)` |
| `families` | Keys of `families.yaml`. A family is a class of lattices that a definition cuts out, not a property that the build derives from the record: `even-unimodular` is a family because its members are a named series, and *unimodular* is a property. To add a family, add its key and one line of meaning to `families.yaml` in the same change as its first member; the build rejects a record whose family is not listed | `irreducible-root-lattice`, `laminated`, `r-plus-a-22` |
| `related.relation` | One sentence that states the related lattice in terms of \(L\): the map or the change of form; TeX between `\(` and `\)` | `The dual lattice \(L^*\).`; `The same module with the form \(-b\).`; `The same module with the form \(2b\).` |
| `references.citation` | Author initials and surnames, the title, and the locator that the source uses; with `url` when the source is on the web | `G. Nebe and N. J. A. Sloane, Catalogue of Lattices, entry LAMBDA9.`; `V. Alexeev, "Reflective hyperbolic 2-elementary lattices, K3 surfaces and hyperkahler manifolds", arXiv:2209.09110v4, Theorem 1.1.` |

The page `fields.html` also lists every family with its meaning and the number of its lattices.

The prose is Pandoc Markdown.
`$...$` is inline TeX and `$$...$$` is display TeX.

Prose, field descriptions and site copy state mathematics by its standard name and in symbols: "primitive sublattice", not "sublattice with a torsion-free quotient".
A root of $L$ is a primitive $r$ with $b(r, r) \neq 0$ and $s_r \in O(L)$; $\Phi(L)$ is the set of roots, and $\Phi_S(L)$ the set of roots with $b(r, r) \in S$, for $S \subseteq \mathbb{Q}$.
$\mathbb{Z}\Phi_S(L)$ is the sublattice that $\Phi_S(L)$ generates, and $L$ is an $S$-root lattice when $L = \mathbb{Z}\Phi_S(L)$.
The definitions have no hypothesis on the signature or on the values of $b$.
The vectors with $b(r, r) = \pm 2$ are $\Phi_{\{\pm 2\}}(L)$, never "the roots" of $L$.

The root sublattice of $L$ is $R(L) := \mathbb{Z}\Phi(L)$, and each record states it.
A definite record states $\Phi(L)$ in `definite.roots`: each irreducible component with its type, its scale and its simple roots.
The build lists $\Phi(L)$ and compares.
In `root_span.roots`, a record that is not definite states roots that generate $\mathbb{Z}\Phi(L)$.
When they do not generate $L$, the prose proves that no root of $L$ is outside the sublattice that they generate, and `root_span.summands` and `root_span.embedding` state $\mathbb{Z}\Phi(L)$ as an orthogonal sum of twists of records with its embedding in $L$.
A summand is a record with a scale, `{tag: '0001', scale: 2}` for $\langle 1 \rangle(2)$, and the rows of `embedding` have the Gram tensor of $M_1(k_1) \oplus M_2(k_2) \oplus \cdots$.
A root is a row of integers: its coordinates in the basis $e_1, \dots, e_n$ of the record.
The page of the lattice writes it as $\sum_i c_i e_i$, and states the orthogonal decomposition of $L$ that the basis gives.
A record that is not definite and has no `root_span` block is not decided, and its page says so.

## Tags

A tag is four characters from `0-9` and `A-Z`. The file name is the tag.
A tag is permanent: it never moves to another lattice, and a record is never renumbered.
When a record leaves the corpus, its tag goes to `retired-tags.yaml` with the lattice that was there and why it is not a record; the build rejects a record under a retired tag, and the next tag is after every tag, retired or not.
The address of a lattice is `tag/<TAG>.html`.

To add a lattice:

1. Search the database page for the lattice, by name and by its invariants (rank, determinant, minimum, kissing number), so that a lattice already in the corpus under another name is not added twice.
   For a definite lattice the command below decides isometry with a record of the corpus (PARI `qfisom`) and refuses a lattice that is already there in another basis; for an indefinite lattice the search is the only check.

2. `just new --gram '[[2, 1], [1, 2]]' --name A2 --latex A_2` writes `lattices/<TAG>.md` under the next tag, with every field that the Gram tensor determines computed.
   `--alias`, `--family`, `--reference` and `--prose` give the other fields; `uv run latticedb new --help` lists them.
   For an entry of the Catalogue of Lattices, `just nebe-sloane LAMBDA10 --name Lambda10 --latex '\Lambda_{10}' --family laminated` reads `sources/nebe_sloane/LAMBDA10.json`. When the entry is absent, it reads the local `union.gz` archive, or fetches its individual page if the archive is absent. It checks the rank, determinant, minimum and kissing number that the catalogue states against the Gram tensor, and writes the record with the reference of the entry.
   The command refuses a record that does not validate, that is a twist $M(n)$ with $n \neq 1$ of the lattice the corpus records (other than a twist by 2 in the family `nikulin-two-elementary`), that repeats the name or the components of a record in the corpus, that is definite and isometric to a record in the corpus, or that names a family not in `families.yaml`, and writes nothing.

3. Edit the file: add `related` entries, the prose, and the declared fields with their sources.
   For a record that is not definite whose `root_span` block the command could not decide, write the block and its proof by hand.

4. `just build` validates the corpus and builds the site.
   It prints each problem of each record with the path of the file and the field.

The corpus is also checked as a whole: two records cannot have the same name or the same components, two definite records cannot be isometric, a `related` entry must name a tag in the corpus, and a family must be a key of `families.yaml`. Isometry is decided by `qfisom` only for the pairs whose rank, determinant, minimum, kissing number, root system, theta series and discriminant group agree.

## Certificates

Each computation is carried out once.
`certificates.yaml` maps the name of each computation that the database has carried out to its certificate: the SHA-256 digest of its inputs, the program that carried it out with its version, and, for a computation that did not finish, the time limit in seconds.

| Name | Computation | Inputs |
| --- | --- | --- |
| `<tag> derive` | The fields that the Gram tensor determines | The Gram tensor |
| `<tag> <block>.<field>` | A value that SageMath computes, such as `0012 integral.genus_symbol` | The Gram tensor |
| `source <name>` | The check of `sources/<name>/` against the records and the morphism files | The files of the source, the Gram tensors and the morphism files |
| `corpus summands` | The embeddings between records that are orthogonal sums, of `latticedb.summands` | The Gram tensors of every record |

`latticedb certify` carries out each computation without a certificate for its present inputs, stores its values, and writes its certificate; a check of a source is certified only when it finds no problem.
A computation that did not finish within the time limit is carried out again only with a larger `--seconds`. To carry out a computation again, after a change to the computation, remove its certificate.
`latticedb new` and `latticedb nebe-sloane` certify the derived values of the record that they write.

The computations are heavy for a large lattice, so they run in the nightly job `.github/workflows/lattice-database-certify.yml`, which opens a pull request with the new values and certificates.
Locally, run `just certify --tag <tag>` for one new record at most.
`latticedb check` validates the records and lists the computations without a certificate; it computes nothing.

## Morphisms

A file `morphisms/<S>-<T>.md` holds morphisms from the lattice with tag `S` to the lattice with tag `T`: maps $\varphi$ with $b_T(\varphi x, \varphi y) = b_S(x, y)$.
The front matter is the record, and the body is notes in Pandoc Markdown.

```yaml
---
source: '0128'
target: 027E
morphisms:
- name: $U \oplus E_8(-1) \hookrightarrow U^3 \oplus E_8(-1)^2$
  description: The inclusion as the first summand $U$ and the first summand $E_8(-1)$.
  matrix:
  - [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  - ...
  row_subdivisions: [2, 4, 6, 14]
  column_subdivisions: [2]
---
```

The matrix is in the bases of the two records, with rank $T$ rows and rank $S$ columns: column $j$ lists the coordinates of $\varphi(e_j)$.
A morphism with `scale: c` is a morphism $S(c) \to T$ from the twist of $S$: $b_T(\varphi x, \varphi y) = c \, b_S(x, y)$.
The corpus records a lattice once up to twist and sign, so a lattice that a source names as $M(c)$ maps through the record $M$ with scale $c$: the coinvariant lattice $\Lambda_G = M(-1)$ of a symplectic K3 group embeds in the K3 lattice with scale $-1$.
The subdivisions are the lines of a block matrix, as SageMath's `M.subdivisions()` returns them: a line $k$ lies between rows (or columns) $k$ and $k + 1$.
The build checks that $M^{\top} G_T M = c \, G_S$, and that the parts that the lines cut are orthogonal summands of $T$ (rows) and of $S$ (columns).

`latticedb certify` writes the embeddings into each record $T$ that is an orthogonal sum.
The orthogonal summands of $T$ are the connected components of the graph on its basis in which $e_i$ and $e_j$ are adjacent when $b(e_i, e_j) \neq 0$; group them by their Gram matrix, $T = \bigoplus_M M^{n_M}$.
The diagonal $x \mapsto (x, \ldots, x)$ embeds $M(k)$ into $M^k$.
For each $M$, a partition $\lambda$ of an integer $m \leq n_M$, with its parts placed on consecutive summands, gives an embedding $\bigoplus_M \bigoplus_j M(\lambda_j) \to T$; with $g = \gcd_j \lambda_j$, it is a morphism of scale $g$ from the record with the summands $M(\lambda_j / g)$, when the corpus holds one.
Up to the permutations of isometric summands there are $\prod_M \sum_{m \leq n_M} p(m)$ such embeddings, with $p$ the partition function; the identity of $T$ is not written.

Each file has the page `morphism/<S>-<T>.html`, which draws each matrix with its lines; `morphisms.html` lists the files, and the page of each lattice links the files that name it.

`just morphism S T --name ... --matrix ...` checks a morphism and appends it to the file.
From SageMath, for a matrix `M` whose columns are the images (a morphism `phi` gives `M = phi.matrix().transpose()`, because SageMath lists the images in rows):

```python
import json
rows, columns = M.subdivisions()
print(json.dumps([[int(x) for x in row] for row in M.rows()]), json.dumps(rows), json.dumps(columns))
```

The three outputs are the values of `--matrix`, `--row-subdivisions` and `--column-subdivisions`.

## Collection pages

A file `pages/<slug>.md` gives the page `collection/<slug>.html`, which lists the lattices whose database row satisfies every condition of `where`.

```yaml
---
title: Even unimodular lattices
summary: Integral lattices with determinant $1$ or $-1$ on which every value $b(x, x)$ is even.
where:
  properties: [even, unimodular]
---
```

A key of `where` is a key of a row of `lattices.json`, for example `rank`, `definiteness`, `properties` or `families`. For a key whose value is a list, the list must contain each required value.
In `title` and `summary`, backticks mark code and dollar signs mark TeX. The body is Pandoc Markdown.
The build fails for a key that no row has and for a collection with no member.

## Theory pages

A file `theory/<slug>.md` gives the page `theory/<slug>.html`, and `theory.html` lists these pages in the order of `order`. Each definition and convention of the site is stated on one theory page, under a heading with an explicit anchor such as `{#signature}`. A lattice page, a collection page, a morphism page and the prose of a record link to that anchor.

```yaml
---
title: Definite lattices
summary: The invariants that a record of a definite lattice states, and the sign convention for negative definite forms.
order: 6
---
```

The build fails when two theory pages have the same `order`. At the end, the build reads every page that it wrote and fails for an internal link to a file that does not exist or to an anchor that the destination page does not have.

## The database page

`database.html` loads `lattices.json` and shows one row for each lattice.
It has filter panes for rank, definiteness, properties and families, a builder for conditions on any column, text search, column selection, and CSV export.

The query string selects filters, so a filtered view has an address:

| Parameter | Selects | Example |
| --- | --- | --- |
| `rank` | ranks | `database.html?rank=8,16` |
| `definiteness` | definiteness | `database.html?definiteness=positive definite` |
| `property` | properties; a row must have all of them | `database.html?property=even,unimodular` |
| `family` | families; a row must have all of them | `database.html?family=irreducible-root-lattice` |
| `q` | text search | `database.html?q=Lambda` |

## Commands

The `latticedb` command line owns validation, the build and deployment.
The `justfile` calls it.

| Recipe | Effect |
| --- | --- |
| `just new ...` | Write the record of a new lattice from its Gram tensor and the options |
| `just nebe-sloane ENTRY ...` | Write the record of an entry of the Catalogue of Lattices |
| `just morphism S T ...` | Check a morphism of lattices and append it to `morphisms/<S>-<T>.md` |
| `just check` | Validate every record and list the computations without a certificate |
| `just certify ...` | Carry out the computations without a certificate, store their values and certify them |
| `just build` | Validate every record and build the site into `_site/` |
| `just deploy` | Build, link `_site/` to `/var/www/static-sites/lattice-database`, and check that nginx serves it |
| `just tag` | Print the tag for the next new record |
| `just test` | Run the tests |

The check of `sources/hashimoto/` checks the records against Tables 10.2 and 10.3 of Hashimoto, and the embeddings of $\Lambda^G$ and $\Lambda_G$ in the K3 lattice `027E` as orthogonal primitive sublattices.
The check of `sources/hoehn_mason/` checks that the morphism files hold the maps that the source determines.

The build needs `pandoc` on `PATH`. The pages load MathJax and DataTables from a CDN. The record commands compute with PARI/GP through `cypari2` and with `python-flint`. `latticedb certify` needs SageMath at `$SAGE_BIN`.

## Sources to absorb

The corpus must absorb the whole Catalogue of Lattices (G. Nebe, N. J. A. Sloane), <https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/>, with its indefinite lattices first.
`sources/nebe_sloane/` holds the absorbed entries and the catalogue's `union.gz` archive. The definite records include the laminated lattices $\Lambda_9$ to $\Lambda_{20}$, $K_{12}$, $\kappa_7$ to $\kappa_9$, $BW_{16}$, the Leech lattice $\Lambda_{24}$, the 23 other Niemeier lattices, and `BGF.2.2112`.

The work that remains, in order:

1. Absorb the remaining entries of the bulk archive.
   The whole archive, read on 2026-10-02 from <https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/union.gz>, holds 823 named entries; 754 give a parseable single Gram tensor, 25 of those have rational components (the dual lattices $A_n^*$, $D_n^*$, $E_6^*$, $E_7^*$ and their relatives), and exactly one of the parseable Gram tensors is indefinite: `Shimada_86`, of signature $(85, 1)$.
   The indefinite material of the corpus therefore does not come from the catalogue; the entries to absorb are definite, plus `Shimada_86`.

2. Make `just nebe-sloane` admit an indefinite entry.
   `nebe_sloane.check` compares the minimum and the kissing number that the catalogue states, which an indefinite lattice does not have.

3. Absorb the entries, `Shimada_86` included.
   The twist and sign rules under *A record* apply: an entry that is $M(n)$ for an integer $n \geq 2$, or the negative of the lattice the corpus records, is not a record.

The survey of 2026-10-02 read these by the test the corpus uses everywhere: a source contributes the claims it states — Gram tensors, identifications, invariants, relations — and every claim lands as a field, a `related` entry, a morphism or a check of a record. Two sources stating a claim about the same lattice is not redundancy, it is convergence, and it is how a stored value gets checked; the modules of Hashimoto and of Höhn and Mason check records no other source supplies the lattice for. Nothing about a lattice being named elsewhere demotes a source. The reasons that do apply are stated at each entry: a claim the schema has no place for gains that place (AGENTS.md), and a displayed decimal is not inexact data where theory states the exact quantity it rounds — the exact value is then absorbed, as a formula evaluated in a symbolic ring, never discarded for its printing. What yields nothing is a number with no exact recovery known, or a page that is not there.

- **Watson's single-class genera**, `Classi/watson` on the catalogue site: 3494 primitive lattices of one class per genus, in machine-readable rows of the lower-triangular Gram entries, dimension by dimension; Lorch's completion is arXiv:1208.5638. A module `latticedb watson` reads it, and each genus's stored `integral.genus_class_count = 1` checks the table's claim.

- **The Brandt-Intrau-Schiemann tables** of odd and even primitive positive ternary forms of discriminant at most 1000, `Brandt_1.html` and `Brandt_2.html` on the catalogue site, as recomputed by Schiemann: rank-3 integral records with genus data.

- **The rank-3 Lorentzian lattices of Allcock, in Dutour-Sikiric's database**, <https://github.com/MathieuDutSik/GeometryDatabase_Rank3_Lorentzian_lattices>: the file `RK3_all` holds 3441 lattices, each row the Gram matrix, the simple roots, the source label `W` for the Weyl group and the ordinal `L` of the lattice within that group, in PARI-readable form; these labels are neither group orders nor subgroup indices (converted to GAP by `Convert_Allcock_RK3`). Every row is read on 2026-10-02: 3415 have signature $(2,1)$, 25 signature $(1,2)$ and one is positive definite; 933 are even and 2508 odd.
  This is the source of indefinite records the Catalogue does not give (it supplies one, `Shimada_86`): rank-3 indefinite integral lattices with their roots, which is exactly what `root_span` and the `hyperbolic` block ask for, and `RK3_explicit` (704) and `RK3_implicit` (715) split the reflective and non-reflective lists of Allcock's 1989 Bielefeld preprint.
  A module `latticedb allcock` reads `RK3_all`, and the corpus absorbs the entries that are not a twist or a sign of a record already present.
  Reached from Martinet's page of links to those working on lattices, <http://jamartin.perso.math.cnrs.fr/>.

- **Jagy's table** of positive ternary forms that are spinor regular but not regular, `Jagy.txt` on the catalogue site: sextuples $(a, b, c, d, e, f)$ of a form's coefficients, so the Gram tensor is their symmetric matrix divided by 2.

- **Kirschmer's tables of genera of small class number**, <https://www.math.uni-bielefeld.de/~mkirschm/forms/>: a survey misread first, and now corrected. The page's own notation section states what each file holds: `res_orth.tar.bz2` is genera of *definite* quadratic lattices over *totally real number fields*, rank 3 to 16, class number 1 or 2, each genus printed as a diagonal matrix over $K$ with a $\mathbb{Z}_K$-module; `unimod.m` and the hermitian, quaternionic-hermitian and binary-form tables are likewise over number fields, and `maxgen.m` is one-class genera of maximal integral lattices over number fields. These are exact claims about lattices — over $\mathbb{Z}_K$, which the corpus has no record kind for. Absorbing them is the schema gaining that kind, an owner decision of some size, not a reason to discard the data; reading them for the $\mathbb{Z}$-lattice the $\mathbb{Z}$-trace or norm gives is a construction that would also need its place. The page is the citation the corpus already uses: the completeness of the class-number-one $\mathbb{Z}$-lattices rests on it (Watson, Kirschmer-Lorch arXiv:1208.5638), and it is the reference for a genus's class number stated in prose.
  Indefinite records over $\mathbb{Z}$ arrive meanwhile from the rank-3 Lorentzian database above and from papers (Nikulin's tables, Hashimoto, Gritsenko–Hulek–Scholsche, the K3 and Leech coinvariant lattices).

- **LMFDB's lattices collection**, <https://beta.lmfdb.org/Lattice/>: 39,293 positive definite integral lattices, dimensions at most 24, the largest class number 56. The Source page states the Gram matrices come from the Catalogue and its tables. The data of Haensch and Anni (<https://github.com/annahaensch/lattice_data>, Magma and PARI) include `class_number`, automorphism-group order and generators, `level`, theta coefficients and `genus_reps`. The record fields hold class number, group order, level and theta data; named subgroup morphisms and `genera/` hold the group and genus claims when entries are identified. The two representatives of genus `3.11.22` are the forms `1 2 6 2 0 0` and `1 1 11 0 0 0` that Brandt–Intrau–Schiemann prints under discriminant $-44$. The Source page cites Kirschmer and Lorch, arXiv:1208.5638, for the completeness of class-number-one lattices.
  The stored `density` and `hermite` are exact mathematics printed as decimals, the schema's standing case of it: the Hermite invariant $\gamma_n(L)=\lambda_1/\det^{1/n}$ and the packing density $\Delta(L)=V_n(\sqrt{\lambda_1}/2)/\sqrt{\det}=\pi^{n/2}\lambda_1^{n/2}/\bigl(2^n\,\Gamma(\tfrac n2+1)\sqrt{\det}\bigr)$ — $\pi/4$ for $\mathbb{Z}^2$, $\pi^4/384$ for $E_8$.   Sampled against the API on 2026-10-02 at rows of dimensions 2 to 24: both formulas reproduce the stored values to the full printed precision except the last one or two digits, whose rounding mode varies by row — a rendering choice, which is why the absorption takes the formula and never the decimal. The values lie in $\mathbb{Q}(\pi^{n/2}, \sqrt{\det})$, a symbolic real a record can hold exactly. `shortest` gives coordinates in the printed basis and is the row's choice of basis, not a claim.
  The API route is <https://beta.lmfdb.org/api/lat_lattices/?_format=json>, read on 2026-10-02: it answers only for a client that first loads a page of the site and returns its `human=1` cookie, the beta gate; a request without it is redirected.
  A module reading this source needs that two-step fetch.

- **Martinet's perfect lattices**, <http://jamartin.perso.math.cnrs.fr/Lattices/index.html>: the perfect lattices of dimensions at most 7 in `perf2to7` and the dimension-8 sets in PARI/GP files (`p8.gp.gz` and siblings), readable by `cypari2`; perfectness is a property a record states in its prose, and the Grams are definite integral records.

- **Borcherds's tables of lattices**, <http://math.berkeley.edu/~reb/lattices/>: for each of the 665 odd unimodular and 121 even determinant-2 lattices of dimension 25 the root system, the order of the orthogonal group modulo the reflection group, and the orbits of norm $0,-2,-4,-6$ vectors of $I\!I_{25,1}$ with coordinates and simple-root counts; King's table of masses of the 32-dimensional even unimodular lattices by root system; the `norm*` and Magma-format files, all read on 2026-10-02. It prints no Gram tensor, so it writes no record — its claims land on records the corpus already holds: the twenty-four norm-zero vectors identify the Niemeier lattices as the orthogonal complements of norm-zero vectors of $I\!I_{25,1}$, which is `related` material and a morphism file for the twenty-three Niemeier records, with the page as the reference; the root system and the group order are the same fields of the rank-25 positive-definite records, the order derived from the stated group structure: Table −2 gives $|O(L)|=|R||G|$ for the even determinant-2 case, while Table −4 gives $|O(L)|=2|R||G|$ for the odd unimodular case, with $R$ the root-reflection group and $G$ the chamber stabilizer — these table values require the identified action before comparison with `definite.automorphism_group_order`; King's mass is a genus-level statement about the 32-dimensional records the corpus does not yet have, to be carried when they arrive.

- **Cohn's kissing-number table**, <https://cohn.mit.edu/kissing-numbers>: the best known bounds per dimension, its lower bounds originally the Catalogue's table and later improvements naming their lattices — a citation for `definite.kissing_number` and, where a record attains a bound stated elsewhere, an outside table the field checks against.

- **Dutour-Sikiric's Delaunay polytopes of the Niemeier lattices**, <https://github.com/MathieuDutSik/delaunaypolytopeniemeier.github.io>: the `lattice-polytopes/` schema can record their vertices and Delaunay sphere in the basis of each Niemeier lattice. The source values and coordinate identifications remain to be imported.

- **Sloane's packing tables**, <https://neilsloane.com/packings/>: the best known sphere packings by dimension, one file per configuration. The lattice files are exact: `E8.8.240.txt` (read on 2026-10-02) prints the 240 minimal vectors of $E_8$ as integer rows in an orthonormal coordinate system, with a comment citing SPLAG page 120 — that is $\Phi(L)$ for a record the corpus holds, landing as `definite.roots` and the kissing count of the $E_8$ record, an identification and a check, the same kind of claim the Catalogue's entry carries. The non-lattice files are point configurations — the 3-simplex file is four rows of $\pm 1/\sqrt{3}$, verified to be the correctly-rounded exact values — objects the schema has no place for; under the rule that a claim with no place gains one, that placement is a schema question, and the decimals are a rendering of it, not a reason the data is discarded.

Sources read on 2026-10-02 that yield nothing, each because the page is not data or is not there — never inexactness of a rendering, and never because another source names the same lattice:

- Scholl's packungen site, <http://www.home.unix-ag.org/scholl/packungen/>: an interactive search over images, no lattice data to read.
- Schiemann's extrep pages: moved with his KIT group and not answering as data on 2026-10-02.
