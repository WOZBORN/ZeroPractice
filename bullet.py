# bullet.py

import pygame
from constants import HEIGHT

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed_y):
        super().__init__()
        self.width = 5
        self.height = 10
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = speed_y

    def update(self):
        self.rect.y += self.speed_y
        # Удаление пули, если она выходит за экран
        if self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()
