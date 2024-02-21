import json

dataJSON = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

with open('dataJSON.json', 'w') as file:
    json.dump(dataJSON, file, indent = 4)