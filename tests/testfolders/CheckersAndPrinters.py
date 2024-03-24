import math

def primeCheck(num):
    x = False
    for i in range(2, num):
        if num % i == 0:
            x = True
    if x:
        return False
    return True
def primeNumberPrinter(low, high, list = False):
    thing = []
    for i in range(low, high+1):
        if primeCheck(i) and not list:
            print(i)
        elif primeCheck(i) and list:
            thing.append(i)
    if list and thing:
        return thing
            
def perfectSquareCheck(num):
    root = math.sqrt(num)

    if math.trunc(root)-root==0:
        return True
    
    return False
def perfectSquarePrinter(low, high, list = False):
    thing = []
    for i in range(low, high+1):
        if perfectSquareCheck(i) and not list:
            print(i)
        elif perfectSquareCheck(i) and list:
            thing.append(i)
    if list and thing:
        return thing
    
def perfectRootCheck(a, b):
    x = root(a, b)
    if x % 1 == 0:
        return True
    return False
def triangularCheck(n):
    for i in range(n):
        if i*(i+1)/2 == n:
            return True
    return False
def triangularPrinter(low, high, list = False):
    thing = []
    for i in range(low, high+1):
        if triangularCheck(i) and not list:
            print(i)
        elif triangularCheck(i) and list:
            thing.append(i)
    if list and thing:
        return thing
    
def pentagonalCheck(n):
    i = 1
    while True:
        p = (3 * i * i - i) / 2
        i += 1
        if p >= n:
            break
    return p == n

def pentagonalPrinter(low, high, list = False):
    thing = []
    for i in range(low, high+1):
        if pentagonalCheck(i) and not list:
            print(i)
        elif pentagonalCheck(i) and list:
            thing.append(i)
    if list and thing:
        return thing
    
def fibonacciTerm(n):
    x = (((((1+math.sqrt(5))/2)**n)-((((1-math.sqrt(5))/2)**n))))/math.sqrt(5)
    return round(x)

def fibonacciCheck(n):
    return perfectSquareCheck(5*n*n + 4) or perfectSquareCheck(5*n*n - 4)

def fibonacciPrinter(low, high, list = False):
    thing = []
    for i in range(low, high+1):
        if fibonacciCheck(i) and not list:
            print(i)
        elif fibonacciCheck(i) and list:
            thing.append(i)
    if list and thing:
        return thing
