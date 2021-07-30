#!/usr/bin/env python

import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import sys
import numpy as np

bridge = CvBridge()


def detect(frame):

	#pub = rospy.Publisher('camera_image', Image, queue_size=100)
	pub = rospy.Publisher('camera_image', Image, queue_size=100)

	rospy.init_node('image_publisher', anonymous=True)
	image_message = bridge.cv2_to_imgmsg(frame,"bgr8")	
	pub.publish(image_message)



def main():
    

	cap = cv2.VideoCapture(0)
	print("dghh")
	#img = cv2.imread('Camera_image.jpg')
	#cv2.imshow('frame',img)
	while(True):
    		if cap.grab():
        		flag, frame = cap.retrieve()
        	if not flag:
            	continue
        else:
            cv2.imshow('video', frame)
    if cv2.waitKey(10) == 27:
        break
		try:
			
			detect(img)
		except rospy.ROSInterruptException:
			pass

		
		#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		#cv2.imshow('frame',gray)
		#if cv2.waitKey(1) & 0xFF == ord('q'):
		#	break

	# When everything done, release the capture
	#cap.release()
	#cv2.destroyAllWindows()



if __name__ == '__main__':
	main()

#cv2.waitKey(0)
#cv2.destroyAllWindows()
