import sys
from socket import *

serverHost = 'localhost'
serverPort = 50007

message = [b'Hello network world']

if len(sys.argv) > 1:
    serverHost = sys.argv[1]  #server from cmd line arg 1
    if len(sys.argv) > 2:     #test frm cmd line args 2...n
        message = (x.encode() for x in sys.argv[2:])
        
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))

for line in message:
    sockobj.send(line)           #send line to server over socket
    data = sockobj.recv(1024)    #receive replay from the server
    print('Clinet received:', data)

sockobj.close()