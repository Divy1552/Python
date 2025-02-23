print("Hello World!")
# Anything written inside print("-----") will simply print ----- as a string. 
print("My name is Divy Bahetra.")
print("I am 18 years old.")
# You can also print your name,age or anything else.
print("My name is Divy Bahetra.","I am 18 years old.")
# If we use a comma (,) after one string and write another string,it will appear on the same line in the output.

print("23")
print(23)
# Writing print("23") prints '23' as a string while print(23) gives 23 as an integer.
# They both seem to behave the same way but behave differently when we perform mathematical operations. 
print("23 + 27")
print(23 + 27)
# Writing print("23 + 27") prints '23 + 27' as a string while print(23 + 27) gives 50 (= 23 + 27) as an integer.
# In Python,we can perform simple mathematical operations like +,-,*,/,%,etc. in our projects. 

Name = "Divy Bahetra" # String Variable
age = 18 # Integer Variable
score = 98.38 # Float Variable

print("My name is", Name) # To insert a variable,write the variable name without quotation marks ("").
print("I am", age,"years old") # Integer/Float Variables can be used in mathematical operations.
print("I scored", score,"percentile in JEE Mains 2024") # Variables simply output their values.
# Identifiers (Variable Names) can be a combination of uppercase and lowercase letters,digits or an underscore (_).
# An Identifier cannot start with a digit.So while Variable1 is valid,1Variable is not valid.
# We can't use special symbols like !,@,#,$,%,etc. in Identifiers. # Identifiers can be of any length.

print(type(Name))
print(type(age))
print(type(score))
# Writing print(type(Variable)) provides the datatype of the Variable.
# There are many datatypes in Python.But we need to study only 5 primary datatypes.
# Primary Datatypes - String (str),Integer (int),Float (float),Boolean (bool),None (NoneType)

boolean = True # Contains True or False values.
none = None # Contains None value.

print(type(boolean))
print(type(none))
print("Earth is Round :", boolean)
print("Choose Tea or Coffee :", none)

# Keywords - Reserved words in Python like True,False,None,if,else,and,etc. are some examples of Keywords.
# These Keywords cannot be used as Identifiers(Variable Names) but can be used as a strings.
# Python is a case-sensitive programming language,i.e.,Apple and apple are considered different variables.

a = 6
print("a =", a)
b = 4
print("b =", b)

sum = a + b
difference = a - b 
multiply = a * b
divide = a / b

print("Sum of a and b :", sum) # or print(a + b)
print("Difference of a and b :", difference) # or print(a - b)
print("Multiplication of a and b :", multiply) # or print(a * b)
print("Division of a and b :", divide) # or print(a / b)

# Comments - Lines or Paragraphs that are not executed in the program.
# Single-Line Comment - HashTag (#) Multi-Line Comments - Triple Quotes ("""-----""")

# Operators - Special characters that perform an operation between operands such as +,-,*,/,%,etc.
# Types of Operators - Arithmetic Operators,Relational/Comparison Operators,Assignment Operators,Logical Operators

# Arithmetic Operators - Addition (+),Subtraction (-),Multiplication (*),Division (/),Modulo (%),Power (**),etc.

print("Remainder left when a is divided by b :", a % b) # Modulo Operator (%) gives the remainder of a / b
print("a raised to the power b :", a ** b) # Power Operator (**) gives the value of a raised to the power b (a^b)

# Relational Operators - Equal to (==),Not equal to (!=),Greater than (>),Less than (<),etc.

print("a is equal to b :", a == b) # False as a is not equal to b
print("a is not equal to b :", a != b) # True as a is not equal to b
# Relational Operators always return a Boolean value as they define a condition between operands.
print("a is greater than b :", a > b) # True as a is greater than b (a > b)
print("a is less than b :", a < b) # False as a is greater than b (a > b)
print("a is greater than or equal to b :", a >= b) # True as a is greater than b (a > b)
print("a is less than or equal to b :", a <= b) # False as a is greater than b (a > b)

# Assignment Operators - Basic Assignment Operator (=),Addition/Subtraction Assignment Operator (+=/-=),etc.

c = 5 # Using the Basic Assignment Operator (=) we assign right side value (5) to the left side variable (c).
print("c =", c)
c += 7 # Using the Addition Assignment Operator (+=) we assign the value c + 7 to the variable (c).
print("c + 7 =", c)
c = 5 # We again assign right side value (5) to the variable (c).
c -= 4 # Using the Subtraction Assignment Operator (-=) we assign the value c - 4 to the variable (c).
print("c - 4 =", c)
c = 5 # We again assign right side value (5) to the variable (c).
c *= 6 # Using the Multiplication Assignment Operator (*=) we assign the value c * 6 to the variable (c).
print("c * 6 =", c)
c = 5 # We again assign right side value (5) to the variable (c).
c /= 3 # Using the Division Assignment Operator (*=) we assign the value c / 3 to the variable (c).
print("c / 3 =", c)
# Similarly,we can use Modulo Assignment Operator (%=) and Power Assignment Operator (**=).

# Logical Operators - AND Operator (and),OR Operator (or),NOT Operator (not) # returns a Boolean value.

d = 50
print("d =", d)
e = 30
print("e =", e)

val_1 = d > e # True as d > e
val_2 = d < e # False as d > e
val_3 = d == e # False as d is not equal to e
val_4 = d != e # True as d is not equal to e

# AND Operator returns True only if all operands are True otherwise it returns False.
print("d > e and d = e :", val_1 and val_3) # False as val_1 is True but val_3 is False
print("d > e and d is not equal to e :", val_1 and val_4) # True as both val_1 and val_4 are True
# OR Operator returns False only if all operands are False otherwise it returns True.
print("d > e or d = e :", val_1 or val_3) # True as val_1 is True
print("d < e or d = e :", val_2 or val_3) # False as both val_2 and val_3 are False
# NOT Operator returns the opposite value of the operand.
print("not d > e :", not val_1) # False as val_1 is True

# Type Conversion - Converting one datatype into another datatype.
# Types of Type Conversions - Type Conversion (automatic) and Type Casting (manual)

a = 3 # Integer Value
print("a =", a)
print(type(a))

b = 4.59 # Float Value
print("b =", b)
print(type(b))

c = "7" # String Value
print("c =", c)
print(type(c))

# Type Conversion in Integer Value + Float Value is possible and the result is a Float Value.
print("a + b =", a + b)
# Type Conversions in Integer Value + String Value and Float Value + String Value are not possible.
# But we can manually convert String Value (c) into Integer Value or Float Value using Type Casting.
# Type Casting only works if the value is convertible from one datatype to another datatype.

int_c = int(c) # Converting String Value into Integer Value using Type Casting
print("int(c) =", int_c)
print(type(int_c))

float_c = float(c) # Converting String Value into Float Value using Type Casting
print("float(c) =", float_c)
print(type(float_c))

# Now,String Value (c) has been converted into an Integer Value (int_c) and Float Value (float_c).
print("a + float(c) =", a + float_c) # Integer Value + Float Value = Float Value
print("b + int(c) =", b + int_c) # Float Value + Integer Value = Float Value

# INPUT - Input statement is used to accept values from the user.
# Result for Input statement is always a string. # Input statement - input()

Username = input("Enter your Username : ") # We can include a message inside input() to prompt the user.

print("Welcome", Username)