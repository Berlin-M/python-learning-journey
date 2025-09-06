"""
======================================================
=== 10: Type Casting | Alchemy with Data           ===
======================================================

In programming, we constantly work with different types of data. Sometimes,
we need to change the identity of a piece of data; for example, converting
a numeric string into a real number so we can perform mathematical
calculations on it.

This process of explicitly converting one data type to another is called
"Type Casting." It's like alchemy: we transform a raw material (one data type)
into a new substance (another data type) so we can use it in a different way.
To do this, we use functions that share the same names as the data types:
`int()`, `float()`, `str()`, and `bool()`.
"""

# ----------------------------------------------------
# 1. Casting to Integer (int)
# ----------------------------------------------------
# The `int()` function attempts to convert a value into an integer.

# ### From float to int:
# When a floating-point number is converted to an int, its decimal part is
# completely "truncated" (cut off).
# **Important:** This process is not rounding!
float_number = 9.99
integer_number = int(float_number)
print(f"The float {float_number} becomes the integer {integer_number}") # Output: 9

# ### From str to int:
# This is only successful if the string represents a whole number exactly.
string_number = "123"
converted_int = int(string_number)
print(f"The string '{string_number}' becomes the integer {converted_int}")

# If the string contains non-numeric characters (even spaces) or a decimal point,
# you will encounter a `ValueError`.
# invalid_string = "123a"
# int(invalid_string) # ValueError: invalid literal for int() with base 10: '123a'

# --- Advanced Tip ---  *Optional
# The `int()` function can take a second argument to specify the number's "base".
# This is very powerful for working with different numeral systems like
# binary (base 2) or hexadecimal (base 16).
binary_string = "1011" # The number 11 in binary
decimal_number = int(binary_string, 2)
print(f"The binary string '{binary_string}' is the decimal number {decimal_number}")


# ----------------------------------------------------
# 2. Casting to Float (float)
# ----------------------------------------------------
# The `float()` function converts a value into a floating-point number.

# ### From int to float:
# A decimal part, `.0`, is added to the number.
integer_val = 15
float_val = float(integer_val)
print(f"The integer {integer_val} becomes the float {float_val}") # Output: 15.0

# ### From str to float:
# The string must represent a number (either an integer or a float).
string_float = "3.14159"
converted_float = float(string_float)
print(f"The string '{string_float}' becomes the float {converted_float}")

# invalid_float_string = "3.14a"
# float(invalid_float_string) # ValueError: could not convert string to float: '3.14a'


# ----------------------------------------------------
# 3. Casting to String (str)
# ----------------------------------------------------
# The `str()` function converts almost any data type into its string representation.
# This function is very safe and almost never causes an error.
# Its main use is when we want to combine non-string values with strings.

number = 42
boolean_val = True
message = "The answer is " + str(number) + " which is " + str(boolean_val) + "."
print(message)


# ----------------------------------------------------
# 4. Casting to Boolean (bool) | The Concept of Truthy & Falsy
# ----------------------------------------------------
# This is one of the most important concepts in Python. When we use `bool()`,
# Python divides values into two categories: those that are inherently "Falsy"
# and all other values, which are considered "Truthy".

# ### Falsy Values (those that convert to False):
# - The `None` value
# - The boolean `False`
# - Any numeric zero: `0`, `0.0`, `0j` (for complex numbers)
# - Any empty sequence or collection: `""` (empty string), `[]` (empty list), `()`, `{}`

print(f"bool(0) is {bool(0)}")
print(f"bool(None) is {bool(None)}")
print(f"bool('') is {bool('')}")
print("-" * 20)

# ### Truthy Values (those that convert to True):
# **Any value other than the Falsy values listed above is considered Truthy.**
# This includes non-zero numbers (even negative ones), non-empty strings, and non-empty collections.
print(f"bool(1) is {bool(1)}")
print(f"bool(-1) is {bool(-1)}")
print(f"bool('Hello') is {bool('Hello')}")
print(f"bool([1, 2]) is {bool([1, 2])}")


print("\nType casting tutorial module loaded successfully.")