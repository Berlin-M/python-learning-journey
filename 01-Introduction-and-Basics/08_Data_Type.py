"""
======================================================
=== 08: Data Types | The Identity of Data          ===
======================================================

In the real world, we deal with different kinds of information: numbers, text,
true/false statements, etc. In Python, every value that is stored in a
variable also has a specific "type" or "identity." This is called a Data Type.

Knowing the data type is crucial because it determines what operations you can
perform on a value.
"""

# ----------------------------------------------------
# What is the type() function?
# ----------------------------------------------------
# `type()` is a built-in and very useful function in Python.
# Its job is simple: you give it a value or a variable, and it tells you
# what the data type of that value is.
# `type()` is like a diagnostic tool that helps us understand the structure of our data.

a_variable = "Hello!"
print("The type of a_variable is:", type(a_variable))

# We will use this function a lot throughout this lesson.


# ----------------------------------------------------
# 1. Numeric Types
# ----------------------------------------------------

# ### 1.1. Integers (int)
# All whole numbers, whether positive, negative, or zero.
age = 30
temperature = -5
print("Type of age:", type(age))

# Pro Tip 1: Python integers have no size limit and can handle extremely
# large numbers without issues (limited only by your system's memory).
large_number = 1_000_000_000_000_000_000
print(large_number)

# ### 1.2. Floating-Point Numbers (float)
# Any number that has a decimal part.
pi_value = 3.14159
price = 99.99
print("Type of price:", type(price))

# Important Note: Computers have limitations in storing some floating-point numbers
# with perfect precision. This is a general concept in computer science, not specific to Python.
# For example, the result of the sum below is not exactly 0.3!
# (We will learn ways to manage this later).
print(0.1 + 0.2)  # Output: 0.30000000000000004

# ### 1.3. Complex Numbers (complex)
# This data type is used to represent complex numbers from mathematics (which have a
# real part and an imaginary part, denoted by a `j`).
# This type is used almost exclusively in scientific computing, engineering, and advanced mathematics.
# Since its application is highly specialized, we won't go into its details in this course,
# but it's good to be aware of its existence.
complex_number = 2 + 3j
print("Type of complex_number:", type(complex_number))


# ----------------------------------------------------
# 2. Sequence Type: String (str)
# ----------------------------------------------------
# Strings are used to store text and are a sequence of characters.
# They can be created with single quotes (''), double quotes (""), or triple quotes ("""...""").
name = "Berlin"
print("Type of name:", type(name))

# Very Important (Advanced Feature): Strings are "Immutable."
# This means that once a string is created, you cannot directly change one of its characters.
# To change it, you must create a new string.
# If you uncomment the line below, you will get an error.
# name[0] = "J" # TypeError: 'str' object does not support item assignment

# Don't worry if the concept of "immutable" seems a bit vague right now. In future
# lessons, when we learn about "lists"—which are "mutable" data—you will
# understand this difference in a completely practical way.


# ----------------------------------------------------
# 3. Boolean Type (bool)
# ----------------------------------------------------
# This data type can only have two possible values: `True` or `False`.
# Booleans are the backbone of logic and decision-making in programming.
# **Note:** Pay attention to the capital T and F.
is_active = True
print("Type of is_active:", type(is_active))


# ----------------------------------------------------
# 4. None Type (NoneType)
# ----------------------------------------------------
# This data type also has only one possible value: `None`.
# `None` is used to represent the "absence of a value" or "nothingness."
# **Note:** `None` is different from `0`, `False`, or an empty string `""`.
winner = None
print("Type of winner:", type(winner))


# ----------------------------------------------------
# 5. Type Casting
# ----------------------------------------------------
# Sometimes, we need to convert a value from one data type to another. This is called Type Casting.

# ### Casting to int
# Converts a string or float to an integer. When converting a float to an int, the decimal part is "truncated" (not rounded).
int_from_float = int(7.9)
print("7.9 becomes", int_from_float) # Output: 7

# ### Casting to bool
# Almost everything in Python evaluates to `True` when cast to a boolean, except for the following values, which are `False`:
# The number zero (0 or 0.0), an empty string (""), the value None, and empty collections (which we will learn about later).
print("bool(0):", bool(0))      # False
print("bool(''):", bool(""))    # False
print("bool(None):", bool(None)) # False
print("bool(12):", bool(12))    # True

print("\nData types tutorial module loaded successfully.")