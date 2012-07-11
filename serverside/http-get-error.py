from BaseHTTPServer import BaseHTTPRequestHandler

class ErrorHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(404)
        return
    
if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('', 8080), ErrorHandler)
    print 'Starting server'
    server.serve_forever()
    