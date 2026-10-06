# Lattice database

A catalogue of lattices.
A *lattice* here is a free module $L$ of finite rank over $\mathbb{Z}$ with a symmetric bilinear form $b \colon L \times L \to \mathbb{Q}$.
The form can be definite, indefinite or degenerate, and its values need not be integers.

Each lattice has one Markdown file, `lattices/<TAG>.md`. The YAML front matter of the file is the record of the lattice; the body is prose about it.
The build reads the cards, writes one page for each lattice, and writes one table, with one row per record, that the database page filters, sorts and exports.

The site is served locally at <http://lattice-database.localhost/>, and published at <https://dzackgarza.github.io/research/lattice-database/> by `.github/workflows/docs.yml`, which deploys it beside the docs book.

## Layout

| Path | Contents |
| --- | --- |
| `lattices/<TAG>.md` | One record and its prose for each lattice |
| `geometric-objects/<slug>.md` | One locally ringed geometric space, its specialized data and cited prose |
| `geometric-families/<slug>.md` | One parameterized geometric family and its cited prose |
| `graphs/<slug>.md` | One weighted graph with stored classification labels and cited prose |
| `lie-groups/<slug>.md` | One Lie group as its own mathematical object; real orthogonal groups use canonical cards `o-p-q` with `p <= q` |
| `arithmetic-groups/<slug>.md` | One arithmetic subgroup attached to a lattice, with its ambient Lie group and parent arithmetic group when applicable |
| `genera/` | Genus records with representative isometry classes and mass |
| `lattice-families/<slug>.md` | One infinite parameterized family of lattices sharing a Gram template in its parameter, with rank, signature and cited prose |
| `lattice-polytopes/`, `toric-varieties/` | Based lattice polytopes, polar duals and normal-fan toric varieties |
| `geometric-maps/`, `moduli-problems/` | Geometric maps, fibrations and specified moduli problems |
| `integral-local-systems/`, `picard-fuchs-operators/` | Integral monodromy and period operators with geometric realizations |
| `geometric-bibliography.bib` | BibTeX entries cited by geometric object and family prose |
| `families.yaml` | Every family that a record may name, with one line of its meaning |
| `retired-tags.yaml` | Every permanent tag whose former record has been retired, with the reason and its current owner when one exists |
| `pages/<slug>.md` | One collection page: conditions on the database rows, and prose |
| `theory/<slug>.md` | One theory page: the definitions and conventions that the other pages link to |
| `src/latticedb/model.py` | The schema of a lattice card, including its outgoing morphisms, and its validators |
| `src/latticedb/geometric.py` | The schema of geometric families, projective varieties, manifolds and symmetric spaces |
| `src/latticedb/graphs.py` | Schema for weighted vertices, edges and stored graph-classification labels; no diagram recognition |
| `src/latticedb/catalogues.py` | Schemas of Lie groups, arithmetic groups, genera, polytopes, toric varieties, maps, local systems and operators |
| `src/latticedb/records.py` | Calls preamble-owned lattice operations for enrichment/CI verification and serializes returned values; writes cards as files |
| `src/latticedb/nebe_sloane.py` | Reads an entry of the Catalogue of Lattices (G. Nebe, N. J. A. Sloane) and writes it as the declared fields of a record |
| `src/latticedb/hashimoto.py` | Reads Tables 10.2 and 10.3 of Hashimoto for source intake and provenance collation; it is not part of mathematical verification |
| `src/latticedb/hoehn_mason.py` | Reads the Höhn--Mason ancillary data for source intake and provenance collation; it is not part of mathematical verification |
| `src/latticedb/genus.py`, `sage_genus.py` | Certification dispatch/serialization adapters for preamble-owned genus and orthogonal-group operations; they contain no lattice algorithms |
| `src/latticedb/corpus.py` | Reads every stored record and validates only the shape of each file |
| `src/latticedb/site.py` | Builds the site |
| `src/latticedb/templates/`, `assets/` | Page templates, styles and the database script |
| `sources/nebe_sloane/union.gz`, `<ENTRY>.json` | The catalogue's standard-format union archive and stored entries read from it or from individual pages |
| `sources/nipp/` | Nipp's quaternary and quinary source tables, read by `src/latticedb/nipp.py` |
| `sources/brandt_intrau/` | Brandt–Intrau–Schiemann's odd and even ternary form tables, read by `src/latticedb/brandt_intrau.py` |
| `sources/watson/watson.txt` | Watson's single-class genus representatives, read by `src/latticedb/watson.py` |
| `sources/normalized/*.jsonl.gz` | Reproducible source-row index: parsed Nipp, Brandt–Intrau–Schiemann, and Watson rows, plus every named Nebe–Sloane archive entry with its source sections and ordinal; the index computes no new mathematical invariants |
| `sources/hashimoto/table_10_2.json`, `table_10_3.json` | Tables 10.2 and 10.3 of K. Hashimoto, arXiv:1012.2682, as printed, each row linked to the records of $\Lambda_G$ and $\Lambda^G$ by a twist and a change of basis |
| `sources/hoehn_mason/leech.json`, `lattices_<i>_<j>.json` | The Leech lattice and the 40 entries `lattices[i,j]` of the Magma file of G. Höhn and G. Mason, arXiv:1505.06420, whose coinvariant lattice is $\Lambda_G(-1)$ for a row of Table 10.2 of Hashimoto: the bases and the stabilizer generators as printed, each linked to its record by a twist and a change of basis |
| `tests/` | Tests of the validators, of the record commands and of the built site |

## Geometric objects

Each file in `geometric-objects/` has one permanent slug and a `kind` that names its mathematical category. The current card kinds are `projective_complex_variety`, `complex_manifold`, `riemannian_symmetric_space` and `hermitian_symmetric_space`. They share a locally ringed-space record identity; fields belong to the category in which they are defined.

The category relations are refinements and structure-changing functors. Schemes over $\mathbb C$ include smooth projective complex varieties. Complex analytic spaces include complex manifolds. Topological manifolds admit PL or differentiable refinements; a $C^\infty$ manifold has a sheaf of smooth functions and can carry a Riemannian metric. A Hermitian symmetric space is both a Riemannian symmetric space and a complex manifold with a compatible Hermitian structure. Analytification sends a finite-type complex scheme to a complex analytic space. Its source and result are separate linked cards through `analytic_space` and `algebraic_model`. Forgetting a metric or changing a structure sheaf is a functor between categories.

A `projective_complex_variety` card describes a smooth connected projective complex variety or a class whose stated invariants are constant. Its `dimension` is complex dimension; its required `hodge_poincare` is the Hodge–Poincaré series. Symmetric-space cards give the connected group quotient, isotropy group, defining involution and metric normalization. Their `rank` is symmetric-space rank. A Hermitian card also gives complex dimension and can state its bounded realization and the parabolic presentation of its compact dual. A compact dual is another symmetric-space card; a projective algebraic model of its analytic space has its own card.

The `diagrams` field on a symmetric-space card links to graph cards. A graph card stores arbitrary YAML vertex and edge weights, edge direction, a named edge relation, and optional source-stated or preamble-computed `properties` labels. Parallel edges and loops are permitted. Lattice-db does not recognize Coxeter, Dynkin, Satake or Vinberg diagrams from those decorations; such recognition belongs to the preamble and the resulting labels are stored on the card.

On projective variety cards, `hodge_poincare` stores the nonzero terms of $H_X(u,v)=\sum_{p,q}h^{p,q}u^pv^q$, where $h^{p,q}=\dim_{\mathbb C}H^q(X,\Omega_X^p)$.
Each term has `p`, `q` and a positive `coefficient`; omitted terms have coefficient zero.
The schema checks only that one bidegree is not stored twice. The optional `symmetry_group` is stored data; lattice-db does not derive it, Betti numbers, Euler characteristics, or Hodge symmetries from the coefficients.

`geometric-families/` holds parameterized families.
An instance names its `family` slug and integer `family_parameter`; verification checks that the family exists and that the parameter meets its minimum.
Each instance retains its own Hodge series.
`local_deformation_dimension` records the dimension of an unobstructed local complex deformation space.
`chern_numbers` stores source-stated or preamble-computed Chern-number index tuples and integral values; the schema only prevents duplicate index tuples.

An optional `cohomology_lattices` entry identifies $H^k(X;\mathbb Z)$ modulo torsion with a tagged lattice, under the named pairing and integer scale.
Verification checks that the tag exists. Any comparison with Betti or Hodge numbers is a mathematical operation and therefore belongs to the preamble.
The pairing names the form: the Hodge numbers alone do not determine it.
The geometric object page links to the lattice page, and the lattice page links back.

```yaml
slug: k3-surface
name: Complex projective K3 surface
kind: projective_complex_variety
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

Each additional catalogue uses one Markdown file per permanent slug. Its front matter is parsed when the corpus is read, and `latticedb verify` checks only structural/reference coherence; its body states the source and mathematical identification. Mathematical validation occurs by constructing the corresponding preamble object in CI. These records remain distinct from the lattice, geometric object and geometric family records they link.

| Catalogue | Defining data and links |
| --- | --- |
| `arithmetic-groups/<slug>.md` | One stored arithmetic subgroup $\Gamma\leq O(L)$, including standard subgroups (`O`, `SO`, `O+`, `SO+`, `Otilde`, `SOtilde`, `Otilde+`, `SOtilde+`) or named subgroups such as $\Gamma_{\mathrm{En},2}$. Its generators name self-isometries stored on the lattice card; it may also state relators, abstract structure, order, index, parent, a stabilized object, a hyperbolic chamber and orbit representatives. |
| `genera/` | Signature, determinant, parity, genus symbol, representative lattice tags, class number, completeness and rational mass. A complete list with known group orders checks $\sum 1/|O(L_i)|$. |
| `lattice-families/` | Parameter name and minimum, rank, signature, and the Gram template whose entries are integers or integer arithmetic in the parameter; the schema checks only template syntax, shape and symmetry. Mathematical claims about the resulting family belong to a preamble-owned family construction, not to lattice-db. |
| `lattice-polytopes/` | Vertices in a based free abelian group, ambient rank, source identifier, reflexivity, polar dual, and optional Delaunay sphere tied to a quadratic lattice. A toric ambient lattice is not the quadratic lattice of a lattice record. |
| `toric-varieties/` | A polytope and its normal fan, with optional subdivision rays. |
| `geometric-maps/` | Source and target geometric records; a fibration also names its generic fiber and can state its singular locus. |
| `moduli-problems/` | A family, moduli dimension, optional polarization orbit and arithmetic subgroup. |
| `integral-local-systems/` | A fibration over a smooth base, its source family, cohomological degree and rank; optional integral fiber lattice and matrices of monodromy around named loops. |
| `picard-fuchs-operators/` | Exact rational polynomial coefficients of $\sum_i a_i(x)(x\,d/dx)^i$, coordinate, normalization, singularities and exponents; each realization names a family, period and relation to the operator. |

`dual_gram_tensor` stores $G^{-1}$, so $L^*$ is a derived object of the lattice card rather than another card. `integral.level` is the least $k$ for which $k b(x,x)$ is even on $L^*$; `integral.modular_scale` records a scale $k$ for which the lattice is known to be $k$-modular. A chosen isometry $L\to L^*(k)$, when one is worth storing, belongs to the `morphisms` data of the card of $L$ rather than to a separate morphism file.

A scaled dual $L^*(k)$ with $k \neq 1$ is a different lattice object, with Gram tensor $kG^{-1}$, and may have its own card. A source title containing the word “dual” therefore does not by itself make a card redundant; only the raw dual $L^*$ is derived automatically from the owner card.

`definite.minimal_vectors` is a complete shell in the record basis and must match the minimum and kissing number. `definite.perfect` is checked by the span of their rank-one tensors. `definite.regular` and `definite.spinor_regular` apply to integral ternary lattices. The Hermite invariant and packing density are exact functions of rank, determinant and minimum; source decimals are checked against those formulas rather than stored as exact values.

Projective complex variety cards can also store Pontryagin numbers, a Beauville–Bogomolov Riemann–Roch polynomial, $\operatorname{Aut}^0$, homotopy groups, Fano and surface data, and a homogeneous, horospherical, Calabi–Yau complete-intersection or toric anticanonical construction. A complete-intersection configuration stores its projective factors and equation multidegrees; the schema checks the Calabi–Yau degree and dimension equations.

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
`dual_gram_tensor` is the Gram tensor $b^*$ of the dual lattice $L^*$ in the dual basis. When populated, lattice-db obtains it from the preamble operation `L.dual_lattice()` and serializes the returned Gram tensor; lattice-db does not invert $G$ itself. A raw dual lattice is therefore never a second record: $L^*$ is represented on the card of $L$.

For an integer $n$, the twist $L(n)$ is the same underlying free abelian group with bilinear form $nb$.
Twisting is not an equivalence relation in the catalogue: $L$, $L(2)$ and $L(-1)$ are different bilinear lattices and may each have their own cards when they are mathematically relevant. In particular, cards such as $E_{10}$ and $E_{10}(2)$ must not be collapsed merely because their forms differ by a scalar.
A construction can still name a twist by reference to another card plus a scale when that is the natural description. For example, `root_span.summands` can state a summand as $M(k)$ without asserting that the catalogue identifies $M(k)$ with $M$.

The Gram tensor is the defining mathematical input. Lattice-db itself performs no mathematical computation. Enrichment and certification construct the corresponding preamble objects, call preamble-owned operations, serialize the returned values into cards, and in the certification phase attach certificate hashes. Potentially expensive exact invariants, including `integral.overlattice_count`, are requested only in the CI certification phase. Archived intake sources are provenance, not verification oracles.
The build reads the stored values and renders every card.
A person writes `name`, `latex`, `aliases`, `families`, `related`, `references` and the prose.
`latticedb certify` requests exact `integral.overlattice_count`, `integral.genus_symbol`, `integral.genus_class_count`, `integral.hyperbolic_index`, `integral.spinor_genus_count`, `integral.spinor_genera`, `definite.automorphism_group_order` and `definite.automorphism_group_generator_morphisms` from the research preamble. Lattice-db contains no implementation of these operations. For a definite integral lattice, CI consumes `L.orthogonal_group()`: the preamble computes and frames $O(L)$, and lattice-db only serializes its cardinality and generator isometries. Generator matrices are stored once as scale-one self-morphisms and the `definite` field stores their names. `integral.discriminant_sequence`, `integral.primitive_orbits` and `integral.discriminant_orbits` remain card fields but are not CI-computed until corresponding preamble-owned operations are exposed. A completed computation replaces any disagreeing authored value in the scope it computes and then certifies the resulting card value. A computation that does not finish within the time limit writes neither a replacement nor a certificate.
`hyperbolic.reflective` and a `root_span` block that enrichment does not decide are declared: the prose states the source of each one, and the page of the lattice marks `hyperbolic.reflective` *declared*.

An invariant that exists only under a hypothesis lives in a block named for that hypothesis. The block itself is stored data: the schema validates its shape, while mathematical verification of the hypothesis belongs to the preamble.

| Block | Hypothesis on the lattice | Fields |
| --- | --- | --- |
| `integral` | every $b(e_i, e_j)$ is an integer | `parity`, `level`, `modular_scale`, `discriminant_group`, `discriminant_sequence`, `overlattice_count`, `delta`, `bad_reduction_primes`, `quadratic_character`, `genus_symbol`, `genus_class_count`, `spinor_genus_count`, `spinor_genera`, `hyperbolic_index`, `primitive_orbits` |
| `definite` | $b$ is positive or negative definite | `minimum`, `kissing_number`, `minimal_vectors`, `perfect`, `regular`, `spinor_regular`, `automorphism_group_order`, `automorphism_group_generator_morphisms`, `theta_series`, `root_system`, `roots` |
| `root_span` | $b$ is not definite | `roots`, `norms`, `summands`, `embedding` |
| `root_sublattice` | $b$ is definite, or the record has `root_span` | `invariant_factors`, `norms` |
| `indefinite` | $b(x, x)$ takes both signs | `isotropic` |
| `hyperbolic` | $b$ is nondegenerate with signature $(1, n)$ or $(n, 1)$, rank at least 2 | `reflective` |

All invariant blocks and computed fields may be absent on a sparse card. A populated field is either authored/source-stated or the serialized result of a preamble operation. `definite.automorphism_group_generator_morphisms` is a list of names of scale-one self-morphisms on the same card; its certificate commits to the corresponding matrices, not to the chosen names. `integral.discriminant_sequence` is stored when available; lattice-db does not currently compute it.
`integral.primitive_orbits` maps each of `O`, `SO`, `O+`, `SO+`, `Otilde`, `SOtilde`, `Otilde+` and `SOtilde+` to the coefficients `constant`, `z` and `w` of the series $F_{L,\Gamma}(z, w)$ of the numbers of $\Gamma$-orbits of primitive vectors of each norm, null where a coefficient is not known (`theory/orbits.md`).

### Orthogonal, arithmetic and Lie groups

A nondegenerate lattice card records the lattice $L$, not the groups built from it. Its canonical integral orthogonal group is $O(L)$, and base change gives an inclusion
$$
O(L) \hookrightarrow O(L_{\mathbb R}), \qquad L_{\mathbb R}=L\otimes_{\mathbb Z}\mathbb R.
$$
If $L$ has signature $(p,q)$, the real quadratic space determines the Lie group $O(L_{\mathbb R})$, which is isomorphic to the canonical Lie-group card $O(\min(p,q),\max(p,q))$. The isomorphism to the standard $O(p,q)$ model is not a choice of basis stored on the lattice card.

`lie-groups/<slug>.md` owns the Lie group itself: dimension, real rank, components, Lie algebra, maximal compact factors and references. Real orthogonal cards use slugs `o-p-q` with $p\leq q$.

`arithmetic-groups/<slug>.md` owns a stored arithmetic group such as $O(L)$, $SO(L)$, $O^+(L)$, $\widetilde O(L)$ or a named subgroup such as $\Gamma_{\mathrm{En},2}$. The card names its lattice, its ambient Lie group, its parent arithmetic group when one is stored, and any generators, index, orbit representatives or cited group description. Supplied generators describe that arithmetic-group card; they never stand in for the canonical mathematical object $O(L)$.

A lattice uses `orthogonal_group` when the database has a first-class card for its $O(L)$ and `arithmetic_groups` for the arithmetic-group cards attached to it. A lattice need not materialize an $O(L)$ card merely to know its ambient real Lie group; its signature already determines the link to `o-p-q`.

`integral.overlattice_count` is the number of integral lattices $M$ with $L \subseteq M \subseteq L^*$, with $M = L$ counted.
A lattice $M \supseteq L$ of finite index is integral exactly when $H = M/L$ is a subgroup of the discriminant group $A_L = L^*/L$ on which the form $b_{A_L}(x + L, y + L) = b(x, y) + \mathbb{Z}$ vanishes, so the field is the number of those subgroups.
It counts subgroups, not their orbits under the isometries of $L$, and it counts every integral $M$: for an even $L$ some $M$ can be odd.
For $U(2)$ the count is 4, and 3 of the 4 lattices are even.
Certification asks the exact lattice/discriminant-form API for this cardinality. If that computation has not completed, the field is absent and uncertified; there is no approximation or subgroup-count cutoff.

`integral.delta` is Nikulin's invariant $\delta$ of an even lattice with $2 A_L = 0$, and it is required for exactly those lattices, $A_L = 0$ included: 0 when $b(x, x)$ is an integer for every $x$ in $L^*$, and 1 otherwise.
With the rank $r$ and $A_L \cong (\mathbb{Z}/2)^a$ it gives Nikulin's $(r, a, \delta)$.
Because $2 L^* \subseteq L$, every $2 b(x, y)$ with $x, y \in L^*$ is an integer, so $\delta = 0$ exactly when every diagonal entry of $G^{-1}$ is an integer.

`integral.bad_reduction_primes` stores the preamble-returned set $\Sigma_L$ of primes that divide $2 \det L$ when that computation has been populated.
`integral.quadratic_character` is, for rank $2m$ and a nonzero determinant, the discriminant of $\mathbb{Q}(\sqrt{D})$ with $D = (-1)^m \det L$, and 1 when $D$ is a square.
The mathematical relation of these fields to zeta functions of the quadrics $Q(x)=n$ is documented on `theory/zeta.md`; the site does not derive those formulas from the card.

`fields.html` is generated from `model.py`.

The fields that a person writes follow these conventions:

| Field | Convention | Examples |
| --- | --- | --- |
| `name` | Plain text, as the lattice is written on a blackboard: `+` for the orthogonal sum, `^n` for a power, `*` for the dual lattice, `(k)` for the form scaled by $k$, `<a>` for the rank-one lattice with $b(e, e) = a$ | `E8`, `A3*`, `U + E8(-1)`, `E8^2 + A1`, `<2> + <-2>`, `I_{1,3}`, `I_{11,0}`, `affine D5`, `Lambda10` |
| `latex` | The same name as TeX, without `$` | `E_{8}`, `A_{3}^{*}`, `U \oplus E_{8}(-1)`, `\langle 2 \rangle`, `\mathrm{I}_{1,3}`, `\mathrm{I}_{11,0}`, `\widetilde{D}_{5}`, `\Lambda_{10}` |
| `aliases` | Other names in the literature and the names of the same lattice in other conventions, each as plain text; the name of the entry when the source is a catalogue | `II_{4,4}`; `LAMBDA16`, `BW16`, `Barnes-Wall lattice`; `(r, a, delta) = (15, 7, 1)` |
| `families` | Keys of `families.yaml`. Membership is stored explicitly; the build never derives family membership from invariants. To add a family, add its key and one line of meaning to `families.yaml` in the same change as its first member | `irreducible-root-lattice`, `even-unimodular`, `laminated` |
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
When a record leaves the corpus, its tag goes to `retired-tags.yaml` with the lattice that was there and why it is not a record. Verification reports a reused tag.
The address of a lattice is `tag/<TAG>.html`.

## Workflows

**Seed:** `just seed` converts stored source rows into `lattices/<TAG>.md`. Each card keeps its permanent tag, defining Gram tensor, source identity and citation. Seeding reads the source rows and writes cards.

**Author:** Write or edit `lattices/<TAG>.md` for a lattice without a stored source row. The tag names its permanent page. State only data and claims that the card can support.

**Enrich:** `just enrich` calls preamble-owned operations and stores their returned values on existing cards without changing certification status. A sparse card remains a site card while it awaits preamble computation.

**Certify:** `just certify` is the CI orchestration phase. It asks the preamble for each uncertified result, replaces a disagreeing authored value with the returned value, and only then writes the certificate hash to the card and certificate log.

**Verify:** `just verify` performs structural/reference/certificate-coherence checks only. Mathematical validation is a CI construction step: CI instantiates the relevant preamble lattice, morphism, group or other mathematical object, and validity is enforced by that object's constructor. Lattice-db does not run a second mathematical checker. Archived intake sources are not verification oracles. `just build` reads cards and renders stored values.

## Certificates

For a fixed input, a completed computation certifies its value permanently.
The value itself is stored only on the lattice card. The card's `certifications` map cites one SHA-256 certificate hash for each completed computation. That hash commits to the computation name, the card's Gram tensor and the stored result. `certificates.yaml` stores the same hash with the program and version that computed it, but does not duplicate the result. Thus a certificate states a fact $I(G)=v$ without creating a second store of $v$. It does not expire when the implementation changes. Editing $G$ or $v$ breaks the card's hash commitment; a computation that times out or otherwise does not finish has no certificate.

| Name | Computation | Inputs |
| --- | --- | --- |
| `<tag> derive` | Preamble-returned fields serialized by ordinary enrichment | The Gram tensor |
| `<tag> <block>.<field>` | A value returned by a preamble operation, such as `0012 integral.genus_symbol` | The Gram tensor |

`latticedb certify` requests a preamble computation exactly when the card does not already cite the matching completed certificate. It writes the returned result to the card whether or not an authored value was already present, then writes the hash citation to `certifications` and writes only the hash and computation provenance to `certificates.yaml`.

Run ordinary enrichment for selected cards with `just enrich --tag <tag>`. Certification is run by the nightly CI certification workflow; a selected card can be certified explicitly with `just certify --tag <tag>` when debugging that workflow.

## Morphisms

A lattice card owns every stored morphism whose domain is that lattice. Each item of its `morphisms` list names the target card and records a map $\varphi:S(c)\to T$ with $b_T(\varphi x,\varphi y)=c\,b_S(x,y)$. The domain is therefore structural and is not duplicated inside the morphism.

```yaml
morphisms:
- target: 027E
  name: $U \oplus E_8(-1) \hookrightarrow U^3 \oplus E_8(-1)^2$
  description: The inclusion as the first summand $U$ and the first summand $E_8(-1)$.
  matrix:
  - [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  - ...
  row_subdivisions: [2, 4, 6, 14]
  column_subdivisions: [2]
```

The matrix is in the bases of the two records, with rank $T$ rows and rank $S$ columns: column $j$ lists the coordinates of $\varphi(e_j)$.
A morphism with `scale: c` has domain the twist $S(c)$ of its source card $S$, so $b_T(\varphi x,\varphi y)=c\,b_S(x,y)$. This is notation for that map, not a database normalization rule: $S(c)$ may itself also have a lattice card.
The subdivisions are the lines of a block matrix, as SageMath's `M.subdivisions()` returns them: a line $k$ lies between rows (or columns) $k$ and $k + 1$.
Verification checks that $M^{\top} G_T M = c \, G_S$, and that the parts that the lines cut are orthogonal summands of $T$ (rows) and of $S$ (columns).

`latticedb enrich --summand-maps` writes the resulting embeddings on their source lattice cards, with each morphism naming its orthogonal-sum target $T$.
The orthogonal summands of $T$ are the connected components of the graph on its basis in which $e_i$ and $e_j$ are adjacent when $b(e_i, e_j) \neq 0$; group them by their Gram matrix, $T = \bigoplus_M M^{n_M}$.
The diagonal $x \mapsto (x, \ldots, x)$ embeds $M(k)$ into $M^k$.
For each $M$, a partition $\lambda$ of an integer $m \leq n_M$, with its parts placed on consecutive summands, gives an embedding $\bigoplus_M \bigoplus_j M(\lambda_j) \to T$; with $g = \gcd_j \lambda_j$, it is a morphism of scale $g$ from the record with the summands $M(\lambda_j / g)$, when the corpus holds one.
Up to the permutations of isometric summands there are $\prod_M \sum_{m \leq n_M} p(m)$ such embeddings, with $p$ the partition function; the identity of $T$ is not written.

The page of the source lattice renders its outgoing morphisms and matrices. The page of a target lattice derives its incoming-morphism links by indexing all source cards; incoming maps are never stored a second time.

`just morphism S T --name ... --matrix ...` appends the morphism to lattice card `S`. Scheduled verification checks its equation.
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
| `signature` | nondegenerate lattices of signature (p, q); repeat for both orders | `database.html?signature=2,3&signature=3,2` |

## Commands

The `latticedb` command line owns the four workflows, the build and deployment.
The `justfile` calls it.

| Recipe | Effect |
| --- | --- |
| `just seed` | Convert stored source rows into permanent lattice cards |
| `just new ...` | Author a lattice card from a Gram tensor and supplied fields |
| `just morphism S T ...` | Append a morphism with domain `S` and codomain `T` to lattice card `S` |
| `just enrich ...` | Compute and store additional fields on existing cards |
| `just certify ...` | CI orchestration: store preamble-returned uncertified scopes and attach certificate hashes |
| `just verify` | Report schema/reference/certificate-coherence errors |
| `just duplicates` | List the tags that share a Gram tensor |
| `just build` | Render every lattice card into `_site/` |
| `just deploy` | Build, link `_site/` to `/var/www/static-sites/lattice-database`, and check that nginx serves it |
| `just tag` | Print the tag for the next new record |
| `just test` | Run only preamble-free data-model/schema coherence tests; this is the local sub-second gate |
| `just test-validation` | CI-only mathematical and integration validation under Sage/preamble |
| `just test-source-intake` | Exercise archived-source importers and source-to-card collation; provenance only |

`just test` must not import Sage or `dzack_research`. The schema layer parses stored data and checks internal shape/coherence only. Mathematical validation in CI is performed by construction of the corresponding preamble objects; underlying algorithms and constructor contracts are tested at their preamble owners.

`just test-source-intake` exercises the Hashimoto and Höhn--Mason readers and their collation against the cards produced from those sources. These tests detect importer/transcription drift. They do not certify a lattice invariant and do not contribute to `just verify`.

The build needs `pandoc` on `PATH`. The pages load MathJax and DataTables from a CDN. Ordinary enrichment uses the preamble's lattice computations. `latticedb certify` needs SageMath at `$SAGE_BIN` for the expensive certification computations.

## Sources to absorb

For source intake, search the local Zotero library first. Read the source's attached extraction and PDF before searching outside Zotero.

The corpus must absorb the whole Catalogue of Lattices (G. Nebe, N. J. A. Sloane), <https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/>.
`sources/nebe_sloane/` holds the absorbed entries and the catalogue's `union.gz` archive. The definite records include the laminated lattices $\Lambda_9$ to $\Lambda_{20}$, $K_{12}$, $\kappa_7$ to $\kappa_9$, $BW_{16}$, the Leech lattice $\Lambda_{24}$, the 23 other Niemeier lattices, and the binary `BGF.2.2112`, `BGF.2.213`, `BGF.2.214`, and `BGF.2.216` entries.

The work that remains, in order:

1. Absorb the remaining entries of the bulk archive.
   The archive is stored at `sources/nebe_sloane/union.gz`. Its `D_n*` entries print exact halves, while `Bring8` and `mcc` print rounded decimal Gram components that require source-specific exact data. The `Shimada_86` entry has two conflicting matrices: its full `GRAM_MATRIX` is positive definite with the stated determinant, while its lower-triangular `GRAM` is indefinite and has a different determinant. The [source audit](sources/INVARIANT-AUDIT.md#shimada_86-source-conflict) records the exact comparison. Source entries are not discarded merely because their forms are scalar twists of other lattice cards.

Source intake is one-way. A source contributes the claims it states — Gram tensors, identifications, invariants, relations, generators and maps — and every claim that belongs to the mathematical corpus lands in the appropriate card, relation, morphism or catalogue record. The source can be used to check that this seeding/import step copied what it was meant to copy, but it is not an oracle afterward. Computable claims are certified independently by mathematics or computation from the stored defining data. Two sources stating the same value are useful provenance, but agreement between sources is not a substitute for certification.

- **Watson's single-class genera**, `Classi/watson` on the catalogue site: 3494 primitive lattices of one class per genus, in machine-readable rows of the lower-triangular Gram entries, dimension by dimension; Lorch's completion is arXiv:1208.5638. A module `latticedb watson` reads it, and each genus's stored `integral.genus_class_count = 1` checks the table's claim.

- **The Brandt-Intrau-Schiemann tables** of odd and even primitive positive ternary forms of discriminant at most 1000, `Brandt_1.html` and `Brandt_2.html` on the catalogue site, as recomputed by Schiemann: rank-3 integral records with genus data.

- **The rank-3 Lorentzian lattices of Allcock, in Dutour-Sikiric's database**, <https://github.com/MathieuDutSik/GeometryDatabase_Rank3_Lorentzian_lattices>: the file `RK3_all` holds 3441 lattices, each row the Gram matrix, the simple roots, the source label `W` for the Weyl group and the ordinal `L` of the lattice within that group, in PARI-readable form; these labels are neither group orders nor subgroup indices (converted to GAP by `Convert_Allcock_RK3`). Every row is read on 2026-10-02: 3415 have signature $(2,1)$, 25 signature $(1,2)$ and one is positive definite; 933 are even and 2508 odd.
  This is the source of indefinite records the Catalogue does not give (it supplies one, `Shimada_86`): rank-3 indefinite integral lattices with their roots, which is exactly what `root_span` and the `hyperbolic` block ask for, and `RK3_explicit` (704) and `RK3_implicit` (715) split the reflective and non-reflective lists of Allcock's 1989 Bielefeld preprint.
  A module `latticedb allcock` reads `RK3_all`; scalar twists or sign changes are not automatically identified with existing cards.
  Reached from Martinet's page of links to those working on lattices, <http://jamartin.perso.math.cnrs.fr/>.

- **AN06 — Alexeev and Nikulin, *Del Pezzo and K3 Surfaces* (2006)**, <https://arxiv.org/abs/math/0406536>: start with the Zotero item `RYAAK5WJ`, its attached extraction and PDF. Absorb every Coxeter diagram printed in its tables, including the reflection-chamber diagrams of Table 1 and the extremal K3 diagrams of Table 2, as weighted graph cards. Keep each table and row label, page, vertex marking, and edge weight with its source citation.

- **Jagy's table** of positive ternary forms that are spinor regular but not regular, `Jagy.txt` on the catalogue site: sextuples $(a, b, c, d, e, f)$ of a form's coefficients, so the Gram tensor is their symmetric matrix divided by 2.

- **Kirschmer's tables of genera of small class number**, <https://www.math.uni-bielefeld.de/~mkirschm/forms/>: a survey misread first, and now corrected. The page's own notation section states what each file holds: `res_orth.tar.bz2` is genera of *definite* quadratic lattices over *totally real number fields*, rank 3 to 16, class number 1 or 2, each genus printed as a diagonal matrix over $K$ with a $\mathbb{Z}_K$-module; `unimod.m` and the hermitian, quaternionic-hermitian and binary-form tables are likewise over number fields, and `maxgen.m` is one-class genera of maximal integral lattices over number fields. These are exact claims about lattices — over $\mathbb{Z}_K$, which the corpus has no record kind for. Absorbing them is the schema gaining that kind, an owner decision of some size, not a reason to discard the data; reading them for the $\mathbb{Z}$-lattice the $\mathbb{Z}$-trace or norm gives is a construction that would also need its place. The page is the citation the corpus already uses: the completeness of the class-number-one $\mathbb{Z}$-lattices rests on it (Watson, Kirschmer-Lorch arXiv:1208.5638), and it is the reference for a genus's class number stated in prose.
  Indefinite records over $\mathbb{Z}$ arrive meanwhile from the rank-3 Lorentzian database above and from papers (Nikulin's tables, Hashimoto, Gritsenko–Hulek–Scholsche, the K3 and Leech coinvariant lattices).

- **LMFDB's lattices collection**, <https://beta.lmfdb.org/Lattice/>: 39,293 positive definite integral lattices, dimensions at most 24, the largest class number 56. The Source page states the Gram matrices come from the Catalogue and its tables. The data of Haensch and Anni (<https://github.com/annahaensch/lattice_data>, Magma and PARI) include `class_number`, automorphism-group order and generators, `level`, theta coefficients and `genus_reps`. The record fields hold class number, group order, level and theta data; named subgroup morphisms and `genera/` hold the group and genus claims when entries are identified. The two representatives of genus `3.11.22` are the forms `1 2 6 2 0 0` and `1 1 11 0 0 0` that Brandt–Intrau–Schiemann prints under discriminant $-44$. The Source page cites Kirschmer and Lorch, arXiv:1208.5638, for the completeness of class-number-one lattices.
  The stored `density` and `hermite` are exact mathematics printed as decimals, the schema's standing case of it: the Hermite invariant $\gamma_n(L)=\lambda_1/\det^{1/n}$ and the packing density $\Delta(L)=V_n(\sqrt{\lambda_1}/2)/\sqrt{\det}=\pi^{n/2}\lambda_1^{n/2}/\bigl(2^n\,\Gamma(\tfrac n2+1)\sqrt{\det}\bigr)$ — $\pi/4$ for $\mathbb{Z}^2$, $\pi^4/384$ for $E_8$.   Sampled against the API on 2026-10-02 at rows of dimensions 2 to 24: both formulas reproduce the stored values to the full printed precision except the last one or two digits, whose rounding mode varies by row — a rendering choice, which is why the absorption takes the formula and never the decimal. The values lie in $\mathbb{Q}(\pi^{n/2}, \sqrt{\det})$, a symbolic real a record can hold exactly. `shortest` gives coordinates in the printed basis and is the row's choice of basis, not a claim.
  The API route is <https://beta.lmfdb.org/api/lat_lattices/?_format=json>, read on 2026-10-02: it answers only for a client that first loads a page of the site and returns its `human=1` cookie, the beta gate; a request without it is redirected.
  A module reading this source needs that two-step fetch.

- **Martinet's perfect lattices**, <http://jamartin.perso.math.cnrs.fr/Lattices/index.html>: the perfect lattices of dimensions at most 7 in `perf2to7` and the dimension-8 sets in PARI/GP files (`p8.gp.gz` and siblings), readable by `cypari2`; perfectness is a property a record states in its prose, and the Grams are definite integral records.

- **Borcherds's tables of lattices**, <http://math.berkeley.edu/~reb/lattices/>: for each of the 665 odd unimodular and 121 even determinant-2 lattices of dimension 25 the root system, the order of the orthogonal group modulo the reflection group, and the orbits of norm $0,-2,-4,-6$ vectors of $I\!I_{25,1}$ with coordinates and simple-root counts; King's table of masses of the 32-dimensional even unimodular lattices by root system; the `norm*` and Magma-format files, all read on 2026-10-02. It prints no Gram tensor, so it writes no record — its claims land on records the corpus already holds: the twenty-four norm-zero vectors identify the Niemeier lattices as the orthogonal complements of norm-zero vectors of $I\!I_{25,1}$, which is `related` material and outgoing morphism data on the twenty-three Niemeier cards, with the page as the reference; the root system and the group order are the same fields of the rank-25 positive-definite records, the order derived from the stated group structure: Table −2 gives $|O(L)|=|R||G|$ for the even determinant-2 case, while Table −4 gives $|O(L)|=2|R||G|$ for the odd unimodular case, with $R$ the root-reflection group and $G$ the chamber stabilizer — these table values require the identified action before comparison with `definite.automorphism_group_order`; King's mass is a genus-level statement about the 32-dimensional records the corpus does not yet have, to be carried when they arrive.

- **Cohn's kissing-number table**, <https://cohn.mit.edu/kissing-numbers>: the best known bounds per dimension, its lower bounds originally the Catalogue's table and later improvements naming their lattices — a citation for `definite.kissing_number` and, where a record attains a bound stated elsewhere, an outside table the field checks against.

- **Dutour-Sikiric's Delaunay polytopes of the Niemeier lattices**, <https://github.com/MathieuDutSik/delaunaypolytopeniemeier.github.io>: the `lattice-polytopes/` schema can record their vertices and Delaunay sphere in the basis of each Niemeier lattice. The source values and coordinate identifications remain to be imported.

- **Sloane's packing tables**, <https://neilsloane.com/packings/>: the best known sphere packings by dimension, one file per configuration. The lattice files are exact: `E8.8.240.txt` (read on 2026-10-02) prints the 240 minimal vectors of $E_8$ as integer rows in an orthonormal coordinate system, with a comment citing SPLAG page 120 — that is $\Phi(L)$ for a record the corpus holds, landing as `definite.roots` and the kissing count of the $E_8$ record, an identification and a check, the same kind of claim the Catalogue's entry carries. The non-lattice files are point configurations — the 3-simplex file is four rows of $\pm 1/\sqrt{3}$, verified to be the correctly-rounded exact values — objects the schema has no place for; under the rule that a claim with no place gains one, that placement is a schema question, and the decimals are a rendering of it, not a reason the data is discarded.

Sources read on 2026-10-02 that yield nothing, each because the page is not data or is not there — never inexactness of a rendering, and never because another source names the same lattice:

- Scholl's packungen site, <http://www.home.unix-ag.org/scholl/packungen/>: an interactive search over images, no lattice data to read.
- Schiemann's extrep pages: moved with his KIT group and not answering as data on 2026-10-02.
