#!/usr/bin/env python3

import random
from briscola_game import game2player

# relevant informarmations:
# - Briscola Suit are the card with a powerful seed
# - dealer is the player responsable to distrubute cards at the beginnig of each turn the person after the dealer is the first to play in each game, so the dealer is the last player to play
#   each turn
# - the player who leads the game is the one who won the last game, he is the first two draw as well

def main():
    new_game = game2player()
    new_game.setup_game()
    new_game.run_game()

if __name__ == '__main__': main()