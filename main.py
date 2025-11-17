from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from logger import log_state
from logger import log_event
from score import Score

import pygame
import sys


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2, radius=PLAYER_RADIUS)
    asteroid_field = AsteroidField()
    score = Score()

    # GAME LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        score.update(dt)
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
                    break  # stop checking this asteroid after it's destroyed

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        
        score.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000  # Limit to 60 FPS and delta time


if __name__ == "__main__":
    main()
