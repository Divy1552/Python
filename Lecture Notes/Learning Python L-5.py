# Loops - Loops are used to execute a block of code repeatedly until a specific condition is met.
# Types of Loops - while Loop (Repeats a block of code) and for Loop (Iterates over a sequence)

# while Loops are used to execute a block of code repeatedly until a certain condition remains True
# while Condition: # while Loop executes Block of Code repeatedly until given Condition remains True
#   Block of Code  # This process of repeatedly executing a Block of Code is known as Iteration.

i = 1 # Iterator
while i <= 5:
    print(i)
    i += 1

print('---------------------------------------------------------------------------------------------------------')

# Practice Problems

# Print Multiplication Table of 7

i = 1
while i <= 10:
    print("7 X", i,"=", i*7)
    i += 1

print('---------------------------------------------------------------------------------------------------------')

# Break - Loop Control Statement used to terminate the loop's execution when a specific condition is met
# Continue - Loop Control Statement used to skip the current iteration and move on to the next iteration

# Search for 49 in Tuple

tuple = (1,4,9,16,25,36,49,64,81,100)
print("Tuple =", tuple)

i = 0

while i < 9:

    if(tuple[i] == 49):
        print("49 is found at Index Number", i)
        i += 1
        break
    else:
        print("Searching for 49 at Index Number", i)
        i += 1

print('---------------------------------------------------------------------------------------------------------')

# for Loops are used to iterate over a sequence (like a list,tuple,string,range or other iterable objects)
# for Element in List: # for Loop executes Block of Code repeatedly for each Element of the List (or Tuple)
#   Block of Code      # else statement is used with for Loop to execute Ending Code at the end of the Loop

str = "Hello"

for i in str:
    print(i)
else:
    print("☺")

print('---------------------------------------------------------------------------------------------------------')

# Range - range(Start* - 0,Stop,Step* - 1 | Default*) is a built-in function that generates a Sequence of Numbers

for i in range(1,6): # range(1,6) generates a Sequence of Numbers from 1 to 5
    print(i)         # Note - Stoping Number is not included in the range() function
else:
    print('-----------------------------------------------------------------------------------------------------')

list = list(range(2,10,2)) # Start - 2,Stop - 10,Step - 2 generates a Sequence of first four Even Numbers

print("List of first four Even Numbers :", list) 

# Pass - "pass" is a null statement that does nothing.It is used as a placeholder for future code.

for i in list:
    pass

print('---------------------------------------------------------------------------------------------------------')

# Practice Problems

# Write a Program to find the factorial of a number n given by user.

n = int(input("n = "))

factorial = 1

for i in range(1,n+1):
    factorial *= i

print("n! =", factorial)