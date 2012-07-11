from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import threading

class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        message = threading.currentThread().getName()
        self.wfile.write(message)
        self.wfile.write('\n')
        return
    
#the order of inheritance is important, cannot swap.
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    '''handler requests in a seperate thread'''
    
if __name__ == '__main__':
    server = ThreadedHTTPServer(('', 8080), GetHandler)
    print 'Starting server'
    server.serve_forever()
    