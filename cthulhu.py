import pygame
import math
import random
import circleshape
from constants import *
from tentacle import Tentacle


class Cthulhu(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, CTHULHU_RADIUS)
        self.time_alive = 0.0
        self.tentacle_cooldown = CTHULHU_TENTACLE_COOLDOWN
        self.animation_offset = random.uniform(0, math.pi * 2)
        
        # Movement pattern: move horizontally across screen with sine wave
        self.start_x = x
        self.direction = 1 if x < SCREEN_WIDTH / 2 else -1
        self.velocity = pygame.Vector2(self.direction * CTHULHU_SPEED, 0)
        
    def draw(self, screen):
        """Draw Cthulhu as a cosmic horror with tentacles"""
        # Main body - large circle for the head
        pygame.draw.circle(screen, CTHULHU_COLOR, self.position, self.radius, width=3)
        
        # Draw eyes - menacing
        eye_offset = self.radius * 0.3
        eye_radius = self.radius * 0.15
        left_eye = self.position + pygame.Vector2(-eye_offset, -eye_offset)
        right_eye = self.position + pygame.Vector2(eye_offset, -eye_offset)
        pygame.draw.circle(screen, (255, 0, 0), left_eye, eye_radius)
        pygame.draw.circle(screen, (255, 0, 0), right_eye, eye_radius)
        
        # Draw multiple writhing tentacles
        num_tentacles = 8
        for i in range(num_tentacles):
            angle = (i / num_tentacles) * math.pi * 2
            # Animate tentacles with sine wave
            writhe = math.sin(self.time_alive * 3 + angle + self.animation_offset) * 15
            
            # Tentacle base point on the body
            base_x = self.position.x + math.cos(angle) * self.radius * 0.8
            base_y = self.position.y + math.sin(angle) * self.radius * 0.8
            
            # Tentacle end point (writhing)
            end_x = self.position.x + math.cos(angle) * (self.radius * 1.5 + writhe)
            end_y = self.position.y + math.sin(angle) * (self.radius * 1.5 + writhe)
            
            pygame.draw.line(screen, CTHULHU_COLOR, (base_x, base_y), (end_x, end_y), 3)
    
    def update(self, dt):
        self.time_alive += dt
        
        # Sinusoidal vertical movement for dramatic effect
        amplitude = 100
        frequency = 0.5
        center_y = SCREEN_HEIGHT / 2
        self.position.y = center_y + amplitude * math.sin(self.time_alive * frequency)
        
        # Horizontal movement
        self.position.x += self.velocity.x * dt
        
        # Wrap around screen
        if self.position.x < -self.radius * 2:
            self.position.x = SCREEN_WIDTH + self.radius * 2
        elif self.position.x > SCREEN_WIDTH + self.radius * 2:
            self.position.x = -self.radius * 2
        
        # Tentacle whip attack cooldown
        self.tentacle_cooldown -= dt
        if self.tentacle_cooldown <= 0:
            self.trigger_tentacle_whip()
            self.tentacle_cooldown = CTHULHU_TENTACLE_COOLDOWN
    
    def trigger_tentacle_whip(self):
        """Spawn a tentacle whip attack"""
        from logger import log_event
        log_event("tentacle_whip_started")
        
        # Random orientation - horizontal or vertical
        orientation = random.choice(["horizontal", "vertical"])
        
        if orientation == "horizontal":
            # Horizontal sweep across screen
            y_pos = random.uniform(CTHULHU_TENTACLE_WIDTH, SCREEN_HEIGHT - CTHULHU_TENTACLE_WIDTH)
            Tentacle(0, y_pos, SCREEN_WIDTH, CTHULHU_TENTACLE_WIDTH, "horizontal")
        else:
            # Vertical sweep across screen
            x_pos = random.uniform(CTHULHU_TENTACLE_WIDTH, SCREEN_WIDTH - CTHULHU_TENTACLE_WIDTH)
            Tentacle(x_pos, 0, CTHULHU_TENTACLE_WIDTH, SCREEN_HEIGHT, "vertical")
