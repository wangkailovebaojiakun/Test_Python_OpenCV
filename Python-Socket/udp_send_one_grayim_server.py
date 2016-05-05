#coding:utf-8
#coding:gbk
from socket import *
from time import ctime
import numpy as np
import cv2

HOST = '0.0.0.0'
PORT = 8082
BUFSIZE = 65534
ADDR = (HOST,PORT)

##AF_INET（又称 PF_INET）是 IPv4网络协议的套接字类型
##AF_INET6 则是 IPv6 的
##AF_UNIX 则是 Unix 系统本地通信。
##AF 表示ADDRESS FAMILY 地址族，PF 表示PROTOCOL FAMILY 协议族
##在windows中AF_INET与PF_INET完全一样。
##在Unix/Linux系统中，在不同的版本中这两者有微小差别
##对于BSD,是AF,对于POSIX是PF
##两个重要的类型是 SOCK_STREAM 和 SOCK_DGRAM。 
##SOCK_STREAM表明数据象字符流一样通过 socket,是基于TCP的 
##SOCK_DGRAM 则表明数据将是数据报(datagrams)的形式,是基于UDP的

udp_Ser_Sock = socket(AF_INET,SOCK_DGRAM)

'''--
调用bind()函数，为socket()函数创建的套接字关联一个相应地址，
发送到bind(地址)的数据可以通过该套接字读取与使用。
传送给参数addr的实际结构依赖于网络协议族
--'''
udp_Ser_Sock.bind(ADDR)
n_array = []
while True:
    print 'wating for message...'
#recvfrom()用来接收远程主机经指定的socket传来的数据,
#并把数据存到由参数data 指向的内存空间, 
#参数BUFSIZE 为可接收数据的最大长度. 
    data,addr = udp_Ser_Sock.recvfrom(BUFSIZE)
#接收客户端消息
    n_array = np.fromstring(data, np.uint8)
    if n_array.all():
        print n_array.shape
        print n_array.size
        break
im_array = n_array.reshape((200,133))
print im_array.shape
print im_array
cv2.namedWindow('test')
cv2.imshow('test',im_array)
cv2.waitKey(300)
udp_Ser_Sock.close()   
