from sympy import *
from sympy.abc import x, y, z
import tkinter
from tkinter import *
from tabulate import tabulate
import string
from fractions import Fraction
from tkinter import messagebox
import numpy as np
import math
import cmath
import random
import time
import sys
import keyboard
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import inspect
import re
import mpmath


"""
SHUNTING YARD ALGORITHM
A safe replacement for eval
"""

operatorsDict = {"*": 2, "/": 2, "+": 1, "%": 2, '': 4, "-": 1, "^": 3, "**": 3}
operators = operatorsDict.keys()

def tokenize(inputExpression):
    return re.split("([()" + ''.join(operators) + "])", inputExpression.replace(" ", ""))

def shunting_yard(inputExpression):
    queue = []
    stack = []

    tokens = tokenize(inputExpression)
    tokens = [x for x in tokens if x]
    for token in tokens:
        if(token not in operators and token != "(" and token != ")"):
            queue.append(token)

        if(token == "("):
            stack.append(token)
       
        if(token == ")"):
            while(len(stack) != 0 and stack[-1] != "("):
                queue.append(stack.pop())
     
            stack.pop()
       
        if(token in operators):
            while(len(stack) != 0 and stack[-1] in operators and operatorsDict[stack[-1]] >= operatorsDict[token]):
                queue.append(stack.pop())

            stack.append(token)

    while(len(stack) != 0):
        queue.append(stack.pop())

    return queue

def evaluatePostfix(inputList):
    stack = []
    
    for token in inputList:
        if(token not in operators):
            stack.append(token)
        else:
            operand2 = float(stack.pop())
            operand1 = float(stack.pop())
            if(token == "+"):
                stack.append(operand1 + operand2)

            if(token == "-"):
                stack.append(operand1 - operand2)

            if(token == "*"):
                stack.append(operand1 * operand2)

            if(token == "/"):
                stack.append(operand1 / operand2)

            if(token == '^'):
                stack.append(operand1 ** operand2)
               
    return stack[0]

def evaluateExpression(inputExpression):
    return evaluatePostfix(shunting_yard(inputExpression))

"""
END OF SHUNTING YARD
"""



"""
MATH TEACHERS
"""

def teach_me_trig():
    print("Welcome to the trigonometry basics course!")
    time.sleep(0.5)
    print("One of the most fundamental formulas in trigonometry is the Pythagorean theorem - a^2 + b^2 = c^2, which allows you to find missing sides in a right angled triangle.")
    time.sleep(2)
    print("it works on all right angled triangles")
    time.sleep(1)
    print("Then, to calculate sides given an angle and one other side, SOHCAHTOA will help you remember the ratios:")
    time.sleep(0.5)
    print("sin = opposite/hypotenuse")
    time.sleep(1)
    print("cos = adjacent/hypotenuse")
    time.sleep(1)
    print("and tan = opposite/adjacent")
    time.sleep(1)
    ans = input("If one side of a triangle is 3 and another is 4, what is the hypotenuse? ")
    chances = 2
    while ans.lower().replace(" ", "") not in ["hypotenuse=5", "hyp=5", "5", "five"] and chances > 0:
        print("That is not correct. Please refer to the pythagorean theorem!")
        ans = input("If one side of a triangle is 3 and another is 4, what is the hypotenuse? ")
        chances = chances - 1
    if ans in ["hypotenuse=5", "hyp=5", "5", "five"]:
        print("Great job! This is also a special case for right angled triangles and is known as a Pythagorean triplet.")
    else:
        print("The answer was 5. We needed to use the Pythagorean theorem which states that a^2 + b^2 = c^2, therefore, 3^2 + 4^2 = c^2, and c = 5")
    print("Wikipedia, mathisfun, and other websites can help too")
    print("Thank you!")
    
def teach_me_algebra():
    print("Welcome to the algebra basics course!")
    time.sleep(0.5)
    print("In this basic algebra course, you will learn the basics of solving equations and working with variables.")
    time.sleep(2)
    print("In order to solve one step equations, we will try to isolate all of the varaibles. This means that we want all instances of a variable on one side, and all regular numbers on another.")
    time.sleep(3)
    print("You will often be given an equation where you will have a few operations taking place on either side of the equation. If an 'x' variable is on a side with other numbers, we will perform the opposite operation that eliminates it from that side that it is on.")
    time.sleep(3)
    print("For instance, if we have x+3 = 5, we notice that we have a 3 on the same side as the x. In order to solve for x, we notice that we are adding a three, therefore, we will subtract a three to eliminate it from the x side. However, we need to remember to do the same thing on the other side of the equation. Therefore, the right side becomes 5 -3 = 2. x = 2.")
    time.sleep(3)
    print("In general, a + on one side becomes a - to eliminate it, a * becomes a /, a ^ becomes a root. ")
    time.sleep(1)
    ans = input("3x+5=8, what is x? ")
    chances = 2
    while ans.lower().replace(" ", "") not in ["x=1", "1", "one"] and chances > 0:
        if chances == 2:
            print("That is not correct. Notice that the 3x means 3*x.")
        elif chances == 1:
            print("That is not correct. First, subtract the 5 on both sides. As we have 3*x. We will need to divide both sides by three to solve for x.")
        ans = input("3x+5=8, what is x? ")
        chances = chances - 1
    if ans in ["x=1", "1", "one"]:
        print("Great job!")
    else:
        print("The answer was 1")
        
    print("Wikipedia, mathisfun, and other websites can help too")
    print("Thank you!")
    
def teach_me_derivitives():
    print("welcome to the derivitives basics course!")
    time.sleep(0.5)
    print("a you solve basic derivitives by using a set of rules")
    time.sleep(0.5)
    print("use this link")
    time.sleep(1)
    print("https://www.mathsisfun.com/calculus/derivatives-rules.html")
    print("press enter when you are done")
    while True:
        if keyboard.is_pressed("enter"):
            break
        else:
            pass
    ans = input("what is the derivitive of 1/3x^3? ")
    chances = 2
    while ans not in ["X**2", "x^2", "X^2", "x**2"] and chances > 0:
        print("not correct")
        ans = input("what is the derivitive of 1/3x^3? ")
        chances = chances - 1
    if ans in ["X**2", "x^2", "X^2", "x**2"]:
        print("great job!")
    else:
        print("the answer was x^2")
    print("wikipedia, mathisfun, and other websites can help too")
    print("thank you!")
def teach_me_integrals():
    print("this is a course on basic integrals")
    print("make sure you know derivitives first")
    print("press control C to cancel this course and type teach_me_derivitives() to begin that course")
    time.sleep(2)
    print("integration involves you finding the function for which the derivitive is the function you are integrating (the antidreavative)")
    time.sleep(1)
    print("use the rules from https://www.mathsisfun.com/calculus/integration-rules.html to learn them")
    print("to find the definite integral of a function, you must take the function of the upper bound minus the function of the lower bound")
    print("press enter to continue")
    while True:
        if keyboard.is_pressed("enter"):
            break
        else:
            pass
    time.sleep(1)
    ans = input("what is the integral of x^2? ")
    chances = 2
    while ans not in [9] and chances > 0:
        print("not correct")
        ans = input("what is the integral of x^2? ")
        chances = chances - 1
    if ans in [9]:
        print("great job!")
    else:
        print("the answer was 9")
    print("wikipedia, mathisfun, and other websites can help too")
    print("thank you!")
def teach_me_adalgebra():
    print("welcome to advanced algebra!")
    print("make sure you know basic algebra first")
    print("press control C to cancel this course and type teach_me_algebra() to begin that course")
    time.sleep(1)
    print("let us start with simeltaneous equations")
    print("simultaneous equations involve 2 equations and 2 variables")
    time.sleep(1)
    print("you solve by substituting an equation of x into y in the other one")
    time.sleep(2)
    ans = input("If x + 2y = 14 and 2x + 2= y, find x and y").lower()
    chances = 2
    while ans not in ["x=2, y=6", "x = 2, y=6", "x=2, y = 6", "x = 2, y = 6", "y=6, x=2", "y = 6, x=2", "y=6, x = 2", "y = 6, x = 2", "2, 6", "6, 2"] and chances > 0:
        print("not correct")
        ans = input("If x + 2y = 14 and 2x + 2= y, find x and y").lower()
        chances = chances - 1
    if ans in ["x=2, y=6", "x = 2, y=6", "x=2, y = 6", "x = 2, y = 6", "y=6, x=2", "y = 6, x=2", "y=6, x = 2", "y = 6, x = 2", "2, 6", "6, 2"]:
        print("great job!")
    else:
        print("the answer was x = 2, y = 6")
    print("wikipedia, mathisfun, and other websites can help too")
    print("Now for quadratics")
    print("quadratics are always ax^2 + bx + c = 0")
    print("they have two answers and you use a formula to solve them")
    print("the formula is:")
    print("(-b+_ sqrt(4ac))/2a")
    ans = input("If x^2 - 3x + 2 = 0, find x").lower()
    chances = 2
    while ans not in ["x=1, x=2", "x=2, x=1", "x = 1, x = 2", "x = 2, x = 1", "1 and 2", "1, 2"] and chances > 0:
        print("not correct")
        ans = input("If x^2 - 3x + 2 = 0, find x").lower()
        chances = chances - 1
    if ans in ["x=1, x=2", "x=2, x=1", "x = 1, x = 2", "x = 2, x = 1"]:
        print("great job!")
    else:
        print("the answers were 1 and 2")
def teach_me_adtrig():
    print("welcome to advanced trig!")
    print("make sure you know basic trig first")
    print("press control C to cancel this course and type teach_me_trig() to begin that course")
    time.sleep(1)
    print("let us start with trig identities")
    print("trig identities are relationships between trigonometric functions")
    print("before we learn the identities, we must learn the other three trigonometric functions:")
    time.sleep(1)
    print("csc = hyp/opp")
    time.sleep(1)
    print("sec = hyp/adj")
    time.sleep(1)
    print("cot = adj/opp")
    time.sleep(2)
    print("https://www.mathsisfun.com/algebra/trigonometric-identities.html")
    print("press enter when you are done")
    while True:
        if keyboard.is_pressed("enter"):
            break
        else:
            pass
    print("complete the equation:")
    ans = int(input("sin^2 θ + cos^2 θ = "))
    chances = 2
    while ans not in [1] and chances > 0:
        print("not correct")
        print("complete the equation:")
        ans = int(input("sin^2 θ + cos^2 θ = "))
        chances = chances - 1
    if ans in [1]:
        print("great job!")
    else:
        print("the answer was 1")
def teach():
    print("welcome to random teach (basic)! we will choose a random concept to teach you!")
    rnum = random.randint(1, 4)
    if rnum == 1:
        print("We found derivitives!")
        teach_me_derivitives()
    elif rnum == 2:
        print("We found trig!")
        teach_me_trig()
    else:
        print("We found algebra!")
        teach_me_algebra()
def adteach():
    print("welcome to random teach (advanced)! we will choose a random concept to teach you!")
    rnum = random.randint(1, 3)
    if rnum == 1:
        print("We found integrals!")
        teach_me_integrals()
    elif rnum == 2:
        print("We found trig (advanced)!")
        teach_me_adtrig()
    else:
        print("We found algebra (advanced)!")
        teach_me_adalgebra()

val = ""
def ShowCalculator():
    global bt
    global do_it
    global tk
    global clear
    tk = Tk()
    global data
    data= StringVar()
    lbl=Label(
        tk,
        text="Label",
        anchor=SE,
        font=("Verdana",20),
        textvariable=data,
        background="#ffffff",
        fg="#000000",
    )
    lbl.grid(row = 0, column = 0)
    btn1 = Button(tk, text="1", command= lambda: bt("1"))
    btn1.grid(row = 1, column = 0, sticky = W)
    btn2 = Button(tk, text="2", command= lambda: bt("2"))
    btn2.grid(row = 1, column = 1, sticky = W)
    btn3 = Button(tk, text="3", command= lambda: bt("3"))
    btn3.grid(row = 1, column = 2, sticky = W)
    plus = Button(tk, text="+", command= lambda: bt("+"))
    plus.grid(row = 1, column = 3, sticky = W)
    btn4 = Button(tk, text="4", command= lambda: bt("4"))
    btn4.grid(row = 2, column = 0, sticky = W)
    btn5 = Button(tk, text="5", command= lambda: bt("5"))
    btn5.grid(row = 2, column = 1, sticky = W)
    btn6 = Button(tk, text="6", command= lambda: bt("6"))
    btn6.grid(row = 2, column = 2, sticky = W)
    minus = Button(tk, text="-", command= lambda: bt("-"))
    minus.grid(row = 2, column = 3, sticky = W)
    btn7 = Button(tk, text="7", command= lambda: bt("7"))
    btn7.grid(row = 3, column = 0, sticky = W)
    btn8 = Button(tk, text="8", command= lambda: bt("8"))
    btn8.grid(row = 3, column = 1, sticky = W)
    btn9 = Button(tk, text="9", command= lambda: bt("9"))
    btn9.grid(row = 3, column = 2, sticky = W)
    times = Button(tk, text="*", command= lambda: bt("*"))
    times.grid(row = 3, column = 3, sticky = W)
    btn0 = Button(tk, text="0", command= lambda: bt("0"))
    btn0.grid(row = 4, column = 0, sticky = W)
    dot = Button(tk, text=".", command= lambda: bt("."))
    dot.grid(row = 4, column = 1, sticky = W)
    divide = Button(tk, text="/", command= lambda: bt("/"))
    divide.grid(row = 4, column = 2, sticky = W)
    clr = Button(tk, text="C", command= lambda: clear())
    clr.grid(row = 4, column = 3, sticky = W)
    eq = Button(tk, text="=", command= lambda: do_it())
    eq.grid(row = 5, column = 0, sticky = W)
def HideCalculator():
    tk.destroy()
def bt(x):
    global val
    val = val + x
    data.set(val)
def do_it():
    global val
    y = evaluateExpression(val)
    data.set(y)
    ans = val
    val=""
def clear():
    global val
    val =""
    data.set(val)
    

"""
END OF MATH TEACHERS
"""


def recLimit(a):
    messagebox.askyesno("RECURSION SETTINGS", "Setting your recursion limit may slow your laptop or cause a crash. Proceed with caution. Do You wish to continue?")

    
"""
OPERATIONS
"""

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

#Multiplies all of the elements in a list
def listMultiply(lis):
    x = 1
    y = 0
    while y < len(List):
        x = x*List[y]
        y+=1
    return x

def power(base, exponent):
    if exponent == 0:
        return 1
    if exponent > 0:
        return (base * power(base, exponent - 1))
    return 1 /(base * power(base, -exponent - 1))

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

def factorial(a):
    x = 1
    while a > 0:
        x *=a
        a -=1
    return x

def log(num, base):
    return math.log(num, base)

def ln(a):
    return log(a, math.e)

def sigFig(a, b):
    rounded = round(a, b - int(math.floor(math.log10(abs(a)))) - 1)
    return rounded
def absVal(a):
    return math.fabs(a)
def remainder(a, b):
    return math.remainder(a, b)

def HCF(a, b):
    a, b = max(a, b), min(a, b)
    while b!=0:
        a, b = b, a % b
    return a
def LCM(a, b):
    return (a*b)/HCF(a, b)

"""
END OF OPERATIONS
"""



"""
PRIME NUMBERS
"""

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

def checkPrime(num):
    x = False
    for i in range(2, num):
        if num % i == 0:
            x = True
    if x:
        return False
    return True

def primeNumberPrinter(low, high):
    for num in range(low, high+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num)
"""
END OF PRIME NUMBERS
"""


"""
NUMBER/SEQUENCE CHECKS
"""

def perfectSquare(num):
    root = math.sqrt(num)

    if math.trunc(root)-root==0:
        return True
    return False

def perfectSquareCheck(num):
    if perfectSquare(num) == True:
        return True
    return False

def perfectSquarePrinter(low, high):
    for i in range(low, high):
        if perfectSquare(i) == True:
            print(i)
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
def triangularPrinter(low, high):
    for i in range(low, high):
        if triangularCheck(i) == True:
            print(i)
def pentagonalCheck(n):
    i = 1
    while True:
        p = (3 * i * i - i) / 2
        i += 1
        if p >= n:
            break
    return p == n

def pentagonalPrinter(low, high):
    for i in range(low, high):
        if pentagonalCheck(i) == True:
            print(i)

"""
END OF NUMBER/SEQUENCE CHECKS
"""



"""
FIBONACCI
"""

def fibonacciBinet(n):
    x = (((((1+math.sqrt(5))/2)**n)-((((1-math.sqrt(5))/2)**n))))/math.sqrt(5)
    return round(x)
def fibonacci(n):
    n0, n = n, abs(n)
    F = {}
    
    qinx = []  
    qinx.append(n)
    F[n] = -1
    while qinx:
        k = qinx.pop() >> 1
        if k not in F:
            F[k] = -1
            qinx.append(k)
        if (k + 1) not in F:
            F[k+1] = -1
            qinx.append(k + 1)
    
    F[0], F[1], F[2] = 0, 1, 1
    keys_sorted = sorted(F.keys())
    for k in keys_sorted[3:]:
        k2 = k >> 1
        f1, f2 = F[k2], F[k2 + 1]
        if k % 2 == 0:
            F[k] = 2 * f2 * f1 - f1 * f1
        else:
            F[k] = f2 * f2 + f1 * f1
    
    r = F[n]
    if n0 < 0:
        return negativeFib(n, r)
    return r

def fibonacciCheck(n):
    return perfectSquareCheck(5*n*n + 4) or perfectSquareCheck(5*n*n - 4)
def fibonacciPrinter(low, high):
    for i in range(low, high+1):
        if fibonacciCheck(i) == True:
            print(i)

"""
END OF FIBONACCI
"""



"""
DIVISIBILITY CHECKS
"""

def div2Check(num):
    if num % 2 == 0:
        return True
    else:
        return False
def div3Check(num):
    if num % 3 == 0:
        return True
    else:
        return False
def div4Check(num):
    if num % 4 == 0:
        return True
    else:
        return False
def div5Check(num):
    if num % 5 == 0:
        return True
    else:
        return False
def div6Check(num):
    if num % 6 == 0:
        return True
    else:
        return False
def div7Check(num):
    if num % 7 == 0:
        return True
    else:
        return False
def div8Check(num):
    if num % 8 == 0:
        return True
    else:
        return False
def div9Check(num):
    if num % 9 == 0:
        return True
    else:
        return False
def divCheck(num, num2):
    if num % num2 == 0:
        return True
    else:
        return False

"""
END OF DIVISIBILITY CHECKS
"""

    
def summate(n, a, b):
    return sum(nthRange(n, a, b))
def product(n, a, b):
    return listMultiply(nthRange(n, a, b))

def timesTables(n):
    for i in range(1, n+1):
        for j in range(i, (n*i)+i, i):
            print(str(j) + " ", end="")
        print("")

def CoefficientsQuadratic(string):
    string = "".join(" " if i == "x" or i == "+" else i for i in string)
    string = string.replace("^2", " ")
    return list(map(int, string.split()))



"""
FRACTIONS
"""

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

def PercentagetoDecimal(percentage):
    return percentage / 100
def PerToFrac(p):
    dec = p / 100
    fraction = Fraction(dec)
    return str(fraction)
def PercentagetoFraction(percentage):
    fracOutput = PerToFrac(percentage)
    return "{0}".format(fracOutput)
def FractiontoDecimal(fraction):
    dec = f
    return str(round(dec, 5))
def FractiontoPercentage(fraction):
    return f * 100
def DecimaltoPercentage(decimal):
    percentage = "{:.0%}".format(decimal)
    return str(percentage)
def DecimaltoFraction(decimal):
    return str(Fraction(decimal).limit_denominator())

"""
END OF FRACTIONS
"""



"""
GEOMETRY
"""

def validTriangle(s1, s2, s3):
    if s1 + s2 >= s3 and s2 + s3 >= s1 and s1 + s3 >= s2:
        return True
    return False

def triangleArea(l, w):
    return (l*w)/2
def trapeziumArea(a, b, h):
    return (a+b)/h
def paraHeight(a, b):
    return a/b
def paraArea(b, h):
    return b*h
def circleCircumference(r):
    return 2*math.pi*r
def circleArea(r):
    return math.pi*(r**2)
def sphereVolume(r):
    return 4/3*math.pi*(r**3)
def sphereArea(r):
    return 4*math.pi*(r**2)
def sphereDiametre(r):
    return 2*r
def surfaceArea(a, b, c):
    d = a*b
    e = a*c
    f = b*c
    return 2*(d+e+f)
def surfAreaPrism(farea, *args):
    total = 2*farea
    i = 0
    while i < len(args):
        total += args[i]
        i += 1
    return total
def volume(a, b, c):
    return a*b*c
def cylinderVolume(r, h):
    return (math.pi*(r**2))*h
def cylinderArea(r, h):
    return (2*math.pi*r*h)+(2*math.pi*(r**2))
def cylinderDiametre(v, h):
    return 2*(math.sqrt(v/math.pi*h))
def cylinderHeight(v, r):
    return v/(math.pi*(r**2))
def cylindeRadius(h, A):
    return round(0.5*math.sqrt(h**2 + 2*(A/math.pi))-h/2, 5)
def coneArea(r, h):
    pi = math.pi
    area = pi*r*(r + math.sqrt(h**2 + r**2))
    return round(area, 5)
def coneVolume(r, h):
    pi = math.pi
    vol = pi*r**2*(h/3)
    return round(vol, 5)
def coneRadius(h, vol):
    pi = math.pi
    rad = math.sqrt(3*(vol/(pi*h)))
    return round(rad, 5)
def coneHeight(r, vol):
    pi = math.pi
    height = 3*(vol/(pi*r**2))
    return round(height, 5)

##def sin(a):
##    return math.sin(a)
##def cos(a):
##    return math.cos(a)
##def tan(a):
##    return math.tan(a)
##def asin(a):
##    return math.asin(a)
##def acos(a):
##    return math.acos(a)
##def atan(a):
##    return math.atan(a)
##def sinh(a):
##    return math.sinh(a)
##def cosh(a):
##    return math.cosh(a)
##def tanh(a):
##    return math.tanh(a)
##def asinh(a):
##    return math.asinh(a)
##def acosh(a):
##    return math.acosh(a)
##def atanh(a):
##    return math.atanh(a)
##def sec(a):
##    return round(1/cos(a), 5)
##def csc(a):
##    return round(1/sin(a), 5)
##def cot(a):
##    return round(1/tan(a), 5)
def gamma(a):
    return math.gamma(a)
def lgamma(a):
    return math.lgamma(a)

def toDegrees(a):
    return math.degrees(a)
def toRadians(a):
    return math.radians(a)

def pytheoromside(a, b):
    if a > c:
        a1 = a*a
        b1 = b*b
        c1 = a1 - b1
        c = math.sqrt(c1)
    else:
        a1 = a*a
        b1 = b*b
        c1 = b1 - a1
        c = math.sqrt(c1)
    return c
def pyTheoremAB(a, b):
    a1 = a*a
    b1 = b*b
    c1 = a1 + b1
    c = math.sqrt(c1)
    return c
def pyTheoremCA(c, a):
    c1 = c*c
    a1 = a*a
    b1 = c1 - a1
    b = math.sqrt(b1)
    return b
def pyTheoremCB(c, b):
    c1 = c*c
    b1 = a*a
    a1 = c1 - b1
    a = math.sqrt(a1)
    return a
def cos_rule(c, b, A):
    c1 *= c
    b1 *= b
    a1 = math.cos(A)
    thing = a1*c*b
    ans = b1 + a1 - thing
    answer = math.sqrt(answer)
    return answer
def areabytan(n, s):
    s1 = s*s
    up = n*s1
    intan = 180/n
    tanpart = math.tan(intan)
    down = 4*tanpart
    ans = up/down
    return ans
def pythagoreanTriplets(n):
  for b in range(n):
    for a in range(1, b):
        c = math.sqrt(a * a + b * b)
        if c % 1 == 0:
            print(a, b, int(c))
def pythagoreanTripletsCheck(a, b, c):
    return True if a * a + b * b == c * c else False

"""
END OF OF GEOMETRY
"""

def quadraticSolver(a,b,c):
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))
    if dis > 0:
        print((-b + sqrt_val)/(2 * a))
        print((-b - sqrt_val)/(2 * a))
    elif dis == 0:
        print(-b / (2 * a))
    else:
        print("Complex Roots")
        print(- b / (2 * a), " + i", sqrt_val)
        print(- b / (2 * a), " - i", sqrt_val)

"""
SEQUENCES
"""

def sequenceChecker(a, b, c):
    while True:
        if b - a == c - b:
            print("Arithmetic")
            break
        if b / a == c / b or a / b == b / c:
            print("Geometric")
            break
        else:
            print("Quadratic")
            break

def nthFinder(a, b):
    a = str(a)
    b = str(b)
    x = a.replace("n", b)
    y = eval(x)
    return y

def nthRange(a, b, c):
    ls = []
    a = str(a)
    b = str(b)
    c = str(c)
    if int(b) > int(c):
        while int(c) < int(b)+1:
            x = a.replace("n", c)
            y = int(evaluateExpression(x))
            ls.append(y)
            c = int(c)
            c=int(c)+1
            c = str(c)
    elif int(c) > int(b):
        while int(b) < int(c)+1:
            x = a.replace("n", b)
            y = int(evaluateExpression(x))
            ls.append(y)
            b = int(b)
            b=int(b)+1
            b = str(b)
    return list(ls)
def nthTable(a, b, c):
    ls = []
    a = str(a)
    b = str(b)
    c = str(c)
    if int(b) > int(c):
        while int(c) < int(b)+1:
            x = a.replace("n", c)
            y = evaluateExpression(x)
            q = [c, y]
            ls.append(q)
            ls.append(q)
            c = int(c)
            c=int(c)+1
            c = str(c)
    elif int(c) > int(b):
        while int(b) < int(c)+1:
            x = a.replace("n", b)
            y = evaluateExpression(x)
            q = [b, y]
            ls.append(q)
            b = int(b)
            b=int(b)+1
            b = str(b)
    headers = ["term", "value"]
    thing = tabulate(ls, headers = headers)
    print(thing)

def arithemeticSequence(term1, term2, term = 1):
    dif = term2 - term1
    before = term1 - dif
    newTerm = dif*term+before
    if before == 0:
        print("Nth Term:", str(dif) + "n")
        print(str(term) + "th term:", str(newTerm))
        
    else:
        if before < 0:
            print("Nth Term:", str(dif) + "n" + str(before))
            print(str(term) + "th term:", str(newTerm)) 
        else:
            print("Nth Term:", str(dif) + "n" + " + " + str(before))
            print(str(term) + "th term:", str(newTerm))

def removeDecimal(num):
        if(num == int(num)):
            return int(num)
        return num
    
def Nth_Term_Quadratic(*series):
    
    r1d1 = series[1] - series[0]
    r1d2 = series[2] - series[1] 
    d2 = r1d2 - r1d1 
    a = d2/2
    b = r1d1 - 3 * a
    c = series[0] - (a + b)
    
    a = removeDecimal(a) 
    b = removeDecimal(b)
    c = removeDecimal(c)
    
    quadraticDict = {0: "", 1: "n^2", -1: "-n^2"}
    linearDict = {0: "", 1: "n", -1: "-n"}
    constantDict = {0: ""}

    quadraticTerm = "{}n^2".format(a) if (a != 0 and a != 1 and a != -1) else quadraticDict[a]
    linearTerm = "{}n".format(b) if (b != 0 and b != 1 and b != -1) else linearDict[b]
    constantTerm = "{}".format(c) if (c != 0) else constantDict[c]

    bSign = "+" if b > 0 else ""
    cSign = "+" if c > 0 else ""

    print(quadraticTerm + bSign + linearTerm + cSign + constantTerm)
    
"""
END OF SEQUENCES
"""




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
        eq += str(args[int(i)]) + '*(n**' + str(i) + ') +'
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
        eq += str(args[int(i)]) + '*(n**' + str(i) + ') +'
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
        eq += str(args[int(i)]) + '*(n**' + str(i) + ') +'
        i = int(i)
        i += 1
        i = str(i)
    eq += '0'  
    return nthTable(eq, a, b)



"""
FORMULAS
"""
#Force, Mass, Acceleration - F=ma
def Force(m, a):
    return m*a
def Mass(f, a):
    return f/a
def Acceleration(f, m):
    return f/m

#Speed, Distance, Time - S=d/t
def Speed(d, t):
    return d/t
def Distance(s, t):
    return s*t
def Time(s, d):
    return s*d
"""
END OF FORMULAS
"""



"""
BASE CONVERSIONS
"""

def baseConverter(x, base):
    if not isinstance(x, int):
        if x.isdigit():
            x = int(x)
        else:
            x = int("".join(map(str, [ord(i) for i in x])))
            
    digs = string.digits + string.ascii_letters
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[x % base])
        x = x // base

    if sign < 0:
        digits.append("-")

    digits.reverse()
    return "".join(digits)

def IntToBinary(num):
    return bin(num)[2:]
def BinaryToInt(num):
    return int(str(num), 2)

def IntToHexa(num):
    return hex(num)[2:]
def HexaToInt(num):
    return int(str(num, 2))

def BinaryToHex(num):
    return hex(int(str(num), 2))[2:]
def HexToBinary(num):
    return bin(int(str(num), 2))[2:]

def binaryAdd(a, b):
    sum = BinaryToInt(a) + BinaryToInt(b)
    print("Binary:", IntToBinary(sum))
    print("Base 10:", sum)
    
def binarySubtract(a, b):
    sub = BinaryToInt(a) - BinaryToInt(b)
    print("Binary:", IntToBinary(sub))
    print("Base 10:", sub)
    
def binaryMultiply(a, b):
    mult = BinaryToInt(a) * BinaryToInt(b)
    print("Binary:", IntToBinary(mult))
    print("Base 10:", mult)
    
def binaryDivide(a, b):
    div = BinaryToInt(a) / BinaryToInt(b)
    print("Binary:", IntToBinary(div))
    print("Base 10:", div)
    
def hexaAdd(a, b):
    sum = HexaToInt(a) + HexaToInt(b)
    print("Hexadecimal:", IntToHexa(sum))
    print("Base 10:", sum)
def hexaSubtract(a, b):
    sub = HexaToInt(a) - HexaToInt(b)
    print("Hexadecimal:", IntToHexa(sub))
    print("Base 10:", sub)
def hexaMultiply(a, b):
    mult = HexaToInt(a) * HexaToInt(b)
    print("Hexadecimal:", IntToHexa(mult))
    print("Base 10:", mult)
def hexaDivide(a, b):
    div = HexaToInt(a) / HexaToInt(b)
    print("Hexadecimal:", IntToHexa(div))
    print("Base 10:", div)

"""
END OF BASE CONVERSIONS
"""



def constSearch(con):
    G = 6.67384*10**(-11)
    c = 2.99792458*10**(8)
    h = 6.626070040*10**(-34)
    k = 1.38064852*10**(-23)
    F = 9.648533289*10**(4)
    pi = 3.141592653589793238462643
    e = 2.718281828459045235360287
    π = pi
    phi = 1.618033988749894848204586
    φ = phi
    conlist = [G, c, h, k, F, pi, π, φ, phi, e]
    x = 0
    while x < 10:
        variable_name = [k for k, v in locals().items() if v == conlist[x]][0]
        if variable_name == con:
            constant = conlist[x]
            return constant
        x += 1
    return None

def constTable():
    G = 6.67384*10**(-11)
    c = 2.99792458*10**(8)
    h = 6.626070040*10**(-34)
    k = 1.38064852*10**(-23)
    F = 9.648533289*10**(4)
    pi = 3.141592653589793238462643
    e = 2.718281828459045235360287
    π = pi
    phi = 1.618033988749894848204586
    φ = phi
    conlist = [["The gravitational constant", "G", G], ["The speed of light in vacuum", "c", c], ["Planck's constant", "h", h], ["Boltzmann's constant", "k", k], ["Faraday's constant", "F", F], ["e", "e", e], ["pi", "φ", π], ["Phi", "φ", φ]]
    headers = ["Name", "Symbol", "Value"]
    constants = tabulate(conlist, headers = headers)
    print(constants)
    
def trigTable():
        identities = {"Quotient Identities": ["tanθ = sinθ/cosθ", "cotθ = cosθ/sinθ"],
               "Reciprocal Identities": ["cotθ = 1/tanθ", "cscθ = 1/sinθ", "sec = 1/cosθ"],
               "Pythagorean Identities": ["sin^2θ + cos^2θ = 1", "tan^2θ + 1 = sec^2θ", "1 + cot^2θ = csc^2θ"],
               "Sum Identities": ["sin(a+b) = sin(a)cos(b)+cos(a)sin(b)", "cos(a+b) = cos(a)cos(b)-sin(a)sin(b)", "tan(a+b) = (tan(a) + tan(b))/1 - tan(a)tan(b)"],
               "Difference Identities": ["sin(a-b) = sin(a)cos(b)-cos(a)sin(b)", "cos(a-b) = cos(a)cos(b)+sin(a)sin(b)", "tan(a-b) = (tan(a)-tan(b))/1 + tan(a)tan(b)"],
               "Double-Angle Formulas": ["sin(2a) = 2sin(a)cos(a)", "cos(2a) = 2cos^2 a - 1 = 1 - 2sin^2 a", "tan(2a) = 2tan(a)/1-tan^2 a"]
               }
        print(tabulate(identities, headers = "keys"))

def sumToPalindrome(num, stepsList = False):
    isPalindrome = lambda num: num == num[::-1]
    steps = 0
    stepList = [] if stepsList else None
    while not isPalindrome(str(num)):
        num = str(num)
        num = str(int(num) + int(str(num)[::-1]))
        steps += 1
        stepList.append(num) if stepsList else None
    return "Final palindrome: " + num + ", Steps: " + str(steps) if not stepsList else "Final Palindrome: " + num + ", Steps: " + str(steps) + ", Step List: " + str([(i+1, int(j)) for i, j in enumerate(stepList)]).strip("[]")


def primeCheck(n):
    if n == 1 or not n:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    maxNum = math.floor(math.sqrt(n))
    for i in range(3, maxNum + 1, 2):
        if not n % i:
            return False
    return True
        
def prothPrimes(k):
    n = 1
    while not primeCheck((k * 2**n) + 1):
        n += 1
    return "Number: " + str((k * 2**n) + 1) + ", n: " + str(n)
    
def prothPrimesCheck(k, n):
    return primeCheck((k * 2**n) + 1)

def isPolydivisible(number):
    polydiv = False
    if number > 0:
        n = number
        length = 0
        while n > 0:
            n = int(n / 10)
            length += 1
        if n == 1:
            polydiv = True
        else:
            data = [0] * length
            i = length - 1
            num = 0
            n = number
            while n > 0:
                data[i] = n % 10
                n = int(n / 10)
                i -= 1
            num = data[0]
            i = 1
            if num:
                polydiv = True
            while i < length and polydiv:
                num = (num * 10) + data[i]
                if ((num % (i + 1)) != 0):
                    polydiv = False
                i += 1          
    return polydiv

def perfectNumberCheck(n):
    pFactors = []
    for i in range(1, n):
        if not n % i:
            pFactors.append(i)
    return sum(pFactors) == n
def perfectNumberPrinter(lower, upper, list = False):
    perfects = [i for i in range(lower, upper+1) if perfectNumberCheck(i)]
    if list:
        return perfects
    for i in perfects:
        print(i)

        

def f(fx, x, y):
    if type(eval(fx)) == np.ndarray:
        return eval(fx)

"""
GRAPHING
"""

#graph("2*x", "3*x")
def graph(*args, lrangex=-10, urangex=10, lrangey=-10, urangey=10, graph_points=100, gridset=True, scaling=True, graph_title=None, xtitle=None, ytitle=None):
    i = 0
    x = np.linspace(lrangex, urangex, graph_points)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines["left"].set_position("center")
    ax.spines["bottom"].set_position("zero")
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")
    while i < len(args):
        if type(eval(args[i])) == np.ndarray:
            y = eval(args[i])
            plt.plot(x,y, "-b", label=args)
            i+=1
    plt.title(graph_title)
    plt.xlabel(xtitle,fontsize=20)
    plt.ylabel(ytitle,fontsize=20)
    plt.autoscale(enable=scaling)
    plt.grid(gridset)
    if lrangex or urangex != False:
        plt.xlim([lrangex,urangex])
        if lrangey or urangey != False:
            plt.ylim([lrangey,urangey])
            plt.show()

    
def graph3dcontour(*args, lrangex=-10, lrangey=-10, urangex=10, urangey=10, lrangez=-10, urangez=10, graph_points=1000, lablex='x', labley='y', lablez='z', graph_title=None, cmap='binary'):
    x = np.linspace(lrangex, urangex, graph_points)
    y = np.linspace(lrangey, urangey, graph_points)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    i = 0
    while i < len(args):
        X, Y = np.meshgrid(x, y)
        Z = f(args[i], X, Y)
        ax.contour3D(X, Y, Z, 50, cmap=cmap)
        i += 1
    ax.set_xlabel(lablex)
    ax.set_ylabel(labley)
    ax.set_zlabel(lablez)
    ax.set_title(graph_title)
    if lrangez != False or urangez == False:
        ax.set_zlim(lrangez, urangez)
    if lrangex != False or urangex == False:
        ax.set_zlim(lrangex, urangex)
    if lrangey != False or urangey == False:
        ax.set_zlim(lrangey, urangey)
    return plt.show()

def linein3d(*args, lrangex=-10, lrangey=-10, lrangez = -10, urangex=10, urangey=10, urangez = 10, graph_points=1000, lablex='x', labley='y', lablez='z', graph_title=None, color='gray'):
    x = np.linspace(lrangex, urangex, graph_points)
    y = np.linspace(lrangey, urangey, graph_points)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    i = 0
    while i < len(args):
        lis = args[i]
        fz = lis[0]
        fy = lis[1]
        if type(eval(fz)) == np.ndarray:
            zline = eval(fz)
        else:
            pass
        if type(eval(fy)) == np.ndarray:
            yline = eval(fy)
        else:
            pass
        ax.plot3D(x, yline, zline, color)
        i+=1
    ax.set_xlabel(lablex)
    ax.set_ylabel(labley)
    ax.set_zlabel(lablez)
    ax.set_title(graph_title)
    if lrangez != False or urangez == False:
        ax.set_zlim(lrangez, urangez)
    if lrangex != False or urangex == False:
        ax.set_zlim(lrangex, urangex)
    if lrangey != False or urangey == False:
        ax.set_zlim(lrangey, urangey)
    return plt.show()

def graph3dwire(*args, lrangex=-10, lrangey=-10, urangex=10, urangey=10, lrangez=-10, urangez=10, graph_points=1000, lablex='x', labley='y', lablez='z', graph_title=None, edgecolor=False, color='black', fill='viridis'):
    x = np.linspace(lrangex, urangex, graph_points)
    y = np.linspace(lrangey, urangey, graph_points)
    ax = plt.axes(projection='3d')
    X, Y = np.meshgrid(x, y)
    i = 0
    while i < len(args):
        Z = f(args[i], X, Y)
        if fill==False:
            ax.plot_wireframe(X, Y, Z, color=color)
        elif edgecolor == True:
            ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                    cmap=fill, edgecolor=color)
        elif edgecolor == False:
            ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                    cmap=fill, edgecolor='none')
        else:
            raise TypeError('Parameter "edgecolor" must be a boolean operator')
        i += 1
    ax.set_xlabel(lablex)
    ax.set_ylabel(labley)
    ax.set_zlabel(lablez)   
    ax.set_title(graph_title)
    if lrangez != False or urangez == False:
        ax.set_zlim(lrangez, urangez)
    if lrangex != False or urangex == False:
        ax.set_zlim(lrangex, urangex)
    if lrangey != False or urangey == False:
        ax.set_zlim(lrangey, urangey)
    return plt.show()

"""
END OF GRAPHING
"""




def isInfinite(x):
    return mpmath.isinf(x)
def isFinite(x):
    return mpmath.isfinite(x)
def isInt(x, gaussian = False): 
    return mpmath.isint(x, gaussian)

def Zeta(s):
    return zeta(s)

"""
ALGEBRA
"""
def solveGaussElimination(*equations):              
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

def LinearSystem2x2(equation1, equation2):
    def preprocess_equation(eq):
        eq = eq.replace(" ", "")
        eq = eq.replace("+x", "+1x").replace("+y", "+1y")
        eq = eq.replace("-x", "-1x").replace("-y", "-1y")
        if eq[0] == "x" or eq[0] == "y":
            eq = "1" + eq
        return eq

    equation1, equation2 = preprocess_equation(equation1), preprocess_equation(equation2)

    def parse_equation(eq):
        eq = eq.replace("x", " ").replace("y", " ").replace("=", " ").replace("+", "").split()
        coefficients = list(map(float, eq[:2]))
        product = float(eq[2])
        return coefficients, product

    coefficients1, product1 = parse_equation(equation1)
    coefficients2, product2 = parse_equation(equation2)

    coMatrix = np.array([coefficients1, coefficients2])
    productMatrix = np.array([[product1], [product2]])

    solMatrix = np.linalg.solve(coMatrix, productMatrix)
    sols = [round(float(x), 1) if round(float(x)) == float(x) else "%0.4f" % x for x in solMatrix.flatten()]
    check = np.allclose(np.dot(coMatrix, solMatrix), productMatrix)

    return print(f"x: {sols[0]}\ny: {sols[1]}") if check else None

def LinearSystemNxN(*equations):
    n = len(equations)

    def preprocess_equation(eq):
        eq = eq.replace(" ", "")
        return eq

    preprocessed_equations = [preprocess_equation(eq) for eq in equations]

    def parse_variables(eqs):
        var_set = set()
        for eq in eqs:
            var_set.update(re.findall(r"[a-zA-Z]+", eq))
        return sorted(list(var_set))

    variables = parse_variables(preprocessed_equations)

    def parse_equation(eq, n, variables):
        coeffs = [0.0] * n
        for i, var in enumerate(variables):
            match = re.search(f"[-+]?\d*\.?\d*{var}", eq)
            if match:
                coeff = re.search("[-+]?\d*\.?\d+", match.group(0))
                if coeff:
                    coeffs[i] = float(coeff.group(0))
                else:
                    coeffs[i] = 1.0 if match.group(0)[0] == '+' else -1.0
        product = float(re.search("[-+]?\d*\.?\d*$", eq).group(0))
        return coeffs, product

    coefficients, products = [], []

    for eq in preprocessed_equations:
        coeffs, product = parse_equation(eq, n, variables)
        coefficients.append(coeffs)
        products.append(product)

    coMatrix = np.array(coefficients)
    productMatrix = np.array(products).reshape(n, 1)

    solMatrix, residuals, rank, s = np.linalg.lstsq(coMatrix, productMatrix, rcond=None)
    sols = [round(float(x), 4) for x in solMatrix.flatten()]
    check = np.allclose(np.dot(coMatrix, solMatrix), productMatrix)

    if check:
        return {var: sol for var, sol in zip(variables, sols)}
    else:
        return None
    

def discriminantQuadratic(a, b, c):
    return b**2 - 4 * a * c

def root1Quadratic(a, b, c, disc):
    return (-b + disc ** (1/2)) / (2 * a)

def root2Quadratic(a, b, c, disc):
    return (-b - disc ** (1/2)) / (2 * a)

def solve_first_degree(b, c):
    return -c / b

def secondDegreeSolver(a, b, c):
    if a == 0:
        if b == 0:
            return "The equation is indeterminate" if c == 0 else "Impossible situation. Wrong entries"
        return f"It is a first degree equation. Solution: {'0.0' if c == 0 else solve_first_degree(b, c)}"
    else:
        disc = discriminantQuadratic(a, b, c)
        if disc < 0:
            return "There are no real solutions"
        elif disc == 0:
            root = root1Quadratic(a, b, c, disc)
            return f"It has one double solution: {abs(root)}"
        else:
            root1, root2 = root1Quadratic(a, b, c, disc), root2Quadratic(a, b, c, disc)
            sorted_sol = sorted([abs(root1) if root1 == -0.0 else root1, abs(root2) if root2 == -0.0 else root2])
            return f"Two solutions: {sorted_sol[0]}, {sorted_sol[1]}"

def inequality(eq):
    pass

"""
END OF ALGEBRA
"""

def parseEquation(eq):
    pass



"""
CALCULUS
"""

def derivativeAt(f_of, x):
    h = 0.00001
    return round(1 / (12 * h) * (f_of(x - 2 * h) - 8 * f_of(x - h) + 8 * f_of(x + h) - f_of(x + 2 * h)), 7)

def derivative(f_of, solvefor):
    return diff(f_of, solvefor)
    
def defIntegral(f, lowerbound, upperbound, n = 10000):
    stepLen = (upperbound - lowerbound) / n
    lb = lowerbound
    xRange = np.arange(lb, upperbound, stepLen)
    total = f(lowerbound) + f(upperbound)
    for i in range(1, n):
        total += 2*f(xRange[i])
    integralVal = total * stepLen / 2
    return round(integralVal, 5)

def indefIntegral(f_of, solvefor):
    integral = str(integrate(f_of, solvefor)) + " + C"
    return integral 

"""
END OF CALCULUS
"""



"""
LINEAR ALGEBRA
"""
def DiagonalSum(mat):
    left = 0
    right = 0
    for i in range(0, len(mat)):
        left += mat[i][i]
        right += mat[i][len(mat) - i - 1]
    total = left + right
    if len(mat) % 2 != 0:
        return total - (mat[len(mat) // 2][len(mat) // 2])
    return total

def Adjacent2x2(matrix):
    return np.array([[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]]).tolist()

def Adjacent3x3(matrix):
    a = np.array([[(matrix[1][1]*matrix[2][2]) - (matrix[1][2]*matrix[2][1]),
                   -((matrix[1][0]*matrix[2][2]) - (matrix[1][2]*matrix[2][0])),
                   ((matrix[1][0]*matrix[2][1]) - (matrix[1][1]*matrix[2][0]))],
                                    
                  [-((matrix[0][1]*matrix[2][2]) - (matrix[0][2]*matrix[2][1])),
                    ((matrix[0][0]*matrix[2][2]) - (matrix[0][2]*matrix[2][0])),
                    -((matrix[0][0]*matrix[2][1]) - (matrix[0][1]*matrix[2][0]))],
                                    
                  [((matrix[0][1]*matrix[1][2]) - (matrix[0][2]*matrix[1][1])),
                   -((matrix[0][0]*matrix[1][2]) - (matrix[0][2]*matrix[1][0])),
                    ((matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0]))]])

    return np.transpose(a)

def cofactorMatrix(matrix, tempMatrix, row, col, order):
    i = 0
    j = 0
    for r in range(order):
        for c in range(order):
            if r != row and c != col:
                tempMatrix[i][j] = matrix[r][c]
                j += 1
                if j == order - 1:
                    j = 0
                    i += 1

def determinant(matrix, order=1):
    det = 0
    order = len(matrix[0])
    if order == 1:
        return matrix[0][0]
    tempMatrix = [[None for i in range(order)] for i in range(order)]
    sign = 1

    for f in range(order):
        cofactorMatrix(matrix, tempMatrix, 0, f, order)
        det += sign * matrix[0][f] * determinant(tempMatrix, order = order - 1)
        sign = -sign

    return det    

"""
END OF LINEAR ALGEBRA
"""





"""
COMPLEX
"""

def complexLn(num):
    principle = str(ln(-num)) + ' + iπ'
    general = str(ln(-num)) + 'iπ(2n+1) n ∊ ℤ'
    print(f"Principal Value: {principle}")
    print(f"General: {general}")
    return str(ln(-num)) + " + " + str(math.pi) + 'i'


"""
END OF COMPLEX
"""


"""
MISC
"""

"""
END OF MISC
"""



"""
PHYSICS
"""

"""
END OF PHYSICS
"""
