# Import a library of functions called 'pygame'
import pygame
from math import pi
import numpy as np
import AStar_Grid2
from AStar_Grid2 import *
 
# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
YELLOW = (255, 255, 0)
XCOLOR = (100, 100, 200)


#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# This sets the WIDTH and HEIGHT of each grid location i.e. the pixel (Point)
pointW = 2
pointH = 2

while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(FPS)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
     
    # Clear the screen and set the screen background
    screen.fill(WHITE)

    for i in obstaclePoints:
        pygame.draw.rect(screen, BLACK, [i[0], i[1] , pointW, pointH])

    for i in n:
        pygame.draw.rect(screen, RED, [i[0], i[1] , pointW, pointH])


#    for i in closedNodes:           
#        pygame.draw.rect(screen, RED, [i[0], i[1], pointW, pointH])     

#    for i in openNodes:
#        pygame.draw.rect(screen, YELLOW, [i[0], i[1] , pointW, pointH])   



    pygame.draw.rect(screen, GREEN, [G[0], G[1] , 5, 5])
    pygame.draw.rect(screen, BLUE, [x1[0], x1[1] , 5, 5])

    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()