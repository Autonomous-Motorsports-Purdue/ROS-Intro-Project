#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt
from std_msgs.msg import String

pose = Pose()

def subscriber():
        # Creates a node with name 'turtlebot_controller' and make sure it is a
        # unique node (using anonymous=True).
        rospy.init_node('turtlebot_controller', anonymous=True)
        pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, update_pose)
        # Publisher which will publish to the topic '/turtle2/cmd_vel'.
        velocity_publisher = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)
        turtle2_subscriber = rospy.Subscriber('/turtle2/cmd_vel', Pose, update_pose)
        rate = rospy.Rate(1)
        while not rospy.is_shutdown():
            rospy.loginfo(pose)
            rate.sleep()

def update_pose(data):
    global pose
    pose = data
    pose.x = pose.x
    pose.y = pose.y
    pose.theta = pose.theta


if __name__ == '__main__':
    try:
        subscriber();
    except rospy.ROSInterruptException:
        pass
