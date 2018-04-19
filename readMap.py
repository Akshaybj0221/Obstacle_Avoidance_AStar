#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from nav_msgs.msg import OccupancyGrid
from nav_msgs.msg import MapMetaData
from geometry_msgs.msg import Pose

class mapData(object):

#	def map_listener(self):
	
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
		

	def callback(self, data):
	#    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)	
		self.occupancyMap = data.data
		self.occList = []
		self.occList.append(self.occupancyMap)
#		self.xyz = [1,2,2,3]

	def callback2(self, data):
	#    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.resolution)
		self.res = data.resolution
		self.w = data.width
		self.h = data.height
		self.o = data.origin
				

#		print("res: ",self.res, "     W: ", self.w, "    H: ", self.h)
#		print( "o: ")
#		print(self.o)
#		print("occupancy Map: ", self.xyz)

		
	def gridConversion(self):
#		print(self.res)
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
		obj = mapData()
		print(obj.gridConversion())

#		obj.map_listener()
#		print(res)
#		mapData().map_listener()
	except rospy.ROSInterruptException:
		pass

