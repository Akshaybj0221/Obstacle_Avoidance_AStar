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

x1 = (15, 15)
G = (120,15)
#G = (100,85)
visited = []
openNodes = []
closedNodes = []
finalTable = []
finalTableDict = {}
nodesInfo = []
minDist = 100000


def appendInOpen(element, openNodes):
    flag = 0
    for item in closedNodes:
        if (item == element):
            flag = 1
            break
    for item in openNodes:
        if (item == element):
            flag = 1
            break    
    if (flag == 0):
        openNodes.append(element)
    openNodes = set(openNodes)
    openNodes = list(openNodes)


def aStar(obstaclePoints):
    openNodes.append(x1)
    previousNode = x1
    startDist = getDistance(x1, x1)
    goalDist = getDistance(x1, G)
    totalDist = startDist + goalDist
    tableRow = [x1, startDist, goalDist, totalDist, previousNode]
#    finalTable.append(tableRow)

#    finalTableDict = {x1: tableRow}
#    finalTableDict[x1].append(tableRow)
    finalTableDict.update({x1:tableRow})

#    x = finalTable[0][0]
    x = finalTableDict[x1][0]

    iterations = 0

    while (len(openNodes) != 0): 

        iterations +=  1
        if iterations >= 100000:  #Stop the computation if more than 100,000 nodes are visited
            print("Cannot find solution in finite time")
            print("Nodes Visited (Closed): ", closedNodes)
            print(" ")
            print("Path Table: ", finalTableDict)
            print(" ")
            break

        if x == G :     #Stop the computation if result is found
            print("SUCCESS")
            print("Open Nodes: ", openNodes)
            print(" ")
            print("Nodes Visited (Closed): ", closedNodes)
            print(" ")
            print("Path Table: ", finalTableDict)
            print(" ")
            break


#        x = finalTable[0][0]
#        x = openNodes[0]

        xDash = right(x)  #Now adding the result of moving right into the xDash
        if (xDash not in obstaclePoints):   #Checking if unvisited
#            openNodes.append(xDash)
            appendInOpen(xDash, openNodes)
            previousNode = x
            startDist = getDistance(x1, xDash)
            goalDist = getDistance(xDash, G)
            totalDist = startDist + goalDist
    #        nodesInfo.append((visited.index(xDash), visited.index(x), totalDist))
            tableRow = [xDash, startDist, goalDist, totalDist, previousNode]
            
            if xDash in finalTableDict:
                finalTableDict[xDash] = tableRow
            else:
#                finalTableDict[xDash].append(tableRow)
                finalTableDict.update({xDash:tableRow})


#            finalTable.append(tableRow)

            '''
            for row in finalTable:
                print("Checking if xDash in FinalTabe already present:-", row, "XDASH: ", xDash)
                if (xDash not in row[0]):
                    print ("If ", xDash, " not inside ", row[0])
                    finalTable.append(tableRow)
                    break
            '''
#            print("Final Table: ", finalTable)
#                    break
#                if (xDash in row[0]):
#                    for idx, item in enumerate(finalTable):
#                        if (xDash in item):
#                            finalTable[idx] = tableRow                   


###--------------CONT: TAKE CARE OF WHEN TO APPPEND A ROW WITH SIMILAR NODE IN FINAL TABLE OR UPDATE ITS VALUE-----------------------------#

    #        if (xDash not in finalTable[0]):
    #            finalTable.append(tableRow)

    #        if (xDash in finalTable[0]):
    #            for idx, item in enumerate(finalTable):
    #                if xDash in item:
    #                finalTable[idx] = tableRow

        xDash = left(x)       #Now adding the result of moving left into the xDash
        if (xDash not in obstaclePoints):   #Checking if unvisited
#            openNodes.append(xDash)
            appendInOpen(xDash, openNodes)
            previousNode = x
            startDist = getDistance(x1, xDash)
            goalDist = getDistance(xDash, G)
            totalDist = startDist + goalDist
            tableRow = [xDash, startDist, goalDist, totalDist, previousNode]
            if xDash in finalTableDict:
                finalTableDict[xDash] = tableRow
            else:
#                finalTableDict[xDash].append(tableRow)
                finalTableDict.update({xDash:tableRow})


#            finalTable.append(tableRow)
            '''
            for row in finalTable:
                print("Checking if xDash in FinalTabe already present:-", row, "XDASH: ", xDash)
                if (xDash not in row[0]):
                    print ("If ", xDash, " not inside ", row[0])
                    finalTable.append(tableRow)
                    break
            '''

        xDash = up(x)         #Now adding the result of moving up into the xDash
        if (xDash not in obstaclePoints):   #Checking if unvisited
#            openNodes.append(xDash)
            appendInOpen(xDash, openNodes)
            previousNode = x
            startDist = getDistance(x1, xDash)
            goalDist = getDistance(xDash, G)
            totalDist = startDist + goalDist
            tableRow = [xDash, startDist, goalDist, totalDist, previousNode]
            if xDash in finalTableDict:
                finalTableDict[xDash] = tableRow
            else:
#                finalTableDict[xDash].append(tableRow)
                finalTableDict.update({xDash:tableRow})


#            finalTable.append(tableRow)
            '''
            for row in finalTable:
                print("Checking if xDash in FinalTabe already present:-", row, "XDASH: ", xDash)
                if (xDash not in row[0]):
                    print ("If ", xDash, " not inside ", row[0])
                    finalTable.append(tableRow)
                    break
            '''

        xDash = down(x)       #Now adding the result of moving Down into the xDash
        if (xDash not in obstaclePoints):   #Checking if unvisited
#            openNodes.append(xDash)
            appendInOpen(xDash, openNodes)
            previousNode = x
            startDist = getDistance(x1, xDash)
            goalDist = getDistance(xDash, G)
            totalDist = startDist + goalDist
            tableRow = [xDash, startDist, goalDist, totalDist, previousNode]
            if xDash in finalTableDict:
                finalTableDict[xDash] = tableRow
            else:
#                finalTableDict[xDash].append(tableRow)
                finalTableDict.update({xDash:tableRow})


#            finalTable.append(tableRow)
            '''
            for row in finalTable:
                print("Checking if xDash in FinalTabe already present:-", row, "XDASH: ", xDash)
                if (xDash not in row[0]):
                    print ("If ", xDash, " not inside ", row[0])
                    finalTable.append(tableRow)
                    break
            '''

        xDash = upL(x)       #Now adding the result of moving Down into the xDash
        if (xDash not in obstaclePoints):   #Checking if unvisited
#            openNodes.append(xDash)
            appendInOpen(xDash, openNodes)
            previousNode = x
            startDist = getDistance(x1, xDash)
            goalDist = getDistance(xDash, G)
            totalDist = startDist + goalDist
            tableRow = [xDash, startDist, goalDist, totalDist, previousNode]
            if xDash in finalTableDict:
                finalTableDict[xDash] = tableRow
            else:
#                finalTableDict[xDash].append(tableRow)
                finalTableDict.update({xDash:tableRow})


#            finalTable.append(tableRow)
            '''
            for row in finalTable:
                print("Checking if xDash in FinalTabe already present:-", row, "XDASH: ", xDash)
                if (xDash not in row[0]):
                    print ("If ", xDash, " not inside ", row[0])
                    finalTable.append(tableRow)
                    break
            '''
 
        xDash = upR(x)       #Now adding the result of moving Down into the xDash
        if (xDash not in obstaclePoints):   #Checking if unvisited
#            openNodes.append(xDash)
            appendInOpen(xDash, openNodes)
            previousNode = x
            startDist = getDistance(x1, xDash)
            goalDist = getDistance(xDash, G)
            totalDist = startDist + goalDist
            tableRow = [xDash, startDist, goalDist, totalDist, previousNode]
            if xDash in finalTableDict:
                finalTableDict[xDash] = tableRow
            else:
#                finalTableDict[xDash].append(tableRow)
                finalTableDict.update({xDash:tableRow})


#            finalTable.append(tableRow)
            '''
            for row in finalTable:
                print("Checking if xDash in FinalTabe already present:-", row, "XDASH: ", xDash)
                if (xDash not in row[0]):
                    print ("If ", xDash, " not inside ", row[0])
                    finalTable.append(tableRow)
                    break
            '''

        xDash = downL(x)       #Now adding the result of moving Down into the xDash
        if (xDash not in obstaclePoints):   #Checking if unvisited
#            openNodes.append(xDash)
            appendInOpen(xDash, openNodes)
            previousNode = x
            startDist = getDistance(x1, xDash)
            goalDist = getDistance(xDash, G)
            totalDist = startDist + goalDist
            tableRow = [xDash, startDist, goalDist, totalDist, previousNode]
            if xDash in finalTableDict:
                finalTableDict[xDash] = tableRow
            else:
#                finalTableDict[xDash].append(tableRow)
                finalTableDict.update({xDash:tableRow})


#            finalTable.append(tableRow)
            '''
            for row in finalTable:
                print("Checking if xDash in FinalTabe already present:-", row, "XDASH: ", xDash)
                if (xDash not in row[0]):
                    print ("If ", xDash, " not inside ", row[0])
                    finalTable.append(tableRow)
                    break
            '''

        xDash = downR(x)       #Now adding the result of moving Down into the xDash
        if (xDash not in obstaclePoints):   #Checking if unvisited
#            openNodes.append(xDash)
            appendInOpen(xDash, openNodes)
            previousNode = x
            startDist = getDistance(x1, xDash)
            goalDist = getDistance(xDash, G)
            totalDist = startDist + goalDist
            tableRow = [xDash, startDist, goalDist, totalDist, previousNode]
            if xDash in finalTableDict:
                finalTableDict[xDash] = tableRow
            else:
#                finalTableDict[xDash].append(tableRow)
                finalTableDict.update({xDash:tableRow})


#            finalTable.append(tableRow)
            '''
            for row in finalTable:
                print("Checking if xDash in FinalTabe already present:-", row, "XDASH: ", xDash)
                if (xDash not in row[0]):
                    print ("If ", xDash, " not inside ", row[0])
                    finalTable.append(tableRow)
                    break
            '''

        closedNodes.append(x)
        openNodes.pop(0)

        minValue = 100000
        for node in openNodes:
            if (node not in closedNodes):
                if (node in finalTableDict):
                    temp = finalTableDict[node][3]
                    if (minValue > temp):
                        minValue = temp
                        x = node

#        sorted(finalTable, key=itemgetter(3))
        
#        for row in finalTable:       
#            print ("For ROW: ", row, " If ", row[0]," is in openNodes: ", openNodes)     
#            if (row[0] in openNodes):
#                x = row[0]
#                print ("Found x! ", x)
#                break
                
#        print(" ")
#        print("Closed: ", closedNodes)
#        print(" ")
#        print("Open: ", openNodes)
#        print(" ")
#        print("Final Table Dictionary: ", finalTableDict)
#        print(" ")
#        time.sleep(1)
#        print("New x is : ", x)
#        print(" ")


 #   print("Open Nodes:", openNodes)
 #   print(" ")
 #   print("Closed: ", closedNodes)
 #   print(" ")

    return finalTableDict


'''

##-----------------------------BREADTH FIRST SEARCH-----------------------------------------------------
Q = []
path = []
cost = 0
x1 = (15, 15)
G = (120,15)
visited = []
nodesInfo = []

def BFS(obstaclePoints, finalSquare):

    if (G in obstaclePoints) or (x1 in obstaclePoints):
        print("The point you chose is in the obstacle space, Choose another point")
        return 0

    Q.append(x1)     #Putting first state in Q
    visited.append(x1)     #Putting x1 in Visited

    print(" ")
    print("Q initial: ", Q, "visited initial: ", visited)
    print("Goal : ", G)
    print(" ")
    QSize = len(Q)


    while QSize != 0:       #Runs until Q is empty
        x = Q[0]

        if len(visited) >= 100000:  #Stop the computation if more than 100,000 nodes are visited
            print("Cannot find solution in finite time")
            print("x: ", x)
            print("visited Nodes: ", visited)
            break

        if x == G :     #Stop the computation if result is found
            visited.append(x)
            nodesInfo.append((visited.index(x), visited.index(x), cost))
            print("SUCCESS")
            break
    
        else:
            xDash = right(x)  #Now adding the result of moving right into the xDash
            if (xDash not in visited) and (xDash not in obstaclePoints):   #Checking if unvisited
                visited.append(xDash)
                Q.append(xDash)
                nodesInfo.append((visited.index(xDash), visited.index(x), cost))


            xDash = left(x)       #Now adding the result of moving left into the xDash
            if (xDash not in visited) and (xDash not in obstaclePoints):   #Checking if unvisited
                visited.append(xDash)
                Q.append(xDash)
                nodesInfo.append((visited.index(xDash), visited.index(x), cost))


            xDash = up(x)         #Now adding the result of moving up into the xDash
            if (xDash not in visited) and (xDash not in obstaclePoints):   #Checking if unvisited
                visited.append(xDash)
                Q.append(xDash)
                nodesInfo.append((visited.index(xDash), visited.index(x), cost))


            xDash = down(x)       #Now adding the result of moving Down into the xDash
            if (xDash not in visited) and (xDash not in obstaclePoints):   #Checking if unvisited
                visited.append(xDash)
                Q.append(xDash)
                nodesInfo.append((visited.index(xDash), visited.index(x), cost))


            xDash = upL(x)       #Now adding the result of moving Down into the xDash
            if (xDash not in visited) and (xDash not in obstaclePoints):   #Checking if unvisited
#                path.append("UL")
                visited.append(xDash)
                Q.append(xDash)
                nodesInfo.append((visited.index(xDash), visited.index(x), cost))
    
            xDash = upR(x)       #Now adding the result of moving Down into the xDash
            if (xDash not in visited) and (xDash not in obstaclePoints):   #Checking if unvisited
#                path.append("UR")
                visited.append(xDash)
                Q.append(xDash)
                nodesInfo.append((visited.index(xDash), visited.index(x), cost))

            xDash = downL(x)       #Now adding the result of moving Down into the xDash
            if (xDash not in visited) and (xDash not in obstaclePoints):   #Checking if unvisited
                visited.append(xDash)
                Q.append(xDash)
                nodesInfo.append((visited.index(xDash), visited.index(x), cost))

            xDash = downR(x)       #Now adding the result of moving Down into the xDash
            if (xDash not in visited) and (xDash not in obstaclePoints):   #Checking if unvisited
                visited.append(xDash)
                Q.append(xDash)
                nodesInfo.append((visited.index(xDash), visited.index(x), cost))

        Q.pop(0)        #Pop the node whose all the childrens are computed and stored
        
    return x

'''
