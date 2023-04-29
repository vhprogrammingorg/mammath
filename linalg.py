import numpy as np

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

def determinant(matrix, order=1):
    """
    Returns the determinant of an nxn matrix
    """
    det = 0
    order = len(matrix[0])-1
    print(order)
    if order == 1:
        return matrix[0][0]
    tempMatrix = [[None for i in range(order)] for i in range(order)]
    sign = 1

    for f in range(order):
        cofactor_matrix(matrix, tempMatrix, 0, f, order)
        det += sign * matrix[0][f] * determinant(tempMatrix, order = order - 1)
        sign = -sign

    return det    

"""
END OF LINEAR ALGEBRA
"""


