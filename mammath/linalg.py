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

def matrix_inverse(matrix):
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

def matrix_transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def matrix_multiply(A, B):
    result = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
    return result

def mat_gauss_elim(mat, sol):
    """
    Enter an nxn 2D list of coefficients and n length list of solutions such as:
    3x + 5y + z = 3, y + z = 8, x + 4y + 2z = 4
    to 3x3 list
    [[3, 5, 1], [0, 1, 1], [1, 4, 2]]
    and [3, 8, 4]
    """
    a = matrix_inverse(mat)
    new = np.matmul(a, [[i] for i in sol])
    return [i[0] for i in new]

def eigenvalues_and_eigenvectors(matrix_data, num_simulations=100):
    matrix = Matrix(matrix_data)
    eigenvalue, eigenvector = matrix.power_iteration(num_simulations)
    return eigenvalue, eigenvector

def linear_least_squares(A, b):
    A_T = matrix_transpose(A)
    A_T_A = matrix_multiply(A_T, A)
    A_T_A_inv = matrix_inverse(A_T_A)
    A_T_b = matrix_multiply(A_T, [[x] for x in b])
    x = matrix_multiply(A_T_A_inv, A_T_b)
    return [xi[0] for xi in x]

class Vector:
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
    new = Vector()
    new.ij(v1.ihat + v2.ihat, v1.jhat + v2.jhat)
    return new

def scalarvec(v, s):
    '''
    Vector v multiplied by scalar s.
    '''
    if not v.init:
        raise Exception("Vector not initialized")
    new = Vector()
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

class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])
        if not all(len(row) == self.cols for row in data):
            raise ValueError("All rows must have the same number of columns")
    
    def multiply_vector(self, vec):
        """
        Multiplies the matrix by a vector.

        Args:
            vec (list): The vector to multiply by.

        Returns:
            list: The resulting vector after multiplication.
        """
        result = [sum(row[j] * vec[j] for j in range(self.cols)) for row in self.data]
        return result
    
    def transpose(self):
        """
        Transposes the matrix.

        Returns:
            Matrix: A new Matrix object that is the transpose of the original.
        """
        transposed_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrix(transposed_data)
    
    def subtract_identity(self, lam):
        """
        Subtracts lambda times the identity matrix from the matrix.

        Args:
            lam (float): The scalar value to subtract along the diagonal.

        Returns:
            Matrix: A new Matrix object after the subtraction.
        """
        result = [[self.data[i][j] - (lam if i == j else 0) for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)
    
    def norm(self, vec):
        """
        Computes the Euclidean norm of a vector.

        Args:
            vec (list): The vector to compute the norm of.

        Returns:
            float: The Euclidean norm of the vector.
        """
        return sum(x**2 for x in vec) ** 0.5
    
    def normalize(self, vec):
        """
        Normalizes a vector to have unit norm.

        Args:
            vec (list): The vector to normalize.

        Returns:
            list: The normalized vector.
        """
        norm = self.norm(vec)
        return [x / norm for x in vec]
    
    def power_iteration(self, num_simulations=100):
        """
        Performs power iteration to find the dominant eigenvalue and corresponding eigenvector.

        Args:
            num_simulations (int, optional): The number of iterations to perform. Defaults to 100.

        Returns:
            tuple: The dominant eigenvalue and the corresponding eigenvector.
        """
        b_k = [1] * self.rows
        for _ in range(num_simulations):
            b_k1 = self.multiply_vector(b_k)
            b_k1_norm = self.norm(b_k1)
            b_k = self.normalize(b_k1)
        eigenvalue = self.multiply_vector(b_k)[0] / b_k[0]
        eigenvector = b_k
        return eigenvalue, eigenvector

"""
END OF LINEAR ALGEBRA
"""


