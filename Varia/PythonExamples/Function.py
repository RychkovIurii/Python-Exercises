"""
To create a function, you use the "DEFINE" keyword: `def` + 'function name' + '()' + ':'
The 'def' keyword is followed by the function name, then parentheses "()" containing "arguments."
After the parentheses, add a colon ":" to begin the "block" that holds the function's instructions.
Indentation is crucial; everything indented under the function block belongs to the function.
"""

def myFunction():  # Function declaration
    print("This is a print statement inside the function.")  # Print statement within the function

myFunction()  # Calling the function

"""
After declaring the function "myFunction," we added a print statement inside it.
We then called the function using its name, "myFunction()," and the parentheses can hold "arguments,"
which are then sent to the function.
"""

def myFunction2(arg):  # Function declaration with ONE "argument"
    print(arg)  # Print the argument inside the function

myFunction2("Argument sent to print.")  # Calling the function with an ARGUMENT in string type

"""
In the following, we sent a "String"/str as an argument during the function call.
It is passed to the function and used within the "Print."

We can also use multiple arguments when defining a function.
"""

def myFunction3(arg1, arg2):  # Function declaration with 2 ARGUMENTS, 1 and 2
    print(arg1, arg2)  # Print the given Arguments, separated by a Comma

myFunction3("1st argument", "2nd argument")  # Calling the function with TWO string-type arguments separated by a Comma

"""
In the following call, we sent TWO arguments with a COMMA separating them.
The "myFunction3" has TWO arguments defined in brackets (arg1, arg2) to receive the arguments 
from the call myFunction3() on line 34. If we flip the two strings, the placements in the print 
will be reversed because when using multiple arguments, we provide them in the same order to 
the argument slots in the function as we send them during the call (1 -> 1st slot, 2 -> 2nd slot, etc.).
"""

# Default Argument
def myFunction4(name="User"):
    print("Hello, " + name + "!")
    print(f"Hello, {name}!")  # Two ways to insert variable values into a string

myFunction4()

# Default Argument: Provides a default value if an argument is not provided.
