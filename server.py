#!user/bin/python3

#server.py


import socket
import sys

serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()

port=9999

serversocket.bind((host,port))

serversocket.listen(5)

while 1:
    clientsocket.addr=serversocket.accept()

    print("连接地址：%s "%str(addr))
    print()
    msg='welcome to your comming'+"\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()
