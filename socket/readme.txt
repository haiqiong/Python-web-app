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






