import pygame


class Pacman(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def update(self):
        self._player_input()
        self._player_movement()
        self._render_player()
        self._check_for_next_level()
