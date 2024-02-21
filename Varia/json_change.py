import json

with open('dataJSON.json', 'r') as file:
    json_decoded = json.load(file)

y = {"pin":110096}
  
json_decoded.update(y)
with open('dataJSON.json', 'w') as file:
    json.dump(json_decoded, file)
#print(json.dumps(json_decoded))