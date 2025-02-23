import random

characters = [chr(i) for i in range(33,127)]

def random_password(n,password = ""):

    if(len(password) == n):
        return password

    character = random.choice(characters)
    password += character

    return random_password(n,password)

print(random_password(8))