#!/usr/bin/env python
import rospy
import numpy as np
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


bridge=CvBridge()

def callback(ros_image):
	global bridge
	try:
		image=bridge.imgmsg_to_cv2(ros_image,"bgr8")
	except CvBridgeError as e:
		print(e)
	#cv2.imshow("Feed",image)
	#cv2.waitKey(3)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
	circles = cv2.HoughCircles(thresh, cv2.HOUGH_GRADIENT, 1, minDist=150, param1=200, param2=18, minRadius=0)
	if circles is not None:
	    circles = np.round(circles[0, :]).astype("int")
	    for (x,y,r) in circles:
		#cv2.circle(image, (x,y), r, (36,255,12), 2)
		cv2.rectangle(image,(x-r,y+r),(x+r,y-r), (0,255,0), 1)

	#cv2.imshow('thresh', thresh)
	cv2.imshow('image', image)
	cv2.waitKey(3)

if __name__=='__main__':
	rospy.init_node('display',anonymous= True)
	rospy.Subscriber("/usb_cam/image_raw",Image,callback)
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print("shutting down")
	cv2.destroyAllWindows()

