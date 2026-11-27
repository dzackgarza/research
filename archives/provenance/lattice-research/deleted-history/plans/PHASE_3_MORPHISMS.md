# Phase 3: Concrete Morphism Wrappers and the Cokernel Machine

Build the concrete morphism layer on top of `ModulesWithForms(R)`: thin
hom-space wrappers as genuine Sage homsets, thin morphism wrappers as Sage
`Morphism` instances (not matrices), kernel/image/cokernel returning proper
objects in the relevant meets of `ModulesWithForms(R)`, and validation at
construction. The cokernel method is still the single most critical piece:
it must produce the correct descended object and enable the discriminant
descent `L -> L* -> A_L` in Phase 4.

**Depends on:** Phase 2 (`ModulesWithForms` category mixins, forms,
codomains, and thin concrete carriers). Generic homset and morphism
interfaces are already specified in the category definitions from Phase 2;
Phase 3 supplies the concrete wrapper classes and the quotient algorithms.

**Supersedes:** PHASE_1 Steps 8 and 13.

**Style guide:** `plans/LATTICE_STYLE_GUIDE.md`.
Core style constraints for this phase: morphisms are not matrices, hom-space
containment owns isometry testing, the cokernel constructs the correct
mathematical object, explicit morphisms replace implicit identifications.


## Files

```
src/lattices/
    categories/
        modules_with_forms.py     # category-owned homset/morphism mixins
    morphisms/
        homspaces.py              # thin concrete hom-space wrappers
        bilinear.py               # thin concrete morphism wrappers
    validation/
        presentations.py          # (extend) MorphismFromImagesModel, MorphismFromMatrixModel
```


## Implementation Steps


### Step 3.1: Concrete Hom-Space Wrappers

**File:** `morphisms/homspaces.py`

**Existing code:** 107-line `BilinearModuleHomSpace(Homset)` with
`from_dict`, `from_matrix`, `from_images`.

This is a genuine Sage `Homset`, registered via category dispatch from
`ModulesWithForms(R)`. The important correction is that the generic
hom-space behavior already lives in
`ModulesWithForms(...).Homsets.ParentMethods`; this file only supplies the
concrete wrappers and constructors.

```python
class BilinearModuleHomSpace(Homset):
    """Hom(M, N) in ModulesWithForms(R).Bilinear().

    Elements are BilinearModuleMorphisms. Construction is via
    from_dict or from_matrix, never by coercing
    a raw matrix.
    """

    Element = BilinearModuleMorphism

    def from_dict(self, mapping: dict) -> BilinearModuleMorphism:
        """Construct morphism from {generator: image} dict.

        This is the PREFERRED construction method. The dict maps
        generators of self.domain() to elements of self.codomain().
        """
        ...

    def from_matrix(self, M: Matrix) -> BilinearModuleMorphism:
        """Construct morphism from matrix representation.

        Converts to dict internally: column j is the image of
        generator j expressed in codomain generators.
        """
        ...

    def from_images(self, images: list) -> BilinearModuleMorphism:
        """Construct from ordered list of images of domain generators."""
        ...

    def identity(self) -> BilinearModuleMorphism:
        """Identity morphism. Only valid when domain == codomain."""
        assert self.domain() == self.codomain()
        ...

    def natural_map(self) -> BilinearModuleMorphism:
        """Natural inclusion or projection when one exists."""
        ...

    def zero(self) -> BilinearModuleMorphism:
        """The zero morphism."""
        ...
```

**Hierarchy:**
```
BilinearModuleHomSpace(Homset)
+-- FreeBilinearModuleHomSpace
|   +-- RationalLatticeHomSpace     (Phase 4)
|   |   +-- LatticeHomSpace         (Phase 4)
+-- TorsionBilinearModuleHomSpace
|   +-- DiscriminantGroupHomSpace   (Phase 4)
```

Phase 3 implements the concrete bilinear hom-space wrappers. The later
phase-specific names remain thin refinements layered on the same category
machinery.

**Key decisions:**

- **`__contains__` owns isometry checking.** `f in Hom(L1, L2)` checks
  that f preserves the bilinear form. This is the SINGLE source of truth
  for form-preservation; no scattered matrix equations elsewhere.

- **Matrices are NOT in hom spaces.** `matrix(ZZ, [[0,1],[1,0]]) not in H`
  must hold. Only constructed `BilinearModuleMorphism` objects live in hom
  spaces. The `__call__` on the hom space is a thin dispatcher that routes
  matrices through `from_matrix`.

- **Module structure.** `Hom(M, N)` is an `R`-module: morphisms can be
  added and scaled. This comes from the `Homsets` extra super-category
  declared in `ModulesWithForms` during Phase 2.

- **Dispatch by meets.** The category examines domain and codomain
  predicates to select the most specific hom-space wrapper. This should be
  driven by category membership and meets, not by ad hoc parallel
  hierarchies.


### Step 3.2: Concrete Morphism Wrappers

**File:** `morphisms/bilinear.py`

**Existing code:** 123-line `BilinearModuleMorphism(Morphism)` with
`to_matrix`, `kernel`, `image`, `cokernel`, `is_isometry`.

A genuine Sage `Morphism` instance. NOT a matrix, NOT a container. As with
hom spaces, the generic behavior belongs to the category mixins; this file
provides the concrete wrapper and storage.

```python
class BilinearModuleMorphism(Morphism):
    """A morphism in ModulesWithForms(R).Bilinear().

    Internally wraps an FGP module morphism. The bilinear form
    is NOT automatically preserved -- containment in a hom space
    checks form preservation.
    """

    def _call_(self, element):
        """Evaluate the morphism on an element of the domain."""
        assert element in self.domain()
        ...

    def to_matrix(self) -> Matrix:
        """Matrix representation w.r.t. domain/codomain generators."""
        ...

    def to_dict(self) -> dict:
        """Generator-image dict."""
        ...
```

**Structural methods:**
- `is_injective()` -- delegates to underlying FGP morphism
- `is_surjective()` -- delegates to underlying FGP morphism
- `is_bijective()` -- `self.is_injective() and self.is_surjective()`
- `is_isomorphism()` -- `self.is_bijective()` (for modules; isometry is
  separate)
- `is_isometry()` -- checks form preservation:
  `beta_N(f(x), f(y)) == beta_M(x, y)` for all generator pairs. This is
  equivalent to `f in Hom(M, N)` when M, N have forms; the hom space
  `__contains__` delegates here.
- `is_primitive()` -- `self.cokernel().is_torsionfree()` (meaningful for
  lattice morphisms)
- `inverse()` -- when bijective, construct the inverse morphism

**Algebraic operations:**
- `__mul__(other)` -- composition: `(f * g)(x) = f(g(x))`. Domain/codomain
  compatibility asserted.
- `__add__(other)` -- sum of morphisms (module structure on Hom)
- `__neg__()` -- negation
- `__rmul__(scalar)` -- scalar multiplication
- `direct_sum(other)` -- block diagonal morphism on `M1 + M2 -> N1 + N2`
- `__eq__` -- equal iff same domain, codomain, and matrix representation

**Hierarchy:**
```
BilinearModuleMorphism(Morphism)
+-- FreeBilinearModuleMorphism
|   +-- RationalLatticeMorphism     (Phase 4)
|   |   +-- LatticeMorphism         (Phase 4)
+-- TorsionBilinearModuleMorphism
|   +-- DiscriminantGroupMorphism   (Phase 4)
```

Phase 3 implements `BilinearModuleMorphism` and
`FreeBilinearModuleMorphism`. Phase 4 adds the lattice-specific and
discriminant-specific methods (`order`, `is_involution`, `is_reflection`,
`reflection_decomposition`, `as_word_in_generators`, etc.).


### Step 3.3: Kernel and Image

**File:** `morphisms/bilinear.py` (methods on `BilinearModuleMorphism`)

Kernel and image return proper objects in the relevant
`ModulesWithForms(R).Bilinear()` meets, not raw FGP modules.

```python
def kernel(self) -> BilinearModule:
    """Kernel with restricted bilinear form from domain.

    ker(f) inherits its bilinear form from the domain:
    beta_{ker}(x, y) = beta_M(x, y) for x, y in ker(f).
    """
    fgp_kernel = self._underlying_morphism.kernel()
    restricted_gram = self._restrict_gram_to_submodule(
        fgp_kernel, self.domain()
    )
    return ModuleWithForm.from_module_and_form_data(
        fgp_kernel, restricted_gram,
        self.domain().bilinear_form().codomain()
    )

def image(self) -> BilinearModule:
    """Image with restricted bilinear form from codomain.

    im(f) inherits its bilinear form from the codomain:
    beta_{im}(f(x), f(y)) = beta_N(f(x), f(y)).
    """
    fgp_image = self._underlying_morphism.image()
    restricted_gram = self._restrict_gram_to_submodule(
        fgp_image, self.codomain()
    )
    return ModuleWithForm.from_module_and_form_data(
        fgp_image, restricted_gram,
        self.codomain().bilinear_form().codomain()
    )
```

Both delegate to the Phase 2 promotion machinery, which should land the
result in the richest correct meet.

**The zero object.** `kernel()` of an injective morphism returns the zero
object in the relevant bilinear meet:
`ModulesWithForms(R).Bilinear().zero()`.


### Step 3.4: The Cokernel Method

**File:** `morphisms/bilinear.py` (method on `BilinearModuleMorphism`)

This is the SINGLE most critical method in the entire design. It:
- Computes the FGP cokernel module
- Descends the bilinear form to the quotient
- Determines the correct codomain for the descended form
- Automatically promotes to the correct meet/category realization

```python
def cokernel(self) -> BilinearModule:
    """Cokernel with descended bilinear form.

    For f: M -> N, coker(f) = N / im(f) with the form descended
    from N. The descended form's codomain is determined by the
    input codomains.
    """
    # 1. Compute underlying module cokernel
    fgp_cokernel = self._compute_fgp_cokernel()

    # 2. Determine codomain for induced form
    induced_codomain = self._induced_form_codomain()

    # 3. Compute Gram matrix of descended form on cokernel generators
    cokernel_gram = self._descend_bilinear_form(
        fgp_cokernel, induced_codomain
    )

    # 4. Promote to correct type
    return ModuleWithForm.from_module_and_form_data(
        fgp_cokernel, cokernel_gram, induced_codomain
    )
```

**Form descent.** Given `f: M -> N` with `beta_N: N x N -> C_N`, the
descended form on `coker(f) = N / im(f)` is:

    beta_coker(x_bar, y_bar) := beta_N(x, y) mod (appropriate relation)

where x, y are lifts of x_bar, y_bar. This is well-defined when
`beta_N(im(f), N) = 0` in the appropriate codomain. For the discriminant
descent path `iota: L -> L*`, the form on `L*/L` takes values in `QQ/ZZ`
because `beta_{L*}(iota(v), w) in ZZ` for all `v in L`, `w in L*`.

**Codomain determination (`_induced_form_codomain`).** The descended form's
codomain depends on the input forms:

| Domain codomain | Codomain codomain | Cokernel codomain |
|----------------|-------------------|-------------------|
| ZZ (integral)  | QQ (rational)     | QQ/ZZ (torsion bilinear) |
| ZZ (integral)  | ZZ (integral)     | ZZ (integral, when cokernel is free) |
| QQ (rational)  | QQ (rational)     | QQ (rational, when cokernel is free) |

The critical case: `iota: L -> L*` has integral domain and rational
codomain, so the cokernel form lands in `QQ/ZZ`.

**Automatic promotion.** Phase 2's promotion machinery examines:

- form arity,
- free vs torsion,
- nondegeneracy,
- codomain stratum,
- any source-lattice metadata carried by the morphism.

The output should then land in the richest correct meet, for example:

- `ModulesWithForms(R).Bilinear().Torsion()`
- `ModulesWithForms(R).Bilinear().Free().Rational()`
- later in Phase 4, the named lattice and discriminant meets.


### Step 3.5: Cokernel Contract (Projection and Lift)

The cokernel comes equipped with structural morphisms that must be
accessible. These are not stored on the morphism but on the cokernel
object itself.

```python
# On the cokernel BilinearModule:
def projection(self) -> BilinearModuleMorphism:
    """The canonical surjection pi: N -> coker(f).

    pi.is_surjective() == True
    pi.kernel() == f.image()
    """
    ...

# On cokernel elements:
def lift(self) -> element:
    """Lift to a preimage in the codomain of the original morphism.

    For g_bar in coker(f), g_bar.lift() is some g in N such that
    pi(g) == g_bar.
    """
    ...
```

**Design:** The cokernel object stores a reference to the projection
morphism (constructed at cokernel creation time). The `lift` method on
cokernel elements delegates to the underlying FGP module's lift, then
wraps the result as an element of the codomain.

**Invariants on the cokernel:**
- `cokernel().invariants()` -- Smith normal form invariants of the
  underlying torsion module (when torsion)
- `cokernel().cardinality()` -- product of invariants (when finite)
- `cokernel().gens()` -- canonical generators of the quotient


### Step 3.6: End and Aut

**File:** `morphisms/homspaces.py` (convenience on `BilinearModule`)

```python
# On ModulesWithForms(...).ParentMethods (wired concretely in Phase 3):
def End(self) -> BilinearModuleHomSpace:
    """Endomorphism ring End(M) = Hom(M, M)."""
    return self.Hom(self)

def Aut(self) -> ...:
    """Automorphism group Aut(M) = {f in End(M) : f is bijective}."""
    ...
```

`End(M)` is a monoid under composition. `Aut(M)` is a group. Both are
subsets of `Hom(M, M)`.

`End(M).identity()` is the identity morphism. It must satisfy:
- `End(M).identity() in Aut(M)`
- `End(M).identity()(v) == v` for all `v in M`
- `End(M).identity().to_matrix() == identity_matrix(R, M.rank())`


### Step 3.7: Quotient Notation

**File:** `core/abstract.py` (extend `BilinearModule.__truediv__`)

Phase 2 stubbed `__truediv__`. Phase 3 fills it in:

```python
def __truediv__(self, other):
    """Quotient M / N via the cokernel of the inclusion N -> M.

    Requires N to be a sub-bilinear-module of M (i.e., there
    exists a canonical inclusion morphism N -> M).
    """
    inclusion = other.inclusion_into(self)
    return inclusion.cokernel()
```

This makes `L / M` work when `M` is a sub-bilinear-module of `L` with
a natural inclusion. The inclusion morphism is constructed from the
sub-module relationship.


### Step 3.8: Morphism Validation

**File:** `validation/presentations.py` (extend with morphism validators)

```python
class MorphismFromImagesModel(BaseModel):
    """Validates morphism constructed from generator images."""
    model_config = ConfigDict(arbitrary_types_allowed=True)

    domain: Parent
    codomain: Parent
    images: list

    @model_validator(mode="after")
    def validate_morphism(self):
        assert len(self.images) == len(list(self.domain.gens())), \
            "Number of images must equal number of domain generators"
        for img in self.images:
            assert img in self.codomain, \
                "Each image must be an element of the codomain"
        return self

class MorphismFromMatrixModel(BaseModel):
    """Validates morphism constructed from matrix."""
    model_config = ConfigDict(arbitrary_types_allowed=True)

    domain: Parent
    codomain: Parent
    matrix_data: Matrix

    @model_validator(mode="after")
    def validate_matrix(self):
        n = len(list(self.domain.gens()))
        m = len(list(self.codomain.gens()))
        assert self.matrix_data.nrows() == m and \
               self.matrix_data.ncols() == n, \
            "Matrix dimensions must match domain/codomain ranks"
        assert self.matrix_data.base_ring() == self.domain.base_ring(), \
            "Matrix entries must be in the base ring"
        return self
```


## Explicitly Out of Scope for Phase 3

- **Dual lattices, discriminant groups** -- Phase 4
- **`LatticeMorphism` extensions** (`order`, `is_involution`,
  `is_reflection`, `reflection_decomposition`, `as_word_in_generators`,
  `as_word_in_reflections`) -- Phase 5
- **Orthogonal groups** -- Phase 5
- **`DiscriminantGroupMorphism`, `DiscriminantFormMorphism`** -- Phase 4
- **Enumeration of hom spaces** -- deferred


## Functional Checkpoint

Run in a Sage session after completing Phase 3:

```python
import src.sage_patches
from src.lattices.categories.modules_with_forms import ModulesWithForms
from src.lattices.core.free import FreeBilinearModule

# ------------------------------------------------------------------
# Hom space construction
# ------------------------------------------------------------------

L.<e, f> = FreeBilinearModule(ZZ, matrix(ZZ, [[0,1],[1,0]]))
M.<g, h> = FreeBilinearModule(ZZ, matrix(ZZ, [[0,1],[1,0]]))
H = L.Hom(M)
assert H in ModulesWithForms(ZZ).Bilinear().Homsets()
assert H in Modules(ZZ)

# ------------------------------------------------------------------
# Morphism from dict (preferred construction)
# ------------------------------------------------------------------

swap = H.from_dict({e: h, f: g})
assert swap in H
assert swap(e) == h and swap(f) == g

# ------------------------------------------------------------------
# Morphism from matrix
# ------------------------------------------------------------------

swap2 = H.from_matrix(matrix(ZZ, [[0,1],[1,0]]))
assert swap2 == swap

# ------------------------------------------------------------------
# Matrix is NOT in the hom space
# ------------------------------------------------------------------

assert matrix(ZZ, [[0,1],[1,0]]) not in H

# ------------------------------------------------------------------
# Morphism is not its matrix
# ------------------------------------------------------------------

assert swap.to_matrix() == matrix(ZZ, [[0,1],[1,0]])
assert swap != matrix(ZZ, [[0,1],[1,0]])

# ------------------------------------------------------------------
# Structural queries
# ------------------------------------------------------------------

assert swap.is_injective() and swap.is_surjective()
assert swap.is_bijective() and swap.is_isomorphism()
assert swap.is_isometry()

# ------------------------------------------------------------------
# Kernel of an isomorphism is zero
# ------------------------------------------------------------------

assert swap.kernel() == ModulesWithForms(ZZ).Bilinear().zero()
assert swap.kernel().rank() == 0

# ------------------------------------------------------------------
# Nontrivial kernel and cokernel
# ------------------------------------------------------------------

diag = H.from_matrix(diagonal_matrix(ZZ, [2, 3]))
assert diag.is_injective()  # Injective over ZZ (det != 0)
assert not diag.is_surjective()

C = diag.cokernel()
assert C in ModulesWithForms(ZZ).Bilinear()
assert C.invariants() == [2, 3]
assert C.cardinality() == 6

# ------------------------------------------------------------------
# Cokernel contract: projection and lift
# ------------------------------------------------------------------

pi = C.projection()
assert pi.is_surjective()
assert pi.kernel() == diag.image()

c1, c2 = tuple(C.gens())
assert c1.lift() in M
assert c2.lift() in M
assert pi(c1.lift()) == c1
assert pi(c2.lift()) == c2

# ------------------------------------------------------------------
# Image as a sub-bilinear-module
# ------------------------------------------------------------------

im = diag.image()
assert im in ModulesWithForms(ZZ).Bilinear()
assert im.rank() == 2
# Image inherits bilinear form from codomain
assert im.gram_matrix() == diag.to_matrix().transpose() * M.gram_matrix() * diag.to_matrix()

# ------------------------------------------------------------------
# End and Aut
# ------------------------------------------------------------------

E = L.End()
assert E == L.Hom(L)
assert E.identity() in L.Aut()
assert E.identity()(e) == e and E.identity()(f) == f
assert E.identity().to_matrix() == identity_matrix(ZZ, 2)

# ------------------------------------------------------------------
# Composition
# ------------------------------------------------------------------

f1 = L.End().from_dict({e: f, f: e})
f2 = L.End().from_dict({e: -e, f: -f})
f3 = f1 * f2  # Composition: f3(x) = f1(f2(x))
assert f3(e) == -f and f3(f) == -e
assert f3.to_matrix() == f1.to_matrix() * f2.to_matrix()

# Composition is associative
f4 = L.End().from_dict({e: e + f, f: f})
assert (f1 * f2) * f4 == f1 * (f2 * f4)

# ------------------------------------------------------------------
# Morphism algebra: addition and scalar multiplication
# ------------------------------------------------------------------

id_L = L.End().identity()
neg_id = -id_L
assert neg_id(e) == -e
assert (id_L + neg_id)(e) == L.zero_element()
assert (2 * id_L)(e) == 2 * e

# ------------------------------------------------------------------
# Direct sum of morphisms
# ------------------------------------------------------------------

f_sum = f1.direct_sum(f2)
assert f_sum.domain().rank() == 4
assert f_sum.codomain().rank() == 4
assert f_sum.to_matrix() == block_diagonal_matrix(
    f1.to_matrix(), f2.to_matrix()
)

# ------------------------------------------------------------------
# Isometry checking via hom-space containment
# ------------------------------------------------------------------

# f1 swaps e <-> f in the hyperbolic plane, preserving the form
assert f1.is_isometry()
assert f1 in L.End()

# This morphism does NOT preserve the form
bad = L.End().from_matrix(matrix(ZZ, [[1, 1], [0, 1]]))
assert not bad.is_isometry()
# bad is still in End(L) as a module morphism, but not as an isometry

# ------------------------------------------------------------------
# Quotient notation
# ------------------------------------------------------------------

S = L.span([e])
# S is a rank-1 degenerate sub-bilinear-module
Q = L / S  # Quotient via cokernel of inclusion
assert Q in ModulesWithForms(ZZ).Bilinear()

# ------------------------------------------------------------------
# Module-level morphism specs from sage_spec/misc.sage
# ------------------------------------------------------------------

M1.<g1, g2> = FreeBilinearModule(ZZ, identity_matrix(ZZ, 2))
M2.<h1, h2> = FreeBilinearModule(ZZ, identity_matrix(ZZ, 2))
H12 = M1.Hom(M2)

f = H12.from_matrix(matrix(ZZ, 2, [0,1,1,0]))
assert f in H12
assert f(g1) == h2 and f(g2) == h1
assert f.to_matrix() == matrix(ZZ, 2, [0,1,1,0])
assert f.is_injective() and f.kernel() == ModulesWithForms(ZZ).Bilinear().zero()
assert f.is_surjective() and f.cokernel() == ModulesWithForms(ZZ).Bilinear().zero()
assert f.is_bijective() and f.is_isomorphism()

# Nontrivial cokernel with projection/lift
g = H12.from_images([2*h1, 3*h2])
assert g.to_matrix() == diagonal_matrix(ZZ, [2,3])
C = g.cokernel()
assert C in ModulesWithForms(ZZ).Bilinear()
c1_bar, c2_bar = tuple(C.gens())
pi = C.projection()
assert pi(h1) == c1_bar and pi(h2) == c2_bar
assert c1_bar.lift() in M2
assert pi.is_surjective()
assert pi.kernel() == M2.span([2*h1, 3*h2])
```


## Risks

| Risk | Mitigation |
|------|-----------|
| Sage `Morphism` composition may conflict with our `__mul__` | Test early; use `_call_` not `__call__` for element evaluation |
| FGP module cokernel may not carry enough metadata for form descent | Compute form descent explicitly from generator lifts, not from FGP internals |
| `__contains__` on HomSpace may be slow for large-rank modules | Isometry check reduces to `M^T G_N M == G_M`, which is O(n^3); acceptable |
| Cokernel promotion to named discriminant objects requires source lattice metadata | Phase 3 promotes to the generic torsion bilinear meet; Phase 4 adds the named discriminant path |
| Direct sum of morphisms requires matching summand structure | Assert domain/codomain compatibility at construction; block diagonal matrix is unambiguous |
