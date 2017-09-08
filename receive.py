import socket
import random

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5100

print"""
===========
Chat Receive
===========
"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
while 1:
    s.listen(1)
    conn, addr = s.accept()
    data = conn.recv(1024)
    if not data: break
    print data
    conn.sendall(data)
conn.close()