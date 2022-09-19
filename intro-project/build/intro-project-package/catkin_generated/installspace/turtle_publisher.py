#!/usr/bin/env python3

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt, cos, sin, pi


turtle1_pos = Pose()
turtle2_pos = Pose()


def update_pos_1(data):
    global turtle1_pos
    turtle1_pos = data

def update_pos_2(data):
    global turtle2_pos
    turtle2_pos = data

def publish():
    #velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
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
        #velocity_publisher.publish()

        rate.sleep()

def distancToTurtle1() {
    global turtle1_pos
    global turtle2_pos

    return sqrt(pow(turtle1_pos.x - turtle2_pos.x, 2) + pow(turtle1_pos.y - turtle2_pos.y, 2))
}

def getAngleToTurn() {
    global turtle1_pos
    global turtle2_pos

    heading = atan2(turtle1_pos.y - turtle2_pos.y, turtle1_pos.x - turtle2_pos.x)
    angleToTurn = heading - turtle2_pos.theta

    //make angle more efficient for turtle to turn
    if(angleToTurn > PI):
        angleToTurn = angleToTurn - 2 * PI
    if(angleToTurn < -PI):
        angleToTurn = angleToTurn + 2 * PI
}

def calculate_twist():
    global turtle1_pos
    global turtle2_pos

    distance = distanceToTurtle1()
    angleToTurn = getAngleToTurn()
    twist = Twist()

    if(distance > 0.1):
        if(abs(angleToTurn) > 0.1):
            twist.linear.x = 0.0
            twist.angular.z = 0.5 * angleToTurn
        else:
            twist.linear.x = distance * 0.5
            twist.angular.z = 0.0
    else:
        twist.linear.x = 0.0
        twist.angular.z = 0.0
    
    twist.angular.z = angle #Make turtle2 go in direction of turtle1

    twist.linear.x = 3

    return twist

    

if __name__ == '__main__':
    try:
        publish()

    except rospy.ROSInterruptException:
        pass
