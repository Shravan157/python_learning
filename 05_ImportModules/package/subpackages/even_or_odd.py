"""
even_or_odd.py - Number Classification Module (Inside Subpackage)

PURPOSE:
--------
This module demonstrates how to create modules inside subpackages.
It contains functions to classify numbers as even or odd.

USE CASE:
---------
When you have related functionality that should be grouped together in a subpackage,
you create modules like this inside subdirectories.

IMPORT SYNTAX (How to use this module):
----------------------------------------

METHOD 1: Import from main script (outside package)
    from package.subpackages.even_or_odd import is_even
    result = is_even(10)

METHOD 2: Import with alias
    from package.subpackages.even_or_odd import is_even as check_even
    result = check_even(10)

METHOD 3: Import all functions
    from package.subpackages.even_or_odd import *
    result = is_even(10)

METHOD 4: Import entire module
    from package.subpackages import even_or_odd
    result = even_or_odd.is_even(10)

PACKAGE STRUCTURE:
------------------
package/
    __init__.py
    maths.py
    subpackages/
        __init__.py
        even_or_odd.py  <- This file (module in subpackage)
"""


def is_even(num):
    """
    Check if a number is even.
    
    Args:
        num (int): The number to check
    
    Returns:
        bool: True if even, False if odd
    
    Example:
        >>> is_even(4)
        True
        >>> is_even(7)
        False
    """
    if num % 2 == 0:
        return True
    else:
        return False


def is_odd(num):
    """
    Check if a number is odd.
    
    Args:
        num (int): The number to check
    
    Returns:
        bool: True if odd, False if even
    
    Example:
        >>> is_odd(5)
        True
        >>> is_odd(8)
        False
    """
    return not is_even(num)


def classify_number(num):
    """
    Classify a number as even or odd and return a descriptive string.
    
    Args:
        num (int): The number to classify
    
    Returns:
        str: Description of whether the number is even or odd
    
    Example:
        >>> classify_number(10)
        '10 is an even number'
        >>> classify_number(7)
        '7 is an odd number'
    """
    if is_even(num):
        return f"{num} is an even number"
    else:
        return f"{num} is an odd number"


# Test code that runs only when this file is executed directly
if __name__ == "__main__":
    print("Testing even_or_odd module...")
    test_numbers = [2, 5, 10, 13, 20, 25]
    
    for num in test_numbers:
        print(f"{num}: {classify_number(num)}")

