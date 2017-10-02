# Python Chat Server v1.0 by Matthew Taylor. See more at matthewaptaylor.github.io. This is licensed under the MIT license. This license requires credit to be given to the program's creator.
import socket
import random
import os

HOST = "0.0.0.0"                 # Symbolic name meaning all available interfaces
PORT = random.randint(5000, 6000)              # Arbitrary non-privileged port

os.system("title " + "Python Chat Server")

print"""
===========
Chat Server
===========
"""

print "This program's connection info: "
print "Host: " + socket.gethostbyname(socket.gethostname())
print "Port: " + str(PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
name = ""

while 1:
    data = conn.recv(1024)
    if not data: break
    if name == "":
        exec("name = " + data + "[0]")
        os.system("title Chat with " + name + " - Python Chat Server")
        print
        print "Now chatting with " + name
        print
    else:
        print name + ": " + data
    conn.sendall(data)
conn.close()

#add clients to a list and iteratre through, checking is something new has been sent.
