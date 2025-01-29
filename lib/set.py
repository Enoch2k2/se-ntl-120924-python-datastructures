# sets are non indexable, but mutable collections

names = { "Bob", "Sarah", "Leah", "Sam" }

names.add("Rodney") # adds to the set

names.remove("Rodney") # removes from the set

for name in names: # sets are iterable!
  print(name)
