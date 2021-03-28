#!/usr/bin/env python3

import random

SEEDS = ("swords", "clubs", "cups", "coins")
RANKS =({'ID': 1 , 'name': "ACE"  , 'rank': 9, 'points': 11},
        {'ID': 2 , 'name': "TWO"  , 'rank': 0, 'points': 0},
        {'ID': 3 , 'name': "THREE", 'rank': 8, 'points': 10},
        {'ID': 4 , 'name': "FOUR" , 'rank': 1, 'points': 0},
        {'ID': 5 , 'name': "FIVE" , 'rank': 2, 'points': 0},
        {'ID': 6 , 'name': "SIX"  , 'rank': 3, 'points': 0},
        {'ID': 7 , 'name': "SEVEN", 'rank': 4, 'points': 0},
        {'ID': 8 , 'name': "JACK" , 'rank': 5, 'points': 2},
        {'ID': 9 , 'name': "QUEEN", 'rank': 6, 'points': 3},
        {'ID': 10, 'name': "KING" , 'rank': 7, 'points': 4})

class card: 
    def __init__(self, seed, card_id, name, rank, points): 
        self.seed   = seed
        self.card_id= card_id
        self.name   = name 
        self.rank   = rank
        self.points = points

    def print_card(self):
        print(str(self.card_id)+" ("+self.name+") of "+self.seed+" with value "+str(self.points))


class deck:
    def __init__(self):
        self.deck_card = []
        for seed in SEEDS:
            for rank in RANKS:
                new_card = card(seed, rank.get('ID'), rank.get('name'), rank.get('rank'), rank.get('points'))
                self.deck_card.append(new_card)

    def shuffle_deck(self):
        random.shuffle(self.deck_card)
    
    def draw_card(self):
        if self.deck_size()>0:
            return self.deck_card.pop()

    def appen_card(self, card):
        self.deck_card.append(card)

    def deck_size(self):
        return len(self.deck_card)

    def print_deck(self):
        print("The Deck contains the following cards:\n")
        for p_card in self.deck_card:
            p_card.print_card()
