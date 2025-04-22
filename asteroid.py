from circleshape import CircleShape
import pygame

class Asteroid(CircleShape): 
    def __init__(self, x, y, radius):         
        self.radius = radius 
        super().__init__(x, y, radius)        

    def draw(self, screen):
        width_of_circle = 2
        self.position = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, width_of_circle)
    
    def update(self, dt): 
        movement = self.velocity * dt 
        self.position += movement

