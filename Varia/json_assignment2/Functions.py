import json

# Function to say Hello
def from_first_file_Function(user):
    print("This is Hello from the first file")
    print("Hello " + user)

# Function to create JSON
def create_json(file_path):
    schedule_json = {
    "Futsali": "Tuesday",
    "Padel": "Wednesday",
    "Ohjelmointi": "Monday",
    "Beer": "Friday",
    "Outdoor activities": "Sunday"
    }
    with open(file_path, 'w') as file:
        json.dump(schedule_json, file, indent = 9)

# Function to wipe JSON
def wipe_json(file_path):
    with open(file_path, "w") as file:
        file.truncate(0)

# Function to read from JSON
def read_json(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            print("Information from JSON file:")
            print(data)
    except FileNotFoundError:
        print("JSON file not found.")

# Function to get input for adding data
def getInput():
    key = input("Enter new task: ")
    value = input("Enter day: ")
    return key, value

# Function to add info to JSON
def add_json(file_path):
    try:
        while True:
            key, value = getInput()
            try:
                with open(file_path, 'r') as file:
                    existingData = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                existingData = {}

            # Update data with new input
            existingData[key] = value

            # Write updated data back to the file
            with open(file_path, 'w') as file:
                json.dump(existingData, file, indent=4)
            print("JSON file updated successfully.")

            # Ask if user wants to continue adding data
            userInput = input("Do you want to stop (yes/no(Enter)): ")
            if userInput.lower() in ("yes", "y"):
                break

    except FileNotFoundError:
        print("Error: JSON file not found.")
    except PermissionError:
        print("Error: Permission denied to write to JSON file.")
    except OSError as e:
        print(f"Error: {e.strerror} - {e.filename}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")