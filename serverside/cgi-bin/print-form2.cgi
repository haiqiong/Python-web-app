#!/usr/bin/env python3
import cgi
import cgitb
import os

cgitb.enable()
form = cgi.FieldStorage()

print('Content-type: text/html \n')
print('<html>')
print('<body>')
if form.keys():
    #verb = os.environ['REQEUST_METHOD']
    print('<p>Here are the values your form submission:</p>')
    print('<ul>')
    for field in form.keys():
        valueObj = form[field]
        if isinstance(valueObj, list):
            values = [v.value for v in valueObj]
            if len(values) == 2:
                connector = '" and "'   #"foo" and "bar"
            else:
                connector = '", and "'  #"foo", "bar", and "boo"
            value = '", "'.join(values[:-1]) + connector + values[-1]
        else:
            value = valueObj.value
        print('<li>For <var>%s</var>, I got "%s"</li>' % (field, value))
    print('</ul>')
else:
    print('<p>no form</p>')
print('</body>')
print('</html>')
                                
