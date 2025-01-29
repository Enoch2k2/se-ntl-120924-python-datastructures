

names = ["Bob", "Sam", "Sarah", "Mariah"]

names.append("Leah") # append (push) adds to the end of a list in python

# names.pop(0) # pop by default removes from the end of a list, can specify an index to remove that specific position in the list

# list comprehension, can make a clone / map / filter of a list

clone_of_names = [name for name in names] # clone of names
mapped_names = [name + "!" for name in names] # mapping the list by adding an exclamation mark at the end of the name
filtered_names = [name for name in names if len(name) > 3] # filtered list by adding an if statement at the end
filtered_and_mapped_lists = [name + "!" for name in names if len(name) > 3] # filteres out any name that has 3 or less characters, and adds an exclamation mark to the end of the name

# looping
# for element in names:
#   print(element)

# index = 0

# while index < len(names):
#   print(names[index])
#   index += 1

# persons = [{"name": "Bob", "age": 42}, {"name": "Leah", "age": 27}]

# for person in persons:
#   print(person["name"])

numbers = [1,2,3,4,5, 6,7,8,9,10]

if 5 in numbers:
  print("5 is in numbers")
else:
  print("5 is not in numbers")