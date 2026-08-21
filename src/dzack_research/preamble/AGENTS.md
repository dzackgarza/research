## Conclusion

Yes, the preamble should own every mathematical category and every inclusion.

Sage’s native category graph provides no essential mathematical value here. Its useful behavior comes from Sage’s runtime machinery, not its category definitions.

## Mathematical assertions

Every executable assertion must state a mathematical proposition.

Mathematics fixes its truth. Code can satisfy or violate the proposition. Code does not define its truth.

Assert cardinalities, universal properties, algebraic identities, and functor laws.

Do not assert method placement, class layout, source text, diagnostic totals, or past defects.

Inspect source ownership to verify architecture. Use mathematical specimens to verify behavior.

State the mathematical proposition before the code path that must realize it.

## Keep these Sage components

- `Parent` and `Element`
- `Homset` and `Morphism`
- The coercion model
- Dynamic method installation
- Category refinement by properties and axioms
- Join and construction-class generation

These parts are not trivial to reproduce. Sage creates parent, element, and morphism classes from the category graph. It also changes classes during refinement. [Sage’s category documentation](https://doc.sagemath.org/html/en/reference/categories/sage/categories/category.html) describes this mechanism.

This behavior lets one Sage object gain owned methods without a wrapper. The archived code instead uses adapters such as `ConsolidatedLattice` and a separate `LatticeHomset`. See [category.py](/home/dzack/research/archives/lattice-research/src/lattices/category/category.py).

The current [owned_category.py](/home/dzack/research/src/dzack_research/preamble/owned_category.py#L1) shows the real complexity. It handles dynamic classes, C3 method order, metaclasses, pickling, and Sage parent initialization.

## Remove these Sage links

Links such as these should not define the mathematical hierarchy:

```python
return [
    SageModules(self.base_ring()),
    OwnedAdditiveGroups(),
    AdditiveGroups().AdditiveCommutative(),
]
```

This appears in [modules.sage](/home/dzack/research/src/dzack_research/preamble/categories/modules/pure/modules.sage#L60).

Such links mainly provide generic methods:

- `Modules(R)` provides `module_morphism`, `quotient`, `linear_combination`, and `tensor_square`.
- `Rings()` provides ideals, quotients, and localization.
- `Monoids()` provides `prod`, powers, and inverse operations.
- `Sets()` provides sample elements and product constructions.

These methods need not make Sage categories mathematical supercategories. The owned category remains the mathematical owner.

A Sage implementation can supply an algorithm. Do not keep a same-name forwarding method as a second owner.

The Sage graph also contains known mathematical defects. These include missing inclusions and weak join semantics. See [Sage-Category-Framework-Inventory.md](/home/dzack/research/docs/sage/Sage-Category-Framework-Inventory.md#L114).

## One current exception

The present implementation needs `SageSets()` below each owned root. Sage’s `Parent._init_category_` otherwise creates a duplicate dynamic base. [owned_category.py](/home/dzack/research/src/dzack_research/preamble/owned_category.py#L33) records this constraint.

This is a runtime compatibility condition. It is not mathematical ownership.

Removing even this link requires replacing part of Sage parent initialization. That work is possible, but not trivial.

## Recommended boundary

- The preamble owns the complete mathematical category graph.
- Sage supplies concrete computational objects and algorithms.
- Sage categories serve only as implementation providers or compatibility tags.
- Native Sage categories do not occur as mathematical supercategories.
- The Sage category engine remains until the preamble replaces dynamic refinement.
- The coercion model remains independent of Sage’s mathematical category graph. [Sage coercion documentation](https://doc.sagemath.org/html/en/reference/coercion/sage/structure/coerce.html)

## Current architectural closeout

- Put set-theoretic answers at the owned `Sets()` layer.
- Construct each enriched object as the structure it claims to be.
- Represent forgetting with a functor. Do not use `forget_*` methods.
- Put element and morphism operations on their category surfaces.
- Send data through construction. Use refinement only for properties and axioms.
- Replace instance-dictionary probes with category membership, accessors, or `cached_method`.
- Remove same-name forwarding and duplicate mathematical owners.

Therefore:

- Owning all mathematical categories: **yes**.
- Removing native Sage category inheritance: **yes**.
- Removing Sage’s category runtime: **no**, unless wrapper objects or a major runtime replacement are acceptable.

<oai-mem-citation>
<citation_entries>
MEMORY.md:48-61|note=[Used prior category ownership and Sage runtime boundary findings]
</citation_entries>
<rollout_ids>
019ffc95-e905-7da1-8b3f-ada166759c79
</rollout_ids>
</oai-mem-citation>
