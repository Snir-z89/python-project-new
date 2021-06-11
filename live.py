def welcome(name):
    return "Hello " + name + ", and welcome to the World of Games (WoG).\nHere you can find many cool games to play. \n"


def load_game():
    print("Please choose a game to play:\n1. Memory Game - a sequence of numbers will appear for 1 second and you "
          "have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS \n")


def get_game():
    game_num = int(input("Enter: 1- Memory Game, 2- Guess Game, 3- Currency Roulette: \n"))
    while game_num > 3 or game_num < 1:
        print("Please choose only a number between 1 and 3!")
        game_num = int(input("Enter: 1- Memory Game, 2- Guess Game, 3- Currency Roulette: \n"))
    return game_num


def difficulty_level():
    difficulty = int(input("Please choose game difficulty from 1 to 5: \n"))
    while difficulty > 5 or difficulty < 1:
        print("Please choose only a number between 1 and 5!")
        difficulty = int(input("Please choose game difficulty from 1 to 5: \n"))
    return difficulty
