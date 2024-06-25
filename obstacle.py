import pygame
from const import WALLS
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
        self.rect.topleft = WALLS[10]
        self.direction = Direction.RIGHT

    def _move(self):
        ...
        # check if position is occupied by something

    def update(self):
        self._move()

        position = random.randint(0, len(WALLS) - 1)
        self.rect.topleft = WALLS[position]
