import functionLibrary

# Importing the second script as module to use functions
# We call the function with and argument "userInput"
userInput = str(input("Insert your Name: "))

functionLibrary.ThatFunction(userInput)

# Calling the function as a module "reference.functionName(argument)"


"""

from functionLibrary import *
userInput = str(input("Insert your Name: "))
ThatFunction(userInput)

"""