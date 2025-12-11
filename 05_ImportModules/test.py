"""
test.py - Demonstration of Different Import Methods

PURPOSE:
--------
This file demonstrates ALL the different ways to import modules and packages in Python.
It serves as a practical guide for understanding import statements.

USE CASE:
---------
When developing projects with multiple .py files, you need to import functions and classes
from other modules. This file shows you how to do that with various syntax options.

WHY THIS FILE EXISTS:
---------------------
While Jupyter notebooks (.ipynb) are great for learning, real projects use .py files.
This demonstrates how to import packages in actual Python scripts that you'll use in production.

PACKAGE STRUCTURE WE'RE IMPORTING FROM:
----------------------------------------
05_ImportModules/
    test.py                          <- This file
    package/
        __init__.py
        maths.py                     <- Contains: addition, subtraction, multiplication, division, etc.
        subpackages/
            __init__.py
            even_or_odd.py           <- Contains: is_even, is_odd, classify_number
"""

print("=" * 80)
print("PYTHON IMPORT METHODS DEMONSTRATION")
print("=" * 80)

# ============================================================================
# METHOD 1: Import all functions using * (wildcard import)
# ============================================================================
print("\n[METHOD 1] Import all functions using * (wildcard)")
print("-" * 80)
print("Syntax: from package.module import *")
print("Use Case: Quick prototyping, but NOT recommended for production")
print("Why: Can cause naming conflicts and makes code harder to debug\n")

from package.maths import *

print("Code: from package.maths import *")
print(f"Result: addition(10, 5) = {addition(10, 5)}")
print(f"Result: subtraction(10, 5) = {subtraction(10, 5)}")
print(f"Result: multiplication(10, 5) = {multiplication(10, 5)}")
print(f"Result: division(10, 5) = {division(10, 5)}")

# ============================================================================
# METHOD 2: Import specific functions (RECOMMENDED)
# ============================================================================
print("\n[METHOD 2] Import specific functions (RECOMMENDED)")
print("-" * 80)
print("Syntax: from package.module import function1, function2")
print("Use Case: When you know exactly which functions you need")
print("Why: Clean, explicit, and avoids namespace pollution\n")

from package.subpackages.even_or_odd import is_even, is_odd, classify_number

print("Code: from package.subpackages.even_or_odd import is_even, is_odd")
print(f"Result: is_even(10) = {is_even(10)}")
print(f"Result: is_odd(10) = {is_odd(10)}")
print(f"Result: classify_number(25) = {classify_number(25)}")

# ============================================================================
# METHOD 3: Import entire module
# ============================================================================
print("\n[METHOD 3] Import entire module")
print("-" * 80)
print("Syntax: import package.module")
print("Use Case: When you want to keep the namespace clear")
print("Why: Makes it obvious where functions come from\n")

import package.maths

print("Code: import package.maths")
print(f"Result: package.maths.power(2, 8) = {package.maths.power(2, 8)}")
print(f"Result: package.maths.square_root(16) = {package.maths.square_root(16)}")
print(f"Result: package.maths.PI = {package.maths.PI}")

# ============================================================================
# METHOD 4: Import module with alias
# ============================================================================
print("\n[METHOD 4] Import module with alias")
print("-" * 80)
print("Syntax: import package.module as alias")
print("Use Case: When module names are long or you want shorter names")
print("Why: Improves code readability with shorter aliases\n")

import package.subpackages.even_or_odd as checker

print("Code: import package.subpackages.even_or_odd as checker")
print(f"Result: checker.is_even(100) = {checker.is_even(100)}")
print(f"Result: checker.classify_number(77) = {checker.classify_number(77)}")

# ============================================================================
# METHOD 5: Import specific function with alias
# ============================================================================
print("\n[METHOD 5] Import specific function with alias")
print("-" * 80)
print("Syntax: from package.module import function as alias")
print("Use Case: When function name conflicts with existing names")
print("Why: Avoids naming conflicts while keeping code clean\n")

from package.maths import addition as add, subtraction as sub

print("Code: from package.maths import addition as add, subtraction as sub")
print(f"Result: add(100, 50) = {add(100, 50)}")
print(f"Result: sub(100, 50) = {sub(100, 50)}")

# ============================================================================
# METHOD 6: Import from subpackage
# ============================================================================
print("\n[METHOD 6] Import from nested subpackage")
print("-" * 80)
print("Syntax: from package.subpackage.module import function")
print("Use Case: When working with deeply nested package structures")
print("Why: Allows organized code structure in large projects\n")

from package.subpackages.even_or_odd import is_even as check_even

print("Code: from package.subpackages.even_or_odd import is_even as check_even")
print(f"Result: check_even(42) = {check_even(42)}")
print(f"Result: check_even(43) = {check_even(43)}")

# ============================================================================
# BONUS: Importing standard library modules
# ============================================================================
print("\n[BONUS] Importing Python Standard Library")
print("-" * 80)
print("Syntax: import module_name")
print("Use Case: Using built-in Python modules")
print("Why: Python comes with many useful modules\n")

import random
import datetime
import os

print("Code: import random, datetime, os")
print(f"Result: random.randint(1, 100) = {random.randint(1, 100)}")
print(f"Result: datetime.datetime.now() = {datetime.datetime.now()}")
print(f"Result: os.getcwd() = {os.getcwd()}")

# ============================================================================
# SUMMARY AND BEST PRACTICES
# ============================================================================
print("\n" + "=" * 80)
print("BEST PRACTICES SUMMARY")
print("=" * 80)
print("""
1. ✅ PREFER: from package.module import specific_function
   - Clean and explicit
   - Easy to track dependencies
   
2. ✅ GOOD: import package.module as alias
   - Clear namespace
   - Avoids conflicts
   
3. ⚠️  CAUTION: from package.module import *
   - Only for quick prototyping
   - Can cause naming conflicts
   
4. ✅ ALWAYS: Use meaningful aliases
   - Makes code more readable
   - Follows Python conventions (e.g., import numpy as np)
   
5. ✅ ORGANIZE: Group imports at the top of file
   - Standard library imports first
   - Third-party imports second
   - Local application imports last
""")

print("\n" + "=" * 80)
print("DEMONSTRATION COMPLETE!")
print("=" * 80)