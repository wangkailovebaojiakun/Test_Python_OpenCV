from socket import *
import os
import stat
import struct
import numpy as np
import cv2

MAX_PACK_SIZE = 100
A_IP  = 'localhost'
A_PORT = 8082
ADDR = (A_IP,A_PORT)
filename = '/home/wk/Pictures/test.jpg'
filesize = os.stat(filename)[stat.ST_SIZE]

im = cv2.imread(filename,0)
f_array = np.array(im,'uint8')
f_string = im.tostring()
 
print f_array
print f_array.shape
print f_array.size
data = f_string
#build a  socket with addr  
udp_Socket = socket(AF_INET,SOCK_DGRAM)
udp_Socket.sendto(data,ADDR)
udp_Socket.close()
