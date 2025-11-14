import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def wrap_position(self):
        """
        Wrap the object's position around the screen edges.
        If the object goes off one edge, it appears on the opposite edge.
        This creates a "flat world" effect where the screen wraps like a torus.
        """
        # Wrap horizontally: if x goes past the right edge, appear on the left
        # The modulo operator (%) automatically handles both directions
        self.position.x = self.position.x % SCREEN_WIDTH
        
        # Wrap vertically: if y goes past the bottom edge, appear on the top
        self.position.y = self.position.y % SCREEN_HEIGHT

    def collides_with(self, other):
        distance = self.position.distance_to(other.position)
        return distance < (self.radius + other.radius)
