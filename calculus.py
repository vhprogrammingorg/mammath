import numpy as np
import math
from operations import *

"""
CALCULUS
"""
exp = lambda x: e ** x

def derivative_at(f_of, x):
    """
    Returns the derivative of any function at a point x
    """
    h = 0.00001
    return round(1 / (12 * h) * (f_of(x - 2 * h) - 8 * f_of(x - h) + 8 * f_of(x + h) - f_of(x + 2 * h)), 7)
    #1/12h * f(x-2 *h) - 8*f(x-h) + 8*f(x+h) - f(x+2*h)

def derivative(f_of, solvefor):
    """
    Returns the symbolic derivative of any function
    """
    pass
    
def def_integral(f, lowerbound, upperbound, n = 10000):
    """
    Returns the definite integral of any function with the lower and upper bounds specified
    """
    stepLen = (upperbound - lowerbound) / n
    lb = lowerbound
    xRange = np.arange(lb, upperbound, stepLen)
    total = f(lowerbound) + f(upperbound)
    for i in range(1, n):
        total += 2*f(xRange[i])
    integralVal = total * stepLen / 2
    return round(integralVal, 5)

def indef_integral(f_of, solvefor):
    """
    Returns the symbolic integral of any function
    """
    pass

def gamma(x):
    gammaF = lambda t: t**(x) * math.exp(-t)
    return def_integral(gammaF, 0.001, 1000)

"""
END OF CALCULUS
"""
