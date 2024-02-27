# Lists
fruits = ["apple", "banana", "orange"]

# Nested Lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing List Elements
print(fruits[0])  # Output: apple

# Modifying List Elements
fruits[1] = "grape"

# Adding Elements to the List
fruits.append("kiwi")

# Removing Elements from the List
removedFruit = fruits.pop(2)  # Removes the element at index 2
print("Removed Fruit:", removedFruit)

# Looping Through a List
for fruit in fruits:
    print(fruit)

# Using Range to Access Indices
for i in range(len(fruits)):
    print("Index:", i, " - Fruit:", fruits[i])

# Nested List Iteration
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

"""
Accessing List Elements: Indexing starts from 0.
Modifying List Elements: Lists are mutable, and elements can be changed.
Adding Elements to the List: append() adds an element to the end of the list.
Removing Elements from the List: pop() removes and returns an element at the specified index.
Looping Through a List: Iterating through each element in the list.
Using Range to Access Indices: Using range() to generate indices for list access.
"""