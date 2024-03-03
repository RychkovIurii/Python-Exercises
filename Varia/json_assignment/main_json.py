import json
from create_wipe import create_json, wipe_json
import os

current_path = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(current_path, "data.json")

# Execute function from second file to create JSON
create_json(json_file_path) 

# Function to read information from JSON file
def read_json():
    try:
        with open(json_file_path, "r") as file:
            data = json.load(file)
            print("Information from JSON file:")
            print(data)
    except FileNotFoundError:
        print("JSON file not found.")

# Read information from JSON
read_json()

# Option to wipe JSON file
wipe_option = input("Do you want to wipe the JSON file? (yes/no): ")
if wipe_option.lower() == "yes":
    wipe_json(json_file_path)
    print("JSON file wiped.")
