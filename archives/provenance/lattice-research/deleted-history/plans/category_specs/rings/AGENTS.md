
GOAL: record the entirety of the existing set of ring methods as a proper set of ABC specs on specific sets of subcategories.
This should operate as a replacement for the categories SageX where X = Rings, PIDs, etc, which operates non-destructively by intercepting and overwriting all constructors, using existing implementations wherever possible, and refining the results to lie in the new subcategory hierarchy.
Tasks:
    - Ensure all named rings have a specific one-object subcategory speccing their methods, e.g. Rings.ZZ() = {ZZ} is the category whose parentmethods spec what methods ZZ should have.
        - N.B. some categories like Rings.Zp() = {Zp(2), Zp(3), Zp(5), ...,} are parameterized by another object like an integer, a tuple of integers, another ring, etc, and that's fine.
    - Find and list all named sage rings X and expose Rings().Constructors().X() to return it. E.g. PolynomialRing(...), MatrixRing(...), ZZ, Zp(..), QQ, Qp, QQbar, RR, CC, etc, all refined to these subcategories.
    - Spot-check at runtime to find all methods on these ring objects, and ensure *all* ring-specific methods are reflected in the spec as an abstractmethod in some subcategory's parentmethods (do not try to automate or script this, just manual checks)
    - Check all upstream concrete ring implementations for ring/ideal/etc-related methods and ensure they're all in the spec
    - Check all upstream ring-specific subcategories and ensure their methods/properties/etc are represented in this subcategory hierarchy
    - Ensure that each of the 10+ named rings and constructors have a subcategory of rings that precisely corresponds to a subcategory in the new hierarchy speccing it.
