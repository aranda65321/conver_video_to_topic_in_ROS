# conver_video_to_topic_in_ROS
Hello, in this repository i will teach to how convert all format video to topic in Ros, then we will convert dato of topic in .bag file

#Fist step: we will create the package in ROS

In a console we execute the following command

$ roscore

In a new console we execute the following command

$ cd catkin_ws

$ cd src

now, we will create the package

$  catkin_create_make convertvideo rospy cv_bridge

In this moment we will create a package with the name convertvideo and this use rospy, cv_bridge librarys

#second step: we will create the script in python

 we execute the following command in console
 
 $ cd convertvideo
 
 $ mkdir nodes
 
 $ cd nodes
 
 $ touch code.py
 
 $ gedit code
 
 now open the text editor and copy, pasted the next code
 
 you will should change the path of video in the line 77  captura = cv2.VideoCapture('/home/user/catkin_ws/src/p_video/videos/video.mp4')
 
 
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

#iniciamos un nodo llamado image_pub

	rospy.init_node('image_pub')
  
#escribimos un mensaje informado que se ha iniciado el nodo

	rospy.loginfo('image_pub nodo iniciado')
  
#instanciamos al metodo CbBridge

bridge = CvBridge() 

#cargamos el video en este caso el video esta en una carpeta  del paquete

#el usuario debe cambiar esa ruta por la donde tiene su video

        captura = cv2.VideoCapture('/home/user/catkin_ws/src/p_video/videos/video.mp4')
        
#ahora separamos el video en frames, la variable cv_imagen es un frame del video

	ret, cv_imagen = captura.read()
  
#creamos un ciclo while que funciona reproducciendo y avanzando cada frame del video

	while (True):
  
	  ret, cv_imagen = captura.read()
    
#si se esta cargando la informacion o frames del video se hace lo siguiente

	  if ret == True:
    
#mostramos cada frame del video con un imshow

	    cv2.imshow('video', cv_imagen)
#convierto cada frame de open_cv a tipo imagen ros

	    imgMsg = bridge.cv2_to_imgmsg(cv_imagen, "bgr8")
      
#publicamos en un topic llamado video_to_topic la imagen convertida, el nombre del topic se puede cambiar

	    pub = rospy.Publisher('video_to_topic', Image)
      
            pub.publish(imgMsg)
            
##se crea un delay entre cada frame de 25 milisegundos

	    if cv2.waitKey(25) == ord('s'):
      
	      break
        
	  else: break
    
	captura.release()
  
	cv2.destroyAllWindows()
  
           
if __name__ == '__main__':

    try:
    
#funcion que se inicia con cuando ejecutamos el script, apenas se ejecuta el script llamamos a la funcion start_node que esta arriba

        start_node()
        
    except rospy.ROSInterruptException:
    
        pass

#

Now we will convert the data published in the topic to a bag file to be used later easily
in a new console we execute the following command
$ rosbag record video_to_topic
now ros saved the file .bag in the /home/user/ and we will have our .bag file where our video will be saved

