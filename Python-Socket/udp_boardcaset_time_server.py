#coding:utf-8
#udp server boardcast the time
#by wangkai001_tg@163.com
import traceback,time,struct
from socket import *
BUFSIZE = 65000
host = ''
port = 8085
#build a socket
sock = socket(AF_INET,SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sock.bind((host,port))
while 1:
    try:
	message,address = sock.recvfrom(BUFSIZE)
	secs = int(time.time())
	reply = struct.pack("!I",secs)
	sock.sendto(reply,address)
    except (KeyboardInterrupt,SystemExit):
	raise
    except:
	traceback.print_exc()
	
