import numpy as np
import math
from prime_numbers import *

"""
MISC
"""

def percentage_change(a, b):
    """
    Returns the percentage change from a to b
    """
    if a == b:
        return 100.0
    try:
        return round(((b - a)/a)*100, 3)
    except ZeroDivisionError:
        return float("inf")
    
def percentage(a, b, integer = False):
    """
    Returns what percent a is of b
    """
    percent = a / b * 100
    if integer:
        return int(percent)
    return percent

def average(*numbers):
    """
    Returns the average of any amount of given numbers
    """
    total = np.sum(list(numbers))
    length = len(numbers)
    return total / length

def consecutive_int_calc(x):
    """
    Returns three consecutive numbers that sum to the given number x
    """
    a = (x/3)-1
    b = x/3
    c = (x/3)+1
    return [a, b, c]

def ascending_sort(*args):
    """
    Sorts given values in ascending order
    """
    argList = list(args)
    argList.sort()
    return argList

def descending_sort(*args):
    """
    Sorts given values in descending order
    """
    argList = list(args)
    argList.sort(reverse=True)
    return argList

def times_tables(n):
    """
    Prints times tables until n
    """
    for i in range(1, n+1):
        for j in range(i, (n*i)+i, i):
            print(str(j) + " ", end="")
        print("")

def coefficients_quadratic(string):
    """
    Returns the coefficients of a quadratic equation in a list given in the form of ax^2 + bx + c
    """
    string = "".join(" " if i == "x" or i == "+" else i for i in string)
    string = string.replace("^2", " ")
    return list(map(int, string.split()))

def sum_to_palindrome(num, stepsList = False):
    """
    Returns the amount of iterations it takes for the reverse of a number, added to the number to be a palindrome, and the resulting palindrome
    """
    isPalindrome = lambda num: num == num[::-1]
    steps = 0
    stepList = [] if stepsList else None
    while not isPalindrome(str(num)):
        num = str(num)
        num = str(int(num) + int(str(num)[::-1]))
        steps += 1
        stepList.append(num) if stepsList else None
  
    return "Final palindrome: " + num + ", Steps: " + str(steps) if not stepsList else "Final Palindrome: " + num + ", Steps: " + str(steps) + ", Step List: " + str([(i+1, int(j)) for i, j in enumerate(stepList)]).strip("[]")
        
def proth_primes(k):
    """
    Returns the next Proth prime (k*2^n + 1) with k given 
    """
    n = 1
    while not prime_check((k * 2**n) + 1):
        n += 1
    return "Number: " + str((k * 2**n) + 1) + ", n: " + str(n)
    
def proth_primes_check(k, n):
    """
    Checks if a number is in the form of a Proth prime
    """
    return prime_check((k * 2**n) + 1)

def is_polydivisible(number):
    """
    Returns whether a number is polydivisible or not - a number where the first to the nth digit in the number is divisible by n
    """
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

def weighted_avg(*args):
    """
    Input any nmber of numbers with values and weights in tuple of that orders
    """
    t = 0
    x = 0
    for i in args:
        t += i[1]
        x += i[0] * i[1]
    return x / t

def reflect_num(n, rn):
    """
    Reflects a number over another number on a number line
    """
    return rn * 2 - n

"""
END OF MISC
"""
