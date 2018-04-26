#!/usr/bin/env python
from astar_ttbot.srv import *
import rospy

def map_service_request(req):
    print "Returning [map parameters sent as (request) = ", req.map)
    return AddTwoIntsResponse(req.map)

def map_service_server():
    rospy.init_node('map_service_server')
    s = rospy.Service('map_service', mapService, map_service_request)
    print ("Ready to edit map parameters that we get from MAP_SERVICE_SERVER")
    rospy.spin()

if __name__ == "__main__":
    map_service_server()
