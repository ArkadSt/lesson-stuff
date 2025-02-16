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


