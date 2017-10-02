<<<<<<< HEAD
# Python Chat Server v1.0 by Matthew Taylor. See more at matthewaptaylor.github.io. This is licensed under the MIT license. This license requires credit to be given to the program's creator.
=======
# Python chat server by Matthew Taylor. See more at matthewaptaylor.github.io. This is licensed under the MIT license. This license requires credit to be given to the program's creator.
>>>>>>> 238b87f42b80f11ab88e5b4abb32fbcceae088e9
import socket
import random
import os

<<<<<<< HEAD
HOST = "0.0.0.0"                 # Symbolic name meaning all available interfaces
PORT = random.randint(5000, 6000)              # Arbitrary non-privileged port

os.system("title " + "Python Chat Server")
=======
HOST = socket.gethostbyname(socket.gethostname())                 # Symbolic name meaning all available interfaces
PORT = random.randint(5000, 6000)              # Arbitrary non-privileged port
>>>>>>> 238b87f42b80f11ab88e5b4abb32fbcceae088e9

print"""
===========
Chat Server
===========
"""

<<<<<<< HEAD
print "This program's connection info: "
print "Host: " + socket.gethostbyname(socket.gethostname())
print "Port: " + str(PORT)
=======
print "Connect to this computer by opening the client app, and typing this in the host: " + HOST
print "and this in the port: " + str(PORT)
>>>>>>> 238b87f42b80f11ab88e5b4abb32fbcceae088e9

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
<<<<<<< HEAD
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
=======
print 'Connected to: ', addr
while 1:
    data = conn.recv(1024)
    if not data: break
    print data
>>>>>>> 238b87f42b80f11ab88e5b4abb32fbcceae088e9
    conn.sendall(data)
conn.close()

#add clients to a list and iteratre through, checking is something new has been sent.
