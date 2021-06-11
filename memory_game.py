import os
import time
import random
from live import difficulty_level
from score import add_score


def generate_sequence(diff):
    if int(diff) == 1:
        list_len = 2
    elif int(diff) == 2:
        list_len = 3
    elif int(diff) == 3:
        list_len = 4
    elif int(diff) == 4:
        list_len = 5
    else:
        list_len = 6
    my_list = random.sample(range(1, 101), list_len)
    print(my_list)
    return my_list


def get_list_from_user():
    user_list = [int(i) for i in input("Enter the numbers you saw: ").split()]
    return user_list


def play():
    diff = difficulty_level()
    my_list = generate_sequence(diff)
    time.sleep(1.5)
    clear_screen = os.system('clear')
    user_list = get_list_from_user()

    a = set(my_list)
    b = set(user_list)
    if a == b:
        print(True)
        add_score(diff)
    else:
        print(False)
