import pygame
from const import WIDTH, HEIGHT, WALLS
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
        self.rect.topleft = WALLS[63]
        self.direction = Direction.RIGHT

    def _move(self):
        if self.direction == Direction.RIGHT:
            potential_right_field = (self.rect.topleft[0] + 50, self.rect.topleft[1])
            # check if out of the game field

            if self._check_if_in_game_field(potential_right_field):
                self.rect.topleft = potential_right_field
            else:
                print("out of game field")

            # check if move is even possible

            # self.direction = Direction.LEFT
        # check if position is occupied by something

    def _check_if_in_game_field(self, position):
        if position[0] < WIDTH:
            return False

    def update(self):
        self._move()

        # position = random.randint(0, len(WALLS) - 1)
        # self.rect.topleft = WALLS[position]
