import math
from operations import *

"""
PRIME NUMBERS
"""

def prime_factors(n, Print=False):
    """
    Returns a list of prime factors.
    
    Args:
        n (int): The number to find the prime factors of.
        Print (bool, optional): If True, print the prime factors. Default is False.
        
    Returns:
        list: A list of the prime factors.
    """
    l = []
    while n % 2 == 0:
        l.append(2)
        if Print:
            print(2)
        n = n / 2  
    for i in range(3,int(sqrt(n))+1,2):
        while n % i== 0:
            l.append(i)
            if Print:
                print(i)
            n = n / i
    if n > 2 and prime_check(n):
        l.append(n)
        if Print:
            print(n)
    return l

def prime_number_printer(lower, upper):
    """
    Prints prime numbers from the lowerbound to the upperbound
    
    Args:
        lower (int): The lower bound of the range.
        upper (int): The upper bound of the range.
        
    Returns:
        None
    """
    for num in range(lower, upper+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num)

def prime_check(n):
    """
    Checks if a number is prime.
    
    Args:
        n (int): The number to check.
        
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n == 1 or not n:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    maxNum = math.floor(sqrt(n))
    for i in range(3, maxNum + 1, 2):
        if not n % i:
            return False
    return True


"""
END OF PRIME NUMBERS
"""
