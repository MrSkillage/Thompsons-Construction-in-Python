#! /usr/bin/env python3

# Conor Rabbitte 04/02/2020
# Calculate the square root of a number.

def sqrt(x):
    """
    Calculate the sqaure root of arguement x
    """
    # Check that x is positive.
    if x < 0:
        print("Error: negative value supplied")
        return -1
    else:
        print("Here we go...")

    # Initial guess for the square root
    z = x / 2.0

    # Continuosly improve the guess
    # Adapted from https://tour.golang.org/flowcontrol/8
    while abs(x - (z*z)) > 0.00001:
        z -= (z*z - x) / (2 * z)

    # Return is the end of the sqrt function
    return z

# Prints sqrt function to screen
myval = -63.0
print("The sqaure root of", myval,"is", sqrt(myval))


