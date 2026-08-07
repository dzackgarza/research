from sage.all import *
from sage.matrix.matrix0 import Matrix

class MyMatrix(Matrix):
    def __init__(self, parent, morphism):
        # Matrix.__init__(self, parent) # Matrix has no __init__ that takes parent?
        self._morphism = morphism

try:
    MS = MatrixSpace(ZZ, 2)
    m = MS([1,0,0,1])
    # Can we just change the class of an existing matrix?
    m.__class__ = MyMatrix
    print("Class changed successfully")
    m._morphism = "test"
    print(f"Morphism: {m._morphism}")
except Exception as e:
    print(f"Error: {e}")

