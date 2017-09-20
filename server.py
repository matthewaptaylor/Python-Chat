# Python chat server by Matthew Taylor. See more at matthewaptaylor.github.io. This is licensed under the MIT license. This license requires credit to be given to the program's creator.
import socket
import random

HOST = socket.gethostbyname(socket.gethostname())                 # Symbolic name meaning all available interfaces
PORT = random.randint(5000, 6000)              # Arbitrary non-privileged port

print"""
===========
Chat Server
===========
"""

print "Connect to this computer by opening the client app, and typing this in the host: " + HOST
print "and this in the port: " + str(PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected to: ', addr
while 1:
    data = conn.recv(1024)
    if not data: break
    print data
    conn.sendall(data)
conn.close()

#add clients to a list and iteratre through, checking is something new has been sent.
