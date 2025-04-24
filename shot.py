from circleshape import CircleShape
from constants import SHOT_RADIUS
import pygame

class Shot(CircleShape):
    def __init__(self, position, radius):        
        super().__init__(position.x, position.y, radius) 

    def draw(self, screen):
        width_of_circle = 2        
        self.position = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, (255,255,255), self.position, SHOT_RADIUS, width_of_circle)
    
    def update(self, dt): 
        movement = self.velocity * dt 
        self.position += movement