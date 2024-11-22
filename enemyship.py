# enemyship.py

import pygame
import random
from enemy import Enemy
from bullet import Bullet
from constants import WIDTH, HEIGHT

img_path = "res/img/"

class EnemyShip(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(img_path + "enemy.png")
        self.image = pygame.transform.scale(self.image, (100, 80))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(self.width + 10, WIDTH - (self.width + 10))
        self.rect.y = -self.rect.height
        self.speed_y = random.randint(2, 4)
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = 1000  # миллисекунды

    def update(self) -> Bullet | None:
        super().update()
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.bottom + 10, 10)
            return bullet
        return None
