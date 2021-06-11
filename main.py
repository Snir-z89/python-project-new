import live
import guess_game
import memory_game
import currency_roulette_game

print(live.welcome("Guy"))
live.load_game()

chosen_game = live.get_game()
if chosen_game == 1:
    memory_game.play()
elif chosen_game == 2:
    guess_game.play()
else:
    currency_roulette_game.play()

