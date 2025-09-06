"""
=========================================================
=== 11: String Manipulation | The Art of Shaping Text ===
=========================================================

Strings, or text, are one of the most fundamental data types we work with,
from usernames and passwords to the content of a file or a web page. Python
provides very powerful tools for searching, modifying, and shaping strings.

In this lesson, we'll learn how to work with text like an artist: we'll cut it,
join it together, format it, and change its appearance as we wish.

Important Note: Remember that strings are "Immutable." All of these
operations create a **new string** and do not modify the original one.
"""

# ----------------------------------------------------
# 1. Basic String Operations
# ----------------------------------------------------

# ### 1.1. Concatenation
# You can join two or more strings together using the `+` operator.
first_name = "Mahdi"
last_name = "Masoumi"
full_name = first_name + " " + last_name
print(full_name)

# Warning: You cannot directly concatenate a string with a number.
# print("Age: " + 30) # TypeError: can only concatenate str (not "int") to str
# Solution: You must convert the number to a string using `str()`.
print("Age: " + str(30))

# ### 1.2. Repetition
# You can repeat a string multiple times using the `*` operator.
divider = "-" * 20
print(divider) # Output: --------------------
print("ha" * 3)    # Output: hahaha


# ----------------------------------------------------
# 2. String Formatting with f-strings (The Modern & Recommended Way)
# ----------------------------------------------------
# F-strings are the best and most readable way to embed variables inside a string.
# Simply place an `f` before the opening quote and write variable names inside `{}`.

name = "Berlin"
age = 30
city = "Tehran"

# F-strings easily handle different data types.
message = f"Hello, my name is {name}. I am {age} years old and I live in {city}."
print(message)


# ----------------------------------------------------
# 3. Common String Methods (The String Toolbox)
# ----------------------------------------------------
# Methods are functions that "belong" to a specific data type and are called with a dot `.`.
# Strings have many useful methods; here are some of the most common ones.

my_text = "   Welcome to the Python Journey!   "
print(f"Original Text: '{my_text}'")

# ### 3.1. Changing Case
# .upper(): Converts all characters to uppercase.
print("UPPER:", my_text.upper())

# .lower(): Converts all characters to lowercase.
print("lower:", my_text.lower())

# .capitalize(): Capitalizes only the first character of the string and lowercases the rest.
print("Capitalize:", my_text.capitalize())

# .title(): Capitalizes the first character of every word and lowercases the rest.
print("Title:", my_text.title())

# ### 3.2. Cleaning Whitespace
# .strip(): Removes whitespace (spaces, tabs, newlines) from the beginning and end of the string.
# This method is extremely useful for cleaning user input.
cleaned_text = my_text.strip()
print(f"Stripped Text: '{cleaned_text}'")

# .lstrip() and .rstrip() also exist to strip whitespace only from the left or right side.

# --- Pro Tip: Method Chaining ---
# You can "chain" methods together, passing the output of one method directly
# as the input to the next. The execution happens from left to right.
# Example: First, strip the whitespace, then convert everything to uppercase.
pro_cleaned_text = my_text.strip().upper()
print("Chained Methods:", pro_cleaned_text)


print("\nString manipulation tutorial module loaded successfully.")