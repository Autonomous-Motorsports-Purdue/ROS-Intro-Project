#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt
from std_msgs.msg import String
import math

pos1 = Pose()
pos2 = Pose()

def follow():
        global pos1
        global pos2
        # Creates a node with name 'turtlebot_controller' and make sure it is a
        # unique node (using anonymous=True).
        rospy.init_node('turtlebot_controller', anonymous=True)
        pose1_sub = rospy.Subscriber('/turtle1/pose', Pose, update_pose1)
        pose2_sub = rospy.Subscriber('/turtle2/pose', Pose, update_pose2)
        # Publisher which will publish to the topic '/turtle2/cmd_vel'.
        pub1 = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)
        rate = rospy.Rate(1)
        while not rospy.is_shutdown():
            twist = Twist()
            if math.hypot(pos1.x - pos2.x, pos1.y - pos2.y) > 1:
                twist.linear.x = 1
            else:
                twist.linear.x = 0;
            angle = math.atan2(pos1.y-pos2.y, pos1.x-pos2.x) - pos2.theta
            twist.angular.z = angle
            pub1.publish(twist)
            rospy.loginfo(twist)
            rate.sleep()

def update_pose1(data):
    global pos1
    pos1 = data
    

def update_pose2(data):
    global pos2
    pos2 = data




if __name__ == '__main__':
    try:
        follow();
    except rospy.ROSInterruptException:
        pass
