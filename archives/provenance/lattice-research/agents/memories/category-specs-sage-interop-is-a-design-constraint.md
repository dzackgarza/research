# Category Specs: Sage Interop Is a Design Constraint

## Trigger

When planning, implementing, auditing, or classifying category_specs work involving
Sage inventory, Sage wrappers, constructor-obligation examples, or refined Sage
objects.

## Rule

The category-spec project defines an ideal mathematical interface inside Sage's category/object universe. Current Sage coverage is not the adequacy standard: if current Sage already satisfied the desired interface, this project would have no reason to exist.

Sage interop is still a design constraint. The project extends Sage without editing upstream source yet, and refined Sage objects should remain usable by existing Sage code when mathematically appropriate. Use Sage as implementation evidence and a feasibility witness. Existing Sage methods, constructors, docs, and algorithms help preserve functionality and prevent unimplementable wishlists. They do not cap the spec and they are not negative evidence against mathematically required methods.

Refined Sage objects are partial witnesses, not proof of spec satisfaction. The project
declares stronger category contracts than Sage currently knows, so most refined Sage
objects are expected to miss project methods during the spec phase. That mismatch is the
object under study: it tells later implementation work what Sage wrappers, constructors,
or replacement implementations must supply.

Do not treat Sage interop as a refinement-admission test. A constructor or refinement
path may declare a Sage object into a project category even when that object does not
yet satisfy the full project contract. Category-obligation examples expose the gap;
refinement does not validate it away.

## Action

If a category assertion fails because a current Sage/refined object lacks a spec
method, record an implementation, wrapper, constructor, decision, or source-mining
gap. Do not delete, weaken, or move the spec obligation unless a source-grounded
replacement weakest category preserves the mathematical statement.

## Verification

Task, phase, or plan acceptance for spec work should locally state how the
ideal-interface obligation is preserved when category-obligation examples fail.
