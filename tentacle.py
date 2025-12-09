import pygame
import math
from constants import *


class Tentacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, orientation):
        """
        Create a tentacle whip attack
        
        Args:
            x, y: Top-left position
            width, height: Dimensions (for horizontal: width=screen_width, height=thickness)
            orientation: "horizontal" or "vertical"
        """
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.rect = pygame.Rect(x, y, width, height)
        self.orientation = orientation
        self.lifetime = CTHULHU_TENTACLE_DURATION
        self.max_lifetime = CTHULHU_TENTACLE_DURATION
    
    def draw(self, screen):
        """Draw the tentacle whip with pulsing animation"""
        # Calculate alpha based on lifetime for fade in/out effect
        alpha_factor = min(1.0, self.lifetime / 0.3)  # Fade in first 0.3 seconds
        if self.lifetime < 0.2:  # Fade out last 0.2 seconds
            alpha_factor = self.lifetime / 0.2
        
        # Pulsing effect
        pulse = (math.sin(self.lifetime * 20) + 1) / 2  # Oscillate between 0 and 1
        color_intensity = int(200 + 55 * pulse)
        
        color = (min(255, color_intensity), 0, int(100 * alpha_factor))
        
        # Draw main tentacle body
        pygame.draw.rect(screen, color, self.rect)
        
        # Draw outline for emphasis
        pygame.draw.rect(screen, TENTACLE_COLOR, self.rect, width=2)
    
    def update(self, dt):
        """Update animation timer and remove when expired"""
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()
    
    def collides_with_circle(self, circle_obj):
        """
        Check collision between this rectangle and a circular object
        
        Args:
            circle_obj: Object with .position (pygame.Vector2) and .radius attributes
            
        Returns:
            bool: True if collision detected
        """
        # Find the closest point on the rectangle to the circle center
        closest_x = max(self.rect.left, min(circle_obj.position.x, self.rect.right))
        closest_y = max(self.rect.top, min(circle_obj.position.y, self.rect.bottom))
        
        # Calculate distance from circle center to this closest point
        distance_x = circle_obj.position.x - closest_x
        distance_y = circle_obj.position.y - closest_y
        distance_squared = distance_x ** 2 + distance_y ** 2
        
        # Collision occurs if distance is less than radius
        return distance_squared < (circle_obj.radius ** 2)
