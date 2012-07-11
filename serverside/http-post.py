from BaseHTTPServer import BaseHTTPRequestHandler
import cgi

class PostHandler(BaseHTTPRequestHandler):
    def do_POST(self):
       #parse the form data
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        #begin the response
        self.send_response(200)
        self.end_headers()
        self.wfile.write('Client: %s\n' % str(self.client_address))
        self.wfile.write('User-agent: %s\n' % str(self.headers['user-agent']))
        self.wfile.write('Path: %s\n' % self.path)
        self.wfile.write('Form data:\n')
        #display the posted data
        for field in form.keys():
            field_item = form[field]
            if field_item.filename:
                #the field contains an upload file
                file_data = field_item.file.read()
                file_len = len(file_data)
                del file_data
                self.wfile.write('\tUpload %s as "%s" (%d bytes)\n' % \
                                 (field, field_item.filename, file_len))
                #form={'path': \path, 'datafile': a.py, 'name':'john'}
            else:
                #regular form value
                self.wfile.write('\t%s=%s\n' % (field, form[field].value))
        return 
    
if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('', 8080), PostHandler)
    print 'Strting server'
    server.serve_forever()