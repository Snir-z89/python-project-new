from forex_python.converter import CurrencyRates
from live import difficulty_level
from score import add_score
import random


def get_exchange():
    c = CurrencyRates()
    get_exchange_rate = c.get_rate('USD', 'ILS')
    return get_exchange_rate


def generate_number():
    generated_num = int(random.randint(1, 100))
    print("The amount in USD is " + str(generated_num) + ", How much do you think it is in ILS???")
    return generated_num


def get_guess_from_user():
    guess = input("Write your guess below: \n")
    return guess


def play():
    diff = difficulty_level()
    get_exchange_rate = get_exchange()
    generated_num = generate_number()
    guess = get_guess_from_user()

    max_interval = int(((generated_num * get_exchange_rate) + (5-diff)))
    min_interval = int(((generated_num * get_exchange_rate) - (5-diff)))

    if min_interval <= int(guess) <= max_interval:
        print(True)
        add_score(diff)
    else:
        print(False)
