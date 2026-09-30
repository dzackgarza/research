# Lattice database

A catalogue of lattices. A *lattice* here is a free module $L$ of finite rank over
$\mathbb{Z}$ with a symmetric bilinear form $b \colon L \times L \to \mathbb{Q}$. The form
can be definite, indefinite or degenerate, and its values need not be integers.

Each lattice has one Markdown file, `lattices/<TAG>.md`. The YAML front matter of the file
is the record of the lattice; the body is prose about it. The build validates every record,
writes one page for each lattice, and writes the union of the records as one table that the
database page filters, sorts and exports.

The site is served at <http://lattice-database.localhost/>.

## Layout

| Path | Contents |
| --- | --- |
| `lattices/<TAG>.md` | One record and its prose for each lattice |
| `pages/<slug>.md` | One collection page: conditions on the database rows, and prose |
| `src/latticedb/model.py` | The schema of a record and its validators |
| `src/latticedb/arithmetic.py` | Exact arithmetic on the Gram tensor that the validators use |
| `src/latticedb/corpus.py` | Reads all records and checks the statements that concern more than one record |
| `src/latticedb/site.py` | Builds the site |
| `src/latticedb/templates/`, `assets/` | Page templates, styles and the database script |
| `scripts/` | The SageMath seed that wrote the first records, and its source data |
| `tests/` | Tests of the validators and of the built site |

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

`gram_tensor` is the defining datum: the components $b(e_i, e_j)$ of the Gram tensor $b$, a
symmetric $(0,2)$-tensor, in a basis $e_1, \dots, e_n$ of $L$. A component is an integer or
a string `p/q`. Floats are refused.

Every other invariant of a record is a declaration, and the build checks each declaration
against the Gram tensor with exact arithmetic. A record with `signature: [2, 0]` and the
components above is rejected.

An invariant that exists only under a hypothesis lives in a block named for the hypothesis.
A block on a lattice that does not satisfy the hypothesis is a validation error, and so is
a field whose own hypothesis fails.

| Block | Hypothesis on the lattice | Fields |
| --- | --- | --- |
| `integral` | every $b(e_i, e_j)$ is an integer | `parity`, `discriminant_group`, `genus_symbol` |
| `definite` | $b$ is positive or negative definite | `minimum`, `kissing_number`, `automorphism_group_order`, `theta_series`, `root_system` |
| `indefinite` | $b(x, x)$ takes both signs | `isotropic` |
| `hyperbolic` | $b$ is nondegenerate with signature $(1, n)$ or $(n, 1)$, rank at least 2 | `reflective` |

The `integral` block is required when its hypothesis holds; the other blocks are optional.

The page `fields.html` of the site documents every field. The build generates it from the
schema, so it states what the validators enforce.

The prose is Pandoc Markdown. `$...$` is inline TeX and `$$...$$` is display TeX.

## Tags

A tag is four characters from `0-9` and `A-Z`. The file name is the tag. A tag is permanent:
it never moves to another lattice, and a record is never renumbered. The address of a
lattice is `tag/<TAG>.html`.

To add a lattice:

1. `just tag` prints the next tag.
2. Write `lattices/<TAG>.md` with the record and the prose.
3. `just build` validates the corpus and builds the site. It prints each problem of each
   record with the path of the file and the field.

The corpus is also checked as a whole: two records cannot have the same name or the same
components, and a `related` entry must name a tag in the corpus.

## Collection pages

A file `pages/<slug>.md` gives the page `collection/<slug>.html`, which lists the lattices
whose database row satisfies every condition of `where`.

```yaml
---
title: Even unimodular lattices
summary: Integral lattices with determinant $1$ or $-1$ on which every value $b(x, x)$ is even.
where:
  properties: [even, unimodular]
---
```

A key of `where` is a key of a row of `lattices.json`, for example `rank`, `definiteness`,
`properties` or `families`. For a key whose value is a list, the list must contain each
required value. In `title` and `summary`, backticks mark code and dollar signs mark TeX.
The body is Pandoc Markdown. The build fails for a key that no row has and for a collection
with no member.

## The database page

`database.html` loads `lattices.json` and shows one row for each lattice. It has filter
panes for rank, definiteness, properties and families, a builder for conditions on any
column, text search, column selection, and CSV export.

The query string selects filters, so a filtered view has an address:

| Parameter | Selects | Example |
| --- | --- | --- |
| `rank` | ranks | `database.html?rank=8,16` |
| `definiteness` | definiteness | `database.html?definiteness=positive definite` |
| `property` | properties; a row must have all of them | `database.html?property=even,unimodular` |
| `family` | families; a row must have all of them | `database.html?family=root-lattice` |
| `q` | text search | `database.html?q=Lambda` |

## Commands

The `latticedb` command line owns validation, the build and deployment. The `justfile`
calls it.

| Recipe | Effect |
| --- | --- |
| `just build` | Validate every record and build the site into `_site/` |
| `just deploy` | Build, link `_site/` to `/var/www/static-sites/lattice-database`, and check that nginx serves it |
| `just tag` | Print the tag for the next new record |
| `just test` | Run the tests |
| `just seed` | Write the first records into an empty `lattices/` directory; needs SageMath at `SAGE_BIN` |

`uv run latticedb check` validates the records and builds nothing.

The build needs `pandoc` on `PATH`. The pages load MathJax and DataTables from a CDN.

`just seed` is a bootstrap. It assigns tags in the order of its own list, so it must not
run on a directory that has records.
