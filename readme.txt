Python web application by Haiqiong Yao
July 9, 2012

1. socket programming
/socket
test on localhost
(1) the server replies prefix, echo, on each line sent by the client.
echo-server.py, echo-client.py
(2) multiple clients at the same time and one server. Some requests denied.
(3) handling multi clients with fork.
fork-echo-server.py 
using the wait to clean dead child processes. Dead processes exist between two requests. 
fork-signal-server.py 
using signal to avoid dead child processes. No dead process appears. Work on my mac(Linux OS).
(4) handling multi clients with thread
thread-server.py
using thread module, more portable and simpler
(5) handling multi clients with socketserver
socketserver.py bug, no data sent back to client
(6) download a file from server to client. option -mode, -file, -host, -port
download-file.py

2. client side of common Internet protocols
/clientside
(1) read a file by ftplib.
get-one-file.py
(2) read a file with urllib.request
get-fiel-urllib.py


3. server side
/serverside
(1) get client and server info with HTTP GET by BaseHTTPServer
http-get.py
(2) post form data to server with HTTP POST by BaseHTTPServer
http-post.py
(3) threading for HTTP GET
http-get-thread.py
(4) download data with urllib.urlretrieve()
urllib-get.py
(5) get full log info of request and response.
webserver-simple2.py, test by http://localhost:8080/hello.html
(6) display the form filled by the user dynamically.
form.html, cgi-bin/print-form.cgi, cgi-bin/print-form2.cgi
(7) content management-wiki
SimpleWiki.py






