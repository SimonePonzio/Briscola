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
        return self.deck_card.pop()

    def appen_card(self, card):
        self.deck_card.append(card)

    def deck_size(self):
        return len(self.deck_card)

    def print_deck(self):
        print("The Deck contains the following cards:\n")
        for p_card in self.deck_card:
            p_card.print_card()

class player:
    def __init__(self, pl_id):
        self.player_id = pl_id
        self.pl_card = []
        self.game_leader = False
        self.pl_points = 0

    def draw_card(self, deck):
        if len(self.pl_card) < 3:
            self.pl_card.append(deck.draw_card())
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

    def add_points(self, points):
        self.pl_points += points

    def get_points(self):
        return self.pl_points


class game2player:
    def __init__(self):
        self.game_deck = deck()
        self.player_list = []
        self.briscola_suit = 'none'
        for pl_nr in range(2):
            new_player = player(pl_nr)
            self.player_list.append(new_player)

    def setup_game(self):
        print("\nShaffle the deck... \n")
        self.game_deck.shuffle_deck()
        # randomly set a player as game leader for the first turn
        print("Randomly set a player as game leader for the first turn and distribute the cards\n\n")
        random.shuffle(self.player_list)
        self.player_list[0].set_leader()
        for player in self.player_list:
            while(player.draw_card(self.game_deck)): continue
        # get the briscola suit
        briscola_card = self.game_deck.draw_card()
        self.briscola_suit = briscola_card.seed
        # put the card at the bottom of the deck
        self.game_deck.appen_card(briscola_card)
        

    def play_turn(self):
        card_trick = []
        for player in self.player_list:
            while(player.draw_card(self.game_deck)): continue
            played_card = player.play_rnd_card()
            card_trick.append(played_card)
            # print the cards
            print("Player_"+str(player.player_id)+" is playing:")
            played_card.print_card()
        # check if only 2 cards have been played
        if len(card_trick) != 2: return 0
        # run the trick:
        #  reverse the player list if the player lead looses the turn
        turn_points = card_trick[0].points + card_trick[1].points
        if card_trick[0].seed == card_trick[1].seed:
            if card_trick[0].rank > card_trick[1].rank:
                print("player_"+str(self.player_list[0].player_id)+" win the trick")
                self.player_list[0].add_points(turn_points)
            else:
                print("player_"+str(self.player_list[1].player_id)+" win the trick")
                self.player_list[1].add_points(turn_points)
                self.player_list.reverse()
        else:
            if (card_trick[1].seed == self.briscola_suit) and (card_trick[0].seed != self.briscola_suit):
                print("player_"+str(self.player_list[1].player_id)+" win the trick")
                self.player_list[1].add_points(turn_points)
                self.player_list.reverse()
            else:
                print("player_"+str(self.player_list[0].player_id)+" win the trick")
                self.player_list[0].add_points(turn_points)

    def run_game(self):
        turn = 0
        while self.game_deck.deck_size() > 0:
            turn += 1
            print("TURN NUMBER "+str(turn)+" briscola is: "+self.briscola_suit)
            self.play_turn()
            print("-------------------------\n")
        # the winner is...
        if self.player_list[0].pl_points > self.player_list[1].pl_points:
            print("player_"+str(self.player_list[0].player_id)+" win the game with "+str(self.player_list[0].pl_points)+ " points!")
        else:
            print("player_"+str(self.player_list[1].player_id)+" win the game with "+str(self.player_list[1].pl_points)+ " points!")

    def print_game(self):
        print("The briscola suit is: "+self.briscola_suit)
        for player in self.player_list:
            player.print_player()


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