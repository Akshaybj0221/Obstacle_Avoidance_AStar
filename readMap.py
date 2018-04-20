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


class mapData:

#	def map_listener(self):
	'''	
	def __init__(self):
		rospy.init_node('map_listener', anonymous=True)
		#initialze node named"map_listener"
	
		rospy.Subscriber("/map", OccupancyGrid, self.callback) 
		#subscribe to /map	

		rospy.Subscriber("/map_metadata", MapMetaData, self.callback2)			
		
		self.gridConversion()
#		print(res)
	#	print("dimension map res", dimensionMap)
	
		rospy.spin()   # spin() simply keeps python from exiting until this node is stopped
	'''	
	def __init__(self, res, w, h, o, occupancyMap):
		self.res = res
		self.w = w
		self.h = h
		self.o = o
		self.occupancyMap = occupancyMap


	def callback(self, data):
	#    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)	
		self.occupancyMap = data.data
		self.occList = []
		self.occList.append(self.occupancyMap)


	def callback2(self, data):
	#    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.resolution)
		self.res = data.resolution
		self.w = data.width
		self.h = data.height
		self.o = data.origin

		self.mapData = []
		self.mapData.append(self.res)	
		self.mapData.append(self.w)
		self.mapData.append(self.h)	
		self.mapData.append(self.o)

#		rate = rospy.rate(10)
#		while not rospy.is_shutdown():
#			self.callback_pub.publish(data)	
#			rate.sleep()

		print("res: ",self.res, "     W: ", self.w, "    H: ", self.h)
#		print( "o: ")
#		print(self.o)
#		print("occupancy Map: ", self.xyz)
	
		
	def gridConversion(self):
#		print(self.res)

		files = open("/home/akshaybajaj/catkin_ws/src/astar_ttbot/new.txt", "r")
		lines = files.readlines()
		files.close()

		lines = lines[0]
		lines = [x for x in lines if x != ','] #remove all ','
		lines = lines[0:278528] #reduce the size to toal grid elements
		

		#Made a grid of 512*544
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
		obj = mapData(0, 0, 0, 0, 0)

		rospy.init_node('map_listener', anonymous=True)	#initialze node named"map_listener"

#		obj.callback_pub = rospy.Publisher("callback_res",MapMetaData, queue_size=10)

		rospy.Subscriber("/map", OccupancyGrid, obj.callback) #subscribe to /map	

		rospy.Subscriber("/map_metadata", MapMetaData, obj.callback2)			
		
#		obj = mapData()
		print(obj.res)

		obj.gridConversion()
#		obj.map_listener()
#		print(res)
#		mapData().map_listener()



#		self.gridConversion()
#		print(res)
	#	print("dimension map res", dimensionMap)
	
		rospy.spin()   # spin() simply keeps python from exiting until this node is stopped


	except rospy.ROSInterruptException:
		pass
