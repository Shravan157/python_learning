"""
maths.py - A Module with Mathematical Operations

PURPOSE:
--------
This is a Python module (a .py file) that contains reusable mathematical functions.
Modules help organize code and promote reusability across different parts of a project.

USE CASE:
---------
When you need basic mathematical operations in multiple files, instead of rewriting
the same functions everywhere, you create a module and import it wherever needed.

IMPORT SYNTAX (How to use this module from other files):
---------------------------------------------------------

METHOD 1: Import entire module
    import package.maths
    result = package.maths.addition(5, 3)

METHOD 2: Import module with alias
    import package.maths as math_ops
    result = math_ops.addition(5, 3)

METHOD 3: Import specific functions
    from package.maths import addition, subtraction
    result = addition(5, 3)

METHOD 4: Import all functions (not recommended for large modules)
    from package.maths import *
    result = addition(5, 3)

METHOD 5: Import from parent directory (when in subpackage)
    from ..maths import addition

WHEN TO USE EACH METHOD:
------------------------
- Method 1: When you want to keep the namespace clear and avoid conflicts
- Method 2: When the module name is long and you want a shorter alias
- Method 3: When you only need specific functions (RECOMMENDED)
- Method 4: Quick prototyping, but can cause naming conflicts
- Method 5: When importing from parent package in nested structures
"""

import math  # Standard library import example

# ============================================================================
# BASIC ARITHMETIC FUNCTIONS
# ============================================================================

def addition(a, b):
    """
    Add two numbers together.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
    
    Returns:
        int/float: Sum of a and b
    
    Example:
        >>> addition(5, 3)
        8
    """
    return a + b


def subtraction(a, b):
    """
    Subtract second number from first number.
    
    Args:
        a (int/float): Number to subtract from
        b (int/float): Number to subtract
    
    Returns:
        int/float: Difference of a and b
    
    Example:
        >>> subtraction(10, 3)
        7
    """
    return a - b


def multiplication(a, b):
    """
    Multiply two numbers.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
    
    Returns:
        int/float: Product of a and b
    
    Example:
        >>> multiplication(4, 5)
        20
    """
    return a * b


def division(a, b):
    """
    Divide first number by second number.
    
    Args:
        a (int/float): Numerator
        b (int/float): Denominator (cannot be zero)
    
    Returns:
        float: Quotient of a and b
    
    Raises:
        ZeroDivisionError: If b is zero
    
    Example:
        >>> division(10, 2)
        5.0
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b


def power(base, exponent):
    """
    Calculate base raised to the power of exponent.
    
    Args:
        base (int/float): The base number
        exponent (int/float): The exponent
    
    Returns:
        int/float: base^exponent
    
    Example:
        >>> power(2, 3)
        8
    """
    return base ** exponent


def square_root(num):
    """
    Calculate square root using the math module.
    
    Args:
        num (int/float): Number to find square root of
    
    Returns:
        float: Square root of num
    
    Example:
        >>> square_root(16)
        4.0
    """
    return math.sqrt(num)


# ============================================================================
# MODULE-LEVEL VARIABLES (can be imported too!)
# ============================================================================

PI = 3.14159
E = 2.71828

# This code runs when the module is imported
if __name__ == "__main__":
    # This block only runs when this file is executed directly
    # Not when it's imported as a module
    print("Testing maths module...")
    print(f"5 + 3 = {addition(5, 3)}")
    print(f"10 - 4 = {subtraction(10, 4)}")
    print(f"6 * 7 = {multiplication(6, 7)}")
    print(f"15 / 3 = {division(15, 3)}")
    print(f"2^8 = {power(2, 8)}")
    print(f"√25 = {square_root(25)}")

