r"""
# Escape Sequences
An escape sequence is a backslash \ followed by a character,
 used inside a string to represent special characters that are otherwise hard to type.
(Sequence)	    (Short English Description)
\n	            Newline
\t	            Horizontal Tab
\\	            Literal backslash
\'	            Single quote
\"	            Double quote
\b	            Backspace
\r	            Carriage Return
\f	            Formfeed
\a	            Bell / Alert
\v	            Vertical Tab
\ooo	        Character with octal value
\xhh	        Character with hex value
"""
# 1. Newline: \n
# Moves the text after it to the next line.
print("Hello\nWorld!")

print("🚀--------------------🚀")

# 2. Horizontal Tab: \t
# Adds a tab space.
print("Username:\tAdmin")
print("Password:\tSecret")

print("🏮--------------------------------------------🏮")

# 3. Literal Backslash: \\
# Used to print an actual backslash character.
print("The file is located at: C:\\Users\\Profile")

print("🏮--------------------------------------------🏮")

# 4. Double Quote: \"
# Allows you to include a double quote inside a double-quoted string.
print("He said, \"Python is awesome!\"")

print("🏮--------------------------------------------🏮")

# 5. Single Quote: \'
# Allows you to include a single quote inside a single-quoted string.
print('It\'s a sunny day.')

print("🏮--------------------------------------------🏮")

# 6. Backspace: \b
# Deletes the character before it
print("Hello\bWorld")  # Output may appear as 'HellWorld' depending on terminal

print("🏮--------------------------------------------🏮")

# 7. Carriage Return: \r
# Moves the cursor to the beginning of the line
print("12345\rABCDE")  # Output may appear as 'ABCDE5' in some terminals

print("🏮--------------------------------------------🏮")

# 8. Formfeed: \f
# Advances the paper to the next page (mostly affects printing, in terminal may just add a small space)
print("Hello\fWorld")

print("🏮--------------------------------------------🏮")

# 9. Bell / Alert: \a
# Produces a sound alert (may not work in all terminals)
print("Alert!\a")

print("🏮--------------------------------------------🏮")

# 10. Vertical Tab: \v
# Moves the cursor down to the next vertical tab position
print("Hello\vWorld")

print("🏮--------------------------------------------🏮")

# 11. Character with octal value: \ooo
# Prints a character based on its octal ASCII code
print("\101\102\103")  # Prints 'ABC' (\101 = A, \102 = B, \103 = C)

print("🏮--------------------------------------------🏮")

# 12. Character with hex value: \xhh
# Prints a character based on its hexadecimal ASCII code
print("\x41\x42\x43")  # Prints 'ABC' (\x41 = A, \x42 = B, \x43 = C)

r"""
Don’t worry about the length of this list. For now, you will mostly work with the first six (\n, \t, \\, \", \', \b). 🚀

Examples 11 and 12 (\ooo and \xhh) will be fully explained later in the course. 📚
"""