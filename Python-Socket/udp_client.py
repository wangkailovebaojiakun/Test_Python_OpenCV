from socket import *

HOST = 'localhost'
PORT = 8080
BUFSIZE = 1024
ADDR = (HOST,PORT)
udp_cli_sock = socket(AF_INET,SOCK_DGRAM)
while True:
    data = raw_input('>')
    if not data:
        break
    udp_cli_sock.sendto(data,ADDR)
    data,ADDR = udp_cli_sock.recvfrom(BUFSIZE)
    if not data:
        break
    print data
udp_cli_sock.close()
