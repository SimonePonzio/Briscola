from briscola_player import player

class game_stats:
    def __init__(self, num_players):
        # Order of the players
        self._start_player = []
        # Game ended with a draw
        self._game_is_draw = 0
        # Winning player at the end of the game
        self._winning_player_id = 0
        # Player scores
        self._player_scores = []

    def set_start_player(self, player_list):
        for plr in player_list:
            self._start_player.append(plr.player_id)

    def set_draw(self):
        self._game_is_draw = 1

    def set_winning_player_id(self, plr_id):
        self._game_is_draw = 0
        self._winning_player_id = plr_id

    def set_player_scores(self, player_list):
        for plr in player_list:
            score = plr.get_points()
            self._player_scores.append(score)

    def get_start_player(self):
        return self._start_player[0]

    def get_draw(self):
        return self._game_is_draw

    def get_winning_player_id(self):
        return self._winning_player_id

class set_stats:
    def __init__(self):
        # Variable: list of the game stat
        self.stat_list = []

    def add_stat(self, stat):
        self.stat_list.append(stat)

    def get_draw_rate(self):
        draw_count = 0
        for game_stat in self.stat_list:
            if(game_stat.get_draw()):
                draw_count = draw_count + 1
        return float(draw_count)/len(self.stat_list)

    def get_plr_win_rate(self, plr_id):
        win_count = 0
        for game_stat in self.stat_list:
            if (game_stat.get_winning_player_id() == plr_id and not game_stat.get_draw()):
                win_count = win_count + 1
        return float(win_count)/len(self.stat_list)
    
    def get_start_plr_rate(self, plr_id):
        order_count = 0
        for game_stat in self.stat_list:
            if (game_stat.get_start_player() == plr_id):
                order_count = order_count + 1
        return float(order_count)/len(self.stat_list)
