import pygame
import csv
from math import *
import numpy as np
import BFS_Grid3
from BFS_Grid3 import *

# Set the height and width of the screen
screenX = 250
screenY = 150 

size = [screenX, screenY]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("C-Space")


# The pixel location (x,y) of the center of circle
circleX = 180
circleY = 30
circleR = 15


# Pixel location (x,y) of each line of a square obstacles rounded to the closest integer value

squareAx = 55
squareAy = 83

squareBx = 55
squareBy = 38

squareCx = 105
squareCy = 38

squareDx = 105
squareDy = 83


# Set the pixel location (x,y) of each line of obstacles

polyAx = 145
polyAy = 136

polyBx = 120
polyBy = 95

polyCx = 158
polyCy = 99

polyDx = 165
polyDy = 61

polyEx = 188
polyEy = 99

polyFx = 168
polyFy = 136


#Clock Speed
FPS = 60
 
# Specifying a grid for an entire workspace so that I can access and draw on any vertex
axisX = []
for i in range(screenX):
    axisX.append(i)

axisY = []
for j in range(screenY):
        axisY.append(j)

# Getting Half plane for the rectangle type obstacle
# Getting x and y coordinates of all the pixels from left side of the square to the right end
squareLx = []
squareLy = []
squareLnodes = []

y = squareBy
while y <= squareAy:
    squareLy.append(y)
    y += 1

for i in axisX[squareAx:]:
    squareLx.append(i)

# list of (x,y)LEFT side of square till the right end of the window
for y in squareLy:
    for x in squareLx:
        squareLnodes.append((x,y))


# Getting x and y coordinates of all the pixels from Right side of the square to the right end
squareRx = []
squareRy = squareLy[:]
squareRnodes = []

for i in axisX[0:squareCx]:
    squareRx.append(i)

# list of (x,y)RIGHT side of square till the Left end of the window
for y in squareRy:
    for x in squareRx:
        squareRnodes.append((x,y))


# Getting x and y coordinates of all the pixels from Up side of the square to the bottom end
squareUx = []
squareUy = []
squareUnodes = []

y = squareBy
while y <= axisY[-1]:
    squareUy.append(y)
    y += 1

for i in axisX[squareBx:squareCx]:
    squareUx.append(i)

# list of (x,y)UP side of square till the Bottom end of the window
for y in squareUy:
    for x in squareUx:
        squareUnodes.append((x,y))


# Getting x and y coordinates of all the pixels from Down side of the square to the Upward end
squareDownX = squareUx[:]
squareDownY = []
squareDownNodes = []

y = squareAy
while y >= axisY[0]:
    squareDownY.append(y)
    y -= 1

# list of (x,y) DOWN side of square till the Upward end of the window
for y in squareDownY:
    for x in squareDownX:
        squareDownNodes.append((x,y))


squareSetL = set(squareLnodes)
squareSetR = set(squareRnodes)
squareSetU = set(squareUnodes)
squareSetD = set(squareDownNodes)
finalSquare = squareSetL.intersection(squareSetD, squareSetR, squareSetU)
finalSquare = list(finalSquare)


# Determine if a point is inside a given polygon or not
# Polygon is a list of (x,y) pairs.

# A function to check whether point P(x, y)
# lies inside the triangle formed by 
# A(x1, y1), B(x2, y2) and C(x3, y3) 
def isInside(x1, y1, x2, y2, x3, y3, x, y):
 
    # Calculate area of triangle ABC
    A = area (x1, y1, x2, y2, x3, y3)
 
    # Calculate area of triangle PBC 
    A1 = area (x, y, x2, y2, x3, y3)
     
    # Calculate area of triangle PAC 
    A2 = area (x1, y1, x, y, x3, y3)
     
    # Calculate area of triangle PAB 
    A3 = area (x1, y1, x2, y2, x, y)
     
    # Check if sum of A1, A2 and A3 
    # is same as A
    if(A == A1 + A2 + A3):
        return True
    else:
        return False

def area(x1, y1, x2, y2, x3, y3):
    triangleArea = (0.5*(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)))
    return abs(triangleArea)

def point_inside_triangle(x1, y1, x2, y2, x3, y3, x, y):
    # Calculate area of triangle ABC
    A = area (x1, y1, x2, y2, x3, y3)
    # Calculate area of triangle PBC 
    A1 = area (x, y, x2, y2, x3, y3)
    # Calculate area of triangle PAC 
    A2 = area (x1, y1, x, y, x3, y3)
    # Calculate area of triangle PAB 
    A3 = area (x1, y1, x2, y2, x, y)
    # Check if sum of A1, A2 and A3 
    # is same as A

    if(A == A1 + A2 + A3):
        return 1
    else:
        return 0


def point_inside_polygon(x, y):
    t1 = point_inside_triangle(polyCx, polyCy, polyDx, polyDy, polyEx, polyEy, x, y)
    t2 = point_inside_triangle(polyFx, polyFy, polyCx, polyCy, polyEx, polyEy,  x, y)
    t3 = point_inside_triangle(polyAx, polyAy, polyCx, polyCy, polyFx, polyFy, x, y)
    t4 = point_inside_triangle(polyAx, polyAy, polyCx, polyCy, polyBx, polyBy, x, y)
    t = t1 + t2 + t3 + t4
    if(t == 0):
        t = 0
        return False
    else:
        t = 0
        return True


# Getting all the coordinate values inside the Half plane for the non convex polygon
polygonPoints = []

for i in axisX:
    for j in axisY:
        polyPoints = point_inside_polygon(i, j)
        if polyPoints == True:
            polygonPoints.append((i,j))


# Getting Half plane for the circular type obstacle
def point_inside_circle(x, y):
    # Calculate area of triangle ABC
    if ((x - circleX)**2) + ((y - circleY)**2) <= (circleR**2):
        return True
    else:
        return False

# Getting all the coordinate values inside the Half plane for the circular obstacle

circlePoints = []

for i in axisX:
    for j in axisY:
        cPoints = point_inside_circle(i, j)
        if cPoints == True:
            circlePoints.append((i,j))

#Getting all the obstacle points inside a single list
obstaclePoints = []
obstaclePoints.extend(circlePoints)
obstaclePoints.extend(polygonPoints)
obstaclePoints.extend(finalSquare)



completeTable = aStar(obstaclePoints)

'''
a = G
temp = (102919,210292)
path.append(G)
while temp != x1:
    temp = completeTable[a][4]
    path.append(temp)
    a = temp
    print(path)

print("Path: ", path)
'''

"""
# Calling the Bredth First Search function
finalState = BFS(obstaclePoints, finalSquare)

print(" ")
print("We got from ",x1, " to ", finalState, " in ", len(visited), " moves")

i = visited.index(G)
z = len(nodesInfo)-1    

path.append(visited[nodesInfo[-1][0]])

while z != 0:
    a = nodesInfo[z][1]
    path.append(visited[a])
    z = a

#print("Path: ", path)

with open('nodeSet.csv', 'w', newline='') as node_file:
    csv_writer = csv.writer(node_file, delimiter = "\n")
    csv_writer.writerow(visited)

with open('pathNodes.csv', 'w', newline='') as node_file:
    csv_writer = csv.writer(node_file, delimiter = "\n")
    csv_writer.writerow(path)

with open('NodesInfo.csv', 'w', newline='') as node_file:
    csv_writer = csv.writer(node_file, delimiter = "\n")
    csv_writer.writerow(nodesInfo)
    """


