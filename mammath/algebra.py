from .operations import *
from .geometry import *
from .helper import parse_equation, preprocess_equation
import numpy as np

"""
ALGEBRA
"""

def quadratic_solver(a,b,c) -> tuple:
    """
    Returns the roots of any quadratic equation in the form of ax^2 + bx + c = 0
    """
    dis = b**2 - 4*a*c
    if dis != 0:
        return (-b + csqrt(dis))/(2*a), (-b - csqrt(dis))/(2*a)
    return (-b / (2*a))

def discriminant_quadratic(a, b, c):
    """
    Discriminant of a quadratic equation in the form of ax^2 + bx + c = 0
    """
    return b**2 - 4 * a * c

def rootp_quadratic(a, b, c, disc):
    """
    Returns the positive root of a quadratic equation in the form of ax^2 + bx + c = 0
    """
    return (-b + disc ** (1/2)) / (2 * a)

def rootm_quadratic(a, b, c, disc):
    """
    Returns the negative root of a quadratic equation in the form of ax^2 + bx + c = 0
    """
    return (-b - disc ** (1/2)) / (2 * a)

def roots_quadratic(a, b, c):
    """
    Returns the roots of a quadratic equation in the form of ax^2 + bx + c = 0 as a tuple
    """
    return (rootp_quadratic(a, b, c, discriminant_quadratic(a, b, c), rootm_quadratic(a, b, c, discriminant_quadratic(a, b, c))))
            
def solve_first_degree(b, c):
    """
    Returns the solution of a first degree equation in the form of bx+c=0
    """
    return -c / b

def second_degree_solver(a, b, c, formatted = False):
    """
    Returns the solutions up to a second degree equation

    Args:
    a, b, c (floats): The coefficients
    formatted (boolean): Whether the returned value is a formatted string or the numerical solutions. Set to false by default
    """
    if a == 0:
        if b == 0:
            return "The equation is indeterminate" if c == 0 else "Impossible situation. Wrong entries"
        if print:
            return f"It is a first degree equation. Solution: {'0.0' if c == 0 else solve_first_degree(b, c)}"
        else:
            return '0.0' if c == 0 else solve_first_degree(b, c)
    else:
        disc = discriminant_quadratic(a, b, c)
        if disc < 0:
            return "There are no real solutions"
        elif disc == 0:
            root = rootm_quadratic(a, b, c, disc)
            if print:
                return f"It has one double solution: {abs(root)}"
            else:
                return abs(root)
        else:
            root1, root2 = rootm_quadratic(a, b, c, disc), roots_quadratic(a, b, c, disc)
            sorted_sol = sorted([abs(root1) if root1 == -0.0 else root1, abs(root2) if root2 == -0.0 else root2])
            if print:
                return f"Two solutions: {sorted_sol[0]}, {sorted_sol[1]}"
            else:
                return (sorted_sol[0], sorted_sol[1])
        
def solve_gauss_elimination(*equations):
    """
    Solves any system of equations using Gaussian Elimination. Standard equation input supported.
    """
    equations = list(equations)
    for i in range(0, len(equations)):
        equations[i] = equations[i].replace(" ", "")
        
    eqs = []
    varis = set()
    for k in range(len(equations)):
        equations[k] = equations[k].replace('-','+-')
        eqDict = dict()
        sides = equations[k].split('=')
        termsLeft = sides[0].split('+')
        termsRight = sides[1].split('+')
        for term in termsLeft:
            if term != '':
                if term.isnumeric():
                    if 'constant' in eqDict:
                        eqDict['constant'] += -int(term)
                    else:
                        eqDict['constant'] = -int(term)
                    continue
                elif not '-' in term:
                    if term.isalpha():
                        coeff = 1
                        vari = term
                    else:
                        l = 0
                        while term[l].isdigit():
                            l += 1
                        coeff = int(term[:l])
                        vari = term[l:]
                else:
                    if term[1:].isnumeric():
                        if 'constant' in eqDict:
                            eqDict['constant'] += -int(term)
                        else:
                            eqDict['constant'] = -int(term)
                        continue
                    elif term[1:].isalpha():
                        coeff = -1
                        vari = term[1:]
                    else:
                        l = 1
                        while term[l].isdigit():
                            l += 1
                        coeff = -int(term[1:l])
                        vari = term[l:]
                varis.add(vari)
                if vari in eqDict:
                    eqDict[vari] += coeff
                else:
                    eqDict[vari] = coeff
        for term in termsRight:
            if term != '':
                if term.isnumeric():
                    if 'constant' in eqDict:
                        eqDict['constant'] += int(term)
                    else:
                        eqDict['constant'] = int(term)
                    continue
                elif not '-' in term:
                    if term.isalpha():
                        coeff = -1
                        vari = term
                    else:
                        l = 0
                        while term[l].isdigit():
                            l += 1
                        coeff = -int(term[:l])
                        vari = term[l:]
                else:
                    if term[1:].isnumeric():
                        if 'constant' in eqDict:
                            eqDict['constant'] += int(term)
                        else:
                            eqDict['constant'] = int(term)
                        continue
                    if term[1:].isalpha():
                        coeff = 1
                        vari = term[1:]
                    else:
                        l = 1
                        while term[l].isdigit():
                            l += 1
                        coeff = int(term[1:l])
                        vari = term[l:]
                varis.add(vari)
                if vari in eqDict:
                    eqDict[vari] += coeff
                else:
                    eqDict[vari] = coeff
        if not 'constant' in eqDict:
            eqDict['constant'] = 0
        eqs.append(eqDict)
    if len(eqs) < len(varis):
        return None
    varis = sorted(list(varis))
    matrix = []
    for eq in eqs:
        row = []
        for vari in varis:
            if vari in eq:
                row.append(eq[vari])
            else:
                row.append(0)
        matrix.append(row)
    b = [eq['constant'] for eq in eqs]
    
    nothingHappened = False
    while not nothingHappened:
        nothingHappened = True
        for i1 in range(len(matrix)-1):
            for i2 in range(1+i1,len(matrix)):
                j1 = 0
                while matrix[i1][j1] == 0:
                    j1 += 1
                j2 = 0
                while matrix[i2][j2] == 0:
                    j2 += 1
                if [matrix[i1][j]/matrix[i1][j1] for j in range(len(matrix[i1]))] == [matrix[i2][j]/matrix[i2][j2] for j in range(len(matrix[i2]))]:
                    if b[i1]/matrix[i1][j1] != b[i2]/matrix[i2][j2]:
                        return None
                    else:
                        matrix = matrix[:i1]+matrix[i1+1:]
                        b = b[:i1]+b[i1+1:]
                        nothingHappened = False
                        break
            if not nothingHappened:
                break
    if len(matrix) != len(matrix[0]):
        return None
    n = 0
    while n < len(matrix):
        while matrix[n][n] == 0:
            if n == len(matrix)-1:
                return None
            r = matrix[n]
            matrix.pop(n)
            matrix.append(r)
            v = b[n]
            b.pop(n)
            b.append(v)
        c = 1/matrix[n][n]
        matrix[n] = [c*matrix[n][j] for j in range(len(matrix[n]))]
        b[n] = c*b[n]
        k = 1
        while n+k < len(matrix):
            c = matrix[n+k][n]
            matrix[n+k] = [matrix[n+k][j] - c*matrix[n][j] for j in range(len(matrix[n]))]
            if matrix[n+k] == [0]*len(matrix[n+k]):
                return None
            b[n+k] = b[n+k] - c*b[n]
            k += 1
        n += 1
    n = len(matrix)-1
    while n >= 0:
        k = 1
        while n-k >= 0:
            c = matrix[n-k][n]
            matrix[n-k] = [matrix[n-k][j] - c*matrix[n][j] for j in range(len(matrix[n]))]
            b[n-k] = b[n-k] - c*b[n]
            k += 1
        n -= 1
    answer = {}
    for k in range(len(varis)):
        answer[varis[k]] = b[k]
    return answer

def linear_system_2x2(equation1: str, equation2: str, print = False):
    """
    Solves a 2x2 system of equations
    """
    coefficients1, product1 = parse_equation(equation1)
    coefficients2, product2 = parse_equation(equation2)

    coefficientsMatrix = np.array([coefficients1, coefficients2])
    productMatrix = np.array([[product1], [product2]])

    solMatrix = np.linalg.solve(coefficientsMatrix, productMatrix)
    sols = [round(float(x), 1) if round(float(x)) == float(x) else "%0.4f" % x for x in solMatrix.flatten()]
    check = np.allclose(np.dot(coefficientsMatrix, solMatrix), productMatrix)

    return (print(f"x: {sols[0]}\ny: {sols[1]}") if print else sols[0], sols[1]) if check else None   

def linear_system_nxn(*equations: list[str]) -> list:
    """
    Solves an nxn system of equations
    """
    n = len(equations)
    
    preprocessed_equations = [preprocess_equation(eq) for eq in equations]

    coefficients, products = [], []
    for eq in preprocessed_equations:
        coeffs, product = parse_equation(eq, n)
        coefficients.append(coeffs)
        products.append(product)
    
    coMatrix = np.array(coefficients)
    productMatrix = np.array(products).reshape(n, 1)
    
    solMatrix = np.linalg.solve(coMatrix, productMatrix)
    sols = [round(float(x), 1) if round(float(x)) == float(x) else "%0.4f" % x for x in solMatrix.flatten()]
    check = np.allclose(np.dot(coMatrix, solMatrix), productMatrix)
    
    if check:
        return {f"x{i+1}": sol for i, sol in enumerate(sols)}
    else:
        return None
    
def inequality(eq):
    #2x > 10
    pass


"""
END OF ALGEBRA
"""



