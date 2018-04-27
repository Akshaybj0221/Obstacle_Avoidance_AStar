#!/usr/bin/env python
import rospy
import subprocess
from std_msgs.msg import String
from nav_msgs.msg import OccupancyGrid
from nav_msgs.msg import MapMetaData
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Quaternion

import matplotlib.pyplot as plt
import numpy as np
from numpy import loadtxt
import csv


#global occList	
#occList = []

def callback(data):
	occupancyMap = data.data
#	print(occupancyM

	occList = []
	occList.append(occupancyMap)
	print("c")

	out = open('/home/akshaybajaj/catkin_ws/src/astar_ttbot/rrl_custom_small_map_data.txt', 'w')
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

#	print("global occList from callback 1: ", occList)

#	rate = rospy.rate(10)
#	while not rospy.is_shutdown():
#		self.callback_pub.publish(data)	
#		rate.sleep()

	print("res: ",res, "     W: ", w, "    H: ", h)
#	print( "o: ")
#	print(self.o)
#	print("occupancy Map: ", self.xyz)
	

#def function1():
#	print(occList)


def gridConversion():
#	print(self.res)
	
	files = open("/home/akshaybajaj/catkin_ws/src/astar_ttbot/rrl_custom_small_map_data.txt", "r")
	lines = files.readlines()
	files.close()
	
	lines = lines[0]
#	print(lines)

#	lines = lines[0:len(lines)-2] #removing garbage value present at the end of the list (in string form)
	
	lines = lines.split(",")

#	lines = [x for x in lines if x != '\n'] #remove all ','
#	lines = [x for x in lines if x != ']'] #remove all ' '
	lines = [x for x in lines if x != ''] #remove all '''

	lines = list(map(int, lines))	#converting string elements in the list to int
#	print(lines)

	print(len(lines))
#	print(lines[16653])

#	lines = lines[0:278528] #reduce the size to toal grid elements
			
#	print("lines After removing things: ", lines)

	# Made a grid of 512*544
	row = []
	grid = []
	totalRow = 512
	totalCol = 544
		
	i=0
	while (i < totalRow):	
		j = 0
		while (j < totalCol):
			row.append(lines[i])
			j+=1
		grid.append(row)			
		row = []
		i += 1

#	nodeList = []
#	print("nodelist", nodelist)

#	print(grid[2])
#	count = 0
#	for i in grid:
#		count+=1
#		for j in grid[count]:
#			nodeList.append((i,j))		
#		print(nodeList)

	return grid

	'''
	occW = []
	occH = []
	count = 0

	for i in occupancyMap:
		count+=1
		if (count <= w):
			accW.append(i)
		if (count > w):
			accH.append(i)
	
	print("Width List: ", accW)
	print("Height List: ", accH)
	'''




if __name__ == '__main__':
	try:
#		global occList
		
		rospy.init_node('map_listener', anonymous=True)	#initialze node named"map_listener"

		rospy.Subscriber("/map", OccupancyGrid, callback) #subscribe to /map	

		rospy.Subscriber("/map_metadata", MapMetaData, callback2)  #subscribe to /map_metadata
		
		grid = gridConversion()
		print(grid)


		rospy.spin()   # spin() simply keeps python from exiting until this node is stopped


	except rospy.ROSInterruptException:
		pass
