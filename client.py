import socket

HOST = raw_input("Host: ")
PORT = 5000

print"""
===========
Chat Client
===========
"""

while True:
    msg = raw_input("Enter message: ")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(msg)

s.close()