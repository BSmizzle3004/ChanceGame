import random

def generate_random_number():
    return random.randint(1, 30)

def user_guess():
    user_num = int(input("Please enter a number between 1 and 30: "))
    if 0 <= user_num <= 30:
        print("number accepted")
        return user_num
    print("Invalid number")
    return -1

def user_amount():
    user_amount = int(input("Please enter your amount: "))
    if user_amount > 0:
        print("amount accepted")
        return user_amount
    print("Invalid amount")
    return -1

def user_bet_input(total):
    user_bet = int(input("Please enter your bet: "))
    if  0 < user_bet <= 10 and total >= user_bet:
        print("amount accepted")
        return user_bet
    print("Invalid amount")
    return -1

def is_even(number):
    return (number % 2 == 0)

def is_multiple_of_10(number):
    return (number % 10 == 0)

def is_prime(number):
    if number > 1:
        for i in range(2, int(number/2)+1):
            if (number % i) == 0:
                return False
            else:
                return True
            
    return False
        
def is_less_than_5(number):
    return (number < 5)



def main():
    user_total = user_amount()
    print("This is the number betting game")
    print("You will win different amounts based on your guess")
    
    while user_total > 0:

        random_number = generate_random_number()
        user_number = -1
        user_bet = -1
        multiplier = 1

        while user_number == -1:
            user_number = user_guess()
        while user_bet == -1:
            user_bet = user_bet_input(user_total)

        if is_even(user_number):
            multiplier = multiplier * 2
        if is_multiple_of_10(user_number):
            multiplier = multiplier * 3
        if is_prime(user_number):
            multiplier = multiplier * 5
        if is_less_than_5(user_number):
            multiplier = multiplier * 2
        
        if user_number == random_number:
            print("you win, your multiplier is: " + str(multiplier))
            user_total = user_total + (user_bet * multiplier)
        else:
            print("you lost, your multiplier is: 1")
            user_total = user_total - user_bet

        print("random number: " + str(random_number))

        print("your new total is: " + str(user_total))
            
main()