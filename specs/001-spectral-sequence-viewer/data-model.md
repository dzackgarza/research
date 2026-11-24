# Author input and viewer state

## Public schema

| Record | Fields and rules |
| --- | --- |
| Sequence | Required `convention` (cohomological or homological), `firstPage`, `extent`, and nonempty ordered `pages`. Optional `pageCount` equals the array length. Page indices increase by one from firstPage. Optional `degenerationPage` may exceed the last supplied index. |
| Rectangle | Inclusive signed integer `pMin,pMax,qMin,qMax`, each minimum at most its maximum. The extent bounds term records. The display viewport defaults to the projected extent. |
| Page | Required `index`, `terms`, and `maps`; optional TeX `formula`. Within each list coordinates are unique. |
| Term | `p,q,status` with status zero, nonzero, or unknown, and optional TeX `label`. Sequence-level `stableTerms` records contain `p,q,fromPage`, unique per coordinate. This makes the declared first stable page available on all later pages. |
| Map | `p,q` locate the source. Required `status` is zero, nonzero, or undetermined. Optional TeX `formula`. The convention and page determine the target. |
| Settings | Optional `settings` contains `initialPage` (default first supplied), `viewport`, `title`, `pLabel`, `qLabel`, and `zeroStyle` (zero, dot, blank; default zero). Sequence-level `unlisted` is unknown by default, or zero. |

Use nonnegative integer page indices and signed integer record coordinates. Resolve an unlisted cell inside the extent with the author's unlisted policy. Outside the extent an unlisted cell within support is unknown. Outside declared support it is zero. Require map sources in the extent; allow a computed target outside it.

For page r use displacement (r,1−r) in cohomology and (−r,r−1) in homology. Add the displacement for the outgoing target and subtract it for the incoming source. A known zero endpoint or global degeneration forces the map to zero. Local permanence from page s likewise forces incident differentials to vanish from s onward. Reject a nonzero assertion that conflicts with forced vanishing. Otherwise use the stated map status, defaulting to undetermined. Validate bounds, counts, ordering and duplicate keys before accepting the sequence.

Navigation changes the selected page and preserves the inspected coordinate and filter. Changing the filter or zero glyph changes presentation only. Local stability text gives its first page. The selector identifies the supplied degeneration page with infinity and keeps every later supplied page selectable.

## Signed support, projection, and assignments

Use `support: "unrestricted"` for signed native bidegrees or `"first-quadrant"` (default). Set `settings.projection` to `"total-filtration"` for horizontal total degree and vertical filtration, or `"native"` (default). A support restriction gives mathematical vanishing. The data extent governs missing records, and the viewport crops the projected diagram. Key terms, stability declarations, and differential sources by native bidegree under every projection. A component can supply an ordered `assignments` array of distinct generator and image pairs. The current singular `generator` and `image` fields describe only one assignment.

### Classes and relations

`terms[].classes` lists individual classes in a nonzero term. Each has a page-local
`id` and a TeX `label`. Set `permanent: true` on an individual permanent cycle.
A class on a later page can name its `previous` representative in the same
bidegree on the preceding page. This also describes a quotient class.
A representative linked to a permanent class inherits permanence. Reusing
a page-local ID alone establishes no relation between the classes.

A generator assignment can identify its chart endpoints with `sourceClass`
and `targetClass`. Its `image` still gives the full expression, including
coefficients. For instance, the edge to the class labelled \(z\) can carry
the assignment \(x\mapsto 2z\).

Each entry in `pages[].relations` has a `kind`, two page-local class IDs
(`source` and `target`), and a TeX `formula`. Use `multiplication` for
products and `extension` for an extension supplied on `degenerationPage`.
