import pygame
from const import WIDTH, HEIGHT, POSSIBLE_MOVES
import random
from enum import Enum, auto
from collections import namedtuple


TIME_DELAY_IN_MILLISECONDS = 600


class Direction(Enum):
    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()


Position = namedtuple(
    "Position",
    [
        "direction",
        "position",
    ],
)


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()

        self.image = pygame.Surface([50, 50])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = POSSIBLE_MOVES[63]
        self.direction = Direction.RIGHT
        self.is_move_possible = True
        self.time_with_delay = 0

    def _move(self):
        if self.direction == Direction.RIGHT:
            potential_position = (self.rect.topleft[0] + 50, self.rect.topleft[1])

            if self._is_move_possible(potential_position):
                possible_moves = self._get_possible_moves_in_ninty_degree_direction(
                    self.rect.topleft
                )
                possible_moves_positions = [move.position for move in possible_moves]

                all_possible_moves = [
                    *possible_moves_positions,
                    potential_position,
                ]

                self.rect.topleft = random.choice(all_possible_moves)

                # TO DO: refine this movement by checking if there are other directions possible
                # change direction if possible but with low probability for example 1/4 changing
                # direction 4/4 going straight
            else:
                self._check_available_directions(self.rect.topleft)

        if self.direction == Direction.LEFT:
            potential_position = (self.rect.topleft[0] - 50, self.rect.topleft[1])

            if self._is_move_possible(potential_position):
                possible_moves = self._get_possible_moves_in_ninty_degree_direction(
                    self.rect.topleft
                )
                possible_moves_positions = [move.position for move in possible_moves]

                all_possible_moves = [
                    *possible_moves_positions,
                    potential_position,
                ]

                self.rect.topleft = random.choice(all_possible_moves)
            else:
                self._check_available_directions(self.rect.topleft)

        if self.direction == Direction.UP:
            potential_position = (self.rect.topleft[0], self.rect.topleft[1] - 50)

            if self._is_move_possible(potential_position):
                possible_moves = self._get_possible_moves_in_ninty_degree_direction(
                    self.rect.topleft
                )
                possible_moves_positions = [move.position for move in possible_moves]

                all_possible_moves = [
                    *possible_moves_positions,
                    potential_position,
                ]

                self.rect.topleft = random.choice(all_possible_moves)
            else:
                self._check_available_directions(self.rect.topleft)

        if self.direction == Direction.DOWN:
            potential_position = (self.rect.topleft[0], self.rect.topleft[1] + 50)

            if self._is_move_possible(potential_position):
                possible_moves = self._get_possible_moves_in_ninty_degree_direction(
                    self.rect.topleft
                )
                possible_moves_positions = [move.position for move in possible_moves]

                all_possible_moves = [
                    *possible_moves_positions,
                    potential_position,
                ]

                self.rect.topleft = random.choice(all_possible_moves)
            else:
                self._check_available_directions(self.rect.topleft)

    def _get_possible_moves_in_ninty_degree_direction(self, position):
        available_directions = []

        if self.direction == Direction.UP or self.direction == Direction.DOWN:
            # check to the right
            potential_move = (position[0] + 50, position[1])
            if self._is_move_possible(potential_move):
                available_directions.append(
                    Position(direction=Direction.RIGHT, position=potential_move)
                )

            # check to the left
            potential_move = (position[0] - 50, position[1])
            if self._is_move_possible(potential_move):
                available_directions.append(
                    Position(direction=Direction.LEFT, position=potential_move)
                )

        if self.direction == Direction.LEFT or self.direction == Direction.RIGHT:
            # check to the top
            potential_move = (position[0], position[1] - 50)
            if self._is_move_possible(potential_move):
                available_directions.append(
                    Position(direction=Direction.UP, position=potential_move)
                )

            # check to the bottom
            potential_move = (position[0], position[1] + 50)
            if self._is_move_possible(potential_move):
                available_directions.append(
                    Position(direction=Direction.DOWN, position=potential_move)
                )

        return available_directions

    def _check_available_directions(self, position):
        # TO DO:
        # subtract 50 in all directions and chek if is in possible fields
        # remember direction of that field from current field, because it needs to be set as direciton

        available_directions = []

        # check to the right
        potential_move = (position[0] + 50, position[1])
        if self._is_move_possible(potential_move):
            available_directions.append(
                Position(direction=Direction.RIGHT, position=potential_move)
            )

        # check to the left
        potential_move = (position[0] - 50, position[1])
        if self._is_move_possible(potential_move):
            available_directions.append(
                Position(direction=Direction.LEFT, position=potential_move)
            )

        # check to the top
        potential_move = (position[0], position[1] - 50)
        if self._is_move_possible(potential_move):
            available_directions.append(
                Position(direction=Direction.UP, position=potential_move)
            )

        # check to the bottom
        potential_move = (position[0], position[1] + 50)
        if self._is_move_possible(potential_move):
            available_directions.append(
                Position(direction=Direction.DOWN, position=potential_move)
            )

        next_move = random.choice(available_directions)

        self.rect.topleft = next_move.position
        self.direction = next_move.direction

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

    def _block_movement(self):
        time_now = pygame.time.get_ticks()
        if time_now > self.time_with_delay:
            delay = TIME_DELAY_IN_MILLISECONDS
            self.time_with_delay = time_now + delay
            self.is_move_possible = True
        else:
            self.is_move_possible = False

    def update(self):
        # here add some code that will slow down sprite update
        self._block_movement()
        if self.is_move_possible:
            self._move()
