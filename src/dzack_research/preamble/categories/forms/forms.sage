r"""Forms as morphisms.

A bilinear form is a morphism out of the tensor square,
$b: M\otimes_R M\to W$, which needs nothing of $W$ but that it be a module --
so this covers every value module, $\mathbb Q/\mathbb Z$ included.

A quadratic form is a morphism $q: M\to W$ with $q(nx)=n^2q(x)$ whose
polarization is bilinear.  Every $q$ here is the diagonal of a bilinear form
read into a coarser value module: $q(x)=B(x,x)$ in $W$.  That is Nikulin's
convention for the discriminant form, where $B$ is the $\mathbb Q$-valued form
of $L^\vee$, $q$ reads it modulo $2\mathbb Z$ and the polarization $b_q$ reads
the same $B$ modulo $\mathbb Z$.  So $q$ and $b_q$ are two forms with two value
modules, each with its own Gram matrix, and neither is a matrix whose entries
live in different places.

This module is the boundary: :class:`BilinearForm` is the one place a Gram
matrix becomes a form.  Everything downstream consumes forms and morphisms and
extracts matrices when it needs them.
"""

from typing import Any

from sage.matrix.matrix0 import Matrix


def tensor_square_relations(morphism: Any) -> Matrix:
    r"""Return the relations of $A\otimes A$ for $A=\operatorname{coker}$ ``morphism``.

    Right exactness of $\otimes$ applied twice: $A\otimes A$ is the cokernel of
    $f\otimes 1$ and $1\otimes f$ together, so its relations are those two
    families stacked.  The point of expressing it this way is that the result is
    again a cokernel of a morphism of free modules, so the owned quotient layer
    covers it with nothing new.
    """
    relations = matrix(ZZ, morphism.matrix())
    identity = identity_matrix(ZZ, relations.ncols())
    return relations.tensor_product(identity).stack(
        identity.tensor_product(relations)
    )


class _BilinearFormData:
    r"""$b: M\otimes_R M\to W$, held as the morphism it is.

    The Gram matrix is this morphism's values on the generators of
    $M\otimes M$, reshaped.  Building one is how a matrix becomes a form; after
    that the form is what gets passed, and the matrix is a reading of it.
    """

    def __init__(self, module: Any, value_module: Any, gram_matrix: Matrix) -> None:
        if not isinstance(gram_matrix, Matrix):
            gram_matrix = matrix(gram_matrix)
        size = len(tuple(module.gens()))
        assert gram_matrix.is_symmetric(), "a bilinear form's Gram matrix is symmetric"
        assert gram_matrix.nrows() == size, (
            f"the Gram matrix is {gram_matrix.nrows()}x{gram_matrix.ncols()} but the "
            f"module has {size} generators"
        )
        assert all(entry in value_module for entry in gram_matrix.list()), (
            f"b takes its values in {value_module}"
        )
        self._module = module
        self._value_module = value_module
        self._gram_matrix = gram_matrix

    def module(self) -> Any:
        return self._module

    def value_module(self) -> Any:
        return self._value_module

    def gram_matrix(self) -> Matrix:
        r"""Return $b$ on the generators, as a matrix over the value module's lift."""
        return self._gram_matrix

    def __call__(self, x: Any, y: Any) -> Any:
        r"""Return $b(x,y)\in W$ for elements ``x`` and ``y`` of :meth:`module`.

        Elements, not coordinate vectors: $b$ is defined on the module, and a
        pair of vectors is a pair of values in $W$ only once someone says which
        generating set they are written in.  The coordinates are read here,
        from elements that already know them.
        """
        for argument in (x, y):
            assert argument.parent() is self._module, (
                "b is defined on elements, and this is not one of "
                f"{self._module}.\n"
                "  - A coordinate vector stands for a combination of "
                "generators only once someone says which: name it with the "
                "module's linear_combination, then pair the elements.\n"
                "  - An element of another module has to be carried here by a "
                "morphism first; a form does not pair across objects.\n"
                f"got: {argument} in {argument.parent()}"
            )
        return self._value_module(
            _coordinate_vector(x) * self._gram_matrix * _coordinate_vector(y)
        )

    def b(self, x: Any, y: Any) -> Any:
        r"""Return $b(x,y)$: for a bilinear form, itself."""
        return self(x, y)

    def polar_form(self) -> "_BilinearFormData":
        r"""Return the bilinear form underlying this one: itself."""
        return self

    def norm(self, x: Any) -> Any:
        r"""Return $b(x,x)$, this form's value on the diagonal."""
        return self(x, x)

    def on_module(self, module: Any) -> "_BilinearFormData":
        r"""Return the same values, read on ``module``'s generators.

        Used to carry $L^\vee$'s form onto $\operatorname{coker} c$, whose
        generators are the images of $L^\vee$'s: the pairings are unchanged, and
        what makes them well defined on classes is :meth:`descends_along`.
        """
        return _BilinearFormData(module, self._value_module, self._gram_matrix)

    def reduced(self, value_module: Any) -> "_BilinearFormData":
        r"""Return the same pairings read in a coarser ``value_module``."""
        return _BilinearFormData(self._module, value_module, self._gram_matrix)

    def pullback(self, morphism: Any) -> "_BilinearFormData":
        r"""Return $f^*b$, the form $(x,y)\mapsto b(f x, f y)$ on ``morphism``'s domain.

        The matrix is extracted here rather than passed in: $f$ is the datum, and
        $MG_BM^{\mathsf T}$ is what it does to the form.
        """
        transporter = morphism.matrix()
        domain = morphism.domain()
        # The module a form is written on is the one its elements belong to,
        # so a form module hands over the module beneath it rather than
        # itself; otherwise this form would refuse the very elements it is
        # about.
        return _BilinearFormData(
            domain.forget_form() if isinstance(domain, FormModule) else domain,
            self._value_module,
            transporter * self._gram_matrix * transporter.transpose(),
        )

    def descends_along(self, morphism: Any) -> bool:
        r"""Return whether $b$ factors through the cokernel of ``morphism``.

        Asked of the $\mathbb Q$-valued form on the codomain, about elements of
        it: $\bar b(\bar x,\bar y)$ is well defined exactly when moving a lift
        by an $f(a)$ changes the pairing by an integer, and by bilinearity it
        is enough to check that on generators of both sides.

        No relation matrix appears.  A relation is $f(a)$ for a generator $a$
        of the domain, which is an element, so this is a statement about
        elements and pairings rather than about rows.
        """
        return all(
            self(morphism(a).forget_form(), g.forget_form()) in ZZ
            for a in morphism.domain().gens()
            for g in morphism.codomain().gens()
        )

    def values_matrix(self) -> tuple:
        r"""Return the Gram matrix as an element of $\mathrm{Mat}_n(W)$.

        Rows of $W$-elements rather than a Sage matrix, because $\mathbb
        Q/\mathbb Z$ is not a ring and has no matrix space; the stored Gram
        matrix holds representatives, and this is what they represent.
        """
        target = self._value_module
        return tuple(
            tuple(target(entry) for entry in row)
            for row in self._gram_matrix.rows()
        )

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, _BilinearFormData):
            return False
        return self.values_matrix() == other.values_matrix()

    def __repr__(self) -> str:
        return (
            f"Bilinear form on {len(tuple(self._module.gens()))} generators "
            f"with values in {self._value_module}"
        )

    def form_module(self) -> Any:
        """Return the single formed parent carrying this bilinear form."""
        formed = FormModule(self)
        match (
            self._module in FreeModules(self._module.base_ring()),
            self._module in TorsionModules(self._module.base_ring()),
        ):
            case (True, False):
                refine(formed, [BilinearFormModules(), FreeFormModules()])
            case (False, True):
                refine(formed, [BilinearFormModules(), TorsionModulesWithForm()])
            case (False, False):
                refine(formed, BilinearFormModules())
        if (
            self._module.base_ring() is ZZ
            and self._module in FreeModules(ZZ)
            and self._value_module is ZZ
        ):
            refine_one_lattice(formed)
        formed._initialize_framing()
        return formed


def BilinearForm(module: Any, value_module: Any, gram_matrix: Matrix) -> Any:
    """Construct the classified formed object for a bilinear form."""
    return _BilinearFormData(module, value_module, gram_matrix).form_module()


class _QuadraticFormData:
    r"""$q: M\to W$, the diagonal $q(x)=B(x,x)$ of a bilinear form read in $W$.

    $B$ is the datum, $W$ says how coarsely to read it, and the two derived
    forms have their own value modules: $q$ into $W$ and the polarization $b_q$
    into the $W$ in which $\tfrac12(q(x+y)-q(x)-q(y))$ is defined -- $\mathbb
    Q/2\mathbb Z$ and $\mathbb Q/\mathbb Z$ for a discriminant form.

    Whether such a $q$ exists is a condition on $B$ and the relations, not on
    this class: it descends to a quotient exactly when the relations have norms
    in $2\mathbb Z$, which is evenness, and the categories that build
    discriminant forms are where that is asserted.
    """

    def __init__(self, bilinear_form: Any, value_module: Any) -> None:
        match bilinear_form:
            case FormModule():
                bilinear_form = bilinear_form.form()
            case _BilinearFormData():
                pass
            case _:
                raise TypeError(
                    "QuadraticForm requires a BilinearForm or its formed object"
                )
        self._lift = bilinear_form
        self._value_module = value_module

    def module(self) -> Any:
        return self._lift.module()

    def value_module(self) -> Any:
        return self._value_module

    def lift_form(self) -> _BilinearFormData:
        r"""Return the $B$ this is the diagonal of."""
        return self._lift

    def __call__(self, x: Any) -> Any:
        r"""Return $q(x)\in W$ for an element ``x`` of :meth:`module`."""
        assert x.parent() is self.module(), (
            "q is defined on elements, and this is not one of "
            f"{self.module()}.\n"
            "  - For a coordinate vector, name the combination of generators "
            "it stands for with the module's linear_combination.\n"
            "  - For an element of another module, apply the morphism that "
            "carries it here.\n"
            f"got: {x} in {x.parent()}"
        )
        coordinates = _coordinate_vector(x)
        return self._value_module(coordinates * self.gram_matrix() * coordinates)

    def polar_form(self) -> _BilinearFormData:
        r"""Return $b_q$, valued where $\tfrac12(q(x+y)-q(x)-q(y))$ lives.

        For $q$ into $\mathbb Q/2\mathbb Z$ that is $\mathbb Q/\mathbb Z$: the
        same $B$, read half as coarsely.
        """
        return self._lift.reduced(self._polar_value_module())

    def _polar_value_module(self) -> Any:
        from sage.groups.additive_abelian.qmodnz import QmodnZ

        assert isinstance(self._value_module, QmodnZ), (
            f"the polarization of a form valued in {self._value_module} is not "
            "derived by halving a modulus; that step is what Q/nZ targets have "
            "and this one does not"
        )
        return QmodnZ(QQ(self._value_module.n) / 2)

    def b(self, x: Any, y: Any) -> Any:
        r"""Return the polarization $b_q(x,y)$."""
        return self.polar_form()(x, y)

    def norm(self, x: Any) -> Any:
        r"""Return $q(x)$, this form's value on the diagonal.

        Finer than $b_q(x,x)$: it lives in $\mathbb Q/2\mathbb Z$, and that
        extra factor of two is the whole difference between $q$ and its
        polarization at the prime 2.
        """
        return self(x)

    def gram_matrix(self) -> Matrix:
        r"""Return $A$, upper triangular, with $q(x)=x^{\mathsf T}Ax$.

        Every entry is a value of $q$'s own $W$: $a_{ii}=B(g_i,g_i)$ and
        $a_{ij}=2B(g_i,g_j)$ for $i<j$, which is the coefficient of $x_ix_j$ in
        $\sum_{i\le j}a_{ij}x_ix_j$.  A symmetric matrix would be the polar
        form's, and reading $q$ off its diagonal while reading $b_q$ off the
        rest is what puts two value modules in one array.
        """
        gram = self._lift.gram_matrix()
        size = gram.nrows()
        upper = matrix(gram.base_ring(), size, size)
        for i in range(size):
            upper[i, i] = gram[i, i]
            for j in range(i + 1, size):
                upper[i, j] = 2 * gram[i, j]
        upper.subdivide(*gram.subdivisions())
        return upper

    def on_module(self, module: Any) -> "_QuadraticFormData":
        r"""Return the same $q$, read on ``module``'s generators."""
        return _QuadraticFormData(self._lift.on_module(module), self._value_module)

    def pullback(self, morphism: Any) -> "_QuadraticFormData":
        r"""Return $f^*q = q\circ f$ on ``morphism``'s domain."""
        return _QuadraticFormData(self._lift.pullback(morphism), self._value_module)

    def descends_along(self, morphism: Any) -> bool:
        r"""Return whether $q$ factors through the cokernel of ``morphism``.

        Two conditions, because $q$ is coarser than $B$ in one direction and
        finer in the other: $B$ itself has to descend, and every $f(a)$ has to
        have $q$-norm zero -- which for $\mathbb Q/2\mathbb Z$ is evenness.
        The first is asked of the $\mathbb Q$-valued $B$ rather than of the
        polarization, because that is where integrality is a question at all.
        """
        if not self._lift.descends_along(morphism):
            return False
        return all(
            self(morphism(a).forget_form()) == self._value_module.zero()
            for a in morphism.domain().gens()
        )

    def values_matrix(self) -> tuple:
        r"""Return $A$ as an element of $\mathrm{Mat}_n(W)$."""
        target = self._value_module
        return tuple(
            tuple(target(entry) for entry in row)
            for row in self.gram_matrix().rows()
        )

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, _QuadraticFormData):
            return False
        return self.values_matrix() == other.values_matrix()

    def __repr__(self) -> str:
        return (
            f"Quadratic form on {len(tuple(self.module().gens()))} generators "
            f"with values in {self._value_module}"
        )

    def form_module(self) -> Any:
        """Return the single formed parent carrying this quadratic form."""
        formed = FormModule(self)
        match (
            self.module() in FreeModules(self.module().base_ring()),
            self.module() in TorsionModules(self.module().base_ring()),
        ):
            case (True, False):
                refine(formed, [QuadraticFormModules(), FreeFormModules()])
            case (False, True):
                refine(formed, [QuadraticFormModules(), TorsionModulesWithForm()])
            case (False, False):
                refine(formed, QuadraticFormModules())
        formed._initialize_framing()
        return formed


def QuadraticForm(module: Any, value_module: Any, gram_matrix: Matrix) -> Any:
    """Construct the classified formed object for a quadratic form."""
    lift = _BilinearFormData(module, QQ, gram_matrix)
    return _QuadraticFormData(lift, value_module).form_module()
