# Convertir videos a topic en Ros
_Hola a todos, en este repositorio enseñaré cómo convertir videos de cualquier formatos a topics usando la plataforma de simulacion de robots Ros,  para luego convertir los datos captado en un archivo de datos tipo bag_

### Pre requisitos  📋

_Debes tener instalado los siguientes softwares y librerias_

```
Sistema operativo Linux preferiblemete la version ubuntu 19.04
Instalado ROS con todas sus librerias actualizadas, version Melodic
Librerias de Python
Librerias de open_cv

```


### Instalación 🔧


_Para el correcto funcionamiento del script convert.py debes realizar los siguientes pasos_

_Paso 1: crearemos el paquete en ROS tecleando los siguientes comando en una nueva consola, la llamaremos consola 1_

```
$ roscore

```

_En una nueva consola ejecutamos el siguiente comando, dejando la consola 1 ejecutandose aparte_

```
$ cd catkin_ws

$ cd src
```
_En este punto crearemos un paquete con el nombre convertvideo y este usaremos rospy, cv_bridge librarys_

```
$  catkin_create_make convertvideo rospy cv_bridge

```

_Paso 2: crearemos un script en python en donde seleccionaremos un video y lo convertiremos a topic, para que luego el codigo de convert.py tenga un topic del cual reciba informacion_

_Ejecutamos los siguientes comandos_

 ```
 $ cd convertvideo
 
 $ mkdir nodes
 
 $ cd nodes
 
 $ touch code.py
 
 $ gedit code
 
 ```
 _ahora abra el editor de texto y copie, pegue el siguiente código_
 
 ```
Deberáscambiar la ruta del video en la línea 77 captura = cv2.VideoCapture ('/ home / user / catkin_ws / src / p_video / videos / video.mp4'), por la ubicacion donde se encuentre el video
 ```
_CODIGO_
 ```
 
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
 ```
_Paso 3:_
```
Ahora convertiremos los datos publicados en el tema a un archivo bag para poder usarlo más tarde fácilmente
en una nueva consola ejecutamos el siguiente comando
$ rosbag grabar video_to_topic
ahora ros guardó el archivo .bag en / home / user / y tendremos nuestro archivo .bag donde se guardará nuestro video
```
## Autores ✒️
* **Juan Camilo Aranda** - *Desarrollo script* - 

