#!/usr/bin/env python

import sys
import rospy
from astar_ttbot.srv import *

def map_service_client(mapParam):
    rospy.wait_for_service('map_service')
    try:
        map_service = rospy.ServiceProxy('map_service', mapService)
        resp1 = map_service(mapParam)
        return mapParam
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print usage()
        sys.exit(1)
    print "Requesting %s+%s"%(x, y)
    print "%s + %s = %s"%(x, y, add_two_ints_client(mapParam))
