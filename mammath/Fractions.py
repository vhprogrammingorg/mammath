from fractions import Fraction

"""
FRACTIONS
"""

def add_fraction(a, b):
    """
    Adds fractions.
    
    Args:
        a (str): The first fraction.
        b (str): The second fraction.
        
    Returns:
        str: The result of a + b as a simplified fraction.
    """
    ans = Fraction(a) + Fraction(b)
    return str(ans)


def subtract_fraction(a, b):
    """
    Subtracts fractions.
    
    Args:
        a (str): The first fraction.
        b (str): The second fraction.
        
    Returns:
        str: The result of a - b as a simplified fraction.
    """
    ans = Fraction(a) - Fraction(b)
    return str(ans)


def multiply_fraction(a, b):
    """
    Multiplies fractions.
    
    Args:
        a (str): The first fraction.
        b (str): The second fraction.
        
    Returns:
        str: The result of a * b as a simplified fraction.
    """
    ans = Fraction(a) * Fraction(b)
    return str(ans)


def divide_fraction(a, b):
    """
    Divides fractions.
    
    Args:
        a (str): The first fraction.
        b (str): The second fraction.
        
    Returns:
        str: The result of a / b as a simplified fraction.
    """
    ans = Fraction(a) / Fraction(b)
    return str(ans)


def simplify_fraction(a):
    """
    Simplifies fractions.
    
    Args:
        a (str): The fraction to be simplified.
        
    Returns:
        str: The simplified fraction.
    """
    return str(Fraction(a).limit_denominator())


def percentage_decimal(percentage):
    """
    Converts percentages to decimals.
    
    Args:
        percentage (float): The percentage to be converted.
        
    Returns:
        float: The decimal equivalent of the percentage.
    """
    return percentage / 100


def per_frac(p):
    """
    Converts percentages to fractions.
    
    Args:
        p (float): The percentage to be converted.
        
    Returns:
        str: The fraction equivalent of the percentage.
    """
    dec = p / 100
    fraction = Fraction(dec)
    return str(fraction)


def percentage_fraction(percentage):
    """
    Converts percentages to fractions.
    
    Args:
        percentage (float): The percentage to be converted.
        
    Returns:
        str: The fraction equivalent of the percentage.
    """
    fracOutput = per_frac(percentage)
    return "{0}".format(fracOutput)


def fraction_decimal(fraction):
    """
    Converts fractions to decimals.
    
    Args:
        fraction (str): The fraction to be converted.
        
    Returns:
        str: The decimal equivalent of the fraction, rounded to 5 decimal places.
    """
    dec = float(fraction)
    return str(round(dec, 5))


def fraction_percentage(fraction):
    """
    Converts fractions to percentages.
    
    Args:
        fraction (str): The fraction to be converted.
        
    Returns:
        float: The percentage equivalent of the fraction.
    """
    f = float(fraction)
    return f * 100


def decimal_percentage(decimal):
    """
    Converts decimals to percentages.
    
    Args:
        decimal (float): The decimal to be converted.
        
    Returns:
        str: The percentage equivalent of the decimal.
    """
    percentage = "{:.0%}".format(decimal)
    return str(percentage)

def decimal_fraction(decimal):
    """
    Converts decimals to fractions.
    
    Args:
        decimal (float): The decimal to be converted.
        
    Returns:
        str: The fraction equivalent of the decimal.
    """
    return str(Fraction(decimal).limit_denominator())

"""
END OF FRACTIONS
"""

