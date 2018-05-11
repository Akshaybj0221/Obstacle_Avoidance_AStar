#!/usr/bin/env python
#import roslib; roslib.load_manifest('Phoebe')
import rospy

from nav_msgs.msg import Odometry

def callback(data):
#    print msg.pose.pose
#    completePose = data.data
    rospy.sleep(1)
    curr_time = data.header.stamp
    pose = data.pose.pose #  the x,y,z pose and quaternion orientation
    poseX = data.pose.pose.position.x
    poseY = data.pose.pose.position.y
    poseZ = data.pose.pose.position.z

#    print("Pose x:-")
    print(poseX)
#    print("All data", completePose)


if __name__ == "__main__":
    rospy.init_node('getPoseTTBot', anonymous=False) #make node 
    rospy.Subscriber('odom', Odometry, callback)
    rospy.spin()


