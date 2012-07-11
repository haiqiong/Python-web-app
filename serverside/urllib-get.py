import urllib
import os

def reporthook(block_read, block_size, total_size):
    #when server dosen't return Content-length header, urlretrieve() doesn't
    #know how big the data should be and pass -1 as total_size
    if not block_read:
        print 'Connection opened'
        return
    if total_size < 0:
        print 'Read %d blocks (%d bytes)' % (block_read, \
                                             block_read * block_size)
    else:
        amount_read = block_read * block_size
        print 'Read %d blocks, or %d/%d' % (block_read, amount_read, total_size)
    
try:
    filename, msg = urllib.urlretrieve('http://blog.doughellmann.com/', \
                                       reporthook=reporthook)
    print '\nFile:', filename
    print 'Headers:'
    print msg
    print 'File exists before cleanup:', os.path.exists(filename)
finally:
    urllib.urlcleanup()
    
    print 'File still exists:', os.path.exists(filename)
    