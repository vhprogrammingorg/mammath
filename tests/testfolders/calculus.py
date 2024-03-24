from sympy import *
from sympy.abc import x

def derivative(f_of, solvefor):
    return diff(f_of, solvefor)
def secondDerivative(f_of, solvefor):
    return diff(f_of, solvefor, solvefor)
def indefIntegral(f_of, solvefor):
    integral = str(integrate(f_of, solvefor)) + " + C"
    return integral

def defIntegral(f_of, solvefor, lowerbound, upperbound):
    return integrate((f_of), (solvefor, lowerbound, upperbound))
    
def Limit(f_of, solvefor, to):
    return limit(f_of, solvefor, to)
