#
#
#

import pygame


class GameState():
    def __init__(self):
        self.score = 0
        self.lives = 3
        self.wave = 1
        self.game_paused = True


    def add_points(self, points):
        self.score += points

    def on_player_hit(self):
        if self.lives == 0:
            self.reset_game()
        else:
            self.lives -= 1

    def reset_game(self):
        self.score = 0
        self.lives = 3
        self.wave = 1

    def on_wave_complete(self):
        pass
