import string
from typing import Union

"""
BASE CONVERSIONS
"""

def base_converter(x: Union[int, str], base: int) -> str:
    """
    Converts number x to any given base between 2 and 36 (inclusive).
    
    Args:
        x (Union[int, str]): The number to be converted. Can be an integer or a string containing digits or characters.
        base (int): The target base to convert the number to, must be between 2 and 36 (inclusive).
        
    Returns:
        str: The converted number in the target base as a string.
    """
    if not isinstance(x, int):
        if x.isdigit():
            x = int(x)
        else:
            x = sum(digs.index(char) for char in x)
            
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

def int_to_binary(num: int) -> str:
    """
    Converts an integer in base 10 to a binary number in base 2.

    Args:
        num (int): Integer in base 10.

    Returns:
        str: Binary representation of the input integer.
    """
    return bin(num)[2:]

def binary_to_int(num: str) -> int:
    """
    Converts a binary number in base 2 to an integer in base 10.

    Args:
        num (str): Binary number in base 2.

    Returns:
        int: Integer representation of the input binary number.
    """
    return int(num, 2)

def int_to_hex(num: int) -> str:
    """
    Converts an integer in base 10 to a hexadecimal number in base 16.

    Args:
        num (int): Integer in base 10.

    Returns:
        str: Hexadecimal representation of the input integer.
    """
    return hex(num)[2:]

def hex_to_int(num: str) -> int:
    """
    Converts a hexadecimal value in base 16 to an integer in base 10.

    Args:
        num (str): Hexadecimal value in base 16.

    Returns:
        int: Integer representation of the input hexadecimal value.
    """
    return int(num, 16)

def binary_to_hex(num: str) -> str:
    """
    Converts a binary number in base 2 to a hexadecimal number in base 16.

    Args:
        num (str): Binary number in base 2.

    Returns:
        str: Hexadecimal representation of the input binary number.
    """
    return hex(int(num, 2))[2:]

def hex_to_binary(num: str) -> str:
    """
    Converts a hexadecimal value in base 16 to a binary number in base 2.

    Args:
        num (str): Hexadecimal value in base 16.

    Returns:
        str: Binary representation of the input hexadecimal value.
    """
    return bin(int(num, 16))[2:]



def binary_add(a, b, print_all=False):
    """
    Adds two binary numbers in base two and prints the base 10 result as well.
    
    Args:
        a (str): The first binary number.
        b (str): The second binary number.
        print_all (bool, optional): If True, prints the result in base 10 and binary. Defaults to False.
        
    Returns:
        str: The binary sum of a and b.
    """
    sum = binary_to_int(a) + binary_to_int(b)
    if print_all:
        print("Binary:", int_to_binary(sum))
        print("Base 10:", sum)
    return int_to_binary(sum)

def binary_subtract(a, b, print_all=False):
    """
    Subtracts two binary numbers in base two and prints the base 10 result as well.
    
    Args:
        a (str): The first binary number.
        b (str): The second binary number.
        print_all (bool, optional): If True, prints the result in base 10 and binary. Defaults to False.
        
    Returns:
        str: The binary result of a subtracted by b.
    """
    sub = binary_to_int(a) - binary_to_int(b)
    if print_all:
        print("Binary:", int_to_binary(sub))
        print("Base 10:", sub)
    return int_to_binary(sub)


def binary_multiply(a, b, print_all=False):
    """
    Multiplies two binary numbers in base two and prints the base 10 result as well.
    
    Args:
        a (str): The first binary number.
        b (str): The second binary number.
        print_all (bool, optional): If True, prints the result in base 10 and binary. Defaults to False.
        
    Returns:
        str: The binary product of a and b.
    """
    mult = binary_to_int(a) * binary_to_int(b)
    if print_all:
        print("Binary:", int_to_binary(mult))
        print("Base 10:", mult)
    return int_to_binary(mult)


def binary_divide(a, b, print_all=False):
    """
    Divides two binary numbers in base two and prints the base 10 result as well.
    
    Args:
        a (str): The first binary number.
        b (str): The second binary number.
        print_all (bool, optional): If True, prints the result in base 10 and binary. Defaults to False.
        
    Returns:
        str: The binary result of a divided by b.
    """
    div = binary_to_int(a) / binary_to_int(b)
    div = int(div)
    if print_all:
        print("Binary:", int_to_binary(div))
        print("Base 10:", div)
    return int_to_binary(div)



def hex_add(a, b, print_all=False):
    """
    Adds two hexadecimal numbers in base 16 and prints the base 10 result as well.
    
    Args:
        a (str): The first hexadecimal number.
        b (str): The second hexadecimal number.
        print_all (bool, optional): If True, prints the result in base 10 and hexadecimal. Defaults to False.
        
    Returns:
        str: The hexadecimal sum of a and b.
    """
    sum = hex_to_int(a) + hex_to_int(b)
    if print_all:
        print("Hexadecimal:", int_to_hex(sum))
        print("Base 10:", sum)
    return int_to_hex(sum)


def hex_subtract(a, b, print_all=False):
    """
    Subtracts two hexadecimal numbers in base 16 and prints the base 10 result as well.
    
    Args:
        a (str): The first hexadecimal number.
        b (str): The second hexadecimal number.
        print_all (bool, optional): If True, prints the result in base 10 and hexadecimal. Defaults to False.
        
    Returns:
        str: The hexadecimal result of a subtracted by b.
    """
    sub = hex_to_int(a) - hex_to_int(b)
    if print_all:
        print("Hexadecimal:", int_to_hex(sub))
        print("Base 10:", sub)
    return int_to_hex(sub)


def hex_multiply(a, b, print_all=False):
    """
    Multiplies two hexadecimal numbers in base 16 and prints the base 10 result as well.
    
    Args:
        a (str): The first hexadecimal number.
        b (str): The second hexadecimal number.
        print_all (bool, optional): If True, prints the result in base 10 and hexadecimal. Defaults to False.
        
    Returns:
        str: The hexadecimal product of a and b.
    """
    mult = hex_to_int(a) * hex_to_int(b)
    if print_all:
        print("Hexadecimal:", int_to_hex(mult))
        print("Base 10:", mult)
    return int_to_hex(mult)


def hex_divide(a, b, print_all=False):
    """
    Divides two hexadecimal numbers in base 16 and prints the base 10 result as well.
    
    Args:
        a (str): The first hexadecimal number.
        b (str): The second hexadecimal number.
        print_all (bool, optional): If True, prints the result in base 10 and hexadecimal. Defaults to False.
        
    Returns:
        str: The hexadecimal result of a divided by b.
    """
    div = hex_to_int(a) / hex_to_int(b)
    div = int(div)
    if print_all:
        print("Hexadecimal:", int_to_hex(div))
        print("Base 10:", div)
    return int_to_hex(div)

"""
END OF BASE CONVERSIONS
"""
