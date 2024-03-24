from fractions import Fraction

def addFraction(a, b, simplified = True):
    ans = (Fraction(a) + Fraction(b))
    return str(ans.limit_denominator()) if simplified else ans
def subtractFraction(a, b, simplified = True):
    ans = (Fraction(a) - Fraction(b))
    return str(ans.limit_denominator()) if simplified else ans
def multiplyFraction(a, b, simplified = True):
    ans = (Fraction(a) * Fraction(b))
    return str(ans.limit_denominator()) if simplified else ans
def divideFraction(a, b, simplified = True):
    ans = (Fraction(a) / Fraction(b))
    return str(ans.limit_denominator()) if simplified else ans
def simplifyFraction(a):
    return str(Fraction(a).limit_denominator())

 
