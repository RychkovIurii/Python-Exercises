
thisDict = { # Making a dictionary with 3 items, and 3 values
    "police": "an Officer of the law",
    "motorcycle": "a Motorized bike with 2 wheels",
    "car": "a Vehicle with 4 wheels"
}

word = input("Search Name: ") # Input to search in the dictionary
word = word.lower() # Converting to lowercase, because the dictionary is case sensitive
if word in thisDict: # Going through the Dictionary to find a possible match
    print(thisDict[word]) # Using the Dictionary with a string index to pring the value of the item
else:
    print("Name not found") # If nothing found "Name not found"











# for x in thisDict:
#     print(x)
# print("\n")

# for x in thisDict:
#     print(thisDict[x])
# print("\n")

# for x, y in thisDict.items():
#   print(x, y)