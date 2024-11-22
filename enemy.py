# enemy.py

import pygame
import random
from constants import WIDTH, HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 40
        self.height = 30
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill("white")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(self.width + 10, WIDTH - (self.width + 10))
        self.rect.y = -self.height
        self.speed_y = random.randint(2, 5)

    def update(self):
        self.rect.y += self.speed_y
        # Удаление, если выходит за нижнюю границу
        if self.rect.top > HEIGHT:
            self.kill()
