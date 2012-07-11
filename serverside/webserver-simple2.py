#!/usr/bin/python
import http.server
from http.server import SimpleHTTPRequestHandler, HTTPServer

port = 8080

class GetHandler(SimpleHTTPRequestHandler):
    #get full HTTP request and response.
    def log_request(self, code='-', size='-'):
        print(self._heading('HTTP Request'))
        #print the resource id and desired operation
        print(self.raw_requestline,)
        for header, value in self.headers.items():
            print(header + ": ", value)

    def do_GET(self, method='GET'):
        #copy all data into a place we can see later.
        self.wfile = FileWrapper(self.wfile)
        #give the actual work of handling the request to SimpleHTTPRequestHandler
        SimpleHTTPRequestHandler.do_GET(self)
        #by this time, the shim file object we created previously is
        #full of the response data and is ready to display.
        print('')
        print(self._heading('HTTP Response'))
        print(self.wfile)

    def _heading(self, s):
        line = '-' * len(s)
        return line + '\n' + s + '\n' + line

class FileWrapper:
    #everything written to the file is appended to a buffer to be used later
    def __init__(self, wfile):
        self.wfile = wfile
        self.contents = []

    def __getattr__(self, key):
        return getattr(self.wfile, key)

    def write(self, s):
        #write a string to real file
        #s is binary bytes
        self.contents.append(str(s))
        self.wfile.write(s)

    def __str__(self):
        #return the output so far as a string
        return ''.join(self.contents)

if __name__ == '__main__':
    httpd = HTTPServer(('', port), GetHandler)
    httpd.serve_forever()
        
