# Try-Except Block
try:    # Try will attempt to complete the action if not possible 
    result = 10 / 0 # the Except block will be executed instead
except ZeroDivisionError: 
    print("Cannot divide by zero!")

"""
Try-Except Block: Catches and handles exceptions (errors) 
that may occur during code execution.
"""

try:
    # Code that might raise an exception
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2

except ValueError:
    print("Invalid input. Please enter a valid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print(f"Result: {result}") # If try succeeds Except blocks will be skipped and Else will be executed

finally:
    print("Execution complete, regardless of exceptions.")

"""
The try block attempts to get user input, convert it to integers, and perform division.
If a ValueError occurs (e.g., if the user enters a non-numeric value), the first except block is executed.
If a ZeroDivisionError occurs, the second except block is executed.
If no exception occurs, the else block is executed, and the result is printed.
The finally block is always executed, whether an exception occurred or not, for cleanup.
Error handling is crucial for writing robust programs that can gracefully handle unexpected situations, improving the overall reliability of your code.
"""