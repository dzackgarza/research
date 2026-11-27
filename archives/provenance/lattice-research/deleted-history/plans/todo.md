# Todo

## Two distinct issues to address:

### 1. Dual objects are homs — the missing connection

M* = Hom_R(M, R) is not merely a module — it IS a homset. The correct `extra_super_categories` for `DualObjects` should route through `Homsets`, not bypass it:

```python
class DualObjects(DualObjectsCategory):  
    def extra_super_categories(self):  
        # M* = Hom_R(M, R) is a homset, not just a module  
        return [self.base_category().Homsets()]
```

Then `Homsets.extra_super_categories` returning `[MyFGModules(R)]` handles the rest of the chain. The existing `ModulesWithBasis.DualObjects.extra_super_categories` returns `[Modules(R)]` directly, which is the shortcut the user is correctly identifying as wrong: `modules_with_basis.py:2776-2789`

With the correct routing, elements of M* automatically inherit both `MorphismMethods` (they are morphisms M → R) and `ElementMethods` from `MyFGModules(R)` (they are module elements) — because the dynamic element class is built from the full category chain, not just the module part.

### 2. Generalization of methods

Every method should be moved to the most general category on which it makes sense.

**Specific violations and tasks:**

*   **Move to `Modules.Torsion`**:
    *   `ParentMethods`: `p_part`, `is_p_elementary` (currently in `ModulesWithForms.Torsion`).
    *   `ElementMethods`: `order` (currently in `ModulesWithForms.Torsion`).
*   **Move to `Modules.Free`**:
    *   `ParentMethods`: `rank` (currently in `ModulesWithForms.Free`).
    *   `ElementMethods`: `divisibility`, `is_primitive` (currently in `ModulesWithForms.Free`).
    *   *Note*: `free_rank` in `ModulesWithForms.Free` is redundant as it is already in `Modules.Free`.
*   **Move to `ModuleHomsets`**:
    *   Generic methods from `ModulesWithFormsHomsets` (`domain`, `codomain`, `from_dict`, etc.).
*   **Move to `ModuleHomsets.Endset`**:
    *   `ParentMethods`: `identity`, `id`, `Aut` (currently in `ModulesWithFormsHomsets.Endset`).
*   **Move to `Modules.DualObjects`**:
    *   `ParentMethods`: `as_linear_dual` (currently in `ModulesWithFormsDualObjects`).
    *   `ElementMethods`: `as_linear_functional`, `evaluate` (currently in `ModulesWithFormsDualObjects`).
*   **Move to `ModulesWithForms` (general)**:
    *   `ParentMethods`: `determinant`, `discriminant`, `is_isometric_to`, `is_rationally_isometric_to`, `is_locally_isometric_to`, `orthogonal_group` (currently restricted to `NonDegenerate`). These should be moved to the base `ModulesWithForms` or partitioned correctly into `Bilinear`/`Quadratic`.

**Removal of Redundant Predicates:**
*   **REMOVE** `is_isometry()` and `is_form_preserving()` from `ModulesWithForms.Bilinear.MorphismMethods`.
*   **REPLACE** these with homset containment logic: a morphism is an isometry if and only if it is contained in the homset of the category of modules with forms (e.g., `phi in Hom(L, M, category=Modules(R).WithForm().Bilinear())`).

### 3. Centralization of types
Define the following centrally (e.g., in a `types.py`) by aliasing them to the respective `ParentMethods` and `ElementMethods` classes. These aliases provide types for Parent and Element instances within the category hierarchy.

**Category: `Modules`**
- `RModule` (object in `Modules(R)`): `Modules.ParentMethods`
- `RModuleElement` (element in an `RModule`): `Modules.ElementMethods`
- `SubModule` (object in `Modules.Subobjects`): `Modules.Subobjects.ParentMethods`
- `Ideal` (object in `Ideals`, a separate category declaring `Modules.Subobjects` as a supercategory): `Ideals.ParentMethods`
- `RModHomset`: `Modules.Homsets.ParentMethods`
- `RModHomsetElement`: `Modules.Homsets.ElementMethods`
- `RModEndset`: `Modules.Homsets.Endset.ParentMethods`
- `RModEndsetElement`: `Modules.Homsets.Endset.ElementMethods`
- `RModAutset`: `Modules.Homsets.Endset.Autset.ParentMethods`
- `RModAutsetElement`: `Modules.Homsets.Endset.Autset.ElementMethods`
- `DualModule`: `Modules.DualObjects.ParentMethods`
- `DualModuleElement`: `Modules.DualObjects.ElementMethods`

**Category: `ModulesWithForms`**
- `RModuleWithForm` (object in `ModulesWithForms(R)`): `ModulesWithForms.ParentMethods`
- `RModuleWithFormElement` (element in an `RModuleWithForm`): `ModulesWithForms.ElementMethods`
- `RModWithFormHomset`: `ModulesWithForms.Homsets.ParentMethods`
- `RModWithFormHomsetElement`: `ModulesWithForms.Homsets.ElementMethods`
- `RModWithFormEndset`: `ModulesWithForms.Homsets.Endset.ParentMethods`
- `RModWithFormEndsetElement`: `ModulesWithForms.Homsets.Endset.ElementMethods`
- `RModWithFormAutset`: `ModulesWithForms.Homsets.Endset.Autset.ParentMethods`
- `RModWithFormAutsetElement`: `ModulesWithForms.Homsets.Endset.Autset.ElementMethods`
- `DualModuleWithForm`: `ModulesWithForms.DualObjects.ParentMethods`
- `DualModuleWithFormElement`: `ModulesWithForms.DualObjects.ElementMethods`

**Generic/Support Types**
- `Ring` (object in our `ModuleBaseRings` category): `ModuleBaseRings.ParentMethods`
- `RingElement` (element of the base ring): `ModuleBaseRings.ElementMethods`
- `BilinearForm`: `BilinearForms.ParentMethods`
- `QuadraticForm`: `QuadraticForms.ParentMethods`
- `Cardinality` (N \cup {∞}): `Integer | InfinityElement`

### 4. Refactor Forms into `TwistedForms` Category
Currently, `ModulesWithForms` is doing too much and forms (`BilinearForm`, `QuadraticForm`) are handled somewhat manually. We need to introduce a rigorous category for the forms themselves:

1. **Define `TwistedForms` Category**:
   - Objects are elements of $\text{Hom}_R(T_R(M)[k], R)^\sigma$.
   - Here $T_R(M)$ is the tensor algebra of $M$ in $R$-Mod, $[k]$ denotes the $k$-th graded piece, and $\sigma \in \text{Aut}(R)$.
   - These represent forms where $f(r \cdot m) = \sigma(r) \cdot f(m)$ twisted by an automorphism.
   - This category should have explicit `.Bilinear()` and `.Quadratic()` subcategories.

2. **Refactor `ModulesWithForms`**:
   - `ModulesWithForms` should be redefined as a subcategory of `Modules(R)` equipped with extra structure.
   - The extra structure is specifically an object from the `TwistedForms` category.
