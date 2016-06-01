#coding:utf-8
#send a char to the server and get the time
#by wangkai001_tg@163.com
from socket import *
import sys,struct,time

BUFSIZE = 65000
host = raw_input('Please input the address of the server:')
port = 8085
sock = socket(AF_INET,SOCK_DGRAM)
sock.sendto('',(host,port))
print 'Waiting for reply...'
buf = sock.recvfrom(BUFSIZE)[0]
if len(buf) != 4:
    print 'The reply is wrong!%d:%s'%(len(buf),buf)
    sys.exit(1)
secs = struct.unpack('!I',buf)[0]
print time.ctime(int(secs))

