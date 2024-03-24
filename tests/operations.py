import math
from sequences import *

def add(*args):
    return sum(args)
def subtract(a, *args):
    return a - sum(args)
def multiply(*args):
    x = 1
    y = 0
    while y < len(args):
        x = x*args[y]
        y+=1
    return x
def divide(a, *args):
    return a / listMultiply(args)
def listMultiply(List):
    x = 1
    y = 0
    while y < len(List):
        x = x*List[y]
        y+=1
    return x
def power(a, *args):    
    b = mult(args)
    x = a**(b)
    if b < 1:
        return root(a, 1/b)
    else:
        return x
def sqrt(a):
    return math.sqrt(a)
def root(a, b):    
    x = a**(1/b)
    try:
        y = round(x)
        if y-x <= 0.000000000000001:
            if x**(b) != a:
                if b % 2 == 0 and a < 0:
                    z = str(abs(y)) + 'i'
                    print(z)
                else:
                    return y
            else:
                 if b % 2 == 0 and a < 0:
                    z = str(abs(y)) + 'i'
                    print(z)
                 else:
                    return x
        elif y-x >= -0.000000000000001:
            if x**(b) != a and y-x<0:
                 if b % 2 == 0 and a < 0:
                    z = str(abs(y)) + 'i'
                    print(z)
                 else:
                    return y
            else:
                 if b % 2 == 0 and a < 0:
                    z = str(abs(y)) + 'i'
                    print(z)
                 else:
                    return x
        else:
             if b % 2 == 0 and a < 0:
                z = str(abs(y)) + 'i'
                print(z)
             else:
                return x
    except:
        c = b/2
        t = cmath.sqrt(a)
        while c > 2:
             t = cmath.sqrt(t)
             c -= 1
        return t
    
def log(a, b):
    return math.log(a, b)
def sf(a, b):
    rounded = round(a, b - int(math.floor(math.log10(abs(a)))) - 1)
    return rounded
def absVal(a):
    return math.fabs(a)
def remainder(a, b):
    return math.remainder(a, b)
def factorial(a):
    x = 1
    while a > 0:
        x *=a
        a -=1
    return x
def gamma(a):
    return math.gamma(a)
def lgamma(a):
    return math.lgamma(a)

def summate(n, a, b):
    return sum(nthRange(n, a, b))
def product(n, a, b):
    return listMultiply(nthRange(n, a, b))
