eng_est_sõnastik = {
    "dictator": "diktaator",
    "apple": "õun",
    "cucumber": "kurk",
    "general": "üldine / kindral"
}

sõna = input("Sisestage sõna: ")

try: 
    print("Eestikeelne tõlge on: " + eng_est_sõnastik[sõna])
except KeyError:
    print(f"'{sõna}' ei ole sõnastikus.")