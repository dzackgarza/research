# Category Creation: Base Rings and Module Categories

There are three interlocking mechanisms to understand here.

## 1. `_refine_category_` — enrolling existing objects

`_refine_category_` is the proper non-monkey-patching way to add `ZZ`, `QQ`, `Zp`, etc.
to a new category. It computes the join of the object's current category with the new
one, and for Python-based parents also updates the dynamic class:

```python
# At import time in your package:
ZZ._refine_category_(ModuleBaseRings())
QQ._refine_category_(ModuleBaseRings())
```

After this, `ZZ in ModuleBaseRings()` is `True`, and methods from
`ModuleBaseRings.ParentMethods` become accessible.

**Important caveat for Cython types:** `ZZ` is a Cython extension type
(`IntegerRing_class`), so `can_assign_class(ZZ)` is `False` — `_refine_category_`
updates `ZZ._category` but does NOT replace `ZZ.__class__` with a dynamic subclass.
Methods from `ParentMethods` are still reachable via `__getattr__` →
`getattr_from_category`, which looks up `self.category().parent_class`. `QQ` (a Python
class `RationalField_with_category`) gets its class replaced directly.

## 2. Defining `ModuleBaseRings` as a `Category_singleton`

```python
from sage.categories.category_singleton import Category_singleton
from sage.categories.rings import Rings

class ModuleBaseRings(Category_singleton):
    """Rings that are valid base rings for MyModules."""
    def super_categories(self):
        return [Rings()]

    class ParentMethods:
        def my_new_ring_method(self):
            ...
```

Use `Category_singleton` (not plain `Category`) for the `x in ModuleBaseRings()`
containment check to be fast — it uses a Cython `isinstance` check on the parent class
rather than traversing the category graph.

## 3. Defining `MyModules(R)` as a `Category_over_base_ring`

```python
from sage.categories.category_types import Category_over_base_ring
from sage.categories.category import Category

class MyModules(Category_over_base_ring):
    def __init__(self, base):
        if not (base in ModuleBaseRings() or
                isinstance(base, Category) and base.is_subcategory(ModuleBaseRings())):
            raise ValueError("base must be in ModuleBaseRings()")
        Category_over_base_ring.__init__(self, base)

    def super_categories(self):
        from sage.categories.modules import Modules
        return [Modules(self.base_ring())]

    class ParentMethods:
        ...
```

The `__init__` of `Category_over_base_ring` only checks `base in Rings()`.

You override it to check `base in ModuleBaseRings()` instead.

## The `_make_named_class_key` implication

`Category_over_base._make_named_class_key` returns `self.__base.category()` when the
base is a parent:

This means `MyModules(ZZ).parent_class` depends on `ZZ.category()`. If you call
`ZZ._refine_category_(ModuleBaseRings())` **after** `MyModules(ZZ)` has been
constructed, the cached `parent_class` could be stale.
The framework detects this and recomputes.

So you should call `_refine_category_` on all your base rings **before** constructing
any `MyModules(R)` instances — i.e., at package import time.

## Passing a category as base

You can also pass `ModuleBaseRings()` itself as the base:

```python
MyModules(ModuleBaseRings())   # generic: all modules over any ModuleBaseRing
MyModules(ZZ)                   # specific: ZZ-modules
```

The `_subcategory_hook_` in `Category_over_base_ring` handles this:
`MyModules(ZZ).is_subcategory(MyModules(ModuleBaseRings()))` returns `True` if
`ZZ in ModuleBaseRings()`.

This is the same pattern used by `VectorSpaces(Fields())` vs `VectorSpaces(QQ)`.

## Summary of the full pattern

```python
# 1. Define the base ring category
class ModuleBaseRings(Category_singleton):
    super_categories → [Rings()]
    ParentMethods → new methods on ZZ, QQ, etc.

# 2. Enroll specific rings at import time
ZZ._refine_category_(ModuleBaseRings())
QQ._refine_category_(ModuleBaseRings())
Zp(p)._refine_category_(ModuleBaseRings())  # for each p you care about

# 3. Define the module category
class MyModules(Category_over_base_ring):
    __init__ → validates base in ModuleBaseRings()
    super_categories → [Modules(self.base_ring())]
    ParentMethods → new methods on modules
```

The `_refine_category_` calls are the only "mutation" of existing Sage objects, and they
are explicitly supported by the framework — the same mechanism is used internally (e.g.,
`_is_Field` calls `x._refine_category_(_Fields)` on rings that turn out to be fields).

### Citations

**File:** src/sage/structure/parent.pyx (L345-438)
```text
    def _refine_category_(self, category):
        """
        Change the category of ``self`` into a subcategory.

        INPUT:

        - ``category`` -- a category or list or tuple thereof

        The new category is obtained by adjoining ``category`` to the
        current one.

        .. NOTE::

            The class of ``self`` might be replaced by a sub-class.

        .. SEEALSO::

            :meth:`CategoryObject._refine_category`

        EXAMPLES::

            sage: P.<x,y> = QQ[]
            sage: Q = P.quotient(x^2 + 2)
            sage: Q.category()
            Join of
             Category of commutative rings and
             Category of subquotients of monoids and
             Category of quotients of semigroups
            sage: first_class = Q.__class__
            sage: Q._refine_category_(Fields())
            sage: Q.category()
            Join of
             Category of fields and
             Category of subquotients of monoids and
             Category of quotients of semigroups
            sage: first_class == Q.__class__
            False
            sage: TestSuite(Q).run()                                                    # needs sage.libs.singular

        TESTS:

        Here is a test against :issue:`14471`. Refining the category will issue
        a warning, if this change affects the hash value (note that this will
        only be seen in doctest mode)::

            sage: class MyParent(Parent):
            ....:     def __hash__(self):
            ....:         return hash(type(self))   # subtle mistake
            sage: a = MyParent()
            sage: h_a = hash(a)
            sage: a._refine_category_(Algebras(QQ))
            hash of <class '__main__.MyParent_with_category'> changed in
            Parent._refine_category_ during initialisation

            sage: b = MyParent(category=Rings())
            sage: h_b = hash(b)
            sage: h_a == h_b
            False
            sage: b._refine_category_(Algebras(QQ))
            hash of <class '__main__.MyParent_with_category'> changed in
            Parent._refine_category_ during refinement
            sage: hash(a) == hash(b)
            True
            sage: hash(a) != h_a
            True
        """
        cdef Py_hash_t hash_old = -1
        if debug.refine_category_hash_check:
            # check that the hash stays the same after refinement
            hash_old = hash(self)

        if self._category is None:
            self._init_category_(category)
            if hash_old != -1 and hash_old != hash(self):
                print(f'hash of {type(self)} changed in Parent._refine_category_ during initialisation')
            return
        if category is self._category:
            return
        CategoryObject._refine_category_(self, category)
        category = self._category

        # This substitutes the class of this parent to a subclass
        # which also subclasses the parent_class of the category.
        # However, we only do so if we do not have an extension class.
        if can_assign_class(self):
            # We tested in the very beginning that this parent
            # had its category initialised. Hence, the class
            # is already a dynamic class.
            base = self.__class__.__base__
            # documentation transfer is handled by dynamic_class
            self.__class__ = dynamic_class(
                "%s_with_category" % base.__name__,
                (base, category.parent_class),
                doccls=base)
```

**File:** src/sage/structure/category_object.pyx (L244-257)
```text
            sage: type(QQ)
            <class 'sage.rings.rational_field.RationalField_with_category'>
            sage: QQ._underlying_class()
            <class 'sage.rings.rational_field.RationalField'>
            sage: type(ZZ)
            <... 'sage.rings.integer_ring.IntegerRing_class'>
            sage: ZZ._underlying_class()
            <... 'sage.rings.integer_ring.IntegerRing_class'>
        """
        cls = type(self)
        if isinstance(cls, DynamicMetaclass):
            return cls.__bases__[0]
        else:
            return cls
```

**File:** src/sage/categories/category_singleton.pyx (L83-145)
```text
class Category_singleton(Category):
    """
    A base class for implementing singleton category.

    A *singleton* category is a category whose class takes no
    parameters like ``Fields()`` or ``Rings()``. See also the
    :wikipedia:`Singleton design pattern <Singleton_pattern>`.

    This is a subclass of :class:`Category`, with a couple
    optimizations for singleton categories.

    The main purpose is to make the idioms::

        sage: QQ in Fields()
        True
        sage: ZZ in Fields()
        False

    as fast as possible, and in particular competitive to calling a
    constant Python method, in order to foster its systematic use
    throughout the Sage library. Such tests are time critical, in
    particular when creating a lot of polynomial rings over small
    fields like in the elliptic curve code.

    EXAMPLES::

        sage: from sage.categories.category_singleton import Category_singleton
        sage: class MyRings(Category):
        ....:     def super_categories(self): return Rings().super_categories()
        sage: class MyRingsSingleton(Category_singleton):
        ....:     def super_categories(self): return Rings().super_categories()

    We create three rings. One of them is contained in the usual category of
    rings, one in the category of "my rings" and the third in the category of
    "my rings singleton"::

        sage: R = QQ['x,y']
        sage: R1 = Parent(category = MyRings())
        sage: R2 = Parent(category = MyRingsSingleton())
        sage: R in MyRings()
        False
        sage: R1 in MyRings()
        True
        sage: R1 in MyRingsSingleton()
        False
        sage: R2 in MyRings()
        False
        sage: R2 in MyRingsSingleton()
        True

    One sees that containment tests for the singleton class is a lot faster
    than for a usual class::

        sage: # not tested
        sage: timeit("R in MyRings()", number=10000)
        10000 loops, best of 3: 7.12 µs per loop
        sage: timeit("R1 in MyRings()", number=10000)
        10000 loops, best of 3: 6.98 µs per loop
        sage: timeit("R in MyRingsSingleton()", number=10000)
        10000 loops, best of 3: 3.08 µs per loop
        sage: timeit("R2 in MyRingsSingleton()", number=10000)
        10000 loops, best of 3: 2.99 µs per loop
```

**File:** src/sage/categories/category_types.py (L215-251)
```python
    def _make_named_class_key(self, name):
        r"""
        Return what the element/parent/... classes depend on.

        Since :issue:`11935`, the element and parent classes of a
        category over base only depend on the category of the base (or
        the base itself if it is a category).

        .. SEEALSO::

            - :meth:`CategoryWithParameters`
            - :meth:`CategoryWithParameters._make_named_class_key`

        EXAMPLES::

            sage: Modules(ZZ)._make_named_class_key('element_class')
            Join of Category of Dedekind domains
             and Category of euclidean domains
             and Category of noetherian rings
             and Category of infinite enumerated sets
             and Category of metric spaces
            sage: Modules(QQ)._make_named_class_key('parent_class')
            Join of Category of number fields
             and Category of quotient fields
             and Category of metric spaces
            sage: Schemes(Spec(ZZ))._make_named_class_key('parent_class')
            Category of schemes
            sage: ModularAbelianVarieties(QQ)._make_named_class_key('parent_class')
            Join of Category of number fields
             and Category of quotient fields
             and Category of metric spaces
            sage: Algebras(Fields())._make_named_class_key('morphism_class')
            Category of fields
        """
        if isinstance(self.__base, Category):
            return self.__base
        return self.__base.category()
```

**File:** src/sage/categories/category_types.py (L347-362)
```python
class Category_over_base_ring(Category_over_base):
    def __init__(self, base, name=None):
        """
        Initialize ``self``.

        EXAMPLES::

            sage: C = Algebras(GF(2)); C
            Category of algebras over Finite Field of size 2
            sage: TestSuite(C).run()
        """
        from sage.categories.rings import Rings
        if not (base in Rings() or
                isinstance(base, Category) and base.is_subcategory(Rings())):
            raise ValueError("base must be a ring or a subcategory of Rings()")
        Category_over_base.__init__(self, base, name)
```

**File:** src/sage/categories/category_types.py (L480-492)
```python
        if not issubclass(C.parent_class, self.parent_class):
            return False
        if not isinstance(C, Category_over_base_ring):
            return Unknown
        base_ring = self.base_ring()
        if C.base_ring() is base_ring:
            return True
        if isinstance(base_ring, Category):
            if isinstance(C.base(), Category):
                return C.base().is_subcategory(base_ring)
            # otherwise, C.base() is a parent
            return C.base() in base_ring
        return False
```

**File:** src/sage/categories/category.py (L2836-2851)
```python
        """
        cls = self.__class__
        if isinstance(cls, DynamicMetaclass):
            cls = cls.__base__
        key = (cls, name, self._make_named_class_key(name))
        try:
            return self._make_named_class_cache[key]
        except KeyError:
            pass
        result = Category._make_named_class(self, name, method_provider,
                                            cache=cache, **options)
        if key[2] != self._make_named_class_key(name):
            # the object in the parameter may have had its category refined, which might modify the key
            # throw result away and recompute
            return self._make_named_class(name, method_provider, cache=cache, **options)
        self._make_named_class_cache[key] = result
```

**File:** src/sage/rings/ring.pyx (L650-658)
```text
    # The result is not immediately returned, since we want to refine
    # x's category, so that calling x in Fields() will be faster next time.
    try:
        result = isinstance(x, Field) or x.is_field()
    except AttributeError:
        result = False
    if result:
        x._refine_category_(_Fields)
    return result
```
