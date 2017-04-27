import pygame
from Process import *
from Classes import *

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
isQuit = 0
clock = pygame.time.Clock()
fps = 30
total_frames = 0

# background_image = 

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], pygame.FULLSCREEN, 32)

survivor = Human(100, 100, 100, "survivor.gif")

while not isQuit:

    #PROCESS
    
    Process()
    
    #PROCESS

    #LOGIC
    
    total_frames+=1


    #LOGIC
    
    
    #DRAW
    BaseClass.List.draw(screen)
    screen.blit(screen, (0,0))


    #DRAW





    pygame.display.flip()
    clock.tick(fps)
    