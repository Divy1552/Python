# Function - Function is a Block of Code that performs a specific task.For example - sum(a,b) gives result a+b

# def function_name(Parameter 1,Parameter 2,...): # Function Definition
#     Block of Code
#     return Value

# print(function_name(Argument 1,Argument 2,...)) # Function Call

def sum(a,b):
    sum = a + b
    return sum

print("Sum of 3 and 5 :", sum(3,5))

# Types of Functions - There are two types of Functions : Built-in Functions and User Defined Functions

print("My name is Divy Bahetra.","I am 18 years old",sep = "",end = ".\n") # sep* = " " and end* = "\n"

# Default Parameter - Default Value assigned to a Parameter which is used in absence of corresponding Argument. 

def average(a,b=6):
    average = (a + b)/2
    return average

print("Average of 4 and 5 :", average(4,5))
print("Average of 4 and 6 :", average(4))

print('---------------------------------------------------------------------------------------------------------')

# Practice Problems

# Write a Function to print the length of a List.

def len(list):

    len = 0
    for i in list:
        len += 1

    print("Length of the List :", len)

List = [1,2,"Apple",6.78]
print("List =", List)
len(List)

print('---------------------------------------------------------------------------------------------------------')

# Write a Function to convert USD to INR.

def USD_to_INR(USD):
    INR = 85.26 * USD
    return INR

USD = 100 # We can also take input() here.
print("USD =", USD,"INR =", USD_to_INR(USD))

print('---------------------------------------------------------------------------------------------------------')

# Recursion - Programming Technique where a Function calls itself repeatedly until a certain condition is met.

def show(n): # Recursive Function

    if(n == 0): # Base Case
        return
    print(n) # Main Task
    show(n-1) # Recursive Case

show(5) # Recursive Function Call

print('---------------------------------------------------------------------------------------------------------')

# Practice Problems

# Write a Recursive Function to find the factorial of n.

def factorial(n):

    if(n < 0):
        return
    elif(n == 0):
        return 1
    else:
        return n * factorial(n-1)
    
print("Factorial of 5 :", factorial(5))

print('---------------------------------------------------------------------------------------------------------')

# Write a Recursive Function to calculate the sum of first n Natural Numbers.

def Sum_of_Natural_Numbers(n):

    if(n <= 0):
        return
    elif(n == 1):
        return 1
    else:
        return sum(n,Sum_of_Natural_Numbers(n-1))
    
print("Sum of first 7 Natural Numbers :", Sum_of_Natural_Numbers(7))