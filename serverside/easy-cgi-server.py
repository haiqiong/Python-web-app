#!/usr/bin/python
import http.server
from http.server import HTTPServer, CGIHTTPRequestHandler

def run(server_class=HTTPServer, handler_class=CGIHTTPRequestHandler):
    server_addr=('', 8001)
    httpd=server_class(server_addr, handler_class)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
