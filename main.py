import pygame
from sys import exit
from const import WIDTH, HEIGHT, POSSIBLE_MOVES
from pacman import Pacman
from obstacle import Obstacle


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pacman")
clock = pygame.time.Clock()
game_active = True

font = pygame.font.SysFont("ubuntu", 30)
font_small = pygame.font.SysFont("ubuntu", 20)

pacman = Pacman()
pacman_group = pygame.sprite.GroupSingle()
pacman_group.add(pacman)

obstacle = Obstacle()
obstacle_group = pygame.sprite.Group()
obstacle_group.add(obstacle)

SQUARE_SIZE = 50


while True:
    screen.fill("black")

    for move in POSSIBLE_MOVES:
        position_rect = pygame.Rect(move[0], move[1], SQUARE_SIZE, SQUARE_SIZE)
        pygame.draw.rect(screen, "grey", position_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            ...

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True

    if game_active:
        pacman_group.draw(screen)
        pacman_group.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

    else:
        ...

    pygame.display.update()
    clock.tick(60)
