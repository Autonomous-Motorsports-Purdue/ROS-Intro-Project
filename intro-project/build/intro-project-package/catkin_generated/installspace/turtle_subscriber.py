#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from turtlesim.msg import Pose

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data)

def subscribe():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('subscriber', anonymous=True)

    rospy.Subscriber('pose_topic', Pose, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    subscribe()
