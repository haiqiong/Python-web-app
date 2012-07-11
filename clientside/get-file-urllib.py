#!/usr/local/bin/python

import os, getpass
from urllib.request import urlopen, urlretrieve     #works for 3.x, not for 2.7

#filename = 'inputoutput.html'
filename = 'index.html'
#password = getpass.getpass('Pswd?')

remoteaddr = 'http://docs.python.org/tutorial/%s' % (filename)

print('Downloading ', remoteaddr)

#this works too:
#urllib.request.urlretrieve(remoteaddr, filename)

urlretrieve(remoteaddr, filename)

'''
remotefile = urlopen(remoteaddr)        #return a file-like object
localfile = open(filename, 'wb')
localfile.write(remotefile.read())      #get the content by read()
localfile.close()
remotefile.close()
'''
