"""
======================================================
=== 07: Advanced Variable Techniques               ===
======================================================

Now that you are familiar with the basics of variables, let's explore some
more advanced and professional techniques that will make your code shorter,
more readable, and significantly more powerful.
These techniques are part of Python's beautiful features that set it
apart from many other languages.
"""

# ----------------------------------------------------
# 1. Multiple Assignment
# ----------------------------------------------------
# You can assign a single value to multiple variables simultaneously.
# This is very useful for initializing several variables to the same constant value.

# Instead of writing three separate lines:
# x = 0
# y = 0
# z = 0

# You can write it all on one line:
x = y = z = 0
print(x, y, z)


# ----------------------------------------------------
# 2. Packing and Unpacking
# ----------------------------------------------------
# This is a very powerful and "Pythonic" feature. You can assign
# multiple values to multiple variables at the same time.

# Multiple values are assigned to multiple variables on one line
user_name, user_age, user_city = "Berlin", 30, "Tehran"

print("Name:", user_name)
print("Age:", user_age)
# Important Note: The number of variables on the left must be exactly equal to the number of values on the right.


# ----------------------------------------------------
# 3. Constants by Convention
# ----------------------------------------------------
# In many languages, there is a concept of a "constant," which is an unchangeable value.
# While Python doesn't technically have true constants, there is a very important
# convention among developers:

# **Write the names of variables whose values are not meant to change in all uppercase letters (UPPER_CASE).**

# This signals to others (and your future self) "Do not change this value!".
PI = 3.14159
MAX_LOGIN_ATTEMPTS = 5
SITE_NAME = "My Awesome App"


# ----------------------------------------------------
# 4. Dynamic Typing
# ----------------------------------------------------
# This is one of Python's core features. You do not need to declare a variable's
# type in advance. Python automatically detects the data type, and you can
# even change the type of a variable during the program's execution.

my_var = "This is a string"  # Here, my_var is a string
print(my_var)

my_var = 100  # Now, the same variable has become an integer!
print(my_var)

my_var = True  # And now it has been changed to a boolean
print(my_var)


# ----------------------------------------------------
# 5. The Throwaway Variable (`_`)
# ----------------------------------------------------
# Sometimes when unpacking, you don't need all the values. By a common
# convention, the underscore (`_`) is used as a variable name for values
# you want to discard. This tells the reader of the code: "I am intentionally ignoring this value."

# Imagine you only need the name and city, and you don't care about the age
user_name, _, user_city = "Berlin", 30, "Tehran"
print("User", user_name, "is from", user_city)


# ----------------------------------------------------
# 6. Deleting a Variable (`del`)
# ----------------------------------------------------
# You can completely remove a variable from memory after you are done with it.
# This is done with the `del` statement and can be useful for memory management
# in large applications (when working with very large variables).

temporary_data = "This is a very large amount of data..."
# ... operations are performed with this data ...
print("Data exists.")

del temporary_data

# If you uncomment the next line, you will get an error because the variable no longer exists
# print(temporary_data) # NameError: name 'temporary_data' is not defined
print("Data has been deleted.")


print("\nAdvanced variables techniques module loaded successfully.")