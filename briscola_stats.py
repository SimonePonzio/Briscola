from briscola_player import player

class game_stats:
    def __init__(self, num_players):
        # Order of the players
        self._player_order = []
        # Game ended with a draw
        self._game_is_draw = 0
        # Winning player at the end of the game
        self._winning_player_id = 0
        # Player scores
        self._player_scores = []

    def set_player_order(self, player_list):
        for plr in player_list:
            self._player_order.append(plr.player_id)

    def set_draw(self):
        self._game_is_draw = 1

    def set_winning_player_id(self, plr_id):
        self._game_is_draw = 0
        self._winning_player_id = plr_id

    def set_player_scores(self, player_list):
        for plr in player_list:
            score = plr.get_points()
            self._player_scores.append(score)

    def get_player_order(self):
        return self._player_order

    def get_winning_player_id(self):
        return self._winning_player_id

    def get_stats(self):
        return

class set_stats:
    def __init__(self):
        # Variable: list of the game stat
        self.stat_list = []

    def add_stat(self, stat):
        self.stat_list.append(stat)

    # def get_plr_win_rate(self, plr_id):
    #     win_count = 0
    #     for game_stat in self.stat_list:
    #         win_count = game_stat
    
