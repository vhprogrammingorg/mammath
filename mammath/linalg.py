import numpy as np
from .geometry import sin, cos, atan

"""
LINEAR ALGEBRA
"""
def diagonal_sum(mat):
    """
    Returns the sum of the diagonal elements in a matrix
    """
    left = 0
    right = 0
    for i in range(0, len(mat)):
        left += mat[i][i]
        right += mat[i][len(mat) - i - 1]
    total = left + right
    if len(mat) % 2 != 0:
        return total - (mat[len(mat) // 2][len(mat) // 2])
    return total

def adjoint2x2(matrix):
    return np.array([[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]]).tolist()

def adjoint3x3(matrix):
    a = np.array([[(matrix[1][1]*matrix[2][2]) - (matrix[1][2]*matrix[2][1]),
                   -((matrix[1][0]*matrix[2][2]) - (matrix[1][2]*matrix[2][0])),
                   ((matrix[1][0]*matrix[2][1]) - (matrix[1][1]*matrix[2][0]))],
                                    
                  [-((matrix[0][1]*matrix[2][2]) - (matrix[0][2]*matrix[2][1])),
                    ((matrix[0][0]*matrix[2][2]) - (matrix[0][2]*matrix[2][0])),
                    -((matrix[0][0]*matrix[2][1]) - (matrix[0][1]*matrix[2][0]))],
                                    
                  [((matrix[0][1]*matrix[1][2]) - (matrix[0][2]*matrix[1][1])),
                   -((matrix[0][0]*matrix[1][2]) - (matrix[0][2]*matrix[1][0])),
                    ((matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0]))]])

    return np.transpose(a)

def cofactor_matrix(matrix, tempMatrix, row, col, order):
    """
    Helper function for finding the cofactor matrix, which can be transposed to get the adjoint matrix, useful for finding the inverse of a matrix
    """
    i = 0
    j = 0
    for r in range(order):
        for c in range(order):
            if r != row and c != col:
                tempMatrix[i][j] = matrix[r][c]
                j += 1
                if j == order - 1:
                    j = 0
                    i += 1

def adjoint(matrix):
    """
    Computes the adjoint of an NxN matrix.

    Args:
        matrix: An NxN list of lists representing the matrix.

    Returns:
        The adjoint of the matrix as an NxN list of lists.
    """
    n = len(matrix)
    adj = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            sign = (-1) ** (i + j)
            sub_matrix = [row[:j] + row[j+1:] for row in matrix[:i] + matrix[i+1:]]
            adj[j][i] = sign * determinant(sub_matrix)
    return adj

def determinant(matrix):
    """
    Computes the determinant of an NxN matrix.

    Args:
        matrix: An NxN list of lists representing the matrix.

    Returns:
        The determinant of the matrix.
    """
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(n):
            sub_matrix = [row[:i] + row[i+1:] for row in matrix[1:]]
            sign = (-1) ** i
            det += sign * matrix[0][i] * determinant(sub_matrix)
        return det

def inverse(matrix):
    """
    Computes the inverse of an NxN matrix.

    Args:
        matrix: An NxN list of lists representing the matrix.

    Returns:
        The inverse of the matrix as an NxN list of lists.
    """
    det = determinant(matrix)
    if det == 0:
        raise ValueError("The matrix is not invertible")
    adj = adjoint(matrix)
    inv = [[adj[i][j] / det for j in range(len(adj))] for i in range(len(adj))]
    return inv

def mat_gauss_elim(mat, sol):
    """
    Enter an nxn 2D list of coefficients and n length list of solutions such as:
    3x + 5y + z = 3, y + z = 8, x + 4y + 2z = 4
    to 3x3 list
    [[3, 5, 1], [0, 1, 1], [1, 4, 2]]
    and [3, 8, 4]
    """
    a = inverse(mat)
    new = np.matmul(a, [[i] for i in sol])
    return [i[0] for i in new]

class vector:
    def __init__(self):
        self.init = False
    def ij(self, i, j):
        self.ihat, self.jhat, self.mag, self.theta = i, j, (i ** 2 + j ** 2) ** (1 / 2), atan(j / i)
        self.init = True
    def magtheta(self, mag, theta):
        self.ihat, self.jhat, self.mag, self.theta = mag * cos(theta), mag * sin(theta), mag, theta
        self.init = True

def addvec(v1, v2):
    '''
    Vector v1 plus vector v2.
    '''
    if not v1.init or not v2.init:
        raise Exception("Vector not initialized")
    new = vector()
    new.ij(v1.ihat + v2.ihat, v1.jhat + v2.jhat)
    return new

def scalarvec(v, s):
    '''
    Vector v multiplied by scalar s.
    '''
    if not v.init:
        raise Exception("Vector not initialized")
    new = vector()
    new.ij(v.ihat * s, v.jhat * s)
    return new

def subvec(v1, v2):
    '''
    Vector v1 minus Vector v1.
    '''
    if not v1.init or not v2.init:
        raise Exception("Vector not initialized")
    return addvec(v1, scalarvec(v2, -1))

def crossprod(v1, v2):
    '''
    Returns the magnitude of the v1 cross v2 along the z axis.
    '''
    if not v1.init or not v2.init:
        raise Exception("Vector not initialized")
    return v1.ihat * v2.jhat - v1.jhat * v2.ihat

def dotprod(v1, v2):
    '''
    Returns the dot product of v1 and v2.
    '''
    if not v1.init or not v2.init:
        raise Exception("Vector not initialized")
    return v1.ihat * v2.ihat + v1.jhat * v2.jhat


"""
END OF LINEAR ALGEBRA
"""


