
#!/usr/bin/env python3
import rospy
import csv
import pygame
import math
from std_msgs.msg import String
from nav_msgs.msg import OccupancyGrid
from nav_msgs.msg import MapMetaData
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Quaternion
import numpy as np
from numpy import loadtxt
import matplotlib.pyplot as plt
import AStar_Grid3
from AStar_Grid3 import *



def callback(data):
	occupancyMap = data.data

	occList = []
	occList.append(occupancyMap)

	# Writing static_map values from the file 'mapData.txt' 
	out = open('/home/viki/rosRoboticsByExample_WS/src/astar_ttbot/config/mapData.txt', 'w')
	for row in occList:
		for column in row:
			out.write('%d,' % column)
		out.write('\n')
	out.close()
	

def callback2(data):
	res = data.resolution
	w = data.width
	h = data.height
	o = data.origin

	mapData = []
	mapData.append(res)	
	mapData.append(w)
	mapData.append(h)	
	mapData.append(o)


def gridConversion():
	# Reading static_map values from the file 'mapData.txt' 
	files = open("/home/viki/rosRoboticsByExample_WS/src/astar_ttbot/mapData.txt", "r")
	
	lines = files.readlines()
	files.close()
	
	lines = lines[0]
	lines = lines.split(" ")


	lines = [x for x in lines if x != '\n'] #remove all '\n'
	lines = [x for x in lines if x != ''] #remove all ''
	lines = [x for x in lines if x != ' '] #remove all ' ' 

	lines = list(map(int, lines))	#converting string elements in the list to int

	lines = [x for x in lines if x != ''] #remove all '''

	lines = list(map(int, lines))	#converting string elements in the list to int


	row = []
	grid = []
	totalCol = 544
	totalRow = 512
	count = 0

	for i in lines:
		count += 1
		row.append(i)

		if ((count%totalRow) == 0):
			grid.append(row)
			row = []

	return grid

# Calling gridCOnversion function to convert linear map data to the grid width and length
grid = gridConversion()

#Convert grid into list of tuples:
finalMap = []
row =0
col =0
for i in grid:
	row += 1
	col = 0
	for j in i:
		col += 1
		finalMap.append((row-1, col-1, j))


# Obstacle points is the list of free-space nodes in the map
obstaclePoints = []
for i in finalMap:
	if (i[2] == 0):
		obstaclePoints.append((i[0],i[1]))


print("Processing...")
print(" ")


# Calling A Star Algorithm
completeTable = aStar(obstaclePoints)
print(" ")


# Getting nodes for final Path from the table into a list 'n'
finalNode = G
n = []
n.append(G)

while(finalNode != x1):
    temp = completeTable[finalNode][4]
    n.append(temp)
    finalNode = temp


# Printing nodes of path which we get from A Star Algorithm
print("Final Path:-")
print(n)

print(" ")
print("Finding linear and angular velocities for turtlebot")
print("Storing velocities into a file 'turtlebot_velocities'....")


#Finding angular velocities from final path nodes i.e. list "n"
time = 0.5 #sec (constant due to contant MHz range)
velocitiesList = []
num = 0
while (num < len(n)-1):
	num += 1
	X2 = n[num][0] #1st value of the next node tuple
	X1 = i[0]	#1st value of the current node tuple
	Y2 = n[num-1][1] #2nd value of the next node tuple
	Y1 = i[1] #2nd value of the current node tuple

	linearX = (X2 - X1)/time
	linearY = (Y2 - Y1)/time

	if (linearX == 0) :
		print("No change in theta",theta)
	else:
		theta = math.atan(linearY/linearX) #Finding tan inverse
	
	angularZ = theta/time	#angular velocity is angle divided by time (contant time, i.e. 0.5)
	velocitiesList.append((linearX/1000, linearY/1000, angularZ))	# Adding linear velocities in Meter/sec thats why dividing it by 1000


# Printing list of final linear and angular velocities that turtlebot should follow
print(" ")
print("Final Velocities to be published are as follows:-")
print(velocitiesList)


# Writing the velocities in a file named 'turtlebot_velocities'
out = open('/home/viki/rosRoboticsByExample_WS/src/astar_ttbot/turtlebot_velocities.txt', 'w')
for row in velocitiesList:
	for column in row:
		out.write('%f ' % column)
	out.write('\n')
out.close()


# Mai of the script
if __name__ == '__main__':
	try:		
		rospy.init_node('map_listener', anonymous=True)	#initialze node named"map_listener"

		rospy.Subscriber("/map", OccupancyGrid, callback) #subscribe to /map	

		rospy.Subscriber("/map_metadata", MapMetaData, callback2)  #subscribe to /map_metadata
		
		rospy.spin()   # spin() simply keeps python from exiting until this node is stopped


	except rospy.ROSInterruptException:
		pass
