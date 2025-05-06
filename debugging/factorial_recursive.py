#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a non-negative integer n using recursion.

    Parameters:
        n (int): A non-negative integer for which the factorial is to be calculated.

    Returns:
        int: The factorial of the input integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Convert the first command-line argument to an integer and calculate its factorial
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
