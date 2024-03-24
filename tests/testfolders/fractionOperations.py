from fractions import Fraction

def addFraction(a, b):
    ans = Fraction(a) + Fraction(b)
    return str(ans)
def subtractFraction(a, b):
    ans = Fraction(a) - Fraction(b)
    return str(ans)
def multiplyFraction(a, b):
    ans = Fraction(a) * Fraction(b)
    return str(ans)
def divideFraction(a, b):
    ans = Fraction(a) / Fraction(b)
    return str(ans)
def simplifyFraction(a):
    return str(Fraction(a).limit_denominator())

 