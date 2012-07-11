#!/usr/bin/python

import os
import cgitb
cgitb.enable()

CGI_ENVIRONMENT_KEYS = [ 'SERVER_SOFTWARE',
        'SERVER_NAME', 'GATEWAY_INTERFACE', 'SERVER_PROTOCOL', 'SERVER_PORT',
        'REQUEST_MEHTOD', 'PATH_INTO', 'SCRIPT_NAME', 'QUERY_STRING'
        'REMOTE_HOST', 'AUTH_TYPE', 'REMOTE_USER', 'REMOTE_IDENT', 
        'CONTENT_TYPE', 'CONTENT_LENGTH']

print('Content-type: text/plain\n')
print('Here are the headers for the request you just made')

for key, value in os.environ.items():
    if key.find('HTTP') == 0 or key in CGI_ENVIRONMENT_KEYS:
        print('%s = %s' %(key,value))
