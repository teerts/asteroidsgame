from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random

class Asteroid(CircleShape): 
    def __init__(self, x, y, radius):         
        self.radius = radius 
        self.minimum_angle = 20
        self.maximum_angle = 50
        self.velocity_scale_factor = 1.2         
        super().__init__(x, y, radius)        

    def draw(self, screen):
        width_of_circle = 2
        self.position = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, width_of_circle)
    
    def update(self, dt): 
        movement = self.velocity * dt 
        self.position += movement

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(self.minimum_angle, self.maximum_angle)        

        vector_one = pygame.Vector2(0, 1).rotate(random_angle)
        vector_two = pygame.Vector2(0, -1).rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_one = Asteroid(int(self.position[0]), int(self.position[1]), new_radius)
        new_asteroid_two = Asteroid(int(self.position[0]), int(self.position[1]), new_radius)
        
        new_asteroid_one.velocity = vector_one * self.velocity_scale_factor
        new_asteroid_two.velocity = vector_two * self.velocity_scale_factor
        



        

