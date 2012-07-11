#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
textField = form.getfirst('textField')
radioButton = form.getfirst('radioButton')
submitButton = form.getfirst('button')

print('Content-type: text/html \n')
print('<html>')
print('<body>')
print('<p>Here are the values your submitted:</p>')
print('<ul>')
print('<li>In the text field, you enter "%s". </li>' % textField)
print('<li>Of the radio buttons, you select "%s". </li>' % radioButton)
print('<li>the name of the sumit button your pick: "%s".</li>' % submitButton)
print('</ul>')
print('</body>')
print('</html>')
