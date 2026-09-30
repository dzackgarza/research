# Lattice database

A catalogue of lattices.
A *lattice* here is a free module $L$ of finite rank over $\mathbb{Z}$ with a symmetric bilinear form $b \colon L \times L \to \mathbb{Q}$.
The form can be definite, indefinite or degenerate, and its values need not be integers.

Each lattice has one Markdown file, `lattices/<TAG>.md`. The YAML front matter of the file is the record of the lattice; the body is prose about it.
The build validates every record, writes one page for each lattice, and writes the union of the records as one table that the database page filters, sorts and exports.

The site is served at <http://lattice-database.localhost/>.

## Layout

| Path | Contents |
| --- | --- |
| `lattices/<TAG>.md` | One record and its prose for each lattice |
| `families.yaml` | Every family that a record may name, with one line of its meaning |
| `pages/<slug>.md` | One collection page: conditions on the database rows, and prose |
| `src/latticedb/model.py` | The schema of a record and its validators |
| `src/latticedb/arithmetic.py` | Exact arithmetic on the Gram tensor that the validators use |
| `src/latticedb/root_systems.py` | The types of the irreducible root systems, their Cartan data and the lattices that they generate |
| `src/latticedb/roots.py` | $\Phi(L)$ of a definite lattice as its irreducible components; roots that generate $\mathbb{Z}\Phi(L)$ for the others |
| `src/latticedb/records.py` | Computes the fields of a record that the Gram tensor determines, and writes a record as a file |
| `src/latticedb/nebe_sloane.py` | Reads an entry of the Catalogue of Lattices (G. Nebe, N. J. A. Sloane) and writes it as the declared fields of a record |
| `src/latticedb/corpus.py` | Reads all records and checks the statements that concern more than one record |
| `src/latticedb/site.py` | Builds the site |
| `src/latticedb/templates/`, `assets/` | Page templates, styles and the database script |
| `sources/nebe_sloane/<ENTRY>.json` | An entry of the Catalogue of Lattices as fetched, the source of the record that cites it |
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
  genus_symbol: II_{1,1}
indefinite:
  isotropic: true
families: [even-unimodular]
provenance:
  source: Constructed in SageMath. The invariants were computed from the Gram tensor.
---

$U$ is the lattice with basis $e, f$ and $b(e, e) = b(f, f) = 0$, $b(e, f) = 1$.
```

`gram_tensor` is the defining datum: the components $b(e_i, e_j)$ of the Gram tensor $b$, a symmetric $(0,2)$-tensor, in a basis $e_1, \dots, e_n$ of $L$.
A component is an integer or a string `p/q`. Floats are refused.

The fields of a record are of two kinds.
The Gram tensor determines `rank`, `signature`, `determinant`, `definiteness`, `integral.parity`, `integral.discriminant_group`, `definite.minimum`, `definite.kissing_number`, `definite.theta_series`, `definite.root_system`, `definite.roots` and `indefinite.isotropic`. `latticedb new` computes them, and the build computes each again with exact arithmetic and rejects a record that states another value: a record with `signature: [2, 0]` and the components above is rejected.
A person writes `name`, `latex`, `aliases`, `families`, `related`, `references`, `provenance` and the prose, and declares `integral.genus_symbol`, `definite.automorphism_group_order`, `hyperbolic.reflective` and a `root_span` block that `latticedb new` could not decide, each with its source in the prose.
The page of the lattice marks each declared value *declared*; every other value on the page, the build computed.

An invariant that exists only under a hypothesis lives in a block named for the hypothesis.
A block on a lattice that does not satisfy the hypothesis is a validation error, and so is a field whose own hypothesis fails.

| Block | Hypothesis on the lattice | Fields |
| --- | --- | --- |
| `integral` | every $b(e_i, e_j)$ is an integer | `parity`, `discriminant_group`, `genus_symbol` |
| `definite` | $b$ is positive or negative definite | `minimum`, `kissing_number`, `automorphism_group_order`, `theta_series`, `root_system`, `roots` |
| `root_span` | $b$ is not definite | `roots`, `summands`, `embedding` |
| `indefinite` | $b(x, x)$ takes both signs | `isotropic` |
| `hyperbolic` | $b$ is nondegenerate with signature $(1, n)$ or $(n, 1)$, rank at least 2 | `reflective` |

The `integral`, `definite` and `indefinite` blocks are required when their hypotheses hold; `root_span` and `hyperbolic` are optional.
`definite.theta_series` and `definite.root_system` are required exactly when the lattice is integral, and `definite.automorphism_group_order` and `integral.genus_symbol` are optional.

The page `fields.html` of the site documents every field.
The build generates it from the schema, so it states what the validators enforce.

The fields that a person writes follow these conventions, so that the database reads as one hand wrote it:

| Field | Convention | Examples |
| --- | --- | --- |
| `name` | Plain text, as the lattice is written on a blackboard: `+` for the orthogonal sum, `^n` for a power, `*` for the dual lattice, `(k)` for the form scaled by $k$, `<a>` for the rank-one lattice with $b(e, e) = a$ | `E8`, `A3*`, `U + E8(-1)`, `E8^2 + A1`, `<2> + <-2>`, `I_{1,3}`, `Z^11`, `affine D5`, `Lambda10` |
| `latex` | The same name as TeX, without `$` | `E_{8}`, `A_{3}^{*}`, `U \oplus E_{8}(-1)`, `\langle 2 \rangle`, `\mathrm{I}_{1,3}`, `\mathbb{Z}^{11}`, `\widetilde{D}_{5}`, `\Lambda_{10}` |
| `aliases` | Other names in the literature and the names of the same lattice in other conventions, each as plain text; the name of the entry when the source is a catalogue | `II_{4,4}`; `LAMBDA16`, `BW16`, `Barnes-Wall lattice`; `(r, a, delta) = (15, 7, 1)` |
| `families` | Keys of `families.yaml`. A family is a class of lattices that a definition cuts out, not a property that the build derives from the record: `even-unimodular` is a family because its members are a named series, and *unimodular* is a property. To add a family, add its key and one line of meaning to `families.yaml` in the same change as its first member; the build rejects a record whose family is not listed | `root-lattice`, `laminated`, `r-plus-a-22` |
| `related.relation` | One sentence, from this record to the related one, that states the map or the change of form; TeX between `\(` and `\)` | `The dual lattice, in the basis dual to the basis of this record.`; `The same module with the form \(-b\).`; `The same module with the form \(2b\).` |
| `references.citation` | Author initials and surnames, the title, and the locator that the source uses; with `url` when the source is on the web | `G. Nebe and N. J. A. Sloane, Catalogue of Lattices, entry LAMBDA9.`; `V. Alexeev, "Reflective hyperbolic 2-elementary lattices, K3 surfaces and hyperkahler manifolds", arXiv:2209.09110v4, Theorem 1.1.` |
| `provenance.source` | Where the Gram tensor comes from, then how the invariants were obtained, as one or two sentences | `Constructed in SageMath. The invariants were computed from the Gram tensor.`; `Catalogue of Lattices (G. Nebe, N. J. A. Sloane), entry LAMBDA9. The invariants were computed again from the Gram tensor.` |

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
When they do not generate $L$, the prose proves that no root of $L$ is outside the sublattice that they generate, and `root_span.summands` and `root_span.embedding` state $\mathbb{Z}\Phi(L)$ as an orthogonal sum of records with its embedding in $L$.
A root is a row of integers: its coordinates in the basis $e_1, \dots, e_n$ of the record.
The page of the lattice writes it as $\sum_i c_i e_i$, and states the orthogonal decomposition of $L$ that the basis gives.
A record that is not definite and has no `root_span` block is not decided, and its page says so.

## Tags

A tag is four characters from `0-9` and `A-Z`. The file name is the tag.
A tag is permanent: it never moves to another lattice, and a record is never renumbered.
The address of a lattice is `tag/<TAG>.html`.

To add a lattice:

1. Search the database page for the lattice, by name and by its invariants (rank, determinant, minimum, kissing number), so that a lattice already in the corpus under another basis or another name is not added twice.

2. `just new --gram '[[2, 1], [1, 2]]' --name A2 --latex A_2 --source '...'` writes `lattices/<TAG>.md` under the next tag, with every field that the Gram tensor determines computed.
   `--alias`, `--family`, `--reference`, `--url` and `--prose` give the other fields; `uv run latticedb new --help` lists them.
   For an entry of the Catalogue of Lattices, `just nebe-sloane LAMBDA10 --name Lambda10 --latex '\Lambda_{10}' --family laminated` reads `sources/nebe_sloane/LAMBDA10.json`, fetches it first when it does not exist, checks the rank, determinant, minimum and kissing number that the catalogue states against the Gram tensor, and writes the record with the reference and the provenance of the entry.
   The command refuses a record that does not validate, that repeats the name or the components of a record in the corpus, or that names a family not in `families.yaml`, and writes nothing.

3. Edit the file: add `related` entries, the prose, and the declared fields with their sources.
   For a record that is not definite whose `root_span` block the command could not decide, write the block and its proof by hand.

4. `just build` validates the corpus and builds the site.
   It prints each problem of each record with the path of the file and the field.

The corpus is also checked as a whole: two records cannot have the same name or the same components, a `related` entry must name a tag in the corpus, and a family must be a key of `families.yaml`.

`just derive` computes again, in every record, each field that the Gram tensor determines, and writes the records that change.
Run it after a change to the computation, and read the diff.

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

## The database page

`database.html` loads `lattices.json` and shows one row for each lattice.
It has filter panes for rank, definiteness, properties and families, a builder for conditions on any column, text search, column selection, and CSV export.

The query string selects filters, so a filtered view has an address:

| Parameter | Selects | Example |
| --- | --- | --- |
| `rank` | ranks | `database.html?rank=8,16` |
| `definiteness` | definiteness | `database.html?definiteness=positive definite` |
| `property` | properties; a row must have all of them | `database.html?property=even,unimodular` |
| `family` | families; a row must have all of them | `database.html?family=root-lattice` |
| `q` | text search | `database.html?q=Lambda` |

## Commands

The `latticedb` command line owns validation, the build and deployment.
The `justfile` calls it.

| Recipe | Effect |
| --- | --- |
| `just new ...` | Write the record of a new lattice from its Gram tensor and the options |
| `just nebe-sloane ENTRY ...` | Write the record of an entry of the Catalogue of Lattices |
| `just derive` | Compute again, in every record, each field that the Gram tensor determines; write the records that change |
| `just build` | Validate every record and build the site into `_site/` |
| `just deploy` | Build, link `_site/` to `/var/www/static-sites/lattice-database`, and check that nginx serves it |
| `just tag` | Print the tag for the next new record |
| `just test` | Run the tests |

`uv run latticedb check` validates the records and builds nothing.

The build needs `pandoc` on `PATH`. The pages load MathJax and DataTables from a CDN. The record commands compute with PARI/GP through `cypari2` and with `python-flint`, and `provenance.computed_with` names their versions.
