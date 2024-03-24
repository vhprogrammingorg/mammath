import mpmath as mp
from sequences import *
import math
from tkinter.messagebox import *
import sys

def isInfinite(x):
    return mp.isinf(x)
def isFinite(x):
    return mp.isfinite(x)
def isInt(x, gaussian = False): 
    return mp.isint(x, gaussian)

def Zeta(s):
    mp.pretty = True
    return mp.zeta(s)
def percentageChange(a, b):
    if a == b:
        return 100.0
    try:
        return round(((b - a)/a)*100, 3)
    except ZeroDivisionError:
        return float("inf")
def percentage(a, b, integer = False):
    percent = a / b * 100
    if integer:
        return int(percent)
    return percent

def average(*argv):
    total = np.sum(list(argv))
    length = len(argv)
    return total / length
def consecutiveIntCalc(x):
    a = (x/3)-1
    b = x/3
    c = (x/3)+1
    return [a, b, c]

def ascendingSort(*args):
    argList = list(args)
    argList.sort()
    return argList
def descendingSort(*args):
    argList = list(args)
    argList.sort(reverse=True)
    return argList

def ascendingPowers(a, *args):
    args = list(args)
    i = '0'
    eq = ''
    while int(i) < len(args):
        eq += str(args[int(i)]) + '*(n^' + str(i) + ') +'
        i = int(i)
        i += 1
        i = str(i)
    eq += '0'
    return nthFinder(eq, a)
def ascendingPowersRange(a, b, *args):
    args = list(args)
    i = '0'
    eq = ''
    while int(i) < len(args):
        eq += str(args[int(i)]) + '*(n^' + str(i) + ') +'
        i = int(i)
        i += 1
        i = str(i)
    eq += '0'  
    return nthRange(eq, a, b)
def ascendingpowersTable(a, b, *args):
    args = list(args)
    i = '0'
    eq = ''
    while int(i) < len(args):
        eq += str(args[int(i)]) + '*(n^' + str(i) + ') +'
        i = int(i)
        i += 1
        i = str(i)
    eq += '0'  
    return nthTable(eq, a, b)
    
def HCF(a, b):
    a, b = max(a, b), min(a, b)
    while b!=0:
        a, b = b, a % b
    return a
def LCM(a, b):
    return (a*b)/HCF(a, b)
def primeFactors(n):
    while n % 2 == 0:
            print(2)
            n = n / 2  
    for i in range(3,int(math.sqrt(n))+1,2):
            while n % i== 0:
                    print(i)
                    n = n / i
    if n > 2:
            print(n)
    
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
def recLimit(a):
    messagebox.askyesno("RECURSION SETTINGS", "Setting your recursion limit may slow your laptop or cause a crash. Proceed with caution. Do You wish to continue?")
