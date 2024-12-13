# main.py

import pygame
import sys
import random
from player import Player
from asteroid import Asteroid
from enemyship import EnemyShip
from constants import WIDTH, HEIGHT, FPS

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Scroll Shooter")
    clock = pygame.time.Clock()

    # Спрайт группы
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    player = Player()
    all_sprites.add(player)

    # Таймер спавна врагов
    enemy_spawn_event = pygame.USEREVENT + 1
    pygame.time.set_timer(enemy_spawn_event, 1000)  # каждые 1 сек

    running = True
    game_over = False
    game_over_time = 0

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == enemy_spawn_event and not game_over:
                enemy_type = random.choice(['asteroid', 'enemyship'])
                if enemy_type == 'asteroid':
                    enemy = Asteroid()
                else:
                    enemy = EnemyShip()
                all_sprites.add(enemy)
                enemies.add(enemy)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    bullet = player.shoot()
                    if bullet:
                        all_sprites.add(bullet)
                        bullets.add(bullet)

        if not game_over:
            # Обновление спрайтов
            all_sprites.update()

            # Проверка стрельбы EnemyShip
            for enemy in enemies:
                if isinstance(enemy, EnemyShip):
                    bullet = enemy.update()
                    if bullet:
                        all_sprites.add(bullet)
                        bullets.add(bullet)

            # Проверка столкновений пуль с врагами
            hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
            for hit in hits:
                pass  # Здесь можно добавить эффекты или увеличение счета

            # Проверка столкновений врагов с игроком
            hits = pygame.sprite.spritecollide(player, enemies, True)
            for hit in hits:
                player.take_damage(20)  # Урон при столкновении

            # Проверка столкновений игрока с пулями
            hits = pygame.sprite.spritecollide(player, bullets, True)
            for hit in hits:
                player.take_damage(10)

            # Проверка здоровья игрока
            if not player.alive():
                game_over = True
                game_over_time = pygame.time.get_ticks()

        else:
            # После Game Over ждём 3 секунды и закрываем
            if pygame.time.get_ticks() - game_over_time > 3000:
                running = False

        # Рендеринг
        screen.fill("black")
        all_sprites.draw(screen)

        # Отображение здоровья
        if player.alive():
            font = pygame.font.SysFont(None, 24)
            health_text = font.render(f'Health: {player.health}', True, (255, 255, 255))
            screen.blit(health_text, (10, 10))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
