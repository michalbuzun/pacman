import pygame


class Pacman(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        # self.image.fill("green")
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (200, 200)

    def update(self): ...
