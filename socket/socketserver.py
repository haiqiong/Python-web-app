#!/usr/bin/python
import time, SocketServer

myHost = ''
myPort = 50007

def now():
    return time.ctime(time.time())

class EchoClientHandler(SocketServer.BaseRequestHandler):
    def handler(self):
        print('Server connected by %s at %s' % \
              (self.client_address, now()))
        time.sleep(5)
        while True:
            data = self.request.recv(1024)
            if not data: break
            reply = 'Echo=>%s at %s' % (data, now())
            self.request.send(reply.encode())
        self.request.close()
        
#make a threaded server, listen/handler clients forever
myAdd = (myHost, myPort)
server = SocketServer.ThreadingTCPServer(myAdd, EchoClientHandler)
server.serve_forever()

