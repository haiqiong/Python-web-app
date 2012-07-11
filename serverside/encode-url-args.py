import urllib
import urllib2

query_args = {'q': 'query string', 'foo': 'bar'}
encoded_args = urllib.urlencode(query_args)
print 'Encoded: ', encoded_args

url = 'http://blog.doughellmann.com/?' + encoded_args
print urllib2.urlopen(url).read()
