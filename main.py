# this allows us to use code from 
# the open-source pygame library 
# throughout this file 
import pygame
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main(): 
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}") 
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock_obj = pygame.time.Clock() 
    dt = 0
    
    updateable_group = pygame.sprite.Group() 
    drawable_group = pygame.sprite.Group() 
    asteroids_group = pygame.sprite.Group()  

    Player.containers = (updateable_group, drawable_group)
    Asteroid.containers = (asteroids_group, updateable_group, drawable_group)
    AsteroidField.containers = (updateable_group)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    print(len(drawable_group))
  
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.Surface.fill(screen, (0,0,0))
       
        updateable_group.update(dt)        
      
        for drawable in drawable_group:             
            drawable.draw(screen)       

        pygame.display.flip()
        
        dt = clock_obj.tick(60)
        dt /= 1000 # Convert ms to seconds


        

if __name__ == "__main__":
    main()
