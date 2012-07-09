from socket import *

#connect to POP server
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('pop.secureserver.net', 110))  #talk to pop server
print(sock.recv(70))
sock.close()

#connect to FTP server
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('learning-python.com', 21))
print(sock.recv(70))
sock.close()

#connect to HTTP server
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('www.python.net', 80))
#fetch root page only, type 7
sock.send(b'GET /\r\n')

#type two recv()
#sock.recv(70)
#sock.recv(70)
#sock.close()
