#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt
from std_msgs.msg import String

def publisher():
        # Creates a node with name 'turtlebot_controller' and make sure it is a
        # unique node (using anonymous=True).
        rospy.init_node('turtlebot_controller', anonymous=True)
        pose_publisher = rospy.Publisher('/turtle1/pose', Pose, queue_size=10)
        pose = Pose()
        rate = rospy.Rate(1)
        while not rospy.is_shutdown():
            pose.x = round(pose.x, 4)
            pose.y = round(pose.y, 4)
            pose.theta = round(pose.theta, 4)
            rospy.loginfo(pose)
            pose_publisher.publish(pose)
            rate.sleep()

def update_pose():
    pose.x = round(pose.x, 4)
    pose.y = round(pose.y, 4)
    pose.theta = round(pose.theta, 4)


if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
