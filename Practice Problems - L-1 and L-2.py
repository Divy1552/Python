# Q1.Write a program that calculates and prints the result of the expression on float inputs 'a','b' and 'c'.
#    Expression = (a^3 + b^2 - c) / (a - b + c)

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

exp = (a**3 + b**2 - c) / (a - b + c)

print("Expression = (a^3 + b^2 - c) / (a - b + c)")
print("Value of Expression : ", exp)

print('---------------------------------------------------------------------------------------------------------')

# Q2.Write a program that takes two integer inputs from the user and swaps their values.
#    Print the values before and after the swap.

a = int(input("a = ")) # Let a = 2
b = int(input("b = ")) # Let b = 3

print("Before swapping : a =", a,"b =", b)

a = a + b # Now a will become a + b = 5  # DSA
b = a - b # Now b will become (a + b) - b = a = 2
a = a - b # Now a will become (a + b) - a = b = 3

print("After swapping : a =", a,"b =", b)

print('---------------------------------------------------------------------------------------------------------')

# Q3.Write a program to compute the area 'A' of a circle given it's radius 'r'.
#    A = πr^2  (assume π = 3.14159)

π = 3.14159
r = float(input("r = "))
A = π*r**2
print("A = πr^2")
print("A =", A)

print('---------------------------------------------------------------------------------------------------------')

# Q4.Write a program that takes three integer inputs x,y and z.The program should:
#    a.Check if all three numbers are even using the modulo operator (%).
#      Based on the result,print either 'All numbers are Even.' or 'Not all numbers are Even.'
#    b.Check if x is the largest number using relational operators (>) and logical operators (and).
#      Based on the result,print either 'x is the largest number.' or 'x is not the largest number.'
#    c.Check if the sum of any two numbers equals the third.
#      Based on the result,print either 'Sum condition is met.' or 'Sum condition is not met.'

x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))

if(x % 2 == 0 and y % 2 == 0 and z % 2 == 0):
    print("All numbers are Even.")
else:
    print("Not all numbers are Even.")

if(x > y and x > z):
    print("x is the largest number.")
else:
    print("x is not the largest number.")

if(x + y == z or y + z == x or z + x == y):
    print("Sum condition is met.")
else:
    print("Sum condition is not met.")

print('---------------------------------------------------------------------------------------------------------')

# Q5.Write a program that takes a student's score (integer) as input and print their grades on the basis of
#       90+ : Grade A     80-89 : Grade B     70-79 : Grade C     60-69 : Grade D     Below 60 : Grade F 
                 
score = int(input("Enter your Marks : "))

if(0 <= score <= 100):

    if(score >= 90):
        print("You passed with Grade A.")
    elif(score >= 80):
        print("You passed with Grade B.")
    elif(score >= 70):
        print("You passed with Grade C.")
    elif(score >= 60):
        print("You passed with Grade D.")
    else:
        print("You failed with Grade F.")

else:
    print("Please enter a valid score.")