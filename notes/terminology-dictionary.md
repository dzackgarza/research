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
| `CS10` | Conway & Sloane, *Sphere Packings, Lattices and Groups*, 3rd ed. — Ch. 15 | genus symbol, p-adic symbols, Jordan decomposition of forms |
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

## Legitimate terms — do NOT flag

Correct where used: **Smith normal form** (of a *matrix*), **discriminant form / discriminant
group** (`Nik80`), **genus / genus symbol** (`CS10`), **signature**, **Gram matrix**,
**isometry / reflection**, **Pontryagin dual** (the group), **Brown invariant**, **kernel**
`ker(f)` of a morphism, `End(L)`, `O(L)`, and real Sage class names
(`TorsionQuadraticModule`, `IntegralLattice`, `FGP_Module`) inside code calls. "Nodes" of a
plane sextic and "strata of a flag" are genuine geometry — unrelated to the drift above.
