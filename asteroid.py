import pygame
import circleshape
from constants import *


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        """Draw the asterioid. It accepts the surface to draw on, the colour and the width of the line from constants."""
        pygame.draw.circle(
            screen, "white", self.position, self.radius, width=LINE_WIDTH
        )

    def update(self, dt):
        self.position += self.velocity * dt
