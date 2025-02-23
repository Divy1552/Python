# List - A built-in datatype that stores set of values.For example - [23,45,46,29,67]

marks = [34,56,78,93,21] # All these values are now stored in a single variable.
print("Marks List :", marks) # Properties of Lists are very similar to those of strings.
print(type(marks))
print("Marks of Student :", marks[2]) # We can access any element of List using it's Index Number.

Student = ["Divy Bahetra",78,7.54] # We can also store element of different datatypes in a single List.
print("Student Details : Name -", Student[0],"Marks -", Student[1],"CPI -", Student[2])

# Difference between Strings and Lists - Strings are immutable while Lists are mutable in Python.

Student[2] = 9.11 # We can change any element by assigning another element in it's position in List.
print("Student Details : Name -", Student[0],"Marks -", Student[1],"CPI -", Student[2])

# List Slicing - Similar to String Slicing # list_name[start:end] access List from start to end (excluded).

print("Marks and CPI of Student :", Student[1:3]) # or print(Student[1:])

# List Functions

list = [2,1,3]
print("List =", list)
list.append(4) # list_name.append(X) adds an element X to the end of the List
print("List =", list)
list.insert(1,5) # list_name.insert(Index Number,Y) inserts an element Y at that Index Number of the List
print("List =", list)
list.reverse() # list_name.reverse() reverses List
print("List =", list)
list.sort() # list_name.sort() sorts List in ascending order
print("List =", list)
list.sort(reverse = True) # list_name.sort(reverse = True) sorts List in descending order
print("List =", list)
list = [2,1,3,1]
print("List =", list)
list.remove(1) # list_name.remove(Z) removes the first occurrence of an element Z from the List
print("List =", list)
list.pop(1) # list_name.pop(Index Number) removes an element from that Index Number of the List
print("List =", list)

print('---------------------------------------------------------------------------------------------------------')

# Tuple - A built-in datatype that stores an immutable set of values.For example - (24,56,23,78,95)

tuple = (4,5,2,7) # Properties of Tuples are very similar to those of strings.
print("Tuple =", tuple)
print(type(tuple))

print("2nd element of Tuple :", tuple[1]) # We can access any element of Tuple using it's Index Number.
# tuple[2] = 9 # We cannot change any element by assigning another element in it's position in Tuple.

tuple = () # Empty Tuple
print("Tuple =", tuple)
tuple = (1,) # Tuple with a single element 
print("Tuple =", tuple) # Note - We need to add a comma (,) at the end of the element.
tuple = (1) # This is considered an integer.
print(type(tuple))

# Tuple Slicing - Similar to String Slicing # tuple_name[start:end] access Tuple from start to end (excluded).

tuple = (3,4,6,9)
print("Tuple =", tuple)
print("Last 2 elements of Tuple :", tuple[2:4]) # or print(tuple[2:])

# Tuple Functions

tuple = (4,5,7,5,9)
print("Tuple =", tuple)
print(tuple.index(7)) # tuple_name.index(Element) returns Index Number of first occurence of that Element
print(tuple.count(5)) # tuple_name.count(Element) counts total occurrences of that Element in the Tuple