#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math 

pose1: Pose = Pose()
pose2: Pose = Pose()

def sub1cb(data):
    global pose1
    pose1 = data

def sub2cb(data):
    global pose2
    pose2 = data    


def turtlefollow():
    global pose1, pose2 

    rospy.init_node("turtlefollow")
    pub = rospy.Publisher("turtle2/cmd_vel", Twist)
    sub1 = rospy.Subscriber("turtle1/pose", Pose, sub1cb)
    sub2 = rospy.Subscriber("turtle2/pose", Pose, sub2cb)
    rate = rospy.Rate(60)

    while not rospy.is_shutdown():
        vel = Twist()
        vel.linear.x = 1 if (pose1.y-pose2.y)**2 + (pose1.x-pose2.x)**2 > 1 else 0 
        angleDif = (math.atan2(pose1.y-pose2.y,pose1.x-pose2.x) - pose2.theta) % math.tau 
        if angleDif > math.pi: vel.angular.z -= math.tau
        
        vel.angular.z = angleDif

        rospy.loginfo(vel)

        pub.publish(vel)
        
        rate.sleep()


if __name__ == "__main__":
    try:
        turtlefollow()
    except rospy.ROSInterruptException:
        pass
