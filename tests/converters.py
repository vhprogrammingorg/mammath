import math
from fractions import Fraction

def toDegrees(a):
    return math.degrees(a)
def toRadians(a):
    return math.radians(a)

def PercentagetoDecimal(percentage):
    return p / 100
def PerToFrac(p):
    dec = p / 100
    fraction = Fraction(dec)
    return str(fraction)
def PercentagetoFraction(percentage):
    fracOutput = PertoFrac(p)
    return "{0}".format(fracOutput)
def FractiontoDecimal(fraction):
    dec = f
    return str(round(dec, 5))
def FractiontoPercentage(fraction):
    return f * 100
def DecimaltoPercentage(decimal):
    percentage = "{:.0%}".format(d)
    return str(percentage)
def DecimaltoFraction(decimal):
    return str(Fraction(d).limit_denominator())
