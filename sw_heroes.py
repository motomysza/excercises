import json
with open("py1.2.json") as file:
    new_data = json.load(file)
heros = open("sw_all_heros", "w")

for element in new_data:
    single_sentence = element["name"]
    if element["mass"] != "unknown":
        single_sentence += " waży " + element["mass"] + " kg"
    if element["gender"] == "female":
        single_sentence += " jest dziewczyną"
    elif element["gender"] == "male":
        single_sentence += " jest mężczyzną"
    if element["homeworld"] != "unknown":
        single_sentence += " i pochodzi z " + element["homeworld"]
    single_sentence += ".\n"
    heros.writelines(single_sentence)

file.close()
heros.close()
