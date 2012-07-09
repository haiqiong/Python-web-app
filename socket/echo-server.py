from socket import *
myHost = ''      #get the machine that the script runs on
myPort = 50007

sockobj = socket(AF_INET, SOCK_STREAM)       #IP/TCP protocol
sockobj.bind((myHost, myPort))
sockobj.listen(5)          #The size of the queue of incoming requests

while True:
    connection, address = sockobj.accept() #a new sockobj for the request client
    print('Server connected by ', address) #address is IP addr.
    while True:
        data = connection.recv(1024)        #data is byte string
        if not data: break
        connection.send(b'Echo=>' + data)
    connection.close()