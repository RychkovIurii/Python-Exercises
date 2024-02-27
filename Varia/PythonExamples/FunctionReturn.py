"""
One common method for exporting data from a function is using "return".
This allows the function to send data outside, to the point where the function was called.
"""

# Simple function with no arguments
def myFunction():
    return "Hello"  # The function returns the string "Hello"

print(myFunction())  # The function is called, and its return value is printed

# Using 'return' with multiple variables by separating them with a comma
def myFunction2():
    return "Hello", "This is the second return data"

print(myFunction2())  # The function is called, and both return values are printed

# An example demonstrating the use of 'return' to pass data between functions
def function1():
    x = 10  # Declaring a variable 'x' with a value of 10
    return x  # Returning the value to the caller

def function2():
    y = function1()  # Declaring variable 'y' with the value from function1
    print("Value of Y:", y)  # Printing the value of 'y' (result: 10)

function2()  # Calling function2, which also activates function1 since some data depends on the return value of function1
