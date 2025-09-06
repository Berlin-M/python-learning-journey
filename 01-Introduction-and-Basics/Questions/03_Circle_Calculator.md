### Challenge Question 3: Circle Calculator

**Goal:** Write a program that gets the radius of a circle from the user and calculates its circumference and area with high precision.

**Steps:**
1.  First, define a "constant" variable for Pi (`PI`) with the value `3.14159`.
2.  Get the radius of the circle from the user. Note that the radius can be a decimal number (e.g., `2.5`).
3.  Convert the input to the `float` type.
4.  Calculate the **circumference** of the circle using the formula `2 * PI * r`.
5.  Calculate the **area** of the circle using the formula `PI * r²`.
6.  Display the results, along with the input radius, in a complete message to the user.

**Sample Output:**

```text
Enter the radius of the circle: 2.5
--- Circle Calculations ---
For a circle with radius 2.5:
- The circumference is: 15.70795
- The area is: 19.6349375
```
>**Hint:** Pay close attention to operator precedence! To calculate the power of 2, you must use the exponentiation operator (**). Make sure you implement the area formula correctly.