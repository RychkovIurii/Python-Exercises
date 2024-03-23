import Functions   # Connect second file as a module
import os
import json

# Define current folder
current_path = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(current_path, "schedule_Rychkov.json")

name = str(input("What is your name? "))    # Take input from user
Functions.from_first_file_Function(name)    # Call the function from Functons.py

Functions.create_json(json_file_path)

# Read from JSON
Functions.read_json(json_file_path)

# Option to wipe JSON
while True:
    choose_option = input("\nChoose option for the JSON file: \n1: Wipe Data\n2: Add Data\n3: Read Data\n4: Exit\n")
    if choose_option == "1":
        Functions.wipe_json(json_file_path)
        print("JSON file wiped.\n")
    elif choose_option == "2":
        Functions.add_json(json_file_path)
    elif choose_option == "3":
        Functions.read_json(json_file_path)
    elif choose_option == "4":
        print("Thank you! Exiting...")
        break
    else:
        print("Incorrect input. Next time try to be more careful")

