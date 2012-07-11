#!/usr/bin/python
import http.server
from http.server import BaseHTTPRequestHandler, HTTPServer

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_addr = ('', 8080)
    httpd = server_class(server_addr, handler_class)
    httpd.serve_forever()
    
if __name__ == '__main__':
    run()
