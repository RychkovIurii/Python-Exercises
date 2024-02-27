"""
Comparison are used to indentify moments in the code when an action
must be executed or stopped etc.
most common comparison's are:  ==  !=  <  <=  >  >=
you always have data that is compared against other data
most common logic is "if  elif  else  and  or  not"
"""

# If Statement
x = 10

if x > 5:
    print("x is greater than 5")

# If-Else Statement
y = 3

if y > 5:
    print("y is greater than 5")
else:
    print("y is not greater than 5")

# If-Elif-Else Statement
z = 7

if z > 10:
    print("z is greater than 10")
elif z == 7:
    print("z is equal to 7")
else:
    print("z is less than 10 and not equal to 7")

# Not, And, Or
a = True
b = False

if not b:
    print("b is not true")

if a and b:
    print("both a and b are true")
else:
    print("at least one of a or b is false")

if a or b:
    print("at least one of a or b is true")
else:
    print("both a and b are false")


"""
If Statement: Executes a block of code if a condition is true.
If-Else Statement: Executes one block of code if the condition is true, another if false.
If-Elif-Else Statement: Handles multiple conditions.
Not: Reverses the result of a condition.
And: Returns True if both conditions are true.
Or: Returns True if at least one condition is true.
"""