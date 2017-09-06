# Echo client program
import socket

HOST = raw_input("Host: ")    # The remote host
PORT = int(raw_input("Port: "))           # The same port as used by the server

print"""
===========
Chat Client
===========
"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    s.sendall(raw_input("Enter message: "))
    #data = s.recv(1024)
    #print 'Received', repr(data)

s.close()

# Have one server, one app that makes messages, one app that receives them
