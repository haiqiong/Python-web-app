import Cookie

#decode a cookie from a string without header to cookie
http_cookie = ';'.join([
    r'integer=5',
    r'string_with_quote="He said, \"Hello, world\""',
    ])
print 'from constructor:'
c1 = Cookie.SimpleCookie(http_cookie)
print c1

print '\nFrom load():'
c2 = Cookie.SimpleCookie()
c2.load(http_cookie)
print c2
    
#JavaScript output
c3 = Cookie.SimpleCookie()
c3['mycookie'] = 'cookie_value'
c3['another_cookie'] = 'second value'
print c3.js_output()