# Research Mathematical Argument Standards

Trigger: writing or reviewing mathematical notes, proof sketches, computational proof artifacts, source-backed theory prose, or spec cards that make mathematical claims.

Rule: research-level arguments in this repo must expose the dependency chain. Do not start from a named expected object and argue by authority. Construct the relevant objects, name the maps between them, derive the invariants, state standard theorems with hypotheses, and only then state the conclusion.

Standardness calibration is mandatory. Before accepting a claim as "standard", classify it:

- Immediate fact: follows directly from a presentation, definition, rank, signature, Gram matrix, or standard decomposition. State it directly; do not cite papers for authority.
- Trivial first-principles derivation: follows in a few lines from definitions and basic linear algebra or algebraic geometry. Write the derivation in place; do not route it to source-mining or present it as major progress.
- Textbook standard theorem: reusable foundational or graduate-level material with explicit hypotheses, e.g. Hartshorne-level algebraic geometry. State the theorem and hypotheses; cite a canonical source only if needed.
- Niche research theorem: specialized result from a paper. Cite the exact theorem/proposition and state the hypotheses.
- Project-specific claim: depends on this repo's construction, vocabulary, or computation. Construct or compute it; do not call it standard.

Do not let difficulty drift upward. The correction transcript established that agents can repeatedly fail to see how immediate some facts are. For example, once a Type IV period lattice $T$ is presented with rank $r$ and signature $(2,r-2)$, $\dim D_T=r-2$ is immediate. Once a lattice is given by a standard decomposition or Gram presentation, rank and signature are immediate. The nontrivial work is deriving the lattice, maps, moduli comparison, arithmetic group, or construction that makes those immediate facts relevant.

Some facts are not "standard" because they require a standard theorem; they are ordinary because the derivation is tiny. For a Type IV domain, one can read the definition, complexify the lattice, projectivize, impose the quadratic equation, and restrict to the open semialgebraic component. Each step has the elementary dimension change expected from basic linear algebra and algebraic geometry. This is not a research claim.

Do not place a trivial derivation beside a niche claim as if they had comparable proof weight. A claim like "the Coble moduli problem is compared to the period quotient for $T_{\mathrm{Co}}$" is not the same kind of claim as "the resulting Type IV domain has dimension $r-2$". The former can hide the moduli functor, construction, K3 relation, lattice derivation, arithmetic group, period map, and birational comparison. The latter is a direct calculation after the input is known.

Progress accounting must respect this asymmetry. Recording the trivial dimension calculation does not complete a meaningful fraction of a task whose real content is identifying the object, construction, theorem, or comparison map that makes the calculation relevant.

Apply these checks:

- Separate definitions, constructions, immediate consequences, trivial derivations, standard theorem invocations, niche cited claims, computed results, and unproved claims.
- Treat immediate facts as immediate. Do not spend citations or rhetoric on rank, signature, dimension, or other quantities that follow directly from a presentation.
- Replace vague language such as "associated to", "governed by", "correct for", or "right target" with maps, embeddings, pullbacks, quotients, period maps, or birational comparisons.
- Do not smuggle conclusions into names. If a lattice, moduli space, group, or period domain has not been constructed from the setup, it is not yet available as an input.
- Use mature frameworks at the right abstraction level instead of rederiving them badly; state what the framework parameterizes and what input data it requires.
- Computational proofs should read as mathematics: public code should expose mathematical nouns and morphisms; raw matrices, vectors, lists, and dicts are internal realizations only.
- Audit public Sage-facing types aggressively. Returning raw nonmathematical Sage base
  types such as `Parent` or `Element` is usually a sign that the code has not stated
  the mathematical category of the result. Reserve such broad types for true base
  bridges only.
- If a broad Sage-backed type is genuinely necessary, require an explicit alias such as
  `SageCategoryObject` or `SageElement` rather than exposing naked infrastructure names
  in the mathematical API or proof surface.
- Generality matters. If the code or prose only works as a bespoke one-off for the current claim, it is not expressing the intended mathematical vocabulary.

Verification: before accepting a mathematical artifact, a future agent should be able to point to the constructed objects, the connecting maps, the immediate facts, the trivial derivations, the standard theorem invocations with hypotheses, the niche cited claims with hypotheses, and the exact remaining gaps. If any of those are missing, route the work to source-mining, vocabulary/spec design, or proof repair instead of polishing prose.
