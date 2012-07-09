#!/usr/bin/python
import time, thread
from socket import *
myHost = ''
myPort = 50007

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(5)

def now():
    return time.ctime(time.time())

      
def handleClient(connection):
    time.sleep(5)        #simulate a blocking activity
    while True:
        data = connection.recv(1024)
        if not data: break
        reply = 'Echo=>%s at %s' % (data, now())
        connection.send(reply.encode())
    connection.close()
    
def dispatcher():
    while True:          #wait for next conncetion
        connection, address = sockobj.accept()
        print('Server connected by %s at %s' % (address, now()))
        thread.start_new_thread(handleClient, (connection,))
            
dispatcher()
    
