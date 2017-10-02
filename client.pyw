# Python Chat Client v1.0 by Matthew Taylor. See more at matthewaptaylor.github.io. This is licensed under the MIT license. This license requires credit to be given to the program's creator.
#socket.getfqdn()
import socket
import time
from easygui import *

connection = multenterbox("Enter connection information", "Python Chat Client", ["Host", "Port"])

host = connection[0]    # The remote host
port = int(connection[1])          # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while 1:
    name = multenterbox("Enter your name", "Python Chat Client", ["Name"])[0]
    if name != "":
        break

connectionInfo = [name, time.time(), socket.gethostbyname(socket.gethostname()), socket.getfqdn()]
s.sendall(str(connectionInfo))

while True:
    msg = multenterbox("Enter message", "Python Chat Client", ["Message"])[0]
    if msg != "":
        s.sendall(str(msg))

s.close()
