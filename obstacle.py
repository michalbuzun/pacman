import pygame
from const import WIDTH, HEIGHT, POSSIBLE_MOVES
import random
from enum import Enum, auto


class Direction(Enum):
    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()


class Obstacle(pygame.sprite.Sprite):
    def __init__(
        self,
    ):
        super().__init__()

        self.image = pygame.Surface([50, 50])
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.topleft = POSSIBLE_MOVES[63]
        # self.rect.topleft = (100, 350)
        self.direction = Direction.RIGHT

    def _move(self):
        if self.direction == Direction.RIGHT:
            potential_right_field = (self.rect.topleft[0] + 50, self.rect.topleft[1])

            if self._is_move_possible(potential_right_field):
                self.rect.topleft = potential_right_field
                # TO DO: refine this movement by checking if there are other directions possible
                # change direction if possible but with low probability for example 1/4 changing
                # direction 4/4 going straight
            else:
                ...
                # next move algorithm for ghost:
                # 1. check available directions
                # 2. randomly choose a direction
                # 3. go to the end in that direction

    def _is_move_possible(self, position):
        return self._is_in_game_field(position) and self._is_in_possible_moves(position)

    def _is_in_game_field(self, position):
        # check if not to far to the right
        if position[0] >= WIDTH:
            return False

        # check if not to far to the left
        if position[0] < 0:
            return False

        # check if not to far to the top
        if position[1] < 0:
            return False

        # check if not to far to the bottom
        if position[1] >= HEIGHT:
            return False

        return True

    def _is_in_possible_moves(self, position):
        return position in POSSIBLE_MOVES

    def update(self):
        self._move()

        # position = random.randint(0, len(WALLS) - 1)
        # self.rect.topleft = WALLS[position]
