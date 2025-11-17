import pygame
import circleshape
from constants import *


class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        # Immunity timer prevents the shot from hitting the player immediately after firing
        # This allows the shot to travel away from the player's position first
        self.player_immunity_timer = SHOT_PLAYER_IMMUNITY_SECONDS

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
        # Wrap position around screen edges to create a "flat world" effect
        self.wrap_position()
        # Count down the immunity timer (prevents instant self-collision)
        self.player_immunity_timer = max(0.0, self.player_immunity_timer - dt)
