#!/usr/bin/env python3

import random

# need to add information on the briscola suit
class player:
    def __init__(self, pl_id):
        self.player_id = pl_id
        self.pl_card = []
        self.game_leader = False
        self.pl_points = 0

    def draw_card(self, new_card):
        if len(self.pl_card) < 3:
            self.pl_card.append(new_card)
            return 1
        else:
            return 0

    def print_player(self):
        player_string = "Player_"+str(self.player_id)+" has "+str(self.pl_points)+" and "+str(len(self.pl_card))+" cards and they are:"
        print(player_string)
        for pl_card in self.pl_card:
            pl_card.print_card()

    def set_leader(self): self.game_leader = True

    def set_normal(self): self.game_leader = False

    def play_rnd_card(self):
        random.shuffle(self.pl_card)
        return self.pl_card.pop()
    
    # def play_respond(self, card):


    def count_cards(self):
        return len(self.pl_card)

    def add_points(self, points):
        self.pl_points += points

    def get_points(self):
        return self.pl_points
