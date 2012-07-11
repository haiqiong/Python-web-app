#!/usr/local/bin/python

import os, sys
from getpass import getpass        #hidden psw input
from ftplib import FTP

nonpassive = False              #force active mode FTP
filename = 'monkeys.jpg'
dirname = '.'
sitename = 'ftp.rmi.net'
#userinfo = ('lutz', getpass('Pswd?'))   #user () for anonymouse
if len(sys.argv) > 1: filename = sys.argv[1]

print('Connecting...')
connection = FTP(sitename)
#connection.login(*userinfo)         #default is anonymouse
connection.login()                  #user anonymous, psw anonymous
connection.cwd(dirname)             #xfer 1K at a time to localfile
if nonpassive:
    connection.set_pasv(False)
    
print('Downloading...')
localfile = open(filename, 'wb')
#localfile = open(filename, 'rb')
connection.retrbinary('RETR ' + filename, localfile.write, 1024)
#upload a file to server
#connection.storbinary('STOR ' + filename, localfile, 1024)
connection.quit()
localfile.clos()
