import random
from live import difficulty_level
from score import add_score


def generate_number(diff):
    if int(diff) == 1:
        upper_limit = 3
    elif int(diff) == 2:
        upper_limit = 5
    elif int(diff) == 3:
        upper_limit = 10
    elif int(diff) == 4:
        upper_limit = 15
    else:
        upper_limit = 20
    secret_number = int(random.randint(1, upper_limit))
    return secret_number


def get_guess(diff):
    limit = 0
    if int(diff) == 1:
        limit = 3
    elif int(diff) == 2:
        limit = 5
    elif int(diff) == 3:
        limit = 10
    elif int(diff) == 4:
        limit = 15
    else:
        limit = 20
    guess = int(input("Guess a number between 1 and " + str(limit) + ": \n"))

    while guess > limit or guess < 1:
        print("Wrong value! Guess only a number between 1 and " + str(limit) + "!\n")
        guess = int(input("Guess a number between 1 and " + str(limit) + ": \n"))
        continue
    return guess


def play():
    diff = difficulty_level()
    secret_num = generate_number(diff)
    user_guess = get_guess(diff)

    if user_guess != secret_num:
        print("Wrong! The secret number was: " + str(secret_num))
    else:
        print("Good job!")
        add_score(diff)
