# Escape Sequence Characters - These are special characters used to give formatting to the string.

str1 = "This is a string.\tWe are creating this in Python."
print(str1) # Here \t is a Escape Sequence Character which gives Tab formatting to the string.
str2 = "This is a string.\nWe are creating this in Python."
print(str2) # Here \n is a Escape Sequence Character which gives Next Line formatting to the string.

# Concatenation - Combination of two Strings.For example - "Hello" + "World" = "HelloWorld"

str1 = "My name is Divy Bahetra."
str2 = "I am studying at IIT (BHU) Varanasi."
str = str1 + str2 # Concatenation of str1 and str2.
print(str) # Note : There is no space between two strings during Concatenation.
print("Length of the string :", len(str)) # We can calculate length of string using len function.
str = str1 + " " + str2 # We can also add space between two strings using Concatenation.

# Indexing - Accessing a specific element in a string.Index Numbers are assigned from 0 to len(str) - 1.

str = "Apna_College" # Index Numbers - A(0) p(1) n(2) a(3) _(4) C(5) o(6) l(7) l(8) e(9) g(10) e(11)
print("String =", str,"\n6th element :", str[5]) # We can do Indexing using str[Index Number].
# str[5] = "a" # We cannot change the element by assigning another element in it's position.

# Slicing - Accessing part of a string. # str[start:end] access string from start to end (excluded).

print("String from 2nd element to 4th element :", str[1:4]) # access string "pna"
print("String from 1st element to 4th element :", str[0:4]) # or print(str[:4])
print("String from 6th element to last element :", str[5:len(str)]) # or print(str[5:])
# We can also do negative indexing in Python where Index Number -1 refers to the last element.
print("String from 1st element to 3rd element (negative indexing) :", str[:-9])

# String Functions

str = "i am studying Python from Apna College."
print("String = ", str)
print("String ends with 'ege.' :", str.endswith("ege.")) # gives True
print("Capitalized String :", str.capitalize()) # gives capitalized string
print("Replace Python with C++ :", str.replace("Python","C++")) # replaces Python with C++
print("Index Number of 'P' in 'Python' :", str.find("Python")) # gives 14
print("Number of times 'm' arrives in String :", str.count("m")) # gives 2

# Conditional Statements - if..elif..else Statements

# if(Condition 1): # If Condition 1 is True Statement 1 is implemented.
#   Statement 1 # or If Condition 1 is False Condition 2 is checked.
# elif(Condition 2): # Now if Condition 2 is True Statement 2 is implemented.
#   Statement 2 # or If Condition 2 is False Condition 3 is checked.
# .
# .
# .
# elif(Condition n): # Now if Condition n is True Statement n is implemented.
#   Statement n # or If Condition n is False Final Statement is implemented.
# else:
#   Final Statement

TrafficLight = "Green"
print("Traffic Light :", TrafficLight)

if(TrafficLight == "Red"): # Check if Traffic Light is Red
    print("Command : Stop!")
elif(TrafficLight == "Yellow"): # Check if Traffic Light is Yellow
    print("Command : Wait!")
elif(TrafficLight == "Green"): # Check if Traffic Light is Green
    print("Command : Go!")
else: # Do not checks any condition.
    print("Traffic Light is broken.") 

# Indentation - Use of spaces or tabs at the beginning of a line of code to indicate a code block.

n = 6
print("n =",n)

if(n > 3): # Checks if n is greater than 3
    print("n is greater than 3.")
if(n > 4): # Checks if n is greater than 4
    print("n is greater than 4.")

# Nesting - Placing one construct inside other.For example,if statement inside another if statement.

age = 23
print("age =",age)

if(age >= 18):

    if(age >= 25):
        print("Eligible for driving both Motorcycle and Car.")
    else:
        print("Eligible for driving Motorcycle only.")

else:
    print("Ineligible for driving.")