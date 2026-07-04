# Terminology Dictionary — drift → real mathematical term

Agents working the lattice code drift into engineering/implementation jargon and into
plausible-but-invented terms in place of established mathematical terminology. This
dictionary is the canonical replacement lexicon: each **drifted term** maps to the **real
term**, a **grounded good/bad phrasing**, and the **source** where the real term is defined.

**This dictionary does not track occurrence locations.** `file:line` lists go stale the
moment a fix lands; they live in the terminology-cleanup **plan** (agent-memory), which is
the worklist for actually applying these replacements. Occurrences only *informed* the
grounded examples below — they are not part of this durable artifact.

## Rule for adding an entry

**No entry without a citable replacement lexicon.** Every replacement *mathematical* term
must cite a source where it is actually defined — do not manufacture a plausible-sounding
term (e.g. "genus normal form" was confabulated and is *not* real). Cite a **bibkey** from
the running Zotero instance; its attached PDF and, where present, its markdown extraction
(`~/Zotero/storage/<attachment-key>/*.md`) can be read to corroborate the term verbatim
before committing the entry. If you cannot cite a source, the entry is not admissible —
find the source or leave the term flagged, do not coin one. (Pure jargon→plain-English
replacements, where the target is not a specialized term, are marked "plain".)

## Sources (Zotero bibkeys)

| bibkey | reference | used for |
|--------|-----------|----------|
| `DF04` | Dummit & Foote, *Abstract Algebra*, 3rd ed. | invariant factors, elementary divisors, Smith normal form, modules over a PID, endomorphism ring, kernel |
| `Nik80` | Nikulin, *Integral symmetric bilinear forms and some of their applications* (1979/80) | discriminant group, discriminant (bilinear/quadratic) form, signature invariants, genus of even lattices |
| `CS10` | Conway & Sloane, *Sphere Packings, Lattices and Groups*, 3rd ed. | root-lattice invariants, kissing numbers, theta series, shell cardinalities; genus symbol, p-adic symbols, Jordan decomposition of forms |
| `Cas08` | Cassels, *Rational Quadratic Forms* — Ch. 8 | Jordan splitting of a form over ℤ_p |
| `MM09` | Miranda & Morrison, *Embeddings of integral quadratic forms* | finite quadratic forms; the canonical form Sage's `normal_form()` computes |
| `Mac98` | Mac Lane, *Categories for the Working Mathematician* | category, object/morphism, axioms, underlying object, endomorphism monoid |
| `Rie16` | Riehl, *Category Theory in Context* | same categorical vocabulary |

---

## Tier A — substantive: invented terms, wrong field, or a tool's name used for the object

| Drifted term | Replace with | Source · locus |
|---|---|---|
| **`Cryptographic` axiom / `CryptographicLattices`** ("cryptographic refinement of a positive-definite lattice") | *Relocate, don't delete.* "Cryptographic" is an application, not a lattice property — move the M6 crypto methods (`vectors_of_square`, `roots`, LLL/CVP/SVP) to the mathematically valid subcategory where they are all defined, **likely definite + unimodular** (to validate). Separately, Sage has many constructors that *generate* cryptographic-style lattices (q-ary, LWE/NTRU, random unimodular, etc.) — expose those generators widely as constructors rather than gating an axiom on them. | `Nik80` §1; `CS10` Ch. 1 |
| **"Smith invariants" / "Smith invariant count / coordinates"** | **invariant factors** (or **elementary divisors**); "invariant-factor coordinates" | `DF04` Ch. 12 (§12.1) |
| **"Smith form of a module" / "Smith quotient" / "Smith-based `A/H`" / "Smith presentation / generators / coordinates"** | the **invariant factor decomposition** `M ≅ R/(d₁)⊕…⊕R/(dᵣ)⊕Rᶠ` and its generators/coordinates. *Smith normal form is the algorithm on a matrix that produces this — legitimate only when it names the operation on an actual matrix (`matrix.smith_form()`), never the module or its decomposition.* | `DF04` Ch. 12 |
| **"FGP quotient / module / surface / morphism"** (leaks Sage's `FGP_Module` class) | a **finitely generated module over a PID** (here a finite abelian group) and its invariant-factor decomposition | `DF04` Ch. 12 |
| **`normal_form()` / bare "normal form"** of a discriminant form | *Not well-defined as stated — name the object.* The literature objects are the **Jordan decomposition (Jordan splitting)** and the **genus symbol** (with per-prime **p-adic symbols**), the complete isometry invariant. Sage's `normal_form()` returns a canonical Gram representative following Miranda–Morrison; describe it as such, do not coin a name. Comparing them decides **isometry of finite quadratic forms**. | Jordan splitting: `Cas08` Ch. 8, `CS10` Ch. 15 · genus symbol: `CS10` Ch. 15, `Nik80` §1 · canonical rep: `MM09` |
| **"fractional sublattice"** (a lattice from non-integral / rational generators) | *Non-mathematical as stated.* `L` is a ℤ-module with no ℚ-action, so `(1/2)e ∉ L` and rational generators span **no** ℤ-submodule of `L`. The object lives in the rational quadratic space **`L_ℚ := L ⊗_ℤ ℚ`**: name it a **ℚ-subspace of `L_ℚ`**, or (for overlattices / duals) a **ℤ-lattice in `L_ℚ`** commensurable with `L` — e.g. the dual `L* = {x ∈ L_ℚ : b(x, L) ⊆ ℤ}`. Always state the ambient `L_ℚ`; never call it a "sublattice of `L`". | `Nik80` §1 (`L* ⊂ L⊗ℚ`, overlattices); `DF04` Ch. 10–12 (extension of scalars `L⊗ℚ`) |

---

## Tier B — engineering jargon → mathematical description

| Drifted term | Replace with | Source · locus |
|---|---|---|
| **"carrier" / "carrier module"** | the **underlying set / underlying module** of the object (image of the forgetful functor) | `Mac98` §I.1; `Rie16` §1.1 |
| **"domain algebra" / "the typed language of the spike"** | the **objects and operations of the lattice category** (its signature) | `Mac98` §I.1–I.2 |
| **"engine" / "delegation engine" / "oracle" / "engine-grounded"** | "**computed by Sage** (`IntegralLattice` / `TorsionQuadraticModule`)"; "**decided for** definite lattices" — name the operation, not a personified backend | plain |
| **"substrate"** (e.g. "owned + delegation substrate") | the **operations / methods** the object provides | plain |
| **"stratum / strata" / "stratum router"** | **subcategory** / the concrete class for an axiom | `Mac98` §I.3 |
| **"contract" / "protocol" / "protocol mirror"** (methods an object must provide; a "parallel mirror") | the **categorical structure / axioms**; the **operations the object supports** | `Mac98` §I.1; `Rie16` §1.1 |
| **"surface"** (meaning an API / set of methods) | the **class / its methods**, or the **underlying group** | plain |
| **"node"** (for a subcategory / object) | the **object** / the **subcategory** | `Mac98` §I.2 |
| **"facade" / "meet-based facade" / "join class"** | the **meet (intersection) of axiom subcategories** | `Mac98` §I.3 |
| **"kernel"** (used for an implementation core, e.g. "PD kernel") | the **implementation / core routine**. *Do not use "kernel" for this — it collides with the genuine kernel `ker(f)` of a morphism.* | contrast `DF04` Ch. 10 (kernel of a hom) |
| **"form-free" (layer/duplicate)** | the **underlying finite abelian group** of a discriminant form (the group without its bilinear/quadratic form) | `Nik80` §1.3 (`A_L = L*/L`) |
| **"sourced" (discriminant form/stratum)** | the **discriminant form of a lattice** `L`, i.e. `A_L = L*/L` built from `L` | `Nik80` §1.3 |
| **"FQF class"** | a **finite quadratic form** (discriminant quadratic form) | `Nik80` §1.3–1.7; `MM09` |
| **"composition monoid"** (for `End(L)`) | the **endomorphism monoid** `(End(L), ∘)` | `DF04` Ch. 10; `Mac98` §I.1 |
| **"typed Pontryagin identification"** | the **Pontryagin dual** `A ≅ Hom(A, ℚ/ℤ)`; the discriminant pairing `A_L → ℚ/ℤ` | `Nik80` §1.3 |
| **"value object" / "form-value object"** | the **value module** `K/R` in which the form takes values (the code's `value_module()` is fine) | `Nik80` §1.3 |
| **"brute-force body"** | **exhaustive enumeration** of the (automorphism) group | plain |
| **"alias residue / purge", "dispatch/alias"** | choosing **one canonical name per operation** (naming cleanup, not a math object) | plain |
| **"seam" / "construction-provenance seam"** | name the **mathematical distinction** being abstracted | plain |
| **"wrapper"** | a **promoted/renamed method** exposing a Sage operation | plain |
| **"adapter"** | (SWE pattern) — name the **operation** it exposes | plain |
| **"spike"** (as a noun for this code) | the **exploratory implementation** | plain |

---

## Tier C — typing & idiom discipline (raw numbers are constructor inputs, never objects)

Raw numerical data — coordinate vectors and matrices — are **constructor inputs only**.
They are not lattice elements or morphisms and must not propagate, cross object
boundaries, or be compared as if typed. Letting raw numbers stand in for typed objects is
what lets untyped data poison the DSL; the fix is to force everything through the
element/morphism language so the code must reconcile with the mathematical definition.
Idiom: inject named generators **once** — `U.<e, f> = …` — then work with `e + 2*f`
(elements) and hom objects (morphisms), never `[1, 2]` or bare matrices.

| Loose usage | Why it's wrong | Idiomatic replacement | Source |
|---|---|---|---|
| a lattice "contains vectors" / "`[1,2]` is an element of `L`" / lists of numbers as elements | A lattice element is a typed object of the ℤ-module `L`, not a coordinate tuple. `[1,2]` is coordinates relative to a chosen basis; the *same* tuple names *different* elements in *different* lattices. Footgun: with `L = U`, `Lp = U(2)`, "`[1,2] ∈ L` **and** `∈ Lp`" is a type error — equal coordinates, distinct objects and forms. | Construct once (`L.<e,f> = …`, or `L(coords)` at a boundary); then work symbolically: `e + 2*f`. A bare coordinate vector must never stand for, escape, or be compared as an element. (Cf. `x + y ∈ k[x,y]/(x²,y²)`, never `[1,1]`.) | `DF04` Ch. 12 (free-module element vs coordinates rel. a basis) |
| a raw **matrix** used or compared **as** a morphism outside a constructor | A morphism is a typed arrow (a hom object) with a domain and codomain, not its matrix. A matrix is a representation relative to chosen bases; using it directly bypasses domain/codomain typing and the morphism machinery. | Construct via the hom constructor (`Hom(L, M)(…)` / the lattice-morphism constructor); then compose and apply as morphisms. A raw matrix outside a constructor is a red flag. | `Mac98` §I.1 (morphisms as arrows); `DF04` Ch. 11 (matrix of a map rel. bases) |
| **manually raising `ValueError` / `NotImplementedError` / `TypeError` / `ArithmeticError`** (or the branch `if not X: raise AssertionError(...)`) to reject bad input, an unmet hypothesis, or a wrong-type argument | Mathematics has no "NotImplemented", "TypeError", or "ValueError". A method is *defined* exactly where its mathematical hypotheses hold; a typed exception is runtime-error vocabulary that lets an undefined call start running and then branch out of it. `NotImplementedError` reframes an unmet hypothesis as a missing feature; `TypeError` admits the code could run on an object the operation is not defined for. | **`assert` the hypothesis (or category membership) early**, ADDD-shaped, naming what was violated — so every line below is provably defined wherever reached: `assert q(v) != 0, ...`; `assert denom != 0, ...`; `assert L.is_definite(), "algorithm defined only for definite L"`; and for typing, assert the object lies in the category that *defines* the operation instead of type-checking and raising. No manual typed raise; no `if not X: raise`. | project policy — `global/advice/research-code-style.md` "Assertions Over Exceptions" (ratified, commit `8d75349`); **not** a math bibkey |

**Rule:** raw integer vectors and matrices appear **only** as arguments inside
constructors. Everywhere else the code speaks elements (`e + 2*f`) and morphisms — never
raw coordinate vectors or bare matrices. And code **asserts** its mathematical hypotheses
and category membership; it never manually raises `ValueError`/`NotImplementedError`/
`TypeError`/`ArithmeticError` to police them.

---

## Tier D — test assertion drift: ad-hoc construction → source concept

Tests should state the mathematical concept they witness. A low-level computation is
admissible only as the implementation of the assertion, not as the assertion's vocabulary.
Each row below is a self-contained bad→good replacement pattern, not an occurrence list.

| Drifted assertion / phrasing | Idiomatic mathematical replacement | Source · locus |
|---|---|---|
| Bad: `assert abs(det(L) / det(Lprime)) == 4` as the claimed content of an overlattice test. | Good: "The overlattice `L ⊂ L'` has index `[L':L] = 2` (or `[L':L] = \|H\|` for the isotropic subgroup `H ⊂ A_L`), and `q_{L'} ≅ H^⊥/H`." The determinant quotient is only the numerical shadow of the index formula. | `Nik80` §1.4 |
| Bad: "the p-local determinant factorization is pinned" by `ratio.is_square()`, `prime_divisors() == [p]`, or unchanged off-prime valuations. | Good: "`M = L.maximal_overlattice(p)` is the p-local saturation / p-maximal overlattice; the extension index is p-primary and the off-p primary discriminant data is unchanged." | `Nik80` §1.4–1.9; `CS10` Ch. 15 |
| Bad: replacing a rejected echelon-basis assertion by `assert saturation(L).gram_matrix() == G` or `assert det(saturation(L)) == d`. | Good: "`S.saturation(in_ambient=L)` is the primitive closure of `S` in `L`; assert `S.saturation(in_ambient=L) == S.primitive_closure(L)` and assert `S.index_in_saturation()` when the index is the mathematical invariant." | `DF04` Ch. 12; `Nik80` §1 |
| Bad: "intersection row" followed only by `assert (L.intersection(M)).gram_matrix() == G`. | Good: "`L ∩ M` is the meet/intersection sublattice: it is a sublattice of both `L` and `M`, contains exactly the common elements in the ambient rational space, and satisfies `L ∩ M = M ∩ L`." Gram data is a presentation witness. | `DF04` Ch. 10–12 |
| Bad: `assert coordinates(x) == (1, 3)`, identity invariant-factor generator matrices, or duplicated coordinate rows as the content of a quotient test. | Good: "The quotient is `A/B ≅ Z/4 ⊕ Z/12`; its generators have the stated orders, the projection/lift identities hold, and the kernel/image/cokernel exact-sequence data is correct." Coordinates are basis-dependent presentation data. | `DF04` Ch. 12 |
| Bad: `assert sorted(H.cardinality() for H in A.all_submodules()) == [1] + [2]*7 + [4]*7 + [8]` with no named object. | Good: "For `A ≅ (F_2)^3`, the subgroup lattice is the subspace lattice: one 0-plane, seven lines, seven planes, and one whole 3-space." | `DF04` Ch. 11–12 |
| Bad: direct-sum embeddings checked only by rank addition and pairwise equations `b(i(x), j(y)) = 0`. | Good: "The summand maps are orthogonal primitive isometric embeddings whose images span the orthogonal direct sum." Assert isometry of each embedding, orthogonality of images, primitivity, and spanning. | `Nik80` §1; `Mac98` §I.1 |
| Bad: `assert update_reduced_basis(v).determinant() == L.determinant()` as the claimed content of a basis-update/reduction test. | Good: "The basis update presents the same lattice / same isometry class and satisfies the intended reduced-basis property." Determinant equality alone is too weak. | `DF04` Ch. 12; `CS10` Ch. 1 |
| Bad: `[len(L.vectors_of_square(k)) for k in K] == [...]` or `[len(shell) for shell in L.short_vectors(B)] == [...]` with no named invariant. | Good: "These are shell cardinalities / representation numbers `r_L(m)`, equivalently initial coefficients of the theta series `θ_L(q) = Σ_m r_L(m)q^m`." State which shells are being computed; the list of lengths is only presentation data. | `CS10` Ch. 4, Ch. 7 |
| Bad: `assert len(L.roots()) == 240` with no named invariant. | Good: "The root lattice has kissing number / number of roots `240`." Counts are legitimate when they are the citable invariant (e.g. Conway-Sloane root-lattice tables), not when they stand in for hidden structure. | `CS10` Ch. 4 |

---

## Legitimate terms — do NOT flag

Correct where used: **Smith normal form** (of a *matrix*), **discriminant form / discriminant
group** (`Nik80`), **genus / genus symbol** (`CS10`), **signature**, **Gram matrix**,
**isometry / reflection**, **Pontryagin dual** (the group), **Brown invariant**, **kernel**
`ker(f)` of a morphism, `End(L)`, `O(L)`, and real Sage class names
(`TorsionQuadraticModule`, `IntegralLattice`, `FGP_Module`) inside code calls. "Nodes" of a
plane sextic and "strata of a flag" are genuine geometry — unrelated to the drift above.
