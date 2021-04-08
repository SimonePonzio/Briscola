#!/usr/bin/env python3

import random
import argparse
import logging
from briscola_game import game2player

# relevant informarmations:
# - Briscola Suit are the card with a powerful seed
# - dealer is the player responsable to distrubute cards at the beginnig of each turn the person after the dealer is the first to play in each game, so the dealer is the last player to play
#   each turn
# - the player who leads the game is the one who won the last game, he is the first two draw as well

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d', '--debug',
        help="Print lots of debugging statements",
        action="store_const", dest="loglevel", const=logging.DEBUG,
        default=logging.WARNING,
    )
    parser.add_argument(
        '-v', '--verbose',
        help="Be verbose",
        action="store_const", dest="loglevel", const=logging.INFO,
    )
    args = parser.parse_args()    
    logging.basicConfig(level=args.loglevel)
    
    # run the game
    new_game = game2player()
    new_game.setup_game()
    new_game.run_game()

if __name__ == '__main__': main()