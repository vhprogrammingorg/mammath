from sympy import *
from sympy.abc import *
import numpy as np

def quadraticSolver(a,b,c):
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))
    if dis > 0:
            print(" real and different roots ")
            print((-b + sqrt_val)/(2 * a))
            print((-b - sqrt_val)/(2 * a))
    elif dis == 0:
            print(" real and same roots")
            print(-b / (2 * a))
    else:
            print("Complex Roots")
            print(- b / (2 * a), " + i", sqrt_val)
            print(- b / (2 * a), " - i", sqrt_val)

def simplifyEquation(equation):
    simplified = simplify(equation)
    return simplified
def expandEquation(equation):
    expanded = expand(equation)
    return expanded
def factoriseEquation(equation):
    factorised = factor(equation)
    return factorised
def trigSimplify(trigEquation):
    simplified = trigsimp(trigEquation)
    return simplified
def trigExpand(trigEquation):
    expanded = expand_trig(trigEquation)
    return expanded
def powerSimplifier(equation):
    simplified = powsimp(equation, force=True)   
    return simplified
def nestedPowerSimplifier(equation):
    simplified = powdenest(equation, force=True)
    return simplified 
