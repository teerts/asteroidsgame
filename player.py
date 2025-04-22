import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS

class Player(CircleShape):

    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        super().__init__(position_x, position_y, PLAYER_RADIUS)    
        self.rotation = 0

    def draw(self, screen):
        line_width = 2
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), line_width)

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
