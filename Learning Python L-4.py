# Dictionary - A built-in datatype that stores data values in key:value pairs.For example - {key : value}

info = {"Name" : "Divy Bahetra","Marks" : [67,56,72],"CPI" : 9.78} # Each pair is seperated by a comma (,)
print("Student's Information :", info) # We can store almost all datatypes as values in a Dictionary.
print(type(info)) # Note - We can only use immutable(unchangeable) datatypes as keys in a Dictionary.

# Dictionaries are unordered and mutable(changeable). # Dictionaries do not allow to use duplicate keys.

print("Student's Name :", info["Name"]) # We can access any value of Dictionary using dict_name(key).
info["CPI"] = 8.96 # We can change any value by assigning another value in it's key in a Dictionary.
print("Student's Information : Name -", info["Name"],"Marks -", info["Marks"],"CPI -", info["CPI"])
info["Town"] = "Rewa" # We can add another pair in a Dictionary by assigning some value to a new key.
print("Student's Information : Name -", info["Name"],"Town -", info["Town"],"CPI -", info["CPI"])

info = {"Name" : "Divy Bahetra","Marks" : {"PHY" : 52,"CY" : 66,"MA" : 47}} # Nested Dictionary
print("Marks : PHY -", info["Marks"]["PHY"],"CY -", info["Marks"]["CY"],"MA -", info["Marks"]["MA"])

# Dictionary Functions

print(list(info.keys())) # dict_name.keys() returns all outer Keys as dict_keys([Keys])
print(list(info.values())) # dict_name.values() returns all values as dict_values([Values])
print(list(info.items())) # dict_name.items() returns all (key,value) pairs as dict_items([(Key,Value)])
print("Name -", info.get("Name")) # dict_name.get(Key) returns the value according to the key
info.update({"Town" : "Rewa"}) # dict_name.update(New_Dict) updates Dictionary with pairs from New_Dict
print("Student's Information : Name -", info["Name"],"Marks -", info["Marks"],"Town -", info["Town"])

print('---------------------------------------------------------------------------------------------------------')

# Set - Set is an unordered collection of unique and immutable elements.For example - {1,2,3}

Num = {1,2,3,4,5} # Set of first five Natural Numbers # Set = {1,2,2} is same as Set = {1,2}
print("First five Natural Numbers :", Num) # Duplicate elements are always ignored in a Set.
print(type(Num)) # We can also get length of a Set using len(Set). # len({1,2,2,3,4}) gives 4
Empty_Set = set() # Empty Set # Note - {} is considered an empty dictionary not an empty set.

# Set Functions


Num.add(6) # Set.add(Element) adds an Element in a Set
print("First six Natural Numbers :", Num)
Num.remove(1) # Set.remove(Element) removes an Element from the Set
print("Integers between 2 to 6 :", Num)
Num.clear() # Set.clear() clears/removes all Elements from the Set
print("Empty Set :", Num)

fruits = {"Apple","Orange","Mango","Banana"}
print("Fruits =", fruits)
print("Favourite Fruit :", fruits.pop()) # Set.pop() gives a random element from the Set
print("Remaining Fruits :", fruits) # Set.pop() also removes a random element from the Set

set1 = {1,2,3}
print("Set 1 =", set1)
set2 = {3,4,5}
print("Set 2 =", set2)

union = set1.union(set2) # set1.union(set2) returns union of two sets
print("Union of the two Sets :", union)

intersection = set1.intersection(set2) # set1.intersection(set2) returns intersection of two sets
print("Intersection of the two Sets :", intersection)