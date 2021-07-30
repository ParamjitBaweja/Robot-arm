#!/usr/bin/env python3
import rospy
import time
import random
import sys
import getch
from geometry_msgs.msg import Twist
if __name__=='__main__':
	rospy.init_node('teleop')
	pub=rospy.Publisher("/cmd_vel",Twist,queue_size=10)
	print("w for forward,\ns for backward,\na for left,\nd for right,\nv for screw,\nu for unscrew,t for switching tool \nk to kill")
	while True:
		msg=Twist()
		sys.stdout.flush()
		char=getch.getch()
		#print(char)
		sys.stdout.flush()
		if (char=='w'):
			msg.linear.x=3
		elif(char=='s'):
			msg.linear.x=0
			msg.angular.z=0
		elif(char=='a'):
			msg.linear.x=3
			msg.angular.z=0.3
		elif(char=='d'):
			msg.linear.x=3
			msg.angular.z=-0.3
		elif(char=='k'):
			exit()
		else:
			msg.linear.x=0
			msg.angular.z=0
		pub.publish(msg)
		msg.linear.x=0
		msg.angular.z=0
				
