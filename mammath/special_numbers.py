from .operations import sqrt, factorial, root
import math

"""
NUMBER/SEQUENCE CHECKS AND PRINTERS
"""

def is_perfect_square(num):
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
        if is_perfect_square(i) == True:
            print(i)
            
def is_perfect_root(a, b):
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

def is_triangular(n):
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
        if is_triangular(i) == True:
            print(i)

            
def is_pentagonal(n):
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
        if is_pentagonal(i) == True:
            print(i)

def is_perfect_number(n):
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
    perfects = [i for i in range(lower, upper+1) if is_perfect_number(i)]
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
            print("")
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
            
def pascals_nth_row(n):
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

def bernoulli_number(n):
    """
    Returns the nth Bernoulli number.
    
    Args:
        n (int): The index of the Bernoulli number.
        
    Returns:
        float: The nth Bernoulli number.
    """
    A = [0] * (n+1)
    for m in range(n+1):
        A[m] = 1 / (m + 1)
        for j in range(m, 0, -1):
            A[j-1] = j * (A[j-1] - A[j])
    return A[0]

def bernoulli_printer(n):
    """
    Returns the first n Bernoulli numbers.
    
    Args:
        n (int): The number of Bernoulli numbers to return.
        
    Returns:
        list: The first n Bernoulli numbers.
    """
    return [bernoulli_number(i) for i in range(n)]

def catalan_number(n):
    """
    Returns the nth Catalan number.
    
    Args:
        n (int): The index of the Catalan number.
        
    Returns:
        int: The nth Catalan number.
    """
    from math import comb
    return comb(2*n, n) // (n + 1)

def catalan_printer(n):
    """
    Returns the first n Catalan numbers.
    
    Args:
        n (int): The number of Catalan numbers to return.
        
    Returns:
        list: The first n Catalan numbers.
    """
    return [catalan_number(i) for i in range(n)]

def lucas_sequence(n):
    """
    Returns the first n terms of the Lucas sequence.
    
    Args:
        n (int): The number of terms to return.
        
    Returns:
        list: The first n terms of the Lucas sequence.
    """
    lucas_seq = [2, 1]
    while len(lucas_seq) < n:
        lucas_seq.append(lucas_seq[-1] + lucas_seq[-2])
    return lucas_seq[:n]

"""
END OF NUMBER/SEQUENCE CHECKS AND PRINTERS
"""

