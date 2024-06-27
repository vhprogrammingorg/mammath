from .operations import sqrt
from .special_numbers import is_perfect_square

"""
FIBONACCI
"""

def fibonacci_binet(n):
    """
    Fast Fibonacci calculator using Binets formula.
    
    Args:
        n (int): The nth number in the Fibonacci sequence.
        
    Returns:
        int: The nth Fibonacci number.
    """
    x = (((((1+sqrt(5))/2)**n)-((((1-sqrt(5))/2)**n))))/sqrt(5)
    return round(x)

def fibonacci(n):
    """
    Very efficient Fibonacci computation.

    Args:
        n (int): The nth number in the Fibonacci sequence.
        
    Returns:
        int: The nth Fibonacci number.
    """
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
    # if n0 < 0:
    #     return negativeFib(n, r)
    return r

def fibonacci_check(n):
    """
    Checks if a number is in the classic Fibonacci sequence.
    
    Args:
        n (int): The number to check.
        
    Returns:
        bool: True if the number is in the Fibonacci sequence, False otherwise.
    """
    return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)

def fibonacci_printer(low, high):
    """
    Prints the Fibonacci numbers in the given range (inclusive).
    
    Args:
        low (int): The lower bound of the range.
        high (int): The upper bound of the range.
        
    Returns:
        None
    """
    for i in range(low, high+1):
        if fibonacci_check(i) == True:
            print(i)

"""
END OF FIBONACCI
"""

