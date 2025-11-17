import pygame
from constants import *


class Score:
    def __init__(self):
        self.points = 0
        self.survival_time = 0.0
        self.last_bonus_time = 0.0
        self.level = 1
        self.asteroids_destroyed = 0
        
    def update(self, dt):
        """Update survival time and award points for staying alive"""
        self.survival_time += dt
        
        # Award points for survival every second
        self.points += SCORE_SURVIVAL_PER_SECOND * dt
        
        # Check if player has reached next level (every 10 seconds)
        if self.survival_time - self.last_bonus_time >= SCORE_SURVIVAL_BONUS_INTERVAL:
            self.level += 1
            self.points += SCORE_SURVIVAL_BONUS
            self.last_bonus_time = self.survival_time
            
    def asteroid_destroyed(self):
        """Award points for destroying an asteroid"""
        self.asteroids_destroyed += 1
        self.points += SCORE_ASTEROID_DESTROYED
        
    def draw(self, screen):
        """Draw the score, level, and time on screen"""
        font = pygame.font.Font(None, 36)
        
        # Draw score in top-left
        score_text = font.render(f"Score: {int(self.points)}", True, "white")
        screen.blit(score_text, (10, 10))
        
        # Draw level below score
        level_text = font.render(f"Level: {self.level}", True, "yellow")
        screen.blit(level_text, (10, 50))
        
        # Draw survival time below level
        time_text = font.render(f"Time: {int(self.survival_time)}s", True, "cyan")
        screen.blit(time_text, (10, 90))
        
        # Draw asteroid count
        asteroids_text = font.render(f"Asteroids: {self.asteroids_destroyed}", True, "green")
        screen.blit(asteroids_text, (10, 130))
        
    def get_final_message(self):
        """Return a message with final statistics"""
        return (
            f"Game Over!\n"
            f"Final Score: {int(self.points)}\n"
            f"Level Reached: {self.level}\n"
            f"Survival Time: {int(self.survival_time)} seconds\n"
            f"Asteroids Destroyed: {self.asteroids_destroyed}"
        )
