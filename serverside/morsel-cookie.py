import Cookie
import datetime

def show_cookie(c):
    print c
    #morsel contains info on cookie
    for key, morsel in c.iteritems():
        print '\nkey = ', morsel.key
        print 'value = ', morsel.value
        print 'coded_value = ', morsel.coded_value
        for name in morsel.keys():
            if morsel[name]:
                print ' %s = %s' % (name, morsel[name])
                
c = Cookie.SimpleCookie()

#a cookie with a value htat has to be encoded to fit into the header
c['encoded_value_cookie'] = '"cookie_value"' 
c['encoded_value_cookie']['comment'] = 'Value has escaped quotes'

#a cookie that only applies to part of a site
c['restricted_cookie'] = 'cookie_value'
c['restricted_cookie']['path'] = '/sub/path'
c['restricted_cookie']['domain'] = 'PyMOTW'
c['restricted_cookie']['secure'] = True

#a cookie that expired in 5 mins
c['with_max_age'] = 'expires in 5 mins'
c['with_max_age']['max-age'] = 300     #seconds

#a cookie that expires at a specific time
c['expires_at_time'] = 'cookie_value'
time_to_live = datetime.timedelta(hours=1)
expires = datetime.datetime(2012, 7, 9, 23, 28, 12) + time_to_live
expires_at_time = expires.strftime('%a, %d %b %Y %H: %M: %S')
c['expires_at_time']['expires'] = expires_at_time

show_cookie(c)

c1 = Cookie.SimpleCookie()
c1['integer'] = 5
c1['string_with_quote'] = 'He said, "hello, world"'

for name in ['integer', 'string_with_quote']:
    print c1[name].key
    print ' %s', c1[name]
    print ' value=%r' % c1[name].value
    print ' coded_value=%r\n' % c1[name].coded_value

        