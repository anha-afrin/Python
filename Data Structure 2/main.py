my_tupple=("Mango", 3.4, 78, "W", 590)
print(my_tupple[0])
sets={11, 35, 9, 90, 23, "Anha", 5.6}
print(sets)
sets.add(300)
print(sets)
sets2={20, 40, 90, 11, "Apple", 7.6}
# Intersection of sets
sets3=sets.intersection(sets2)
print(sets3)
# Union of sets
sets4=sets.union(sets2)
print(sets4)
# Set diffrences
print(sets.difference(sets2))
# cemetrick defferences
print(sets.symmetric_difference(sets2))
print("Add")