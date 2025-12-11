"""
__init__.py - Subpackage Initialization File

PURPOSE:
--------
This file marks the 'subpackages' directory as a Python subpackage.
It works the same way as the parent package's __init__.py but for nested packages.

USE CASE:
---------
When you want to organize related modules into subdirectories within a package,
you create subpackages. Each subpackage needs its own __init__.py file.

STRUCTURE:
----------
package/                    <- Main package
    __init__.py            <- Main package initializer
    maths.py               <- Module in main package
    subpackages/           <- Subpackage directory
        __init__.py        <- This file (subpackage initializer)
        even_or_odd.py     <- Module in subpackage

IMPORT EXAMPLES:
----------------
# Import from subpackage
from package.subpackages.even_or_odd import is_even

# Import subpackage module
from package.subpackages import even_or_odd

HOW IT WORKS:
-------------
When you import from 'package.subpackages', Python executes this __init__.py file.
You can use it to expose specific modules or functions from the subpackage.
"""

# Subpackage metadata
__version__ = "1.0.0"

# You can make modules available at subpackage level
# Uncomment below to allow: from package.subpackages import is_even
# from .even_or_odd import is_even, is_odd, classify_number

# Define what gets imported with "from package.subpackages import *"
__all__ = ['even_or_odd']

print("Subpackage 'subpackages' has been initialized!")