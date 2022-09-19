#!/usr/bin/env python

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt, cos, sin, pi


turtle1_pos = Pose()
turtle2_pos = Pose()


def publish():
    rospy.init_node('manual_turtle', anonymous=True)

    turtle1_subscriber = rospy.Subscriber("turtle1/pose", Pose, update_pos_1)
    turtle2_subscriber = rospy.Subscriber("turtle2/pose", Pose, update_pos_2)

    turtle2_publisher = rospy.Publisher("turtle2/cmd_vel", Twist, queue_size=10)
    
    
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        twist = calculate_twist()
        rospy.loginfo(twist)
        rospy.loginfo(rate)

        turtle2_publisher.publish(twist)

        rate.sleep()

def update_pos_1(data):
    global turtle1_pos
    turtle1_pos = data

def update_pos_2(data):
    global turtle2_pos
    turtle2_pos = data

def get_angle_to_turn():
    global turtle1_pos
    global turtle2_pos

    heading = atan2(turtle1_pos.y - turtle2_pos.y, turtle1_pos.x - turtle2_pos.x)
    angle_to_turn = heading - turtle2_pos.theta

    #make angle more efficient
    if(angle_to_turn > pi):
        angle_to_turn = angle_to_turn - 2 * pi
    if(angle_to_turn < -pi):
        angle_to_turn = angle_to_turn + 2 * pi

    return angle_to_turn

def calculate_twist():
    global turtle1_pos
    global turtle2_pos

    angle_to_turn = get_angle_to_turn()
    twist = Twist()

    angle_threshold = 0.1
    angular_speed_factor = 10
    linear_speed = 2

    if(abs(angle_to_turn) > angle_threshold):
        twist.angular.z = angular_speed_factor * angle_to_turn
    else:
        twist.linear.x = linear_speed

    return twist

    

if __name__ == '__main__':
    try:
        publish()

    except rospy.ROSInterruptException:
        pass
