

import random

def generate_random_number():
    return random.randint(0, 30)

def user_guess():
    user_num = int(input("Please enter a number between 1 and 30"))
    if 0 <= user_num <= 30:
        print("number accepted")
        if user_num == random_number:
            print("congratulations you won")
        else:
            print("Oooh unlucky, the number was" + random_number)
        

def main():
    print("This is the number betting game")
    print("You will win different amounts based on your guess")

random_number = generate_random_number()


