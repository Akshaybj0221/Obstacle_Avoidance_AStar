# Import a library of functions called 'pygame'
import pygame
from math import pi
import numpy as np
import math
from operator import itemgetter
import time


#------------------This function Moving the block (0 element) to the Right, if possible--------------------------

def right(node):
    copyR = list(node[:])
    copyR[0] = abs(copyR[0] + 1)
    copyR = tuple(copyR)
    return copyR

#------------------This function Moving the block (0 element) to the Left, if possible--------------------------
def left(node):
    copyL = list(node[:])
    copyL[0] = abs(copyL[0] - 1)
    copyL = tuple(copyL)
    return copyL

#------------------This function Moving the node Upward, if possible--------------------------
def up(node):
    copyU = list(node[:])
    copyU[1] = abs(copyU[1] + 1)
    return tuple(copyU)

#------------------This function Moving the node Downward, if possible--------------------------
def down(node):
    copyD = list(node[:])
    copyD[1] = abs(copyD[1] - 1)
    return tuple(copyD)
 
#------------------This function Moving the node upward and to the right, if possible--------------------------
def upR(node):
    copyUpR = list(node[:])
    copyUpR[0] = abs(copyUpR[0] + 1)
    copyUpR[1] = abs(copyUpR[1] + 1)
    return tuple(copyUpR)
 
#------------------This function Moving the node upward and to the Left, if possible--------------------------
def upL(node):
    copyUpL = list(node[:])
    copyUpL[0] = abs(copyUpL[0] - 1)
    copyUpL[1] = abs(copyUpL[1] + 1)
    return tuple(copyUpL)

#------------------This function Moving the node downward and to the Left, if possible--------------------------
def downL(node):
    copyDownL = list(node[:])
    copyDownL[0] = abs(copyDownL[0] - 1)
    copyDownL[1] = abs(copyDownL[1] - 1)
    return tuple(copyDownL)

#------------------This function Moving the node downward and to the Right, if possible--------------------------
def downR(node):
    copyDownR = list(node[:]) 
    copyDownR[0] = abs(copyDownR[0] + 1)
    copyDownR[1] = abs(copyDownR[1] - 1)
    return tuple(copyDownR)


##-----------------------------  A - STAR  -----------------------------------------------------##

def getDistance(node1, node2):
    dist = math.sqrt((node2[0] - node1[0])**2 + (node2[1] - node1[1])**2)
    return dist

x1 = (150, 215)
G = (237,211)
#HighG = (120,85)
#G = (100, 35)
visited = []
openNodes = []
closedNodes = []
finalTable = []
finalTableDict = {}
nodesInfo = []
minDist = 100000


def appendInOpen(element, openNodes):
    flag = 0
    for item in closedNodes:    #checks if element to be added is already closed, no need
        if (item == element):   #to add it to open and BREAK out of the loop
            flag = 1
            break
    for item in openNodes:      #Checks if element is already in Open list, if yes then break
        if (item == element):
            flag = 1
            break    
    if (flag == 0):             
        openNodes.append(element)
    openNodes = set(openNodes)  #trying to keep the openNodes list element unique and not
    openNodes = list(openNodes) #redundant if missed.


def aStar(obstaclePoints):
    openNodes.append(x1)
    previousNode = x1
    startDist = getDistance(x1, x1)
    goalDist = getDistance(x1, G)
    totalDist = startDist + goalDist
    tableRow = [x1, startDist, goalDist, totalDist, previousNode]
    finalTableDict.update({x1:tableRow})




    x = finalTableDict[x1][0]

    iterations = 0
    value = 1
#    while (len(openNodes) != 0):
    while (value):
#        print("inside a star")

        iterations +=  1

        if iterations >= 100000:  #Stop the computation if more than 100,000 nodes are visited
            print("Cannot find solution in finite time")
            print("Nodes Visited (Closed): ", closedNodes)
            print(" ")
            print("Path Table: ", finalTableDict)
            print(" ")
            break

        if x == G :     #Stop the computation if result is found
            print("SUCCESSFULLY FOUND OPTIMAL PATH")
            value = 0            
            break

        if (x not in obstaclePoints):
            print("Please input the START NODE inside the free space of the map")
            break

        if (G not in obstaclePoints):
            print("Please input the GOAL NODE inside the free space of the map")
            break

        xDash = right(x)  #Now adding the result of moving right into the xDash
        if (xDash in obstaclePoints):   #Checking if unvisited
            appendInOpen(xDash, openNodes)
            previousNode = x
            startDist = getDistance(x1, xDash)
            goalDist = getDistance(xDash, G)
            totalDist = startDist + goalDist
            tableRow = [xDash, startDist, goalDist, totalDist, previousNode]
            
            if (xDash in finalTableDict): #checking for keys in the finalTableDict
                if (totalDist < finalTableDict[xDash][3]): #Overwrite only if the totaldistance
                    finalTableDict[xDash] = tableRow #for new path is less than previous one 
            else:                                    #else do not add it and let the old values be
                finalTableDict.update({xDash:tableRow}) #Adding a new row in dictionary

        xDash = left(x)       #Now adding the result of moving left into the xDash
        if (xDash in obstaclePoints):   #Checking if unvisited
            appendInOpen(xDash, openNodes)
            previousNode = x
            startDist = getDistance(x1, xDash)
            goalDist = getDistance(xDash, G)
            totalDist = startDist + goalDist
            tableRow = [xDash, startDist, goalDist, totalDist, previousNode]
            
            if (xDash in finalTableDict): #checking for keys in the finalTableDict
                if (totalDist < finalTableDict[xDash][3]): #Overwrite only if the totaldistance
                    finalTableDict[xDash] = tableRow #for new path is less than previous one 
            else:                                    #else do not add it and let the old values be
                finalTableDict.update({xDash:tableRow}) #Adding a new row in dictionary


        xDash = up(x)         #Now adding the result of moving up into the xDash
        if (xDash in obstaclePoints):   #Checking if unvisited
            appendInOpen(xDash, openNodes)
            previousNode = x
            startDist = getDistance(x1, xDash)
            goalDist = getDistance(xDash, G)
            totalDist = startDist + goalDist
            tableRow = [xDash, startDist, goalDist, totalDist, previousNode]
            
            if (xDash in finalTableDict): #checking for keys in the finalTableDict
                if (totalDist < finalTableDict[xDash][3]): #Overwrite only if the totaldistance
                    finalTableDict[xDash] = tableRow #for new path is less than previous one 
            else:                                    #else do not add it and let the old values be
                finalTableDict.update({xDash:tableRow}) #Adding a new row in dictionary


        xDash = down(x)       #Now adding the result of moving Down into the xDash
        if (xDash in obstaclePoints):   #Checking if unvisited
            appendInOpen(xDash, openNodes)
            previousNode = x
            startDist = getDistance(x1, xDash)
            goalDist = getDistance(xDash, G)
            totalDist = startDist + goalDist
            tableRow = [xDash, startDist, goalDist, totalDist, previousNode]
            
            if (xDash in finalTableDict): #checking for keys in the finalTableDict
                if (totalDist < finalTableDict[xDash][3]): #Overwrite only if the totaldistance
                    finalTableDict[xDash] = tableRow #for new path is less than previous one 
            else:                                    #else do not add it and let the old values be
                finalTableDict.update({xDash:tableRow}) #Adding a new row in dictionary


        xDash = upL(x)       #Now adding the result of moving Down into the xDash
        if (xDash in obstaclePoints):   #Checking if unvisited
            appendInOpen(xDash, openNodes)
            previousNode = x
            startDist = getDistance(x1, xDash)
            goalDist = getDistance(xDash, G)
            totalDist = startDist + goalDist
            tableRow = [xDash, startDist, goalDist, totalDist, previousNode]
            
            if (xDash in finalTableDict): #checking for keys in the finalTableDict
                if (totalDist < finalTableDict[xDash][3]): #Overwrite only if the totaldistance
                    finalTableDict[xDash] = tableRow #for new path is less than previous one 
            else:                                    #else do not add it and let the old values be
                finalTableDict.update({xDash:tableRow}) #Adding a new row in dictionary

 
        xDash = upR(x)       #Now adding the result of moving Down into the xDash
        if (xDash in obstaclePoints):   #Checking if unvisited
            appendInOpen(xDash, openNodes)
            previousNode = x
            startDist = getDistance(x1, xDash)
            goalDist = getDistance(xDash, G)
            totalDist = startDist + goalDist
            tableRow = [xDash, startDist, goalDist, totalDist, previousNode]
            
            if (xDash in finalTableDict): #checking for keys in the finalTableDict
                if (totalDist < finalTableDict[xDash][3]): #Overwrite only if the totaldistance
                    finalTableDict[xDash] = tableRow #for new path is less than previous one 
            else:                                    #else do not add it and let the old values be
                finalTableDict.update({xDash:tableRow}) #Adding a new row in dictionary


        xDash = downL(x)       #Now adding the result of moving Down into the xDash
        if (xDash in obstaclePoints):   #Checking if unvisited
            appendInOpen(xDash, openNodes)
            previousNode = x
            startDist = getDistance(x1, xDash)
            goalDist = getDistance(xDash, G)
            totalDist = startDist + goalDist
            tableRow = [xDash, startDist, goalDist, totalDist, previousNode]
            
            if (xDash in finalTableDict): #checking for keys in the finalTableDict
                if (totalDist < finalTableDict[xDash][3]): #Overwrite only if the totaldistance
                    finalTableDict[xDash] = tableRow #for new path is less than previous one 
            else:                                    #else do not add it and let the old values be
                finalTableDict.update({xDash:tableRow}) #Adding a new row in dictionary


        xDash = downR(x)       #Now adding the result of moving Down into the xDash
        if (xDash in obstaclePoints):   #Checking if unvisited
            appendInOpen(xDash, openNodes)
            previousNode = x
            startDist = getDistance(x1, xDash)
            goalDist = getDistance(xDash, G)
            totalDist = startDist + goalDist
            tableRow = [xDash, startDist, goalDist, totalDist, previousNode]
            
            if (xDash in finalTableDict): #checking for keys in the finalTableDict
                if (totalDist < finalTableDict[xDash][3]): #Overwrite only if the totaldistance
                    finalTableDict[xDash] = tableRow #for new path is less than previous one 
            else:                                    #else do not add it and let the old values be
                finalTableDict.update({xDash:tableRow}) #Adding a new row in dictionary


        closedNodes.append(x)
        openNodes.pop(0)

        minValue = 100000
        for node in openNodes:      # Selecting the node with least total distance amongst all other nodes
            if (node not in closedNodes):   #present in the openNodes list
                if (node in finalTableDict):
                    temp = finalTableDict[node][3]
                    if (minValue > temp):
                        minValue = temp
                        x = node

    return finalTableDict
