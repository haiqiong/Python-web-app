import urllib2

response = urllib2.urlopen('http://blog.doughellmann.com/')
#response = urllib2.urlopen('http://localhost:8080/')
print 'Response:', response
print 'url:', response.geturl()

headers = response.info()
print 'date:', headers['date']
print 'headers:'
print headers

data = response.read()
print 'length:', len(data)
print 'data:'
print data