"""
======================================================
=== 12: Operators | The Verbs of the Programming World ===
======================================================

Operators are special symbols that take one or more values (called operands)
and perform a specific operation (like addition, comparison, or assignment)
on them.

If variables and values are the "nouns" of the coding world, then operators
are its "verbs." They give our program the power to perform actions and
make decisions. In this lesson, we will get to know the different
categories of operators in Python.
"""
# operators

# arithmetic operator, +, -, /, //, %, *, **(power)
# logical operator: (and, or, not) | || && ~
# comparision operator: ==, !=, <=, >=, <, >
# bitwise operator: &(and) |(or) ^(xor)
# assignment operator: =, +=, -=, *=, /=, ...

# ----------------------------------------------------
# 1. Arithmetic Operators
# ----------------------------------------------------
# These operators are used to perform basic mathematical calculations.
a = 10
b = 3

print(f"{a} + {b} = {a + b}")    # + (Addition)
print(f"{a} - {b} = {a - b}")    # - (Subtraction)
print(f"{a} * {b} = {a * b}")    # * (Multiplication)
print(f"{a} / {b} = {a / b}")    # / (Division) -> Note: Always returns a float.
print(f"{a} // {b} = {a // b}")  # // (Floor Division) -> Truncates the decimal part.
print(f"{a} % {b} = {a % b}")    # % (Modulo) -> Returns the remainder. Often used to check for even/odd.
print(f"{a} ** {b} = {a ** b}")  # ** (Exponentiation) -> a to the power of b


# ----------------------------------------------------
# 2. Assignment Operators
# ----------------------------------------------------
# These operators are used to assign values to variables.

# = (Simple Assignment)
x = 5
print(f"Initial x: {x}")

# Compound (Shorthand) Operators
# These operators combine an arithmetic operation with an assignment, making the code shorter.
x += 2  # Equivalent to: x = x + 2
print(f"After x += 2: {x}")

x -= 1  # Equivalent to: x = x - 1
print(f"After x -= 1: {x}")

x *= 3  # Equivalent to: x = x * 3
print(f"After x *= 3: {x}")

# These operators exist for all other arithmetic operators as well ( /=, //=, %=, **= )


# ----------------------------------------------------
# 3. Comparison Operators
# ----------------------------------------------------
# These operators compare two values and **always** return a Boolean value (`True` or `False`).
# They are the foundation of decision-making in code.
val1 = 10
val2 = 20

print(f"{val1} == {val2}: {val1 == val2}") # == (Equal to) -> Note: Do not confuse with = (assignment)!
print(f"{val1} != {val2}: {val1 != val2}") # != (Not equal to)
print(f"{val1} > {val2}: {val1 > val2}")   # > (Greater than)
print(f"{val1} < {val2}: {val1 < val2}")   # < (Less than)
print(f"{val1} >= {val2}: {val1 >= val2}") # >= (Greater than or equal to)
print(f"{val1} <= {val2}: {val1 <= val2}") # <= (Less than or equal to)


# ----------------------------------------------------
# 4. Logical Operators
# ----------------------------------------------------
# These operators are used to combine multiple conditions (Boolean expressions).
# **Very Important Note:** In Python, the logical operators are the English words
# `and`, `or`, and `not`. Symbols like `&&` or `||` belong to other languages
# (like C++ or JavaScript).

has_key = True
is_admin = False

print(f"has_key and is_admin: {has_key and is_admin}") # and: Returns True only if both sides are True.
print(f"has_key or is_admin: {has_key or is_admin}")   # or: Returns True if at least one side is True.
print(f"not has_key: {not has_key}")                   # not: Inverts the result (True becomes False, and vice versa).


# ----------------------------------------------------
# 5. Bitwise Operators - [Advanced Topic] *Optional
# ----------------------------------------------------
# **Warning:** This section is advanced and is used infrequently in everyday programming.
# These operators work directly on the bits (binary digits 0 and 1) of numbers.
# Their main use is in low-level programming, networking, and specific algorithms.

# Example: 5 in binary is `101` and 3 in binary is `011`.
num1 = 5  # 101
num2 = 3  # 011

# & (Bitwise AND): The resulting bit is 1 only if both corresponding bits are 1.
# 101 & 011 = 001 (which is 1 in decimal)
print(f"5 & 3 = {num1 & num2}")

# | (Bitwise OR): The resulting bit is 1 if at least one of the corresponding bits is 1.
# 101 | 011 = 111 (which is 7 in decimal)
print(f"5 | 3 = {num1 | num2}")

# ^ (Bitwise XOR): The resulting bit is 1 if the corresponding bits are different.
# 101 ^ 011 = 110 (which is 6 in decimal)
print(f"5 ^ 3 = {num1 ^ num2}")


# ----------------------------------------------------
# 6. Operator Precedence
# ----------------------------------------------------
# Just like in mathematics, Python has a specific order for executing operators.
# The order of precedence from highest to lowest:
# 1. ()              (Parentheses - always has the highest priority)
# 2. ** (Exponentiation)
# 3. *, /, //, %   (Multiplication & Division)
# 4. +, -            (Addition & Subtraction)
# 5. ==, !=, >, <  (Comparison)
# 6. not, and, or    (Logical)

result = 2 + 3 * 4
print(f"2 + 3 * 4 = {result}") # The output is 14, not 20 (because multiplication has higher precedence)

# **The Golden Rule:** Whenever you are in doubt about precedence, or to make your
# code more readable, **always use parentheses `()`**. Parentheses will save your
# code from any ambiguity.
clear_result = (2 + 3) * 4
print(f"(2 + 3) * 4 = {clear_result}")


print("\nOperators tutorial module loaded successfully.")