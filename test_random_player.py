#!/usr/bin/env python3

import random
from briscola_game import game2player

# too many print from the run_game function. Need to make the verbosity settable.

def main():
    game_nr = 0
    win_pl1 = 0
    win_pl0 = 0
    while game_nr < 100:
        new_game = game2player()
        new_game.setup_game()
        winning_pl_id = new_game.run_game()
        if winning_pl_id:
            win_pl1 += 1
        else:
            win_pl0 += 1
        game_nr += 1
    print("win0: "+str(win_pl0)+" win1: "+str(win_pl1))

if __name__ == '__main__': main()