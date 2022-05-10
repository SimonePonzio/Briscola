#!/usr/bin/env python3

import random
from briscola_cards import card
import logging

class player:
    def __init__(self, pl_id):
        self.player_id = pl_id
        self.briscola_card = 0
        self.pl_card = []
        self.game_leader = False
        self.pl_points = 0

    def read_briscola_card(self, briscola_card):
        self.briscola_card = briscola_card

    def draw_card(self, new_card):
        if len(self.pl_card) < 3:
            self.pl_card.append(new_card)
            return 1
        else:
            return 0

    def print_player(self):
        player_string = "Player_"+str(self.player_id)+" has "+str(self.pl_points)+" and "+str(len(self.pl_card))+" cards and they are:"
        logging.debug(player_string)
        for pl_card in self.pl_card:
            pl_card.print_card()

    def set_leader(self): self.game_leader = True

    def set_normal(self): self.game_leader = False

    def play_card(self, card_list):
        return self.play_rnd_card(card_list)

    def play_rnd_card(self, card_list):
        random.shuffle(self.pl_card)
        return self.pl_card.pop()

    def count_cards(self):
        return len(self.pl_card)

    def add_points(self, points):
        self.pl_points += points

    def get_points(self):
        return self.pl_points

class resp_player(player):
    
    def play_respond(self, card_list):
        # edit this: replace the content of this function with a proper response
        return self.play_rnd_card(card_list)
