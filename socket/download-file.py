import sys, os, time, thread
from socket import *

blocksize = 1024
defaultHost = 'localhost'
defaultPort = 50001

helptext = ''' usage...'''

def now():
    return time.asctime()

def parseCmd():
    dict = {}
    args = sys.argv[1:]
    while len(args) >= 2:
        dict[args[0]] = args[1]
        args = args[2:]     #start after 2 items
    return dict

def client(host, port, filename):     #filename with path
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    sock.send((filename + '\n').encode())    #send filename with path to server
    dropdir = os.path.split(filename)[1]     #filename at the end of path
    file = open(dropdir, 'wb')        #create a local binary-mode file
    while True:                       #receive data from server
        data = sock.recv(blocksize)
        if not data: break
        file.write(data)
    sock.close()
    file.close()
    print('client got ', filename, ' at ', now())
    
def serverthread(clientsock):
    sockfile = clientsock.makefile('r')       #wrapper sock in binary file
    filename = sockfile.readline()[:-1]       #filename up to the end of file
    try:
        file = open(filename, 'rb')           #filename with path
        while True:
            bytes = file.read(blocksize)
            if not bytes: break
            sent = clientsock.send(bytes)
            assert sent == len(bytes)
    except:
        print('error downloading file on the server')
    clientsock.close()
    
def server(host, port):
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.bind((host, port))
    serversock.listen(5)
    while True:
        clientsock, clientaddr = serversock.accept()
        print('server connected by ', clientaddr, ' at', now())
        thread.start_new_thread(serverthread, (clientsock,))
        
def main(args):
    host = args.get('-host', defaultHost)
    port = args.get('-port', defaultPort)
    if args.get('-mode') == 'server':
        if host == 'localhost': host = ''
        server(host, port)
    elif args.get('-file'):
        client(host, port, args['-file'])    #client mode need file
    else:
        print(helptext)
        
if __name__ == '__main__':
    args = parseCmd()
    main(args)