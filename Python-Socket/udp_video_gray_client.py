from socket import *
import os
import stat
import struct
import numpy as np
import cv2

def get_imlist(path):
    path = path+'/image'
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

A_IP  = 'localhost'
A_PORT = 8083
ADDR = (A_IP,A_PORT)
imlist = get_imlist(os.getcwd())
imlist.sort()
#build a  socket with addr  
udp_Socket = socket(AF_INET,SOCK_DGRAM)
imlist_len = len(imlist)
print imlist_len
file_num = 0
for filename in imlist:
    im = cv2.imread(filename,0)
    global imlist_len
    global file_num
    file_num = file_num+1
    im=cv2.resize(im,(120,160),interpolation=cv2.INTER_CUBIC)
    f_array = np.array(im,'uint8')
    f_string = im.tostring()
    data = f_string
    stopkey = cv2.waitKey(20)
    udp_Socket.sendto(data,ADDR)

    if (stopkey == 27)|(file_num==imlist_len):
        udp_Socket.sendto('stop',ADDR)
	print file_num
	break
udp_Socket.close()
