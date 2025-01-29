# dictionaries are our javascript objects!
# dictionaries you cannot use dot notation, only bracket
# keys must be strings unless you are wanting to use a variable for the key


# key = "name"
# value = "Bob"

# person = {"key": value}

# person = {
#   "name": "Bob",
#   "age": 32,
#   "job": "Works as a hand model",
#   "loves": "saving money at walmart"
# }

# def describe():
#   print(f'{person["name"]} is {person["age"]} years old. Job is {person["job"]} and loves {person["loves"]}!')

# person["describe"] = describe

# print(person)

person = {
  "name": "Bob",
  "age": 32,
  "description": "Tall and majestic"
}

# list_of_keys = [f"{key} is {person[key]}" for key in person.keys()if key != "age"]

# for property in list_of_keys:
#   print(property)

# if "location" in person.keys():
#   print("dictionary has a name key")