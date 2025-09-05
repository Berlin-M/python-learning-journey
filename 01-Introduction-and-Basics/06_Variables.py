"""
======================================================
=== 06: Variables | The Smart Containers of Code     ===
======================================================

In programming, variables are like containers for storing data.
We put a label on each container (the variable name) and place a value inside it.
This allows us to save data, refer to it, and change it throughout the
program. Using variables correctly makes code readable, flexible,
and powerful.
"""

# ----------------------------------------------------
# 1. Defining a Variable (Creating a Box)
# ----------------------------------------------------
# To create a variable, you simply choose a name for it and assign
# a value to it using the assignment operator (=).

# General Structure:
# variable_name = value

# Example:
course_name = "Python Learning Journey"
course_version = 1.0
is_beginner_friendly = True

# Now, we can access the value inside the variable by calling its name.
print(course_name)
print(course_version)


# ----------------------------------------------------
# 2. Mandatory Naming Rules (Enforced by Python)
# ----------------------------------------------------
# If you don't follow these rules, your program will crash with an error.

# 1. A variable name must start with a letter (a-z, A-Z) or an underscore (_).
#    ✅ Correct: name, _user_id
#    ❌ Incorrect: 1st_place (Cannot start with a number)

# 2. A variable name cannot contain special characters like !, @, #, $, -, +, etc.
#    ✅ Correct: user_age, user1
#    ❌ Incorrect: user-age, user@name

# 3. Variable names are Case-Sensitive.
#    `age`, `Age`, and `AGE` are three completely different variables.
age = 30
Age = 40
print(age)  # Output: 30
print(Age)  # Output: 40

# 4. A variable name cannot be any of Python's reserved keywords (e.g., if, for, True).


# ----------------------------------------------------
# 3. Naming Conventions (The Unwritten Rules for Professionals)
# ----------------------------------------------------
# These rules are not mandatory, but following them will make your code more readable,
# cleaner, and more professional.

# 1. The Python Standard: snake_case
#    In this standard, all letters are lowercase, and words are separated by underscores (_).
#    ✅ Recommended: first_name, user_profile_url, items_in_cart
#    ❌ Not Recommended: FirstName, userprofileurl

# 2. Choose descriptive and meaningful names.
#    The variable's name should clearly state its purpose.
#    ✅ Good: user_password, number_of_login_attempts
#    ❌ Bad:   p, n, temp1, x

# 3. Avoid using the lowercase letter 'L' (l), the uppercase letter 'O' (O),
#    and the uppercase letter 'I' (I) as single-character variable names.
#    They can be mistaken for the numbers 1 and 0.


# ----------------------------------------------------
# 4. Why Do We Use Variables?
# ----------------------------------------------------

# 1. Reusability
#    You can define a value once and use it hundreds of times in your program.
#    If you need to change that value, you only have to edit it in one place.

app_name = "My Awesome App"
print("Welcome to", app_name)
print("Thank you for using", app_name)
print(app_name, "Version 2.1")

# 2. Readability
#    Variables give meaning to your code and make its logic clearer.

# ❌ Without variables (ambiguous code):
print("User: Mahdi | Action: LOGIN_SUCCESS | IP: 192.168.1.1")

# ✅ With variables (readable and manageable code):
user = "Mahdi"
action = "LOGIN_SUCCESS"
ip_address = "192.168.1.1"
print("User:", user, "| Action:", action, "| IP:", ip_address)


# ----------------------------------------------------
# 5. Python Keywords
# ----------------------------------------------------
# These are the reserved words in Python that have special meanings. You cannot
# use them as variable names.
# A list of some keywords:
# False, None, True, and, as, break, class, continue, def, if, for, while, ...

print("\nVariables tutorial module loaded successfully.")