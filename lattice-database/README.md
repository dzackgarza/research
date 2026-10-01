# Lattice database

A catalogue of lattices.
A *lattice* here is a free module $L$ of finite rank over $\mathbb{Z}$ with a symmetric bilinear form $b \colon L \times L \to \mathbb{Q}$.
The form can be definite, indefinite or degenerate, and its values need not be integers.

Each lattice has one Markdown file, `lattices/<TAG>.md`. The YAML front matter of the file is the record of the lattice; the body is prose about it.
The build validates every record, writes one page for each lattice, and writes one table, with one row per record, that the database page filters, sorts and exports.

The site is served at <http://lattice-database.localhost/>.

## Layout

| Path | Contents |
| --- | --- |
| `lattices/<TAG>.md` | One record and its prose for each lattice |
| `families.yaml` | Every family that a record may name, with one line of its meaning |
| `retired-tags.yaml` | Every tag whose record the corpus no longer admits, with the lattice that was there and the twist of a record that it is |
| `morphisms/<S>-<T>.md` | Morphisms from the lattice `S` to the lattice `T`, as matrices, and prose |
| `pages/<slug>.md` | One collection page: conditions on the database rows, and prose |
| `theory/<slug>.md` | One theory page: the definitions and conventions that the other pages link to |
| `src/latticedb/model.py` | The schema of a record and of a morphism file, and their validators |
| `src/latticedb/arithmetic.py` | Exact arithmetic on the Gram tensor that the validators use |
| `src/latticedb/root_systems.py` | The types of the irreducible root systems, their Cartan data and the lattices that they generate |
| `src/latticedb/roots.py` | $\Phi(L)$ of a definite lattice as its irreducible components; roots that generate $\mathbb{Z}\Phi(L)$ for the others |
| `src/latticedb/records.py` | Computes the fields of a record that the Gram tensor determines, and writes a record as a file |
| `src/latticedb/nebe_sloane.py` | Reads an entry of the Catalogue of Lattices (G. Nebe, N. J. A. Sloane) and writes it as the declared fields of a record |
| `src/latticedb/hashimoto.py` | Reads Tables 10.2 and 10.3 of Hashimoto, the finite symplectic groups of the K3 lattice, checks every equation they state against the records, and checks that the morphism files embed each $\Lambda^G$ and its $\Lambda_G$ in the K3 lattice as orthogonal primitive sublattices |
| `src/latticedb/hoehn_mason.py` | Reads the coinvariant lattices of the Leech lattice of Höhn and Mason, computes their inclusions in the Leech lattice and the actions of their stabilizers, and checks them against the records, Table 10.2 of Hashimoto and the morphism files |
| `src/latticedb/corpus.py` | Reads all records and checks the statements that concern more than one record |
| `src/latticedb/site.py` | Builds the site |
| `src/latticedb/templates/`, `assets/` | Page templates, styles and the database script |
| `sources/nebe_sloane/<ENTRY>.json` | An entry of the Catalogue of Lattices as fetched, the source of the record that cites it |
| `sources/hashimoto/table_10_2.json`, `table_10_3.json` | Tables 10.2 and 10.3 of K. Hashimoto, arXiv:1012.2682, as printed, each row linked to the records of $\Lambda_G$ and $\Lambda^G$ by a twist and a change of basis |
| `sources/hoehn_mason/leech.json`, `lattices_<i>_<j>.json` | The Leech lattice and the 40 entries `lattices[i,j]` of the Magma file of G. Höhn and G. Mason, arXiv:1505.06420, whose coinvariant lattice is $\Lambda_G(-1)$ for a row of Table 10.2 of Hashimoto: the bases and the stabilizer generators as printed, each linked to its record by a twist and a change of basis |
| `tests/` | Tests of the validators, of the record commands and of the built site |

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
The Gram tensor determines `rank`, `signature`, `determinant`, `definiteness`, `integral.parity`, `integral.discriminant_group`, `integral.overlattice_count`, `integral.delta`, `definite.minimum`, `definite.kissing_number`, `definite.theta_series`, `definite.root_system`, `definite.roots`, `indefinite.isotropic`, `root_span.norms` and `root_sublattice`. `latticedb new`, `latticedb nebe-sloane` and `latticedb derive` compute them once, with exact arithmetic, when they write the record.
`latticedb new` refuses a Gram tensor that is not symmetric or is a twist, a declared value that is false, and a definite lattice isometric to a record of the corpus.
The build reads the stored values and computes nothing again.
`latticedb check` computes again only the equations that the files under `sources/` state.
A person writes `name`, `latex`, `aliases`, `families`, `related`, `references` and the prose.
A person also writes `integral.genus_symbol` and `integral.genus_class_count`, computed from the Gram tensor with `Genus` of SageMath, and `definite.automorphism_group_order`, computed with `qfauto` of PARI/GP. `hyperbolic.reflective` and a `root_span` block that `latticedb new` could not decide are declared: the prose states the source of each one, and the page of the lattice marks `hyperbolic.reflective` *declared*.

An invariant that exists only under a hypothesis lives in a block named for the hypothesis.
A block on a lattice that does not satisfy the hypothesis is a validation error, and so is a field whose own hypothesis fails.

| Block | Hypothesis on the lattice | Fields |
| --- | --- | --- |
| `integral` | every $b(e_i, e_j)$ is an integer | `parity`, `discriminant_group`, `overlattice_count`, `delta`, `genus_symbol`, `genus_class_count` |
| `definite` | $b$ is positive or negative definite | `minimum`, `kissing_number`, `automorphism_group_order`, `theta_series`, `root_system`, `roots` |
| `root_span` | $b$ is not definite | `roots`, `norms`, `summands`, `embedding` |
| `root_sublattice` | $b$ is definite, or the record has `root_span` | `invariant_factors`, `norms` |
| `indefinite` | $b(x, x)$ takes both signs | `isotropic` |
| `hyperbolic` | $b$ is nondegenerate with signature $(1, n)$ or $(n, 1)$, rank at least 2 | `reflective` |

The `integral`, `definite`, `indefinite` and `root_sublattice` blocks are required when their hypotheses hold; `root_span` and `hyperbolic` are optional.
`definite.theta_series` and `definite.root_system` are required exactly when the lattice is integral, and `definite.automorphism_group_order`, `integral.genus_symbol` and `integral.genus_class_count` are optional.

`integral.overlattice_count` is the number of integral lattices $M$ with $L \subseteq M \subseteq L^*$, with $M = L$ counted.
A lattice $M \supseteq L$ of finite index is integral exactly when $H = M/L$ is a subgroup of the discriminant group $A_L = L^*/L$ on which the form $b_{A_L}(x + L, y + L) = b(x, y) + \mathbb{Z}$ vanishes, so the field is the number of those subgroups.
It counts subgroups, not their orbits under the isometries of $L$, and it counts every integral $M$: for an even $L$ some $M$ can be odd.
For $U(2)$ the count is 4, and 3 of the 4 lattices are even.
The record commands enumerate the subgroups of $A_L$, so the field is stated exactly when the determinant is not zero and $A_L$ has at most 100000 subgroups.
A record without it is not decided, and its page says so: $(\mathbb{Z}/2)^8$ has 417199 subgroups.

`integral.delta` is Nikulin's invariant $\delta$ of an even lattice with $2 A_L = 0$, and it is required for exactly those lattices, $A_L = 0$ included: 0 when $b(x, x)$ is an integer for every $x$ in $L^*$, and 1 otherwise.
With the rank $r$ and $A_L \cong (\mathbb{Z}/2)^a$ it gives Nikulin's $(r, a, \delta)$.
Because $2 L^* \subseteq L$, every $2 b(x, y)$ with $x, y \in L^*$ is an integer, so $\delta = 0$ exactly when every diagonal entry of $G^{-1}$ is an integer.

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
   For an entry of the Catalogue of Lattices, `just nebe-sloane LAMBDA10 --name Lambda10 --latex '\Lambda_{10}' --family laminated` reads `sources/nebe_sloane/LAMBDA10.json`, fetches it first when it does not exist, checks the rank, determinant, minimum and kissing number that the catalogue states against the Gram tensor, and writes the record with the reference of the entry.
   The command refuses a record that does not validate, that is a twist $M(n)$ with $n \neq 1$ of the lattice the corpus records (other than a twist by 2 in the family `nikulin-two-elementary`), that repeats the name or the components of a record in the corpus, that is definite and isometric to a record in the corpus, or that names a family not in `families.yaml`, and writes nothing.

3. Edit the file: add `related` entries, the prose, and the declared fields with their sources.
   For a record that is not definite whose `root_span` block the command could not decide, write the block and its proof by hand.

4. `just build` validates the corpus and builds the site.
   It prints each problem of each record with the path of the file and the field.

The corpus is also checked as a whole: two records cannot have the same name or the same components, two definite records cannot be isometric, a `related` entry must name a tag in the corpus, and a family must be a key of `families.yaml`. Isometry is decided by `qfisom` only for the pairs whose rank, determinant, minimum, kissing number, root system, theta series and discriminant group agree.

`just derive` computes again, in every record, each field that the Gram tensor determines, and writes the records that change.
Run it after a change to the computation, and read the diff.

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
| `just derive` | Compute again, in every record, each field that the Gram tensor determines; write the records that change |
| `just build` | Validate every record and build the site into `_site/` |
| `just deploy` | Build, link `_site/` to `/var/www/static-sites/lattice-database`, and check that nginx serves it |
| `just tag` | Print the tag for the next new record |
| `just test` | Run the tests |

`uv run latticedb check` validates the records, checks them against the files under `sources/hashimoto/` and `sources/hoehn_mason/`, checks that the morphism files hold the maps that `sources/hoehn_mason/` determines and the embeddings of $\Lambda^G$ and $\Lambda_G$ in the K3 lattice `027E` as orthogonal primitive sublattices, and builds nothing.

The build needs `pandoc` on `PATH`. The pages load MathJax and DataTables from a CDN. The record commands compute with PARI/GP through `cypari2` and with `python-flint`.

## Sources to absorb

The corpus must absorb the whole Catalogue of Lattices (G. Nebe, N. J. A. Sloane), <https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/>, with its indefinite lattices first.
`sources/nebe_sloane/` holds the 41 entries absorbed so far, all definite: the laminated lattices $\Lambda_9$ to $\Lambda_{20}$, $K_{12}$, $\kappa_7$ to $\kappa_9$, $BW_{16}$, the Leech lattice $\Lambda_{24}$ and the 23 other Niemeier lattices.

The work that remains, in order:

1. Find the indefinite entries.
   The index page, read on 2026-10-01, contains none of the words "indefinite", "hyperbolic", "Lorentzian" and "signature"; its sections are ordered by dimension and by class (root, laminated, modular, unimodular, perfect, Niemeier, the tables of quaternary and quinary forms).
   The entry pages were not read, so the signature of each entry is not known: read every entry page and compute the signature from its Gram tensor.

2. Make `just nebe-sloane` admit an indefinite entry.
   `nebe_sloane.check` compares the minimum and the kissing number that the catalogue states, which an indefinite lattice does not have.

3. Absorb the indefinite entries, then the definite ones.
   The twist and sign rules under *A record* apply: an entry that is $M(n)$ for an integer $n \geq 2$, or the negative of the lattice the corpus records, is not a record.
