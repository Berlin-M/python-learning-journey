"""
=============================================================
=== 09: Getting User Input | Interacting with the Program ===
=============================================================

Until now, all the programs we've written have been static; meaning they
followed a fixed path from start to finish. But the real power of programming
is revealed when we can interact with the user.

The `input()` function is the bridge between our program and the user. This
function allows the program to pause its execution, ask the user for information,
and then use that information in the rest of the program. This lesson is our first
step toward building dynamic and interactive applications.
"""

# ----------------------------------------------------
# 1. The Basic Structure of the `input()` Function
# ----------------------------------------------------
# Working with `input()` is very simple. The function takes an optional string
# as an argument, which is called the "prompt." It displays this prompt to the user,
# then waits for the user to type something and press the Enter key.

# General Structure:
# variable_to_store_result = input("Your prompt message to the user: ")

# Very important note: The text shown to the user as a guide (the prompt)
# should always be written inside the `input()` function itself. This method
# makes the code shorter and more readable.
user_city = input("Where are you from? ")
print("Wow,", user_city, "is a beautiful place!")


# ----------------------------------------------------
# 2. The Most Important Rule of `input()`: The Output is ALWAYS a String (str)!
# ----------------------------------------------------
# Never forget this point. It doesn't matter if the user enters a number, a word,
# or anything else; the value that the `input()` function returns is **always and
# forever** of the string data type.

user_age_str = input("Please enter your age: ")
print("The type of your input is:", type(user_age_str))

# What problem does this rule cause?
# If you try to perform a mathematical operation with this input, you will get an error.
# If you uncomment the line below, the program will crash with an error:
# birth_year = 2025 - user_age_str # TypeError: unsupported operand type(s) for -: 'int' and 'str'

# Python is telling us that it cannot subtract a string from an integer.


# ----------------------------------------------------
# 3. The Solution: Combining `input()` with Type Casting
# ----------------------------------------------------
# To solve the problem above, we must explicitly tell Python to convert the
# user's input to the data type we need (e.g., `int` or `float`).

# Step-by-step method:
num1_str = input("Enter the first number: ")
num1_int = int(num1_str) # Convert the string to an integer

num2_str = input("Enter the second number: ")
num2_int = int(num2_str) # Convert the string to an integer

result = num1_int + num2_int
print("The sum is:", result)

# Professional and shorter method (combining two steps in one line):
# This method is much more common.
num3 = int(input("Enter another number: "))
print("The type is now:", type(num3))


# Advanced Note: What happens if the user enters a word instead of a number?
# In this case, the `int()` function cannot convert it, and the program will crash
# with another error called a `ValueError`. This error tells us that the given

# value is not a valid format for converting to an integer. We will learn
# how to handle these errors in future lessons to build more robust programs.


print("\nUser input tutorial module loaded successfully.")