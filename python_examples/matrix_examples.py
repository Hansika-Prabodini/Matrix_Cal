import numpy as numpy


def ex1_add() -> numpy.ndarray:
    """
    Matrix addition example corresponding to the EXAMPLES.md.
    This function demonstrates a deterministic 2x2 matrix addition using NumPy.
    See EXAMPLES.md for the Matrix Addition example mapping.
    """
    A = numpy.array([[1, 2], [3, 4]], dtype=int)
    B = numpy.array([[2, 0], [1, 3]], dtype=int)
    return A + B
