# player.py

import pygame
from bullet import Bullet
from constants import WIDTH, HEIGHT

img_path = "res/img/"

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 100
        self.height = 80
        self.image = pygame.image.load(img_path + "player.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speed_x = 0
        self.speed_y = 0
        self.health = 100
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = 250  # миллисекунды

    def update(self):
        self.speed_x = 0
        self.speed_y = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.speed_x = -10
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.speed_x = 10
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.speed_y = -10
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.speed_y = 10
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Ограничение движения по экрану
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < HEIGHT // 2:
            self.rect.top = HEIGHT // 2
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.top, -10)
            return bullet
        return None

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()
