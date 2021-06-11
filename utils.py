import os

scores_file_name = "Scores.txt"
bad_return_code = 400


def screen_cleaner():
    clear_screen = os.system('clear')
    return clear_screen
