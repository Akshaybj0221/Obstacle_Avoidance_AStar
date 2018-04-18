#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from nav_msgs.msg import OccupancyGrid
from nav_msgs.msg import MapMetaData
from geometry_msgs.msg import Pose

class mapData:
	def callback(self, data):
	#    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)	
		self.occupancyMap = data.data
		self.occList = []
		self.occList.append(occupancyMap)
		return 

	def callback2(self, data):
	#    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.resolution)
		self.res = data.resolution
		self.w = data.width
		self.h = data.height
		self.o = data.origin
	#	print("res: ",res, "     W: ", w, "    H: ", h,)
	#	print( "o: ")
	#	print(o)
	

	def gridConversion(self, list1, list2):
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

	def map_listener(self):

		self.rospy.init_node('map_listener', anonymous=True) 
		#initialze node named"map_listener"
	
		self.rospy.Subscriber("/map", OccupancyGrid, callback) 
		#subscribe to /map	

		self.rospy.Subscriber("/map_metadata", MapMetaData, callback2)			

	#	print("dimension map res", dimensionMap)
	
		self.rospy.spin()   # spin() simply keeps python from exiting until this node is stopped




if __name__ == '__main__':
    map_listener()
