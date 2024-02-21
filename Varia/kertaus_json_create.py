import json

kertaus_json = {
    "Työelämässä toimiminen": "K5",
    "Matematiikka": "null",
    "Ohjelmointi": "H4",
    "Kyberturvallisuus": "H3",
    "Hyvinvointiteknologian käyttö": "null",
    "Ohjelmointi": "K5",
    "Taide ja luova ilmaisu": "T1",
    "ASPA": "T2",
    "Tietoverkkolaitteiden asennus": "K5"
}

with open('kertaus.json', 'w') as file:
    json.dump(kertaus_json, file, indent = 9)