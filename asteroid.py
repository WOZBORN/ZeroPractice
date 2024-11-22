# asteroid.py

import pygame
import random
from enemy import Enemy
from constants import WIDTH, HEIGHT

img_path = "res/img/"

class Asteroid(Enemy):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load(img_path + "asteroid.png")
        self.original_image = pygame.transform.scale(self.original_image, (60, 60))
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(self.width + 10, WIDTH - (self.width + 10))
        self.rect.y = -self.rect.height
        self.speed_y = random.randint(1, 3)
        self.rotation = 0
        self.rotation_speed = random.randint(-5, 5)
        if self.rotation_speed == 0:
            self.rotation_speed = 1

    def update(self):
        super().update()
        # Обновляем угол вращения
        self.rotation = (self.rotation + self.rotation_speed) % 360
        # Вращаем оригинальное изображение
        rotated_image = pygame.transform.rotate(self.original_image, self.rotation)
        # Обновляем изображение и прямоугольник, сохраняя центр
        self.image = rotated_image
        self.rect = self.image.get_rect(center=self.rect.center)