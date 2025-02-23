import random

target = random.randint(1, 100)

def guess_number():

    guess = int(input("Guess a number between 1 and 100 (Press 0 to exit game) : "))

    if(guess == 0):
        print("You have exited the game!")
        return
    
    if(guess == target):
        print("You guessed correctly!")

    elif(100 > guess > target):
        print("You guessed too high!\nTry a lower number.")
        guess_number()

    elif(1 < guess < target):
        print("You guessed too low!\nTry a higher number.")
        guess_number()
    
    else:
        print("Invalid input!\nTry again.")
        guess_number()

guess_number()

print("Target Number was", target)