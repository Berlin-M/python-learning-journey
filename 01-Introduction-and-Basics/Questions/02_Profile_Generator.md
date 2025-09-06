### Challenge Question 2: User Profile Generator

**Goal:** Write a program that receives information from a user and, based on it, generates a suggested username and password.

**Steps:**
1.  Get the user's full name in lowercase (e.g., `mahdi masoumi`).
2.  Get the user's birth year.
3.  Get the user's favorite animal in lowercase (e.g., `lion`).
4.  **Perform the following operations:**
    * Convert the user's full name to a standard, clean format where the first letter of each word is capitalized (e.g., `Mahdi Masoumi`).
    * Create a username that consists of the **first three letters of the first name** and the **last two digits of the birth year** (e.g., `mah95`).
    * Create a strong password that consists of the **favorite animal with the first letter capitalized**, followed by **@**, the **last two letters of the last name** (in uppercase), and the user's **approximate age** (e.g., `Lion@MI30`).
5.  Display all the generated information in a clean format.

**Sample Output:**

```text
Enter your full name (lowercase): mahdi masoumi
Enter your birth year: 1995
Enter your favorite animal (lowercase): lion

--- Your Profile Summary ---
Full Name: Mahdi Masoumi
Suggested Username: mah95
Suggested Password: Lion@MI30
```

>**Hint:** For this question, you will heavily rely on string manipulation, indexing, slicing, string methods, and type casting.