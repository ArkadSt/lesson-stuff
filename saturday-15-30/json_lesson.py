import json


try:
    with open("config.json", "r", encoding="utf-8") as file:
        contents = file.read()
        config = json.loads(contents)
        print(config["version"])
        print(config["key"])
except FileNotFoundError:
    print ("No config.json found")
except json.decoder.JSONDecodeError:
    print ("Invalid JSON")


person = {
    "name": "Arkadi",
    "surname": "Statsenko",
    "phone": 55616630,
    "phone_contacts": {
        "бабушка": 555555,
        "сестра1": 666,
        "сестра2": 4
    }
}