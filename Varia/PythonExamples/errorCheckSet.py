# Import the randint function from the random module
from random import randint

# Initialize an empty set called exampleSet
exampleSet = set()

# Define a function called errorHandler that takes a parameter x
def errorHandler(x):
    # Add the value of x to the exampleSet
    exampleSet.add(x)
    
    # Print the current contents of exampleSet
    print(exampleSet)

    # Check if all elements in exampleSet are truthy
    if all(exampleSet):
        print("Yeps")
    else:
        print("Not all Functions have returned correct Values")
        print("Nope")

# Define a function called Function1
def Function1():
    # Create a list y containing the strings "Hello" and "Goodbye"
    y = ["Hello", "Goodbye"]

    # Generate a random number x (0 or 1)
    x = randint(0, 1)
    print(x)

    # Select the string at index x from the list y and store it in the variable z
    z = y[x]

    # Check if z is equal to "Hello"
    if z == "Hello":
        # If true, call errorHandler with the function Function1 as an argument
        errorHandler(Function1)
    else:
        # If false, call errorHandler with False as an argument
        errorHandler(False)

# Call the Function1 to execute the code within it
Function1()
