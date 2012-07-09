import os, time, sys, signal
from socket import *
myHost = ''
myPort = 50007

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(5)
signal.signal(signal.SIGCHLD, signal.SIG_IGN)     #avoid dead child processes

def now():
    return time.ctime(time.time())

'''
activeChildren = []
def reapChildren():      #reap dead child processes
    while activeChildren:
        pid, stat = os.waitpid(0, os.WNOHANG)
        if not pid: break
        activeChildren.remove(pid)
'''        
def handleClient(connection):
    time.sleep(5)        #simulate a blocking activity
    while True:
        data = connection.recv(1024)
        if not data: break
        reply = 'Echo=>%s at %s' % (data, now())
        connection.send(reply.encode())
    connection.close()
    os._exit(0)
    
def dispatcher():
    while True:          #wait for next conncetion
        connection, address = sockobj.accept()
        #print('Server connected by', address, end='')
        print('Server connected by %s at %s' % (address, now()))
        #reapChildren()   #clean up exit child processes
        childPid = os.fork()    #copy this process
        if childPid == 0:    #if in child process
            handleClient(connection)
        #else:             #go accept next connection
            #activeChildren.append(childPid)
            
dispatcher()
    
