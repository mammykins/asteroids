"""
Quick test script to verify Cthulhu mechanics
Spawns Cthulhu at 5 seconds instead of 30 for easier testing
"""
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from cthulhu import Cthulhu
from tentacle import Tentacle
from logger import log_state
from logger import log_event
from score import Score

import pygame
import sys

# Override spawn time for testing
TEST_SPAWN_TIME = 5.0
TEST_WARNING_TIME = 3.0

def main():
    pygame.init()
    print("Starting Asteroids - CTHULHU TEST MODE!")
    print(f"Cthulhu will spawn at {TEST_SPAWN_TIME} seconds")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    cthulhu_group = pygame.sprite.Group()
    tentacles = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    Cthulhu.containers = (cthulhu_group, updatable, drawable)
    Tentacle.containers = (tentacles, updatable, drawable)

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2, radius=PLAYER_RADIUS)
    asteroid_field = AsteroidField()
    score = Score()
    cthulhu_spawned = False

    # GAME LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        score.update(dt)
        
        # Spawn Cthulhu at TEST_SPAWN_TIME seconds
        if not cthulhu_spawned and score.survival_time >= TEST_SPAWN_TIME:
            cthulhu = Cthulhu(x=-CTHULHU_RADIUS, y=SCREEN_HEIGHT / 2)
            cthulhu_spawned = True
            log_event("cthulhu_spawned")
            print(f"CTHULHU SPAWNED at {score.survival_time:.1f} seconds!")
        
        updatable.update(dt)

        # player vs asteroids
        for asteroid in list(asteroids):
            if asteroid.collides_with(player):
                log_event("player_hit")
                print(score.get_final_message())
                sys.exit()

        # shots vs asteroids (manual, circle-based)
        for asteroid in list(asteroids):
            for shot in list(shots):
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    score.asteroid_destroyed()
                    asteroid.split()
                    shot.kill()
                    break

        # shots vs player (friendly-fire)
        for shot in list(shots):
            if shot.player_immunity_timer <= 0 and player.collides_with(shot):
                log_event("player_hit")
                print(score.get_final_message())
                sys.exit()
        
        # Cthulhu vs asteroids - asteroids are annihilated
        if cthulhu_spawned:
            for cthulhu in list(cthulhu_group):
                for asteroid in list(asteroids):
                    if cthulhu.collides_with(asteroid):
                        log_event("cthulhu_asteroid_collision")
                        asteroid.kill()
        
        # Cthulhu vs player - instant death
        if cthulhu_spawned:
            for cthulhu in list(cthulhu_group):
                if cthulhu.collides_with(player):
                    log_event("cthulhu_player_collision")
                    print("Consumed by the cosmic horror!")
                    print(score.get_final_message())
                    sys.exit()
        
        # Tentacles vs player - instant death
        for tentacle in list(tentacles):
            if tentacle.collides_with_circle(player):
                log_event("tentacle_player_collision")
                print("Crushed by Cthulhu's tentacle!")
                print(score.get_final_message())
                sys.exit()
        
        # Tentacles vs asteroids - optional annihilation
        for tentacle in list(tentacles):
            for asteroid in list(asteroids):
                if tentacle.collides_with_circle(asteroid):
                    asteroid.kill()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        
        # Draw custom warning for test mode
        if score.survival_time >= TEST_WARNING_TIME and score.survival_time < TEST_SPAWN_TIME:
            import math
            flash = (math.sin(score.survival_time * 8) + 1) / 2
            if flash > 0.3:
                warning_font = pygame.font.Font(None, 64)
                warning_text = warning_font.render("SOMETHING AWAKENS...", True, (255, 0, 0))
                text_rect = warning_text.get_rect(center=(SCREEN_WIDTH / 2, 100))
                screen.blit(warning_text, text_rect)
        elif score.survival_time >= TEST_SPAWN_TIME:
            warning_font = pygame.font.Font(None, 48)
            warning_text = warning_font.render("CTHULHU RISES!", True, CTHULHU_COLOR)
            text_rect = warning_text.get_rect(center=(SCREEN_WIDTH / 2, 100))
            screen.blit(warning_text, text_rect)
        
        score.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
