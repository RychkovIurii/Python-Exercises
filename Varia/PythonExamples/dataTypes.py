# Strings
text = "Hello, World!"

# Integers
number = 42

# Floats
pi = 3.14

# Booleans
isTrue = True
isFalse = False

# Explicit Type Casting Examples

# Integer to Float
x = float(10)
print(f"x as a float: {x}")

# Float to Integer
y = int(3.14)
print(f"y as an integer: {y}")

# Integer to String
a = str(42)
print(f"a as a string: {a}")

# String to Integer
b = int("123")
print(f"b as an integer: {b}")

# String to Float
c = float("3.14")
print(f"c as a float: {c}")

# Boolean to Integer
is_valid = True
d = int(is_valid)
print(f"d as an integer: {d}")

"""
float(10): Converts the integer 10 to a float.
int(3.14): Converts the float 3.14 to an integer (truncating the decimal part).
str(42): Converts the integer 42 to a string.
int("123"): Converts the string "123" to an integer.
float("3.14"): Converts the string "3.14" to a float.
int(True): Converts the boolean True to an integer (1 for True, 0 for False).
These examples demonstrate explicit type casting using constructor functions (int(), float(), str()) to convert values from one data type to another.

Strings: Sequences of characters.
Integers: Whole numbers.
Floats: Numbers with decimal points.
Booleans: Represent either True or False values.
"""