"""
======================================================
=== 05: Comments | Documenting Code Like a Pro     ===
======================================================
The Core Philosophy: "Code tells you HOW, comments tell you WHY."
Well-written code explains its own functionality. Comments are reserved for
expressing intent, complex logic, and notes that cannot be inferred from the
code itself.
"""

# ----------------------------------------------------
# 1. Syntactic Types of Comments
# ----------------------------------------------------

# ### 1.1. Single-Line Comments
# Begins with a hash (#) and extends to the end of the line. Used for short,
# focused explanations. This is the primary and most common commenting method in Python.

# ### 1.2. Inline Comments
# A single-line comment placed on the same line as a statement. It should be
# used sparingly to avoid visual clutter. A minimum of two spaces before an
# inline comment is recommended for readability.
print("STATUS_CODE: 200")  # Return the standard web success code for the operation

# ### 1.3. Block Comments
# To temporarily disable multiple lines of code (Commenting Out) or to write
# multi-line descriptions, using consecutive # symbols is often clearer and
# more standard than using """...""". This technique is especially useful for debugging.
#
# print("Debug: Attempting to establish connection...")
# print("Debug: Connection successful.")


# ### 1.4. Multi-line Strings vs. Docstrings
# The """...""" or '''...''' syntax officially creates a "Multi-line String,"
# not a comment. If the string isn't assigned to a variable, the interpreter
# ignores it.
#
# Its primary and standard use is for writing "Docstrings" as defined by PEP 257.
# Docstrings serve as the official documentation for a module, class, or function
# and can be extracted by automated documentation tools (like Sphinx).

""" test
This is a docstring for the entire module (the file itself).
"""
'''
This is a docstring for the entire module (the file itself).

'''


# ----------------------------------------------------
# 2. Common Commenting Conventions
# ----------------------------------------------------
# These are not Python commands but are globally recognized conventions to improve
# readability and teamwork.

# ### 2.1. Task Tags
# Used to mark tasks that need future attention.
# TODO: A feature or task that needs to be completed.
# FIXME: A known bug or issue that needs to be fixed.
# XXX: A part of the code that is problematic, convoluted, or needs major refactoring.

# FIXME: The error message in this section is not clear for the end-user and needs to be rewritten.
# TODO: The ability to send a report to the admin's email should be added here.

# ### 2.2. Explanatory Tags
# NOTE: Used to explain a specific or non-obvious part of the code.
# NOTE: This error message is kept generic to avoid leaking technical system details.
print("An unexpected error occurred.")


# ----------------------------------------------------
# 3. Principles of Effective Commenting
# ----------------------------------------------------

# ### Principle 1: Don't Paraphrase the Code, Explain the Intent
# ❌ Bad:
# print("Hello, World!")  # Prints the string "Hello, World!"

# ✅ Good:
# print("Process initiated successfully.")  # Inform the user that the main operation has started.


# ### Principle 2: Keep Comments Up-to-Date
# An outdated, incorrect comment is far more harmful than no comment at all because
# it provides misleading information. If you change the code's logic, always review
# and update its corresponding comment.

# ### Principle 3: Strive for Self-Documenting Code
# The best documentation is the code itself. Even with simple commands like print,
# the text you display can convey your intent and eliminate the need for a comment.
# ❌ Bad (Vague):
# print("Done.")

# ✅ Good (Descriptive and Self-Documenting):
# print("User data successfully exported to CSV file.")


print("\nPro-level commenting tutorial module loaded successfully.")