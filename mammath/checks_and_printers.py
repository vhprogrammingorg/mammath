from .operations import sqrt, factorial, root
import math

"""
NUMBER/SEQUENCE CHECKS AND PRINTERS
"""

def perfect_square(num):
    """
    Checks if a number is a perfect square.
    
    Args:
        num (int): The number to check.
        
    Returns:
        bool: True if the number is a perfect square, False otherwise.
    """
    root = sqrt(num)

    if math.trunc(root)-root==0:
        return True
    return False

def perfect_square_check(num):
    """
    Checks if a number is a perfect square.
    
    Args:
        num (int): The number to check.
        
    Returns:
        bool: True if the number is a perfect square, False otherwise.
    """
    if perfect_square(num) == True:
        return True
    return False

def perfect_square_printer(low, high):
    """
    Prints perfect squares within a given range.
    
    Args:
        low (int): The lower bound of the range.
        high (int): The upper bound of the range.
        
    Returns:
        None
    """
    for i in range(low, high):
        if perfect_square(i) == True:
            print(i)
            
def perfect_root_check(a, b):
    """
    Checks if a number is a perfect root.
    
    Args:
        a (int): The number to check.
        b (int): The degree of the root.
        
    Returns:
        bool: True if the number is a perfect root, False otherwise.
    """
    x = root(a, b)
    if x % 1 == 0:
        return True
    return False
def triangular_check(n):
    """
    Checks if a number is a triangular number.
    
    Args:
        n (int): The number to check.
        
    Returns:
        bool: True if the number is a triangular number, False otherwise.
    """
    for i in range(n):
        if i*(i+1)/2 == n:
            return True
    return False

def triangular_printer(low, high):
    """
    Prints triangular numbers within a given range.
    
    Args:
        low (int): The lower bound of the range.
        high (int): The upper bound of the range.
        
    Returns:
        None
    """
    for i in range(low, high):
        if triangular_check(i) == True:
            print(i)

            
def pentagonal_check(n):
    """
    Checks if a number is a pentagonal number.
    
    Args:
        n (int): The number to check.
        
    Returns:
        bool: True if the number is a pentagonal number, False otherwise.
    """
    i = 1
    while True:
        p = (3 * i * i - i) / 2
        i += 1
        if p >= n:
            break
    return p == n

def pentagonal_printer(low, high):
    """
    Prints pentagonal numbers within a given range.
    
    Args:
        low (int): The lower bound of the range.
        high (int): The upper bound of the range.
        
    Returns:
        None
    """
    for i in range(low, high):
        if pentagonal_check(i) == True:
            print(i)

def perfect_number_check(n):
    """
    Checks if a number is a perfect number.
    
    Args:
        n (int): The number to check.
        
    Returns:
        bool: True if the number is a perfect number, False otherwise.
    """
    pFactors = []
    for i in range(1, n):
        if not n % i:
            pFactors.append(i)
    return sum(pFactors) == n

def perfect_number_printer(lower, upper, list = False):
    """
    Prints perfect numbers within a given range.
    
    Args:
        lower (int): The lower bound of the range.
        upper (int): The upper bound of the range.
        list (bool, optional): If True, return a list of perfect numbers instead of printing them. Default is False.
        
    Returns:
        None
    """
    perfects = [i for i in range(lower, upper+1) if perfect_number_check(i)]
    if list:
        return perfects
    for i in perfects:
        print(i)

def pascals_printer(n):
    """
    Gives the rows up to the nth row of Pascal's triangle.
    
    Args:
        n (int): The number of rows to print.
        
    Returns:
        None
    """
    for i in range(n):
        if i > 0:
            print('')
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
            
def pascals(n):
    """
    Gives the nth row of the pascals triangle

    Args:
        n (int): The row number of Pascal's triangle.
    
    Returns:
        list: A list containing the elements of the nth row of Pascal's triangle.
    """
    l = []
    for i in range(n+1):
        l.append(factorial(n)//(factorial(i)*factorial(n-i)))     
    return l



"""
END OF NUMBER/SEQUENCE CHECKS AND PRINTERS
"""

