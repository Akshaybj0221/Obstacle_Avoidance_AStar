#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from nav_msgs.msg import OccupancyGrid
from nav_msgs.msg import MapMetaData
from geometry_msgs.msg import Pose



def callback(data):
#    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)	
	occupancyMap = data.data
#	print(occupancyMap)
	print("here ")
   
def callback2(data):
#    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.resolution)
	res = data.resolution
	w = data.width
	h = data.height
	o = data.origin
	print("res: ",res, "     W: ", w, "    H: ", h,)
	print( "o: ")
	print(o)
	
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

def map_listener():

	rospy.init_node('map_listener', anonymous=True) #initialze node named "map_listener"

#	occupancyMap = rospy.Subscriber("/map", OccupancyGrid, callback) #subscribe to /map

	dimensionMap = rospy.Subscriber("/map_metadata", MapMetaData, callback2)	
	print("dimension map height", dimensionMap[0])

	rospy.spin()   # spin() simply keeps python from exiting until this node is stopped




if __name__ == '__main__':
    map_listener()
