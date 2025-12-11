"""
__init__.py - Package Initialization File

PURPOSE:
--------
This special file marks a directory as a Python package and controls what gets imported
when someone uses "from package import *" or "import package"

USE CASES:
----------
1. Mark a directory as a Python package (required in Python 2.x, optional but recommended in Python 3.x)
2. Initialize package-level variables or constants
3. Control what gets exported from the package using __all__
4. Execute package initialization code
5. Import submodules to make them available at package level

SYNTAX:
-------
# To make specific items available when using "from package import *"
__all__ = ['module1', 'module2', 'function1']

# To import and expose submodules at package level
from .module import function_name

EXAMPLE STRUCTURE:
------------------
package/
    __init__.py       <- This file (makes 'package' a package)
    maths.py          <- Module with math functions
    subpackages/
        __init__.py   <- Makes 'subpackages' a package
        even_or_odd.py <- Module in subpackage

HOW IT WORKS:
-------------
When you do "import package", Python executes this __init__.py file first.
Anything defined here becomes part of the package namespace.
"""

# Package metadata
__version__ = "1.0.0"
__author__ = "Shravan"

# You can import specific functions to make them available at package level
# Uncomment below to make functions directly accessible via 'package.addition()'
# from .maths import addition, subtraction, multiplication, division

# Define what gets imported with "from package import *"
__all__ = ['maths', 'subpackages']

print("Package 'package' has been initialized!")  # This runs when package is first imported
