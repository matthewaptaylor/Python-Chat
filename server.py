import socket
import random

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5000

ip = []

print"""
===========
Chat Server
===========
"""

print "Connect to this computer by opening the client app, and typing this in the host: " + HOST

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
while 1:
    s.listen(1)
    conn, addr = s.accept()
    data = conn.recv(1024)
    print "Connected to: " + str(addr) + ", Message: " + data
    if not data: break
    if ip.count(addr[0]) == 0:
        ip.append(addr[0])
    for x in ip:
        sR = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sR.connect((x, 5100))
        sR.sendall(data)
        sR.close()
    conn.sendall(data)
conn.close()