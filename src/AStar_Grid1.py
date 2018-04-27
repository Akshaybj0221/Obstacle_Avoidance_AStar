# Import a library of functions called 'pygame'
#!/usr/bin/env python3
#import pygame
from math import pi
import numpy as np
import readMap2
from readMap2 import *
#import sys
#import AStar_Grid2
#from AStar_Grid2 import *
 
#print(sys.version)

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


# Set the height and width of the screen
screenX = 512
screenY = 544 

#x1 = (15, 15)
#G = (120,15)

size = [screenX, screenY]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("C-Space")

#Clock Speed
FPS = 60

#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# This sets the WIDTH and HEIGHT of each grid location i.e. the pixel (Point)
pointW = 1
pointH = 1

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
    screen.fill(BLACK)

#    print(finalMap)

#    for i in finalMap:
#        if (i[2] == 0): #0 = freespace
#            pygame.draw.rect(screen, WHITE, [i[0], i[1] , pointW, pointH])


    for i in obstaclePoints:
        pygame.draw.rect(screen, WHITE, [i[0], i[1] , pointW, pointH])

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