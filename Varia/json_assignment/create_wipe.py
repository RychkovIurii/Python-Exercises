import json

# Function to create JSON file with information
def create_json(file_path):
    data = {
         "Ty\u00f6el\u00e4m\u00e4ss\u00e4 toimiminen": "K5",
         "Matematiikka": "null",
         "Ohjelmointi": "K5",
         "Kyberturvallisuus": "H3",
         "Hyvinvointiteknologian k\u00e4ytt\u00f6": "null",
         "Taide ja luova ilmaisu": "T1",
         "ASPA": "T2",
         "Tietoverkkolaitteiden asennus": "K5"
}
    with open(file_path, "w") as file:
        json.dump(data, file)
    print("JSON file created.")

# Function to wipe JSON file
def wipe_json(file_path):
    with open(file_path, "w") as file:
        file.truncate(0)
