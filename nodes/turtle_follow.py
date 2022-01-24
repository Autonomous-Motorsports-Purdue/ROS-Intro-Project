#!/usr/bin/env python
import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn
from turtlesim.srv import SetPen
from turtlesim.msg import Pose

follower_turn_speed = 6
follower_move_speed = 1.25
follower_slowdown_dist = 1

user_pose = Pose()
follower_pose = Pose()

def setup_listeners():
    rospy.init_node('follow_controller', anonymous=True)
    rospy.Subscriber('turtle1/pose', Pose, user_pose_callback)
    rospy.Subscriber('follower/pose', Pose, follower_pose_callback)

def user_pose_callback(data):
    global user_pose
    user_pose = data

def follower_pose_callback(data):
    global follower_pose
    follower_pose = data

def control_follower():
    pub = rospy.Publisher('follower/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(60) # 60hz
    while not rospy.is_shutdown():
        delta_x = user_pose.x - follower_pose.x
        delta_y = user_pose.y - follower_pose.y
        
        angle_to_target = math.atan2(delta_y, delta_x)
        if (angle_to_target < 0): # normalize between 0 and 2pi
            angle_to_target += math.pi * 2
            
        # angle math that I bruteforced
        angle_diff = follower_pose.theta - angle_to_target
        if (angle_diff < 0): # normalize again
            angle_diff += math.pi * 2
        angle_diff -= math.pi
        angle_diff /= math.pi
        angle_diff = 1 - angle_diff
        if angle_diff > 1:
            angle_diff -= 2
        
        direction = Twist()
        direction.angular.z = angle_diff * follower_turn_speed
        slowdown_coeff = math.sqrt(delta_x ** 2 + delta_y ** 2) / follower_slowdown_dist
        if (slowdown_coeff > 1):
            slowdown_coeff = 1
        direction.linear.x = follower_move_speed * slowdown_coeff
        
        pub.publish(direction)
        rate.sleep()

if __name__ == '__main__':
    try:
        rospy.wait_for_service('spawn')
        spawn = rospy.ServiceProxy('spawn', Spawn)
        spawn(5, 5, 0, 'follower')
        rospy.wait_for_service('follower/set_pen')
        set_pen = rospy.ServiceProxy('follower/set_pen', SetPen)
        set_pen(255, 0, 0, 3, 0)
        setup_listeners()
        control_follower()
    except rospy.ROSInterruptException:
        pass
