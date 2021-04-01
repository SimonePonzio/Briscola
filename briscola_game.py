import random
from briscola_cards import deck, card
from briscola_player import player

class game2player:
    def __init__(self):
        self.game_deck = deck()
        self.player_list = []
        self.briscola_suit = 'none'
        for pl_nr in range(2):
            new_player = player(pl_nr)
            self.player_list.append(new_player)

    def setup_game(self):
        self.game_deck.shuffle_deck()
        # randomly set a player as game leader for the first turn
        random.shuffle(self.player_list)
        self.player_list[0].set_leader()
        for player in self.player_list:
            while player.count_cards() < 3:
                new_card = self.game_deck.draw_card()
                player.draw_card(new_card)
            else: continue
        # get the briscola suit
        briscola_card = self.game_deck.draw_card()
        self.briscola_suit = briscola_card.seed
        # put the card at the bottom of the deck
        self.game_deck.append_card(briscola_card)
        print("SETUP GAME - briscola is: "+self.briscola_suit+" deck size: "+str(self.game_deck.deck_size()))
        print("-------------------------\n")
        

    def play_turn(self):
        card_trick = []
        for player in self.player_list:
            if player.count_cards() < 3:
                print("Player_"+str(player.player_id)+" is playing with "+str(player.count_cards())+" cards and draw a card")
                if self.game_deck.deck_size() > 0:
                    new_card = self.game_deck.draw_card()
                    player.draw_card(new_card)
            played_card = player.play_rnd_card(card_trick)
            card_trick.append(played_card)
            # print the cards
            print("Player_"+str(player.player_id)+" is playing with "+str(player.count_cards())+" cards")
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
        print("--------- START GAME ---------\n")
        while self.player_list[0].count_cards() > 0:
            turn += 1
            print("TURN NUMBER "+str(turn)+" briscola is: "+self.briscola_suit+" deck size: "+str(self.game_deck.deck_size()))
            self.play_turn()
            print("-------------------------\n")
        # check if the points sum is 120:
        tot_points = 0
        for player_i in self.player_list:
            tot_points += player_i.get_points()
        if tot_points != 120:
            print("Error: total points is too high: "+str(tot_points))
        # the winner is...
        if self.player_list[0].pl_points > self.player_list[1].pl_points:
            print("player_"+str(self.player_list[0].player_id)+" win the game with "+str(self.player_list[0].pl_points)+ " points!")
        else:
            print("player_"+str(self.player_list[1].player_id)+" win the game with "+str(self.player_list[1].pl_points)+ " points!")
        # returning winner player number
        if self.player_list[0].pl_points > self.player_list[1].pl_points: return 0
        else: return 1

    def print_game(self):
        print("The briscola suit is: "+self.briscola_suit)
        for player in self.player_list:
            player.print_player()
