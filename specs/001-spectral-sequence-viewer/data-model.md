# Author input and viewer state

## Implemented first-quadrant schema

| Record | Fields and rules |
| --- | --- |
| Sequence | Required `convention` (cohomological or homological), `firstPage`, `extent`, and nonempty ordered `pages`. Optional `pageCount` equals the array length. Page indices increase by one from firstPage. Optional `degenerationPage` may exceed the last supplied index. |
| Rectangle | Inclusive nonnegative integer `pMin,pMax,qMin,qMax`, each minimum at most its maximum. The extent bounds term records. The independent viewport defaults to the extent. |
| Page | Required `index`, `terms`, and `maps`; optional TeX `formula`. Within each list coordinates are unique. |
| Term | `p,q,status` with status zero, nonzero, or unknown, and optional TeX `label`. Sequence-level `stableTerms` records contain `p,q,fromPage`, unique per coordinate. This makes the declared first stable page available on all later pages. |
| Map | `p,q` locate the source. Required `status` is zero, nonzero, or undetermined. Optional TeX `formula`. The convention and page determine the target. |
| Settings | Optional `settings` contains `initialPage` (default first supplied), `viewport`, `title`, `pLabel`, `qLabel`, and `zeroStyle` (zero, dot, blank; default zero). Sequence-level `unlisted` is unknown by default, or zero. |

Use nonnegative integer page indices and record coordinates. Resolve an unlisted cell inside the extent with the author's unlisted policy. Outside the extent a first-quadrant cell is unknown. Outside the quadrant it is zero. Require map sources in the extent; allow a computed target outside it.

For page r use displacement (r,1−r) in cohomology and (−r,r−1) in homology. Add the displacement for the outgoing target and subtract it for the incoming source. A known zero endpoint or global degeneration forces the map to zero. Local permanence from page s likewise forces incident differentials to vanish from s onward. Reject a nonzero assertion that conflicts with forced vanishing. Otherwise use the stated map status, defaulting to undetermined. Validate bounds, counts, ordering and duplicate keys before accepting the sequence.

Navigation changes the selected page and preserves the inspected coordinate and filter. Changing the filter or zero glyph changes presentation only. Local stability text gives its first page. The selector identifies the supplied degeneration page with infinity and keeps every later supplied page selectable.

## Model changes required by the extended stories

Store signed native bidegrees independently of the declared support. A support restriction gives mathematical vanishing. The data extent governs missing records, and the viewport crops the projected diagram. Key terms, stability declarations, and differential sources by native bidegree under every projection. A component owns a collection of generator-image assignments. The current singular `generator` and `image` fields describe only one assignment.
