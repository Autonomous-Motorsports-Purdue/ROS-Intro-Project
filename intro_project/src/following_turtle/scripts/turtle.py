#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt

class Following_Turtle:

	def __init__(self):
		rospy.init_node('turtle', anonymous=True)

		self.pose = Pose()
		self.goal = Pose()

		# Things for following turtle
		self.velo_pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)
		self.pose_sub = rospy.Subscriber("turtle2/pose", Pose, self.update_pose)
		# Update goal
		self.goal_sub = rospy.Subscriber("turtle1/pose", Pose, self.update_goal)
		
	def update_pose(self, data):
		self.pose = data
		self.pose.x = round(self.pose.x, 4)
		self.pose.y = round(self.pose.y, 4)

	def update_goal(self,data):
		self.goal = data
		self.goal.x = round(self.goal.x, 4)
		self.goal.y = round(self.goal.y, 4)

	def steering_angle(self):
		return atan2(self.goal.y - self.pose.y, self.goal.x - self.pose.x)

	def linear_vel(self, constant=0.7):
		distance = sqrt(pow((self.goal.x - self.pose.x), 2) + 
				pow((self.goal.y - self.pose.y), 2))
		if distance > 0.5:
			return constant
		elif distance > 0.05:
			return constant * distance
		else:
			return 0
	
	def angular_vel(self, constant=5):
		return constant * (self.steering_angle() - self.pose.theta)

	def follow(self):
		vel_msg = Twist()
		while True:
			vel_msg.linear.x = self.linear_vel()
			vel_msg.linear.y = 0
			vel_msg.linear.z = 0

			vel_msg.angular.x = 0
			vel_msg.angular.y = 0
			vel_msg.angular.z = self.angular_vel()

			self.velo_pub.publish(vel_msg)
		
		vel_msg.linear.x = 0
		vel_msg.angular.z = 0
		self.velo_pub.publish(vel_msg)

		rospy.spin()
			

if __name__ == '__main__':
	turtle = Following_Turtle()
	turtle.follow()
