import random
import logging
from briscola_cards import deck, card
from briscola_player import player
from briscola_stats import game_stats

class game2player:
    def __init__(self):
        # Variable to define the deck of card
        self.game_deck = deck()
        # Variable to define the list of player
        self.player_list = []
        # Variable for the briscola game suit
        self.briscola_suit = 'none'
        # Variable for the game statistics
        self.stats = game_stats(2)
        for pl_nr in range(2):
            new_player = player(pl_nr)
            self.player_list.append(new_player)

    def setup_game(self):
        self.game_deck.shuffle_deck()
        # randomly set a player as game leader for the first turn
        random.shuffle(self.player_list)
        logging.info("player_"+str(self.player_list[0].player_id)+" start first.")
        self.stats.set_player_order(self.player_list)
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
        logging.debug("SETUP GAME - briscola is: "+self.briscola_suit+" deck size: "+str(self.game_deck.deck_size()))
        logging.debug("-------------------------\n")
        

    def play_turn(self):
        card_trick = []
        for player in self.player_list:
            if player.count_cards() < 3:
                logging.debug("Player_"+str(player.player_id)+" is playing with "+str(player.count_cards())+" cards and draw a card")
                if self.game_deck.deck_size() > 0:
                    new_card = self.game_deck.draw_card()
                    player.draw_card(new_card)
            played_card = player.play_rnd_card(card_trick)
            card_trick.append(played_card)
            # print the cards
            logging.debug("Player_"+str(player.player_id)+" plays")
            played_card.print_card()
        # check if only 2 cards have been played
        if len(card_trick) != 2: return 0
        # run the trick:
        #  reverse the player list if the player lead looses the turn
        turn_points = card_trick[0].points + card_trick[1].points
        if card_trick[0].seed == card_trick[1].seed:
            if card_trick[0].rank > card_trick[1].rank:
                logging.debug("player_"+str(self.player_list[0].player_id)+" win the trick")
                self.player_list[0].add_points(turn_points)
            else:
                logging.debug("player_"+str(self.player_list[1].player_id)+" win the trick")
                self.player_list[1].add_points(turn_points)
                self.player_list.reverse()
        else:
            if (card_trick[1].seed == self.briscola_suit) and (card_trick[0].seed != self.briscola_suit):
                logging.debug("player_"+str(self.player_list[1].player_id)+" win the trick")
                self.player_list[1].add_points(turn_points)
                self.player_list.reverse()
            else:
                logging.debug("player_"+str(self.player_list[0].player_id)+" win the trick")
                self.player_list[0].add_points(turn_points)

    def run_game(self):
        turn = 0
        logging.debug("--------- START GAME ---------\n")
        while self.player_list[0].count_cards() > 0:
            turn += 1
            logging.debug("TURN NUMBER "+str(turn)+" briscola is: "+self.briscola_suit+" deck size: "+str(self.game_deck.deck_size()))
            self.play_turn()
            logging.debug("-------------------------\n")
        # check if the points sum is 120:
        tot_points = 0
        for player_i in self.player_list:
            tot_points += player_i.get_points()
        if tot_points != 120:
            logging.error("Error: total points is too high: "+str(tot_points))
        self.stats.set_player_scores(self.player_list)
        # returning winner player number
        if   self.player_list[0].pl_points > self.player_list[1].pl_points:
            logging.info("player_"+str(self.player_list[0].player_id)+" win the game with "+str(self.player_list[0].pl_points)+ " points!") 
            self.stats.set_winning_player_id(self.player_list[0].player_id)
        elif self.player_list[1].pl_points > self.player_list[0].pl_points:
            logging.info("player_"+str(self.player_list[1].player_id)+" win the game with "+str(self.player_list[1].pl_points)+ " points!")
            self.stats.set_winning_player_id(self.player_list[1].player_id)
        else:
            logging.info("the game ended in a draw")
            self.stats.set_draw()

    def get_stats(self):
        return self.stats

    def print_game(self):
        print("The briscola suit is: "+self.briscola_suit)
        for player in self.player_list:
            player.print_player()
