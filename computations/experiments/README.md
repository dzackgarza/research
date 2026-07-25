# Experiments

Runnable exploratory code that is not yet reusable enough for `src/`.

Do not force experiments into object-taxonomy folders such as curves, surfaces, or lattices.
Use a direct file, a dated scratch name, or a named computation thread that matches the actual calculation.

Promote stable code to `src/` (the installable `dzack_research` package) only after preserving the original algorithm and adding verification appropriate to the mathematical claim.
The migration criterion is in `AGENTS.md`: code lives in a spike until a shipped, tested notebook proves a researcher can use it.
