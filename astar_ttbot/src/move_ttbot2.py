# Script to move the TurtleBot 2  on a path trajectory for the map
# Written for indigo

#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose, Point, Quaternion
from nav_msgs.msg import Odometry
from math import radians


def shutdown():
    # stop turtlebot
    rospy.loginfo("Stop Drawing Squares")
    cmd_vel.publish(Twist())
    rospy.sleep(1)
 


def getData():
    print("Inside")
    rospy.loginfo("Inside getData")

    lines = []
    with open("/home/akshaybajaj/ttbot_ws/src/astar_ttbot/SampleCommands2.txt") as file:
        for line in file: 
            line = line.strip() #or some other preprocessing
            lines.append(line) #storing everything in memory!
    
    final = []
    for i in lines:
        n = i.split(" ")
        final.append(n)    

    return final


if __name__ == '__main__':
    try:

        linearVel = getData()
 
        # initiliaze
        rospy.init_node('drawasquare', anonymous=False)

        # What to do you ctrl + c
        rospy.on_shutdown(shutdown)
        
        cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
     
        # 5 HZ
#        r = rospy.Rate(5);
        r = rospy.Rate(2); #2 HZ

        # create a Twist() variable for moving forward
        # let's go forward at 0.2 m/s
        move_cmd = Twist()

        #two keep drawing squares.  Go forward for 2 seconds (10 x 5 HZ) then turn for 2 second
        count = 0
        while not rospy.is_shutdown():
#            print(count, ":   ", linearVel[count][0], ":", linearVel[count][1])
#            print(type(linearVel[count][0]), type(linearVel[count][1]))

            # let's go forward at 0.2 m/s
            move_cmd.linear.x = float(linearVel[count][0])
            move_cmd.angular.z = float(linearVel[count][1])
            count += 1

            print(count, " : ", "Linear Velocity: ", move_cmd.linear.x, "\tAngular Velocity: ", move_cmd.angular.z)
            # go forward 0.4 m (2 seconds * 0.2 m / seconds)
            rospy.loginfo("Moving Forward")
            for x in range(0,1):
                cmd_vel.publish(move_cmd)
                r.sleep()

    except:
    	rospy.loginfo("node terminated.")
