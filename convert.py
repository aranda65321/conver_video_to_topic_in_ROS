#!/usr/bin/env python
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from Conversion_video_to_frame import conver_video_to_image
import rospy
import sys
import cv2
import os
import time


def start_node():
#we start a node called image_pub
	rospy.init_node('image_pub')
#we write a message informed that the node has started
	rospy.loginfo('image_pub nodo iniciado')
#instance the CbBridge function
	bridge = CvBridge() 
# we load the video in this case the video is in a folder of the package
#the user must change that path to the one where they have their video
        captura = cv2.VideoCapture('/home/k-milo/catkin_ws/src/p_video/videos/video.mp4')
#Now we separate the video into frames, the variable cv_imagen is a frame of the video
	ret, cv_imagen = captura.read()
# we create a while loop that works by playing and advancing each frame of the video
	while (True):
	  ret, cv_imagen = captura.read()
#if the information or video frames are being loaded, do the following
	  if ret == True:
#show each frame of the video with an imshow
	    cv2.imshow('video', cv_imagen)
#convert each frame from open_cv to image type ros
	    imgMsg = bridge.cv2_to_imgmsg(cv_imagen, "bgr8")
# we publish the converted image in a topic called video_to_topic, the name of the topic can be changed
	    pub = rospy.Publisher('video_to_topic', Image)
            pub.publish(imgMsg)
# a delay between each frame of 25 milliseconds is created
	    if cv2.waitKey(25) == ord('s'):
	      break
	  else: break
	captura.release()
	cv2.destroyAllWindows()
            


if __name__ == '__main__':
    try:
#function that starts with when we execute the script, as soon as the script is executed we call the start_node function that is above
        start_node()
    except rospy.ROSInterruptException:
        pass

