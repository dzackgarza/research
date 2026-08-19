from sage.all import MatrixGroup


def get_affine_matrix_group(G_affine):
    mats = list(G_affine._GL) # Iterate over the GL(1,F) group to get its elements
    vecs = list(G_affine.vector_space()) # Iterate over the vector space to get its elements

    elements_as_matrices = []
    for A_gl in mats:
        for b_vec in vecs:
            # Construct an AffineGroupElement using its element_class
            # Then get its matrix representation.
            affine_element = G_affine.element_class(G_affine, A_gl, b_vec, check=False, convert=False)
            elements_as_matrices.append(affine_element.matrix())
    return MatrixGroup(elements_as_matrices)
